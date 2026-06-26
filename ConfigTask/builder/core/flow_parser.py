# ConfigTask/builder/core/flow_parser.py
"""操作流程段 → [{phase_name, step_range}]。

仅处理"有操作流程"的文档（内容计费/IPSec 等）。无操作流程的文档（接入控制/eDRX）
此函数返回空列表，由 cut_boundaries 步标记为"待 Agent 分组"（决策 B）。
"""
import re

# phase 起始：行首 "数字. "
_PHASE_START_RE = re.compile(r'^\s*(\d+)\.\s+', re.MULTILINE)
# "步骤 N" 引用
_STEP_REF_RE = re.compile(r'步骤\s*(\d+)')


def parse_flow(flow_text: str) -> list:
    """解析操作流程段，返回 phase 列表。

    每个 phase: {phase_name: str, step_range: (start, end) | None}
    step_range 取该 phase 内"步骤 X"引用的首末（如 [步骤1]-[步骤2]→(1,2)，[步骤6]→(6,6)）。
    """
    starts = [(m.start(), m.group(1)) for m in _PHASE_START_RE.finditer(flow_text)]
    phases = []
    for i, (start, _num) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(flow_text)
        block = flow_text[start:end]
        # phase 名：行首 "N. " 后到首个 。 或换行
        name_m = re.match(r'\s*\d+\.\s*(.+?)(?:。|\n)', block)
        name = name_m.group(1).strip() if name_m else ""
        # step_range：该 block 内所有"步骤 N"的首末
        step_nums = [int(x) for x in _STEP_REF_RE.findall(block)]
        step_range = (step_nums[0], step_nums[-1]) if step_nums else None
        phases.append({"phase_name": name, "step_range": step_range})
    return phases
