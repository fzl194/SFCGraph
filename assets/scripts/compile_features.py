#!/usr/bin/env python3
"""
特性层 Compile 器（Typed LLM Wiki）
把 FeatureGraph/data/{nf}/{version}/features.jsonl 投影成
assets/feature/{nf}/{version}/<feature_code>.md —— 纯代码投影，不需 LLM。

严格复用命令层模式（compile_commands.py / compile_configobjects.py）：
  - jsonl 直读（encoding=utf-8，纯投影）
  - sanitize / id_to_path（四段式 → assets 根路径）
  - markdown 链接引用（已建带 .md，未建 [[ID]] 占位）
  - 关系双向链接（硬约束）
  - 证据按源手册 stem 命名拷贝（与命令层 evidence/ 共用去重）
  - 分级 index

双向关系（特性层）：
  - 所需 License：feature_requires_license 出向（Feature → License）
  - 所属目录 / 子特性：parent_feature_code 双向（catalog_parent，非 depends_on）
  - 特性关系：feature_relations 双向（depends_on/conflicts_with/interacts_with/affects/supports/cooperates_with）

用法:
  python assets/scripts/compile_features.py --nf UDG --version 20.15.2
"""
import argparse
import json
import re
import shutil
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / "FeatureGraph" / "data"
ASSETS = REPO / "assets"
EVID = ASSETS / "evidence"

# 13 节正文（schema §2.1），按文档原始顺序，只在非空时输出
SECTIONS = [
    ("applicable_nf_raw", "适用NF（原文）"),
    ("definition_raw", "定义"),
    ("customer_value_raw", "客户价值"),
    ("application_scenario_raw", "应用场景"),
    ("availability_raw", "可获得性"),
    ("feature_interaction_raw", "与其他特性的交互（原文）"),
    ("system_impact_raw", "对系统的影响"),
    ("restrictions_raw", "应用限制"),
    ("principle_raw", "原理概述"),
    ("charging_raw", "计费与话单"),
    ("spec_raw", "特性规格"),
    ("standards_raw", "遵循标准"),
    ("release_history_raw", "发布历史"),
]

# 关系类型 → 显示标签
REL_LABEL = {
    "depends_on": "依赖",
    "conflicts_with": "互斥",
    "cooperates_with": "协同",
    "interacts_with": "交互",
    "affects": "影响",
    "supports": "支持",
}


def load_jsonl(path: Path):
    out = []
    if not path.exists():
        return out
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return out


def sanitize(s) -> str:
    return re.sub(r'[\s/\\:*?"<>|]+', '-', str(s)).strip('-')


def id_to_path(obj_id: str, otype_dir: str) -> str:
    """四段式 ID → assets 根路径（无 .md 后缀）。非四段式原样返回（给 [[...]] 占位用）。"""
    parts = str(obj_id).split('@')
    if len(parts) >= 4:
        nf, ver = parts[0], parts[1]
        local = '@'.join(parts[3:])
        return f"{otype_dir}/{nf}/{ver}/{sanitize(local)}"
    return obj_id


def load_requires_license(nf: str, ver: str):
    """feature_requires_license：正向 feature→[license]，反向 license→[feature]。"""
    p = SRC / nf / ver / "feature_requires_license.jsonl"
    fwd, rev = {}, {}
    for r in load_jsonl(p):
        s = r.get("source_id"); t = r.get("target_id")
        if s and t:
            fwd.setdefault(s, []).append((t, r))
            rev.setdefault(t, []).append((s, r))
    return fwd, rev


def load_feature_relations(nf: str, ver: str):
    """feature_relations：出向 source→[(target,rec)]，入向 target→[(source,rec)]。双向。"""
    p = SRC / nf / ver / "feature_relations.jsonl"
    outc, inc = {}, {}
    for r in load_jsonl(p):
        s = r.get("source_id"); t = r.get("target_id")
        rt = r.get("relation_type")
        if s and t and rt:
            outc.setdefault(s, []).append((t, r))
            inc.setdefault(t, []).append((s, r))
    return outc, inc


def load_parent_maps(features: list):
    """parent_feature_code 双向：parent→[child_code]，child_code→parent_code。"""
    code2rec = {r.get("feature_code"): r for r in features if r.get("feature_code")}
    parent2children, child2parent = {}, {}
    for r in features:
        code = r.get("feature_code")
        parent = (r.get("parent_feature_code") or "").strip()
        if parent and code:
            parent2children.setdefault(parent, []).append(code)
            child2parent[code] = parent
    return code2rec, parent2children, child2parent


