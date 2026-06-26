# ConfigTask/builder/steps/select.py
"""规则步1 select：从 feature_files.csv 圈配置类文档，可选按 feature_id 单特性过滤。

provides: feature_docs（存入 ctx['feature_docs']）
"""
import os

from builder.steps.registry import step
from builder.core.csv_loader import load_configurable_features


@step("select", provides=("feature_docs",))
def run(ctx):
    csv_path = ctx["feature_csv"]
    if not os.path.isabs(csv_path):
        csv_path = os.path.normpath(os.path.join(str(ctx["project_root"]), csv_path))
    docs = load_configurable_features(csv_path, str(ctx["project_root"]))
    fid = ctx.get("feature_id")
    if fid:
        docs = [d for d in docs if d.feature_id == fid]
    ctx["feature_docs"] = docs
    return len(docs)
