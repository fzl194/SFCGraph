#!/usr/bin/env python3
"""
命令配置方法汇总：扫原始产品文档 (output/) 找命令在多特性下的真实用法，输出汇总 md。
按 assets/task/命令级atom构建SOP.md §3 算法实现。

输入（两棵独立子树，**不**依赖 ConfigTask/assert/command-evidence/）：
  - B 命令原始 md: output/{nf}_Product_Documentation_CH_{ver}/OM参考/命令/...
  - C' 特性激活 md: output/{nf}_Product_Documentation_CH_{ver}/特性部署/特性指南/{nf}特性指南/...

输出（中间态数据，非资产，git 已 ignore）：
  ConfigTask/assert/{nf}/{ver}/_intermediates/command-summary/{CMD}.md

用法:
  # 单命令
  python assets/scripts/aggregate_command_summary.py --nf UDG --version 20.15.2 --cmd "ADD URR"

  # 批量（从 _numbering.json 读所有 atom 对应命令）
  python assets/scripts/aggregate_command_summary.py --nf UDG --version 20.15.2 --all

  # 干跑（只统计，不写）
  python assets/scripts/aggregate_command_summary.py --nf UDG --version 20.15.2 --all --dry-run
"""
import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
# 网元 → 产品文档根目录名（UDG/UNC 命名规则不同）
DOC_ROOT_NAMES = {
    "UDG": "UDG_Product_Documentation_CH_{ver}",
    "UNC": "UNC {ver} 产品文档(裸机容器) 05",
}
INTERMEDIATE_TPL = "assets/_intermediates/command-summary/{nf}/{ver}/{cmd_sanitized}.md"

# 特征 ID 正则（GWFD-/WSFD-/IPFD-）
FEATURE_ID_RE = re.compile(r"(GWFD|WSFD|IPFD)-\d+")
# 命令引用检测（4 类信号，见 SOP §3.2 step 3）
# (a) "**CMD**" 粗体
CMD_BOLD_RE = re.compile(r"\*\*\s*{re_cmd}\s*\*\*")
# (b) 数据规划表行: | **CMD** | 参数 | 取值 | 说明 |
DATA_PLAN_ROW_RE = re.compile(r"^\|\s*\*\*\s*{re_cmd}\s*\*\*\s*\|(.*)$", re.M)
# (c) 任务示例脚本: `CMD:...;` 或 `CMD ...;`
TASK_EXAMPLE_RE = re.compile(r"^\s*`?\s*{re_cmd}\s*[:\s][^`\n;]+;`?", re.M)
# (d) 段落中"通过**CMD**命令"/"使用**CMD**"——弱信号
CMD_PROSE_RE = re.compile(r"(?:通过|使用)\s*\*\*\s*{re_cmd}\s*\*\*(?:命令|配置)?")


def doc_root(nf: str, ver: str) -> Path:
    return REPO / "output" / DOC_ROOT_NAMES[nf].format(ver=ver)


# 文件名命令名提取：中文（CMD）_id.md → CMD（全角括号）
CMD_NAME_RE = re.compile(r"（([A-Z][A-Z0-9]*(?:\s+[A-Z0-9]+)*)）")


def mml_cmd_root(nf: str, ver: str) -> Path:
    """OM参考/命令/{nf} MML命令/ 根（全量 MML 命令源）。"""
    return doc_root(nf, ver) / "OM参考" / "命令" / f"{nf} MML命令"


def discover_all_commands(nf: str, ver: str) -> dict[str, Path]:
    """全量发现 MML 命令（不基于 _numbering.json）。
    扫 OM参考/命令/{nf} MML命令/ 全树，从文件名 中文（CMD）_id.md 提取命令全名，去重。
    返回 {命令全名 → 命令原始 md 路径}。
    """
    base = mml_cmd_root(nf, ver)
    if not base.exists():
        return {}
    cmds: dict[str, Path] = {}
    for md in base.rglob("*.md"):
        m = CMD_NAME_RE.search(md.name)
        if m:
            cmds.setdefault(m.group(1), md)
    return cmds


