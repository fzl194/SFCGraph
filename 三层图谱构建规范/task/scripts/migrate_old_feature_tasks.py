#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
迁移脚本：旧 feature_task (2-XXXXX.md) → FeatureTask ({NF}@FeatureTask@{feature_code}.md)

feature_code 锚（1:1，从 ref 读，不需 slug 表）。8 字段（ref→Feature）。
关联段边：编排 compound / 直接引用 atom + 对应特性(正向)。迁移后回填 Feature 反向边。
**跨 nf 引用**：从 href/wiki4 提 nf（task/UDG/、@UDG@），用对应 nf 的 map（修 CRITICAL 错链）。

复用 migrate_old_compounds 的纯函数 + slug 表；重写链接转换支持跨 nf。
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))
from migrate_old_compounds import (  # noqa: E402
    parse_yaml, extract_yaml_and_body, build_command_map,
    _protect_code_blocks, _restore_code_blocks,
    transform_decision_title, strip_dp_inline_refs, strip_rule_refs,
    strip_orphan_bold_dp_marker, strip_standalone_rule_marker, strip_paren_num,
    SLUG_MAP as UDG_COMPOUND_SLUGS, SLUG_MAP_UNC as UNC_COMPOUND_SLUGS,
)

DEFAULT_NF = "UDG"
DEFAULT_VERSION = "20.15.2"
ROOT = Path(__file__).resolve().parents[3]
NF = DEFAULT_NF
VERSION = DEFAULT_VERSION
SRC_DIR = ROOT / "assets" / "task" / NF / VERSION
DST_DIR = ROOT / "三层图谱资产" / "FeatureTask" / NF / VERSION
FEATURE_DIR_ROOT = ROOT / "三层图谱资产" / "Feature"
FEATURE_NUM_RE = re.compile(r"^2-(\d{5})\.md$")

# 覆盖 import 的正则：href 排除 | 和换行（防源坏链 `path.md|` 跨行吞下一单元格 → 嵌套 wiki）
MD_LINK_RE = re.compile(r"\[([^\]\n]*)\]\(([^)*|\n]+)\)")
# wiki4 占位提 nf：[[UDG@20.15.2@Type@Local]] / [[UNC@...]]
WIKI4_RE = re.compile(r"\[+(UDG|UNC)@20\.15\.2@(\w+)@([^\]\n]+?)\]+")
VALID_NF = ("UDG", "UNC")


def compound_slugmap(nf: str) -> Dict[str, str]:
    return UDG_COMPOUND_SLUGS if nf == "UDG" else UNC_COMPOUND_SLUGS


def build_feature_map(src_dir: Path) -> Dict[str, str]:
    table: Dict[str, str] = {}
    for f in sorted(src_dir.iterdir()):
        if not FEATURE_NUM_RE.match(f.name):
            continue
        try:
            text = f.read_text(encoding="utf-8")
        except Exception:
            continue
        scalar, _ = extract_yaml_and_body(text)[:2]
        ref = scalar.get("ref", "")
        fc = ref.split("@")[-1].strip()
        if fc and fc not in ("null", "None"):
            table[f.stem] = fc
    return table


def build_all_maps(version: str) -> Dict[str, Dict[str, Dict]]:
    """双 nf maps：{nf: {atom:cmdmap, compound:slugmap, feature:fmap}}。"""
    maps: Dict[str, Dict[str, Dict]] = {}
    for nf in VALID_NF:
        src = ROOT / "assets" / "task" / nf / version
        if not src.is_dir():
            continue
        maps[nf] = {
            "atom": build_command_map(src),
            "compound": compound_slugmap(nf),
            "feature": build_feature_map(src),
        }
    return maps


def nf_from_href(href: str, cur_nf: str) -> str:
    """从 href 提 nf（task/UDG/、feature/UDG/、command/UDG/ 等）；提不到用 cur_nf。"""
    m = re.match(r"^[a-z]+/(UDG|UNC)/", href)
    return m.group(1) if m else cur_nf


# ───────────────────────── 链接转换（跨 nf） ─────────────────────────

