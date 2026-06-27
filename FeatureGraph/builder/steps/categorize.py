"""Step categorize (Agent): feature_category / config_relevance 精细化分类。

prep → check → ingest。不调 LLM，纯文件交接（对齐 split_tasks）：
- prep：pending 特性按 batch 写 prompt 到 agent_prompts/categorize/{batch_key}.txt
- check：agent_outputs/categorize/{batch_key}.json 齐了 → ingest；未齐 → 返回 "PAUSE"
- ingest：解析输出 → 回填 features.jsonl 的 feature_category/config_relevance/category_reason

build_all 遇 PAUSE 停；调 Agent 写输出后重跑即续。
"""
from __future__ import annotations

from pathlib import Path

from ..core.categorize import batch_key, build_prompt, parse_agent_output
from ..core.io import load_jsonl, write_jsonl
from ..core.legacy import load_legacy_attributes
from .registry import step


@step("categorize", agent=True)
def run(ctx):
    nf, version = ctx["nf"], ctx["version"]
    data_dir = Path(ctx["data_dir"])
    prompts_dir = data_dir / "agent_prompts" / "categorize"
    outputs_dir = data_dir / "agent_outputs" / "categorize"
    prompts_dir.mkdir(parents=True, exist_ok=True)
    outputs_dir.mkdir(parents=True, exist_ok=True)

    features = load_jsonl(data_dir / "features.jsonl")
    sample = ctx.get("sample")
    rerun = ctx.get("rerun_target")
    pending = [f for f in features
               if (not sample or f["feature_code"] in sample)
               and (not rerun or rerun in f["feature_code"])]
    if not pending:
        print(f"  无待分类特性")
        return 0

    legacy_dir = ctx.get("legacy_dir")
    legacy_attrs = load_legacy_attributes(ctx["project_root"] / legacy_dir, nf) if legacy_dir else {}

    batch_size = ctx.get("agent_batch_size", 5)
    batches = [pending[i:i + batch_size] for i in range(0, len(pending), batch_size)]

    # prep：每批写 prompt（幂等）
    for batch in batches:
        key = batch_key([f["feature_code"] for f in batch])
        (prompts_dir / f"{key}.txt").write_text(build_prompt(batch, legacy_attrs), encoding="utf-8")

    # check + ingest：输出齐了的批回填
    results: dict[str, dict] = {}
    still_pending: list[str] = []
    for batch in batches:
        key = batch_key([f["feature_code"] for f in batch])
        out_file = outputs_dir / f"{key}.json"
        if not out_file.exists():
            still_pending.append(key)
            continue
        results.update(parse_agent_output(out_file.read_text(encoding="utf-8"), batch))

    ingested = 0
    if results:
        for f in features:
            r = results.get(f["feature_code"])
            if not r:
                continue
            if r.get("feature_category"):
                f["feature_category"] = r["feature_category"]
            if r.get("config_relevance"):
                f["config_relevance"] = r["config_relevance"]
            f["category_reason"] = r.get("reason", "")
            ingested += 1
        write_jsonl(data_dir / "features.jsonl", features)

    if still_pending:
        print(f"  prep: {len(batches)} 批 prompt 就绪 → {prompts_dir}")
        print(f"  已回填 {ingested} 特性；仍待处理 {len(still_pending)} 批:")
        for k in still_pending[:12]:
            print(f"    - {prompts_dir}/{k}.txt  →  写输出到 {outputs_dir}/{k}.json")
        return "PAUSE"

    print(f"  全部回填: {ingested} 特性分类完成（{len(batches)} 批）")
    return ingested
