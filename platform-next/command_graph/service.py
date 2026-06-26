"""Command graph data service — scans CommandGraph/data/assets and serves it.

The assets root (config: command_graph.assets_root) is laid out as
``{assets_root}/{nf}/{version}/{object_type}.jsonl``. This service scans that
tree at startup and auto-discovers every network element (nf), version, and
object type found. Adding a new nf/version/object = drop a file and restart.

Object types recognised today:
  - mml_commands.jsonl      → MMLCommand records (main index)
  - command_parameters.jsonl → CommandParameter records, bucketed per (nf, version)
  - command_has_parameter.jsonl → has_parameter edges, bucketed per (nf, version)
  - parameter_depends_on.jsonl  → depends_on edges, bucketed per (nf, version)
  - other relation files       → scanned but only used for discovery/counts

Parameters and both edge classes are loaded in full and indexed by (nf, version)
so that ``get_command_parameters`` and ``get_command_graph`` can serve the detail
page without re-reading files.

All other behaviour (slim item list, single-record lookup, raw md read) is
unchanged. Field naming is unified to ``nf``; ``product`` is gone internally
(the router still accepts ``product`` as a deprecated alias for one more phase).
"""
import json
from pathlib import Path

from shared.config import get_config


def _last_segment(parameter_ref: str) -> str:
    """Return the final colon-delimited segment of a parameter reference.

    A parameter_id is ``nf@version@CommandParameter@command:param``; the
    command segment may contain spaces (e.g. ``SET AUTOLOGPOLICY``) but never a
    colon, so splitting from the right by one colon always yields the parameter
    name.
    """
    if not parameter_ref:
        return ""
    return parameter_ref.rsplit(":", 1)[-1]


def _make_command_id(nf: str, version: str, command_name: str) -> str:
    """Build a MMLCommand instance key.

    Must stay in lockstep with ``CommandGraph/builder/params.make_command_id``
    so that keys constructed here match the ``command_id`` field the builder
    writes into the jsonl assets.
    """
    return f"{nf}@{version}@MMLCommand@{command_name}"


