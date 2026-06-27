# ConfigTask/builder/core/enrich.py
"""按命令从原始 md 三段抽证据，供 candidate/cluster 内联携带。

三段来源（md_reader 切分）：
- 操作步骤 → 步骤描述（任务结构）→ extract_step_text（复用 doc_steps）
- 任务示例 → MML 配置命令原文（含参数与实例取值）→ extract_command_examples
- 数据规划表 → 参数级 获取方法/取值样例（binding_type 判定依据）→ extract_param_rows

所有函数纯逻辑、按 candidate 的命令集合过滤，不读文件——I/O 在调用方做。
"""
import re

# MML 动词（与 extract_steps._CMD_RE 对齐）
VERBS = ("ADD", "SET", "MOD", "DEL", "RMV", "LST", "DSP", "LOD", "SWP", "RST", "EXP", "ACT", "DEA")
_VERBS_RE = "|".join(VERBS)

# 行首 MML 命令：VERB OBJECT
_MML_LINE_RE = re.compile(r"^\s*(" + _VERBS_RE + r")\s+([A-Za-z0-9_]+)\b")
# 文本中嵌入的命令（数据规划表类别单元格）
_CMD_IN_TEXT_RE = re.compile(r"(?:" + _VERBS_RE + r")\s+[A-Z0-9_]+")
# 参数英文码：中文括号或英文括号里的大写串
_PARAM_CODE_RE = re.compile(r"[（(]([A-Z0-9_]+)[)）]")


def _strip_md(s: str) -> str:
    """去 markdown 装饰：[text](url)→text，删链接/加粗/斜体。"""
    if not s:
        return ""
    s = re.sub(r"\[([^\]]*)\]", r"\1", s)  # [text](url) → text
    s = re.sub(r"\([^)]*\)", "", s)        # 残余 (url)
    s = re.sub(r"\*+", "", s)              # 加粗/斜体
    s = re.sub(r"`", "", s)
    return s.strip()


def _cells(row: str) -> list[str]:
    """markdown 表格行 → 单元格列表（去首尾 | 后切分）。"""
    return [c.strip() for c in row.strip().strip("|").split("|")]


def extract_command_examples(body: str, commands: list[str], max_per_cmd: int = 6) -> list[str]:
    """从任务示例正文抽 MML 命令行（配置命令原文），只保留 commands 里的命令。

    重复行去重；同一命令最多保留 max_per_cmd 个变体（变体是 decision_driven 的证据）。
    """
    cmd_set = {c.upper() for c in commands}
    seen: set[str] = set()
    per_cmd: dict[str, int] = {}
    out: list[str] = []
    for line in body.splitlines():
        m = _MML_LINE_RE.match(line)
        if not m:
            continue
        key = f"{m.group(1)} {m.group(2)}".upper()
        if key not in cmd_set:
            continue
        clean = line.strip()
        if clean in seen:
            continue
        if per_cmd.get(key, 0) >= max_per_cmd:
            continue
        seen.add(clean)
        per_cmd[key] = per_cmd.get(key, 0) + 1
        out.append(clean)
    return out


def extract_param_rows(body: str, commands: list[str], max_rows: int = 40) -> list[dict]:
    """从数据规划表正文抽表格行，只保留 commands 里的命令。

    返回 [{command, param, param_code, sample, obtain_method, note}]。
    """
    cmd_set = {c.upper() for c in commands}
    rows: list[dict] = []
    for line in body.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = _cells(line)
        if len(cells) < 4:
            continue
        cat = _strip_md(cells[0])
        if set(cat) <= set("-: "):  # 分隔行 |---|---|
            continue
        m = _CMD_IN_TEXT_RE.search(cat.upper())
        if not m:
            continue
        cmd = m.group(0).upper()
        if cmd not in cmd_set:
            continue
        param_name = _strip_md(cells[1]) if len(cells) > 1 else ""
        pcm = _PARAM_CODE_RE.search(param_name)
        param_code = pcm.group(1) if pcm else ""
        rows.append({
            "command": cmd,
            "param": param_name,
            "param_code": param_code,
            "sample": _strip_md(cells[2]) if len(cells) > 2 else "",
            "obtain_method": _strip_md(cells[3]) if len(cells) > 3 else "",
            "note": _strip_md(cells[4]) if len(cells) > 4 else "",
        })
        if len(rows) >= max_rows:
            break
    return rows


def extract_step_text(doc_record: dict, commands: list[str], max_chars: int = 1500) -> str:
    """从 doc_steps 记录抽命中 commands 的步骤描述（raw_text），按命中步骤拼接。

    复用 extract_steps 已解析的 steps[].commands/raw_text，不再回读 操作步骤 段。
    """
    cmd_set = {c.upper() for c in commands}
    out: list[str] = []
    for step in doc_record.get("steps", []):
        sc = {c.upper() for c in step.get("commands", [])}
        if not (sc & cmd_set):
            continue
        t = step.get("raw_text") or step.get("step_desc") or ""
        t = _strip_md(t)
        if t and t not in out:
            out.append(t)
    text = "\n".join(out)
    return text[:max_chars]
