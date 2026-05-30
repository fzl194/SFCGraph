# Platform MVP Design

## Decision: Static file serving with product-type split

- FastAPI serves `output/` via StaticFiles, split by UDG/UNC
- Pre-built SQLite index (directory tree + FTS5 search)
- IP whitelist middleware (YAML config)
- Vue 3 + TypeScript frontend, light theme
- Graph layers: API routes + DB schema reserved

## Mount Points

```
/docs/udg/  → output/UDG_Product_Documentation_CH_20.15.2/
/docs/unc/  → output/UNC 20.15.2 产品文档(裸机容器) 05/
```

## Tech Stack

- Backend: FastAPI + SQLite + aiosqlite
- Frontend: Vue 3 + TypeScript + Vite
- Config: YAML (config.yaml)
- Search: SQLite FTS5

## API Routes

```
GET /api/v1/docs/{product}/tree?path=...     # directory tree (lazy load)
GET /api/v1/docs/{product}/content?path=...  # md file content
GET /api/v1/docs/{product}/search?q=...      # full-text search
GET /api/v1/health                           # health check
# Reserved:
GET /api/v1/graphs/{layer}/...               # graph management
```