def copy_evidence(src_rel: str, rec: dict) -> str:
    """按源手册文件名 stem 命名拷进 evidence/{nf}/{version}/，与命令层共用去重。"""
    src = REPO / src_rel
    nf = rec.get("nf"); ver = rec.get("version")
    dst_dir = EVID / nf / ver
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst_name = sanitize(Path(src_rel).stem) + ".md"
    dst = dst_dir / dst_name
    if src.exists():
        shutil.copyfile(src, dst)
    else:
        dst.write_text(f"(证据源缺失) {src_rel}\n", encoding="utf-8")
    return f"evidence/{nf}/{ver}/{dst_name}"


def feat_local(obj_id: str) -> str:
    """四段式 Feature ID → feature_code（用于显示与链接 local）。"""
    return str(obj_id).split('@')[-1]


def link_or_placeholder(obj_id: str, otype_dir: str, local: str,
                        exists: set, nf: str, ver: str) -> str:
    """§5.5：已建对象 → markdown 链接（带 .md）；未建 → [[对象ID]] 占位（断链防护）。"""
    if local in exists:
        return f"[{local}]({otype_dir}/{nf}/{ver}/{sanitize(local)}.md)"
    return f"[[{obj_id}]]"


def project_feature(rec: dict, req_fwd: dict, rel_out: dict, rel_in: dict,
                    code2rec: dict, lic_codes: set,
                    parent2children: dict, child2parent: dict,
                    nf: str, ver: str) -> str:
    code = rec.get("feature_code", "")
    fid = rec.get("id", "") or f"{nf}@{ver}@Feature@{code}"
    name = rec.get("name", "") or code
    is_dir = bool(rec.get("is_directory"))

    fm = {
        "id": fid, "type": "Feature", "name": name,
        "nf": nf, "version": ver,
        "feature_code": code,
        "is_directory": is_dir,
        "catalog_section": rec.get("catalog_section") or None,
        "parent_feature_code": rec.get("parent_feature_code") or None,
        "applicable_nf": rec.get("applicable_nf") or [],
        "feature_category": rec.get("feature_category"),
        "config_relevance": rec.get("config_relevance"),
        "first_release_version": rec.get("first_release_version") or None,
        "status": "active",
    }
    fm = {k: v for k, v in fm.items() if v is not None and v != []}

    parts = ["---",
             yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, default_flow_style=False).strip(),
             "---", "", f"# {name}", ""]

    tag = "（目录节点）" if is_dir else ""
    parts.append(f"`{code}` · {rec.get('feature_category','')} · {rec.get('config_relevance','')}{tag}")
    parts.append("")

    # 所属目录（叶子特性指回父目录）
    parent = child2parent.get(code)
    if parent:
        pid = f"{nf}@{ver}@Feature@{parent}"
        parts += ["## 所属目录", "",
                  f"- {link_or_placeholder(pid, 'feature', parent, code2rec, nf, ver)}", ""]

    # 子特性（目录节点列出）
    children = sorted(set(parent2children.get(code, [])))
    if children:
        parts += ["## 子特性", ""]
        for c in children:
            cid = f"{nf}@{ver}@Feature@{c}"
            crec = code2rec.get(c, {})
            cn = crec.get("name", "") or ""
            tail = f" {cn}" if cn else ""
            if c in code2rec:
                parts.append(f"- [{c}{tail}](feature/{nf}/{ver}/{sanitize(c)}.md)")
            else:
                parts.append(f"- [[{cid}]]{tail}")
        parts.append("")

    # 适用性（归一化 NF + 代际矩阵）
    anf = rec.get("applicable_nf") or []
    nfm = (rec.get("nf_support_map") or "").strip()
    if anf or nfm:
        parts += ["## 适用性", ""]
        if anf:
            parts.append("- 适用NF：" + "、".join(anf))
        if nfm:
            parts.append(f"- 代际支持矩阵：`{nfm}`")
        parts.append("")

    # 13 节正文（非空才输出）
    for field, title in SECTIONS:
        txt = (rec.get(field) or "").strip()
        if txt:
            parts += [f"## {title}", "", txt, ""]

    # 差异维度（SubFeature 替代，schema §4.3）
    vd = rec.get("variant_dimensions") or []
    if vd:
        parts += ["## 差异维度", ""]
        for v in vd:
            parts.append(f"- {v}")
        parts.append("")

    # 所需 License（requires_license 出向，双向：License 侧反查在 compile_licenses.py）
    licenses = req_fwd.get(fid, [])
    if licenses:
        parts += ["## 所需 License", ""]
        for lid, er in sorted(licenses, key=lambda x: x[0]):
            lcode = feat_local(lid)  # license local = license_code
            ctrl = er.get('control_item_id', '')
            tail = f"  — 控制项 {ctrl}" if ctrl else ""
            if lcode in lic_codes:
                parts.append(f"- [{lcode}](license/{nf}/{ver}/{sanitize(lcode)}.md){tail}")
            else:
                parts.append(f"- [[{lid}]]{tail}")
        parts.append("")

    # 特性关系（feature_relations 双向，按 relation_type 分组）
    out_edges = rel_out.get(fid, [])
    in_edges = rel_in.get(fid, [])
    if out_edges or in_edges:
        parts += ["## 特性关系", ""]
        # 按关系类型聚合：出向 + 入向
        buckets = {}  # reltype -> list of (other_id, direction, note)
        for tid, r in out_edges:
            buckets.setdefault(r.get("relation_type"), []).append((tid, "出", r.get("interaction_note", "")))
        for sid, r in in_edges:
            buckets.setdefault(r.get("relation_type"), []).append((sid, "入", r.get("interaction_note", "")))
        for rt in sorted(buckets):
            label = REL_LABEL.get(rt, rt)
            parts.append(f"**{label}（{rt}）**")
            parts.append("")
            for other, direction, note in sorted(set(buckets[rt]), key=lambda x: x[0]):
                other_code = feat_local(other)
                line = f"- {link_or_placeholder(other, 'feature', other_code, code2rec, nf, ver)}"
                if note:
                    line += f"：{note}"
                parts.append(line)
            parts.append("")

    # 分解的任务（decomposes_to，任务层未建 → 占位；当前无数据源，预留）
    # 证据（可剥离）
    ev = list(dict.fromkeys(rec.get("source_evidence_ids") or []))
    if ev:
        parts += ["## 证据", ""]
        for e in ev:
            ev_rel = copy_evidence(e, rec)
            parts.append(f"- 原始手册：`{ev_rel}`")
        parts.append("")

    return "\n".join(parts).rstrip() + "\n"


