# ConfigTask/builder/steps/registry.py
"""Step 注册表。每个 step 是 callable(ctx) -> int(产出数)。"""
STEPS = {}
PRODUCT_FILE = {}


def step(name, output_file=None):
    """装饰器：注册一个 pipeline step。"""
    def deco(fn):
        STEPS[name] = fn
        if output_file:
            PRODUCT_FILE[name] = output_file
        return fn
    return deco
