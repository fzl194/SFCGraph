"""Phase 1: Step 0 语料预筛 + Step 1 抽步骤三元组。

读 corpus_manifest.csv → 过滤（has_task_example + has_operation_steps）→ 标记特殊类型
→ 抽 (step_num, step_desc, commands[], raw_text) → 输出 doc_steps.jsonl

产出：ConfigTask/data/doc_steps.jsonl
"""
import csv
import json
import re
import sys
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "ConfigTask"))

from builder.core.md_reader import read_sections  # noqa: E402
from builder.constants import SECTION_STEPS, SECTION_FLOW  # noqa: E402

DATA_DIR = PROJECT_ROOT / "ConfigTask" / "data"

_CMD_RE = re.compile(r'\b(ADD|SET|MOD|DEL|RMV|LST|DSP)\s+(\w+)\b')
_STEP_START_RE = re.compile(r'^(\d+)\.\s', re.MULTILINE)
# 差异配置关键词
_DIFF_KEYWORDS = ("参考部署", "此处仅描述差异", "详细配置请参考", "此处仅描述")


def parse_step_triplets(steps_text: str) -> list:
    """操作步骤段 → [(step_num, step_desc, commands[], raw_text)]"""
    starts = [(m.start(), int(m.group(1))) for m in _STEP_START_RE.finditer(steps_text)]
    triplets = []
    for i, (start, num) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(steps_text)
        block = steps_text[start:end].strip()
        # step_desc: 第一行 "N. xxx" 的 xxx（到换行或句号）
        desc_m = re.match(r'\d+\.\s*(.+?)(?:\n|。)', block)
        desc = desc_m.group(1).strip() if desc_m else ""
        # commands
        cmds = [f"{v} {k}" for v, k in _CMD_RE.findall(block)]
        triplets.append({
            "step_num": num,
            "step_desc": desc,
            "commands": cmds,
            "raw_text": block,
        })
    return triplets


def detect_doc_type(cmds: list, full_text: str) -> str:
    """检测文档特殊类型：license_only / difference_only / standard"""
    if cmds and all("LICENSESWITCH" in c for c in cmds):
        return "license_only"
    if any(kw in full_text for kw in _DIFF_KEYWORDS):
        return "difference_only"
    return "standard"


def main():
    manifest = DATA_DIR / "corpus_manifest.csv"
    output = DATA_DIR / "doc_steps.jsonl"

    results = []
    skipped = 0
    with open(manifest, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            # Step 0: 过滤
            if row.get("has_task_example") != "True" or row.get("has_operation_steps") != "True":
                continue
            doc_path = PROJECT_ROOT / row["doc_path"]
            if not doc_path.exists():
                skipped += 1
                continue

            md_text = doc_path.read_text(encoding="utf-8", errors="ignore")
            sections = read_sections(md_text)
            steps_text = sections.get(SECTION_STEPS, "")
            if not steps_text:
                skipped += 1
                continue

            # Step 1: 抽步骤三元组
            triplets = parse_step_triplets(steps_text)
            if not triplets:
                skipped += 1
                continue

            all_cmds = [c for t in triplets for c in t["commands"]]
            doc_type = detect_doc_type(all_cmds, md_text)
            has_flow = bool(sections.get(SECTION_FLOW, ""))

            results.append({
                "doc_path": row["doc_path"],
                "feature_id": row.get("feature_id", ""),
                "product": row.get("product", ""),
                "category": row.get("category", ""),
                "doc_type": doc_type,
                "has_operation_flow": has_flow,
                "num_steps": len(triplets),
                "total_commands": len(all_cmds),
                "steps": triplets,
            })

    with open(output, "w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    # 统计
    print(f"产出文档数: {len(results)}（跳过 {skipped}）")
    by_type = {}
    for r in results:
        by_type[r["doc_type"]] = by_type.get(r["doc_type"], 0) + 1
    print(f"按类型: {by_type}")
    with_flow = sum(1 for r in results if r["has_operation_flow"])
    print(f"有操作流程: {with_flow} / {len(results)}")
    total_steps = sum(r["num_steps"] for r in results)
    total_cmds = sum(r["total_commands"] for r in results)
    print(f"总步骤: {total_steps}, 总命令: {total_cmds}")
    by_product = {}
    for r in results:
        by_product[r["product"]] = by_product.get(r["product"], 0) + 1
    print(f"按网元: {by_product}")


if __name__ == "__main__":
    main()
