"""
MCP Router — FastAPI router for the embedded MCP HTTP endpoint.

Endpoint: POST /api/mcp
  Body: { method, params }
  params must include story_id (int) to scope the session.

The MCP session is per-story. The LLM can only see and modify the story
identified by the story_id in the request. This gives every story its own
isolated MCP context.

Reference: MCP HTTP endpoint spec — https://modelcontextprotocol.io/docs/specification
"""

from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from services.database_service import get_session
from services.mcp_service import (
    MCPSession,
    call_mcp_tool,
    get_mcp_resources,
    get_mcp_tools,
)


router = APIRouter(prefix="/api/mcp", tags=["MCP"])


# ---------------------------------------------------------------------------
# Request / Response models
# ---------------------------------------------------------------------------

class MCPRequest(BaseModel):
    method: str
    params: dict = {}


class MCPResponse(BaseModel):
    method: str
    result: dict | None = None
    error: dict | None = None


class MCPConfigRequest(BaseModel):
    provider: str = "openrouter"          # openrouter | gemini | openai
    model: str = "default"
    system_prompt: str = ""
    enabled: bool = True


# ---------------------------------------------------------------------------
# MCP Dispatch
# ---------------------------------------------------------------------------

@router.post("")
async def mcp_dispatch(
    body: MCPRequest,
    db: Session = Depends(get_session),
):
    """
    Main MCP endpoint. Accepts a JSON-RPC-like request body.

    Required params:
      - story_id (int): scopes the MCP session to a specific story

    Supported methods:
      - tools/list       → returns all available tools
      - tools/call       → calls a tool with { name, arguments }
      - resources/list   → returns all available resource types
      - resources/read   → reads a resource by URI
    """
    method = body.method
    params = body.params or {}

    story_id: int | None = params.get("story_id")
    user_id = _resolve_user_id(params)

    # -- tools/list --
    if method == "tools/list":
        return {"method": method, "result": {"tools": get_mcp_tools()}}

    # -- resources/list --
    if method == "resources/list":
        return {"method": method, "result": {"resources": get_mcp_resources()}}

    # -- resources/read --
    if method == "resources/read":
        uri = params.get("uri", "")
        return {
            "method": method,
            "result": _read_resource(uri, db, user_id),
        }

    # -- tools/call --
    if method == "tools/call":
        tool_name = params.get("name", "")
        raw_args: dict = params.get("arguments", {}) or {}

        # story_id must be in the args or at the top level of params
        effective_story_id = raw_args.get("story_id") or story_id
        if not effective_story_id:
            raise HTTPException(status_code=400, detail="story_id is required in params or arguments")

        # Load MCP config for this story
        mcp_cfg = _load_mcp_config(db, effective_story_id, user_id)
        if not mcp_cfg["enabled"]:
            raise HTTPException(status_code=403, detail="MCP is disabled for this story")

        mcp_session = MCPSession(
            story_id=effective_story_id,
            user_id=user_id,
            provider=mcp_cfg["provider"],
            model=mcp_cfg["model"] or "default",
            system_prompt=mcp_cfg["system_prompt"],
        )

        result = await call_mcp_tool(tool_name, raw_args, mcp_session, db)

        # Return both the result and metadata about which tools were used.
        # This lets the frontend debug panel show exactly what the LLM called.
        response = {"method": method, "result": result}
        response["tool_calls"] = [{
            "tool": tool_name,
            "args": raw_args,
            "time": datetime.now().isoformat()
        }]
        return response

    # -- generate (MCP-aware generation) --
    if method == "generate":
        # This is the new path that the frontend (StoryEditor, CharacterGenerator, WorldbuildingGenerator)
        # will call. It accepts the same parameters as the old /api/ai/generate but routes through MCP tools.
        raw_args: dict = params.get("arguments", params) or {}
        story_id = raw_args.get("story_id") or params.get("story_id")
        if not story_id:
            raise HTTPException(status_code=400, detail="story_id is required")

        mcp_cfg = _load_mcp_config(db, story_id, user_id)
        if not mcp_cfg["enabled"]:
            # If MCP is disabled for this story, fall back to old behavior
            from services.story_service import StoryService
            svc = StoryService(db)
            result = await svc.generate_from_prompt(
                prompt=raw_args.get("prompt", ""),
                model=raw_args.get("model", "default"),
            )
            return {"method": method, "result": {"content": result}}

        mcp_session = MCPSession(
            story_id=story_id,
            user_id=user_id,
            provider=mcp_cfg["provider"],
            model=raw_args.get("model") or mcp_cfg["model"] or "default",
            system_prompt=mcp_cfg["system_prompt"],
        )

        # Route to the appropriate MCP tool based on context_type or generation_type
        context_type = raw_args.get("context_type", "")
        generation_type = raw_args.get("generation_type", "")

        # Character generation types: protagonist, antagonist, supporting, minor
        CHARACTER_TYPES = {"protagonist", "antagonist", "supporting", "minor", "full_profile", "physical_only"}
        # Worldbuilding generation types: location, culture, magic_system, etc.
        WORLD_TYPES = {"location", "culture", "magic_system", "technology", "history", "creature"}

        if generation_type.lower() in CHARACTER_TYPES:
            tool_name = "generate_character"
        elif generation_type.lower() in WORLD_TYPES:
            tool_name = "generate_worldbuilding"
        elif context_type == "beat" or "beat" in raw_args.get("prompt", "").lower():
            tool_name = "generate_prose"  # beat expansion still uses prose tool for now
        else:
            tool_name = "generate_prose"

        result = await call_mcp_tool(tool_name, raw_args, mcp_session, db)

        # Return both the result and metadata about which tools were used.
        # This lets the frontend debug panel show exactly what the LLM called.
        response = {"method": method, "result": result}
        if isinstance(result, dict) and "tool_calls" in result:
            response["tool_calls"] = result["tool_calls"]
        else:
            response["tool_calls"] = [{
                "tool": tool_name,
                "args": raw_args,
                "time": datetime.now().isoformat()
            }]
        return response

    # Unknown method
    raise HTTPException(status_code=404, detail=f"Unknown MCP method: {method}")


