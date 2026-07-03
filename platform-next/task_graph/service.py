"""ConfigTask (动态任务层) 数据服务 — 扫描 ConfigTask/assert 并服务化。

assets_root(config: task_graph.assets_root)布局:
  {assets_root}/{nf}/{version}/{tasks|task_rules|decision_points}/*.yaml
启动时扫描整树,自动发现每个 nf/version。新增 nf/version/对象 = 丢文件 + 重启。

权威 schema:根目录 `改进后三层图谱定义.md` §4-§7
  - Task §4.1: task_id/task_logical_name/task_layer(atom/compound/feature/solution/generalized)/
    task_intent/task_category/nf/version/status/ref/parameter_bindings/...
  - TaskRule §5(owner_task_ref 挂在 Task 上)
  - DecisionPoint §6(owner_task_ref + options[].impacts[].target_type)
  - TaskRelation §7(内嵌在父 task 的 task_relations[])

本服务只读(YAML 是构建期活源,不转 JSONL)。DP/Rule 按 owner 归属进各自 Task 详情。
"""
import re
from pathlib import Path

import yaml

from shared.config import get_config


def _short(ref: str) -> str:
    """UDG@20.15.2@Task@0-00001 -> 0-00001"""
    return (ref or "").split("@")[-1] if ref else ""


def _parse_ref(ref: str) -> dict:
    """Task.ref -> {type, name/code} 用于跨图谱跳转。
    UDG@20.15.2@MMLCommand@ADD URR -> {type: MMLCommand, value: ADD URR}
    UDG@20.15.2@Feature@GWFD-020301 -> {type: Feature, value: GWFD-020301}
    """
    if not ref:
        return {}
    for t in ("MMLCommand", "Feature", "SubFeature", "ConfigurationSolution"):
        marker = f"@{t}@"
        if marker in ref:
            return {"type": t, "value": ref.split(marker, 1)[1]}
    return {}


