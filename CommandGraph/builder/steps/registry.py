"""步骤注册表 + 数据流依赖校验。

每个 step 是一个【独立的输入→输出单元】：
  - provides: 本 step 产出的数据产品（逻辑名）
  - requires: 需要的【数据产品】——可由列表中更早的 step provides，或磁盘上已有产物
  - 外部输入（source / parameter_csv）由 ctx 提供，不进 requires

依赖由数据流推导（不再硬编码 dep 字典）：
  step B 的 requires 须由它之前的 step provides，或磁盘已有对应文件。
这样反映真实关系：
  - mmlcommand（provides mml_commands）独立可跑
  - enrich（requires mml_commands）须 mmlcommand 在前；若磁盘已有 mml_commands.jsonl
    也可单独重跑（改了 extractor 后快速重 enrich，不必重扫几千个 md）
  - parameter（无 requires，自带 parameter_csv）完全独立可跑

加新 step = 加一个 steps/xxx.py + 在 STEPS/PROVIDES 注册（有依赖再加 REQUIRES）。
"""
from pathlib import Path

from . import enrich, mmlcommand, parameter

STEPS = {
    "mmlcommand": mmlcommand.run,
    "enrich": enrich.run,
    "parameter": parameter.run,
}

# 数据产品 → 产物文件名（相对 out_dir）。用于"磁盘已有也算满足 requires"。
PRODUCT_FILE = {
    "mml_commands": "mml_commands.jsonl",
    "command_parameters": "command_parameters.jsonl",
    "command_has_parameter": "command_has_parameter.jsonl",
    "parameter_depends_on": "parameter_depends_on.jsonl",
}

# 每个 step 声明的产出
PROVIDES = {
    "mmlcommand": ("mml_commands",),
    "enrich": ("mml_commands",),  # 原地富化，产出仍是 mml_commands
    "parameter": ("command_parameters", "command_has_parameter", "parameter_depends_on"),
}

# 每个 step 声明的依赖（需要前置产出或磁盘已有的数据产品）
# mmlcommand / parameter 无 requires：各自从 ctx 取外部输入（source / parameter_csv）
REQUIRES = {
    "enrich": ("mml_commands",),
}


def validate_order(steps, out_dir=None):
    """校验 steps 的 requires 都能被满足。

    满足条件（任一）：
      1. 列表中更早的 step 在 provides 里产出了它
      2. out_dir 下对应的产物文件已存在（支持单独重跑某 step）
    out_dir 为 None 时只做纯数据流校验（不查磁盘）。

    raises ValueError 当：未知 step / 某个 requires 无法满足。
    """
    available = set()
    out = Path(out_dir) if out_dir else None
    for name in steps:
        if name not in STEPS:
            raise ValueError(f"未知 step: {name}（已知: {list(STEPS)})")
        for req in REQUIRES.get(name, ()):
            if req in available:
                continue
            fp = None
            if out is not None:
                fp = out / PRODUCT_FILE.get(req, f"{req}.jsonl")
                if fp.exists():
                    available.add(req)
                    continue
            hint = f"（磁盘也没有 {fp.name}）" if fp else ""
            raise ValueError(
                f"step '{name}' 需要 '{req}'，但前面没有 step 产出它{hint}"
            )
        available.update(PROVIDES.get(name, ()))
    return list(steps)