def cmd_doc_path(nf: str, ver: str, cmd: str) -> Path | None:
    """定位 B：OM参考 命令原始 md（优先文件名精确匹配命令名括号）。"""
    base = mml_cmd_root(nf, ver)
    if not base.exists():
        return None
    # 精确：文件名含 （CMD）
    target = f"（{cmd}）"
    for p in base.rglob("*.md"):
        if target in p.name:
            return p
    # 退而求其次：命令名出现在文件名
    for p in base.rglob("*.md"):
        if cmd in p.name:
            return p
    return None


# ★ 特性树预读缓存（万级命令复用，避免每命令重扫特性树）
_FEATURE_CACHE: dict[tuple[str, str], list[dict]] = {}


def load_feature_docs(nf: str, ver: str) -> list[dict]:
    """C' 特性激活 md 树预读缓存。返回 [{path, feature_id, feature_name, text}, ...]。"""
    cache_key = (nf, ver)
    if cache_key in _FEATURE_CACHE:
        return _FEATURE_CACHE[cache_key]
    # UDG: 特性部署/特性指南/UDG特性指南/
    # UNC: 网络部署/特性部署/UNC特性指南/（多一层 网络部署/，无中间 特性指南）
    candidates = [
        doc_root(nf, ver) / "特性部署" / "特性指南" / f"{nf}特性指南",
        doc_root(nf, ver) / "网络部署" / "特性部署" / f"{nf}特性指南",
        doc_root(nf, ver) / "网络部署" / "特性部署" / "特性指南" / f"{nf}特性指南",
    ]
    base = next((c for c in candidates if c.exists()), None)
    docs: list[dict] = []
    if base.exists():
        for md in base.rglob("*.md"):
            fid = extract_feature_id(md)
            if not fid:
                continue
            try:
                text = md.read_text(encoding="utf-8")
            except Exception:
                continue
            docs.append({
                "path": md,
                "feature_id": fid,
                "feature_name": extract_feature_name_from_path(md),
                "text": text,
            })
    _FEATURE_CACHE[cache_key] = docs
    return docs


def extract_feature_id(path: Path) -> str | None:
    """路径中匹配 (GWFD|WSFD|IPFD)-\\d+ 的段。"""
    for p in path.parts:
        m = FEATURE_ID_RE.match(p)
        if m:
            return m.group(0)
    return None


def extract_feature_name_from_path(path: Path) -> str:
    """从路径提取特性名（feature_id 后段）。"""
    for p in path.parts:
        m = re.match(r"(GWFD|WSFD|IPFD)-\d+\s+(.+)", p)
        if m:
            return m.group(2).strip()
    return ""


def detect_signals(text: str, cmd: str) -> dict:
    """SOP §3.2 step 3：4 类信号检测。
    严格模式：表行首 `| **CMD** |`、行首 `CMD:...;`、`通过**CMD**命令`。
    行中/行末的 `[**CMD**]` 不算（如说明列里的"已通过命令[**ADD URR**]配置"）。
    """
    re_cmd = re.escape(cmd)
    data_plan = re.search(r"^\|\s*\*\*\s*" + re_cmd + r"\s*\*\*\s*\|", text, re.M)
    task_example = re.search(r"^\s*`?\s*" + re_cmd + r"\s*[:\s][^`\n;]+;`?", text, re.M)
    prose = re.search(r"(?:通过|使用)\s*\*\*\s*" + re_cmd + r"\s*\*\*(?:命令|配置)?", text)
    return {
        "data_plan": bool(data_plan),
        "task_example": bool(task_example),
        "prose": bool(prose),
    }