def convert_markdown_links(text: str, all_maps, cur_nf) -> str:
    def repl(m: re.Match) -> str:
        label, href = m.group(1), m.group(2)
        nf = nf_from_href(href, cur_nf)
        mp = all_maps.get(nf, all_maps[cur_nf])
        cmdmap, slugmap, fmap = mp["atom"], mp["compound"], mp["feature"]
        if href.startswith("command/"):
            base = re.sub(r"\.md$", "", href.rsplit("/", 1)[-1])
            return f"[[{nf}@MMLCommand@{base.replace('-', ' ')}]]"
        if href.startswith("configobject/"):
            return ""
        if href.startswith("evidence/"):
            return ""
        if href.startswith("business/"):
            return label
        if href.startswith("feature/"):
            base = re.sub(r"\.md$", "", href.rsplit("/", 1)[-1])
            return f"[[{nf}@Feature@{base}]]"
        if href == "#":
            return ""
        fname = href.rsplit("/", 1)[-1]
        if re.match(r"^(CS|NS|BD|ConfigurationSolution|NetworkScenario|BusinessDomain)@", fname):
            return label
        m_atom = re.match(r"^(0-\d{5})\.md$", fname)
        if m_atom:
            cmd = cmdmap.get(m_atom.group(1))
            return f"[[{nf}@AtomTask@{cmd}]]" if cmd else label
        m_comp = re.match(r"^(1-\d{5})\.md$", fname)
        if m_comp:
            slug = slugmap.get(m_comp.group(1))
            return f"[[{nf}@CompoundTask@{slug}]]" if slug else label
        m_feat = re.match(r"^(2-\d{5})\.md$", fname)
        if m_feat:
            fc = fmap.get(m_feat.group(1))
            return f"[[{nf}@FeatureTask@{fc}]]" if fc else label
        return label
    return MD_LINK_RE.sub(repl, text)


def convert_wiki4_placeholders(text: str, all_maps, cur_nf) -> str:
    def repl(m: re.Match) -> str:
        nf = m.group(1)
        typ, local = m.group(2), m.group(3)
        mp = all_maps.get(nf, all_maps[cur_nf])
        cmdmap, slugmap, fmap = mp["atom"], mp["compound"], mp["feature"]
        if typ == "MMLCommand":
            return f"[[{nf}@MMLCommand@{local}]]"
        if typ == "Task":
            if local.startswith("0-"):
                cmd = cmdmap.get(local)
                return f"[[{nf}@AtomTask@{cmd}]]" if cmd else m.group(0)
            if local.startswith("1-"):
                slug = slugmap.get(local)
                return f"[[{nf}@CompoundTask@{slug}]]" if slug else m.group(0)
            if local.startswith("2-"):
                fc = fmap.get(local)
                return f"[[{nf}@FeatureTask@{fc}]]" if fc else m.group(0)
            return m.group(0)
        if typ == "Feature":
            return f"[[{nf}@Feature@{local}]]"
        if typ in ("DecisionPoint", "ConfigObject"):
            return ""
        return m.group(0)
    return WIKI4_RE.sub(repl, text)


def replace_bare_refs(text: str, cmdmap, slugmap, fmap) -> str:
    """裸编号无 nf 上下文，用 cur_nf 本地 map（跨 nf 裸编号罕见）。"""
    text = re.sub(r"§\s*[0-9]-\d{5}(?:-\d+)?", "", text)
    text = re.sub(r"(feature-rule|selection_rule)\s*[0-9]-\d{5}(?:-\d+)?", r"\1", text)

    def repl_multi(m: re.Match) -> str:
        out = []
        for n in re.findall(r"[012]-\d{5}", m.group(0)):
            if n.startswith("0-") and cmdmap.get(n):
                out.append(f"[[{NF}@AtomTask@{cmdmap[n]}]]")
            elif n.startswith("1-") and slugmap.get(n):
                out.append(f"[[{NF}@CompoundTask@{slugmap[n]}]]")
            elif n.startswith("2-") and fmap.get(n):
                out.append(f"[[{NF}@FeatureTask@{fmap[n]}]]")
            else:
                out.append(n)
        return "/".join(out)
    text = re.sub(r"(?:[012]-\d{5}(?:/[012]-\d{5})+)", repl_multi, text)

    def repl_atom(m):
        cmd = cmdmap.get(m.group(0))
        return f"[[{NF}@AtomTask@{cmd}]]" if cmd else m.group(0)
    text = re.sub(r"(?<![\w/.-])0-\d{5}(?![a-zA-Z0-9/])", repl_atom, text)

    def repl_comp(m):
        slug = slugmap.get(m.group(0))
        return f"[[{NF}@CompoundTask@{slug}]]" if slug else m.group(0)
    text = re.sub(r"(?<![\w/.-])1-\d{5}(?![a-zA-Z0-9/])", repl_comp, text)

    def repl_feat(m):
        fc = fmap.get(m.group(0))
        return f"[[{NF}@FeatureTask@{fc}]]" if fc else m.group(0)
    text = re.sub(r"(?<![\w/.-])2-\d{5}(?![a-zA-Z0-9/])", repl_feat, text)
    return text


