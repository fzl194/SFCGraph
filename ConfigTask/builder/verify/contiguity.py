# ConfigTask/builder/verify/contiguity.py
"""连续性核查：step_range 覆盖 [1, N] 无重叠无缺口。"""


def verify_contiguity(candidates, total_steps):
    """检查 step_range 覆盖 [1, total_steps] 无重叠无缺口。

    Args:
        candidates: [{"step_range": [start, end], ...}, ...]
        total_steps: 原文档总步数
    Returns:
        list[str]: 错误消息列表
    """
    if not candidates:
        return [] if total_steps == 0 else [f"无 candidate 但有 {total_steps} 步"]

    covered = set()
    errors = []
    for c in candidates:
        sr = c.get("step_range")
        if sr is None:
            # step_range=None 表示覆盖全文（用于 step_num 重复编号的文档）
            continue
        if not sr or len(sr) != 2:
            errors.append(f"无效 step_range: {sr}")
            continue
        start, end = sr
        for n in range(start, end + 1):
            if n in covered:
                errors.append(f"步骤重叠: {n}")
            covered.add(n)

    # 只在 step_num 唯一时检查缺口（有 None candidate 时不检查）
    has_null_range = any(c.get("step_range") is None for c in candidates)
    if not has_null_range:
        for n in range(1, total_steps + 1):
            if n not in covered:
                errors.append(f"步骤缺口: {n}")

    return errors
