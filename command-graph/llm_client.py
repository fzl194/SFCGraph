"""
DeepSeek LLM Client — 从项目 .env 读取配置，提供同步/批量调用接口。
"""
import json
import os
import time
import pathlib
import requests

# ── 配置 ──────────────────────────────────────────────
_ROOT = pathlib.Path(__file__).resolve().parent.parent  # SFCGraph 根目录
_DOTENV = _ROOT / ".env"

def _load_env():
    cfg = {}
    if _DOTENV.exists():
        for line in _DOTENV.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            cfg[k.strip()] = v.strip()
    return cfg

_env = _load_env()

BASE_URL = _env.get("LLM_SERVICE_PROVIDER_BASE_URL", "").rstrip("/")
API_KEY  = _env.get("LLM_SERVICE_PROVIDER_API_KEY", "")
MODEL    = _env.get("LLM_SERVICE_PROVIDER_MODEL", "deepseek-chat")

# DeepSeek 的 chat/completions 端点
# .env 中给的是完整 URL，直接用
API_URL = BASE_URL if BASE_URL.endswith("/chat/completions") else BASE_URL.rstrip("/") + "/chat/completions"

# ── 同步调用 ─────────────────────────────────────────
def chat(
    messages: list[dict],
    temperature: float = 0.1,
    max_tokens: int = 4096,
    response_format: dict | None = None,
    retries: int = 3,
    delay: float = 1.0,
) -> str:
    """发送单次 chat 请求，返回 assistant 文本内容。"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    if response_format:
        payload["response_format"] = response_format

    for attempt in range(1, retries + 1):
        try:
            resp = requests.post(API_URL, headers=headers, json=payload, timeout=120)
            resp.raise_for_status()
            data = resp.json()
            return data["choices"][0]["message"]["content"]
        except Exception as e:
            if attempt == retries:
                raise
            wait = delay * attempt
            print(f"  [LLM retry {attempt}/{retries}] {e}, waiting {wait:.1f}s ...")
            time.sleep(wait)
    return ""

def chat_json(
    messages: list[dict],
    **kwargs,
) -> dict | list:
    """发送 chat 请求并解析 JSON 响应。"""
    # 让 deepseek 返回 JSON
    kwargs.setdefault("response_format", {"type": "json_object"})
    text = chat(messages, **kwargs)
    # 尝试提取 ```json ... ``` 包裹的内容
    if "```json" in text:
        text = text.split("```json", 1)[1].split("```", 1)[0]
    elif "```" in text:
        text = text.split("```", 1)[1].split("```", 1)[0]
    return json.loads(text.strip())

# ── 批量调用 ─────────────────────────────────────────
def batch_chat(
    prompts: list[list[dict]],
    interval: float = 0.5,
    on_progress=None,
    **kwargs,
) -> list[str]:
    """批量发送 chat 请求，带速率控制。"""
    results = []
    total = len(prompts)
    for i, msgs in enumerate(prompts):
        result = chat(msgs, **kwargs)
        results.append(result)
        if on_progress:
            on_progress(i + 1, total, result)
        if i < total - 1:
            time.sleep(interval)
    return results

def batch_chat_json(
    prompts: list[list[dict]],
    interval: float = 0.5,
    on_progress=None,
    **kwargs,
) -> list[dict | list]:
    """批量发送 chat 请求并解析 JSON。"""
    results = []
    total = len(prompts)
    for i, msgs in enumerate(prompts):
        result = chat_json(msgs, **kwargs)
        results.append(result)
        if on_progress:
            on_progress(i + 1, total, str(result)[:100])
        if i < total - 1:
            time.sleep(interval)
    return results


if __name__ == "__main__":
    # 快速测试
    print(f"API_URL: {API_URL}")
    print(f"MODEL:   {MODEL}")
    resp = chat([{"role": "user", "content": "Say hello in JSON: {\"greeting\": \"...\"}"}])
    print(f"Response: {resp[:200]}")
