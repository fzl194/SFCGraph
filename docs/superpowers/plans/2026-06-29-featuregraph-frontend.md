# 特性图谱前端展示 Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在 platform-next 重建特性图谱前端展示（参考命令图谱三级结构），数据源用新 FeatureGraph JSONL 流水线。

**Architecture:** 后端 `feature_graph/service.py` 复刻 `command_graph/service.py`（扫描 JSONL 进内存 + _adjacency 统一图 + BFS 子图），前端 4 个 Vue 页面复刻 command_graph（首页统计→网元版本两tab→详情左右侧）。多 md 来自 `source_evidence_ids`（设计态恢复为全部 md），特性关系图复用统一 `{nodes,edges}` 模型。

**Tech Stack:** FastAPI（后端）、Vue 3 + element-plus + vis-network（前端）、pytest（后端测试）。

**Spec:** `docs/superpowers/specs/2026-06-29-featuregraph-frontend-design.md`

**用户约束:** 直接 master 提交，不开分支/worktree。conventional commits，无 Co-Authored-By。

---

## File Structure

**设计态改动（FeatureGraph/）：**
- Modify: `FeatureGraph/builder/steps/feature.py` — source_evidence_ids 恢复为全部 md

**后端新建（platform-next/feature_graph/）：**
- Create: `platform-next/feature_graph/__init__.py`
- Create: `platform-next/feature_graph/service.py` — 扫描 JSONL + _adjacency + 接口
- Create: `platform-next/feature_graph/router.py` — REST 端点
- Modify: `platform-next/main.py` — 注册 feature_router
- Modify: `platform-next/config.yaml` — feature_graph 块（assets_root/doc_root）

**前端新建（platform-next/frontend/src/feature_graph/）：**
- Create: `FeatureOverview.vue` — 首页统计 + 网元版本入口（复刻 CommandOverview）
- Create: `FeatureListPage.vue` — 网元版本页两 tab（特性/license）（复刻 CommandList + tab）
- Create: `FeatureDetail.vue` — 特性详情左右侧（复刻 CommandDetail + 多md tab）
- Create: `LicenseDetail.vue` — license 详情左右侧
- Create: `FeatureRelationGraph.vue` — 特性关系图（vis-network，独立配置）
- Modify: `frontend/src/api.ts` — featureGraphApi 端点
- Modify: `frontend/src/router.ts` — /feature 路由

**复用不变：** `shared/DocViewer.vue`（已支持 feature-graph base path）、`shared/markdown.ts`

---

## Chunk 1: 设计态前置 + 后端 service/router

### Task 1: 设计态 source_evidence_ids 恢复为全部 md

**Files:**
- Modify: `FeatureGraph/builder/steps/feature.py`
- Test: `FeatureGraph/tests/test_feature.py`（已有，加断言）

**背景:** 当前 source_evidence_ids 收紧为仅概述路径，多 md 展示需要全部 md。`find_overview_md` 返回的 `doc_assets` 含该特性所有 md（overview/activation/principle/reference/...），把全部 path 写入 source_evidence_ids。

- [ ] **Step 1: 写集成测试（真实断言，非占位）**

在 `FeatureGraph/tests/test_feature.py` 加集成测试。构造一个临时 corpus 目录，含某特性的 3 个 md（概述+激活+原理），跑 feature step，断言 source_evidence_ids 含全部 3 个 md：

```python
def test_source_evidence_ids_contains_all_md(tmp_path, monkeypatch):
    """feature step 应把该特性全部 md（概述+激活+原理）写入 source_evidence_ids，不只概述。"""
    # Arrange: corpus/{特性目录}/ 下放 3 个 md
    feat_dir = tmp_path / "corpus" / "GWFD-999999 测试特性"
    feat_dir.mkdir(parents=True)
    (feat_dir / "GWFD-999999 测试特性特性概述_1.md").write_text(
        "# GWFD-999999\n\n#### [定义]\n\n测试定义\n\n#### [可获得性]\n\n测试\n", encoding="utf-8")
    (feat_dir / "激活测试特性_2.md").write_text("# 激活\n", encoding="utf-8")
    (feat_dir / "实现原理_3.md").write_text("# 原理\n", encoding="utf-8")
    # Act: 调 find_overview_md + 构造（或直接调 feature step 的核心逻辑）
    from builder.core.overview import find_overview_md
    fps = [str(p.relative_to(tmp_path)) for p in feat_dir.glob("*.md")]
    overview_paths, doc_assets = find_overview_md("GWFD-999999", fps, tmp_path)
    # Assert: doc_assets 含全部 3 个 md
    all_paths = [fp for fp, _ in doc_assets]
    assert len(all_paths) == 3, f"应含全部3个md, 实际 {len(all_paths)}"
    # feature step 应把 all_paths 写入 source_evidence_ids（步骤2实现后）
```

- [ ] **Step 2: 修改 feature step — 所有分支 source_evidence_ids 用 doc_assets 全部 path**

`FeatureGraph/builder/steps/feature.py`。`doc_assets` 是 `find_overview_md` 返回的第二项（含该特性全部 md），在叶节点处理块顶部已解构（`overview_paths, doc_assets = find_overview_md(...)`），yes/no_overview/empty/file_missing/多概述 各分支都在作用域内。

统一改法（所有写 source_evidence_ids 的地方）：
```python
all_doc_paths = [fp for fp, _ in doc_assets]   # 该特性全部 md
```

