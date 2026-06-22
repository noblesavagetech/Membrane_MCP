"""
MCP Tools — domain-specific functions exposed to MCP clients.

Each tool has:
  name        — unique identifier
  description — plain English description for the LLM
  inputSchema — JSON Schema for the tool's arguments
  handler     — async function(args: dict, host: HostContext) -> Any

Reference: https://modelcontextprotocol.io/docs/specification/basic/tools
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Callable

# Ensure backend services are importable
_BACKEND_ROOT = Path(__file__).parent.parent.parent / "backend"
sys.path.insert(0, str(_BACKEND_ROOT))

from host_context import HostContext

# ---- Tool result helpers ----

ToolHandler = Callable[[dict[str, Any], HostContext], Any]


def ok(data: dict[str, Any]) -> dict[str, Any]:
    return {"ok": True, "data": data}


def err(message: str) -> dict[str, Any]:
    return {"ok": False, "error": message}


# ---- Story CRUD tools ----

STORY_TOOLS: list[dict[str, Any]] = [
    # --- Stories ---
    {
        "name": "list_stories",
        "description": (
            "List all stories for the current user. "
            "Returns a list of story objects with id, title, and description."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {},
        },
        "handler": _list_stories,
    },
    {
        "name": "get_story",
        "description": (
            "Get a full story with all chapters, characters, beats, worldbuilding, and key events. "
            "Use this to load the complete state of a story before making edits or generating content."
        ),
        "inputSchema": {
            "type": "object",
            "required": ["story_id"],
            "properties": {
                "story_id": {"type": "integer", "description": "The story's database ID."},
            },
        },
        "handler": _get_story,
    },
    {
        "name": "create_story",
        "description": "Create a new story. Returns the created story object.",
        "inputSchema": {
            "type": "object",
            "required": ["title"],
            "properties": {
                "title": {"type": "string", "description": "Story title."},
                "description": {"type": "string", "description": "Short story description."},
            },
        },
        "handler": _create_story,
    },
    {
        "name": "update_story",
        "description": "Update a story's title or description.",
        "inputSchema": {
            "type": "object",
            "required": ["story_id"],
            "properties": {
                "story_id": {"type": "integer"},
                "title": {"type": "string"},
                "description": {"type": "string"},
            },
        },
        "handler": _update_story,
    },
    {
        "name": "delete_story",
        "description": "Delete a story and all its chapters, characters, beats, etc.",
        "inputSchema": {
            "type": "object",
            "required": ["story_id"],
            "properties": {
                "story_id": {"type": "integer"},
            },
        },
        "handler": _delete_story,
    },
    # --- Chapters ---
    {
        "name": "create_chapter",
        "description": "Create a new chapter within a story.",
        "inputSchema": {
            "type": "object",
            "required": ["story_id", "title"],
            "properties": {
                "story_id": {"type": "integer"},
                "title": {"type": "string"},
            },
        },
        "handler": _create_chapter,
    },
    {
        "name": "update_chapter",
        "description": "Update a chapter's title, text, or summary.",
        "inputSchema": {
            "type": "object",
            "required": ["chapter_id"],
            "properties": {
                "chapter_id": {"type": "integer"},
                "title": {"type": "string"},
                "text": {"type": "string"},
                "summary": {"type": "string"},
            },
        },
        "handler": _update_chapter,
    },
    {
        "name": "summarize_chapter",
        "description": "AI-summarize a chapter's prose. Updates the chapter's summary field.",
        "inputSchema": {
            "type": "object",
            "required": ["chapter_id"],
            "properties": {
                "chapter_id": {"type": "integer"},
                "model": {"type": "string", "description": "OpenRouter model ID (optional)."},
            },
        },
        "handler": _summarize_chapter,
    },
    # --- Characters ---
    {
        "name": "list_characters",
        "description": "List all characters in a story.",
        "inputSchema": {
            "type": "object",
            "required": ["story_id"],
            "properties": {
                "story_id": {"type": "integer"},
            },
        },
        "handler": _list_characters,
    },
    {
        "name": "create_character",
        "description": "Create a new character in a story.",
        "inputSchema": {
            "type": "object",
            "required": ["story_id", "name"],
            "properties": {
                "story_id": {"type": "integer"},
                "name": {"type": "string"},
                "role": {"type": "string", "description": "e.g. protagonist, antagonist, supporting."},
                "traits": {"type": "string", "description": "Personality traits."},
                "backstory": {"type": "string"},
                "description": {"type": "string"},
            },
        },
        "handler": _create_character,
    },
    {
        "name": "update_character",
        "description": "Update a character's fields.",
        "inputSchema": {
            "type": "object",
            "required": ["character_id"],
            "properties": {
                "character_id": {"type": "integer"},
                "name": {"type": "string"},
                "role": {"type": "string"},
                "traits": {"type": "string"},
                "backstory": {"type": "string"},
                "description": {"type": "string"},
            },
        },
        "handler": _update_character,
    },
    {
        "name": "delete_character",
        "description": "Delete a character from a story.",
        "inputSchema": {
            "type": "object",
            "required": ["character_id"],
            "properties": {
                "character_id": {"type": "integer"},
            },
        },
        "handler": _delete_character,
    },
    # --- Beats ---
    {
        "name": "create_beat",
        "description": "Create a new story beat/scene within a chapter.",
        "inputSchema": {
            "type": "object",
            "required": ["chapter_id", "description"],
            "properties": {
                "chapter_id": {"type": "integer"},
                "description": {"type": "string"},
                "order": {"type": "integer", "description": "Optional sort order."},
            },
        },
        "handler": _create_beat,
    },
    {
        "name": "get_beats",
        "description": "Get all beats for a chapter.",
        "inputSchema": {
            "type": "object",
            "required": ["chapter_id"],
            "properties": {
                "chapter_id": {"type": "integer"},
            },
        },
        "handler": _get_beats,
    },
    {
        "name": "update_beat",
        "description": "Update a beat's description or order.",
        "inputSchema": {
            "type": "object",
            "required": ["beat_id"],
            "properties": {
                "beat_id": {"type": "integer"},
                "description": {"type": "string"},
                "order": {"type": "integer"},
            },
        },
        "handler": _update_beat,
    },
    {
        "name": "delete_beat",
        "description": "Delete a beat from a chapter.",
        "inputSchema": {
            "type": "object",
            "required": ["beat_id"],
            "properties": {
                "beat_id": {"type": "integer"},
            },
        },
        "handler": _delete_beat,
    },
    # --- Worldbuilding ---
    {
        "name": "create_world_element",
        "description": "Create a worldbuilding element within a chapter.",
        "inputSchema": {
            "type": "object",
            "required": ["chapter_id", "category", "description"],
            "properties": {
                "chapter_id": {"type": "integer"},
                "category": {"type": "string", "description": "e.g. location, culture, magic_system."},
                "description": {"type": "string"},
            },
        },
        "handler": _create_world_element,
    },
    {
        "name": "get_world_elements",
        "description": "Get all worldbuilding elements for a chapter.",
        "inputSchema": {
            "type": "object",
            "required": ["chapter_id"],
            "properties": {
                "chapter_id": {"type": "integer"},
            },
        },
        "handler": _get_world_elements,
    },
    # --- Key Events ---
    {
        "name": "create_key_event",
        "description": "Create a key event within a chapter.",
        "inputSchema": {
            "type": "object",
            "required": ["chapter_id", "description"],
            "properties": {
                "chapter_id": {"type": "integer"},
                "description": {"type": "string"},
                "order": {"type": "integer"},
            },
        },
        "handler": _create_key_event,
    },
    {
        "name": "get_key_events",
        "description": "Get all key events for a chapter.",
        "inputSchema": {
            "type": "object",
            "required": ["chapter_id"],
            "properties": {
                "chapter_id": {"type": "integer"},
            },
        },
        "handler": _get_key_events,
    },
    # --- Vector Memory ---
    {
        "name": "add_memory",
        "description": "Add a text memory to the vector store for a project. Enables RAG-style retrieval.",
        "inputSchema": {
            "type": "object",
            "required": ["project_id", "content"],
            "properties": {
                "project_id": {"type": "integer"},
                "content": {"type": "string"},
                "metadata": {"type": "object", "description": "Optional extra metadata."},
            },
        },
        "handler": _add_memory,
    },
    {
        "name": "search_memory",
        "description": "Search the vector memory for a project using semantic similarity.",
        "inputSchema": {
            "type": "object",
            "required": ["project_id", "query"],
            "properties": {
                "project_id": {"type": "integer"},
                "query": {"type": "string"},
                "top_k": {"type": "integer", "default": 5, "description": "Number of results."},
            },
        },
        "handler": _search_memory,
    },
]


# ---- Generation / AI tools ----

GENERATION_TOOLS: list[dict[str, Any]] = [
    {
        "name": "generate_character",
        "description": (
            "AI-generate a character profile. "
            "The LLM will produce a name, role, traits, backstory, and physical description. "
            "Set use_context=true to incorporate existing story context."
        ),
        "inputSchema": {
            "type": "object",
            "required": ["story_id", "generation_type"],
            "properties": {
                "story_id": {"type": "integer"},
                "generation_type": {
                    "type": "string",
                    "enum": ["protagonist", "antagonist", "supporting", "minor"],
                    "description": "Character role archetype.",
                },
                "parameters": {
                    "type": "object",
                    "description": "Optional overrides: name_hint, age_range, gender_hint, additional_notes.",
                },
                "use_context": {"type": "boolean", "default": True},
                "model": {"type": "string", "description": "OpenRouter model ID (optional)."},
            },
        },
        "handler": _generate_character,
    },
    {
        "name": "generate_worldbuilding",
        "description": (
            "AI-generate a worldbuilding element for a chapter. "
            "Set use_context=true to incorporate existing story and chapter context."
        ),
        "inputSchema": {
            "type": "object",
            "required": ["story_id", "chapter_id", "generation_type"],
            "properties": {
                "story_id": {"type": "integer"},
                "chapter_id": {"type": "integer"},
                "generation_type": {
                    "type": "string",
                    "enum": ["location", "culture", "magic_system", "technology", "history", "creature"],
                    "description": "Worldbuilding category.",
                },
                "parameters": {"type": "object", "description": "Optional generation parameters."},
                "use_context": {"type": "boolean", "default": True},
                "model": {"type": "string"},
            },
        },
        "handler": _generate_worldbuilding,
    },
    {
        "name": "generate_prose",
        "description": (
            "AI-generate narrative prose for a chapter from its beats and context. "
            "This is the core creative generation tool — it takes the current chapter's "
            "beats, character states, and worldbuilding and produces actual written prose."
        ),
        "inputSchema": {
            "type": "object",
            "required": ["chapter_id", "prompt"],
            "properties": {
                "chapter_id": {"type": "integer"},
                "prompt": {"type": "string", "description": "Specific instructions for this passage."},
                "context_type": {
                    "type": "string",
                    "enum": ["beats_only", "beats_and_characters", "full"],
                    "default": "full",
                    "description": "How much context to include.",
                },
                "model": {"type": "string"},
            },
        },
        "handler": _generate_prose,
    },
    {
        "name": "query_context",
        "description": (
            "RAG-style context query — search the story database and compile relevant context "
            "for a question. Returns a clean 'context package' that can be injected into a prompt."
        ),
        "inputSchema": {
            "type": "object",
            "required": ["story_id", "query"],
            "properties": {
                "story_id": {"type": "integer"},
                "query": {"type": "string", "description": "What you want to find out about the story."},
                "top_k": {"type": "integer", "default": 5},
                "model": {"type": "string"},
            },
        },
        "handler": _query_context,
    },
]


# -----------------------------------------------------------------------
# Tool handlers
# -----------------------------------------------------------------------

async def _list_stories(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from models import Story
    session = host.get_db_session()
    try:
        stories = session.query(Story).order_by(Story.created_at.desc()).all()
        return ok([
            {"id": s.id, "title": s.title, "description": s.description, "created_at": str(s.created_at)}
            for s in stories
        ])
    finally:
        session.close()


async def _get_story(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from models import Story, Chapter, Character, BeatScene, WorldBuildingElement, KeyEvent
    session = host.get_db_session()
    try:
        story_id = int(args["story_id"])
        story = session.query(Story).filter(Story.id == story_id).first()
        if not story:
            return err(f"Story {story_id} not found")

        chapters = (
            session.query(Chapter)
            .filter(Chapter.story_id == story_id)
            .order_by(Chapter.order)
            .all()
        )
        characters = session.query(Character).filter(Character.story_id == story_id).all()

        chapter_data = []
        for c in chapters:
            beats = session.query(BeatScene).filter(BeatScene.chapter_id == c.id).order_by(BeatScene.order).all()
            world = session.query(WorldBuildingElement).filter(WorldBuildingElement.chapter_id == c.id).all()
            key_events = session.query(KeyEvent).filter(KeyEvent.chapter_id == c.id).order_by(KeyEvent.order).all()
            chapter_data.append({
                "id": c.id,
                "title": c.title,
                "text": c.text,
                "summary": c.summary,
                "order": c.order,
                "beats": [{"id": b.id, "description": b.description, "order": b.order} for b in beats],
                "worldbuilding": [{"id": w.id, "category": w.category, "description": w.description} for w in world],
                "key_events": [{"id": k.id, "description": k.description, "order": k.order} for k in key_events],
            })

        return ok({
            "id": story.id,
            "title": story.title,
            "description": story.description,
            "created_at": str(story.created_at),
            "updated_at": str(story.updated_at) if story.updated_at else None,
            "chapters": chapter_data,
            "characters": [
                {"id": c.id, "name": c.name, "role": c.role, "traits": c.traits,
                 "backstory": c.backstory, "description": c.description}
                for c in characters
            ],
        })
    finally:
        session.close()


async def _create_story(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from models import Story, Chapter
    from datetime import datetime
    session = host.get_db_session()
    try:
        title = args.get("title", "Untitled Story")
        description = args.get("description", "")
        story = Story(title=title, description=description, created_at=datetime.utcnow())
        session.add(story)
        session.flush()

        # Auto-create first chapter
        chapter = Chapter(story_id=story.id, title="Chapter 1", order=0, created_at=datetime.utcnow())
        session.add(chapter)
        session.commit()
        return ok({"id": story.id, "title": story.title, "description": story.description})
    except Exception as e:
        session.rollback()
        return err(str(e))
    finally:
        session.close()


async def _update_story(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from models import Story
    from datetime import datetime
    session = host.get_db_session()
    try:
        story_id = int(args["story_id"])
        story = session.query(Story).filter(Story.id == story_id).first()
        if not story:
            return err(f"Story {story_id} not found")
        if "title" in args:
            story.title = args["title"]
        if "description" in args:
            story.description = args["description"]
        story.updated_at = datetime.utcnow()
        session.commit()
        return ok({"id": story.id, "title": story.title, "description": story.description})
    except Exception as e:
        session.rollback()
        return err(str(e))
    finally:
        session.close()


async def _delete_story(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from models import Story, Chapter, Character
    session = host.get_db_session()
    try:
        story_id = int(args["story_id"])
        story = session.query(Story).filter(Story.id == story_id).first()
        if not story:
            return err(f"Story {story_id} not found")
        session.query(Character).filter(Character.story_id == story_id).delete()
        session.query(Chapter).filter(Chapter.story_id == story_id).delete()
        session.delete(story)
        session.commit()
        return ok({"deleted": story_id})
    except Exception as e:
        session.rollback()
        return err(str(e))
    finally:
        session.close()


async def _create_chapter(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from models import Chapter
    from datetime import datetime
    session = host.get_db_session()
    try:
        story_id = int(args["story_id"])
        title = args.get("title", "New Chapter")
        # Determine order
        max_order = session.query(Chapter.order).filter(Chapter.story_id == story_id).order_by(Chapter.order.desc()).first()
        order = (max_order[0] + 1) if max_order else 0
        chapter = Chapter(story_id=story_id, title=title, order=order, created_at=datetime.utcnow())
        session.add(chapter)
        session.commit()
        return ok({"id": chapter.id, "story_id": story_id, "title": chapter.title, "order": chapter.order})
    except Exception as e:
        session.rollback()
        return err(str(e))
    finally:
        session.close()


async def _update_chapter(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from models import Chapter
    from datetime import datetime
    session = host.get_db_session()
    try:
        chapter_id = int(args["chapter_id"])
        chapter = session.query(Chapter).filter(Chapter.id == chapter_id).first()
        if not chapter:
            return err(f"Chapter {chapter_id} not found")
        for field in ("title", "text", "summary"):
            if field in args:
                setattr(chapter, field, args[field])
        chapter.updated_at = datetime.utcnow()
        session.commit()
        return ok({"id": chapter.id, "title": chapter.title, "summary": chapter.summary})
    except Exception as e:
        session.rollback()
        return err(str(e))
    finally:
        session.close()


async def _summarize_chapter(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from services.story_service import StoryService
    session = host.get_db_session()
    try:
        chapter_id = int(args["chapter_id"])
        model = args.get("model") or None
        svc = StoryService(session)
        summary = svc.summarize_chapter(chapter_id, model)
        return ok({"chapter_id": chapter_id, "summary": summary})
    except Exception as e:
        return err(str(e))
    finally:
        session.close()


async def _list_characters(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from models import Character
    session = host.get_db_session()
    try:
        story_id = int(args["story_id"])
        characters = session.query(Character).filter(Character.story_id == story_id).all()
        return ok([{"id": c.id, "name": c.name, "role": c.role, "traits": c.traits} for c in characters])
    finally:
        session.close()


async def _create_character(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from models import Character
    from datetime import datetime
    session = host.get_db_session()
    try:
        story_id = int(args["story_id"])
        character = Character(
            story_id=story_id,
            name=args["name"],
            role=args.get("role", ""),
            traits=args.get("traits", ""),
            backstory=args.get("backstory", ""),
            description=args.get("description", ""),
            created_at=datetime.utcnow(),
        )
        session.add(character)
        session.commit()
        return ok({"id": character.id, "name": character.name, "role": character.role})
    except Exception as e:
        session.rollback()
        return err(str(e))
    finally:
        session.close()


async def _update_character(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from models import Character
    session = host.get_db_session()
    try:
        char_id = int(args["character_id"])
        character = session.query(Character).filter(Character.id == char_id).first()
        if not character:
            return err(f"Character {char_id} not found")
        for field in ("name", "role", "traits", "backstory", "description"):
            if field in args:
                setattr(character, field, args[field])
        session.commit()
        return ok({"id": character.id, "name": character.name})
    except Exception as e:
        session.rollback()
        return err(str(e))
    finally:
        session.close()


async def _delete_character(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from models import Character
    session = host.get_db_session()
    try:
        char_id = int(args["character_id"])
        character = session.query(Character).filter(Character.id == char_id).first()
        if not character:
            return err(f"Character {char_id} not found")
        session.delete(character)
        session.commit()
        return ok({"deleted": char_id})
    except Exception as e:
        session.rollback()
        return err(str(e))
    finally:
        session.close()


async def _create_beat(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from models import BeatScene
    from datetime import datetime
    session = host.get_db_session()
    try:
        chapter_id = int(args["chapter_id"])
        max_order = session.query(BeatScene.order).filter(BeatScene.chapter_id == chapter_id).order_by(BeatScene.order.desc()).first()
        order = args.get("order") or ((max_order[0] + 1) if max_order else 0)
        beat = BeatScene(chapter_id=chapter_id, description=args["description"], order=order, created_at=datetime.utcnow())
        session.add(beat)
        session.commit()
        return ok({"id": beat.id, "chapter_id": chapter_id, "description": beat.description, "order": beat.order})
    except Exception as e:
        session.rollback()
        return err(str(e))
    finally:
        session.close()


async def _get_beats(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from models import BeatScene
    session = host.get_db_session()
    try:
        chapter_id = int(args["chapter_id"])
        beats = session.query(BeatScene).filter(BeatScene.chapter_id == chapter_id).order_by(BeatScene.order).all()
        return ok([{"id": b.id, "description": b.description, "order": b.order} for b in beats])
    finally:
        session.close()


async def _update_beat(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from models import BeatScene
    session = host.get_db_session()
    try:
        beat_id = int(args["beat_id"])
        beat = session.query(BeatScene).filter(BeatScene.id == beat_id).first()
        if not beat:
            return err(f"Beat {beat_id} not found")
        if "description" in args:
            beat.description = args["description"]
        if "order" in args:
            beat.order = args["order"]
        session.commit()
        return ok({"id": beat.id, "description": beat.description, "order": beat.order})
    except Exception as e:
        session.rollback()
        return err(str(e))
    finally:
        session.close()


async def _delete_beat(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from models import BeatScene
    session = host.get_db_session()
    try:
        beat_id = int(args["beat_id"])
        beat = session.query(BeatScene).filter(BeatScene.id == beat_id).first()
        if not beat:
            return err(f"Beat {beat_id} not found")
        session.delete(beat)
        session.commit()
        return ok({"deleted": beat_id})
    except Exception as e:
        session.rollback()
        return err(str(e))
    finally:
        session.close()


async def _create_world_element(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from models import WorldBuildingElement
    from datetime import datetime
    session = host.get_db_session()
    try:
        chapter_id = int(args["chapter_id"])
        elem = WorldBuildingElement(
            chapter_id=chapter_id,
            category=args["category"],
            description=args["description"],
            created_at=datetime.utcnow(),
        )
        session.add(elem)
        session.commit()
        return ok({"id": elem.id, "category": elem.category, "description": elem.description})
    except Exception as e:
        session.rollback()
        return err(str(e))
    finally:
        session.close()


async def _get_world_elements(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from models import WorldBuildingElement
    session = host.get_db_session()
    try:
        chapter_id = int(args["chapter_id"])
        elems = session.query(WorldBuildingElement).filter(WorldBuildingElement.chapter_id == chapter_id).all()
        return ok([{"id": e.id, "category": e.category, "description": e.description} for e in elems])
    finally:
        session.close()


async def _create_key_event(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from models import KeyEvent
    from datetime import datetime
    session = host.get_db_session()
    try:
        chapter_id = int(args["chapter_id"])
        max_order = session.query(KeyEvent.order).filter(KeyEvent.chapter_id == chapter_id).order_by(KeyEvent.order.desc()).first()
        order = args.get("order") or ((max_order[0] + 1) if max_order else 0)
        event = KeyEvent(chapter_id=chapter_id, description=args["description"], order=order, created_at=datetime.utcnow())
        session.add(event)
        session.commit()
        return ok({"id": event.id, "description": event.description, "order": event.order})
    except Exception as e:
        session.rollback()
        return err(str(e))
    finally:
        session.close()


async def _get_key_events(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from models import KeyEvent
    session = host.get_db_session()
    try:
        chapter_id = int(args["chapter_id"])
        events = session.query(KeyEvent).filter(KeyEvent.chapter_id == chapter_id).order_by(KeyEvent.order).all()
        return ok([{"id": k.id, "description": k.description, "order": k.order} for k in events])
    finally:
        session.close()


async def _add_memory(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from services.vector_service import VectorService
    session = host.get_db_session()
    try:
        project_id = int(args["project_id"])
        content = args["content"]
        metadata = args.get("metadata") or {}
        svc = VectorService(session)
        result = svc.add_memory(project_id, content, metadata)
        return ok({"embedding_id": result})
    except Exception as e:
        return err(str(e))
    finally:
        session.close()


async def _search_memory(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from services.vector_service import VectorService
    session = host.get_db_session()
    try:
        project_id = int(args["project_id"])
        query = args["query"]
        top_k = args.get("top_k", 5)
        svc = VectorService(session)
        results = svc.search_memory(project_id, query, top_k)
        return ok(results)
    except Exception as e:
        return err(str(e))
    finally:
        session.close()


# ---- Generation handlers ----

async def _generate_character(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from services.story_service import StoryService
    session = host.get_db_session()
    try:
        story_id = int(args["story_id"])
        generation_type = args.get("generation_type", "supporting")
        parameters = args.get("parameters") or {}
        use_context = args.get("use_context", True)
        model = args.get("model") or None
        svc = StoryService(session)
        result = svc.generate_character_profile(story_id, generation_type, parameters, use_context, model)
        return ok(result)
    except Exception as e:
        return err(str(e))
    finally:
        session.close()


async def _generate_worldbuilding(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from services.story_service import StoryService
    session = host.get_db_session()
    try:
        story_id = int(args["story_id"])
        chapter_id = int(args["chapter_id"])
        generation_type = args.get("generation_type", "location")
        parameters = args.get("parameters") or {}
        use_context = args.get("use_context", True)
        model = args.get("model") or None
        svc = StoryService(session)
        result = svc.generate_worldbuilding_element(story_id, chapter_id, generation_type, parameters, use_context, model)
        return ok(result)
    except Exception as e:
        return err(str(e))
    finally:
        session.close()


async def _generate_prose(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from services.story_service import StoryService
    session = host.get_db_session()
    try:
        chapter_id = int(args["chapter_id"])
        prompt = args.get("prompt", "")
        context_type = args.get("context_type", "full")
        model = args.get("model") or None
        svc = StoryService(session)
        result = svc.generate_prose(chapter_id, prompt, context_type, model)
        return ok(result)
    except Exception as e:
        return err(str(e))
    finally:
        session.close()


async def _query_context(args: dict[str, Any], host: HostContext) -> dict[str, Any]:
    from services.story_service import StoryService
    session = host.get_db_session()
    try:
        story_id = int(args["story_id"])
        query = args.get("query", "")
        top_k = args.get("top_k", 5)
        model = args.get("model") or None
        svc = StoryService(session)
        result = svc.query_context(story_id, query, top_k, model)
        return ok(result)
    except Exception as e:
        return err(str(e))
    finally:
        session.close()
