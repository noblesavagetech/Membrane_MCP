"""
MCP Service — embedded MCP tool registry and handlers.

Each tool handler has the signature:
    (args: dict, session: MCPSession, db: Session) -> dict[str, Any]

Handlers are called by call_mcp_tool() in mcp.py with the active DB session.
"""

from __future__ import annotations

import asyncio
import inspect
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from sqlalchemy.orm import Session


# ---------------------------------------------------------------------------
# MCP Types
# ---------------------------------------------------------------------------

@dataclass
class MCPSession:
    """
    Per-story MCP session context.
    Scopes all tool calls to a specific story so each story has its own
    isolated MCP context.
    """
    story_id: int
    user_id: int
    provider: str = "openrouter"
    model: str = "default"
    system_prompt: str = ""
    _id: str = field(default_factory=lambda: str(uuid.uuid4()))

    @property
    def session_id(self) -> str:
        return self._id


# ---------------------------------------------------------------------------
# Result helpers
# ---------------------------------------------------------------------------

def ok(data: Any) -> dict[str, Any]:
    return {"ok": True, "data": data}


def tool_err(message: str) -> dict[str, Any]:
    return {"ok": False, "error": message}


# ---------------------------------------------------------------------------
# Tool registry
# ---------------------------------------------------------------------------

_TOOL_MAP: dict[str, callable] = {}


def _tool(name: str, description: str, input_schema: dict[str, Any]):
    def decorator(fn: callable) -> callable:
        _TOOL_MAP[name] = fn
        fn._mcp_name = name
        fn._mcp_description = description
        fn._mcp_input_schema = input_schema
        return fn
    return decorator


# ---------------------------------------------------------------------------
# Tool handlers
# ---------------------------------------------------------------------------

# -- Story --

@_tool(name="list_stories", description="List all stories for the current user.",
       input_schema={"type": "object", "properties": {}})