(2a) **多概述无 variant 回退分支**（当前 `all_evidence = list(overview_paths)`，只概览）改为：
```python
all_evidence = [fp for fp, _ in doc_assets]   # 全部 md，不只 overview_paths
```

(2b) **单概述 yes 分支**（当前 `node["source_evidence_ids"] = all_evidence if all_evidence else [primary_overview]`）改为：
```python
node["source_evidence_ids"] = all_doc_paths if all_doc_paths else [primary_overview]
```

(2c) **no_overview / empty / file_missing 分支**也用 `all_doc_paths`（当前用 `[primary_overview]` 或 `[]`）。

- [ ] **Step 3: 多概述父节点 source_evidence_ids 用全部 md；子特性第一版简化声明**

(3a) 多概述**父**节点：`_build_multi_overview_nodes` 传入 doc_assets（父特性全部 md），父节点 source_evidence_ids = 全部 md（含所有代际的所有 md，作索引）：
```python
all_doc_paths = [fp for fp, _ in doc_assets]
multi_nodes = _build_multi_overview_nodes(
    seed, overview_paths, variant_dims, doc_assets, project_root, nf, version)
# build_multi_overview_parent 的 source_evidence_ids 用 all_doc_paths（不只 overview_paths）
```

(3b) **子特性节点第一版简化（声明）**：`build_subfeature_node` 当前 `source_evidence_ids: [overview_path]`（代际概述）。**第一版保持**（子特性只展示代际概述 md，不展开代际目录的全部 md）——因为子特性的多 md 需要单独扫描代际子目录（GWFD-010101/2_3G会话管理/*.md），第一版不实现。子特性是少数（代际细分），多数特性（单概述）已支持全部 md。后续如需可补 `_build_multi_overview_nodes` 按代际目录扫描。

- [ ] **Step 4: 重跑全量验证**

```bash
cd FeatureGraph
rm -f data/UDG/20.15.2/features.jsonl data/UNC/20.15.2/features.jsonl
python build_all.py UDG 20.15.2 feature
python build_all.py UNC 20.15.2 feature
python -c "import json; f=[json.loads(l) for l in open('data/UDG/20.15.2/features.jsonl',encoding='utf-8')]; g=[x for x in f if x['feature_code']=='GWFD-020301'][0]; print('GWFD-020301 source_evidence_ids:', len(g['source_evidence_ids']), '条'); [print(' ',p.split('/')[-1][:40]) for p in g['source_evidence_ids']]"
```
Expected: GWFD-020301 source_evidence_ids ≥3 条（概述/参考/原理/部署等，不只 1 条概述）

- [ ] **Step 5: Commit**

```bash
git add FeatureGraph/builder/steps/feature.py FeatureGraph/tests/test_feature.py
git commit -m "fix(featuregraph): source_evidence_ids恢复为全部md(支撑前端多md展示)"
```

---

### Task 2: 后端 feature_graph/service.py（复刻 command_graph/service.py）

**Files:**
- Create: `platform-next/feature_graph/__init__.py`（空）
- Create: `platform-next/feature_graph/service.py`
- 参考: `platform-next/command_graph/service.py`（_load/get_stats/list/get_xxx/_load_graph/get_subgraph）

**核心结构:** 扫描 `FeatureGraph/data/{nf}/{version}/*.jsonl`，按 (nf,version) 分桶，建 _adjacency 统一图。

- [ ] **Step 1: 写 service.py 骨架 + 数据加载**

```python
"""Feature graph data service — scans FeatureGraph/data and serves it.

Assets root layout: {assets_root}/{nf}/{version}/{features|licenses|feature_relations|feature_requires_license}.jsonl
"""
import json
from pathlib import Path
from shared.config import get_config


def _make_feature_id(nf: str, version: str, code: str) -> str:
    return f"{nf}@{version}@Feature@{code}"


def _make_license_id(nf: str, version: str, code: str) -> str:
    return f"{nf}@{version}@License@{code}"


class FeatureGraphService:
    def __init__(self):
        platform_root = Path(__file__).resolve().parent.parent
        cfg = get_config().get("feature_graph", {})
        assets_root = cfg.get("assets_root")
        doc_root = cfg.get("doc_root", "..")
        self._assets_root = (platform_root / assets_root).resolve() if assets_root else None
        self._doc_root = (platform_root / doc_root).resolve()
        # (nf,version) -> records
        self._features: dict[tuple[str, str], list[dict]] = {}
        self._licenses: dict[tuple[str, str], list[dict]] = {}
        self._relations: dict[tuple[str, str], list[dict]] = {}
        self._req_lic: dict[tuple[str, str], list[dict]] = {}
        self._feat_by_id: dict[str, dict] = {}
        self._lic_by_id: dict[str, dict] = {}
        self._adjacency: dict[str, dict] = {}
        self._load()
        self._load_graph()

    def _load(self) -> None:
        if not self._assets_root or not self._assets_root.exists():
            return
        for fp in sorted(self._assets_root.glob("*/*/*.jsonl")):
            try:
                nf = fp.parent.parent.name
                version = fp.parent.name
            except IndexError:
                continue
            object_type = fp.stem
            target = {"features": self._features, "licenses": self._licenses,
                      "feature_relations": self._relations,
                      "feature_requires_license": self._req_lic}.get(object_type)
            if target is None:
                continue
            bucket = target.setdefault((nf, version), [])
            with fp.open(encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        rec = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    bucket.append(rec)
                    if object_type == "features":
                        self._feat_by_id[rec.get("id", "")] = rec
                    elif object_type == "licenses":
                        self._lic_by_id[rec.get("id", "")] = rec
```

- [ ] **Step 2: 写 get_stats（首页统计）**

```python
    def get_stats(self) -> dict:
        feat_counts: dict[tuple[str, str], int] = {k: len(v) for k, v in self._features.items()}
        lic_counts: dict[tuple[str, str], int] = {k: len(v) for k, v in self._licenses.items()}
        rel_counts: dict[tuple[str, str], int] = {k: len(v) for k, v in self._relations.items()}
        ne_versions = []
        all_keys = sorted(set(feat_counts) | set(lic_counts) | set(rel_counts))
        for (nf, ver) in all_keys:
            ne_versions.append({
                "nf": nf, "version": ver,
                "feature_count": feat_counts.get((nf, ver), 0),
                "license_count": lic_counts.get((nf, ver), 0),
                "relation_count": rel_counts.get((nf, ver), 0),
            })
        return {
            "total_features": sum(feat_counts.values()),
            "total_licenses": sum(lic_counts.values()),
            "total_relations": sum(rel_counts.values()),
            "ne_versions": ne_versions,
        }
```

- [ ] **Step 3: 写 list_features / list_licenses / get_feature / get_license**

```python
    @staticmethod
    def _slim_feature(r: dict) -> dict:
        return {
            "feature_code": r.get("feature_code"), "name": r.get("name"),
            "feature_category": r.get("feature_category"),
            "config_relevance": r.get("config_relevance"),
            "applicable_nf": r.get("applicable_nf", []),
            "has_overview": r.get("has_overview"),
        }

    def list_features(self, nf: str, version: str, search: str | None = None,
                      feature_category: str | None = None, page: int = 1, size: int = 50) -> dict:
        bucket = self._features.get((nf, version), [])
        s = (search or "").lower()
        filtered = []
        for r in bucket:
            if feature_category and r.get("feature_category") != feature_category:
                continue
            if s:
                hay = " ".join([r.get("feature_code") or "", r.get("name") or ""]).lower()
                if s not in hay:
                    continue
            filtered.append(r)
        filtered.sort(key=lambda r: r.get("feature_code") or "")
        total = len(filtered)
        start = (page - 1) * size
        items = [self._slim_feature(r) for r in filtered[start:start + size]]
        return {"total": total, "page": page, "size": size, "items": items}

    @staticmethod
    def _slim_license(r: dict) -> dict:
        return {
            "license_code": r.get("license_code"), "name": r.get("name"),
            "control_item_id": r.get("control_item_id"),
            "applicable_nf": r.get("applicable_nf", []),
            "control_item_type": r.get("control_item_type"),
        }

    def list_licenses(self, nf: str, version: str, search: str | None = None,
                      page: int = 1, size: int = 50) -> dict:
        bucket = self._licenses.get((nf, version), [])
        s = (search or "").lower()
        filtered = [r for r in bucket if (not s) or s in " ".join(
            [r.get("license_code") or "", r.get("name") or ""]).lower()]
        filtered.sort(key=lambda r: r.get("license_code") or "")
        total = len(filtered)
        start = (page - 1) * size
        items = [self._slim_license(r) for r in filtered[start:start + size]]
        return {"total": total, "page": page, "size": size, "items": items}

    def get_feature(self, nf: str, version: str, code: str) -> dict | None:
        return self._feat_by_id.get(_make_feature_id(nf, version, code))

    def get_license(self, nf: str, version: str, code: str) -> dict | None:
        return self._lic_by_id.get(_make_license_id(nf, version, code))
```

- [ ] **Step 4: 写 get_feature_docs / get_feature_relations / get_feature_licenses / get_license_features**

```python
    def get_feature_docs(self, nf: str, version: str, code: str) -> list[dict]:
        """读 features.jsonl 的 source_evidence_ids（全部 md），title 从文件名解析。"""
        rec = self.get_feature(nf, version, code)
        if not rec:
            return []
        out = []
        for path in rec.get("source_evidence_ids") or []:
            fn = path.rsplit("/", 1)[-1].rsplit("\\", 1)[-1]
            title = fn.rsplit("_", 1)[0] if "_" in fn else fn  # 去 _数字hash 后缀
            out.append({"doc_path": path, "doc_title": title})
        return out

    def get_feature_relations(self, nf: str, version: str, code: str) -> list[dict]:
        fid = _make_feature_id(nf, version, code)
        out = []
        for e in self._relations.get((nf, version), []):
            if e.get("source_id") == fid or e.get("target_id") == fid:
                # 解析对端 + relation_type + interaction_note
                peer_id = e.get("target_id") if e.get("source_id") == fid else e.get("source_id")
                peer_code = peer_id.rsplit("@", 1)[-1] if peer_id else ""
                peer_rec = self._feat_by_id.get(peer_id, {})
                out.append({
                    "peer_code": peer_code,
                    "peer_name": peer_rec.get("name", peer_code) if peer_rec else peer_code,
                    "direction": "out" if e.get("source_id") == fid else "in",
                    "relation_type": e.get("relation_type"),
                    "interaction_note": e.get("interaction_note", ""),
                    "dangling": peer_id not in self._feat_by_id,  # 悬空 target 标记
                })
        return out

    def get_feature_licenses(self, nf: str, version: str, code: str) -> list[dict]:
        fid = _make_feature_id(nf, version, code)
        out = []
        for e in self._req_lic.get((nf, version), []):
            if e.get("source_id") == fid:
                lic = self._lic_by_id.get(e.get("target_id", ""), {})
                out.append({
                    "license_code": e.get("license_code"),
                    "license_name": lic.get("name", ""),
                    "control_item_id": e.get("control_item_id", ""),
                })
        return out

    def get_license_features(self, nf: str, version: str, code: str) -> list[str]:
        """反查哪些特性需要此 license（从 requires_license 边）。"""
        lid = _make_license_id(nf, version, code)
        out = []
        for e in self._req_lic.get((nf, version), []):
            if e.get("target_id") == lid:
                out.append(e.get("feature_code", ""))
        return [c for c in out if c]
```

- [ ] **Step 5: 写 _load_graph + get_feature_graph（统一图，复刻 command_graph get_subgraph）**

```python
    def _load_graph(self) -> None:
        adj: dict[str, dict] = {}

        def add_node(node_id, ntype, label, props):
            if not node_id or node_id in adj:
                return
            adj[node_id] = {
                "node": {"id": node_id, "type": ntype, "label": label or node_id, "properties": props or {}},
                "out": [], "in": [],
            }

        def add_edge(from_id, to_id, etype, props):
            if not from_id or not to_id:
                return
            add_node(from_id, None, None, {})
            add_node(to_id, None, None, {})
            adj[from_id]["out"].append((to_id, etype, props))
            adj[to_id]["in"].append((from_id, etype, props))

        for bucket in self._features.values():
            for r in bucket:
                add_node(r.get("id"), "feature", r.get("name"), {"feature_code": r.get("feature_code"), "feature_category": r.get("feature_category")})
        for bucket in self._licenses.values():
            for r in bucket:
                add_node(r.get("id"), "license", r.get("name"), {"license_code": r.get("license_code")})
        for bucket in self._relations.values():
            for e in bucket:
                add_edge(e.get("source_id"), e.get("target_id"), e.get("relation_type"),
                         {"interaction_note": e.get("interaction_note", "")})
        for bucket in self._req_lic.values():
            for e in bucket:
                add_edge(e.get("source_id"), e.get("target_id"), "requires_license", {})
        self._adjacency = adj

    def get_feature_graph(self, nf: str, version: str, code: str,
                          hops: int = 1, edge_types: list[str] | None = None) -> dict:
        """BFS 取特性 N 跳子图（只在该 nf/version 的关系边内遍历）。"""
        center = _make_feature_id(nf, version, code)
        if center not in self._adjacency:
            return {"nodes": [], "edges": []}
        # 限定该 nf/version 的特性间关系边（feature_relations）；
        # 不含 requires_license 边——license 关联在 license tab 单独展示，不进特性关系图
        rel_set = set()
        for e in self._relations.get((nf, version), []):
            rel_set.add((e.get("source_id"), e.get("target_id"), e.get("relation_type")))
        edge_set = set(edge_types) if edge_types else None
        nodes_seen: dict[str, dict] = {center: self._adjacency[center]["node"]}
        edge_seen: set[str] = set()
        edges_out: list[dict] = []
        frontier = [center]
        for _ in range(hops):
            nxt: list[str] = []
            for nid in frontier:
                entry = self._adjacency.get(nid)
                if not entry:
                    continue
                candidates = ([(to, nid, to, et, pr) for (to, et, pr) in entry["out"]]
                              + [(frm, frm, nid, et, pr) for (frm, et, pr) in entry["in"]])
                for other, ef, et_, etype, props in candidates:
                    if (ef, et_, etype) not in rel_set:
                        continue  # 只走该 nf/version 的关系边
                    if edge_set is not None and etype not in edge_set:
                        continue
                    key = f"{ef}\x1f{et_}\x1f{etype}"
                    if key in edge_seen:
                        continue
                    edge_seen.add(key)
                    edges_out.append({"from": ef, "to": et_, "type": etype, "properties": props})
                    if other not in nodes_seen:
                        nodes_seen[other] = self._adjacency[other]["node"]
                        nxt.append(other)
            frontier = nxt
        return {"nodes": list(nodes_seen.values()), "edges": edges_out}

    # ---- md 内容（复用 command_graph 的 resolve_doc_path 容忍 output/ 前缀逻辑）----
    def resolve_doc_path(self, rel_path: str) -> Path | None:
        rel = rel_path.replace('\\', '/')
        if rel.startswith('output/'):
            full = (self._doc_root / rel).resolve()
        else:
            full = (self._doc_root / 'output' / rel).resolve()
        output_root = (self._doc_root / 'output').resolve()
        if not str(full).startswith(str(output_root)):
            return None
        if full.exists() and full.is_file():
            return full
        return None

    def get_doc_content(self, rel_path: str) -> str:
        full = self.resolve_doc_path(rel_path)
        if not full:
            return ""
        return full.read_text(encoding="utf-8")


_service: FeatureGraphService | None = None


def get_service() -> FeatureGraphService:
    global _service
    if _service is None:
        _service = FeatureGraphService()
    return _service
```

- [ ] **Step 6: Commit**

```bash
cd d:/mywork/KnowledgeBase/SFCGraph
git add platform-next/feature_graph/__init__.py platform-next/feature_graph/service.py
git commit -m "feat(platform-next): feature_graph service.py(扫描JSONL+_adjacency+接口, 复刻command_graph)"
```

---

### Task 3: 后端 router.py（复刻 command_graph/router.py）

**Files:**
- Create: `platform-next/feature_graph/router.py`
- 参考: `platform-next/command_graph/router.py`

- [ ] **Step 1: 写 router.py**

```python
"""Feature graph API routes."""
from fastapi import APIRouter, Query
from fastapi.responses import FileResponse
from .service import get_service

router = APIRouter(prefix="/api/v1/feature-graph", tags=["feature-graph"])


@router.get("/stats")
def get_stats():
    return get_service().get_stats()


@router.get("/features")
def list_features(
    nf: str = Query(...), version: str = Query(...),
    search: str | None = Query(None), category: str | None = Query(None),
    page: int = Query(1, ge=1), size: int = Query(50, ge=1, le=200),
):
    return get_service().list_features(nf, version, search, category, page, size)


@router.get("/licenses")
def list_licenses(
    nf: str = Query(...), version: str = Query(...),
    search: str | None = Query(None),
    page: int = Query(1, ge=1), size: int = Query(50, ge=1, le=200),
):
    return get_service().list_licenses(nf, version, search, page, size)


@router.get("/feature")
def get_feature(nf: str = Query(...), version: str = Query(...), code: str = Query(...)):
    rec = get_service().get_feature(nf, version, code)
    return rec or {"error": "Feature not found", "code": code}


@router.get("/feature-docs")
def get_feature_docs(nf: str = Query(...), version: str = Query(...), code: str = Query(...)):
    return {"docs": get_service().get_feature_docs(nf, version, code)}


@router.get("/feature-relations")
def get_feature_relations(nf: str = Query(...), version: str = Query(...), code: str = Query(...)):
    return {"relations": get_service().get_feature_relations(nf, version, code)}


@router.get("/feature-licenses")
def get_feature_licenses(nf: str = Query(...), version: str = Query(...), code: str = Query(...)):
    return {"licenses": get_service().get_feature_licenses(nf, version, code)}


@router.get("/feature-graph")
def get_feature_graph(
    nf: str = Query(...), version: str = Query(...), code: str = Query(...),
    hops: int = Query(1, ge=1, le=3), edge_types: str | None = Query(None),
):
    types = [t.strip() for t in edge_types.split(",") if t.strip()] if edge_types else None
    return get_service().get_feature_graph(nf, version, code, hops, types)


@router.get("/license")
def get_license(nf: str = Query(...), version: str = Query(...), code: str = Query(...)):
    rec = get_service().get_license(nf, version, code)
    return rec or {"error": "License not found", "code": code}


@router.get("/license-features")
def get_license_features(nf: str = Query(...), version: str = Query(...), code: str = Query(...)):
    return {"feature_codes": get_service().get_license_features(nf, version, code)}


@router.get("/doc-content")
def get_doc_content(path: str = Query(...)):
    return {"content": get_service().get_doc_content(path), "path": path}


@router.get("/file")
def serve_file(path: str = Query(...)):
    full = get_service().resolve_doc_path(path)
    if not full:
        return {"error": "Access denied or file not found"}
    content_types = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
                     ".gif": "image/gif", ".svg": "image/svg+xml", ".webp": "image/webp"}
    media_type = content_types.get(full.suffix.lower(), "application/octet-stream")
    return FileResponse(str(full), media_type=media_type)
```

- [ ] **Step 2: Commit**

```bash
git add platform-next/feature_graph/router.py
git commit -m "feat(platform-next): feature_graph router.py(REST端点, 复刻command_graph)"
```

---

### Task 4: config + main 注册 + 端到端验证

**Files:**
- Modify: `platform-next/config.yaml`（加 feature_graph 块）
- Modify: `platform-next/main.py`（注册 feature_router）

- [ ] **Step 1: config.yaml 加 feature_graph 块**

在 `command_graph` 块后加：
```yaml
feature_graph:
  assets_root: "../FeatureGraph/data"
  doc_root: ".."
```

- [ ] **Step 2: main.py 注册 feature_router**

```python
from feature_graph.router import router as feature_router
from command_graph.router import router as command_router
from business_graph.router import router as business_router
# ...
app.include_router(feature_router)
app.include_router(command_router)
app.include_router(business_router)
```

- [ ] **Step 3: 启动后端 + curl 验证**

```bash
cd platform-next
python main.py &
sleep 2
curl -s "http://localhost:8000/api/v1/feature-graph/stats" | python -m json.tool | head -20
curl -s "http://localhost:8000/api/v1/feature-graph/features?nf=UDG&version=20.15.2&size=3" | python -m json.tool | head -20
curl -s "http://localhost:8000/api/v1/feature-graph/feature?nf=UDG&version=20.15.2&code=GWFD-020301" | python -m json.tool | head -10
curl -s "http://localhost:8000/api/v1/feature-graph/feature-docs?nf=UDG&version=20.15.2&code=GWFD-020301" | python -m json.tool
curl -s "http://localhost:8000/api/v1/feature-graph/feature-graph?nf=UDG&version=20.15.2&code=GWFD-020301" | python -m json.tool | head -20
kill %1
```
Expected: stats 返回 total_features≈313/total_licenses=187；features 返回 3 条 slim；feature 返回 GWFD-020301 全字段；feature-docs 返回 ≥3 个 md；feature-graph 返回 {nodes,edges}。

- [ ] **Step 4: Commit**

```bash
git add platform-next/config.yaml platform-next/main.py
git commit -m "feat(platform-next): 注册feature_graph(config+main, 端到端验证通过)"
```

---

## Chunk 2: 前端基础设施 + FeatureOverview + FeatureListPage

### Task 5: 前端 api.ts 加 featureGraphApi

**Files:**
- Modify: `platform-next/frontend/src/api.ts`
- 参考: command_graph 部分的 commandGraphApi

- [ ] **Step 1: 加 featureGraphApi 块**

在 api.ts 的 commandGraphApi 后加：
```typescript
export const featureGraphApi = {
  stats: `${BASE}/feature-graph/stats`,
  features: (nf: string, version: string) => `${BASE}/feature-graph/features?nf=${nf}&version=${version}`,
  licenses: (nf: string, version: string) => `${BASE}/feature-graph/licenses?nf=${nf}&version=${version}`,
  feature: (nf: string, version: string, code: string) =>
    `${BASE}/feature-graph/feature?nf=${nf}&version=${version}&code=${code}`,
  featureDocs: (nf: string, version: string, code: string) =>
    `${BASE}/feature-graph/feature-docs?nf=${nf}&version=${version}&code=${code}`,
  featureRelations: (nf: string, version: string, code: string) =>
    `${BASE}/feature-graph/feature-relations?nf=${nf}&version=${version}&code=${code}`,
  featureLicenses: (nf: string, version: string, code: string) =>
    `${BASE}/feature-graph/feature-licenses?nf=${nf}&version=${version}&code=${code}`,
  featureGraph: (nf: string, version: string, code: string, hops = 1) =>
    `${BASE}/feature-graph/feature-graph?nf=${nf}&version=${version}&code=${code}&hops=${hops}`,
  license: (nf: string, version: string, code: string) =>
    `${BASE}/feature-graph/license?nf=${nf}&version=${version}&code=${code}`,
  licenseFeatures: (nf: string, version: string, code: string) =>
    `${BASE}/feature-graph/license-features?nf=${nf}&version=${version}&code=${code}`,
  docContent: (path: string) => `${BASE}/feature-graph/doc-content?path=${encodeURIComponent(path)}`,
  file: (path: string) => `${BASE}/feature-graph/file?path=${encodeURIComponent(path)}`,
}
```

- [ ] **Step 2: Commit**

```bash
git add platform-next/frontend/src/api.ts
git commit -m "feat(platform-next/frontend): api.ts加featureGraphApi端点"
```

---

### Task 6: FeatureOverview.vue（首页统计 + 网元版本入口，复刻 CommandOverview）

**Files:**
- Create: `platform-next/frontend/src/feature_graph/FeatureOverview.vue`
- 参考: `platform-next/frontend/src/command_graph/CommandOverview.vue`

- [ ] **Step 1: 写 FeatureOverview.vue**

参考 CommandOverview.vue 的卡片网格布局，统计量换特性维度（特性/license/关系数）。关键结构：
- `<script setup>`：onMounted 调 `featureGraphApi.stats`，存 stats（total_features/total_licenses/total_relations/ne_versions）
- template：顶部 3 个统计卡片 + ne_versions 卡片网格（每卡片 nf@version + 特性数/license数/关系数徽章，点击 `router.push('/feature/'+nf+'/'+version)`）
- style：复用 CommandOverview 的卡片样式（.cg-nv-grid 等 token）

完整代码复刻 CommandOverview.vue 改：API 换 featureGraphApi.stats、字段换 feature_count/license_count/relation_count、路由前缀 /feature。

- [ ] **Step 2: 浏览器验证**（Chunk 4 一起验证，先写代码）

- [ ] **Step 3: Commit**

```bash
git add platform-next/frontend/src/feature_graph/FeatureOverview.vue
git commit -m "feat(platform-next/frontend): FeatureOverview首页统计+网元版本入口"
```

---

### Task 7: FeatureIndex.vue + router.ts 加 /feature 路由（对齐命令图谱嵌套模式）

**Files:**
- Create: `platform-next/frontend/src/feature_graph/FeatureIndex.vue`（导航包装，对齐 CommandIndex）
- Modify: `platform-next/frontend/src/router.ts`

- [ ] **Step 1: 创建 FeatureIndex.vue（导航包装）**

参考 `command_graph/CommandIndex.vue`：含特性图谱导航（面包屑/返回首页）+ `<router-view/>`。最小包装（子路由 Overview/ListPage 在此渲染；Detail/LicenseDetail 是独立路由不经过此包装，对齐命令图谱 CommandDetail 独立）。

```vue
<template>
  <div class="feature-index">
    <nav class="feature-nav"><!-- 返回首页 / 面包屑，参考 CommandIndex --></nav>
    <router-view />
  </div>
</template>
<script setup lang="ts"></script>
```

- [ ] **Step 2: 加嵌套路由（单一一套，对齐 command_graph 的 Index+children+独立详情模式）**

```typescript
// router.ts，在 command-graph 路由块后加
{
  path: '/feature',
  component: () => import('./feature_graph/FeatureIndex.vue'),
  children: [
    { path: '', name: 'feature-overview', component: () => import('./feature_graph/FeatureOverview.vue') },
    { path: ':nf/:version', name: 'feature-list', component: () => import('./feature_graph/FeatureListPage.vue') },
  ],
},
{
  path: '/feature/:nf/:version/feature/:code',
  name: 'feature-detail',
  component: () => import('./feature_graph/FeatureDetail.vue'),
},
{
  path: '/feature/:nf/:version/license/:code',
  name: 'license-detail',
  component: () => import('./feature_graph/LicenseDetail.vue'),
},
```

- [ ] **Step 3: Commit**

```bash
git add platform-next/frontend/src/feature_graph/FeatureIndex.vue platform-next/frontend/src/router.ts
git commit -m "feat(platform-next/frontend): FeatureIndex包装+嵌套路由(对齐command_graph模式)"
```

---

### Task 8: FeatureListPage.vue（网元版本页两 tab，复刻 CommandList）

**Files:**
- Create: `platform-next/frontend/src/feature_graph/FeatureListPage.vue`
- 参考: `platform-next/frontend/src/command_graph/CommandList.vue`

- [ ] **Step 1: 写 FeatureListPage.vue**

参考 CommandList.vue，加顶部两 tab（特性 / license）。关键结构：
- `<script setup>`：route.params 取 nf/version，两个 tab 各自的列表加载（features/licenses）、搜索、分页
- template：`<el-tabs>` 两 pane：特性 tab（表格 feature_code/name/feature_category/config_relevance/applicable_nf，点行跳 feature-detail）、license tab（表格 license_code/name/control_item_id，点行跳 license-detail）
- 顶部面包屑：nf@version + 返回首页链接

完整代码复刻 CommandList.vue 改：API 换 featureGraphApi.features/licenses、表格列换特性字段、加 el-tabs、点行跳 `/feature/:nf/:version/feature/:code` 或 `.../license/:code`。

- [ ] **Step 2: Commit**

```bash
git add platform-next/frontend/src/feature_graph/FeatureListPage.vue
git commit -m "feat(platform-next/frontend): FeatureListPage两tab(特性/license列表)"
```

---

## Chunk 3: FeatureDetail + LicenseDetail

### Task 9: FeatureDetail.vue（左右侧 + 多md tab，复刻 CommandDetail）

**Files:**
- Create: `platform-next/frontend/src/feature_graph/FeatureDetail.vue`
- 参考: `platform-next/frontend/src/command_graph/CommandDetail.vue`（左右侧布局 + DocViewer + sections 数据驱动）

- [ ] **Step 1: 写 FeatureDetail.vue 骨架（左右侧 + 左侧 3 tab）**

复刻 CommandDetail.vue 的 `.cmd-split` 左右侧 + 可拖拽分隔条（CSS 直接复用 cmd-* 类）。

左侧 `<el-tabs>`：
- `特性` tab：数据驱动 sections（LABEL_MAP 换特性字段：feature_code/feature_category/config_relevance/catalog_section/applicable_nf/nf_support_map/first_release_version/standards/category_reason 等），复用 CommandDetail 的 isNonEmpty/renderValue/sections computed
- `特性关系` tab：挂 FeatureRelationGraph 组件（vis-network）+ 下方关系表格（get_feature_relations 返回的 peer_code/peer_name/relation_type/interaction_note）
- `license` tab：get_feature_licenses 列表（点跳 license-detail）

- [ ] **Step 2: 右侧多 md 切换（顶部 md tab）**

复刻 CommandDetail 右侧，但 DocViewer 上方加 md 切换：
```vue
<section class="cmd-pane cmd-pane--right" :style="rightStyle">
  <div class="cmd-pane-head">
    <div class="doc-tabs">  <!-- 多 md 切换 -->
      <button v-for="(doc, i) in featureDocs" :key="i"
              :class="['doc-tab', {active: activeDoc===i}]"
              @click="switchDoc(i)">{{ doc.doc_title }}</button>
    </div>
  </div>
  <div class="cmd-pane-body">
    <DocViewer v-if="mdContent" :content="mdContent" :file-path="currentDocPath" api-base="feature-graph" :show-title="true" />
    <div v-else class="cmd-pane-empty">该特性无产品文档</div>
  </div>
</section>
```

`<script setup>` 多 md 逻辑（避免 loadAll 与 switchDoc 竞态：loadAll 内联加载首个 doc，switchDoc 只负责用户切换）：
```typescript
const featureDocs = ref<{doc_path: string; doc_title: string}[]>([])
const activeDoc = ref(0)
const currentDocPath = computed(() => featureDocs.value[activeDoc.value]?.doc_path || '')

// loadAll 内联加载首个 doc（不通过 switchDoc，避免重置/await 顺序问题）
async function loadAll() {
  loading.value = true
  mdContent.value = ''
  try {
    const data = await fetchJson(featureGraphApi.feature(nf.value, version.value, code.value))
    feature.value = data.error ? null : data
    // 加载多 md 列表
    const docsData = await fetchJson(featureGraphApi.featureDocs(nf.value, version.value, code.value))
    featureDocs.value = docsData.docs || []
    activeDoc.value = 0
    // 内联加载首个 doc（若有）
    if (featureDocs.value.length) {
      const mdData = await fetchJson(featureGraphApi.docContent(featureDocs.value[0].doc_path))
      mdContent.value = mdData.content || ''
    }
  } finally {
    loading.value = false
  }
}

// switchDoc 只用于用户点击切换（loadAll 不调它）
async function switchDoc(i: number) {
  activeDoc.value = i
  mdContent.value = ''
  if (currentDocPath.value) {
    const data = await fetchJson(featureGraphApi.docContent(currentDocPath.value))
    mdContent.value = data.content || ''
  }
}
```

- [ ] **Step 3: 关系 tab 懒加载（切到才挂 FeatureRelationGraph）**

复刻 CommandDetail 的 activatedTabs 模式：切到关系 tab 才挂 FeatureRelationGraph + 加载 get_feature_relations。

- [ ] **Step 4: Commit**

```bash
git add platform-next/frontend/src/feature_graph/FeatureDetail.vue
git commit -m "feat(platform-next/frontend): FeatureDetail左右侧+多md切换+3tab"
```

---

### Task 10: LicenseDetail.vue（license 详情左右侧）

**Files:**
- Create: `platform-next/frontend/src/feature_graph/LicenseDetail.vue`
- 参考: CommandDetail.vue（简化版）

- [ ] **Step 1: 写 LicenseDetail.vue**

复刻 CommandDetail 左右侧（CSS 复用 cmd-*），license 字段：
- 左侧 `license` tab：sections 数据驱动（license_code/control_item_id/name/license_domain/control_item_type/applicable_nf/value_range_raw/default_value_raw/description_raw/feature_refs）
- 左侧 `关联特性` tab：get_license_features 返回的 feature_code 列表（点跳 feature-detail）
- 右侧：DocViewer 单 md（license.source_path），api-base="feature-graph"

- [ ] **Step 2: Commit**

```bash
git add platform-next/frontend/src/feature_graph/LicenseDetail.vue
git commit -m "feat(platform-next/frontend): LicenseDetail左右侧(license字段+关联特性+md)"
```

---

## Chunk 4: 特性关系图组件 + 端到端验证

### Task 11: FeatureRelationGraph.vue（vis-network，独立配置）

**Files:**
- Create: `platform-next/frontend/src/feature_graph/FeatureRelationGraph.vue`
- 参考: `platform-next/frontend/src/command_graph/CommandGraph.vue`（vis-network 基础，但 type→颜色/edge→样式独立配置）

- [ ] **Step 1: 写 FeatureRelationGraph.vue**

复刻 CommandGraph.vue 的 vis-network 初始化 + load（调 featureGraphApi.featureGraph），但 type→group/颜色 + edge→样式独立配置：
```typescript
// 节点 group 映射（特性域）
const NODE_GROUPS = {
  feature: { color: { background: '#3b82f6', border: '#1d4ed8' }, shape: 'box' },  // 蓝色方块
}
// 边样式映射
const EDGE_STYLES = {
  depends_on: { color: '#64748b', dashes: false, label: '依赖' },
  conflicts_with: { color: '#dc2626', dashes: false, label: '互斥' },  // 红色
  affects: { color: '#94a3b8', dashes: true, label: '影响' },
  interacts_with: { color: '#94a3b8', dashes: true, label: '交互' },
  supports: { color: '#94a3b8', dashes: true, label: '支持' },
}
```
buildVisNodes：节点 type=feature → 蓝色方块（中心特性高亮放大）；buildVisEdges：按 relation_type 配颜色/虚线/label。点节点跳 `/feature/:nf/:version/feature/:code`（从 node.id 解析 code）。

- [ ] **Step 2: hops 控制**

顶部加"展开 1 跳/2 跳"切换按钮，调 featureGraphApi.featureGraph(code, hops)。

- [ ] **Step 3: Commit**

```bash
git add platform-next/frontend/src/feature_graph/FeatureRelationGraph.vue
git commit -m "feat(platform-next/frontend): FeatureRelationGraph vis-network关系图(独立配色+hops控制)"
```

---

### Task 12: 端到端验证（前端 build + 浏览器全流程）

**Files:** 无（验证任务）

- [ ] **Step 1: 前端 build**

```bash
cd platform-next/frontend
npm run build 2>&1 | tail -20
```
Expected: build 成功，无 TypeScript 错误。

- [ ] **Step 2: 启动后端 + 前端 dev，浏览器验证全流程**

```bash
cd platform-next && python main.py &
cd frontend && npm run dev &
```
浏览器验证：
1. `/feature` → 首页显示统计（特性/license/关系数）+ UDG/UNC 网元版本卡片
2. 点 UDG@20.15.2 卡片 → `/feature/UDG/20.15.2` 两 tab（特性/license 列表）
3. 特性 tab 点 GWFD-020301 → 详情左右侧：左侧特性属性/特性关系图/license 关联；右侧多 md 切换（概述/参考/原理...）
4. 特性关系 tab → vis-network 图（中心 GWFD-020301，周围依赖特性，边按类型配色）
5. license tab 点某 license → `/feature/UDG/20.15.2/license/LKV3G5BCBC01` 详情
6. license 详情左右侧：license 字段 + 关联特性 + md

- [ ] **Step 3: 修复验证发现的问题**

- [ ] **Step 4: Commit（如有修复）**

```bash
git add -A platform-next/frontend/src/feature_graph/
git commit -m "fix(platform-next/frontend): 端到端验证修复"
```

---

## 备注

- **CSS 复用**：所有 Vue 组件复用 CommandDetail/CommandOverview 的 cmd-*/cg-* 类（element-plus + 项目 CSS token），不引入新视觉体系
- **DocViewer 不变**：已支持 api-base="feature-graph" 双 base path，直接用
- **数据驱动渲染**：特性/license 详情用 CommandDetail 的 sections + LABEL_MAP 模式（新增字段自动展示）
- **子特性路由**：feature_code 含 `-N` 后缀（如 GWFD-010101-1）按普通 Feature 路由，:code 参数匹配（不含 /）
- **悬空关系 target**：get_feature_relations 返回 dangling 标记，前端表格显示原始 code + 灰色"悬空"标签
- **关系图范围**：get_feature_graph 只遍历 feature_relations（特性间），不含 requires_license 边（license 关联在 license tab 单独展示）
- **spec §11 废弃前提已成立**：旧 `platform-next/feature_graph/` + `frontend/src/feature_graph/` 已在 brainstorming 阶段删除（上一任务），本 plan 无需再删，直接新建
- **子特性多 md 简化**：第一版子特性（代际 -1/-2/-3）source_evidence_ids 只含代际概述（不展开代际目录全部 md）；单概述特性（多数）已支持全部 md
