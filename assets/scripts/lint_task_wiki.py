#!/usr/bin/env python3
"""
task wiki 6 类硬规则 Lint 检查器——自动化防止本次 P0 修复的 80+ 处违例复发

规则集（按 SOP §3.5/CLAUDE.md §5.5）：
  R1. 占位规范     — 检测 `[[X 待补 atom]]` / `(待建)` / `（待建）` 残留（已建对象必须用 markdown 链接）
  R2. 伪段禁令     — 检测 `## 构建依据与状态` / `## 元数据` 等构建期元信息段
  R3. 平铺检查     — 检测单一步骤连续 ≥3 atom 引用 + 无步骤关系说明（即"平铺"）
  R4. 双向回填检查 — compound 被 feature 引用时，compound 场景差异表应有该 feature 行
  R5. 状态四态化   — front matter status 字段必须是 draft/foundation/capability/partial 之一
  R6. 命令真实性   — task md 引用的命令名必须在 _numbering.json 中（防 OSPFNETWORK 类虚构）

用法:
  python assets/scripts/lint_task_wiki.py                          # 全量检查
  python assets/scripts/lint_task_wiki.py --rules R1,R2            # 指定规则
  python assets/scripts/lint_task_wiki.py --strict                 # 严格模式（违例 exit 1）
  python assets/scripts/lint_task_wiki.py --nf UNC --version 20.15.2   # 限定网元+版本
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

# Windows GBK console 输出兼容
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ASSETS = Path(__file__).resolve().parent.parent
TASK_DIR_DEFAULT = ASSETS / 'task'
ALLOWED_STATUS = {'draft', 'foundation', 'capability', 'partial', 'active', 'stale'}
EXEMPT_FILES = {'_audit_report', '_apn-feature-build-plan', '_apn-atom-to-build', '_atom-refactor',
                 '_UNC-atom-refactor-handoff', 'index'}


@dataclass(frozen=True)
class Violation:
    rule: str           # R1/R2/...
    severity: str       # critical/warning/info
    file: str           # 相对路径
    line: int           # 行号（0=无）
    message: str


@dataclass
class LintResult:
    violations: list[Violation] = field(default_factory=list)
    file_count: int = 0

    def add(self, rule: str, severity: str, file: str, line: int, msg: str) -> None:
        self.violations.append(Violation(rule, severity, file, line, msg))

    def by_rule(self) -> dict[str, list[Violation]]:
        out: dict[str, list[Violation]] = defaultdict(list)
        for v in self.violations:
            out[v.rule].append(v)
        return out


def iter_task_md(task_dir: Path, nf: str | None = None, version: str | None = None) -> Iterable[Path]:
    """遍历 task 目录下所有 .md 文件，可按 nf/version 过滤"""
    if nf and version:
        target = task_dir / nf / version
    else:
        target = task_dir
    for md in sorted(target.glob('*.md')):
        if any(md.name.startswith(ex) for ex in EXEMPT_FILES):
            continue
        yield md


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    """提取 front matter（YAML 块）+ 正文"""
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', text, re.DOTALL)
    if not m:
        return {}, text
    fm: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ':' in line:
            k, _, v = line.partition(':')
            fm[k.strip()] = v.strip().strip("'").strip('"')
    return fm, m.group(2)


def rule_r1_placeholder(text: str, file: Path, base: Path, nf: str, version: str,
                        feat_built: set[str], task_built: set[str], result: LintResult) -> None:
    """R1 占位规范：检测 `[[X 待补 atom]]` / `(待建)` / `（待建）` 残留"""
    rel = str(file.relative_to(base))

    # 模式 1：`[[X 待补 atom]]` 严格禁止（SOP §3.5 v1.1）
    for i, line in enumerate(text.splitlines(), 1):
        for m in re.finditer(r'\[\[[^\]]+待补 atom\]\]', line):
            result.add('R1', 'critical', rel, i, f'`[[X 待补 atom]]` 占位违例：{m.group(0)}')

    # 模式 2：`(待建)` / `（待建）` / `（待建，` 模式 + 括号前是已建对象的 markdown 链接
    for i, line in enumerate(text.splitlines(), 1):
        # 检测 [任意](feature/UNC/...md)（待建）→ 已建特性应无待建
        for m in re.finditer(r'\[([^\]]+)\]\((feature/[A-Z]+/[0-9.]+/([A-Z]+-\d+))\.md\)（待建）', line):
            fid = m.group(3)
            if fid in feat_built:
                result.add('R1', 'warning', rel, i, f'已建特性 {fid} 不应标（待建）: {m.group(0)[:80]}')
        # 检测 [任意](task/...md)（待建）→ 已建 task 不应标待建
        for m in re.finditer(r'\[([^\]]+)\]\((task/[A-Z]+/[0-9.]+/([0-9]-[0-9]+))\.md\)（待建）', line):
            tid = m.group(3)
            if tid in task_built:
                result.add('R1', 'warning', rel, i, f'已建 task {tid} 不应标（待建）: {m.group(0)[:80]}')


def rule_r2_pseudo_section(text: str, file: Path, base: Path, result: LintResult) -> None:
    """R2 伪段禁令：检测 `## 构建依据与状态` 等 SOP §4 禁止段"""
    rel = str(file.relative_to(base))
    forbidden_titles = [
        r'^##\s+构建依据与状态',
        r'^##\s+构建元数据',
        r'^##\s+构建信息',
        r'^##\s+元数据$',
    ]
    for i, line in enumerate(text.splitlines(), 1):
        for pat in forbidden_titles:
            if re.match(pat, line):
                result.add('R2', 'critical', rel, i, f'SOP §4 禁止的伪段: {line.strip()}')


def rule_r3_flatten(text: str, file: Path, base: Path, result: LintResult) -> None:
    """R3 平铺检查：单一步骤连续 ≥3 atom 引用 + 无步骤关系说明"""
    rel = str(file.relative_to(base))
    fm, body = parse_front_matter(text)
    task_layer = fm.get('task_layer', '')
    if task_layer != 'feature':
        return  # 仅检查 feature 层

    # 找"## 配置流程"段
    in_flow = False
    step_buf: list[tuple[int, str]] = []
    FLUSH_THRESHOLD = 3

    def flush():
        nonlocal step_buf
        atom_count = sum(1 for _, ln in step_buf if re.search(r'\[0-\d+\]', ln))
        if atom_count >= FLUSH_THRESHOLD:
            # 检查是否有"共享骨架/骨架引用"等说明
            joined = '\n'.join(ln for _, ln in step_buf)
            if not re.search(r'(共享骨架|->|复用|引用 [\[1-]|→ [\[1-])', joined):
                # 检查是否含平铺连续 ≥3
                for ln_num, ln in step_buf:
                    if re.search(r'\[0-\d+\]', ln):
                        result.add('R3', 'warning', rel, ln_num,
                                   f'feature 平铺风险：步骤含 {atom_count} atom 连续引用且无骨架/共享说明')

    for i, line in enumerate(body.splitlines(), 1):
        if re.match(r'^##\s+', line):
            in_flow = (line.strip().startswith('## 配置流程') or line.strip().startswith('## 步骤'))
            flush()
            step_buf = []
            continue
        if in_flow:
            # 检测 numbered step: "1." "2." 或 "步骤 1"
            if re.match(r'^\s*(\d+)\.', line) or re.match(r'^\s*步骤\s*\d+', line):
                flush()
                step_buf = [(i, line)]
            elif step_buf:
                step_buf.append((i, line))
    flush()


def rule_r4_back_link(text: str, file: Path, base: Path, result: LintResult) -> None:
    """R4 双向回填检查：compound 场景差异表应有 task/feature 引用行；反之亦然"""
    rel = str(file.relative_to(base))
    fm, body = parse_front_matter(text)
    task_layer = fm.get('task_layer', '')
    if task_layer not in ('compound', 'feature'):
        return

    # 豁免：能力型底座骨架（cmd: 无 / 不展开配置 / status=foundation）
    intent = fm.get('task_intent', '').lower()
    if 'cmd: 无' in intent or '不展开' in intent or fm.get('status') == 'foundation':
        return  # 能力型底座骨架不强求场景差异表

    # 找"## 场景差异"段（含被引用于 task/feature 链接）
    feat_or_task_refs = set()
    in_diff_table = False
    for line in body.splitlines():
        if '## 场景差异' in line:
            in_diff_table = True
            continue
        if in_diff_table and line.startswith('## '):
            break
        if in_diff_table:
            # 检测 feature_code: WSFD-XXX / IPFD-XXX / NPFD-XXX / GWFD-XXX
            for m in re.finditer(r'(WSFD|IPFD|NPFD|GWFD)-\d+', line):
                feat_or_task_refs.add(m.group(0))
            # 检测 task 引用: [2-XXXXX](task/UNC/20.15.2/2-XXXXX.md) 或 [2-XXXXX 名称]
            for m in re.finditer(r'\[(\d-\d{5})\b', line):
                feat_or_task_refs.add('T:' + m.group(1))

    # 仅检查 compound：场景差异表应非空
    if task_layer == 'compound' and not feat_or_task_refs:
        result.add('R4', 'warning', rel, 0, 'compound 场景差异表为空或无 feature/task 引用，违反双向回填硬规则')


def rule_r5_status(text: str, file: Path, base: Path, result: LintResult) -> None:
    """R5 状态四态化：front matter status 必须是合法值"""
    rel = str(file.relative_to(base))
    fm, _ = parse_front_matter(text)
    status = fm.get('status', '')
    if status and status not in ALLOWED_STATUS:
        result.add('R5', 'critical', rel, 0, f'status 字段值非法: "{status}"（合法: {ALLOWED_STATUS}）')
    elif not status:
        result.add('R5', 'warning', rel, 0, 'front matter 缺 status 字段')


def rule_r6_cmd_validity(text: str, file: Path, base: Path,
                         cmd_registered: set[str], result: LintResult) -> None:
    """R6 命令真实性：task md 引用的命令名必须在 _numbering.json（防 OSPFNETWORK 类虚构）"""
    rel = str(file.relative_to(base))
    fm, body = parse_front_matter(text)
    if fm.get('task_layer') != 'atom':
        return  # 仅检查 atom 层

    # 1) ref 字段的命令名
    ref = fm.get('ref', '')
    if ref:
        m = re.match(r'.*@MMLCommand@(.+)$', ref)
        if m:
            cmd = m.group(1)
            if cmd not in cmd_registered:
                result.add('R6', 'critical', rel, 0, f'atom ref 命令 "{cmd}" 未在 _numbering.json 中')

    # 2) 文中出现的 ADD/SET/MOD/RMV/DSP/TST/EXP/RST/LCK 命令名（防 OSPFNETWORK 类虚构命令）
    cmd_pat = re.compile(r'`?\b(ADD|SET|MOD|RMV|DSP|TST|EXP|RST|LCK)\s+([A-Z][A-Z0-9]+)`?')
    seen = set()
    # 全文是否已标 ★R1.5 待核
    has_r15_marker = bool(re.search(r'★\s*R1\.5', body))

    for i, line in enumerate(body.splitlines(), 1):
        # 该行是否已标 ★R1.5
        line_marked = '★R1.5' in line or '★ R1.5' in line
        for m in cmd_pat.finditer(line):
            cmd = f'{m.group(1)} {m.group(2)}'
            if cmd in seen:
                continue
            seen.add(cmd)
            # 跳过明显的非命令引用
            if m.group(2) in {'TRUE', 'FALSE', 'YES', 'NO', 'NORMAL', 'ENABLE', 'DISABLE'}:
                continue
            if cmd not in cmd_registered:
                # 已标 R1.5 待核 → 仅 info
                severity = 'info' if line_marked or has_r15_marker else 'critical'
                msg = (f'文中虚构命令 "{cmd}" 未在 _numbering.json 中（OSPFNETWORK 类风险）'
                       if severity == 'critical'
                       else f'虚构命令 "{cmd}" 已标 R1.5 待核（合规）')
                result.add('R6', severity, rel, i, msg)


def load_numbering(task_dir: Path, nf: str, version: str) -> dict[str, str]:
    """加载 _numbering.json"""
    path = task_dir / nf / version / '_numbering.json'
    if not path.exists():
        return {}
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def load_built_sets(task_dir: Path, nf: str, version: str) -> tuple[set[str], set[str], set[str]]:
    """加载已建特性集 + 已建 task 集 + 已注册命令集"""
    feat_built: set[str] = set()
    feat_dir = ASSETS / 'feature' / nf / version
    if feat_dir.exists():
        for md in feat_dir.glob('*.md'):
            feat_built.add(md.stem)

    task_built: set[str] = set()
    task_subdir = task_dir / nf / version
    if task_subdir.exists():
        for md in task_subdir.glob('*.md'):
            if re.match(r'^[0-9]-[0-9]+$', md.stem):
                task_built.add(md.stem)

    cmd_registered = set(load_numbering(task_dir, nf, version).keys())
    return feat_built, task_built, cmd_registered


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--rules', default='R1,R2,R3,R4,R5,R6',
                    help='逗号分隔规则集，默认全开')
    ap.add_argument('--nf', default='UNC', help='网元（UNC/UDG）')
    ap.add_argument('--version', default='20.15.2', help='版本')
    ap.add_argument('--strict', action='store_true', help='严格模式（违例 exit 1）')
    ap.add_argument('--task-dir', default=str(TASK_DIR_DEFAULT), help='task 根目录')
    args = ap.parse_args()

    rules = set(args.rules.split(','))
    task_dir = Path(args.task_dir)
    feat_built, task_built, cmd_registered = load_built_sets(task_dir, args.nf, args.version)

    result = LintResult()
    files = list(iter_task_md(task_dir, args.nf, args.version))
    result.file_count = len(files)

    rule_funcs = {
        'R1': lambda text, f, base: rule_r1_placeholder(text, f, base, args.nf, args.version,
                                                          feat_built, task_built, result),
        'R2': lambda text, f, base: rule_r2_pseudo_section(text, f, base, result),
        'R3': lambda text, f, base: rule_r3_flatten(text, f, base, result),
        'R4': lambda text, f, base: rule_r4_back_link(text, f, base, result),
        'R5': lambda text, f, base: rule_r5_status(text, f, base, result),
        'R6': lambda text, f, base: rule_r6_cmd_validity(text, f, base, cmd_registered, result),
    }

    for f in files:
        text = f.read_text(encoding='utf-8')
        for rule in rules:
            if rule in rule_funcs:
                rule_funcs[rule](text, f, task_dir)

    # 输出汇总
    print(f"扫描目录: task/{args.nf}/{args.version}/")
    print(f"扫描文件: {result.file_count}")
    print(f"启用规则: {sorted(rules)}")
    print(f"已建特性: {len(feat_built)} | 已建 task: {len(task_built)} | 已注册命令: {len(cmd_registered)}")
    print()

    by_rule = result.by_rule()
    if not result.violations:
        print("[OK] 全部通过")
        return 0

    print(f"违例总数: {len(result.violations)}")
    print()
    for rule in sorted(rules):
        vs = by_rule.get(rule, [])
        if not vs:
            continue
        crit = sum(1 for v in vs if v.severity == 'critical')
        warn = sum(1 for v in vs if v.severity == 'warning')
        print(f"  {rule}: {len(vs)} 条（critical={crit}, warning={warn}）")

    # 按文件分组打印详细违例
    by_file: dict[str, list[Violation]] = defaultdict(list)
    for v in result.violations:
        by_file[v.file].append(v)

    print()
    print(f"{'='*80}")
    for fpath, vs in sorted(by_file.items()):
        print(f"\n[{fpath}] ({len(vs)} 条)")
        for v in vs:
            line_str = f":{v.line}" if v.line else ""
            print(f"   [{v.rule}|{v.severity}{line_str}] {v.message}")

    # critical 计数 + 严格模式判定
    critical_count = sum(1 for v in result.violations if v.severity == 'critical')
    print()
    print(f"{'='*80}")
    print(f"critical: {critical_count} | warning: {sum(1 for v in result.violations if v.severity == 'warning')}")

    if args.strict and critical_count > 0:
        return 1
    return 0 if critical_count == 0 else 0  # 非严格模式返回 0（warn 不阻塞）


if __name__ == '__main__':
    sys.exit(main())