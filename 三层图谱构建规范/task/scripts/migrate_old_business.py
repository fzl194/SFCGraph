#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
迁移脚本：旧业务层 assets/business/{domain}/ → 新版 三层图谱资产/Business/{domain}/

把业务层 md（BD/NS/CS）从旧风格（assets/CLAUDE.md 约定：路径链接 + ## 关联 + 证据 + 旧编号 task 引用）
迁到新风格（三层图谱构建规范/business/SKILL.md：裸 [[逻辑ID]] + ## 边 + 无证据 + 7 字段 frontmatter）。

内容不改，只改风格：
  1. frontmatter 加 name_zh（= name）
  2. 所有 markdown 链接 → 裸 [[逻辑ID]]（task/{nf}/.../{0|1|2}-XXXXX.md → [[{nf}@{Type}@{anchor}]]；
     business/.../Type@slug.md → [[Type@slug]]；command/feature → MMLCommand/Feature）
  3. 正文裸旧编号（含 {UDG|UNC} num~num 范围）→ [[新ID]]
  4. ## 关联 段 → ## 边（按"源类型 × 目标类型"打 typed 边标签）；证据/SOP/审视/范本 行自然丢弃
  5. 证据链接 / ## 证据 段 → 删
  6. 结构：YAML 顶 → 内容中 → ## 边 底

映射来源：
  - atom 0-XXXXX → {nf}@AtomTask@{cmd}        （读 assets/task/{nf}/20.15.2/0-*.md 的 ref 末段）
  - compound 1-XXXXX → {nf}@CompoundTask@{slug}（SLUG_MAP / SLUG_MAP_UNC，与 migrate_old_compounds.py 同源）
  - feature_task 2-XXXXX → {nf}@FeatureTask@{code}（读 assets/task/{nf}/20.15.2/2-*.md 的 ref 末段）

用法：
  python migrate_old_business.py                      # 迁整个 business-awareness 域
  python migrate_old_business.py --dry one.cs.md      # 单文件 dry-run（打印，不写）
  python migrate_old_business.py --domain business-awareness
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[3]  # SFCGraph
VERSION = "20.15.2"
NFS = ("UDG", "UNC")
DOMAIN = "business-awareness"

SRC_DOMAIN = ROOT / "assets" / "business" / DOMAIN
DST_DOMAIN = ROOT / "三层图谱资产" / "Business" / DOMAIN

# ── compound slug 表：直接从 migrate_old_compounds 导入（同源，避免转录错误） ──
sys.path.insert(0, str(Path(__file__).resolve().parent))
from migrate_old_compounds import SLUG_MAP, SLUG_MAP_UNC  # noqa: E402

# ── 映射构建 ──
ATOM: Dict[str, Dict[str, str]] = {}
FT: Dict[str, Dict[str, str]] = {}
COMP: Dict[str, Dict[str, str]] = {}
UNRESOLVED: List[str] = []


