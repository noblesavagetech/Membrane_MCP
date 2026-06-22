import hashlib
import json
import os
from typing import AsyncGenerator, Optional
import httpx

MODELS = {
    "default": "anthropic/claude-sonnet-4.5",
    "mini-max": "minimax/minimax-m2.7",
    "gemini-flash": "google/gemini-3.1-flash-lite-preview",
    "deepseek": "deepseek/deepseek-v4-flash",
    "moonshot": "moonshotai/kimi-k2.5",
    "grok": "x-ai/grok-4.3",
    "gpt-oss": "openai/gpt-oss-120b",
    "mimo-v2-pro": "xiaomi/mimo-v2.5",
    "glm-5": "z-ai/glm-5",
}

MODEL_OPTIONS = [
    {"id": "anthropic/claude-sonnet-4.5", "name": "Claude Sonnet 4.5"},
    {"id": "minimax/minimax-m2.7", "name": "MiniMax M2.7"},
    {"id": "google/gemini-3.1-flash-lite-preview", "name": "Gemini 3.1 Flash Preview"},
    {"id": "deepseek/deepseek-v4-flash", "name": "DeepSeek V4 Flash"},
    {"id": "moonshotai/kimi-k2.5", "name": "Kimi K2.5"},
    {"id": "x-ai/grok-4.3", "name": "Grok 4.3"},
    {"id": "openai/gpt-oss-120b", "name": "GPT OSS 120B"},
    {"id": "xiaomi/mimo-v2.5", "name": "MiMo V2.5"},
    {"id": "z-ai/glm-5", "name": "GLM 5"},
]

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")

class OpenRouterService:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or OPENROUTER_API_KEY
        self.base_url = "https://openrouter.ai/api/v1"

    def _get_headers(self):
        return {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json", "HTTP-Referer": "https://membrane.app", "X-Title": "Membrane"}

    def _resolve_model(self, model: str) -> str:
        return MODELS.get(model, model) if model != "default" else MODELS["default"]

    async def stream_chat(self, messages: list, model: str = "default", temperature: float = 0.7, max_tokens: int = 4096) -> AsyncGenerator[str, None]:
        if not self.api_key:
            yield "OpenRouter API key not configured."
            return
        payload = {"model": self._resolve_model(model), "messages": messages, "temperature": temperature, "max_tokens": max_tokens, "stream": True}
        async with httpx.AsyncClient(timeout=120.0) as client:
            async with client.stream("POST", f"{self.base_url}/chat/completions", headers=self._get_headers(), json=payload) as response:
                if response.status_code >= 400:
                    error_body = (await response.aread()).decode("utf-8", errors="ignore")
                    yield f"OpenRouter request failed ({response.status_code}): {error_body[:500]}"
                    return
                async for line in response.aiter_lines():
                    if not line.startswith("data: "):
                        continue
                    data = line[6:]
                    if data == "[DONE]":
                        break
                    try:
                        chunk = json.loads(data)
                        content = chunk.get("choices", [{}])[0].get("delta", {}).get("content", "")
                        if content:
                            yield content
                    except json.JSONDecodeError:
                        continue

    async def chat(self, messages: list, model: str = "default", temperature: float = 0.7, max_tokens: int = 4096) -> str:
        if not self.api_key:
            return "OpenRouter API key not configured."
        payload = {"model": self._resolve_model(model), "messages": messages, "temperature": temperature, "max_tokens": max_tokens}
        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(f"{self.base_url}/chat/completions", headers=self._get_headers(), json=payload)
            if response.status_code >= 400:
                try:
                    error_json = response.json()
                    error_text = json.dumps(error_json)
                except Exception:
                    error_text = response.text
                return f"OpenRouter request failed ({response.status_code}): {error_text[:500]}"
            return response.json()["choices"][0]["message"]["content"]

    async def get_embedding(self, text: str) -> list:
        if not self.api_key:
            digest = hashlib.sha256(text.encode()).digest()
            return [b / 255.0 for b in digest]
        payload = {"model": "text-embedding-3-small", "input": text}
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(f"{self.base_url}/embeddings", headers=self._get_headers(), json=payload)
            response.raise_for_status()
            return response.json()["data"][0]["embedding"]

    async def summarize_text(self, text: str, model: str = "default") -> str:
        return await self.chat([{"role": "system", "content": "Summarize concisely."}, {"role": "user", "content": text}], model, 0.3, 512)

openrouter_service = OpenRouterService()
