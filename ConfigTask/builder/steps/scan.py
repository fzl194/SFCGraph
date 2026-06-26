# ConfigTask/builder/steps/scan.py
"""Step 0: 扫描语料目录 → corpus_manifest.csv"""
import csv
import re
import pathlib

from builder.steps.registry import step

FEATURE_ID_RE = re.compile(r'((?:GWFD|WSFD|IPFD|NPFD)-\d{6})')


@step("scan", output_file="corpus_manifest.csv")
def run(ctx):
    """扫描 corpus_root 下所有 md，标记 has_task_example/has_operation_steps/has_operation_flow。"""
    root = ctx["project_root"] / ctx["corpus_root"]
    data_dir = ctx["data_dir"]
    data_dir.mkdir(parents=True, exist_ok=True)

    results = []
    for md in root.rglob("*.md"):
        try:
            text = md.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        rel = md.relative_to(ctx["project_root"])
        parts = md.relative_to(root).parts
        fid_match = FEATURE_ID_RE.search(str(rel))
        results.append({
            "product": ctx["nf"],
            "feature_id": fid_match.group(1) if fid_match else "",
            "category": parts[0] if parts else "",
            "doc_name": md.stem,
            "has_task_example": "任务示例" in text,
            "has_operation_steps": "操作步骤" in text,
            "has_operation_flow": "操作流程" in text,
            "doc_path": str(rel).replace("\\", "/"),
        })

    out = data_dir / "corpus_manifest.csv"
    with open(out, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(results[0].keys()))
        w.writeheader()
        w.writerows(results)

    n_eligible = sum(1 for r in results if r["has_task_example"] and r["has_operation_steps"])
    print(f"  扫描 {len(results)} md, {n_eligible} 可抽 task")
    return len(results)
