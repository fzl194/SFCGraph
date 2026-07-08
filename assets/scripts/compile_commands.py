#!/usr/bin/env python3
"""
命令层 Compile 器（Typed LLM Wiki）
把 CommandGraph/data/assets/{nf}/{version}/mml_commands.jsonl 投影成
assets/command/{nf}/{version}/<local>.md —— 纯代码投影，不需 LLM。

副作用：
  - 写命令 typed md 到 assets/command/{nf}/{version}/
  - 拷贝原始命令手册到 assets/evidence/{nf}/{version}/（可剥离）
  - 更新 assets/command/{nf}/{version}/index.md（局部 index，按 category_path 分组）

用法:
  python assets/scripts/compile_commands.py --nf UDG --version 20.15.2 [--filter 计费]
"""
import argparse
import json
import re
import shutil
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / "CommandGraph" / "data" / "assets"
TASKS = REPO / "ConfigTask" / "assert"
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


def sanitize(s: str) -> str:
    """文件名友好：空白/路径分隔/特殊字符 → -，保留中文与点。"""
    return re.sub(r'[\s/\\:*?"<>|]+', '-', str(s)).strip('-')


def load_edges(nf: str, ver: str):
    """command_id → [object_id]（命令操作的 ConfigObject）。"""
    p = SRC / nf / ver / "command_object_edges.jsonl"
    m = {}
    for r in load_jsonl(p):
        cmd = r.get("from_command_ref") or r.get("command_ref") or r.get("command_id")
        obj = r.get("to_object_ref") or r.get("object_ref") or r.get("object_id")
        if cmd and obj:
            m.setdefault(cmd, []).append(obj)
    return m


def load_config_objects(nf: str, ver: str):
    p = SRC / nf / ver / "config_objects.jsonl"
    return {r.get("object_id"): r for r in load_jsonl(p) if r.get("object_id")}


def load_task_refs(nf: str, ver: str):
    """command_id → [task_id]，从 ConfigTask assert 的 atom task 反查（ref 含 MMLCommand）。"""
    m = {}
    d = TASKS / nf / ver / "tasks"
    if not d.exists():
        return m
    for fp in d.glob("*.yaml"):
        try:
            rec = yaml.safe_load(fp.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(rec, dict):
            continue
        tid = rec.get("task_id")
        ref = rec.get("ref")
        if tid and ref and "MMLCommand" in str(ref):
            m.setdefault(str(ref), []).append(tid)
    return m


def copy_evidence(src_rel: str, rec: dict) -> str:
    """把原始命令手册拷进 assets/evidence/{nf}/{version}/，返回 assets 内相对路径。"""
    src = REPO / src_rel
    nf = rec.get("nf")
    ver = rec.get("version")
    dst_dir = EVID / nf / ver
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst_name = sanitize(rec.get("command_name", "unknown")) + src.suffix
    dst = dst_dir / dst_name
    if src.exists():
        shutil.copyfile(src, dst)
    else:
        dst.write_text(f"(证据源缺失) {src_rel}\n", encoding="utf-8")
    return f"evidence/{nf}/{ver}/{dst_name}"


def project_command(rec: dict, edges: dict, config_objs: dict, task_refs: dict) -> str:
    cid = rec.get("command_id", "")
    name = rec.get("command_name", "")
    name_zh = rec.get("command_name_zh", "")
    title = f"{name}（{name_zh}）" if name_zh and name_zh != name else name

    fm = {
        "id": cid, "type": "MMLCommand", "name": title,
        "nf": rec.get("nf"), "version": rec.get("version"),
        "verb": rec.get("verb"), "object_keyword": rec.get("object_keyword"),
        "command_category": rec.get("command_category"),
        "applicable_nf": rec.get("applicable_nf") or [],
        "effect_mode": rec.get("effect_mode"),
        "is_dangerous": rec.get("is_dangerous"),
        "max_records": rec.get("max_records"),
        "category_path": rec.get("category_path") or [],
        "status": rec.get("status") or "active",
    }
    fm = {k: v for k, v in fm.items() if v is not None and v != []}

    parts = ["---",
             yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, default_flow_style=False).strip(),
             "---", "", f"# {title}", ""]

    cf = (rec.get("command_function") or "").strip()
    if cf:
        parts += ["## 功能", "", cf, ""]

    notes = rec.get("notes") or []
    if notes:
        parts += ["## 注意事项", ""]
        for n in notes:
            parts.append(str(n).strip())
            parts.append("")

    pt = (rec.get("permission_text") or "").strip()
    if pt:
        parts += ["## 权限", "", pt, ""]

    pd = (rec.get("parameter_description") or "").strip()
    if pd:
        parts += ["## 参数", "", pd, ""]

    objs = edges.get(cid, [])
    if objs:
        parts += ["## 操作的配置对象", ""]
        nf = rec.get("nf"); ver = rec.get("version")
        for oid in objs:
            o = config_objs.get(oid, {})
            local = str(oid).split('@')[-1]
            zh = o.get("object_name_zh") or o.get("object_name") or ""
            label = f"{zh}（{local}）" if zh else local
            ref = f"configobject/{nf}/{ver}/{sanitize(local)}"   # assets 根路径（ConfigObject md 已建）
            parts.append(f"- [[{ref}]] · {label}")
        parts.append("")

    tids = task_refs.get(cid, [])
    if tids:
        parts += ["## 关联任务", ""]
        for tid in sorted(set(tids)):
            parts.append(f"- [[{tid}]]")
        parts.append("")

    ex = rec.get("usage_examples") or []
    if ex:
        parts += ["## 使用实例", ""]
        for e in ex:
            parts.append(str(e).strip())
            parts.append("")

    ev = rec.get("source_evidence_ids") or []
    if ev:
        parts += ["## 证据", ""]
        for e in ev:
            ev_rel = copy_evidence(e, rec)
            parts.append(f"- 原始手册：`{ev_rel}`")
        parts.append("")

    return "\n".join(parts).rstrip() + "\n"


