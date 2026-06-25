"""CommandGraph 常量集中（去掉绝对路径与魔数）。

从旧 command-graph/builder/build_commandparameter.py 搬出，去掉硬编码。
"""

# 占位参数名集合（旧 build_commandparameter.py:21）
# 命中即跳过该行，不产 CommandParameter
PLACEHOLDER_PARAMETER_NAMES = frozenset({"zhanwei", "占位", "placeholder"})

# 占位参数 native id（旧 build_commandparameter.py:98 is_placeholder_row 里写死的 -2）
PLACEHOLDER_ID = -2

# MMLCommand 默认状态（旧 build_mmlcommand.py:43 'active'）
ACTIVE_STATUS = "active"
