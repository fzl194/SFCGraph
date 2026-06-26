# ConfigTask/builder/steps/select.py
"""规则步1 select：从 feature_files.csv 圈配置类文档，可选按 feature_id 单特性过滤。

provides: feature_docs（存入 ctx['feature_docs']）
"""
from builder.steps.registry import step
from builder.core.csv_loader import load_configurable_features


@step("select", provides=("feature_docs",))
def run(ctx):
    docs = load_configurable_features(ctx["feature_csv"], str(ctx["project_root"]))
    fid = ctx.get("feature_id")
    if fid:
        docs = [d for d in docs if d.feature_id == fid]
    ctx["feature_docs"] = docs
    return len(docs)