def extract_step_contexts(text: str, cmd: str, window: int = 2, src_path: str = "") -> list[dict]:
    """SOP §3.2 step 4：操作步骤上下文（±2 行原文 + 行号）。
    命中条件（行级）：
      A) 表行首命令: | **CMD** |  → 视为"该命令是本行主语"
      B) 任务示例: `CMD:...;` 或 `CMD ...;` 行首
    排除：行中/行末 `[**CMD**]`（如说明列里的"已通过命令[**ADD URR**]配置"不算）。
    src_path 由调用方注入。
    """
    re_cmd = re.escape(cmd)
    # A) 表行首: 行首 `|` + 可选空格 + `**CMD**` + `|`
    bold_pat = re.compile(r"^\s*\|\s*\*\*\s*" + re_cmd + r"\s*\*\*\s*\|")
    # B) 任务示例: 行首 `CMD:...;` 或 `CMD ...;`
    cmd_inline_pat = re.compile(r"^\s*`?\s*" + re_cmd + r"\s*[:\s][^`\n;]+;`?")
    lines = text.split("\n")
    # 找所有命中行
    hit_indices = [
        i for i, line in enumerate(lines)
        if bold_pat.search(line) or cmd_inline_pat.match(line)
    ]
    if not hit_indices:
        return []
    # 合并为段（相距 ≤ 2*window）
    segments: list[tuple[int, int]] = []
    seg_start_idx = hit_indices[0]
    prev_idx = hit_indices[0]
    for idx in hit_indices[1:]:
        if idx - prev_idx <= 2 * window:
            prev_idx = idx
            continue
        seg_end_idx = prev_idx
        kept_start = max(0, seg_start_idx - window) + 1
        kept_end = min(len(lines), seg_end_idx + window)
        segments.append((kept_start, kept_end))
        seg_start_idx = idx
        prev_idx = idx
    seg_end_idx = prev_idx
    kept_start = max(0, seg_start_idx - window) + 1
    kept_end = min(len(lines), seg_end_idx + window)
    segments.append((kept_start, kept_end))
    # 段内过滤噪音行（仍用严格匹配，只保留本命令真正主语的行）
    contexts = []
    for start, end in segments:
        kept_lines = []
        for ln_no in range(start, end + 1):
            line_text = lines[ln_no - 1]
            if bold_pat.search(line_text) or cmd_inline_pat.match(line_text):
                kept_lines.append((ln_no, line_text))
        if not kept_lines:
            continue
        ctx_text = "\n".join(f"{ln_no:>4d}: {ln_text}" for ln_no, ln_text in kept_lines)
        contexts.append({
            "src_path": src_path,
            "start_line": kept_lines[0][0],
            "end_line": kept_lines[-1][0],
            "context": ctx_text,
        })
    return contexts


def extract_data_plan_rows(text: str, cmd: str) -> list[str]:
    """SOP §3.2 step 4：数据规划表行（去重）。"""
    re_cmd = re.escape(cmd)
    pat = re.compile(r"^\|\s*\*\*\s*" + re_cmd + r"\s*\*\*\s*\|.*$", re.M)
    rows = pat.findall(text)
    # 去重：保留唯一行
    return list(dict.fromkeys(rows))


def extract_task_examples(text: str, cmd: str) -> list[str]:
    """SOP §3.2 step 4：任务示例脚本行（去重 + 标准化）。"""
    re_cmd = re.escape(cmd)
    pat = re.compile(r"^\s*`?\s*" + re_cmd + r"\s*[:\s][^`\n;]+;`?", re.M)
    examples = pat.findall(text)
    # 去重 + 标准化（去反引号、首尾空白）
    seen = set()
    unique = []
    for e in examples:
        norm = e.strip("`").strip()
        if norm and norm not in seen:
            seen.add(norm)
            unique.append(norm)
    return unique


