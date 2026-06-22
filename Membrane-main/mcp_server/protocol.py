"""
MCP Protocol types — JSON-RPC 2.0 based.
Reference: https://modelcontextprotocol.io/docs/specification
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class JSONRPCVersion(Enum):
    V2 = "2.0"


@dataclass
class JSONRPCRequest:
    jsonrpc: str = "2.0"
    id: str | int | None = None
    method: str = ""
    params: dict[str, Any] = field(default_factory=dict)


@dataclass
class JSONRPCResponse:
    jsonrpc: str = "2.0"
    id: str | int | None = None
    result: dict[str, Any] | None = None
    error: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        out: dict[str, Any] = {"jsonrpc": self.jsonrpc, "id": self.id}
        if self.result is not None:
            out["result"] = self.result
        if self.error is not None:
            out["error"] = self.error
        return out


@dataclass
class MCPInitializeResult:
    protocolVersion: str = "2024-11-05"
    capabilities: dict[str, Any]
    serverInfo: dict[str, str]


# ---- Protocol message types ----

class MSG_TYPE(str, Enum):
    INITIALIZE   = "initialize"
    INITIALIZED   = "initialized"
    TOOLS_LIST    = "tools/list"
    TOOLS_CALL    = "tools/call"
    RESOURCES_LIST = "resources/list"
    RESOURCES_READ = "resources/read"
    SHUTDOWN       = "shutdown"
    CANCEL         = "cancel/notifications/cancelled"
