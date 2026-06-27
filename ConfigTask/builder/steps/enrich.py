# ConfigTask/builder/steps/enrich.py
"""Step 3.5: 给 cluster member 内联补充证据（step_text + command_examples + param_rows）。

聚类后每个 member 只剩 commands/desc，merge_fields 还得回读 md——本步把证据一次性补进去：
- step_text：操作步骤里命中命令的步骤描述（复用 doc_steps）
- command_examples：任务示例里命中命令的 MML 配置原文
- param_rows：数据规划表里命中命令的参数行（含 获取方法，binding_type 依据）

每个原始文档只读一次（按 doc_path 缓存），写入 enriched task_clusters.jsonl。
之后 merge_fields 只对内联数据做 LLM 推理，不再读 md。
"""
import json

from builder.steps.registry import step
from builder.core.md_reader import read_sections
from builder.core.enrich import (
    extract_command_examples,
    extract_param_rows,
    extract_step_text,
)
from builder.constants import SECTION_EXAMPLE, SECTION_DATA


def _load_doc_steps(data_dir) -> dict:
    """doc_steps.jsonl → {doc_path: record}。"""
    path = data_dir / "doc_steps.jsonl"
    out = {}
    if not path.exists():
        return out
    with open(path, encoding="utf-8") as f:
        for line in f:
            rec = json.loads(line)
            out[rec["doc_path"]] = rec
    return out


@step("enrich", output_file="task_clusters_enriched.jsonl")
def run(ctx):
    data_dir = ctx["data_dir"]
    project_root = ctx["project_root"]
    clusters_path = data_dir / "task_clusters.jsonl"        # 输入：cluster 产出的裸簇
    out_path = data_dir / "task_clusters_enriched.jsonl"    # 输出：带证据，独立文件

    # 读 clusters
    with open(clusters_path, encoding="utf-8") as f:
        clusters = [json.loads(line) for line in f]
    print(f"  输入: {len(clusters)} 簇")

    doc_steps = _load_doc_steps(data_dir)

    # 收集所有 member 涉及的唯一 doc_path（每个文档只读一次）
    doc_paths = {}
    for cl in clusters:
        for m in cl["members"]:
            doc_paths.setdefault(m["doc_path"], True)

    # 按文档读 md、切段（缓存）
    sections_cache: dict[str, dict] = {}
    miss = 0
    for dp in doc_paths:
        full = project_root / dp
        if not full.exists():
            miss += 1
            sections_cache[dp] = {}
            continue
        md = full.read_text(encoding="utf-8", errors="ignore")
        sections_cache[dp] = read_sections(md)
    if miss:
        print(f"  警告: {miss} 个文档缺失（member 证据为空）")

    # 给每个 member 补证据
    enriched_members = 0
    empty_members = 0
    for cl in clusters:
        for m in cl["members"]:
            cmds = m.get("commands", [])
            dp = m["doc_path"]
            secs = sections_cache.get(dp, {})
            rec = doc_steps.get(dp, {})

            step_text = extract_step_text(rec, cmds)
            examples = extract_command_examples(secs.get(SECTION_EXAMPLE, ""), cmds)
            rows = extract_param_rows(secs.get(SECTION_DATA, ""), cmds)

            m["step_text"] = step_text
            m["command_examples"] = examples
            m["param_rows"] = rows

            if step_text or examples or rows:
                enriched_members += 1
            else:
                empty_members += 1

    # 写 enriched clusters（独立文件，不污染 cluster 的裸簇输出）
    with open(out_path, "w", encoding="utf-8") as f:
        for cl in clusters:
            f.write(json.dumps(cl, ensure_ascii=False) + "\n")

    print(f"  补证据: {enriched_members} member 有证据, {empty_members} member 空")
    return len(clusters)
