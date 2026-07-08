#!/usr/bin/env python3
"""
ConfigObject Compile 器（Typed LLM Wiki）
把 CommandGraph/data/assets/{nf}/{version}/config_objects.jsonl 投影成
assets/configobject/{nf}/{version}/<local>.md —— 纯代码投影。

ConfigObject 是命令聚合枢纽（同一对象的 ADD/MOD/RMV/LST 命令族通过它串起来）。
双向链接：
  - 操作本对象的命令：从 command_object_edges 反查（命令→对象的反向）
  - 关联对象：object_refers_to（双向）
证据拷进 evidence/（可剥离）。

用法:
  python assets/scripts/compile_configobjects.py --nf UDG --version 20.15.2
"""
import argparse
import json
import re
import shutil
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / "CommandGraph" / "data" / "assets"
ASSETS = REPO / "assets"
EVID = ASSETS / "evidence"


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
    """四段式 ID → assets 根路径（无 .md 后缀，给 [[...]] 用）。"""
    parts = str(obj_id).split('@')
    if len(parts) >= 4:
        nf, ver = parts[0], parts[1]
        local = '@'.join(parts[3:])
        return f"{otype_dir}/{nf}/{ver}/{sanitize(local)}"
    return obj_id


def load_edges_both(nf: str, ver: str):
    """command_object_edges：正向 cmd→[obj]，反向 obj→[cmd]。"""
    p = SRC / nf / ver / "command_object_edges.jsonl"
    fwd, rev = {}, {}
    for r in load_jsonl(p):
        cmd = r.get("from_command_ref") or r.get("command_ref") or r.get("command_id")
        obj = r.get("to_object_ref") or r.get("object_ref") or r.get("object_id")
        if cmd and obj:
            fwd.setdefault(cmd, []).append(obj)
            rev.setdefault(obj, []).append(cmd)
    return fwd, rev


def load_object_refers(nf: str, ver: str):
    """object_refers_to：双向建 object↔[object]。"""
    p = SRC / nf / ver / "object_refers_to.jsonl"
    m = {}
    if not p.exists():
        return m
    for r in load_jsonl(p):
        a = r.get("from_object_ref") or r.get("object_ref") or r.get("source_id") or r.get("from")
        b = r.get("to_object_ref") or r.get("refers_to") or r.get("target_id") or r.get("to")
        if a and b:
            m.setdefault(a, []).append(b)
            m.setdefault(b, []).append(a)
    return m


def copy_evidence(src_rel: str, rec: dict, key: str) -> str:
    src = REPO / src_rel
    nf = rec.get("nf"); ver = rec.get("version")
    dst_dir = EVID / nf / ver
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst_name = sanitize(rec.get(key, "unknown")) + src.suffix
    dst = dst_dir / dst_name
    if src.exists():
        shutil.copyfile(src, dst)
    else:
        dst.write_text(f"(证据源缺失) {src_rel}\n", encoding="utf-8")
    return f"evidence/{nf}/{ver}/{dst_name}"


def project_config_object(rec: dict, rev_edges: dict, obj_refers: dict) -> str:
    oid = rec.get("object_id", "")
    oname = rec.get("object_name", "")
    oname_zh = rec.get("object_name_zh", "") or ""
    title = f"{oname}（{oname_zh}）" if oname_zh and oname_zh != oname else oname

    fm = {
        "id": oid, "type": "ConfigObject", "name": title,
        "nf": rec.get("nf"), "version": rec.get("version"),
        "object_name": oname, "object_kind": rec.get("object_kind"),
        "applicable_nf": rec.get("applicable_nf") or [],
        "identifier_parameters": rec.get("identifier_parameters") or [],
        "uniqueness_keys": rec.get("uniqueness_keys") or [],
        "status": rec.get("status") or "active",
    }
    fm = {k: v for k, v in fm.items() if v is not None and v != []}

    parts = ["---",
             yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, default_flow_style=False).strip(),
             "---", "", f"# {title}", ""]

    desc = (rec.get("description") or "").strip()
    if desc:
        parts += ["## 说明", "", desc, ""]

    cmds = rev_edges.get(oid, [])
    if cmds:
        parts += ["## 操作本对象的命令", ""]
        for cid in sorted(set(cmds)):
            clocal = str(cid).split('@')[-1]
            parts.append(f"- [[{id_to_path(cid, 'command')}]] · {clocal}")
        parts.append("")

    objs = [o for o in obj_refers.get(oid, []) if o != oid]
    if objs:
        parts += ["## 关联对象", ""]
        for o in sorted(set(objs)):
            olocal = str(o).split('@')[-1]
            parts.append(f"- [[{id_to_path(o, 'configobject')}]] · {olocal}")
        parts.append("")

    ev = list(dict.fromkeys(rec.get("source_evidence_ids") or []))
    if ev:
        parts += ["## 证据", ""]
        for e in ev:
            ev_rel = copy_evidence(e, rec, "object_name")
            parts.append(f"- 原始手册：`{ev_rel}`")
        parts.append("")

    return "\n".join(parts).rstrip() + "\n"


def update_local_index(nf: str, ver: str, objs: list):
    idx = ASSETS / "configobject" / nf / ver / "index.md"
    by_kind = {}
    for rec in objs:
        kind = rec.get("object_kind") or "未分类"
        oid = rec.get("object_id", "")
        oname = rec.get("object_name", "")
        oname_zh = rec.get("object_name_zh", "") or ""
        fname = sanitize(oname) + ".md"
        by_kind.setdefault(kind, []).append((oid, oname, oname_zh, fname))

    lines = [f"# index · configobject/{nf}/{ver}", "",
             "> 局部 index（Compile 自动生成，按 object_kind 分组）。顶层导航见 ../../../index.md", ""]
    for kind in sorted(by_kind):
        lines.append(f"## {kind}")
        lines.append("")
        for oid, oname, oname_zh, fname in sorted(by_kind[kind], key=lambda x: x[1]):
            tail = f"（{oname_zh}）" if oname_zh and oname_zh != oname else ""
            lines.append(f"- [[configobject/{nf}/{ver}/{oname}]] · {oname}{tail} — `{fname}`")
        lines.append("")
    idx.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nf", required=True)
    ap.add_argument("--version", required=True)
    args = ap.parse_args()

    objs = load_jsonl(SRC / args.nf / args.version / "config_objects.jsonl")
    _fwd, rev = load_edges_both(args.nf, args.version)
    obj_refers = load_object_refers(args.nf, args.version)

    out_dir = ASSETS / "configobject" / args.nf / args.version
    out_dir.mkdir(parents=True, exist_ok=True)

    n = 0
    for rec in objs:
        if not rec.get("object_id"):
            continue
        md = project_config_object(rec, rev, obj_refers)
        fname = sanitize(rec.get("object_name", "unknown")) + ".md"
        (out_dir / fname).write_text(md, encoding="utf-8")
        n += 1

    update_local_index(args.nf, args.version, objs)
    print(f"Compiled {n} config objects → assets/configobject/{args.nf}/{args.version}/")


if __name__ == "__main__":
    main()
