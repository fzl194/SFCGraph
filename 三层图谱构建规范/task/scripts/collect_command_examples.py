#!/usr/bin/env python3
"""
atom 构建输入采集器：扫已构建的命令层 + 特性层资产，按命令归集"配置示例"，
输出 per-命令汇总 md（atom 构建的工作底稿，**非资产**，git ignore）。

对应: task/SKILL.md A.5 第一步。

输入（已构建资产；前置：Command + Feature 层已构建）:
  - 命令层: {storage}/Command/{nf}/{ver}/{nf}@MMLCommand@{cmd}.md     ← 命令真相
  - 特性层: {storage}/Feature/{nf}/{ver}/{nf}@Feature@{code}/*.md     ← 命令的真实配置示例

输出（中间态·非资产）:
  {storage}/_intermediates/atom-input/{nf}/{ver}/{cmd}.md

汇总 md 四段（agent 读它归纳 atom，不进 atom md）:
  ① 命令真相（功能/notes/参数表，来自命令层资产）
  ② 各特性配置范式（数据规划行/任务脚本/操作步骤上下文，来自特性层资产）
  ③ 配置方法差异汇总（自动派生：每参数取值分布 → DP 线索）
  ④ 数据源

用法:
  # 单命令
  python collect_command_examples.py --nf UDG --version 20.15.2 --cmd "ADD URR"

  # 全量（扫命令层资产发现所有命令）
  python collect_command_examples.py --nf UDG --version 20.15.2 --all

  # 干跑（只统计命中，不写）
  python collect_command_examples.py --nf UDG --version 20.15.2 --all --dry-run
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

# 三层图谱构建规范/task/scripts/ → SFCGraph/
REPO = Path(__file__).resolve().parents[3]
DEFAULT_STORAGE = "三层图谱资产"
INTERMEDIATE_TPL = "{storage}/_intermediates/atom-input/{nf}/{ver}/{cmd}.md"
NOHIT_TPL = "{storage}/_intermediates/atom-input/{nf}/{ver}/_no-hit.txt"

# 命令文件名: {nf}@MMLCommand@{cmd}.md → 提 {cmd}（local 保留空格）
_CMD_FILE_RE = re.compile(r"^(?P<nf>[^@]+)@MMLCommand@(?P<cmd>.+)\.md$")
# 特性文件夹: {nf}@Feature@{code}
# 通用前缀 [A-Z]+FD（覆盖 GWFD/WSFD/IPFD/NPFD/SFFD 及任何未来前缀，避免硬编码漏扫）
_FEATURE_DIR_RE = re.compile(r"^[^@]+@Feature@(?P<code>[A-Z]+FD-\d+)")


# ---------- 路径 ----------
def storage_root(storage: str) -> Path:
    p = Path(storage)
    return p if p.is_absolute() else REPO / p


def command_dir(storage: str, nf: str, ver: str) -> Path:
    return storage_root(storage) / "Command" / nf / ver


def feature_dir(storage: str, nf: str, ver: str) -> Path:
    return storage_root(storage) / "Feature" / nf / ver


def command_md_path(storage: str, nf: str, ver: str, cmd: str) -> Path:
    """命令层资产 md：文件名 = {nf}@MMLCommand@{cmd}.md（local 保留空格）。"""
    return command_dir(storage, nf, ver) / f"{nf}@MMLCommand@{cmd}.md"


def output_path(storage: str, nf: str, ver: str, cmd: str) -> Path:
    rel = INTERMEDIATE_TPL.format(storage=storage, nf=nf, ver=ver, cmd=cmd)
    return REPO / rel


# ---------- 命令发现 ----------
def discover_commands(storage: str, nf: str, ver: str) -> dict[str, Path]:
    """扫命令层资产，从文件名提命令全名。返回 {命令名 → md 路径}。"""
    base = command_dir(storage, nf, ver)
    cmds: dict[str, Path] = {}
    if not base.exists():
        return cmds
    for md in base.glob("*.md"):
        m = _CMD_FILE_RE.match(md.name)
        if m and m.group("nf") == nf:
            cmds.setdefault(m.group("cmd"), md)
    return cmds


# ---------- 特性资产预读（缓存，万级命令复用） ----------
_FEATURE_CACHE: dict[tuple[str, str, str], list[dict]] = {}


def load_feature_docs(storage: str, nf: str, ver: str) -> list[dict]:
    """特性层资产预读缓存。返回 [{path, feature_code, text}, ...]。

    扫 Feature/{nf}/{ver}/{nf}@Feature@{code}/*.md 全部子文档。
    """
    key = (storage, nf, ver)
    if key in _FEATURE_CACHE:
        return _FEATURE_CACHE[key]
    base = feature_dir(storage, nf, ver)
    docs: list[dict] = []
    if base.exists():
        for md in base.rglob("*.md"):
            code = _feature_code_of(md)
            if not code:
                continue
            try:
                text = md.read_text(encoding="utf-8")
            except Exception:
                continue
            docs.append({"path": md, "feature_code": code, "text": text})
    _FEATURE_CACHE[key] = docs
    return docs


def _feature_code_of(path: Path) -> str | None:
    """从路径段 {nf}@Feature@{code} 提 feature_code。"""
    for part in path.parts:
        m = _FEATURE_DIR_RE.match(part)
        if m:
            return m.group("code")
    return None


# ---------- 命中判定 + 提取（复用 assets/scripts/aggregate_command_summary.py 逻辑） ----------
def detect_signals(text: str, cmd: str) -> dict[str, bool]:
    """4 类信号检测（严格：表行首 / 任务脚本行首 / 段落弱信号）。"""
    re_cmd = re.escape(cmd)
    data_plan = re.search(r"^\|\s*\*\*\s*" + re_cmd + r"\s*\*\*\s*\|", text, re.M)
    task_example = re.search(r"^\s*`?\s*" + re_cmd + r"\s*[:\s][^`\n;]+;`?", text, re.M)
    prose = re.search(r"(?:通过|使用)\s*\*\*\s*" + re_cmd + r"\s*\*\*(?:命令|配置)?", text)
    return {"data_plan": bool(data_plan), "task_example": bool(task_example), "prose": bool(prose)}


def extract_data_plan_rows(text: str, cmd: str) -> list[str]:
    re_cmd = re.escape(cmd)
    rows = re.findall(r"^\|\s*\*\*\s*" + re_cmd + r"\s*\*\*\s*\|.*$", text, re.M)
    return list(dict.fromkeys(rows))  # 去重保序


def extract_task_examples(text: str, cmd: str) -> list[str]:
    re_cmd = re.escape(cmd)
    examples = re.findall(r"^\s*`?\s*" + re_cmd + r"\s*[:\s][^`\n;]+;`?", text, re.M)
    seen, unique = set(), []
    for e in examples:
        norm = e.strip("`").strip()
        if norm and norm not in seen:
            seen.add(norm)
            unique.append(norm)
    return unique


def extract_step_contexts(text: str, cmd: str, window: int = 2, src_path: str = "") -> list[dict]:
    """操作步骤上下文：行首 `| **CMD** |` 或 `CMD:...;` 命中，合并相邻段。"""
    re_cmd = re.escape(cmd)
    bold_pat = re.compile(r"^\s*\|\s*\*\*\s*" + re_cmd + r"\s*\*\*\s*\|")
    cmd_inline_pat = re.compile(r"^\s*`?\s*" + re_cmd + r"\s*[:\s][^`\n;]+;`?")
    lines = text.split("\n")
    hit_idx = [i for i, ln in enumerate(lines) if bold_pat.search(ln) or cmd_inline_pat.match(ln)]
    if not hit_idx:
        return []
    # 合并为段（间距 ≤ 2*window）
    segments: list[tuple[int, int]] = []
    seg_start, prev = hit_idx[0], hit_idx[0]
    for idx in hit_idx[1:]:
        if idx - prev <= 2 * window:
            prev = idx
            continue
        segments.append((max(0, seg_start - window) + 1, min(len(lines), prev + window)))
        seg_start, prev = idx, idx
    segments.append((max(0, seg_start - window) + 1, min(len(lines), prev + window)))
    contexts = []
    for start, end in segments:
        kept = [(n, lines[n - 1]) for n in range(start, end + 1)
                if bold_pat.search(lines[n - 1]) or cmd_inline_pat.match(lines[n - 1])]
        if not kept:
            continue
        contexts.append({
            "src_path": src_path,
            "start_line": kept[0][0],
            "end_line": kept[-1][0],
            "context": "\n".join(f"{n:>4d}: {t}" for n, t in kept),
        })
    return contexts


# ---------- 命令真相（从命令层资产 md 提取） ----------
def _section(md: str, name: str) -> str:
    """取 `#### {name}` 到下一个 `####`/`## ` 之间的正文。"""
    lines = md.splitlines()
    start = None
    for i, ln in enumerate(lines):
        if ln.startswith("####") and name in ln:
            start = i + 1
            break
    if start is None:
        return ""
    body = []
    for ln in lines[start:]:
        if ln.startswith("#"):
            break
        body.append(ln)
    return "\n".join(body).strip()


def extract_command_truth(cmd_md: Path, repo: Path) -> dict:
    """从命令层资产 md 抽命令真相（适用NF/功能/notes/参数真相表）。"""
    text = cmd_md.read_text(encoding="utf-8")
    out: dict = {"path": str(cmd_md.relative_to(repo)), "applicable_nf": "", "function": "",
                 "notes": [], "param_table": []}

    func_text = _section(text, "命令功能") or _section(text, "功能")
    if func_text:
        out["function"] = func_text
        m = re.search(r"\*\*适用NF[：:]\s*([^*\n]+)\*\*", func_text)
        if m:
            out["applicable_nf"] = m.group(1).strip()

    notes_text = _section(text, "注意事项") or _section(text, "说明")
    if notes_text:
        out["notes"] = [b.strip() for b in re.findall(r"^[-*]\s+(.+)$", notes_text, re.M)]

    param_text = _section(text, "参数说明") or _section(text, "参数")
    if param_text:
        rows = re.findall(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$", param_text, re.M)
        out["param_table"] = [
            {"param": c[0].strip(), "name": c[1].strip(), "desc": c[2].strip()}
            for c in rows if c[0].strip() and "参数标识" not in c[0] and not set(c[0].strip()) <= set("- :")
        ]
    return out


# ---------- 单命令汇总 ----------
def aggregate_for_command(storage: str, nf: str, ver: str, cmd: str, repo: Path) -> tuple[str, int]:
    """生成单命令汇总 md，返回 (md 文本, 命中特性数)。"""
    # ① 命令真相（命令层资产）
    cmd_md = command_md_path(storage, nf, ver, cmd)
    truth = extract_command_truth(cmd_md, repo) if cmd_md.exists() else {
        "path": f"(未找到命令层资产: {cmd_md.name})", "applicable_nf": "", "function": "",
        "notes": [], "param_table": []}

    # ② 扫特性层资产，命中判定（按 feature_code 聚合）
    hits_by_code: dict[str, dict] = {}
    for doc in load_feature_docs(storage, nf, ver):
        text = doc["text"]
        if cmd not in text:  # 廉价预过滤
            continue
        signals = detect_signals(text, cmd)
        if not (signals["data_plan"] or signals["task_example"]):
            continue  # 强证据：数据规划行或任务脚本（粗体/段落太弱，参考信息页会污染）
        code = doc["feature_code"]
        rel = str(doc["path"].relative_to(repo))
        hit = {
            "feature_code": code,
            "path": rel,
            "data_plan_rows": extract_data_plan_rows(text, cmd),
            "task_examples": extract_task_examples(text, cmd),
            "step_contexts": extract_step_contexts(text, cmd, src_path=rel),
        }
        if code not in hits_by_code:
            hits_by_code[code] = hit
        else:  # 同特性多子文档合并，保留证据更丰的作 primary
            cur = hits_by_code[code]
            cur_score = len(cur["data_plan_rows"]) + len(cur["task_examples"])
            new_score = len(hit["data_plan_rows"]) + len(hit["task_examples"])
            primary, secondary = (cur, hit) if cur_score >= new_score else (hit, cur)
            primary["data_plan_rows"] = list(dict.fromkeys(primary["data_plan_rows"] + secondary["data_plan_rows"]))
            primary["task_examples"] = list(dict.fromkeys(primary["task_examples"] + secondary["task_examples"]))
            seen = {(c["src_path"], c["start_line"], c["end_line"]) for c in primary["step_contexts"]}
            for c in secondary["step_contexts"]:
                k = (c["src_path"], c["start_line"], c["end_line"])
                if k not in seen:
                    seen.add(k)
                    primary["step_contexts"].append(c)
            hits_by_code[code] = primary
    hits = [hits_by_code[k] for k in sorted(hits_by_code.keys())]

    # 模板复用折叠（同指纹特性折叠，避免 activation 模板复用重复）
    def fingerprint(r: str) -> str:
        return re.sub(r"\s+", "", re.sub(r"\d+", "N", r))

    def fp_set(h: dict) -> frozenset:
        return frozenset([fingerprint(r) for r in h["data_plan_rows"]]
                         + [("EX:" + e) for e in h["task_examples"]])

    groups: dict[frozenset, list[dict]] = {}
    for h in hits:
        groups.setdefault(fp_set(h), []).append(h)
    for fs, group in groups.items():
        if len(group) <= 1 or len(fs) < 3:
            continue
        primary = group[0]
        for dup in group[1:]:
            dup["data_plan_rows"] = []
            dup["task_examples"] = []
            dup["template_of"] = primary["feature_code"]

    # ③ 配置方法差异汇总（数据规划行参数列取值分布）
    param_counter: dict[str, Counter] = defaultdict(Counter)
    for h in hits:
        for row in h["data_plan_rows"]:
            cells = [c.strip() for c in row.split("|")]
            if len(cells) >= 5:
                param = cells[2].replace("（", "(").replace("）", ")").strip()
                value = cells[3].strip()
                if param and value:
                    param_counter[param][value] += 1

    # 拼装
    L: list[str] = []
    L.append(f"# atom 构建输入：{cmd} ({nf} {ver})")
    L.append(f"> 命令名: {cmd} | 引用该命令的特性数: {len(hits)} | 命令层资产: {truth['path']}")
    L.append(f"> 工具: 三层图谱构建规范/task/scripts/collect_command_examples.py")
    L.append(f"> 生成时间: {datetime.now().isoformat(timespec='seconds')}")
    L.append("")
    L.append("> ⚠ 本文件是 atom 构建的**工作底稿**（非资产、不进 atom md、git ignore）。")
    L.append("> agent 读它归纳 atom 的 配置方法字典 / DP / 约束（见 task/SKILL.md A.5 第二步）。")
    L.append("")

    L.append("## ① 命令真相（来自命令层资产）")
    if "(未找到" in truth["path"]:
        L.append(f"- **⚠ {truth['path']}**")
    else:
        if truth["applicable_nf"]:
            L.append(f"- 适用NF: {truth['applicable_nf']}")
        if truth["function"]:
            L.append(f"- 功能:\n\n{truth['function']}\n")
        if truth["notes"]:
            L.append("- notes（**应投影为 atom 约束**）:")
            for n in truth["notes"]:
                L.append(f"  - {n}")
            L.append("")
        if truth["param_table"]:
            L.append("- 参数真相表:")
            L.append("")
            L.append("  | 参数 | 名称 | 说明（节选）|")
            L.append("  |---|---|---|")
            for p in truth["param_table"]:
                short = p["desc"][:80].replace("|", "/").replace("\n", " ")
                L.append(f"  | {p['param']} | {p['name']} | {short}… |")
            L.append("")

    L.append("## ② 各特性的配置范式（来自特性层资产）")
    if not hits:
        L.append("- (无命中——该命令未被任何特性文档实际使用；atom 走 SKILL A.2 第二类，直接读命令层 md 梳理)")
    else:
        for i, h in enumerate(hits, 1):
            L.append(f"### 特性 {i}: {h['feature_code']}")
            L.append(f"**md: {h['path']}**")
            if h.get("template_of"):
                L.append(f"- ⚠ 数据规划模板复用：与 {h['template_of']} 同指纹，此处省略，详见该特性段")
            elif h["data_plan_rows"]:
                L.append("- 数据规划表行:")
                L.append("")
                for row in h["data_plan_rows"]:
                    L.append(f"  {row}")
                L.append("")
            if h["task_examples"]:
                L.append("- 任务示例脚本:")
                L.append("")
                for ex in h["task_examples"]:
                    L.append(f"  `{ex}`")
                L.append("")
            if h["step_contexts"]:
                L.append("- 操作步骤上下文（±2 行）:")
                for ctx in h["step_contexts"]:
                    L.append(f"  L{ctx['start_line']}-{ctx['end_line']}:")
                    for ln in ctx["context"].split("\n"):
                        L.append(f"    > {ln}")
                    L.append("")
            L.append("")

    L.append("## ③ 配置方法差异汇总（自动派生 → DP 线索）")
    if param_counter:
        L.append("| 维度（参数） | 取值分布 |")
        L.append("|---|---|")
        for param, c in sorted(param_counter.items()):
            dist = ", ".join(f"{v} ×{n}" for v, n in c.most_common())
            L.append(f"| {param} | {dist} |")
    else:
        L.append("- (无数据规划行可汇总)")
    L.append("")

    L.append("## ④ 数据源")
    L.append(f"- 命令真相: {truth['path']}")
    L.append(f"- 配置范式: Feature/{nf}/{ver}/ 全树（{len(load_feature_docs(storage, nf, ver))} 个特性子文档）")
    L.append(f"- 工具: collect_command_examples.py --nf {nf} --version {ver} --cmd \"{cmd}\"")
    L.append("")

    return "\n".join(L), len(hits)


# ---------- CLI ----------
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--nf", required=True)
    ap.add_argument("--version", required=True)
    ap.add_argument("--storage", default=DEFAULT_STORAGE, help=f"资产根（默认 {DEFAULT_STORAGE}）")
    ap.add_argument("--cmd", help="单条命令全名（如 'ADD URR'）")
    ap.add_argument("--all", action="store_true", help="全量：扫命令层资产发现所有命令")
    ap.add_argument("--limit", type=int, help="限制命令数（测试用）")
    ap.add_argument("--dry-run", action="store_true", help="干跑（只统计命中，不写）")
    ap.add_argument("--skip-existing", action="store_true", default=True, help="跳过已存在汇总（增量，默认开）")
    ap.add_argument("--no-skip-existing", dest="skip_existing", action="store_false")
    args = ap.parse_args()

    if not args.cmd and not args.all:
        ap.error("需指定 --cmd 或 --all")

    if args.cmd:
        md, hits = aggregate_for_command(args.storage, args.nf, args.version, args.cmd, REPO)
        out = output_path(args.storage, args.nf, args.version, args.cmd)
        if args.dry_run:
            print(f"[DRY-RUN] {args.cmd:25s} | 命中 {hits:3d} 特性 | {out.relative_to(REPO)}")
            print("--- 前 40 行预览 ---")
            print("\n".join(md.split("\n")[:40]))
        else:
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(md, encoding="utf-8")
            print(f"[WRITE] {out.relative_to(REPO)} | 命中 {hits} 特性")
        return 0

    # 全量
    cmds = discover_commands(args.storage, args.nf, args.version)
    if not cmds:
        sys.exit(f"未发现命令层资产: {command_dir(args.storage, args.nf, args.version)}")
    print(f"[INFO] 命令层资产: {len(cmds)} 条命令")
    feature_docs = load_feature_docs(args.storage, args.nf, args.version)
    print(f"[INFO] 特性层资产预读: {len(feature_docs)} 个子文档已缓存")

    keys = sorted(cmds.keys())
    if args.limit:
        keys = keys[: args.limit]
        print(f"[INFO] --limit {args.limit}，仅处理前 {len(keys)} 条")

    written = skipped = nohit = failed = 0
    nohit_list: list[str] = []
    for i, cmd in enumerate(keys, 1):
        out = output_path(args.storage, args.nf, args.version, cmd)
        if args.skip_existing and not args.dry_run and out.exists():
            skipped += 1
            continue
        try:
            _, hits = aggregate_for_command(args.storage, args.nf, args.version, cmd, REPO)
        except Exception as e:  # noqa: BLE001
            failed += 1
            if i <= 20 or i % 200 == 0:
                print(f"  [FAIL] {cmd:30s} | {e}")
            continue
        if hits == 0:
            nohit += 1
            nohit_list.append(cmd)
            if i <= 20 or i % 500 == 0:
                print(f"  {i:5d}/{len(keys)} {cmd:30s} | 命中   0 (no-hit)")
            continue
        if args.dry_run:
            if i <= 20 or i % 200 == 0:
                print(f"  {i:5d}/{len(keys)} {cmd:30s} | 命中 {hits:3d}")
        else:
            md, _ = aggregate_for_command(args.storage, args.nf, args.version, cmd, REPO)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(md, encoding="utf-8")
            written += 1
            if i <= 20 or i % 200 == 0:
                print(f"  {i:5d}/{len(keys)} {cmd:30s} | 命中 {hits:3d} | WRITE")

    if nohit_list and not args.dry_run:
        nh = REPO / NOHIT_TPL.format(storage=args.storage, nf=args.nf, ver=args.version)
        nh.parent.mkdir(parents=True, exist_ok=True)
        nh.write_text(
            f"# {args.nf} {args.version} 无特性命中命令（{len(nohit_list)} 条，扫描于 "
            f"{datetime.now().isoformat(timespec='seconds')}）→ atom 走 SKILL A.2 第二类\n"
            + "\n".join(nohit_list) + "\n",
            encoding="utf-8",
        )
    print(f"\n[DONE] 写入 {written} | 跳过 {skipped} | 无命中 {nohit} | 失败 {failed} | 总 {len(keys)}")
    if nohit_list:
        print(f"[NO-HIT] {len(nohit_list)} 条命令无特性配置示例 → atom 直接读命令层 md 梳理")
    return 0


if __name__ == "__main__":
    sys.exit(main())