def _list_stories(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from services.story_service import StoryService
    svc = StoryService(db)
    stories = svc.list_stories(session.user_id)
    return ok([{"id": s.id, "title": s.title, "description": s.description} for s in stories])


@_tool(name="get_story",
       description="Get a full story with all chapters, characters, beats, worldbuilding, and key events.",
       input_schema={"type": "object", "required": ["story_id"], "properties": {
           "story_id": {"type": "integer"},
       }})
def _get_story(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from models import Chapter, Character, BeatScene, WorldBuildingElement, KeyEvent
    from services.story_service import StoryService
    svc = StoryService(db)
    story = svc.get_story(session.story_id, session.user_id)
    if not story:
        return tool_err(f"Story {session.story_id} not found")
    chapters = db.query(Chapter).filter(Chapter.story_id == session.story_id).order_by(Chapter.order).all()
    characters = db.query(Character).filter(Character.story_id == session.story_id).all()
    chapter_data = []
    for c in chapters:
        beats = db.query(BeatScene).filter(BeatScene.chapter_id == c.id).order_by(BeatScene.order).all()
        world = db.query(WorldBuildingElement).filter(WorldBuildingElement.chapter_id == c.id).all()
        key_events = db.query(KeyEvent).filter(KeyEvent.chapter_id == c.id).order_by(KeyEvent.order).all()
        chapter_data.append({
            "id": c.id, "title": c.title, "text": c.text, "summary": c.summary, "order": c.order,
            "beats": [{"id": b.id, "description": b.description, "order": b.order} for b in beats],
            "worldbuilding": [{"id": w.id, "category": w.category, "description": w.description} for w in world],
            "key_events": [{"id": k.id, "description": k.description, "order": k.order} for k in key_events],
        })
    return ok({
        "id": story.id, "title": story.title, "description": story.description,
        "created_at": str(story.created_at),
        "chapters": chapter_data,
        "characters": [{"id": c.id, "name": c.name, "role": c.role, "traits": c.traits,
                        "backstory": c.backstory, "description": c.description} for c in characters],
    })


@_tool(name="create_story", description="Create a new story. Auto-creates the first chapter.",
       input_schema={"type": "object", "required": ["title"], "properties": {
           "title": {"type": "string"}, "description": {"type": "string"},
       }})
def _create_story(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from services.story_service import StoryService
    svc = StoryService(db)
    story = svc.create_story(session.user_id, args.get("title", "Untitled Story"), args.get("description", ""))
    return ok({"id": story.id, "title": story.title, "description": story.description})


@_tool(name="update_story", description="Update a story title or description.",
       input_schema={"type": "object", "required": ["story_id"], "properties": {
           "story_id": {"type": "integer"}, "title": {"type": "string"}, "description": {"type": "string"},
       }})
def _update_story(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from services.story_service import StoryService
    kwargs = {k: v for k, v in args.items() if k != "story_id" and v is not None}
    svc = StoryService(db)
    story = svc.update_story(session.story_id, session.user_id, **kwargs)
    if not story:
        return tool_err(f"Story {session.story_id} not found")
    return ok({"id": story.id, "title": story.title, "description": story.description})


@_tool(name="delete_story", description="Delete a story and all its data.",
       input_schema={"type": "object", "required": ["story_id"], "properties": {
           "story_id": {"type": "integer"},
       }})
def _delete_story(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from services.story_service import StoryService
    svc = StoryService(db)
    if not svc.delete_story(session.story_id, session.user_id):
        return tool_err(f"Story {session.story_id} not found")
    return ok({"deleted": session.story_id})


# -- Chapters --

@_tool(name="create_chapter", description="Create a new chapter within a story.",
       input_schema={"type": "object", "required": ["story_id", "title"], "properties": {
           "story_id": {"type": "integer"}, "title": {"type": "string"},
       }})
def _create_chapter(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from services.story_service import StoryService
    _verify_story_access(session, db)
    svc = StoryService(db)
    chapter = svc.create_chapter(session.story_id, session.user_id, args.get("title", "New Chapter"))
    if not chapter:
        return tool_err("Failed to create chapter")
    return ok({"id": chapter.id, "title": chapter.title, "order": chapter.order})


@_tool(name="update_chapter", description="Update a chapter title, text, or summary.",
       input_schema={"type": "object", "required": ["chapter_id"], "properties": {
           "chapter_id": {"type": "integer"}, "title": {"type": "string"},
           "text": {"type": "string"}, "summary": {"type": "string"},
       }})
def _update_chapter(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from services.story_service import StoryService
    _verify_story_access(session, db)
    svc = StoryService(db)
    kwargs = {k: v for k, v in args.items() if k != "chapter_id" and v is not None}
    chapter = svc.update_chapter(args["chapter_id"], session.user_id, **kwargs)
    if not chapter:
        return tool_err(f"Chapter {args['chapter_id']} not found")
    return ok({"id": chapter.id, "title": chapter.title, "summary": chapter.summary})


@_tool(name="summarize_chapter",
       description="AI-summarize a chapter prose. Updates the chapter summary field.",
       input_schema={"type": "object", "required": ["chapter_id"], "properties": {
           "chapter_id": {"type": "integer"}, "model": {"type": "string"},
       }})
def _summarize_chapter(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from services.story_service import StoryService
    _verify_story_access(session, db)
    svc = StoryService(db)
    summary = svc.summarize_chapter(args["chapter_id"], session.story_id, session.user_id)
    return ok({"chapter_id": args["chapter_id"], "summary": summary})


# -- Characters --

@_tool(name="list_characters", description="List all characters in a story.",
       input_schema={"type": "object", "required": ["story_id"], "properties": {
           "story_id": {"type": "integer"},
       }})
def _list_characters(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from services.story_service import StoryService
    _verify_story_access(session, db)
    svc = StoryService(db)
    chars = svc.list_characters(session.story_id, session.user_id)
    return ok([{"id": c.id, "name": c.name, "role": c.role, "traits": c.traits} for c in chars])


@_tool(name="create_character", description="Create a new character in a story.",
       input_schema={"type": "object", "required": ["story_id", "name"], "properties": {
           "story_id": {"type": "integer"}, "name": {"type": "string"},
           "role": {"type": "string"}, "traits": {"type": "string"},
           "backstory": {"type": "string"}, "description": {"type": "string"},
       }})
def _create_character(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from services.story_service import StoryService
    _verify_story_access(session, db)
    svc = StoryService(db)
    char = svc.create_character(
        session.story_id, session.user_id, args["name"],
        role=args.get("role", ""), traits=args.get("traits", ""),
        backstory=args.get("backstory", ""), description=args.get("description", ""),
    )
    if not char:
        return tool_err("Failed to create character")
    return ok({"id": char.id, "name": char.name, "role": char.role})


@_tool(name="update_character", description="Update a character fields.",
       input_schema={"type": "object", "required": ["character_id"], "properties": {
           "character_id": {"type": "integer"}, "name": {"type": "string"},
           "role": {"type": "string"}, "traits": {"type": "string"},
           "backstory": {"type": "string"}, "description": {"type": "string"},
       }})
def _update_character(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from services.story_service import StoryService
    _verify_story_access(session, db)
    svc = StoryService(db)
    kwargs = {k: v for k, v in args.items() if k != "character_id" and v is not None}
    char = svc.update_character(args["character_id"], session.story_id, session.user_id, **kwargs)
    if not char:
        return tool_err(f"Character {args['character_id']} not found")
    return ok({"id": char.id, "name": char.name})


@_tool(name="delete_character", description="Delete a character from a story.",
       input_schema={"type": "object", "required": ["character_id"], "properties": {
           "character_id": {"type": "integer"},
       }})
def _delete_character(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from services.story_service import StoryService
    _verify_story_access(session, db)
    svc = StoryService(db)
    if not svc.delete_character(args["character_id"], session.story_id, session.user_id):
        return tool_err(f"Character {args['character_id']} not found")
    return ok({"deleted": args["character_id"]})


# -- Beats --

@_tool(name="create_beat", description="Create a new story beat/scene within a chapter.",
       input_schema={"type": "object", "required": ["chapter_id", "description"], "properties": {
           "chapter_id": {"type": "integer"}, "description": {"type": "string"},
           "order": {"type": "integer"},
       }})
def _create_beat(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from services.story_service import StoryService
    _verify_story_access(session, db)
    svc = StoryService(db)
    beat = svc.create_beat(args["chapter_id"], args["description"], args.get("order", 0))
    return ok({"id": beat.id, "chapter_id": beat.chapter_id, "description": beat.description, "order": beat.order})


@_tool(name="get_beats", description="Get all beats for a chapter.",
       input_schema={"type": "object", "required": ["chapter_id"], "properties": {
           "chapter_id": {"type": "integer"},
       }})
def _get_beats(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from services.story_service import StoryService
    _verify_story_access(session, db)
    svc = StoryService(db)
    beats = svc.get_beats(args["chapter_id"])
    return ok([{"id": b.id, "description": b.description, "order": b.order} for b in beats])


@_tool(name="update_beat", description="Update a beat description or order.",
       input_schema={"type": "object", "required": ["beat_id"], "properties": {
           "beat_id": {"type": "integer"}, "description": {"type": "string"}, "order": {"type": "integer"},
       }})
def _update_beat(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from services.story_service import StoryService
    _verify_story_access(session, db)
    svc = StoryService(db)
    kwargs = {k: v for k, v in args.items() if k != "beat_id" and v is not None}
    beat = svc.update_beat(args["beat_id"], **kwargs)
    if not beat:
        return tool_err(f"Beat {args['beat_id']} not found")
    return ok({"id": beat.id, "description": beat.description, "order": beat.order})


@_tool(name="delete_beat", description="Delete a beat from a chapter.",
       input_schema={"type": "object", "required": ["beat_id"], "properties": {
           "beat_id": {"type": "integer"},
       }})
def _delete_beat(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from services.story_service import StoryService
    _verify_story_access(session, db)
    svc = StoryService(db)
    if not svc.delete_beat(args["beat_id"]):
        return tool_err(f"Beat {args['beat_id']} not found")
    return ok({"deleted": args["beat_id"]})


# -- Worldbuilding --

@_tool(name="create_world_element", description="Create a worldbuilding element within a chapter.",
       input_schema={"type": "object", "required": ["chapter_id", "category", "description"], "properties": {
           "chapter_id": {"type": "integer"}, "category": {"type": "string"},
           "description": {"type": "string"},
       }})
def _create_world_element(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from services.story_service import StoryService
    _verify_story_access(session, db)
    svc = StoryService(db)
    elem = svc.create_world_element(args["chapter_id"], args["category"], args["description"])
    return ok({"id": elem.id, "category": elem.category, "description": elem.description})


@_tool(name="get_world_elements", description="Get all worldbuilding elements for a chapter.",
       input_schema={"type": "object", "required": ["chapter_id"], "properties": {
           "chapter_id": {"type": "integer"},
       }})
def _get_world_elements(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from services.story_service import StoryService
    _verify_story_access(session, db)
    svc = StoryService(db)
    elems = svc.get_world_elements(args["chapter_id"])
    return ok([{"id": e.id, "category": e.category, "description": e.description} for e in elems])


# -- Key Events --

@_tool(name="create_key_event", description="Create a key event within a chapter.",
       input_schema={"type": "object", "required": ["chapter_id", "description"], "properties": {
           "chapter_id": {"type": "integer"}, "description": {"type": "string"},
           "order": {"type": "integer"},
       }})
def _create_key_event(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from services.story_service import StoryService
    _verify_story_access(session, db)
    svc = StoryService(db)
    event = svc.create_key_event(args["chapter_id"], args["description"], args.get("order", 0))
    return ok({"id": event.id, "description": event.description, "order": event.order})


@_tool(name="get_key_events", description="Get all key events for a chapter.",
       input_schema={"type": "object", "required": ["chapter_id"], "properties": {
           "chapter_id": {"type": "integer"},
       }})
def _get_key_events(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from services.story_service import StoryService
    _verify_story_access(session, db)
    svc = StoryService(db)
    events = svc.get_key_events(args["chapter_id"])
    return ok([{"id": k.id, "description": k.description, "order": k.order} for k in events])


# -- Memory (RAG) --

@_tool(name="add_memory", description="Add a text memory to the vector store for a project.",
       input_schema={"type": "object", "required": ["project_id", "content"], "properties": {
           "project_id": {"type": "integer"}, "content": {"type": "string"},
           "metadata": {"type": "object"},
       }})
def _add_memory(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from services.vector_service import VectorService
    svc = VectorService(db)
    result = svc.add_memory(args["project_id"], args["content"], args.get("metadata"))
    return ok({"embedding_id": result})


@_tool(name="search_memory", description="Semantic search across project memories.",
       input_schema={"type": "object", "required": ["project_id", "query"], "properties": {
           "project_id": {"type": "integer"}, "query": {"type": "string"},
           "top_k": {"type": "integer", "default": 5},
       }})
def _search_memory(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from services.vector_service import VectorService
    svc = VectorService(db)
    results = svc.search_memory(args["project_id"], args["query"], args.get("top_k", 5))
    return ok(results)


# -- AI Generation --

@_tool(name="generate_character",
       description="AI-generate a character profile for the story.",
       input_schema={"type": "object", "required": ["story_id", "generation_type"], "properties": {
           "story_id": {"type": "integer"},
           "generation_type": {"type": "string", "enum": ["protagonist", "antagonist", "supporting", "minor"]},
           "parameters": {"type": "object"},
           "use_context": {"type": "boolean", "default": True},
           "model": {"type": "string"},
       }})
async def _generate_character(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from services.story_service import StoryService
    _verify_story_access(session, db)
    svc = StoryService(db)
    story = svc.get_story(session.story_id, session.user_id)
    result = await svc.generate_character_profile(
        story, args.get("generation_type", "supporting"),
        args.get("parameters") or {}, args.get("use_context", True), args.get("model"),
    )
    return ok(result)


@_tool(name="generate_worldbuilding",
       description="AI-generate a worldbuilding element for a chapter.",
       input_schema={"type": "object", "required": ["story_id", "chapter_id", "generation_type"], "properties": {
           "story_id": {"type": "integer"}, "chapter_id": {"type": "integer"},
           "generation_type": {"type": "string",
                               "enum": ["location", "culture", "magic_system", "technology", "history", "creature"]},
           "parameters": {"type": "object"},
           "use_context": {"type": "boolean", "default": True},
           "model": {"type": "string"},
       }})
async def _generate_worldbuilding(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from models import Chapter
    from services.story_service import StoryService
    _verify_story_access(session, db)
    svc = StoryService(db)
    story = svc.get_story(session.story_id, session.user_id)
    chapter = db.query(Chapter).filter(Chapter.id == args["chapter_id"], Chapter.story_id == session.story_id).first()
    if not chapter:
        return tool_err(f"Chapter {args['chapter_id']} not found")
    result = await svc.generate_worldbuilding_element(
        story=story,
        chapter=chapter,
        generation_type=args.get("generation_type", "location"),
        parameters=args.get("parameters") or {},
        use_context=args.get("use_context", True),
        model=args.get("model"),
    )
    return ok(result)


@_tool(name="generate_prose",
       description="AI-generate narrative prose for a chapter from its beats and context.",
       input_schema={"type": "object", "required": ["chapter_id", "prompt"], "properties": {
           "chapter_id": {"type": "integer"}, "prompt": {"type": "string"},
           "context_type": {"type": "string",
                            "enum": ["beats_only", "beats_and_characters", "full"],
                            "default": "full"},
           "model": {"type": "string"},
       }})
async def _generate_prose(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from models import Chapter
    from services.story_service import StoryService
    _verify_story_access(session, db)
    svc = StoryService(db)
    story = svc.get_story(session.story_id, session.user_id)
    chapter = db.query(Chapter).filter(Chapter.id == args["chapter_id"], Chapter.story_id == session.story_id).first()
    if not chapter:
        return tool_err(f"Chapter {args['chapter_id']} not found")
    result = await svc.generate_prose(
        chapter=chapter,
        story=story,
        characters=list(story.characters) if story.characters else [],
        beats=list(chapter.beats) if chapter.beats else [],
        key_events=list(story.key_events) if story.key_events else [],
        world_elements=list(chapter.world_elements) if chapter.world_elements else [],
        prompt=args.get("prompt", ""),
        model=args.get("model"),
    )
    return ok(result)


@_tool(name="query_context",
       description="RAG-style context query — compiles relevant story context for a question.",
       input_schema={"type": "object", "required": ["story_id", "query"], "properties": {
           "story_id": {"type": "integer"}, "query": {"type": "string"},
           "top_k": {"type": "integer", "default": 5},
           "model": {"type": "string"},
       }})
async def _query_context(args: dict, session: MCPSession, db: Session) -> dict[str, Any]:
    from services.story_service import StoryService
    _verify_story_access(session, db)
    svc = StoryService(db)
    result = await svc.query_context(
        story_id=session.story_id,
        user_id=session.user_id,
        prompt=args.get("query", ""),
        chapter_id=args.get("chapter_id"),
        model=args.get("model"),
    )
    return ok(result)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _verify_story_access(session: MCPSession, db: Session) -> None:
    from models import Story
    story = db.query(Story).filter(
        Story.id == session.story_id, Story.user_id == session.user_id
    ).first()
    if not story:
        raise PermissionError(f"Story {session.story_id} not found or access denied")


# ---------------------------------------------------------------------------
# Public API (called by mcp.py)
# ---------------------------------------------------------------------------

async def call_mcp_tool(tool_name: str, args: dict[str, Any], session: MCPSession, db: Session) -> dict[str, Any]:
    handler = _TOOL_MAP.get(tool_name)
    if not handler:
        return tool_err(f"Unknown tool: {tool_name}")
    try:
        result = handler(args, session, db)
        if inspect.isawaitable(result):
            result = await result
        return result
    except PermissionError as e:
        return tool_err(str(e))
    except Exception as e:
        return tool_err(f"Tool error: {e}")


def get_mcp_tools() -> list[dict[str, Any]]:
    return [
        {"name": fn._mcp_name, "description": fn._mcp_description, "inputSchema": fn._mcp_input_schema}
        for fn in _TOOL_MAP.values()
    ]


def get_mcp_resources() -> list[dict[str, Any]]:
    return [
        {"uriPattern": "story://{story_id}", "name": "Story",
         "description": "Full story with chapters, characters, beats, worldbuilding.",
         "mimeType": "application/json"},
        {"uriPattern": "chapter://{chapter_id}", "name": "Chapter",
         "description": "Chapter with text, summary, beats, worldbuilding, key events.",
         "mimeType": "application/json"},
        {"uriPattern": "character://{character_id}", "name": "Character",
         "description": "Character profile.",
         "mimeType": "application/json"},
        {"uriPattern": "beat://{beat_id}", "name": "Beat",
         "description": "Single story beat/scene.",
         "mimeType": "application/json"},
        {"uriPattern": "worldelement://{worldelement_id}", "name": "Worldbuilding Element",
         "description": "Worldbuilding element.",
         "mimeType": "application/json"},
        {"uriPattern": "keyevent://{keyevent_id}", "name": "Key Event",
         "description": "Key event/outline point.",
         "mimeType": "application/json"},
    ]
