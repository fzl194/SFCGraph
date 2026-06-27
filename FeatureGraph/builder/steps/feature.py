"""Step feature: xlsx seed + 概述md 13节解析 → features.jsonl 节点表。

每个 Feature 节点自带 `source_evidence_ids`（该特性所有 md 路径列表）和 doc_type 分类。
"""
from __future__ import annotations

import os
import re
from collections import defaultdict
from pathlib import Path

from ..core.feature import build_feature_node, infer_config_relevance
from ..core.io import write_jsonl
from ..core.overview import (
    collect_raw_fields, extract_applicable_nf, extract_first_release,
    extract_standards, find_overview_md, parse_sections,
)
from ..core.seed import NF_COLUMNS, extract_seed
from .registry import step

_DIRPAT = re.compile(r"^(GWFD|WSFD|IPFD|NPFD)-(\d{3,6})\s")
_FIDPREFIX_RE = re.compile(r"^(GWFD|WSFD|IPFD|NPFD)-(\d{3,6})")


def _scan_feature_docs(corpus_root: Path, valid_fids: set, project_root: Path) -> dict:
    """移植 step2：md 归属到路径上最深层特性。"""
    mapping: dict = defaultdict(list)
    for root, dirs, files in os.walk(corpus_root):
        dirs[:] = [d for d in dirs if not d.endswith(".assets")]
        path_fids: list[str] = []
        for part in Path(root).parts:
            m = _DIRPAT.match(part)
            if m:
                path_fids.append(f"{m.group(1)}-{m.group(2)}")
        for fn in sorted(files):
            if not fn.endswith(".md"):
                continue
            fid = path_fids[-1] if path_fids else ""
            if not fid:
                m = _FIDPREFIX_RE.match(fn)
                fid = f"{m.group(1)}-{m.group(2)}" if m else ""
            if fid and fid in valid_fids:
                rel = str((Path(root) / fn).relative_to(project_root)).replace("\\", "/")
                mapping[fid].append(rel)
    return mapping


def _build_directory_node(seed: dict, nf: str, version: str) -> dict:
    """目录特性的最小节点（无概述 md，便于 parent_feature_code 依赖 target 命中）。"""
    code = seed["feature_code"]
    return {
        "id": f"{nf}@{version}@Feature@{code}",
        "feature_code": code,
        "name": seed.get("name", ""),
        "is_directory": True,
        "catalog_section": seed.get("catalog_section", ""),
        "parent_feature_code": "",
        "applicable_nf": [],
        "nf_support_map": seed.get("nf_support_map", ""),
        "first_release_version": "",
        "standards": [],
        "feature_category": "base",
        "config_relevance": "none",
        "nf": nf,
        "version": version,
        "source_path": "",
        "has_overview": "directory",
        "source_evidence_ids": [],
        "applicable_nf_raw": "", "definition_raw": "", "customer_value_raw": "",
        "application_scenario_raw": "", "availability_raw": "", "feature_interaction_raw": "",
        "system_impact_raw": "", "restrictions_raw": "", "principle_raw": "",
        "charging_raw": "", "spec_raw": "", "standards_raw": "", "release_history_raw": "",
        "category_reason": "目录特性(is_directory=true)",
    }


@step("feature", output_file="features.jsonl")
def run(ctx):
    nf, version = ctx["nf"], ctx["version"]
    project_root = ctx["project_root"]
    manifest = Path(ctx["manifest"])
    if not manifest.is_absolute():
        manifest = project_root / ctx["manifest"]
    corpus_root = project_root / ctx["corpus_root"]
    sample = ctx.get("sample")

    seeds = extract_seed(manifest, ctx.get("manifest_sheets", [1, 2]), NF_COLUMNS[nf])
    valid_fids = {s["feature_code"] for s in seeds if not s["is_directory"]}
    file_map = _scan_feature_docs(corpus_root, valid_fids, project_root)

    nodes: list[dict] = []
    stats = {"leaf": 0, "dir": 0, "yes": 0, "no_overview": 0, "no_docs": 0, "empty": 0, "file_missing": 0}

    for seed in seeds:
        code = seed["feature_code"]
        if sample and code not in sample:
            continue

        if seed["is_directory"]:
            nodes.append(_build_directory_node(seed, nf, version))
            stats["dir"] += 1
            continue

        stats["leaf"] += 1

        fps = file_map.get(code, [])
        if not fps:
            n = build_feature_node(seed, {}, applicable_nf=[], first_release="",
                standards=[], overview_path=None, nf=nf, version=version, has_overview="no_docs")
            n["source_evidence_ids"] = []
            n["category_reason"] = ""
            nodes.append(n)
            stats["no_docs"] += 1
            continue

        overview_path, doc_assets = find_overview_md(code, fps, project_root)
        has_activation = any(dt == "activation" for _, dt in doc_assets)
        ev_ids = [fp for fp, _ in doc_assets]

        if not overview_path:
            n = build_feature_node(seed, {}, applicable_nf=[], first_release="",
                standards=[], overview_path=None, nf=nf, version=version, has_overview="no_overview")
            n["source_evidence_ids"] = ev_ids
            n["category_reason"] = ""
            nodes.append(n)
            stats["no_overview"] += 1
            continue

        abs_ov = Path(overview_path) if Path(overview_path).is_absolute() else project_root / overview_path
        if not abs_ov.exists():
            n = build_feature_node(seed, {}, applicable_nf=[], first_release="",
                standards=[], overview_path=overview_path, nf=nf, version=version, has_overview="file_missing")
            n["source_evidence_ids"] = ev_ids
            n["category_reason"] = ""
            nodes.append(n)
            stats["file_missing"] += 1
            continue

        content = abs_ov.read_text(encoding="utf-8", errors="ignore")
        if len(content.strip()) < 50:
            n = build_feature_node(seed, {}, applicable_nf=[], first_release="",
                standards=[], overview_path=overview_path, nf=nf, version=version, has_overview="empty")
            n["source_evidence_ids"] = ev_ids
            n["category_reason"] = ""
            nodes.append(n)
            stats["empty"] += 1
            continue

        sections = parse_sections(content)
        raws = collect_raw_fields(sections)
        no_config = "无需配置" in sections.get("可获得性", "")
        node = build_feature_node(seed, raws,
            applicable_nf=extract_applicable_nf(sections),
            first_release=extract_first_release(sections),
            standards=extract_standards(sections),
            overview_path=overview_path, nf=nf, version=version, has_overview="yes",
            config_relevance=infer_config_relevance(has_activation, no_config))
        node["source_evidence_ids"] = ev_ids
        node["category_reason"] = ""
        nodes.append(node)
        stats["yes"] += 1

    out = Path(ctx["data_dir"]) / "features.jsonl"
    write_jsonl(out, nodes)
    print(f"[feature:{nf}/{version}] {len(nodes)} Feature (leaf={stats['leaf']}, dir={stats['dir']}, "
          f"yes={stats['yes']}, no_overview={stats['no_overview']}, no_docs={stats['no_docs']}, "
          f"empty={stats['empty']}, file_missing={stats['file_missing']}) → {out}")
    return len(nodes)



