"""鉴权中间件：单一共享 KEY（环境变量 GAP_API_KEY）。

- 保护所有 /api/* 请求：须带 X-API-Key header 且等于 GAP_API_KEY，否则 401。
- GAP_API_KEY 未配置 → 旁路（开发友好）。
- 非 /api/ 路径不拦截。
- KEY 取值绝不 echo（spec §6）。
- dispatch 运行时读 config.API_KEY（非 import 期绑定），便于测试 monkeypatch。
"""
import logging

from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from .. import config

logger = logging.getLogger(__name__)
if not config.API_KEY:
    logger.warning("鉴权未启用：未配置环境变量 GAP_API_KEY（生产请配置）")


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        key = config.API_KEY  # 运行时读取，测试可 monkeypatch.setattr(config, "API_KEY", ...)
        if key and request.url.path.startswith("/api/"):
            if request.headers.get("X-API-Key", "") != key:
                return JSONResponse(
                    status_code=401,
                    content={"detail": "missing or invalid api key"},
                )
        return await call_next(request)
