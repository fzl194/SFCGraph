"""Step feature: xlsx seed + 概述md 13节解析 → features.jsonl 节点表 + feature_doc_assets.jsonl。

支持 --sample 过滤（第一批小范围验证）；has_overview 5 态：
yes/no_overview/empty/no_docs/file_missing。

feature_doc_assets.jsonl 同步产出（零额外扫描成本：find_overview_md 已返回 doc_assets 列表）。
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
_DOC_TITLE_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)


def _scan_feature_docs(corpus_root: Path, valid_fids: set, project_root: Path) -> dict:
    """移植 step2：md 归属到路径上最深层特性。返回 {feature_code: [relpath,...]}。"""
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


def _read_doc_title(file_path: str, project_root: Path) -> str:
    """读 md 的 H1 标题（移植 step4 read_doc_title）。"""
    abs_fp = Path(file_path) if Path(file_path).is_absolute() else project_root / file_path
    if not abs_fp.exists():
        return ""
    try:
        text = abs_fp.read_text(encoding="utf-8", errors="ignore")
        m = _DOC_TITLE_RE.search(text)
        return m.group(1).strip() if m else ""
    except Exception:
        return ""


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
    doc_assets_all: list[dict] = []
    stats = {"total": 0, "yes": 0, "no_overview": 0, "no_docs": 0, "empty": 0, "file_missing": 0}

    for seed in seeds:
        if seed["is_directory"]:
            continue
        code = seed["feature_code"]
        if sample and code not in sample:
            continue
        stats["total"] += 1

        fps = file_map.get(code, [])
        if not fps:
            nodes.append(build_feature_node(seed, {}, applicable_nf=[], first_release="",
                standards=[], overview_path=None, nf=nf, version=version, has_overview="no_docs"))
            stats["no_docs"] += 1
            continue

        overview_path, doc_assets = find_overview_md(code, fps, project_root)
        has_activation = any(dt == "activation" for _, dt in doc_assets)
        if not overview_path:
            nodes.append(build_feature_node(seed, {}, applicable_nf=[], first_release="",
                standards=[], overview_path=None, nf=nf, version=version, has_overview="no_overview"))
            stats["no_overview"] += 1
            # 仍记录 doc_assets（有文档但未识别概述）
            for fp, dt in doc_assets:
                doc_assets_all.append({"feature_code": code, "doc_path": fp,
                                       "doc_type": dt, "doc_title": _read_doc_title(fp, project_root)})
            continue

        abs_ov = Path(overview_path) if Path(overview_path).is_absolute() else project_root / overview_path
        if not abs_ov.exists():
            nodes.append(build_feature_node(seed, {}, applicable_nf=[], first_release="",
                standards=[], overview_path=overview_path, nf=nf, version=version, has_overview="file_missing"))
            stats["file_missing"] += 1
            continue

        content = abs_ov.read_text(encoding="utf-8", errors="ignore")
        if len(content.strip()) < 50:
            nodes.append(build_feature_node(seed, {}, applicable_nf=[], first_release="",
                standards=[], overview_path=overview_path, nf=nf, version=version, has_overview="empty"))
            stats["empty"] += 1
            # 仍记录 doc_assets
            for fp, dt in doc_assets:
                doc_assets_all.append({"feature_code": code, "doc_path": fp,
                                       "doc_type": dt, "doc_title": _read_doc_title(fp, project_root)})
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
        node["has_activation_doc"] = has_activation
        nodes.append(node)
        stats["yes"] += 1

        # doc_assets: 覆盖该特性所有 md（含 overview + activation/debug/principle/...）
        for fp, dt in doc_assets:
            doc_assets_all.append({"feature_code": code, "doc_path": fp,
                                   "doc_type": dt, "doc_title": _read_doc_title(fp, project_root)})

    out = Path(ctx["data_dir"]) / "features.jsonl"
    write_jsonl(out, nodes)
    doc_out = Path(ctx["data_dir"]) / "feature_doc_assets.jsonl"
    write_jsonl(doc_out, doc_assets_all)
    print(f"[feature:{nf}/{version}] {len(nodes)} Feature "
          f"(yes={stats['yes']}, no_overview={stats['no_overview']}, no_docs={stats['no_docs']}, "
          f"empty={stats['empty']}, file_missing={stats['file_missing']}) → {out}")
    print(f"[feature:{nf}/{version}] {len(doc_assets_all)} doc_assets → {doc_out}")
    return len(nodes)