# ───────────────────────── 关联段 → 边 ─────────────────────────

def parse_assoc_to_edges(body: str, cmdmap, slugmap) -> Tuple[str, List[Tuple[str, str]]]:
    m = re.search(r"^##\s+关联\s*$", body, re.M)
    if not m:
        return body, []
    head = body[: m.start()].rstrip() + "\n"
    after = body[m.end():]
    tail_m = re.search(r"^##\s+", after, re.M)
    assoc = after[: tail_m.start()] if tail_m else after
    tail = after[tail_m.start():] if tail_m else ""

    edges: List[Tuple[str, str]] = []
    seen = set()

    def add(label, target):
        if (label, target) not in seen:
            seen.add((label, target))
            edges.append((label, target))

    for line in assoc.splitlines():
        s = line.strip()
        ml = re.match(r"^-\s*([^：:]+)[：:]\s*(.*)$", s)
        if not ml:
            continue
        raw = ml.group(1).strip()
        rest = ml.group(2)
        low = raw.lower()
        if "编排" in raw and "compound" in low:
            elabel = "编排 compound"
        elif "直接引用" in raw and "atom" in low:
            elabel = "直接引用 atom"
        else:
            continue
        for num in re.findall(r"1-\d{5}", rest):
            slug = slugmap.get(num)
            if slug:
                add(elabel, f"{NF}@CompoundTask@{slug}")
        for num in re.findall(r"0-\d{5}", rest):
            cmd = cmdmap.get(num)
            if cmd:
                add(elabel, f"{NF}@AtomTask@{cmd}")
    new_body = head + "\n" + tail.lstrip("\n")
    return new_body, edges


_EDGE_ORDER = {"对应特性": 0, "编排 compound": 1, "直接引用 atom": 2}


def render_edges(edges: List[Tuple[str, str]]) -> str:
    if not edges:
        return "## 边\n"
    ordered = sorted(edges, key=lambda e: (_EDGE_ORDER.get(e[0], 9), e[1]))
    return "\n".join(["## 边"] + [f"- {l}: [[{t}]]" for l, t in ordered]) + "\n"


def backfill_feature_edge(fcode: str) -> Tuple[bool, str]:
    feat_ov = FEATURE_DIR_ROOT / NF / VERSION / f"{NF}@Feature@{fcode}" / "概述.md"
    if not feat_ov.exists():
        return False, f"Feature 概述不存在: {feat_ov.name}"
    txt = feat_ov.read_text(encoding="utf-8")
    edge_line = f"- 对应特性task: [[{NF}@FeatureTask@{fcode}]]"
    if edge_line in txt:
        return True, "已有反向边"
    m = re.search(r"^## 边\s*\n(.*?)(?:\n#|\Z)", txt, re.S | re.M)
    if not m:
        txt = txt.rstrip() + f"\n\n## 边\n{edge_line}\n"
    else:
        new_body = m.group(1).rstrip() + f"\n{edge_line}\n"
        tail = txt[m.end():]
        txt = txt[:m.start()] + "## 边\n" + new_body + (("\n" + tail) if tail else "")
    feat_ov.write_text(txt, encoding="utf-8")
    return True, "已加反向边"


