"""全量扫描产品文档目录，找出所有含"任务示例"的配置/激活/部署/调测 md，
按网元拆分输出到 ConfigTask/data/。
"""
import csv
import re
import pathlib
import sys

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent  # SFCGraph/

FEATURE_ID_RE = re.compile(r'((?:GWFD|WSFD|IPFD|NPFD)-\d{6})')

# 产品文档根目录（特性指南）
ROOTS = {
    "UDG": PROJECT_ROOT / "output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南",
    "UNC": PROJECT_ROOT / "output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南",
}


def scan_product(product: str, root: pathlib.Path) -> list:
    """扫描一个产品的特性指南目录，返回所有 md 的元信息。"""
    results = []
    for md in root.rglob("*.md"):
        try:
            text = md.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        has_task_example = "任务示例" in text
        has_operation_steps = "操作步骤" in text
        has_operation_flow = "操作流程" in text
        # 从路径提取 feature_id
        rel = md.relative_to(root)
        parts = rel.parts
        category = parts[0] if parts else ""
        feature_dir = "/".join(parts[1:-1]) if len(parts) > 2 else ""
        fid_match = FEATURE_ID_RE.search(str(rel))
        feature_id = fid_match.group(1) if fid_match else ""
        results.append({
            "product": product,
            "feature_id": feature_id,
            "category": category,
            "feature_dir": feature_dir,
            "doc_name": md.stem,
            "has_task_example": has_task_example,
            "has_operation_steps": has_operation_steps,
            "has_operation_flow": has_operation_flow,
            "doc_path": str(md.relative_to(PROJECT_ROOT)),
        })
    return results


def main():
    data_dir = PROJECT_ROOT / "ConfigTask" / "data"
    all_rows = []
    for product, root in ROOTS.items():
        if root and root.exists():
            print(f"扫描 {product}: {root.relative_to(PROJECT_ROOT)}")
            rows = scan_product(product, root)
            all_rows.extend(rows)
            n_total = len(rows)
            n_te = sum(1 for r in rows if r["has_task_example"])
            n_steps = sum(1 for r in rows if r["has_operation_steps"])
            n_flow = sum(1 for r in rows if r["has_operation_flow"])
            n_both = sum(1 for r in rows if r["has_task_example"] and r["has_operation_steps"])
            print(f"  总 md: {n_total}, 含任务示例: {n_te}, 含操作步骤: {n_steps}, 含操作流程: {n_flow}")
            print(f"  同时含任务示例+操作步骤: {n_both}（=可抽 task 的文档）")
        else:
            print(f"{product}: 根目录未找到")

    # 全量 manifest
    manifest_path = data_dir / "corpus_manifest.csv"
    with open(manifest_path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(all_rows[0].keys()))
        w.writeheader()
        w.writerows(all_rows)
    print(f"\n全量 manifest: {manifest_path}（{len(all_rows)} 行）")

    # 按"含任务示例+操作步骤"过滤 = 可抽 task 的文档
    task_docs = [r for r in all_rows if r["has_task_example"] and r["has_operation_steps"]]
    task_path = data_dir / "task_example_docs.csv"
    with open(task_path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(task_docs[0].keys()))
        w.writeheader()
        w.writerows(task_docs)
    print(f"可抽 task 文档: {task_path}（{len(task_docs)} 行）")

    # 按网元拆分
    for product in ("UDG", "UNC"):
        prod_rows = [r for r in task_docs if r["product"] == product]
        if prod_rows:
            prod_path = data_dir / f"task_example_docs_{product}.csv"
            with open(prod_path, "w", encoding="utf-8-sig", newline="") as f:
                w = csv.DictWriter(f, fieldnames=list(prod_rows[0].keys()))
                w.writeheader()
                w.writerows(prod_rows)
            print(f"  {product}: {prod_path.name}（{len(prod_rows)} 行）")


if __name__ == "__main__":
    main()
