"""Feature graph data service — scans FeatureGraph/data and serves it.

Assets root layout: {assets_root}/{nf}/{version}/{features|licenses|feature_relations|feature_requires_license}.jsonl
对齐 command_graph/service.py 的扫描 + _adjacency 统一图模式。
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
        self._features: dict[tuple[str, str], list[dict]] = {}
        self._licenses: dict[tuple[str, str], list[dict]] = {}
        self._relations: dict[tuple[str, str], list[dict]] = {}
        self._req_lic: dict[tuple[str, str], list[dict]] = {}
        self._feat_by_id: dict[str, dict] = {}
        self._lic_by_id: dict[str, dict] = {}
        self._adjacency: dict[str, dict] = {}
        self._load()
        self._load_graph()

    # ---- loading ----
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
            target = {
                "features": self._features, "licenses": self._licenses,
                "feature_relations": self._relations,
                "feature_requires_license": self._req_lic,
            }.get(object_type)
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

    # ---- stats ----
    def get_stats(self) -> dict:
        feat_counts = {k: len(v) for k, v in self._features.items()}
        lic_counts = {k: len(v) for k, v in self._licenses.items()}
        rel_counts = {k: len(v) for k, v in self._relations.items()}
        ne_versions = []
        for (nf, ver) in sorted(set(feat_counts) | set(lic_counts) | set(rel_counts)):
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

    # ---- list (slim) ----
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

    # ---- single ----
    def get_feature(self, nf: str, version: str, code: str) -> dict | None:
        return self._feat_by_id.get(_make_feature_id(nf, version, code))

    def get_license(self, nf: str, version: str, code: str) -> dict | None:
        return self._lic_by_id.get(_make_license_id(nf, version, code))

    # ---- feature detail: docs / relations / licenses ----
    def get_feature_docs(self, nf: str, version: str, code: str) -> list[dict]:
        """读 features.jsonl 的 source_evidence_ids（全部 md），title 从文件名解析。"""
        rec = self.get_feature(nf, version, code)
        if not rec:
            return []
        out = []
        for path in rec.get("source_evidence_ids") or []:
            fn = path.rsplit("/", 1)[-1].rsplit("\\", 1)[-1]
            title = fn.rsplit("_", 1)[0] if "_" in fn else fn
            out.append({"doc_path": path, "doc_title": title})
        return out

    def get_feature_relations(self, nf: str, version: str, code: str) -> list[dict]:
        fid = _make_feature_id(nf, version, code)
        out = []
        for e in self._relations.get((nf, version), []):
            if e.get("source_id") == fid or e.get("target_id") == fid:
                peer_id = e.get("target_id") if e.get("source_id") == fid else e.get("source_id")
                peer_code = peer_id.rsplit("@", 1)[-1] if peer_id else ""
                peer_rec = self._feat_by_id.get(peer_id, {})
                out.append({
                    "peer_code": peer_code,
                    "peer_name": peer_rec.get("name", peer_code) if peer_rec else peer_code,
                    "direction": "out" if e.get("source_id") == fid else "in",
                    "relation_type": e.get("relation_type"),
                    "interaction_note": e.get("interaction_note", ""),
                    "dangling": peer_id not in self._feat_by_id,
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
        lid = _make_license_id(nf, version, code)
        out = []
        for e in self._req_lic.get((nf, version), []):
            if e.get("target_id") == lid:
                out.append(e.get("feature_code", ""))
        return [c for c in out if c]

    # ---- 统一图（_adjacency + BFS 子图，复刻 command_graph）----
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
                add_node(r.get("id"), "feature", r.get("name"),
                         {"feature_code": r.get("feature_code"), "feature_category": r.get("feature_category")})
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
        """BFS 取特性 N 跳子图（只在该 nf/version 的 feature_relations 边内遍历）。
        不含 requires_license 边——license 关联在 license tab 单独展示。"""
        center = _make_feature_id(nf, version, code)
        if center not in self._adjacency:
            return {"nodes": [], "edges": []}
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
                        continue
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

    # ---- md 内容（复刻 command_graph resolve_doc_path 容忍 output/ 前缀）----
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
