"""派生字段 extractor 注册表。

机制：
  每个 extractor 文件用 @register('field_name') 注册一个 (cmd: dict) -> value 函数。
  enrich 步骤调 apply_all(cmd) 遍历全部已注册 extractor，把结果合并进【新 dict】返回
  （immutable：不修改入参 cmd）。

加派生字段 = 新建一个 extractor 文件 + 写一行 @register(...)，无需改本文件。
"""
from typing import Callable, Dict, List, Tuple

# 保持注册顺序，便于稳定的非空率打印
_REGISTRY: List[Tuple[str, Callable[[dict], object]]] = []
_BY_NAME: Dict[str, Callable[[dict], object]] = {}


def register(name: str):
    """装饰器：把 (cmd: dict) -> value 函数注册为派生字段 `name` 的 extractor。"""

    def decorator(fn: Callable[[dict], object]):
        if name in _BY_NAME:
            raise ValueError(f"duplicate extractor field: {name}")
        _BY_NAME[name] = fn
        _REGISTRY.append((name, fn))
        return fn

    return decorator


def names() -> List[str]:
    """已注册的派生字段名（按注册顺序）。"""
    return [n for n, _ in _REGISTRY]


def apply_all(cmd: dict) -> dict:
    """对 cmd 跑全部已注册 extractor，返回加了派生字段的【新 dict】。"""
    out = dict(cmd)  # immutable：拷贝，不动入参
    for name, fn in _REGISTRY:
        out[name] = fn(out)
    return out


# 导入各 extractor 模块以触发 @register。放在末尾以避免循环导入。
from . import (  # noqa: E402,F401
    command_category,
    applicable_nf,
    max_records,
    permission_groups,
    output_ref_command,
    is_dangerous,
    effect_mode,
    spec_threshold,
    initial_values,
    output_fields,
)
