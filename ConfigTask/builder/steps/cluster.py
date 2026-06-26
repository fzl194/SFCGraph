# ConfigTask/builder/steps/cluster.py
"""Step 3: 按命令集聚类 task candidates → task_clusters.jsonl"""
from builder.steps.registry import step


@step("cluster", output_file="task_clusters.jsonl")
def run(ctx):
    print("  (待实现)")
    return 0