def update_local_index(nf: str, ver: str, commands: list):
    idx = ASSETS / "command" / nf / ver / "index.md"
    by_cat = {}
    for rec in commands:
        cat = " / ".join(rec.get("category_path") or []) or "未分类"
        name = rec.get("command_name", "")
        zh = rec.get("command_name_zh", "")
        cid = rec.get("command_id", "")
        fname = sanitize(name) + ".md"
        by_cat.setdefault(cat, []).append((cid, name, zh, fname))

    lines = [f"# index · command/{nf}/{ver}", "",
             "> 局部 index（Compile 自动生成，按 category_path 分组）。顶层导航见 ../../../index.md", ""]
    for cat in sorted(by_cat):
        lines.append(f"## {cat}")
        lines.append("")
        for cid, name, zh, fname in sorted(by_cat[cat], key=lambda x: x[1]):
            tail = f"（{zh}）" if zh and zh != name else ""
            lines.append(f"- [[{cid}]] · {name}{tail} — `{fname}`")
        lines.append("")
    idx.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nf", required=True)
    ap.add_argument("--version", required=True)
    ap.add_argument("--filter", default=None,
                    help="category_path 子串过滤，如 '计费'。不填=全量")
    args = ap.parse_args()

    cmds = load_jsonl(SRC / args.nf / args.version / "mml_commands.jsonl")
    edges = load_edges(args.nf, args.version)
    config_objs = load_config_objects(args.nf, args.version)
    task_refs = load_task_refs(args.nf, args.version)

    out_dir = ASSETS / "command" / args.nf / args.version
    out_dir.mkdir(parents=True, exist_ok=True)

    selected = []
    for rec in cmds:
        cat = " ".join(rec.get("category_path") or [])
        if args.filter and args.filter not in cat:
            continue
        md = project_command(rec, edges, config_objs, task_refs)
        fname = sanitize(rec.get("command_name", "unknown")) + ".md"
        (out_dir / fname).write_text(md, encoding="utf-8")
        selected.append(rec)

    update_local_index(args.nf, args.version, selected)
    print(f"Compiled {len(selected)} commands → assets/command/{args.nf}/{args.version}/")
    print(f"Evidence → assets/evidence/{args.nf}/{args.version}/")
    print(f"Local index updated.")


if __name__ == "__main__":
    main()