def process_body(body: str, all_maps, cur_nf) -> str:
    body, ph = _protect_code_blocks(body)
    cur = all_maps[cur_nf]
    body = transform_decision_title(body)
    body = strip_rule_refs(body)
    body = convert_markdown_links(body, all_maps, cur_nf)
    body = convert_wiki4_placeholders(body, all_maps, cur_nf)
    body = strip_dp_inline_refs(body)
    body = replace_bare_refs(body, cur["atom"], cur["compound"], cur["feature"])
    body = strip_paren_num(body)
    body = strip_orphan_bold_dp_marker(body)
    body = strip_standalone_rule_marker(body)
    body = _restore_code_blocks(body, ph)
    return body


def render_yaml(scalar: Dict[str, str], fcode: str) -> str:
    name_zh = scalar.get("task_logical_name", "").strip()
    status = scalar.get("status", "").strip() or "draft"
    return "\n".join([
        "---",
        f'id: "{NF}@FeatureTask@{fcode}"',
        f'type: "FeatureTask"',
        f'name: "{fcode}"',
        f'name_zh: "{name_zh}"',
        f'nf: "{NF}"',
        f'version: "{VERSION}"',
        f'ref: "{NF}@Feature@{fcode}"',
        f'status: "{status}"',
        "---", "",
    ])


def migrate_one(src_path: Path, all_maps, cur_nf) -> Tuple[Path, str, List[Tuple[str, str]]]:
    text = src_path.read_text(encoding="utf-8")
    scalar, _, _, body = extract_yaml_and_body(text)
    fcode = all_maps[cur_nf]["feature"][src_path.stem]
    edges: List[Tuple[str, str]] = [("对应特性", f"{NF}@Feature@{fcode}")]
    cur = all_maps[cur_nf]
    body, assoc_edges = parse_assoc_to_edges(body, cur["atom"], cur["compound"])
    edges += assoc_edges
    new_body = process_body(body, all_maps, cur_nf)
    new_yaml = render_yaml(scalar, fcode)
    edge_section = render_edges(edges)
    new_text = new_yaml + new_body.rstrip() + "\n\n" + edge_section
    out_path = DST_DIR / f"{NF}@FeatureTask@{fcode}.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(new_text, encoding="utf-8")
    return out_path, fcode, edges


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(prog="migrate_old_feature_tasks")
    parser.add_argument("--nf", default=DEFAULT_NF)
    parser.add_argument("--version", default=DEFAULT_VERSION)
    parser.add_argument("filename", nargs="?", default=None)
    parser.add_argument("--no-backfill", action="store_true")
    args = parser.parse_args(argv[1:])

    global NF, VERSION, SRC_DIR, DST_DIR
    NF = args.nf
    VERSION = args.version
    SRC_DIR = ROOT / "assets" / "task" / NF / VERSION
    DST_DIR = ROOT / "三层图谱资产" / "FeatureTask" / NF / VERSION
    if not SRC_DIR.is_dir():
        print(f"ERR: src not found: {SRC_DIR}", file=sys.stderr)
        return 2

    all_maps = build_all_maps(VERSION)
    print(f"[maps] " + ", ".join(
        f"{nf}(atom={len(m['atom'])} comp={len(m['compound'])} feat={len(m['feature'])})"
        for nf, m in all_maps.items()), file=sys.stderr)

    targets: List[Path] = []
    if args.filename:
        p = SRC_DIR / args.filename
        if not p.is_file():
            print(f"ERR: {p}", file=sys.stderr)
            return 2
        targets.append(p)
    else:
        for f in sorted(SRC_DIR.iterdir()):
            if FEATURE_NUM_RE.match(f.name):
                targets.append(f)

    print(f"[migrate {NF}] {len(targets)} files", file=sys.stderr)
    written = 0
    bk_ok = bk_skip = bk_fail = 0
    for p in targets:
        out_path, fcode, edges = migrate_one(p, all_maps, NF)
        written += 1
        if not args.no_backfill:
            ok, _ = backfill_feature_edge(fcode)
            if ok:
                bk_ok += 1
            else:
                bk_fail += 1
        if args.filename:
            print(f"[dry-run] {p.name} -> {out_path.name} (edges:{len(edges)})", file=sys.stderr)
            print("=" * 60, file=sys.stderr)
            print(out_path.read_text(encoding="utf-8"))
    print(f"[done {NF}] {written} migrated | 反向边回填: 成功{bk_ok} 概述缺失{bk_fail}",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
