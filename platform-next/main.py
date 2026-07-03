"""SFCGraph Platform-Next — FastAPI entry point."""
import sys
from pathlib import Path
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# Ensure project root is on sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from shared.config import load_config
from feature_graph.router import router as feature_router
from command_graph.router import router as command_router
from business_graph.router import router as business_router
from task_graph.router import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_config()
    yield


app = FastAPI(title="SFCGraph Platform", version="2.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(feature_router)
app.include_router(command_router)
app.include_router(business_router)
app.include_router(task_router)

# Serve frontend static files in production
frontend_dist = Path(__file__).resolve().parent / "frontend" / "dist"
if frontend_dist.exists():
    app.mount("/", StaticFiles(directory=str(frontend_dist), html=True), name="frontend")


if __name__ == "__main__":
    import uvicorn

    cfg = load_config()
    host = cfg.get("server", {}).get("host", "0.0.0.0")
    port = cfg.get("server", {}).get("port", 8000)
    uvicorn.run("main:app", host=host, port=port, reload=True)
