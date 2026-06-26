# ConfigTask/builder/verify/completeness.py
"""完整性核查：命令无遗漏、无重复。"""
from collections import Counter


def verify_completeness(doc, candidates):
    """检查所有命令被覆盖且仅出现一次。

    Args:
        doc: {"steps": [{"commands": [...]}, ...]}
        candidates: [{"commands": [...]}, ...]
    Returns:
        list[str]: 错误消息列表（空 = 通过）
    """
    all_cmds = []
    for s in doc.get("steps", []):
        all_cmds.extend(s.get("commands", []))
    expected = Counter(all_cmds)

    actual = Counter()
    for c in candidates:
        actual.update(c.get("commands", []))

    errors = []
    for cmd, count in expected.items():
        if actual[cmd] < count:
            errors.append(f"命令遗漏: {cmd} (期望 {count}, 实际 {actual[cmd]})")
    for cmd, count in actual.items():
        if cmd in expected and count > expected[cmd]:
            errors.append(f"命令重复: {cmd} (期望 {expected[cmd]}, 实际 {count})")
    return errors
