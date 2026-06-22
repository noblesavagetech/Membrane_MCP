"""
Membrane MCP Server — main loop using stdio transport.

Receives JSON-RPC requests on stdin, writes responses to stdout.
Reference: https://modelcontextprotocol.io/docs/specification
"""

import json
import sys
import traceback
from typing import Any

from protocol import JSONRPCResponse, JSONRPCRequest, MCPInitializeResult, MSG_TYPE

# Import tools and resources after sys.path is set in host_context
from host_context import HOST
from tools import STORY_TOOLS, GENERATION_TOOLS
from resources import STORY_RESOURCES


# ---- Capability registry ----

CAPABILITIES = {
    "tools": {},
    "resources": {"subscribe": False, "listChanged": False},
    "prompts": {},
    "logging": {},
}


# ---- Dispatch table ----

async def handle_initialize(params: dict[str, Any]) -> dict[str, Any]:
    result = MCPInitializeResult(
        protocolVersion="2024-11-05",
        capabilities=CAPABILITIES,
        serverInfo={"name": "membrane-story-engine", "version": "0.1.0"},
    )
    return {
        "protocolVersion": result.protocolVersion,
        "capabilities": result.capabilities,
        "serverInfo": result.serverInfo,
        "instructions": (
            "Membrane Story Engine MCP Server. "
            "Exposes story, chapter, character, beat, and worldbuilding CRUD + AI generation. "
            "Authenticate by setting MEMBRANE_AUTH_TOKEN or OPENROUTER_API_KEY env vars."
        ),
    }


async def handle_tools_list(params: dict[str, Any]) -> dict[str, Any]:
    all_tools = STORY_TOOLS + GENERATION_TOOLS
    return {
        "tools": [
            {
                "name": t["name"],
                "description": t["description"],
                "inputSchema": t["inputSchema"],
            }
            for t in all_tools
        ]
    }


async def handle_tools_call(params: dict[str, Any]) -> dict[str, Any]:
    tool_name: str = params.get("name", "")
    arguments: dict[str, Any] = params.get("arguments", {})

    all_tools = {t["name"]: t for t in STORY_TOOLS + GENERATION_TOOLS}

    if tool_name not in all_tools:
        raise ValueError(f"Unknown tool: {tool_name}")

    tool = all_tools[tool_name]
    handler = tool["handler"]

    try:
        result = await handler(arguments, HOST)
    except Exception as exc:
        return {"content": [{"type": "text", "text": f"Error: {exc}"}], "isError": True}

    return {
        "content": [{"type": "text", "text": json.dumps(result, indent=2, default=str)}]
    }


async def handle_resources_list(params: dict[str, Any]) -> dict[str, Any]:
    return {"resources": STORY_RESOURCES}


async def handle_resources_read(params: dict[str, Any]) -> dict[str, Any]:
    uri: str = params.get("uri", "")
    # Delegate to resource handler
    from resources import handle_resource_read
    result = await handle_resource_read(uri, HOST)
    return {
        "contents": [{"uri": uri, "mimeType": "application/json", "text": json.dumps(result, default=str)}]
    }


DISPATCH = {
    MSG_TYPE.INITIALIZE.value:   handle_initialize,
    MSG_TYPE.TOOLS_LIST.value:  handle_tools_list,
    MSG_TYPE.TOOLS_CALL.value:  handle_tools_call,
    MSG_TYPE.RESOURCES_LIST.value: handle_resources_list,
    MSG_TYPE.RESOURCES_READ.value: handle_resources_read,
}


# ---- JSON-RPC message loop ----

def read_message() -> dict[str, Any] | None:
    """Read a single newline-delimited JSON-RPC message from stdin."""
    try:
        line = sys.stdin.readline()
        if not line:
            return None
        return json.loads(line.strip())
    except json.JSONDecodeError:
        return None


def send_message(msg: dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(msg) + "\n")
    sys.stdout.flush()


def build_error_response(rpc_id: str | int | None, code: int, message: str) -> dict[str, Any]:
    return JSONRPCResponse(
        id=rpc_id,
        error={"code": code, "message": message},
    ).to_dict()


async def process_request(request: dict[str, Any]) -> dict[str, Any] | None:
    """Process a single JSON-RPC request and return the response dict."""
    method: str = request.get("method", "")
    rpc_id = request.get("id")

    # Handle "notificaciones" (no id) — we don't produce responses for these
    if request.get("jsonrpc") != "2.0":
        return build_error_response(rpc_id, -32600, "Invalid JSON-RPC 2.0 request")

    handler = DISPATCH.get(method)
    if handler is None:
        return build_error_response(rpc_id, -32601, f"Method not found: {method}")

    try:
        params = request.get("params", {})
        result = await handler(params)
        return JSONRPCResponse(id=rpc_id, result=result).to_dict()
    except Exception as exc:  # pragma: no cover — log but don't crash
        tb = traceback.format_exc()
        if HOST.debug:
            print(tb, file=sys.stderr)
        return build_error_response(rpc_id, -32603, f"Internal error: {exc}")


async def main() -> None:
    """Main stdio loop."""
    while True:
        raw = read_message()
        if raw is None:
            break  # EOF

        # Batch requests not supported for now — handle single
        response = await process_request(raw)
        if response is not None:
            send_message(response)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
