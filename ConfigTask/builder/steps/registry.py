# ConfigTask/builder/steps/registry.py
"""step 注册表：STEPS/PROVIDES/REQUIRES/PRODUCT_FILE + 顺序校验。

数据流语义：
- select provides feature_docs（声明产物）
- parse→…→assemble 在 ctx 内增量丰富 in-memory skeleton（enrichment，不每步落盘）
- emit_skeleton 序列化 skeleton
- requires 仅 select→parse 生效；skeleton 链靠步骤顺序保证
"""
STEPS = {}        # name → callable(ctx)->int
PROVIDES = {}     # name → tuple of product names
REQUIRES = {}     # name → tuple of required product names
PRODUCT_FILE = {
    "feature_docs": "feature_docs.jsonl",
    "skeleton": "config_tasks.skeleton.jsonl",
}


def step(name, provides=(), requires=()):
    """装饰器：注册一个 pipeline 步骤。"""
    def deco(fn):
        STEPS[name] = fn
        PROVIDES.setdefault(name, tuple(provides))
        REQUIRES.setdefault(name, tuple(requires))
        return fn
    return deco


def validate_order(steps):
    """校验步骤顺序：每个 step 的 requires 必须在它之前有 step provides。"""
    seen = set()
    for s in steps:
        for r in REQUIRES.get(s, ()):
            assert r in seen, f"步骤 {s} 需要 {r}，但未在它之前提供"
        seen.update(PROVIDES.get(s, ()))
