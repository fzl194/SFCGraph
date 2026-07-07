#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""抽取 3 场景(计费/带宽控制/头增强)涉及的 UNC MML 命令清单。

用途: 批量构建 UNC 原子 task 前的初始范围确认。

流程:
  1. 计费/带宽控制: 从 业务图谱体系/{场景}/three-layer-graph/02-feature-graph.md 抽 UNC 特性(WSFD-*)
  2. 头增强族: GWFD-110261/110262/110263 (UDG-only, 在 UNC csv 里查不到 -> 预期空)
  3. 查 FeatureGraph/data/legacy/UNC_feature_files.csv 得每个特性的 md 文件
  4. 正则扫 md 抽 MML 命令 (VERB OBJECT)
  5. 去重, 输出每场景 + 总清单

用法: python extract_unc_commands.py
"""
import csv
import re
import sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[3]  # SFCGraph/

SCENARIO_GRAPH = {
    "计费":     "业务图谱体系/计费场景/three-layer-graph/02-feature-graph.md",
    "带宽控制": "业务图谱体系/带宽控制场景/three-layer-graph/02-feature-graph.md",
}
# 头增强族: UDG-only (无 UNC 侧), 显式列出以确认结果为空
EXTRA_FEATURES = {"头增强": ["GWFD-110261", "GWFD-110262", "GWFD-110263"]}

UNC_CSV = "FeatureGraph/data/legacy/UNC_feature_files.csv"

# MML 动词集 (UDG/UNC 共用); 对象关键字 = 大写字母/数字
VERBS = r"(?:ADD|SET|MOD|DEL|LST|DSP|RMV|ACT|DEA|CLR|RST|BKP|TST|INF|IMP|EXP|CRT|STR|CNT|SND|GET|RUN|CFG|DMP)"
CMD_RE = re.compile(rf"\b{VERBS}\s+([A-Z][A-Z0-9_]{{2,}})\b")
# 完整命令(含动词)用于最终清单
CMD_FULL_RE = re.compile(rf"\b({VERBS})\s+([A-Z][A-Z0-9_]{{2,}})\b")


def unc_features_from_graph(md_path: Path):
    """从 02-feature-graph.md 抽取 UNC 特性 ID (WSFD-\\d+), 去重保序。"""
    if not md_path.exists():
        print(f"[WARN] 未找到 {md_path}", file=sys.stderr)
        return []
    text = md_path.read_text(encoding="utf-8", errors="ignore")
    seen, out = set(), []
    for m in re.finditer(r"\b(WSFD-\d+)\b", text):
        fid = m.group(1)
        if fid not in seen:
            seen.add(fid)
            out.append(fid)
    return out


def load_unc_feature_files():
    """读 UNC_feature_files.csv -> {feature_id: [abs_md_path,...]}。"""
    csv_path = ROOT / UNC_CSV
    fmap = defaultdict(list)
    with csv_path.open(encoding="utf-8-sig", newline="") as f:
        rdr = csv.DictReader(f)
        for row in rdr:
            fid = (row.get("feature_id") or "").strip()
            fpath = (row.get("file_path") or "").strip()
            if fid and fpath:
                fmap[fid].append((ROOT / fpath).resolve())
    return fmap


def extract_commands(md_paths):
    """从一组 md 文件抽取 MML 命令 (VERB OBJECT), 返回 set。"""
    cmds = set()
    for p in md_paths:
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        for m in CMD_FULL_RE.finditer(text):
            verb, obj = m.group(1), m.group(2)
            cmds.add(f"{verb} {obj}")
    return cmds


def main():
    fmap = load_unc_feature_files()

    # 全部 UNC 特性 (校验: 这些特性在 csv 里是否有 md)
    scenario_features = {}
    for name, rel in SCENARIO_GRAPH.items():
        feats = unc_features_from_graph(ROOT / rel)
        scenario_features[name] = feats
    for name, feats in EXTRA_FEATURES.items():
        scenario_features[name] = feats

    print("=" * 70)
    print("UNC 特性范围 (按场景)")
    print("=" * 70)
    for name, feats in scenario_features.items():
        in_csv = [f for f in feats if f in fmap]
        not_in_csv = [f for f in feats if f not in fmap]
        print(f"\n[{name}] {len(feats)} 个特性")
        for f in feats:
            tag = f"({len(fmap.get(f, []))} md)" if f in fmap else "(UNC csv 无 -> UDG-only/空)"
            print(f"  {f} {tag}")
        if not_in_csv:
            print(f"  -> 无 UNC md 的: {not_in_csv}")

    print("\n" + "=" * 70)
    print("各场景 UNC MML 命令 (去重)")
    print("=" * 70)
    all_cmds = set()
    per_scenario = {}
    for name, feats in scenario_features.items():
        md_paths = []
        for f in feats:
            md_paths.extend(fmap.get(f, []))
        cmds = extract_commands(md_paths)
        per_scenario[name] = cmds
        all_cmds |= cmds
        print(f"\n[{name}] {len(cmds)} 条命令 (源 md {len(md_paths)} 个)")
        for c in sorted(cmds):
            print(f"  {c}")

    print("\n" + "=" * 70)
    print(f"合计去重 UNC 命令: {len(all_cmds)} 条")
    print("=" * 70)
    for c in sorted(all_cmds):
        # 标注该命令出现在哪些场景
        scenes = [n for n, cs in per_scenario.items() if c in cs]
        print(f"  {c:<35} [{', '.join(scenes)}]")

    # 写出文件供 review
    out = ROOT / "ConfigTask/task-build-skill/scripts/unc_command_scope.md"
    lines = ["# UNC 命令初始范围（3 场景：计费 / 带宽控制 / 头增强）\n",
             f"> 合计去重 {len(all_cmds)} 条。生成自 extract_unc_commands.py。\n"]
    for name, feats in scenario_features.items():
        lines.append(f"\n## {name}\n")
        lines.append(f"特性: {', '.join(feats) if feats else '(无)'}\n")
        cmds = sorted(per_scenario.get(name, set()))
        lines.append(f"命令 ({len(cmds)} 条):\n")
        for c in cmds:
            lines.append(f"- `{c}`\n")
    lines.append(f"\n## 合计去重 ({len(all_cmds)} 条)\n")
    for c in sorted(all_cmds):
        scenes = [n for n, cs in per_scenario.items() if c in cs]
        lines.append(f"- `{c}`  [{', '.join(scenes)}]\n")
    out.write_text("".join(lines), encoding="utf-8")
    print(f"\n已写出: {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