class CommandGraphService:
    def __init__(self):
        # platform-next/ — config paths (assets_root, doc_root) are relative
        # to this directory.
        platform_root = Path(__file__).resolve().parent.parent
        cfg = get_config().get("command_graph", {})
        assets_root = cfg.get("assets_root")
        doc_root = cfg.get("doc_root", "..")
        self._assets_root = (platform_root / assets_root).resolve() if assets_root else None
        self._doc_root = (platform_root / doc_root).resolve()
        self._records: list[dict] = []
        self._by_id: dict[str, dict] = {}
        # (nf, version) -> full parameter records
        self._params: dict[tuple[str, str], list[dict]] = {}
        # (nf, version) -> has_parameter edge records
        self._has_param: dict[tuple[str, str], list[dict]] = {}
        # (nf, version) -> depends_on edge records
        self._depends: dict[tuple[str, str], list[dict]] = {}
        # ConfigObject
        self._obj_objects: dict[str, dict] = {}  # object_id -> record
        self._obj_edges: dict[tuple[str, str], list[dict]] = {}  # (nf,version) -> command_object_edges
        self._load()

    @property
    def _param_counts(self) -> dict[tuple[str, str], int]:
        """(nf, version) -> parameter count. Derived from _params so the two
        never drift; kept as a property because get_stats still reads it."""
        return {k: len(v) for k, v in self._params.items()}

    # ---- loading ----
    def _load(self) -> None:
        """Scan assets_root/*/*/*.jsonl and load by object type."""
        if not self._assets_root or not self._assets_root.exists():
            return
        for fp in sorted(self._assets_root.glob("*/*/*.jsonl")):
            # path layout: assets_root/{nf}/{version}/{file}.jsonl
            try:
                nf = fp.parent.parent.name
                version = fp.parent.name
            except IndexError:
                continue
            object_type = fp.stem  # e.g. mml_commands, command_parameters

            if object_type == "mml_commands":
                self._load_mml_commands(fp)
            elif object_type == "command_parameters":
                self._load_jsonl_bucket(fp, nf, version, self._params)
            elif object_type == "command_has_parameter":
                self._load_jsonl_bucket(fp, nf, version, self._has_param)
            elif object_type == "parameter_depends_on":
                self._load_jsonl_bucket(fp, nf, version, self._depends)
            elif object_type == "config_objects":
                self._load_config_objects(fp)
            elif object_type == "command_object_edges":
                self._load_jsonl_bucket(fp, nf, version, self._obj_edges)
            # other relation files are recognised as edge classes but not
            # consumed by current endpoints — load on demand when one is needed.

    def _load_mml_commands(self, fp: Path) -> None:
        with fp.open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                self._records.append(rec)
                self._by_id[rec.get("command_id", "")] = rec

    def _load_jsonl_bucket(
        self,
        fp: Path,
        nf: str,
        version: str,
        target: dict[tuple[str, str], list[dict]],
    ) -> None:
        """Load every JSONL record of ``fp`` into ``target[(nf, version)]``.

        The (nf, version) is taken from the asset directory layout
        ({nf}/{version}/{file}.jsonl) rather than from each row's own nf/version
        field — the directory is the authoritative source of which nf/version
        this asset belongs to, and rows may carry stale legacy version values.
        Malformed lines are skipped (counted neither as success nor failure).
        """
        key = (nf, version)
        bucket = target.setdefault(key, [])
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

    def _load_config_objects(self, fp: Path) -> None:
        """加载 config_objects.jsonl，按 object_id 索引。"""
        with fp.open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                self._obj_objects[rec.get("object_id", "")] = rec

    # ---- stats (nested: drives frontend L1/L2) ----
    def get_stats(self) -> dict:
        # {(nf, version): command_count}
        cmd_counts: dict[tuple[str, str], int] = {}
        for r in self._records:
            nf = r.get("nf") or "unknown"
            ver = r.get("version") or "unknown"
            cmd_counts[(nf, ver)] = cmd_counts.get((nf, ver), 0) + 1

        nes_map: dict[str, dict] = {}
        for (nf, ver), n in cmd_counts.items():
            ne = nes_map.setdefault(nf, {"name": nf, "versions_map": {}})
            ne["versions_map"][ver] = n

        # also surface any (nf, version) that has parameters but no commands
        for (nf, ver) in self._param_counts:
            ne = nes_map.setdefault(nf, {"name": nf, "versions_map": {}})
            ne["versions_map"].setdefault(ver, 0)

        nes = []
        for nf in sorted(nes_map.keys()):
            ne = nes_map[nf]
            versions = []
            cmd_total = 0
            param_total = 0
            for ver in sorted(ne["versions_map"].keys()):
                cmd_n = ne["versions_map"][ver]
                param_n = self._param_counts.get((nf, ver), 0)
                cmd_total += cmd_n
                param_total += param_n
                versions.append({
                    "version": ver,
                    "command_count": cmd_n,
                    "parameter_count": param_n,
                })
            nes.append({
                "name": nf,
                "command_count": cmd_total,
                "parameter_count": param_total,
                "versions": versions,
            })

        return {
            "total": len(self._records),
            "total_parameters": sum(self._param_counts.values()),
            "nes": nes,
        }

    # ---- list (slim items) ----
    @staticmethod
    def _slim(r: dict) -> dict:
        return {
            "command_id": r.get("command_id"),
            "command_name": r.get("command_name"),
            "command_name_zh": r.get("command_name_zh"),
            "nf": r.get("nf"),
            "version": r.get("version"),
            "verb": r.get("verb"),
            "category_path": r.get("category_path") or [],
            "command_function": r.get("command_function") or "",
        }

    def list_commands(
        self,
        nf: str | None = None,
        version: str | None = None,
        search: str | None = None,
        page: int = 1,
        size: int = 50,
    ) -> dict:
        s = (search or "").lower()
        filtered: list[dict] = []
        for r in self._records:
            if nf and r.get("nf") != nf:
                continue
            if version and r.get("version") != version:
                continue
            if s:
                cat = " ".join(r.get("category_path") or [])
                hay = " ".join([
                    r.get("command_name") or "",
                    r.get("command_name_zh") or "",
                    r.get("command_function") or "",
                    cat,
                ]).lower()
                if s not in hay:
                    continue
            filtered.append(r)

        filtered.sort(key=lambda r: (r.get("nf") or "", r.get("command_name") or ""))
        total = len(filtered)
        start = (page - 1) * size
        items = [self._slim(r) for r in filtered[start:start + size]]
        return {"total": total, "page": page, "size": size, "items": items}

    # ---- single (full record) ----
    def get_command(
        self, nf: str, command_name: str, version: str | None = None
    ) -> dict | None:
        for r in self._records:
            if r.get("nf") != nf:
                continue
            if r.get("command_name") != command_name:
                continue
            if version and r.get("version") != version:
                continue
            return r
        return None

    def get_command_md(
        self, nf: str, command_name: str, version: str | None = None
    ) -> str:
        rec = self.get_command(nf, command_name, version)
        if not rec:
            return ""
        evidence = rec.get("source_evidence_ids") or []
        md_path = evidence[0] if evidence else ""
        if not md_path:
            return ""
        full = self._doc_root / md_path
        if not full.exists() or not full.is_file():
            return ""
        return full.read_text(encoding="utf-8")

    # ---- parameters & graph (command detail: Tab2 / Tab3) ----
    def get_command_parameters(
        self, nf: str, command_name: str, version: str | None = None
    ) -> list[dict]:
        """Return the full parameter records of one command.

        Matches strictly by ``command_id = _make_command_id(nf, version, command_name)``;
        when ``version`` is None, the latest version that has parameters for
        this (nf, command_name) is used (sorted lexicographically). Returns an
        empty list when the command has no parameters (e.g. UNC commands, or
        commands whose parameter file was never generated).
        """
        if version is None:
            version = self._latest_version_with_params(nf, command_name)
            if version is None:
                return []
        command_id = _make_command_id(nf, version, command_name)
        bucket = self._params.get((nf, version), [])
        return [p for p in bucket if p.get("command_id") == command_id]

    def get_command_object(
        self, nf: str, command_name: str, version: str | None = None
    ) -> dict | None:
        """返回该命令操作的 ConfigObject（来自 command_object_edges）。

        一条命令对应一个 object_keyword → 一个 ConfigObject；返回它，无则 None。
        """
        if version is None:
            version = self._latest_version_with_params(nf, command_name)
        command_id = (
            _make_command_id(nf, version, command_name)
            if version else f"{nf}@MMLCommand@{command_name}"
        )
        for edge in self._obj_edges.get((nf, version) or ("", ""), []):
            if (edge.get("from_command_ref") or "") != command_id:
                continue
            obj = self._obj_objects.get(edge.get("to_object_ref") or "")
            if obj:
                return obj
        return None

    def _latest_version_with_params(self, nf: str, command_name: str) -> str | None:
        """Pick the lexicographically largest version under (nf) that actually
        contains parameters for ``command_name``. Returns None if none match."""
        candidate_versions = sorted(
            v for (n, v) in self._params.keys() if n == nf
        )
        for v in reversed(candidate_versions):
            cid = _make_command_id(nf, v, command_name)
            if any(p.get("command_id") == cid for p in self._params[(nf, v)]):
                return v
        return None

    def get_command_graph(
        self, nf: str, command_name: str, version: str | None = None
    ) -> dict:
        """Assemble a vis-network-ready ``{nodes, edges}`` for one command.

          - 1 command node (group=command)
          - N parameter nodes (group=parameter), or group=parameter_external
            for parameters referenced by a depends_on edge that are not part
            of this command's own parameter set (kept so the relation survives)
          - has_parameter edges (command -> param)
          - depends_on edges (param -> param) with a short condition label and
            a full condition tooltip

        Even for commands with no parameters the command node is emitted so the
        graph is never totally empty (the frontend decides how to render that).
        """
        if version is None:
            version = self._latest_version_with_params(nf, command_name)
        command_id = _make_command_id(nf, version, command_name) if version else f"{nf}@MMLCommand@{command_name}"

        # command node title: prefer the command's Chinese name when available
        cmd_title = command_name
        cmd_rec = self._by_id.get(command_id)
        if cmd_rec and cmd_rec.get("command_name_zh"):
            cmd_title = cmd_rec["command_name_zh"]
        nodes: list[dict] = [{
            "id": command_id,
            "label": command_name,
            "group": "command",
            "title": cmd_title,
        }]
        edges: list[dict] = []

        params = self.get_command_parameters(nf, command_name, version)
        param_id_set = {p.get("parameter_id") for p in params}
        param_by_id = {p.get("parameter_id"): p for p in params}

        # parameter nodes + has_parameter edges
        for p in params:
            pid = p.get("parameter_id")
            title = " | ".join([
                p.get("parameter_name_zh") or "",
                p.get("data_type") or "",
                p.get("required_mode") or "",
            ]).strip(" |")
            nodes.append({
                "id": pid,
                "label": p.get("parameter_name") or pid,
                "group": "parameter",
                "title": title,
            })
            edges.append({
                "from": command_id,
                "to": pid,
                "type": "has_parameter",
            })

        # depends_on edges — keep only those whose source belongs to this command.
        # Membership is checked against this command's own parameter set
        # (param_by_id) rather than by string-prefixing the instance key, so the
        # check is independent of the key format. For each kept edge, if the
        # target is outside this command's parameter set, surface it as a
        # parameter_external node so the dependency is not silently dropped.
        for edge in self._depends.get((nf, version) or ("", ""), []):
            from_ref = edge.get("from_parameter_ref") or ""
            to_ref = edge.get("to_parameter_ref") or ""
            # source-side scope check: from_ref must be one of this command's params
            if from_ref not in param_by_id:
                continue
            # add external target node if needed
            if to_ref not in param_id_set and to_ref:
                nodes.append({
                    "id": to_ref,
                    "label": _last_segment(to_ref),
                    "group": "parameter_external",
                    "title": to_ref,
                })
                param_id_set.add(to_ref)  # avoid duplicate external nodes
            cond_value = edge.get("condition_value") or ""
            cond_logic = edge.get("condition_logic") or ""
            cond_ref = edge.get("condition_ref") or ""
            label = f"={cond_value}" if cond_value else cond_logic
            title = " ".join([t for t in (cond_ref, cond_logic, cond_value) if t])
            edges.append({
                "from": from_ref,
                "to": to_ref,
                "type": "depends_on",
                "label": label,
                "title": title,
            })

        # ConfigObject 节点 + command→object 边（creates/modifies/sets/queries/...）
        for edge in self._obj_edges.get((nf, version) or ("", ""), []):
            if (edge.get("from_command_ref") or "") != command_id:
                continue
            obj_id = edge.get("to_object_ref") or ""
            obj = self._obj_objects.get(obj_id)
            if not obj:
                continue
            obj_title = obj.get("object_name_zh") or obj.get("object_name") or obj_id
            kind = obj.get("object_kind") or ""
            nodes.append({
                "id": obj_id,
                "label": obj.get("object_name") or obj_id,
                "group": "config_object",
                "title": f"{obj_title} [{kind}]" if kind else obj_title,
            })
            relation = edge.get("edge_type") or "operates_on"
            edges.append({
                "from": command_id,
                "to": obj_id,
                "type": relation,
                "label": relation,
                "title": relation,
            })

        return {"nodes": nodes, "edges": edges}

    # ---- static file serving (unchanged contract; images etc.) ----
    def resolve_doc_path(self, rel_path: str) -> Path | None:
        """Resolve a path under doc_root/output, with safety checks.

        容忍路径带或不带 output/ 前缀：DocViewer 用 source_evidence_ids[0]
        （含 output/）当基准拼图片/链接路径，会带前缀；feature-graph 等不带。
        """
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


# Singleton
_service: CommandGraphService | None = None


def get_service() -> CommandGraphService:
    global _service
    if _service is None:
        _service = CommandGraphService()
    return _service
