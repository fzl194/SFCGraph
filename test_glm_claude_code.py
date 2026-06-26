#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GLM Claude Code 套餐 —— 连通性 & 报错诊断脚本

用途:
    复现 Claude Code 经「智谱 BigModel Anthropic 兼容端点」调用 GLM 的请求,
    把每一次请求的 HTTP 状态码、关键响应头、完整响应体都打印出来,
    用来定位 Claude Code「总是报错」的根因。

链路 (来自 ~/.claude/settings.json 的 env):
    Base URL : https://open.bigmodel.cn/api/anthropic
    协议     : Anthropic Messages  ->  POST {BASE_URL}/v1/messages
    认证     : Authorization: Bearer <ANTHROPIC_AUTH_TOKEN>
    模型     : glm-5.2 / glm-5.2[1M] / glm-4.5-air

配置优先级 (高 -> 低):
    1. 命令行参数  --base-url / --token / --model
    2. 环境变量    ANTHROPIC_BASE_URL / ANTHROPIC_AUTH_TOKEN / ANTHROPIC_MODEL
    3. ~/.claude/settings.json 里的 env 字段
    4. 脚本内置 DEFAULT_*

用法:
    python test_glm_claude_code.py            # 跑全部诊断场景
    python test_glm_claude_code.py --case 3   # 只跑场景 3
    python test_glm_claude_code.py --list     # 列出所有场景
