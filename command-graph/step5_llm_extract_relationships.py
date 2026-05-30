"""
Step 5: LLM 语义关系抽取

用 DeepSeek LLM 从命令文档中抽取语义关系：
- 参数→参数条件依赖
- 命令→命令前置依赖
- 命令→命令引用关系
- 参数→参数互斥关系
- 风险等级
- 生效时机
- 配置对象层级关系

每条关系包含 evidence_text（原文引用）。
"""
import csv
import json
import time
import hashlib
import random
from pathlib import Path
from collections import Counter, defaultdict

from llm_client import chat_json, chat

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

INPUT_COMMANDS = DATA_DIR / "udg_command_metadata.csv"
OUTPUT_RAW = DATA_DIR / "udg_semantic_relationships_raw.json"

# ── LLM Prompt ──────────────────────────────────

SYSTEM_PROMPT = """你是一个通信网络MML命令文档分析专家。你的任务是从MML命令文档中抽取语义关系。

你需要抽取以下类型的关系，每条关系必须包含 evidence_text（原文引用）：

1. **param_condition** - 参数条件依赖：当参数A的值为X时，参数B变为必选/可选
   格式: {"type": "param_condition", "from": "参数A", "to": "参数B", "condition": "参数A=X", "effect": "必选/可选", "evidence_text": "原文引用"}

2. **cmd_prerequisite** - 命令前置依赖：执行命令A前必须先执行命令B
   格式: {"type": "cmd_prerequisite", "from": "命令A", "to": "命令B", "description": "描述", "evidence_text": "原文引用"}

3. **cmd_reference** - 命令引用关系：命令A的参数说明中引用了命令B
   格式: {"type": "cmd_reference", "from": "命令A", "to": "命令B", "description": "描述", "evidence_text": "原文引用"}

4. **param_exclusion** - 参数互斥：参数A和参数B不能同时配置
   格式: {"type": "param_exclusion", "from": "参数A", "to": "参数B", "description": "描述", "evidence_text": "原文引用"}

5. **risk_level** - 风险等级：命令的风险级别和说明
   格式: {"type": "risk_level", "from": "命令名", "to": "", "risk": "high/medium/low", "description": "描述", "evidence_text": "原文引用"}

6. **effect_timing** - 生效时机：命令执行后何时生效
   格式: {"type": "effect_timing", "from": "命令名", "to": "", "timing": "立即生效/下次注册/重启后等", "evidence_text": "原文引用"}

7. **config_object_hierarchy** - 配置对象层级：对象A包含/依赖于对象B
   格式: {"type": "config_object_hierarchy", "from": "对象A", "to": "对象B", "relation": "contains/depends_on", "evidence_text": "原文引用"}

请严格按JSON格式输出，不要输出其他内容。输出格式：
{"relationships": [...]}

如果没有发现任何关系，输出：{"relationships": []}

重要规则：
- evidence_text 必须是文档中的原文，不能改写
- 只抽取文档中明确表达的关系，不要推测
- 每条关系都要有意义，不要抽取无价值的关系"""

USER_TEMPLATE = """请分析以下MML命令文档，抽取所有语义关系：

## 命令名
{command_name}

## 命令功能
{description}

## 注意事项
{notes}

## 参数说明
{params}

## 使用实例
{example}

## 输出结果说明
{output_desc}"""


def make_id(*parts):
    raw = ":".join(str(p) for p in parts)
    return hashlib.md5(raw.encode()).hexdigest()[:10]


def extract_for_command(row: dict) -> list[dict]:
    """对单个命令文档进行 LLM 抽取。"""
    user_msg = USER_TEMPLATE.format(
        command_name=row.get("command_name", ""),
        description=row.get("description", ""),
        notes=row.get("notes", ""),
        params=row.get("param_table_raw", "")[:3000],  # 限制长度
        example=row.get("usage_example_raw", "")[:1000],
        output_desc=row.get("output_description_raw", "")[:1000],
    )

    try:
        result = chat_json(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_msg},
            ],
            temperature=0.1,
            max_tokens=4096,
        )
        relationships = result.get("relationships", [])
        return relationships
    except Exception as e:
        print(f"  [ERROR] LLM failed for {row['command_name']}: {e}")
        return []


