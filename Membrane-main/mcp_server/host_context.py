"""
Host context — bridges the MCP server to Membrane's existing backend.

Loads environment variables and provides a shared "service layer" that mirrors
the backend's story_service so the MCP tools don't need to re-implement DB access.
"""

import os
import sys
from pathlib import Path
from typing import Any

# Ensure the backend module is importable
_BACKEND_ROOT = Path(__file__).parent.parent / "backend"
sys.path.insert(0, str(_BACKEND_ROOT))

from dotenv import load_dotenv

load_dotenv(_BACKEND_ROOT / ".env", override=False)


class HostContext:
    """Read-only view of the Membrane backend environment and config."""

    def __init__(self) -> None:
        self.database_url: str | None = os.environ.get("DATABASE_URL")
        self.openrouter_api_key: str | None = os.environ.get("OPENROUTER_API_KEY")
        self.openrouter_base_url: str = os.environ.get(
            "OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"
        )
        self.debug: bool = os.environ.get("DEBUG", "").lower() in ("1", "true", "yes")
        self._db_session_factory = None

    # ---- DB session (lazy init to match backend's database_service) ----

    def get_db_session(self):
        """Return a new DB session. Caller must close it."""
        if self._db_session_factory is None:
            from services.database_service import engine
            from sqlalchemy.orm import sessionmaker
            self._db_session_factory = sessionmaker(bind=engine)
        return self._db_session_factory()


# Global singleton
HOST = HostContext()