def extract_command_truth(cmd_path: Path) -> dict:
    """SOP §3.2 step 1：抽命令真相。"""
    text = cmd_path.read_text(encoding="utf-8")
    out = {
        "path": str(cmd_path.relative_to(REPO)),
        "适用NF": "",
        "功能": "",
        "notes": [],
        "参数真相表": [],
    }
    # 适用NF
    m = re.search(r"\*\*适用NF[：:]\s*([^*]+)\*\*", text)
    if m:
        out["适用NF"] = m.group(1).strip()
    # 命令功能
    m = re.search(r"####?\s*\[?命令功能\]?[^\n]*\n+(.*?)(?=####|\Z)", text, re.S)
    if m:
        body = m.group(1).strip()
        # 去掉首行锚点标题
        body = re.sub(r"^#+.*\n", "", body, count=1)
        out["功能"] = body
    # notes（注意事项/说明）
    m = re.search(r"####?\s*\[?(注意事项|说明)\]?[^\n]*\n+(.*?)(?=####|\Z)", text, re.S)
    if m:
        body = m.group(1)
        bullets = re.findall(r"^[-*]\s+(.+)$", body, re.M)
        out["notes"] = [b.strip() for b in bullets]
    # 参数真相表（参数说明）
    m = re.search(r"####?\s*\[?参数说明\]?[^\n]*\n+(.*?)(?=####|\Z)", text, re.S)
    if m:
        body = m.group(1)
        rows = re.findall(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$", body, re.M)
        out["参数真相表"] = [
            {"参数": c[0].strip(), "名称": c[1].strip(), "说明": c[2].strip()}
            for c in rows if c[0].strip() and "参数标识" not in c[0]
        ]
    return out


def aggregate_for_command(nf: str, ver: str, cmd: str) -> str:
    """对单条命令生成汇总 md。"""
    base = doc_root(nf, ver)
    if not base.exists():
        sys.exit(f"ERROR: 原始产品文档不存在: {base}")

    # 1. 定位 B 命令原始 md
    cmd_path = cmd_doc_path(nf, ver, cmd)
    truth = extract_command_truth(cmd_path) if cmd_path else {
        "path": "(未找到)", "适用NF": "", "功能": "", "notes": [], "参数真相表": []
    }

    # 2-4. 扫 C' 特性激活 md 树（预读缓存，按 feature_id 聚合）
    feature_hits_by_id: dict[str, dict] = {}
    for doc in load_feature_docs(nf, ver):
        text = doc["text"]
        # ★ 廉价预过滤：命令名字符串不在文本中 → 直接跳过（跳过 95%+ 无关 md）
        if cmd not in text:
            continue
        fid = doc["feature_id"]
        md = doc["path"]
        signals = detect_signals(text, cmd)
        if not any(signals.values()):
            continue
        # 强证据：数据规划表行 或 任务示例脚本（粗体引用太弱，参考信息目录页会污染）
        if not (signals["data_plan"] or signals["task_example"]):
            continue
        hit = {
            "feature_id": fid,
            "feature_name": doc["feature_name"],
            "path": str(md.relative_to(REPO)),
            "data_plan_rows": extract_data_plan_rows(text, cmd),
            "task_examples": extract_task_examples(text, cmd),
            "step_contexts": extract_step_contexts(text, cmd, window=2, src_path=str(md.relative_to(REPO))),
        }
        # 合并到同 feature_id：保留路径最详的 md（通常是 激活/配置md），其余合并证据
        if fid not in feature_hits_by_id:
            feature_hits_by_id[fid] = hit
        else:
            cur = feature_hits_by_id[fid]
            cur_score = len(cur["data_plan_rows"]) + len(cur["task_examples"])
            new_score = len(hit["data_plan_rows"]) + len(hit["task_examples"])
            # 保留证据更丰的 md 作 primary path
            if new_score > cur_score:
                primary, secondary = cur, hit
            else:
                primary, secondary = hit, cur
            # 数据规划行/任务示例合并去重（dict.fromkeys 保序）
            primary["data_plan_rows"] = list(dict.fromkeys(primary["data_plan_rows"] + secondary["data_plan_rows"]))
            primary["task_examples"] = list(dict.fromkeys(primary["task_examples"] + secondary["task_examples"]))
            # 操作步骤上下文合并去重：(src_path, start_line, end_line) 唯一
            seen_ctx = {(c.get("src_path", c.get("path", "")), c["start_line"], c["end_line"]) for c in primary["step_contexts"]}
            for c in secondary["step_contexts"]:
                key = (c.get("src_path", c.get("path", "")), c["start_line"], c["end_line"])
                if key not in seen_ctx:
                    seen_ctx.add(key)
                    primary["step_contexts"].append(c)
            feature_hits_by_id[fid] = primary
    # 按 feature_id 排序输出
    feature_hits = [feature_hits_by_id[k] for k in sorted(feature_hits_by_id.keys())]

    # ★ 跨特性模板复用折叠：activation 模板复用识别（产品文档常对相似特性复用同一份激活 md）
    # 指纹 = (data_plan 行集 + 任务示例集) 同时相同 → 视为同模板，折叠
    def row_fingerprint(r: str) -> str:
        return re.sub(r'\s+', '', re.sub(r'\d+', 'N', r))

    def fp_set(hit: dict) -> frozenset:
        return frozenset(
            [row_fingerprint(r) for r in hit["data_plan_rows"]]
            + [("EX:" + ex) for ex in hit["task_examples"]]
        )

    fp_groups: dict[frozenset, list[dict]] = {}
    for h in feature_hits:
        fs = fp_set(h)
        fp_groups.setdefault(fs, []).append(h)
    for fs, group in fp_groups.items():
        # 仅当指纹集足够大（≥3 条 = 至少 3 个数据规划行或任务示例）才折叠；
        # 避免单行任务示例被误判为模板复用
        if len(group) <= 1 or len(fs) < 3:
            continue
        primary = group[0]
        for dup in group[1:]:
            dup["data_plan_rows"] = []
            dup["task_examples"] = []
            dup["template_of"] = primary["feature_id"]
            dup["template_match_lines"] = len(fs)

    # 5. 派生 ③ 配置方法差异汇总（数据规划行参数列）
    param_value_counter = defaultdict(Counter)
    for h in feature_hits:
        for row in h["data_plan_rows"]:
            cells = [c.strip() for c in row.split("|")]
            # cells: ['', '**CMD**', param, value, note, '']
            if len(cells) >= 5:
                param = cells[2].replace("（", "(").replace("）", ")").strip()
                value = cells[3].strip()
                if param and value:
                    param_value_counter[param][value] += 1

    # 6. 拼装汇总 md（4 段）
    lines = []
    lines.append(f"# 命令配置方法汇总：{cmd} ({nf} {ver})")
    lines.append(f"> 命令名: {cmd} | 引用该命令的特性数: {len(feature_hits)} | 扫描特性总数: {len(feature_hits)}")
    lines.append(f"> 原始命令 md: {truth['path']}")
    lines.append(f"> 扫描覆盖: 特性部署/特性指南/{nf}特性指南/ 全树")
    lines.append(f"> 工具: assets/scripts/aggregate_command_summary.py")
    lines.append(f"> 生成时间: {datetime.now().isoformat(timespec='seconds')}")
    lines.append("")

    # ① 命令真相
    lines.append("## ① 命令真相（来自 OM参考）")
    if truth["path"] == "(未找到)":
        lines.append("- **⚠ 未找到原始命令 md**——请检查命令名或 OM参考 路径")
    else:
        if truth["适用NF"]:
            lines.append(f"- 适用NF: {truth['适用NF']}")
        if truth["功能"]:
            lines.append(f"- 功能描述:\n\n{truth['功能']}\n")
        if truth["notes"]:
            lines.append("- notes（**应投影为 atom rule**）:")
            for n in truth["notes"]:
                lines.append(f"  - {n}")
            lines.append("")
        if truth["参数真相表"]:
            lines.append("- 参数真相表:")
            lines.append("")
            lines.append("  | 参数 | 名称 | 说明（节选）|")
            lines.append("  |---|---|---|")
            for p in truth["参数真相表"]:
                desc_short = p["说明"][:80].replace("|", "/").replace("\n", " ")
                lines.append(f"  | {p['参数']} | {p['名称']} | {desc_short}... |")
            lines.append("")

    # ② 各特性的配置范式
    lines.append("## ② 各特性的配置范式（来自特性部署）")
    if not feature_hits:
        lines.append("- (无命中——该命令在本次扫描的 C' 树中未被任何特性文档实际使用)")
    else:
        for idx, h in enumerate(feature_hits, 1):
            lines.append(f"### 特性 {idx}: {h['feature_id']} {h['feature_name']}")
            lines.append(f"**md: {h['path']}**")
            if h.get("template_of"):
                lines.append(f"- ⚠ **数据规划模板复用**：本特性数据规划行与 [{h['template_of']}]({h['feature_id']}.md)（行号）完全相同（{h.get('template_match_lines', 0)} 行），**此处省略**，详见该特性段")
                lines.append("")
            elif h["data_plan_rows"]:
                lines.append("- 数据规划表行（该命令的参数行）:")
                lines.append("")
                for row in h["data_plan_rows"]:
                    lines.append(f"  {row}")
                lines.append("")
            if h["task_examples"]:
                lines.append("- 任务示例脚本（该命令行）:")
                lines.append("")
                for ex in h["task_examples"]:
                    lines.append(f"  `{ex.strip('`').strip()}`")
                lines.append("")
            if h["step_contexts"]:
                lines.append("- 操作步骤上下文（±2 行原文 + 行号，已过滤邻居噪音行）:")
                for ctx in h["step_contexts"]:
                    lines.append(f"  L{ctx['start_line']}-{ctx['end_line']}:")
                    for ln in ctx["context"].split("\n"):
                        lines.append(f"    > {ln}")
                    lines.append("")
            lines.append("")

    # ③ 配置方法差异汇总
    lines.append("## ③ 配置方法差异汇总（自动派生）")
    if param_value_counter:
        lines.append("| 维度（参数列） | 取值分布 |")
        lines.append("|---|---|")
        for param, counter in sorted(param_value_counter.items()):
            dist = ", ".join(f"{v} x {c}" for v, c in counter.most_common())
            lines.append(f"| {param} | {dist} |")
    else:
        lines.append("- (无数据规划表行可汇总)")
    lines.append("")

    # ④ 数据源
    lines.append("## ④ 数据源")
    lines.append(f"- 命令真相源: {truth['path']}")
    lines.append(f"- 特性激活源: 特性部署/特性指南/{nf}特性指南/ 全树（rglob）")
    lines.append(f"- 扫描时间: {datetime.now().isoformat(timespec='seconds')}")
    lines.append(f"- 工具: assets/scripts/aggregate_command_summary.py --nf {nf} --version {ver} --cmd \"{cmd}\"")
    lines.append("")

    return "\n".join(lines)


def cmd_sanitize(cmd: str) -> str:
    """ADD URR → ADD-URR（与 §5.5 文件名规范一致）"""
    return cmd.replace(" ", "-")


def output_path(nf: str, ver: str, cmd: str) -> Path:
    rel = INTERMEDIATE_TPL.format(nf=nf, ver=ver, cmd_sanitized=cmd_sanitize(cmd))
    return REPO / rel


def load_numbering(nf: str, ver: str) -> dict[str, str]:
    """读 _numbering.json：{命令名 → 编号}。"""
    p = REPO / "assets" / "task" / nf / ver / "_numbering.json"
    if not p.exists():
        return {}
    return json.loads(p.read_text(encoding="utf-8"))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--nf", required=True, choices=["UDG", "UNC"])
    ap.add_argument("--version", required=True)
    ap.add_argument("--cmd", help="单条命令全名（如 'ADD URR'）")
    src = ap.add_mutually_exclusive_group()
    src.add_argument("--all", action="store_true",
                     help="全量批量：扫 OM参考/命令/{nf} MML命令/ 发现所有命令（默认行为，面向新建 atom）")
    src.add_argument("--numbering-only", action="store_true",
                     help="仅已建 atom：从 _numbering.json 读命令（用于对账/补建）")
    ap.add_argument("--limit", type=int, help="限制命令数（测试用）")
    ap.add_argument("--dry-run", action="store_true", help="干跑（只统计命中数，不写文件）")
    ap.add_argument("--skip-existing", action="store_true", default=True,
                    help="跳过已存在的汇总 md（增量；默认开，--no-skip-existing 关闭）")
    ap.add_argument("--no-skip-existing", dest="skip_existing", action="store_false")
    args = ap.parse_args()

    if not args.cmd and not args.all and not args.numbering_only:
        ap.error("必须指定 --cmd / --all / --numbering-only 其一")

    if args.cmd:
        # 单命令
        md = aggregate_for_command(args.nf, args.version, args.cmd)
        out = output_path(args.nf, args.version, args.cmd)
        if args.dry_run:
            hits = md.count("### 特性 ")
            print(f"[DRY-RUN] {args.cmd:25s} | 命中 {hits:3d} 个特性 | {out.relative_to(REPO)}")
            print("--- 前 50 行预览 ---")
            print("\n".join(md.split("\n")[:50]))
        else:
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(md, encoding="utf-8")
            print(f"[WRITE] {out.relative_to(REPO)}")
        return

    # 批量
    if args.numbering_only:
        numbering = load_numbering(args.nf, args.version)
        cmds = sorted(numbering.keys())
        print(f"[INFO] numbering-only 模式: {len(cmds)} 条命令（来自 _numbering.json）")
    else:
        all_cmds = discover_all_commands(args.nf, args.version)
        cmds = sorted(all_cmds.keys())
        print(f"[INFO] 全量模式: {len(cmds)} 条命令（来自 OM参考/命令/{args.nf} MML命令/）")

    # 预读特性树缓存（一次性，后续万次复用）
    feature_docs = load_feature_docs(args.nf, args.version)
    print(f"[INFO] 特性树预读: {len(feature_docs)} 个 md 已缓存")

    if args.limit:
        cmds = cmds[:args.limit]
        print(f"[INFO] --limit {args.limit}，仅处理前 {len(cmds)} 条")

    written = 0
    skipped = 0
    nohit = 0
    failed = 0
    nohit_list: list[str] = []
    nohit_path = REPO / "assets" / "_intermediates" / "command-summary" / args.nf / args.version / "_no-hit.txt"
    for i, cmd in enumerate(cmds, 1):
        out = output_path(args.nf, args.version, cmd)
        # 增量跳过
        if args.skip_existing and not args.dry_run and out.exists():
            skipped += 1
            continue
        try:
            md = aggregate_for_command(args.nf, args.version, cmd)
        except Exception as e:
            failed += 1
            if i <= 20 or i % 200 == 0:
                print(f"  [FAIL] {cmd:30s} | {e}")
            continue
        hits = md.count("### 特性 ")
        if hits == 0:
            # 0 命中：不生成空汇总 md，只记入 _no-hit 列表（这些命令无需建 atom 或极简）
            nohit += 1
            nohit_list.append(cmd)
            if i <= 20 or i % 500 == 0:
                print(f"  {i:5d}/{len(cmds)} {cmd:30s} | 命中   0 (no-hit)")
            continue
        if args.dry_run:
            if i <= 20 or i % 200 == 0:
                print(f"  {i:5d}/{len(cmds)} {cmd:30s} | 命中 {hits:3d}")
        else:
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(md, encoding="utf-8")
            written += 1
            if i <= 20 or i % 200 == 0:
                print(f"  {i:5d}/{len(cmds)} {cmd:30s} | 命中 {hits:3d} | WRITE")
    # 写 no-hit 列表
    if nohit_list and not args.dry_run:
        nohit_path.parent.mkdir(parents=True, exist_ok=True)
        nohit_path.write_text(
            f"# {args.nf} {args.version} 无特性命中命令（{len(nohit_list)} 条，扫描于 {datetime.now().isoformat(timespec='seconds')}）\n"
            + "\n".join(nohit_list) + "\n",
            encoding="utf-8",
        )
    print(f"\n[DONE] 写入汇总 {written} | 跳过(已存在) {skipped} | 无命中 {nohit} | 失败 {failed} | 总 {len(cmds)}")
    if nohit_list:
        print(f"[NO-HIT] 列表: {nohit_path.relative_to(REPO)}")


if __name__ == "__main__":
    main()
