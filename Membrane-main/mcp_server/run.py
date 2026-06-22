#!/usr/bin/env python3
"""Entry point — run the MCP server over stdio."""

import asyncio
import sys
from pathlib import Path

# Ensure host_context sets up the path before any other backend imports
sys.path.insert(0, str(Path(__file__).parent))

from server import main

if __name__ == "__main__":
    asyncio.run(main())
