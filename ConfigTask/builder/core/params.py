# ConfigTask/builder/core/params.py
"""从数据规划表（必备事项→数据）抽参数，构造 parameter_ref + reference_hint（纯函数）。

表格式（跨文档一致）：| 类别(命令) | 参数名称(中文(CODE)) | 取值样例 | 获取方法 | 说明 |
reference_hint：获取方法含"已配置数据中获取"→ True。
跨多表（内容计费 表1~4）按命令+参数去重。
"""
import re

# 类别单元格里的命令：**[ADD URR](link)** 或 **ADD URR**
_CMD_IN_CELL_RE = re.compile(r'(ADD|SET|MOD|DEL|RMV|LST|DSP)\s+(\w+)')
# 参数名：中文（CODE）→ 取 CODE（全角括号）
_PARAM_CODE_RE = re.compile(r'（([A-Z][A-Z0-9_]*)）')


def parse_param_table(data_text: str) -> dict:
    """数据规划表段 → {命令全名: [{parameter_name, reference_hint}]}（同命令同参数去重）。"""
    result = {}
    for raw in data_text.splitlines():
        line = raw.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")]
        cells = cells[1:-1] if len(cells) >= 2 else cells  # 去首尾空 cell
        if len(cells) < 4:
            continue
        cat, pname, method = cells[0], cells[1], cells[3]
        if pname in ("参数名称", "参数名"):          # 表头
            continue
        cmd_m = _CMD_IN_CELL_RE.search(cat)
        if not cmd_m:
            continue
        cmd = f"{cmd_m.group(1)} {cmd_m.group(2)}"
        param_m = _PARAM_CODE_RE.search(pname)
        if not param_m:
            continue
        param = param_m.group(1)
        entry = {"parameter_name": param, "reference_hint": "已配置数据中获取" in method}
        lst = result.setdefault(cmd, [])
        if not any(e["parameter_name"] == param for e in lst):   # 去重
            lst.append(entry)
    return result