"""

import argparse
import gzip
import json
import os
import sys
import time
import urllib.error
import urllib.request
import zlib

# Windows 中文控制台默认 GBK, 强制 UTF-8, 避免中文响应体 / emoji 打印时崩溃或乱码
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

DEFAULT_BASE_URL = "https://open.bigmodel.cn/api/anthropic"
SETTINGS_PATH = os.path.expanduser("~/.claude/settings.json")
ANTHROPIC_VERSION = "2023-06-01"

# 模拟 Claude Code 真实发送的 anthropic-beta 组合 (用于探测兼容层是否报错)
CC_BETA_HEADERS = ",".join([
    "interleaved-thinking-2025-05-14",
    "fine-grained-tool-streaming-2025-05-14",
    "token-efficient-tools-2025-02-19",
    "prompt-caching-2024-07-31",
])

# 报错对照表 (FAIL 时按状态码打印提示)
DIAGNOSES = {
    401: "token 无效/过期 —— 检查 ANTHROPIC_AUTH_TOKEN 是否正确、是否被禁用。",
    403: "无权限 —— 该账号没有此模型权限, 或被 IP/风控限制。",
    404: "端点或模型名不存在 —— 注意 glm-5.2[1M] 的 [1M] 后缀, 方括号是模型名的一部分。",
    400: "请求体不被兼容层接受 —— 多半是某个 Anthropic 字段/beta 智谱不支持, 看响应体 error.message。",
    413: "请求体过大 —— system/prompt 太长。",
    429: "限流 (RPM/TPM) —— 稍后重试; Claude Code 并发子会话容易触发。",
    500: "智谱侧内部错误 —— 多为兼容层 bug, 携带 Request-ID 找官方。",
    502: "网关错误 —— 智谱侧临时不可用。",
    503: "服务不可用 —— 智谱侧临时不可用。",
    504: "网关超时 —— 上游响应慢。",
}


def mask(token: str) -> str:
    if not token:
        return "<empty>"
    if len(token) <= 10:
        return "***"
    return f"{token[:6]}...{token[-4:]} (len={len(token)})"


def load_settings():
    """从 ~/.claude/settings.json 的 env 字段读取 token / base_url (可能不存在)。"""
    try:
        with open(SETTINGS_PATH, "r", encoding="utf-8") as f:
            env = json.load(f).get("env", {})
        return env.get("ANTHROPIC_AUTH_TOKEN", ""), env.get("ANTHROPIC_BASE_URL", "")
    except Exception:
        return "", ""


def load_config(args):
    s_token, s_base = load_settings()
    base_url = (args.base_url or os.getenv("ANTHROPIC_BASE_URL") or s_base or DEFAULT_BASE_URL).rstrip("/")
    token = args.token or os.getenv("ANTHROPIC_AUTH_TOKEN") or s_token
    return base_url, token


def decode_body(raw: bytes, encoding: str) -> str:
    encoding = (encoding or "").lower()
    try:
        if "gzip" in encoding:
            return gzip.decompress(raw).decode("utf-8", "replace")
        if "deflate" in encoding:
            return zlib.decompress(raw).decode("utf-8", "replace")
    except Exception as e:
        return f"<decode-failed: {e}; raw-len={len(raw)}>"
    return raw.decode("utf-8", "replace")


def http_request(base_url, token, payload, *, stream=False, extra_headers=None, timeout=60):
    """发一次 POST /v1/messages, 返回 (status, headers_dict, body_text, elapsed_s)。
    status < 0 表示网络层错误 (非 HTTP)。"""
    url = f"{base_url}/v1/messages"
    if stream:
        payload = dict(payload, stream=True)
    data = json.dumps(payload).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        # Claude Code 在设置 ANTHROPIC_AUTH_TOKEN 时, 发的是 Authorization: Bearer
        "Authorization": f"Bearer {token}",
        # 智谱兼容层也接受 x-api-key, 双保险
        "x-api-key": token,
        "anthropic-version": ANTHROPIC_VERSION,
        "User-Agent": "glm-cc-diag/1.0",
    }
    if extra_headers:
        headers.update(extra_headers)

    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    t0 = time.time()
    try:
        resp = urllib.request.urlopen(req, timeout=timeout)
        status = resp.getcode()
        hdrs = {k: v for k, v in resp.headers.items()}
        if stream:
            # 逐行读取 SSE, 原样拼接 (不解析, 便于看原始 event)
            chunks = [line.decode("utf-8", "replace") for line in resp]
            body = "".join(chunks)
        else:
            body = decode_body(resp.read(), hdrs.get("Content-Encoding") or hdrs.get("content-encoding"))
        return status, hdrs, body, time.time() - t0
    except urllib.error.HTTPError as e:
        hdrs = {k: v for k, v in e.headers.items()}
        try:
            body = decode_body(e.read(), hdrs.get("Content-Encoding") or hdrs.get("content-encoding"))
        except Exception:
            body = "<no body>"
        return e.code, hdrs, body, time.time() - t0
    except urllib.error.URLError as e:
        return -1, {}, f"URLError: {e.reason}", time.time() - t0
    except Exception as e:
        return -2, {}, f"{type(e).__name__}: {e}", time.time() - t0


def print_result(label, status, hdrs, body, elapsed):
    line = "=" * 76
    print(f"\n{line}")
    print(f"场景: {label}")
    print(f"HTTP {status}  |  耗时 {elapsed:.2f}s")
    rid = next((v for k, v in hdrs.items() if k.lower() in ("x-request-id", "request-id")), None)
    if rid:
        print(f"Request-ID: {rid}")  # 报障给智谱官方用
    ctype = hdrs.get("Content-Type") or hdrs.get("content-type")
    if ctype:
        print(f"Content-Type: {ctype}")
    print("--- 响应体 ---")
    print(body[:2000] if body else "<empty>")
    if body and len(body) > 2000:
        print(f"...[截断, 共 {len(body)} 字符]")
    if status in DIAGNOSES:
        print(f"[诊断提示] {DIAGNOSES[status]}")
    print(line)


def build_cases():
    """返回 [(name, payload, opts)], opts 可含 stream/extra_headers。"""
    return [
        ("1. 连通性 (最简非流式, glm-4.5-air)", {
            "model": "glm-4.5-air",
            "max_tokens": 64,
            "messages": [{"role": "user", "content": "只回复两个字: 你好"}],
        }, {}),
        ("2. 默认主模型非流式 (glm-5.2)", {
            "model": "glm-5.2",
            "max_tokens": 64,
            "messages": [{"role": "user", "content": "1+1=?"}],
        }, {}),
        ("3. 带[1M]后缀 (glm-5.2[1M]) —— Claude Code 实际用的模型名", {
            "model": "glm-5.2[1M]",
            "max_tokens": 64,
            "messages": [{"role": "user", "content": "1+1=?"}],
        }, {}),
        ("4. 流式 SSE (stream=true) —— Claude Code 默认用流式", {
            "model": "glm-5.2[1M]",
            "max_tokens": 64,
            "messages": [{"role": "user", "content": "只回复两个字: 你好"}],
        }, {"stream": True}),
        ("5. 带 system prompt", {
            "model": "glm-5.2[1M]",
            "max_tokens": 64,
            "system": "你是一个极其简洁的中文助手, 每次只回一句话。",
            "messages": [{"role": "user", "content": "你好"}],
        }, {}),
        ("6. 带 tool use —— Claude Code 核心能力", {
            "model": "glm-5.2[1M]",
            "max_tokens": 256,
            "tools": [{
                "name": "get_weather",
                "description": "获取指定城市的天气",
                "input_schema": {
                    "type": "object",
                    "properties": {"city": {"type": "string", "description": "城市名"}},
                    "required": ["city"],
                },
            }],
            "messages": [{"role": "user", "content": "北京天气如何? 请调用 get_weather 工具。"}],
        }, {}),
        ("7. 带 anthropic-beta 头 (Claude Code 风格组合) —— 探测兼容层", {
            "model": "glm-5.2[1M]",
            "max_tokens": 64,
            "system": "助手",
            "messages": [{"role": "user", "content": "你好"}],
        }, {"extra_headers": {"anthropic-beta": CC_BETA_HEADERS}}),
    ]


def main():
    parser = argparse.ArgumentParser(description="GLM Claude Code 套餐诊断脚本")
    parser.add_argument("--base-url", help="覆盖 API base url")
    parser.add_argument("--token", help="覆盖 auth token")
    parser.add_argument("--model", help="(保留) 覆盖默认模型, 场景内模型名仍各自独立")
    parser.add_argument("--model-override", help="强制覆盖所有场景的 model 字段, 例如 --model-override glm-5.2")
    parser.add_argument("--case", type=int, help="只跑指定场景编号")
    parser.add_argument("--list", action="store_true", help="列出所有场景后退出")
    args = parser.parse_args()

    base_url, token = load_config(args)
    print(f"Base URL : {base_url}")
    print(f"Token    : {mask(token)}")
    print(f"Endpoint : {base_url}/v1/messages")
    if not token:
        print("\nERROR: 未取到 token。请用 --token 传入, 或设置 ANTHROPIC_AUTH_TOKEN, "
              "或写入 ~/.claude/settings.json 的 env.ANTHROPIC_AUTH_TOKEN。")
        sys.exit(1)

    cases = build_cases()
    if args.list:
        for c in cases:
            print(c[0])
        return

    results = []
    for idx, (name, payload, opts) in enumerate(cases, 1):
        if args.case and idx != args.case:
            continue
        if args.model_override:
            payload = {**payload, "model": args.model_override}
        status, hdrs, body, elapsed = http_request(
            base_url, token, payload,
            stream=opts.get("stream", False),
            extra_headers=opts.get("extra_headers"),
        )
        print_result(name, status, hdrs, body, elapsed)
        results.append((idx, name, status, elapsed))

    if results:
        print("\n" + "#" * 76)
        print("汇总:")
        all_ok = True
        for idx, name, status, elapsed in results:
            ok = status == 200
            all_ok = all_ok and ok
            flag = "OK  " if ok else "FAIL"
            print(f"  [{flag}] #{idx} HTTP {status:>4}  {elapsed:5.2f}s  {name}")
        print("#" * 76)
        print("结论: 全部通过 [OK]" if all_ok else "结论: 存在失败 [FAIL] —— 看上方对应场景的「响应体」和「诊断提示」定位。")
        sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