class ConfigTaskService:
    def __init__(self):
        platform_root = Path(__file__).resolve().parent.parent
        cfg = get_config().get("task_graph", {})
        assets_root = cfg.get("assets_root")
        self._doc_root = (platform_root / cfg.get("doc_root", "..")).resolve()
        self._assets_root = (platform_root / assets_root).resolve() if assets_root else None
        self._tasks: list[dict] = []
        self._by_short: dict[str, dict] = {}
        self._rules_by_owner: dict[str, list[dict]] = {}
        self._dps_by_owner: dict[str, list[dict]] = {}
        self._relations_by_task: dict[str, list[dict]] = {}  # task_short -> [edges]
        self._orchestrated_by: dict[str, set[str]] = {}  # child_short -> {parent_short,...}
        self._load()

    # ---- loading ----
    def _load_yaml_dir(self, d: Path) -> list[dict]:
        out = []
        if not d.exists():
            return out
        for p in sorted(d.glob("*.yaml")):
            try:
                doc = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
                if isinstance(doc, dict):
                    out.append(doc)
            except Exception:
                pass
        return out

    def _load(self) -> None:
        if not self._assets_root or not self._assets_root.exists():
            return
        # 布局:{assets_root}/{nf}/{version}/{tasks|task_rules|decision_points}
        for ver_dir in sorted(self._assets_root.glob("*/*")):
            if not ver_dir.is_dir():
                continue
            for t in self._load_yaml_dir(ver_dir / "tasks"):
                if t.get("task_id"):
                    self._tasks.append(t)
            for r in self._load_yaml_dir(ver_dir / "task_rules"):
                if r.get("rule_id"):
                    self._rules_by_owner.setdefault(_short(r.get("owner_task_ref", "")), []).append(r)
            for dp in self._load_yaml_dir(ver_dir / "decision_points"):
                if dp.get("decision_id"):
                    self._dps_by_owner.setdefault(_short(dp.get("owner_task_ref", "")), []).append(dp)

        for t in self._tasks:
            t["_short"] = _short(t.get("task_id", ""))
            self._by_short[t["_short"]] = t

        # 全局关系索引:每个 task 出现在哪些 edge 里(from/to)
        # 注意:edge 存在 owner_task(父,如 feature 2-00002)的 task_relations[],
        # 描述子节点间的边(如 1-00001→1-00002)。owner 自己不在 from/to 里。
        for t in self._tasks:
            me = t["_short"]
            for r in (t.get("task_relations") or []):
                rid = r.get("relation_id", "")
                rtype = r.get("relation_type", "")
                cond = _short(r.get("condition_ref", ""))
                prop = r.get("propagated_context") or []
                src = _short(r.get("from_task_ref", ""))
                dst = _short(r.get("to_task_ref", ""))
                # from/to 的 short 都是被 owner(me) 编排的子节点
                for child in (src, dst):
                    if child and child != me:
                        self._orchestrated_by.setdefault(child, set()).add(me)
                for who, other, direction in ((src, dst, "from"), (dst, src, "to")):
                    if who and other and who != other:
                        self._relations_by_task.setdefault(who, []).append({
                            "other": other, "direction": direction,
                            "relation_type": rtype, "condition_ref": cond,
                            "propagated_context": prop, "relation_id": rid,
                        })

    # ---- API ----
    def get_stats(self) -> dict:
        ne_versions = {}
        layer_count = {}
        for t in self._tasks:
            nf = t.get("nf", "")
            ver = t.get("version", "")
            key = (nf, ver)
            ne_versions.setdefault(key, {"nf": nf, "version": ver, "task_count": 0, "layers": {}})
            ne_versions[key]["task_count"] += 1
            layer = t.get("task_layer", "?")
            ne_versions[key]["layers"][layer] = ne_versions[key]["layers"].get(layer, 0) + 1
            layer_count[layer] = layer_count.get(layer, 0) + 1
        return {
            "total_tasks": len(self._tasks),
            "total_rules": sum(len(v) for v in self._rules_by_owner.values()),
            "total_dps": sum(len(v) for v in self._dps_by_owner.values()),
            "by_layer": layer_count,
            "ne_versions": [
                {**v, "layers": v["layers"]} for v in sorted(ne_versions.values(), key=lambda x: (x["nf"], x["version"]))
            ],
        }

    def _slim(self, t: dict) -> dict:
        return {
            "task_id": t["_short"],
            "task_logical_name": t.get("task_logical_name", ""),
            "task_layer": t.get("task_layer", ""),
            "task_intent": t.get("task_intent", ""),
            "task_category": t.get("task_category", ""),
            "nf": t.get("nf", ""),
            "version": t.get("version", ""),
            "status": t.get("status", ""),
            "ref_type": _parse_ref(t.get("ref", "")).get("type", ""),
            "ref_value": _parse_ref(t.get("ref", "")).get("value", ""),
            "n_params": len(t.get("parameter_bindings") or []),
            "n_relations": len(t.get("task_relations") or []),
            "n_rules": len(self._rules_by_owner.get(t["_short"], [])),
            "n_dps": len(self._dps_by_owner.get(t["_short"], [])),
        }

    def list_tasks(self, nf: str | None = None, version: str | None = None,
                   layer: str | None = None, search: str | None = None,
                   page: int = 1, size: int = 50) -> dict:
        items = self._tasks
        if nf:
            items = [t for t in items if t.get("nf") == nf]
        if version:
            items = [t for t in items if t.get("version") == version]
        if layer:
            items = [t for t in items if t.get("task_layer") == layer]
        if search:
            s = search.lower()
            items = [t for t in items if s in (t.get("task_id", "").lower()
                    or s in (t.get("task_logical_name", "") or "").lower()
                    or s in (t.get("task_intent", "") or "").lower()
                    or s in (t.get("_short", "")).lower())]
        items = sorted(items, key=lambda t: t["_short"])
        total = len(items)
        start = (page - 1) * size
        return {"items": [self._slim(t) for t in items[start:start + size]], "total": total,
                "page": page, "size": size}

    def _resolve_relations(self, short: str) -> list[dict]:
        """返回该 task 自己作为端点出现的边 + 其作为父编排的子节点间边。

        - 作为端点(atom/compound 之间的边):来自 _relations_by_task。
        - 作为父(feature/compound/solution 编排子节点):其 task_relations[]。
        两者都是该 task "自己的" relations,合并去重返回。
        """
        out = []
        seen_pair = set()
        for e in self._relations_by_task.get(short, []):
            other = self._by_short.get(e["other"], {})
            key = (short, e["other"], e["direction"], e["relation_type"])
            if key in seen_pair:
                continue
            seen_pair.add(key)
            out.append({**e,
                        "other_logical_name": other.get("task_logical_name", ""),
                        "other_layer": other.get("task_layer", "")})
        t = self._by_short.get(short, {})
        for e in self._own_relations_resolved(t):
            key = (e["from_short"], e["to_short"], e["relation_type"])
            if key in seen_pair:
                continue
            seen_pair.add(key)
            out.append({"other": None, **e})
        return out

    def _own_relations_resolved(self, t: dict) -> list[dict]:
        """解析 t.task_relations[],补全 from/to 的 logical_name/layer。"""
        out = []
        for r in (t.get("task_relations") or []):
            fs, ts = _short(r.get("from_task_ref", "")), _short(r.get("to_task_ref", ""))
            ft, tt = self._by_short.get(fs, {}), self._by_short.get(ts, {})
            out.append({
                "from_short": fs, "to_short": ts,
                "from_logical_name": ft.get("task_logical_name", ""),
                "from_layer": ft.get("task_layer", ""),
                "to_logical_name": tt.get("task_logical_name", ""),
                "to_layer": tt.get("task_layer", ""),
                "relation_type": r.get("relation_type", ""),
                "condition_ref": _short(r.get("condition_ref", "")),
                "propagated_context": r.get("propagated_context") or [],
            })
        return out

    def _parents(self, short: str) -> list[dict]:
        """谁编排了 short(把 short 列在 task_relations 的 from/to 里的 owner)。"""
        out = []
        for p in sorted(self._orchestrated_by.get(short, set())):
            t = self._by_short.get(p, {})
            out.append({"short": p, "logical_name": t.get("task_logical_name", ""),
                        "layer": t.get("task_layer", "")})
        return out

    def get_task(self, nf: str, version: str, task_id: str) -> dict | None:
        # task_id 可能是短 id(0-00001)或完整 id;统一到 short
        short = _short(task_id) if "@" in task_id else task_id
        t = next((x for x in self._tasks if x["_short"] == short
                  and x.get("nf") == nf and x.get("version") == version), None)
        if not t:
            return None
        ref = _parse_ref(t.get("ref", ""))
        return {
            "task_id": t.get("task_id", ""),
            "short": short,
            "task_logical_name": t.get("task_logical_name", ""),
            "task_layer": t.get("task_layer", ""),
            "task_intent": t.get("task_intent", ""),
            "task_category": t.get("task_category", ""),
            "nf": t.get("nf", ""),
            "version": t.get("version", ""),
            "status": t.get("status", ""),
            "ref": t.get("ref", ""),
            "ref_parsed": ref,
            "confidence": t.get("confidence"),
            "notes": t.get("notes", ""),
            "parameter_bindings": t.get("parameter_bindings") or [],
            "source_evidence_ids": t.get("source_evidence_ids") or [],
            "task_relations": self._own_relations_resolved(t),
            "parents": self._parents(short),
            "rules": self._rules_by_owner.get(short, []),
            "decision_points": self._dps_by_owner.get(short, []),
        }

    def get_task_tree(self, task_id: str) -> dict:
        """以 task 为中心 1~2 跳邻居(供结构导航)。

        邻居来源:
        - 自己作为端点的边(_relations_by_task)
        - 编排自己的父节点(_orchestrated_by)及其编排的其他子节点
        """
        short = _short(task_id) if "@" in task_id else task_id
        seen = {short}
        frontier = [short]
        nodes = []
        edges = []
        for hop in range(2):
            nxt = []
            for s in frontier:
                t = self._by_short.get(s)
                if not t:
                    continue
                nodes.append({"id": s, "logical_name": t.get("task_logical_name", ""),
                              "layer": t.get("task_layer", ""), "status": t.get("status", "")})
                # 同辈边(自己作为端点)
                for e in self._relations_by_task.get(s, []):
                    o = e["other"]
                    pair = tuple(sorted((s, o)))
                    if (pair, e["relation_type"]) not in [(x["pair"], x["relation_type"]) for x in edges]:
                        edges.append({"pair": pair, "from": s, "to": o,
                                      "relation_type": e["relation_type"],
                                      "condition_ref": e["condition_ref"]})
                    if o not in seen:
                        seen.add(o)
                        nxt.append(o)
                # 父节点(编排者)及其编排的其他子节点
                for parent in sorted(self._orchestrated_by.get(s, set())):
                    pt = self._by_short.get(parent, {})
                    if parent not in seen:
                        seen.add(parent)
                        nxt.append(parent)
                    pair = tuple(sorted((s, parent)))
                    if (pair, "orchestrated_by") not in [(x["pair"], x["relation_type"]) for x in edges]:
                        edges.append({"pair": pair, "from": parent, "to": s,
                                      "relation_type": "orchestrated_by",
                                      "condition_ref": ""})
                    # 父编排的其他子节点(兄弟)
                    for sib_r in (pt.get("task_relations") or []):
                        for k in ("from_task_ref", "to_task_ref"):
                            sib = _short(sib_r.get(k, ""))
                            if sib and sib != s and sib not in seen:
                                seen.add(sib)
                                nxt.append(sib)
            frontier = nxt
        return {"center": short, "nodes": nodes, "edges": edges}


_svc: "ConfigTaskService | None" = None


def get_service() -> "ConfigTaskService":
    """懒加载单例(首次请求时初始化,此时 main.py lifespan 已 load_config)。"""
    global _svc
    if _svc is None:
        _svc = ConfigTaskService()
    return _svc

