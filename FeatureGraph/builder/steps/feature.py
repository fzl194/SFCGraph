"""Step feature: xlsx seed + 概述md 13节解析 → features.jsonl 节点表。

每个 Feature 节点：
- source_evidence_ids：该特性**全部关联 md**（概述置首 + 部署/激活/参考/原理…），legacy CSV ∪ 自走语料
- doc_assets：[{path, type}] 供前端做文档类型标签（概述/激活/参考信息/原理/部署/调测/other）
- 单概述特性：1 节点，13 *_raw 字段完整
- 多概述特性（同一 feature_code 有 N 个代际概述）：
    * 父节点 1 个：13 *_raw 字段全空，has_overview=multi_overview，source_evidence_ids=全部 md，doc_assets=全部
    * 子特性 N 个：feature_code = "{父}-{1..N}"，parent_feature_code 指向父，
      本代际 *_raw 字段独立，source_evidence_ids=[本代际概述]，doc_assets=[本代际概述]
    * 边表（feature_relations/feature_requires_license）target/source_id 仍用父 feature_code
"""
from __future__ import annotations

import os
import re
from collections import defaultdict
from pathlib import Path

from ..core.feature import (
    build_feature_node, build_multi_overview_parent, build_subfeature_node,
    infer_config_relevance,
)
from ..core.io import write_jsonl
from ..core.legacy import load_legacy_file_map
from ..core.overview import (
    collect_raw_fields, detect_variant_dimensions, extract_applicable_nf,
    extract_first_release, extract_standards, find_overview_md, parse_sections,
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
    """目录特性的最小节点。"""
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
        "doc_assets": [],
        "variant_dimensions": [],
        "applicable_nf_raw": "", "definition_raw": "", "customer_value_raw": "",
        "application_scenario_raw": "", "availability_raw": "", "feature_interaction_raw": "",
        "system_impact_raw": "", "restrictions_raw": "", "principle_raw": "",
        "charging_raw": "", "spec_raw": "", "standards_raw": "", "release_history_raw": "",
        "category_reason": "目录特性(is_directory=true)",
    }


