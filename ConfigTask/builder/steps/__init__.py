"""导入所有已实现的 step 模块以触发注册。"""
from . import scan, extract_steps, cluster, assemble  # noqa: F401
from . import verify_split, verify_merge, verify_rules  # noqa: F401
from . import split_tasks  # noqa: F401
