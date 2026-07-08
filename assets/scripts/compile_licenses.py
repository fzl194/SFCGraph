#!/usr/bin/env python3
"""
License Compile 器（Typed LLM Wiki）
把 FeatureGraph/data/{nf}/{version}/licenses.jsonl 投影成
assets/license/{nf}/{version}/<license_code>.md —— 纯代码投影，不需 LLM。

严格复用命令层 / 特性层模式（compile_configobjects.py 反向枢纽）。
双向关系：
  - 控制的能力：feature_requires_license 反查（License → Feature），与 compile_features.py 的
    "所需 License" 出向互为正反向，构成 Feature↔License 双向链接。
证据按源手册 stem 命名拷贝（与命令/特性层 evidence/ 共用去重）。

用法:
  python assets/scripts/compile_licenses.py --nf UDG --version 20.15.2
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

# 表格原始字段 → 显示标题（schema §2.3）
FIELDS = [
    ("applicable_nf_raw", "归属/适用NF（原文）"),
    ("description_raw", "功能描述"),
    ("implementation_description_raw", "实现描述"),
    ("value_range_raw", "取值范围"),
    ("default_value_raw", "默认值"),
    ("application_scenario_raw", "应用场景"),
    ("related_control_items_raw", "相关控制项（原文，未解释为边）"),
]


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


def load_requires_license_rev(nf: str, ver: str):
    """feature_requires_license 反向：license_id → [(feature_id, rec)]。"""
    p = SRC / nf / ver / "feature_requires_license.jsonl"
    rev = {}
    for r in load_jsonl(p):
        s = r.get("source_id"); t = r.get("target_id")
        if s and t:
            rev.setdefault(t, []).append((s, r))
    return rev


def copy_evidence(src_rel: str, rec: dict) -> str:
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
    return str(obj_id).split('@')[-1]


def link_or_placeholder(obj_id: str, otype_dir: str, local: str,
                        exists: set, nf: str, ver: str) -> str:
    """§5.5：已建 → markdown 链接（带 .md）；未建 → [[对象ID]] 占位（断链防护）。"""
    if local in exists:
        return f"[{local}]({otype_dir}/{nf}/{ver}/{sanitize(local)}.md)"
    return f"[[{obj_id}]]"


def project_license(rec: dict, rev_req: dict, feat_codes: set) -> str:
    nf = rec.get("nf"); ver = rec.get("version")
    lid = rec.get("id", "")
    lcode = rec.get("license_code", "")
    name = rec.get("name", "") or lcode
    cid = rec.get("control_item_id", "")

    fm = {
        "id": lid, "type": "License", "name": name,
        "nf": nf, "version": ver,
        "license_code": lcode,
        "control_item_id": cid or None,
        "license_domain": rec.get("license_domain") or None,
        "control_item_type": rec.get("control_item_type") or None,
        "applicable_nf": rec.get("applicable_nf") or [],
        "status": "active",
    }
    fm = {k: v for k, v in fm.items() if v is not None and v != []}

    parts = ["---",
             yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, default_flow_style=False).strip(),
             "---", "", f"# {name}", ""]

    parts.append(f"`{lcode}` · 控制项 {cid} · {rec.get('control_item_type','')} · 域 {rec.get('license_domain','')}")
    parts.append("")

    # 表格原始字段（非空才输出）
    for field, title in FIELDS:
        txt = (rec.get(field) or "").strip()
        if txt:
            parts += [f"## {title}", "", txt, ""]

    # 对应特性（原文，license doc 的"对应特性"列）
    frr = (rec.get("feature_refs_raw") or "").strip()
    if frr:
        parts += ["## 对应特性（原文）", "", frr, ""]

    # 控制的能力（requires_license 反查 → Feature，双向）
    feats = rev_req.get(lid, [])
    if feats:
        parts += ["## 控制的能力", ""]
        for fcid, er in sorted(feats, key=lambda x: x[0]):
            fcode = feat_local(fcid)
            ctrl = er.get('control_item_id', '')
            tail = f"  — 控制项 {ctrl}" if ctrl else ""
            parts.append(f"- {link_or_placeholder(fcid, 'feature', fcode, feat_codes, nf, ver)}{tail}")
        parts.append("")

    # 证据（可剥离）
    sp = (rec.get("source_path") or "").strip()
    if sp:
        ev_rel = copy_evidence(sp, rec)
        parts += ["## 证据", "", f"- 原始手册：`{ev_rel}`", ""]

    return "\n".join(parts).rstrip() + "\n"


def update_local_index(nf: str, ver: str, licenses: list):
    idx = ASSETS / "license" / nf / ver / "index.md"
    # 一级按 control_item_type，二级按 license_domain
    by_grp = {}
    for rec in licenses:
        lcode = rec.get("license_code", "")
        if not lcode:
            continue
        ctype = rec.get("control_item_type") or "未分类"
        domain = rec.get("license_domain") or "未分类"
        name = rec.get("name", "") or lcode
        fname = sanitize(lcode) + ".md"
        by_grp.setdefault(ctype, {}).setdefault(domain, []).append((lcode, name, fname))

    lines = [f"# index · license/{nf}/{ver}", "",
             "> 局部 index（Compile 自动生成，按 control_item_type × license_domain 分组）。顶层导航见 ../../../index.md",
             f"> 共 {len(licenses)} 个 License 控制项。", ""]
    for ctype in sorted(by_grp):
        lines.append(f"## {ctype}")
        lines.append("")
        for domain in sorted(by_grp[ctype]):
            lines.append(f"### {domain}")
            lines.append("")
            for lcode, name, fname in sorted(by_grp[ctype][domain], key=lambda x: x[0]):
                lines.append(f"- [{lcode} {name}](license/{nf}/{ver}/{fname})")
            lines.append("")
    idx.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nf", required=True)
    ap.add_argument("--version", required=True)
    args = ap.parse_args()
    nf, ver = args.nf, args.version

    licenses = load_jsonl(SRC / nf / ver / "licenses.jsonl")
    features = load_jsonl(SRC / nf / ver / "features.jsonl")
    feat_codes = {r.get("feature_code") for r in features if r.get("feature_code")}
    rev_req = load_requires_license_rev(nf, ver)

    out_dir = ASSETS / "license" / nf / ver
    out_dir.mkdir(parents=True, exist_ok=True)

    n = 0
    for rec in licenses:
        lcode = rec.get("license_code")
        if not lcode:
            continue
        md = project_license(rec, rev_req, feat_codes)
        (out_dir / (sanitize(lcode) + ".md")).write_text(md, encoding="utf-8")
        n += 1

    update_local_index(nf, ver, licenses)
    print(f"Compiled {n} licenses → assets/license/{nf}/{ver}/")
    print(f"Evidence → assets/evidence/{nf}/{ver}/ (与命令/特性层共用去重)")
    print(f"Local index updated.")


if __name__ == "__main__":
    main()
