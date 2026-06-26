# ConfigTask/builder/steps/emit_skeleton.py
"""规则步10 emit_skeleton：把 ctx['skeleton'] 写成 config_tasks.skeleton.jsonl。

每行一个 task 骨架 dict。路径：assets_root/{nf}/{version}/config_tasks.skeleton.jsonl
"""
import json

from builder.steps.registry import step, PRODUCT_FILE


@step("emit_skeleton")
def run(ctx):
    out_dir = ctx["assets_root"] / ctx["nf"] / ctx["version"]
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / PRODUCT_FILE["skeleton"]
    with open(out_file, "w", encoding="utf-8") as f:
        for task in ctx["skeleton"]:
            f.write(json.dumps(task, ensure_ascii=False) + "\n")
    return len(ctx["skeleton"])