# ---------------------------------------------------------------------------
# MCP Config endpoints (per-story)
# ---------------------------------------------------------------------------

@router.get("/config/{story_id}")
async def get_mcp_config(
    story_id: int,
    db: Session = Depends(get_session),
):
    """Get the MCP configuration for a specific story."""
    user_id = _resolve_user_id({})
    cfg = _load_mcp_config(db, story_id, user_id)
    return cfg


@router.put("/config/{story_id}")
async def update_mcp_config(
    story_id: int,
    payload: MCPConfigRequest,
    db: Session = Depends(get_session),
):
    """Update the MCP configuration for a specific story."""
    user_id = _resolve_user_id({})

    # Verify user owns the story
    from models import Story
    story = db.query(Story).filter(Story.id == story_id, Story.user_id == user_id).first()
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")

    cfg = _upsert_mcp_config(db, story_id, payload)
    return cfg


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _resolve_user_id(params: dict) -> int:
    """
    Resolve user_id from the request context.
    In a real deployment this would come from the JWT auth token.
    For now we support an optional X-User-ID header override for testing.
    """
    # FastAPI Depends can't easily pass headers here, so we check the params
    if "user_id" in params:
        return int(params["user_id"])
    # Default: dev user (matches backend's get_current_user dev fallback)
    return 1


def _load_mcp_config(db: Session, story_id: int, user_id: int) -> dict:
    """Return MCP config for a story, returning defaults if none exists."""
    from models import Story, MCPConfig
    # Verify ownership
    story = db.query(Story).filter(Story.id == story_id, Story.user_id == user_id).first()
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")

    cfg = db.query(MCPConfig).filter(MCPConfig.story_id == story_id).first()
    if not cfg:
        return {"provider": "openrouter", "model": "default", "system_prompt": "", "enabled": True}
    return {
        "provider": cfg.provider,
        "model": cfg.model,
        "system_prompt": cfg.system_prompt,
        "enabled": cfg.enabled,
    }


