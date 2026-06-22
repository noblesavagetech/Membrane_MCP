"""
MCP Resources — represent Membrane story data as addressable resources.

Each resource has a URI like:
  story://<story_id>
  chapter://<chapter_id>
  character://<character_id>
  beat://<beat_id>
  worldelement://<worldelement_id>
  keyevent://<keyevent_id>

Reference: https://modelcontextprotocol.io/docs/specification/basic/resources
"""

from typing import Any

from host_context import HostContext


STORY_RESOURCES = [
    {
        "uri": "story://{story_id}",
        "name": "Story",
        "description": "A full story with chapters, characters, beats, and worldbuilding data.",
        "mimeType": "application/json",
    },
    {
        "uri": "chapter://{chapter_id}",
        "name": "Chapter",
        "description": "A single chapter with its text, summary, beats, worldbuilding, and key events.",
        "mimeType": "application/json",
    },
    {
        "uri": "character://{character_id}",
        "name": "Character",
        "description": "A character profile — name, role, traits, backstory, and description.",
        "mimeType": "application/json",
    },
    {
        "uri": "beat://{beat_id}",
        "name": "Beat",
        "description": "A single story beat/scene within a chapter.",
        "mimeType": "application/json",
    },
    {
        "uri": "worldelement://{worldelement_id}",
        "name": "Worldbuilding Element",
        "description": "A worldbuilding element within a chapter.",
        "mimeType": "application/json",
    },
    {
        "uri": "keyevent://{keyevent_id}",
        "name": "Key Event",
        "description": "A key event/outline point within a chapter.",
        "mimeType": "application/json",
    },
]


def _parse_uri(uri: str) -> tuple[str, dict[str, Any]]:
    """
    Parse a Membrane resource URI and return (resource_type, params).
    E.g. "story://123" → ("story", {"story_id": "123"})
    """
    if uri.startswith("story://"):
        return "story", {"story_id": uri[len("story://") :]}
    if uri.startswith("chapter://"):
        return "chapter", {"chapter_id": uri[len("chapter://") :]}
    if uri.startswith("character://"):
        return "character", {"character_id": uri[len("character://") :]}
    if uri.startswith("beat://"):
        return "beat", {"beat_id": uri[len("beat://") :]}
    if uri.startswith("worldelement://"):
        return "worldelement", {"worldelement_id": uri[len("worldelement://") :]}
    if uri.startswith("keyevent://"):
        return "keyevent", {"keyevent_id": uri[len("keyevent://") :]}
    raise ValueError(f"Unknown resource URI scheme: {uri}")


async def handle_resource_read(uri: str, host: HostContext) -> dict[str, Any]:
    """Fetch the data behind a resource URI."""
    resource_type, params = _parse_uri(uri)
    session = host.get_db_session()

    try:
        from models import Story, Chapter, Character, BeatScene, WorldBuildingElement, KeyEvent

        if resource_type == "story":
            story_id = int(params["story_id"])
            story = session.query(Story).filter(Story.id == story_id).first()
            if not story:
                raise ValueError(f"Story {story_id} not found")

            chapters = (
                session.query(Chapter)
                .filter(Chapter.story_id == story_id)
                .order_by(Chapter.order)
                .all()
            )
            characters = (
                session.query(Character)
                .filter(Character.story_id == story_id)
                .all()
            )

            return {
                "id": story.id,
                "title": story.title,
                "description": story.description,
                "created_at": str(story.created_at),
                "updated_at": str(story.updated_at) if story.updated_at else None,
                "chapters": [
                    {
                        "id": c.id,
                        "title": c.title,
                        "order": c.order,
                        "summary": c.summary,
                    }
                    for c in chapters
                ],
                "characters": [
                    {
                        "id": c.id,
                        "name": c.name,
                        "role": c.role,
                        "traits": c.traits,
                        "backstory": c.backstory,
                        "description": c.description,
                    }
                    for c in characters
                ],
            }

        elif resource_type == "chapter":
            chapter_id = int(params["chapter_id"])
            chapter = session.query(Chapter).filter(Chapter.id == chapter_id).first()
            if not chapter:
                raise ValueError(f"Chapter {chapter_id} not found")

            beats = (
                session.query(BeatScene)
                .filter(BeatScene.chapter_id == chapter_id)
                .order_by(BeatScene.order)
                .all()
            )
            world_elements = (
                session.query(WorldBuildingElement)
                .filter(WorldBuildingElement.chapter_id == chapter_id)
                .all()
            )
            key_events = (
                session.query(KeyEvent)
                .filter(KeyEvent.chapter_id == chapter_id)
                .order_by(KeyEvent.order)
                .all()
            )

            return {
                "id": chapter.id,
                "story_id": chapter.story_id,
                "title": chapter.title,
                "text": chapter.text,
                "summary": chapter.summary,
                "order": chapter.order,
                "created_at": str(chapter.created_at),
                "updated_at": str(chapter.updated_at) if chapter.updated_at else None,
                "beats": [
                    {
                        "id": b.id,
                        "description": b.description,
                        "order": b.order,
                    }
                    for b in beats
                ],
                "worldbuilding": [
                    {
                        "id": w.id,
                        "category": w.category,
                        "description": w.description,
                    }
                    for w in world_elements
                ],
                "key_events": [
                    {
                        "id": k.id,
                        "description": k.description,
                        "order": k.order,
                    }
                    for k in key_events
                ],
            }

        elif resource_type == "character":
            char_id = int(params["character_id"])
            character = session.query(Character).filter(Character.id == char_id).first()
            if not character:
                raise ValueError(f"Character {char_id} not found")
            return {
                "id": character.id,
                "story_id": character.story_id,
                "name": character.name,
                "role": character.role,
                "traits": character.traits,
                "backstory": character.backstory,
                "description": character.description,
                "created_at": str(character.created_at),
            }

        elif resource_type == "beat":
            beat_id = int(params["beat_id"])
            beat = session.query(BeatScene).filter(BeatScene.id == beat_id).first()
            if not beat:
                raise ValueError(f"Beat {beat_id} not found")
            return {
                "id": beat.id,
                "chapter_id": beat.chapter_id,
                "description": beat.description,
                "order": beat.order,
                "created_at": str(beat.created_at),
            }

        elif resource_type == "worldelement":
            elem_id = int(params["worldelement_id"])
            elem = (
                session.query(WorldBuildingElement)
                .filter(WorldBuildingElement.id == elem_id)
                .first()
            )
            if not elem:
                raise ValueError(f"Worldbuilding element {elem_id} not found")
            return {
                "id": elem.id,
                "chapter_id": elem.chapter_id,
                "category": elem.category,
                "description": elem.description,
                "created_at": str(elem.created_at),
            }

        elif resource_type == "keyevent":
            event_id = int(params["keyevent_id"])
            event = session.query(KeyEvent).filter(KeyEvent.id == event_id).first()
            if not event:
                raise ValueError(f"Key event {event_id} not found")
            return {
                "id": event.id,
                "chapter_id": event.chapter_id,
                "description": event.description,
                "order": event.order,
                "created_at": str(event.created_at),
            }

        else:
            raise ValueError(f"Unknown resource type: {resource_type}")
    finally:
        session.close()
