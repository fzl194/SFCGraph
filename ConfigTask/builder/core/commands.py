# ConfigTask/builder/core/commands.py
"""从操作步骤段抽 MML 命令序列，构造 command_ref 实例键（纯函数）。"""
import re

from builder.constants import CMD_REF_TMPL

# MML 命令：动词 + 对象关键字（ADD URR / SET REFRESHSRV / ADD FILTERIPV6 ...）
_CMD_RE = re.compile(r'\b(ADD|SET|MOD|DEL|RMV|LST|DSP)\s+(\w+)\b')
# 步骤起始：行首 "数字. "
_STEP_START_RE = re.compile(r'^(\d+)\.\s', re.MULTILINE)


def parse_step_commands(steps_text: str) -> dict:
    """操作步骤段 → {step_num: [命令全名]}（按出现顺序，含子步骤里的命令）。"""
    starts = [(m.start(), int(m.group(1))) for m in _STEP_START_RE.finditer(steps_text)]
    result = {}
    for i, (start, num) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(steps_text)
        block = steps_text[start:end]
        result[num] = [f"{v} {k}" for v, k in _CMD_RE.findall(block)]
    return result


def commands_for_range(steps_text: str, step_range, nf: str, version: str) -> list:
    """step_range (a,b) → 有序 command_ref 列表（构造 @MMLCommand@ 实例键）。"""
    if not step_range:
        return []
    step_cmds = parse_step_commands(steps_text)
    refs = []
    for n in range(step_range[0], step_range[1] + 1):
        for cmd in step_cmds.get(n, []):
            refs.append(CMD_REF_TMPL.format(nf=nf, version=version, name=cmd))
    return refs
