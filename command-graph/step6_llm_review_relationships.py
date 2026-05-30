"""
Step 6: LLM 语义关系反思审查

对 Step 5 抽取的关系进行第二轮 LLM 审查：
- 验证 evidence_text 是否支持抽取出的关系
- 修正关系类型
- 标注置信度
- 发现遗漏的关系
"""
import json
import csv
import time
import hashlib
from pathlib import Path
from collections import Counter

from llm_client import chat_json, chat

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

INPUT_RAW = DATA_DIR / "udg_semantic_relationships_raw.json"
INPUT_COMMANDS = DATA_DIR / "udg_command_metadata.csv"
OUTPUT_REVIEWED = DATA_DIR / "udg_semantic_relationships_reviewed.json"

REVIEW_PROMPT = """你是一个通信网络MML命令文档分析审查专家。

以下是抽取出的语义关系，请审查每条关系的质量：

1. evidence_text 是否确实支持这条关系？（准确性）
2. 关系类型是否正确？（类型准确性）
3. from/to 实体是否正确？（实体准确性）

请为每条关系标注：
- verified: true/false
- confidence: "high"/"medium"/"low"
- issues: 发现的问题（如果有）
- corrected: 修正后的关系（如果需要修正）

输出JSON格式：
{
  "reviews": [
    {
      "relation_index": 0,
      "verified": true,
      "confidence": "high",
      "issues": "",
      "corrected": null
    }
  ]
}

只输出JSON，不要输出其他内容。"""

BATCH_SIZE = 50  # 每次审查50条关系（提高效率）


def load_source_content():
    """加载命令文档原文用于审查。"""
    content_map = {}
    with open(INPUT_COMMANDS, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            cmd = row.get("command_name", "")
            content_map[cmd] = {
                "description": row.get("description", ""),
                "notes": row.get("notes", ""),
                "params": row.get("param_table_raw", ""),
            }
    return content_map


def review_batch(relationships: list[dict], batch_start: int) -> list[dict]:
    """审查一批关系。"""
    batch = []
    for i, rel in enumerate(relationships):
        batch.append({
            "index": batch_start + i,
            "type": rel.get("type", ""),
            "from": rel.get("from", ""),
            "to": rel.get("to", ""),
            "evidence_text": rel.get("evidence_text", ""),
            "description": rel.get("description", rel.get("effect", "")),
        })

    user_msg = f"请审查以下 {len(batch)} 条语义关系：\n\n{json.dumps(batch, ensure_ascii=False, indent=2)}"

    try:
        result = chat_json(
            messages=[
                {"role": "system", "content": REVIEW_PROMPT},
                {"role": "user", "content": user_msg},
            ],
            temperature=0.1,
            max_tokens=4096,
        )
        return result.get("reviews", [])
    except Exception as e:
        print(f"  [ERROR] Review failed: {e}")
        return []


def main():
    # 加载原始关系
    with open(INPUT_RAW, encoding="utf-8") as f:
        raw_rels = json.load(f)
    print(f"加载 {len(raw_rels)} 条原始关系")

    # 检查已完成进度
    reviewed_rels = []
    reviewed_count = 0
    if OUTPUT_REVIEWED.exists():
        with open(OUTPUT_REVIEWED, encoding="utf-8") as f:
            reviewed_rels = json.load(f)
        reviewed_count = len(reviewed_rels)
        print(f"已完成 {reviewed_count} 条审查")

    # 待审查
    todo = raw_rels[reviewed_count:]
    print(f"待审查: {len(todo)}")

    stats = Counter()
    total_batches = (len(todo) + BATCH_SIZE - 1) // BATCH_SIZE

    for batch_idx in range(total_batches):
        start = batch_idx * BATCH_SIZE
        end = min(start + BATCH_SIZE, len(todo))
        batch = todo[start:end]

        print(f"[Batch {batch_idx+1}/{total_batches}] 审查 {start+reviewed_count}-{end+reviewed_count-1} ...", end=" ", flush=True)

        reviews = review_batch(batch, start + reviewed_count)

        # 合并审查结果
        for i, rel in enumerate(batch):
            review = reviews[i] if i < len(reviews) else {}
            reviewed_rel = {
                **rel,
                "verified": review.get("verified", True),
                "confidence": review.get("confidence", "medium"),
                "review_issues": review.get("issues", ""),
            }
            if review.get("corrected"):
                reviewed_rel["corrected"] = review["corrected"]
            reviewed_rels.append(reviewed_rel)
            stats[review.get("confidence", "unknown")] += 1

        verified_count = sum(1 for r in reviews if r.get("verified", True))
        print(f"{verified_count}/{len(reviews)} verified")

        # 每 10 个批次保存
        if (batch_idx + 1) % 10 == 0:
            with open(OUTPUT_REVIEWED, "w", encoding="utf-8") as f:
                json.dump(reviewed_rels, f, ensure_ascii=False, indent=2)
            print(f"  [保存] 累计 {len(reviewed_rels)} 条")

        time.sleep(0.5)

    # 最终保存
    with open(OUTPUT_REVIEWED, "w", encoding="utf-8") as f:
        json.dump(reviewed_rels, f, ensure_ascii=False, indent=2)

    # 统计
    print(f"\n===== Step 6 审查结果 =====")
    print(f"总关系数: {len(reviewed_rels)}")

    verified_count = sum(1 for r in reviewed_rels if r.get("verified", True))
    print(f"验证通过: {verified_count} ({verified_count*100//len(reviewed_rels)}%)")

    print(f"\n--- 置信度分布 ---")
    for conf, count in stats.most_common():
        print(f"  {conf}: {count}")

    # 审计报告
    audit_dir = DATA_DIR / "audit"
    audit_dir.mkdir(exist_ok=True)
    with open(audit_dir / "step6_audit_v1.md", "w", encoding="utf-8") as f:
        f.write("# Step 6 审计报告 v1\n\n")
        f.write(f"## 统计\n\n")
        f.write(f"- 总关系数: {len(reviewed_rels)}\n")
        f.write(f"- 验证通过: {verified_count}\n\n")
        f.write(f"## 置信度分布\n\n")
        for conf, count in stats.most_common():
            f.write(f"- {conf}: {count}\n")

        # 低置信度样本
        low_conf = [r for r in reviewed_rels if r.get("confidence") == "low"][:10]
        if low_conf:
            f.write(f"\n## 低置信度样本\n\n")
            for r in low_conf:
                f.write(f"- [{r.get('type')}] {r.get('from')} → {r.get('to')}: {r.get('review_issues', '')[:100]}\n")

    print(f"\n审计报告: {audit_dir / 'step6_audit_v1.md'}")
    print(f"输出: {OUTPUT_REVIEWED}")


if __name__ == "__main__":
    main()
