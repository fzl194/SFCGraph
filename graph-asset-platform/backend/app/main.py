"""FastAPI 应用入口：lifespan 预热建索引 + CORS + 挂载 routers + 静态托管前端 dist。

- API 前缀 ``/api/v1``。
- 前端 ``frontend/dist`` 构建产物（如存在）挂在根路径下（SPA 兜底）。
"""
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .routers import assets as assets_router
from .routers import objects as objects_router
from .service import get_service


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动预热：构造单例 → 建索引（assets 目录不存在时 Store 会 mkdir）
    get_service()
    yield


app = FastAPI(title="Graph Asset Platform", version="0.1.0", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(assets_router.router, prefix="/api/v1")
app.include_router(objects_router.router, prefix="/api/v1")

# 前端静态托管（dist 可能尚未构建，不存在则不挂载）
_dist = Path(__file__).resolve().parents[2] / "frontend" / "dist"
if _dist.exists():
    app.mount("/", StaticFiles(directory=_dist, html=True), name="spa")