def _build_multi_overview_nodes(seed: dict, overview_paths: list, variant_dims: list,
                                doc_assets: list, project_root: Path,
                                nf: str, version: str,
                                ordered_docs: list, doc_assets_field: list) -> list[dict]:
    """多概述特性：返回 [父节点] + [子特性节点 × N]。

    子特性按 overview_paths 顺序编号 -1, -2, -3。variant_label 来自 variant_dimensions 中
    对应代际的 key（如 "4G"/"5G"/"2_3G"），便于前端展示。

    父节点承载特性级全部 md（source_evidence_ids=ordered_docs, doc_assets=doc_assets_field）；
    子特性只挂本代际概述（部署/激活属特性级，不重复挂子特性）。
    """
    nodes: list[dict] = []
    parent = build_multi_overview_parent(seed, nf=nf, version=version,
                                         overview_paths=overview_paths, variant_dims=variant_dims)
    parent["source_evidence_ids"] = list(ordered_docs)
    parent["doc_assets"] = list(doc_assets_field)
    parent["category_reason"] = ""
    nodes.append(parent)

    # 代际名映射 (gen → label)
    gen_to_label: dict[str, str] = {}
    if variant_dims:
        for v in variant_dims:
            if v.get("name") == "代际":
                gen_to_label = {gen: gen for gen in v.get("overview_paths", {}).keys()}

    # 全局 doc_assets 用于 has_activation 判定（任一代际有 activation 文档）
    has_activation_any = any(dt == "activation" for _, dt in doc_assets)

    for idx, ov_path in enumerate(overview_paths, start=1):
        suffix = str(idx)
        variant_label = ""
        # 查找该路径对应的代际 label
        for gen, p in (variant_dims[0].get("overview_paths", {}) if variant_dims else {}).items():
            if p == ov_path:
                variant_label = gen
                break

        abs_ov = Path(ov_path) if Path(ov_path).is_absolute() else project_root / ov_path
        content = abs_ov.read_text(encoding="utf-8", errors="ignore") if abs_ov.exists() else ""
        sections = parse_sections(content)
        raws = collect_raw_fields(sections)
        no_config = "无需配置" in sections.get("可获得性", "")
        sub = build_subfeature_node(seed, nf=nf, version=version,
                                    suffix=suffix, variant_label=variant_label,
                                    overview_path=ov_path, raw_fields=raws,
                                    applicable_nf=extract_applicable_nf(sections),
                                    first_release=extract_first_release(sections),
                                    standards=extract_standards(sections),
                                    has_activation=has_activation_any,
                                    no_config=no_config, dep_count=0)
        sub["category_reason"] = ""
        sub["doc_assets"] = [{"path": ov_path, "type": "overview"}]
        nodes.append(sub)
    return nodes


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
    # legacy CSV 补全 file_map：历史 step2 全量 md 清单，比自走语料更全 + 兜住漏扫特性
    legacy_dir = ctx.get("legacy_dir")
    if legacy_dir:
        _ld = Path(legacy_dir)
        if not _ld.is_absolute():
            _ld = project_root / _ld
        for fid, paths in load_legacy_file_map(_ld, nf).items():
            file_map[fid] = sorted(set(file_map.get(fid, [])) | set(paths))

    nodes: list[dict] = []
    stats = {"leaf": 0, "dir": 0, "yes": 0, "no_overview": 0, "no_docs": 0,
             "empty": 0, "file_missing": 0, "multi_overview_parent": 0,
             "subfeature": 0}

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
            n["doc_assets"] = []
            n["variant_dimensions"] = []
            n["category_reason"] = ""
            nodes.append(n)
            stats["no_docs"] += 1
            continue

        overview_paths, doc_assets = find_overview_md(code, fps, project_root)
        # 全量 md（概述置首，去重）+ doc_assets 展示字段
        ordered_docs = overview_paths + [fp for fp in fps if fp not in overview_paths]
        doc_assets_field = [{"path": fp, "type": dt} for fp, dt in doc_assets]
        has_activation = any(dt == "activation" for _, dt in doc_assets)
        variant_dims = detect_variant_dimensions(overview_paths, code)

        # 多概述 + 检测到代际 variant → 拆 SubFeature（父 + 子 × N）
        # 多概述但无稳定 variant（UNC NF/接口细分）→ 父节点取第一条概述内容 + 列全部 md，不拆
        if len(overview_paths) > 1 and variant_dims:
            multi_nodes = _build_multi_overview_nodes(
                seed, overview_paths, variant_dims, doc_assets, project_root, nf, version,
                ordered_docs, doc_assets_field)
            if not sample or code in sample:
                nodes.extend(multi_nodes)
                stats["multi_overview_parent"] += 1
                stats["subfeature"] += len(overview_paths)
                stats["yes"] += len(overview_paths)
            continue

        primary_overview = overview_paths[0] if overview_paths else ""

        # 有 md 但无概述：列全部 md（issue 3 受益：漏扫/无概述特性也有文档可看）
        if not overview_paths:
            n = build_feature_node(seed, {}, applicable_nf=[], first_release="",
                standards=[], overview_path=None, nf=nf, version=version, has_overview="no_overview")
            n["source_evidence_ids"] = list(ordered_docs)
            n["doc_assets"] = list(doc_assets_field)
            n["variant_dimensions"] = []
            n["category_reason"] = ""
            nodes.append(n)
            stats["no_overview"] += 1
            continue

        abs_ov = Path(primary_overview) if Path(primary_overview).is_absolute() else project_root / primary_overview
        if not abs_ov.exists():
            n = build_feature_node(seed, {}, applicable_nf=[], first_release="",
                standards=[], overview_path=primary_overview, nf=nf, version=version, has_overview="file_missing")
            n["source_evidence_ids"] = list(ordered_docs)
            n["doc_assets"] = list(doc_assets_field)
            n["variant_dimensions"] = []
            n["category_reason"] = ""
            nodes.append(n)
            stats["file_missing"] += 1
            continue

        content = abs_ov.read_text(encoding="utf-8", errors="ignore")
        if len(content.strip()) < 50:
            n = build_feature_node(seed, {}, applicable_nf=[], first_release="",
                standards=[], overview_path=primary_overview, nf=nf, version=version, has_overview="empty")
            n["source_evidence_ids"] = list(ordered_docs)
            n["doc_assets"] = list(doc_assets_field)
            n["variant_dimensions"] = []
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
            overview_path=primary_overview, nf=nf, version=version, has_overview="yes",
            config_relevance=infer_config_relevance(has_activation, no_config))
        # source_evidence_ids：全部关联 md（概述置首）；多概述无 variant 时同样列全部
        node["source_evidence_ids"] = list(ordered_docs)
        node["doc_assets"] = list(doc_assets_field)
        node["variant_dimensions"] = []
        node["category_reason"] = ""
        nodes.append(node)
        stats["yes"] += 1

    out = Path(ctx["data_dir"]) / "features.jsonl"
    write_jsonl(out, nodes)
    print(f"[feature:{nf}/{version}] {len(nodes)} Feature (leaf={stats['leaf']}, dir={stats['dir']}, "
          f"yes={stats['yes']}, multi_parent={stats['multi_overview_parent']}, "
          f"sub={stats['subfeature']}, no_overview={stats['no_overview']}, "
          f"no_docs={stats['no_docs']}, empty={stats['empty']}, "
          f"file_missing={stats['file_missing']}) → {out}")
    return len(nodes)