def _upsert_mcp_config(db: Session, story_id: int, payload: MCPConfigRequest) -> dict:
    from models import MCPConfig
    cfg = db.query(MCPConfig).filter(MCPConfig.story_id == story_id).first()
    if not cfg:
        cfg = MCPConfig(story_id=story_id)
        db.add(cfg)
    cfg.provider = payload.provider
    cfg.model = payload.model
    cfg.system_prompt = payload.system_prompt
    cfg.enabled = payload.enabled
    db.commit()
    db.refresh(cfg)
    return {
        "provider": cfg.provider,
        "model": cfg.model,
        "system_prompt": cfg.system_prompt,
        "enabled": cfg.enabled,
    }


def _read_resource(uri: str, db: Session, user_id: int) -> dict:
    """Read a resource by URI within the user's story context."""
    from models import Story, Chapter, Character, BeatScene, WorldBuildingElement, KeyEvent
    from services.story_service import StoryService

    if uri.startswith("story://"):
        story_id = int(uri[len("story://") :])
        svc = StoryService(db)
        story = svc.get_story(story_id, user_id)
        if not story:
            raise HTTPException(status_code=404, detail="Story not found")
        chapters = db.query(Chapter).filter(Chapter.story_id == story_id).order_by(Chapter.order).all()
        characters = db.query(Character).filter(Character.story_id == story_id).all()
        return {
            "id": story.id, "title": story.title, "description": story.description,
            "chapters": [{"id": c.id, "title": c.title, "order": c.order} for c in chapters],
            "characters": [{"id": c.id, "name": c.name, "role": c.role} for c in characters],
        }

    if uri.startswith("chapter://"):
        chapter_id = int(uri[len("chapter://") :])
        chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
        if not chapter:
            raise HTTPException(status_code=404, detail="Chapter not found")
        beats = db.query(BeatScene).filter(BeatScene.chapter_id == chapter_id).order_by(BeatScene.order).all()
        world = db.query(WorldBuildingElement).filter(WorldBuildingElement.chapter_id == chapter_id).all()
        key_events = db.query(KeyEvent).filter(KeyEvent.chapter_id == chapter_id).order_by(KeyEvent.order).all()
        return {
            "id": chapter.id, "title": chapter.title, "text": chapter.text, "summary": chapter.summary, "order": chapter.order,
            "beats": [{"id": b.id, "description": b.description, "order": b.order} for b in beats],
            "worldbuilding": [{"id": w.id, "category": w.category, "description": w.description} for w in world],
            "key_events": [{"id": k.id, "description": k.description, "order": k.order} for k in key_events],
        }

    if uri.startswith("character://"):
        char_id = int(uri[len("character://") :])
        char = db.query(Character).filter(Character.id == char_id).first()
        if not char:
            raise HTTPException(status_code=404, detail="Character not found")
        return {"id": char.id, "story_id": char.story_id, "name": char.name, "role": char.role,
                "traits": char.traits, "backstory": char.backstory, "description": char.description}

    if uri.startswith("beat://"):
        beat_id = int(uri[len("beat://") :])
        beat = db.query(BeatScene).filter(BeatScene.id == beat_id).first()
        if not beat:
            raise HTTPException(status_code=404, detail="Beat not found")
        return {"id": beat.id, "chapter_id": beat.chapter_id, "description": beat.description, "order": beat.order}

    if uri.startswith("worldelement://"):
        elem_id = int(uri[len("worldelement://") :])
        elem = db.query(WorldBuildingElement).filter(WorldBuildingElement.id == elem_id).first()
        if not elem:
            raise HTTPException(status_code=404, detail="Worldbuilding element not found")
        return {"id": elem.id, "chapter_id": elem.chapter_id, "category": elem.category, "description": elem.description}

    if uri.startswith("keyevent://"):
        event_id = int(uri[len("keyevent://") :])
        event = db.query(KeyEvent).filter(KeyEvent.id == event_id).first()
        if not event:
            raise HTTPException(status_code=404, detail="Key event not found")
        return {"id": event.id, "chapter_id": event.chapter_id, "description": event.description, "order": event.order}

    raise HTTPException(status_code=400, detail=f"Unknown resource URI: {uri}")