def update_local_index(nf: str, ver: str, features: list):
    idx = ASSETS / "feature" / nf / ver / "index.md"
    by_section = {}
    for rec in features:
        code = rec.get("feature_code", "")
        if not code:
            continue
        section = rec.get("catalog_section") or "未分类"
        name = rec.get("name", "") or code
        is_dir = bool(rec.get("is_directory"))
        fname = sanitize(code) + ".md"
        by_section.setdefault(section, []).append((code, name, is_dir, fname))

    lines = [f"# index · feature/{nf}/{ver}", "",
             "> 局部 index（Compile 自动生成，按 catalog_section 分组）。顶层导航见 ../../../index.md",
             f"> 共 {len(features)} 个特性节点。", ""]
    for section in sorted(by_section):
        lines.append(f"## {section}")
        lines.append("")
        for code, name, is_dir, fname in sorted(by_section[section], key=lambda x: x[0]):
            tag = " 📁" if is_dir else ""
            lines.append(f"- [{code} {name}](feature/{nf}/{ver}/{fname}){tag}")
        lines.append("")
    idx.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nf", required=True)
    ap.add_argument("--version", required=True)
    args = ap.parse_args()
    nf, ver = args.nf, args.version

    features = load_jsonl(SRC / nf / ver / "features.jsonl")
    licenses = load_jsonl(SRC / nf / ver / "licenses.jsonl")
    lic_codes = {r.get("license_code") for r in licenses if r.get("license_code")}
    req_fwd, _rev_lic = load_requires_license(nf, ver)
    rel_out, rel_in = load_feature_relations(nf, ver)
    code2rec, parent2children, child2parent = load_parent_maps(features)

    out_dir = ASSETS / "feature" / nf / ver
    out_dir.mkdir(parents=True, exist_ok=True)

    n = 0
    for rec in features:
        code = rec.get("feature_code")
        if not code:
            continue
        md = project_feature(rec, req_fwd, rel_out, rel_in,
                             code2rec, lic_codes,
                             parent2children, child2parent, nf, ver)
        (out_dir / (sanitize(code) + ".md")).write_text(md, encoding="utf-8")
        n += 1

    update_local_index(nf, ver, features)
    print(f"Compiled {n} features → assets/feature/{nf}/{ver}/")
    print(f"Evidence → assets/evidence/{nf}/{ver}/ (与命令层共用去重)")
    print(f"Local index updated.")


if __name__ == "__main__":
    main()
