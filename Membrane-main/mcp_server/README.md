# Membrane MCP Server

Exposes the Membrane story engine as a [Model Context Protocol](https://modelcontextprotocol.io) (MCP) server. Once connected, any MCP-compatible AI client (Claude Desktop, Cursor, etc.) can directly query and edit your Membrane stories, characters, beats, and worldbuilding — and invoke AI generation — without any custom API glue code.

---

## Architecture

```
┌─────────────────────────────┐        ┌──────────────────────────────┐
│   MCP Client (Claude etc.)  │───────▶│   Membrane MCP Server         │
│                             │  stdio │   ├── protocol.py  (JSON-RPC) │
│   Tools: get_story,          │        │   ├── server.py   (dispatch)  │
│   create_beat,              │        │   ├── host_context.py       │
│   generate_prose, …         │        │   ├── tools/      (domain)    │
│                             │        │   └── resources/  (data)     │
└─────────────────────────────┘        └────────────┬─────────────────┘
                                                     │
                                              ┌──────▼──────┐
                                              │  Membrane   │
                                              │  Backend    │
                                              │  (SQLAlchemy│
                                              │   + FastAPI)│
                                              └─────────────┘
```

The MCP server is a **standalone Python process** that communicates over stdio using JSON-RPC 2.0. It shares the same `backend/` models and services, so it never re-implements database logic.

---

## Features

### Tools (20 total)

#### Story Management
| Tool | Description |
|------|-------------|
| `list_stories` | List all stories |
| `get_story` | Full story with chapters, characters, beats, worldbuilding |
| `create_story` | New story (auto-creates first chapter) |
| `update_story` | Update title/description |
| `delete_story` | Delete story and all children |

#### Chapter Management
| Tool | Description |
|------|-------------|
| `create_chapter` | Add chapter to a story |
| `update_chapter` | Update title, text, or summary |
| `summarize_chapter` | AI-summarize chapter prose |

#### Character Management
| Tool | Description |
|------|-------------|
| `list_characters` | All characters in a story |
| `create_character` | New character |
| `update_character` | Update fields |
| `delete_character` | Remove character |

#### Beat / Scene Management
| Tool | Description |
|------|-------------|
| `create_beat` | Add beat/scene to chapter |
| `get_beats` | List chapter beats |
| `update_beat` | Update beat description or order |
| `delete_beat` | Remove beat |

#### Worldbuilding & Key Events
| Tool | Description |
|------|-------------|
| `create_world_element` | Add worldbuilding to chapter |
| `get_world_elements` | List chapter worldbuilding |
| `create_key_event` | Add key event to chapter |
| `get_key_events` | List chapter key events |

#### Memory (RAG)
| Tool | Description |
|------|-------------|
| `add_memory` | Add text to vector store |
| `search_memory` | Semantic search across project |

#### AI Generation
| Tool | Description |
|------|-------------|
| `generate_character` | AI-generate full character profile |
| `generate_worldbuilding` | AI-generate worldbuilding element |
| `generate_prose` | AI-generate prose from beats & context |
| `query_context` | RAG-style context compilation |

### Resources

| URI Pattern | Description |
|-------------|-------------|
| `story://{id}` | Full story data |
| `chapter://{id}` | Chapter with beats, worldbuilding, key events |
| `character://{id}` | Character profile |
| `beat://{id}` | Single beat |
| `worldelement://{id}` | Worldbuilding element |
| `keyevent://{id}` | Key event |

---

## Setup

### 1. Install Dependencies

```bash
cd Membrane-main/mcp_server
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env with your database URL and OpenRouter API key
```

Required variables:
- `DATABASE_URL` (PostgreSQL or SQLite)
- `OPENROUTER_API_KEY`
- `JWT_SECRET` (any random string for dev)

### 3. Run the Server

```bash
python run.py
```

The server runs over **stdio** — it reads JSON-RPC requests from stdin and writes responses to stdout. This is the standard transport for MCP.

---

## MCP Client Configuration

### Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "membrane": {
      "command": "python",
      "args": ["/absolute/path/to/Membrane-main/mcp_server/run.py"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost:5432/membrane",
        "OPENROUTER_API_KEY": "sk-or-v1-...",
        "JWT_SECRET": "your-jwt-secret"
      }
    }
  }
}
```

### Cursor

Add to Cursor settings → MCP Servers:

```json
{
  "membrane": {
    "command": "python",
    "args": ["/path/to/Membrane-main/mcp_server/run.py"]
  }
}
```

### VS Code Copilot (Agent Mode)

Add to your workspace `.vscode/mcp.json`:

```json
{
  "servers": {
    "membrane": {
      "command": "python",
      "args": ["${workspaceFolder}/Membrane-main/mcp_server/run.py"]
    }
  }
}
```

---

## Example AI Conversations

Once connected, you can ask Claude or any MCP client:

> "Give me a summary of Sarah's character arc across all chapters."

> "Generate a new scene beat for chapter 3 where Marcus confronts the villain."

> "Write the prose for chapter 2 using the current beats."

> "What worldbuilding elements have we defined for the northern kingdom?"

The LLM calls the appropriate tools in sequence — querying your live Membrane database — and synthesizes a response grounded in your actual story data.

---

## Extending the Server

### Adding a New Tool

1. Add the tool definition to `STORY_TOOLS` or `GENERATION_TOOLS` in `mcp_server/tools/__init__.py`
2. Implement the handler function (`async def _my_tool(args, host) -> dict`)
3. The tool is automatically registered on next startup

### Adding a New Resource

1. Add the resource definition to `STORY_RESOURCES` in `mcp_server/resources/__init__.py`
2. Extend `_parse_uri()` and `handle_resource_read()` with the new URI scheme

---

## Protocol Reference

- [MCP Specification](https://modelcontextprotocol.io/docs/specification)
- [MCP Architecture](https://modelcontextprotocol.io/docs/learn/architecture)
- [JSON-RPC 2.0](https://www.jsonrpc.org/specification)