def _ref_last_seg(path: Path) -> Optional[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return None
    m = re.search(r'^ref:\s*(.+)$', text, re.M)
    if not m:
        return None
    val = m.group(1).strip()
    if val in ("null", ""):
        return None
    return val.split("@")[-1].strip()


def build_maps() -> None:
    for nf in NFS:
        d = ROOT / "assets" / "task" / nf / VERSION
        atom, ft = {}, {}
        for f in sorted(d.glob("0-*.md")):
            cmd = _ref_last_seg(f)
            if cmd:
                atom[f.stem] = f"{nf}@AtomTask@{cmd}"
        for f in sorted(d.glob("2-*.md")):
            code = _ref_last_seg(f)
            if code:
                ft[f.stem] = f"{nf}@FeatureTask@{code}"
        ATOM[nf] = atom
        FT[nf] = ft
        slug_src = SLUG_MAP if nf == "UDG" else SLUG_MAP_UNC
        COMP[nf] = {k: f"{nf}@CompoundTask@{v}" for k, v in slug_src.items()}
    print(f"[maps] atom UDG/UNC={len(ATOM['UDG'])}/{len(ATOM['UNC'])} "
          f"compound={len(COMP['UDG'])}/{len(COMP['UNC'])} "
          f"feature_task={len(FT['UDG'])}/{len(FT['UNC'])}", file=sys.stderr)


def resolve(nf: str, num: str) -> Optional[str]:
    if num.startswith("0-"):
        return ATOM.get(nf, {}).get(num)
    if num.startswith("1-"):
        return COMP.get(nf, {}).get(num)
    if num.startswith("2-"):
        return FT.get(nf, {}).get(num)
    return None


# ── 链接/裸编号转换 ──
MD_LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
TASK_HREF_RE = re.compile(r"task/(UDG|UNC)/[\d.]+/([012]-\d{5})\.md")


def href_to_id(href: str) -> Optional[str]:
    """把 markdown 链接的 href 转成 [[逻辑ID]] 内部 ID（不含双方括号）。返回 None 表示该链接应丢弃。"""
    m = TASK_HREF_RE.search(href)
    if m:
        nf, num = m.group(1), m.group(2)
        nid = resolve(nf, num)
        if not nid:
            UNRESOLVED.append(f"task {nf} {num}")
            return None
        return nid
    m = re.search(r"(BusinessDomain|NetworkScenario|ConfigurationSolution)@[A-Za-z0-9_-]+\.md", href)
    if m:
        return m.group(0)[:-3]  # strip .md
    m = re.search(r"command/(UDG|UNC)/[\d.]+/(.+)\.md", href)
    if m:
        return f"{m.group(1)}@MMLCommand@{m.group(2).replace('-', ' ')}"
    m = re.search(r"feature/(UDG|UNC)/[\d.]+/(.+)\.md", href)
    if m:
        return f"{m.group(1)}@Feature@{m.group(2)}"
    if href.startswith("evidence/") or href.startswith("evidence\\"):
        return None  # 证据 → 丢弃
    return None  # 未知 → 丢弃链接


def convert_links_in_text(text: str) -> str:
    """正文里的 markdown 链接 → [[ID]]（裸）。evidence/未知 → 丢链接留 label 文字。"""
    def repl(m: re.Match) -> str:
        label, href = m.group(1), m.group(2)
        nid = href_to_id(href)
        if nid:
            return f"[[{nid}]]"
        return label  # 丢链接，留文字
    return MD_LINK_RE.sub(repl, text)


def convert_bare_numbers(text: str) -> str:
    """正文裸旧编号 → [[新ID]]。先处理 {UDG|UNC} 前缀（含范围），再处理孤立编号。"""
    # 1) {nf} num~num  范围（同 nf，仅取两端，中间 ~ 保留）
    def repl_range(m: re.Match) -> str:
        nf, a, b = m.group(1), m.group(2), m.group(3)
        ra, rb = resolve(nf, a), resolve(nf, b)
        if ra and rb:
            return f"{nf} [[{ra}]]~[[{rb}]]"
        return m.group(0)
    text = re.sub(r"(UDG|UNC)\s+([012]-\d{5})~([012]-\d{5})", repl_range, text)

    # 2) {nf} num  单个
    def repl_nf(m: re.Match) -> str:
        nf, num = m.group(1), m.group(2)
        nid = resolve(nf, num)
        if nid:
            return f"{nf} [[{nid}]]"
        return m.group(0)
    text = re.sub(r"(UDG|UNC)\s+([012]-\d{5})(?!\d)", repl_nf, text)

    # 3) 孤立 num（无 nf 前缀）：若仅一个 nf 能解析则用之，否则不动
    def repl_bare(m: re.Match) -> str:
        num = m.group(0)
        hits = [(nf, resolve(nf, num)) for nf in NFS if resolve(nf, num)]
        if len(hits) == 1:
            return f"[[{hits[0][1]}]]"
        if len(hits) > 1:
            UNRESOLVED.append(f"ambiguous bare {num} (both nfs)")
        return num
    text = re.sub(r"(?<![\w/.-])[012]-\d{5}(?![\w/-])", repl_bare, text)
    return text


# ── 代码块保护 ──
def protect_code(text: str) -> Tuple[str, List[str]]:
    ph: List[str] = []

    def repl_fence(m: re.Match) -> str:
        ph.append(m.group(0))
        return f"\x00CB{len(ph) - 1}\x00"
    text = re.sub(r"```.*?```", repl_fence, text, flags=re.S)

    def repl_inline(m: re.Match) -> str:
        ph.append(m.group(0))
        return f"\x00CI{len(ph) - 1}\x00"
    text = re.sub(r"`[^`\n]+`", repl_inline, text)
    return text, ph


def restore_code(text: str, ph: List[str]) -> str:
    for i, orig in enumerate(ph):
        text = text.replace(f"\x00CB{i}\x00", orig)
        text = text.replace(f"\x00CI{i}\x00", orig)
    return text


# ── ## 关联 → ## 边（按 源类型 × 目标类型 打标签） ──
EDGE_LABEL = {
    ("BusinessDomain", "ns"): "下游场景",
    ("NetworkScenario", "bd"): "上游域",
    ("NetworkScenario", "cs"): "下游方案",
    ("ConfigurationSolution", "ns"): "上游场景",
    ("ConfigurationSolution", "ft"): "编排特性",
    ("ConfigurationSolution", "compound"): "复用步骤",
    ("ConfigurationSolution", "atom"): "复用命令",
}
EDGE_ORDER = {
    "BusinessDomain": ["下游场景"],
    "NetworkScenario": ["上游域", "下游方案"],
    "ConfigurationSolution": ["上游场景", "编排特性", "复用步骤", "复用命令"],
}


def classify_target(href: str) -> Optional[Tuple[str, str]]:
    """从 href 判 (kind, id)。kind ∈ ns/cs/bd/ft/compound/atom。"""
    m = TASK_HREF_RE.search(href)
    if m:
        nf, num = m.group(1), m.group(2)
        nid = resolve(nf, num)
        if not nid:
            UNRESOLVED.append(f"assoc task {nf} {num}")
            return None
        kind = {"0": "atom", "1": "compound", "2": "ft"}[num[0]]
        return (kind, nid)
    for kind, typ in (("cs", "ConfigurationSolution"), ("ns", "NetworkScenario"),
                      ("bd", "BusinessDomain")):
        m = re.search(re.escape(typ) + r"@([A-Za-z0-9_-]+)\.md", href)
        if m:
            return (kind, f"{typ}@{m.group(1)}")
    return None


def assoc_to_edges(assoc_text: str, src_type: str) -> List[Tuple[str, str]]:
    """解析 ## 关联 段所有 markdown 链接 → 按 (src_type, target_kind) 归类边。"""
    grouped: Dict[str, List[str]] = defaultdict(list)
    seen: set = set()
    for label, href in MD_LINK_RE.findall(assoc_text):
        cls = classify_target(href)
        if not cls:
            continue
        kind, tid = cls
        elabel = EDGE_LABEL.get((src_type, kind))
        if not elabel:
            continue
        if tid not in seen:
            seen.add(tid)
            grouped[elabel].append(tid)
    edges: List[Tuple[str, str]] = []
    for elabel in EDGE_ORDER.get(src_type, []):
        for tid in grouped.get(elabel, []):
            edges.append((elabel, tid))
    return edges


def render_edges(edges: List[Tuple[str, str]]) -> str:
    if not edges:
        return "## 边\n"
    grouped: Dict[str, List[str]] = defaultdict(list)
    for label, tid in edges:
        grouped[label].append(tid)
    lines = ["## 边"]
    for label, tids in grouped.items():
        lines.append(f"- {label}: " + ", ".join(f"[[{t}]]" for t in tids))
    return "\n".join(lines) + "\n"


# ── frontmatter 加 name_zh ──
def add_name_zh(yaml_text: str) -> str:
    if re.search(r'^name_zh:', yaml_text, re.M):
        return yaml_text
    m = re.search(r'^(name:\s*)(.+)$', yaml_text, re.M)
    if not m:
        return yaml_text
    name_val = m.group(2).strip()
    return yaml_text.replace(m.group(0), m.group(0) + "\n" + f"name_zh: {name_val}", 1)


# ── 段落抽取工具 ──
def split_frontmatter(text: str) -> Tuple[str, str]:
    m = re.match(r'^---\n(.*?)\n---\n?(.*)$', text, re.S)
    if not m:
        return "", text
    return m.group(1), m.group(2)


def extract_section(body: str, title: str) -> Tuple[str, Optional[str]]:
    """抽 ## {title} 段（到下一个 ## 或 EOF）。返回 (去掉该段的 body, 段内容)。"""
    m = re.search(rf'^##\s+{re.escape(title)}\s*$', body, re.M)
    if not m:
        return body, None
    head = body[: m.start()]
    after = body[m.end():]
    nxt = re.search(r'^##\s+', after, re.M)
    section = after[: nxt.start()] if nxt else after
    tail = after[nxt.start():] if nxt else ""
    new_body = head.rstrip() + "\n\n" + tail.lstrip("\n") if tail else head.rstrip() + "\n"
    return new_body, section


# ── 单文件迁移 ──
def migrate_text(text: str) -> str:
    yaml_text, body = split_frontmatter(text)
    src_type_m = re.search(r'^type:\s*(.+)$', yaml_text, re.M)
    src_type = src_type_m.group(1).strip() if src_type_m else ""

    # 抽 ## 关联（→ 边）与 ## 证据（→ 删）
    body, assoc = extract_section(body, "关联")
    body, _evid = extract_section(body, "证据")

    # 代码块保护后转正文
    body, ph = protect_code(body)
    body = convert_links_in_text(body)
    body = convert_bare_numbers(body)
    body = restore_code(body, ph)

    # 关联段 → 边（关联段内也做一遍裸编号/链接不需要，因为 classify 直接读 href）
    edges: List[Tuple[str, str]] = []
    if assoc:
        edges = assoc_to_edges(assoc, src_type)

    # 拼装：YAML(加 name_zh) + 正文(rstrip) + 空行 + ## 边
    new_yaml = add_name_zh(yaml_text)
    edge_section = render_edges(edges)
    new_text = f"---\n{new_yaml}\n---\n\n" + body.strip() + "\n\n" + edge_section
    return new_text


def migrate_file(src: Path, dry: bool = False) -> Path:
    text = src.read_text(encoding="utf-8")
    new_text = migrate_text(text)
    rel = src.relative_to(SRC_DOMAIN)
    dst = DST_DOMAIN / rel
    if dry:
        print(f"===== DRY: {src.name} → {dst.relative_to(ROOT)} =====", file=sys.stderr)
        print(new_text)
        return dst
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(new_text, encoding="utf-8")
    return dst


def main(argv: List[str]) -> int:
    global DOMAIN, SRC_DOMAIN, DST_DOMAIN
    ap = argparse.ArgumentParser()
    ap.add_argument("--domain", default=DOMAIN)
    ap.add_argument("--dry", nargs="?", const="", default=None,
                    help="单文件 dry-run：--dry <相对路径或文件名>")
    args = ap.parse_args(argv[1:])

    DOMAIN = args.domain
    SRC_DOMAIN = ROOT / "assets" / "business" / DOMAIN
    DST_DOMAIN = ROOT / "三层图谱资产" / "Business" / DOMAIN
    if not SRC_DOMAIN.is_dir():
        print(f"ERR: src domain not found: {SRC_DOMAIN}", file=sys.stderr)
        return 2

    build_maps()

    if args.dry is not None:
        target = args.dry.strip()
        cand = [p for p in SRC_DOMAIN.rglob("*.md") if (not target or target in p.name or target in str(p.relative_to(SRC_DOMAIN)))]
        if not cand:
            print(f"ERR: no file matches '{target}'", file=sys.stderr)
            return 2
        for p in cand:
            migrate_file(p, dry=True)
        return 0

    files = sorted(p for p in SRC_DOMAIN.rglob("*.md") if not p.name.startswith("_"))
    print(f"[migrate] {len(files)} asset files in {DOMAIN} (excluded _-prefixed)", file=sys.stderr)
    for p in files:
        migrate_file(p)
    print(f"[done] {len(files)} migrated → {DST_DOMAIN.relative_to(ROOT)}", file=sys.stderr)
    if UNRESOLVED:
        print(f"[WARN] {len(UNRESOLVED)} unresolved refs:", file=sys.stderr)
        for u in sorted(set(UNRESOLVED)):
            print(f"  - {u}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