def main():
    # 读取命令元数据
    with open(INPUT_COMMANDS, encoding="utf-8-sig") as f:
        commands = list(csv.DictReader(f))

    # 过滤：只处理有内容的命令（有注意事项或参数说明的优先）
    rich_commands = [c for c in commands if c.get("notes") or c.get("param_table_raw")]
    print(f"总命令数: {len(commands)}")
    print(f"有内容的命令: {len(rich_commands)}")

    # 检查已完成的进度
    completed_commands = set()
    all_relationships = []
    if OUTPUT_RAW.exists():
        with open(OUTPUT_RAW, encoding="utf-8") as f:
            existing = json.load(f)
        all_relationships = existing
        completed_commands = {r["source_command"] for r in all_relationships if "source_command" in r}
        print(f"已有 {len(completed_commands)} 条命令已处理，跳过")

    # 待处理
    todo = [c for c in rich_commands if c["command_name"] not in completed_commands]
    print(f"待处理: {len(todo)}")

    # 优先处理用户面服务管理（最有价值）
    todo_user = [c for c in todo if c["service_category"] == "用户面服务管理"]
    todo_other = [c for c in todo if c["service_category"] != "用户面服务管理"]
    todo = todo_user + todo_other

    stats = Counter()

    for i, cmd in enumerate(todo):
        cmd_name = cmd["command_name"]
        print(f"[{i+1}/{len(todo)}] {cmd_name} ...", end=" ", flush=True)

        rels = extract_for_command(cmd)

        # 添加元数据
        for rel in rels:
            rel["source_command"] = cmd_name
            rel["source_file"] = cmd.get("file_path", "")
            rel["relation_id"] = make_id(
                rel.get("type", ""),
                rel.get("from", ""),
                rel.get("to", ""),
                cmd_name,
            )
            rel["service_category"] = cmd.get("service_category", "")
            rel["service_domain"] = cmd.get("service_domain", "")
            all_relationships.append(rel)
            stats[rel.get("type", "unknown")] += 1

        print(f"{len(rels)} 条关系")

        # 每 50 条保存一次
        if (i + 1) % 50 == 0:
            with open(OUTPUT_RAW, "w", encoding="utf-8") as f:
                json.dump(all_relationships, f, ensure_ascii=False, indent=2)
            print(f"  [保存] 累计 {len(all_relationships)} 条关系")

        # 速率控制
        time.sleep(0.5)

    # 最终保存
    with open(OUTPUT_RAW, "w", encoding="utf-8") as f:
        json.dump(all_relationships, f, ensure_ascii=False, indent=2)

    # 统计
    print(f"\n===== Step 5 LLM 语义关系抽取结果 =====")
    print(f"总关系数: {len(all_relationships)}")
    print(f"\n--- 关系类型分布 ---")
    for rtype, count in stats.most_common():
        print(f"  {rtype}: {count}")

    # 审计报告
    audit_dir = DATA_DIR / "audit"
    audit_dir.mkdir(exist_ok=True)
    with open(audit_dir / "step5_audit_v1.md", "w", encoding="utf-8") as f:
        f.write("# Step 5 审计报告 v1\n\n")
        f.write(f"## 统计\n\n")
        f.write(f"- 处理命令数: {len(todo) + len(completed_commands)}\n")
        f.write(f"- 总关系数: {len(all_relationships)}\n\n")
        f.write(f"## 关系类型分布\n\n")
        for rtype, count in stats.most_common():
            f.write(f"- {rtype}: {count}\n")

        # 各类型抽样
        by_type = defaultdict(list)
        for rel in all_relationships:
            by_type[rel.get("type", "unknown")].append(rel)

        for rtype in ["cmd_prerequisite", "cmd_reference", "param_condition"]:
            samples = by_type.get(rtype, [])[:5]
            if samples:
                f.write(f"\n### {rtype} 样本\n\n")
                for s in samples:
                    f.write(f"- **{s.get('from', '')}** → **{s.get('to', '')}**: {s.get('description', s.get('effect', ''))[:80]}\n")
                    f.write(f"  > {s.get('evidence_text', '')[:100]}\n")

    print(f"\n审计报告: {audit_dir / 'step5_audit_v1.md'}")
    print(f"输出: {OUTPUT_RAW}")


if __name__ == "__main__":
    main()
