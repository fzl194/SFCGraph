"""categorize Agent 步骨架（prep/check/ingest，对齐 ConfigTask split_tasks）。

prep: 待分类特性(所有或 sample 子集)按 batch_size 分批 → prompt 写
      data/{nf}/{version}/agent_prompts/categorize/{batch_key}.txt
check: data/{nf}/{version}/agent_outputs/categorize/{batch_key}.json 齐了 → ingest；未齐 → 返回 PAUSE
ingest: 解析输出 {feature_code: {feature_category, config_relevance, reason}} → 回填 features.jsonl

不调 LLM，纯文件交接。build_all 遇 PAUSE 停（尾随 verify 仍跑）。
"""
from __future__ import annotations

import hashlib
import json
import re

from ..agent.prompts import CATEGORIZE_PROMPT
from ..core.legacy import load_legacy_attributes


def batch_key(codes: list[str]) -> str:
    """批内特性集合的稳定哈希 → batch_<hash8>。"""
    h = hashlib.md5("|".join(sorted(codes)).encode()).hexdigest()[:8]
    return f"batch_{h}"


def build_agent_input(features: list[dict], legacy_attrs: dict) -> list[dict]:
    """构造 Agent 输入（每特性含分类所需上下文 + 规则初值 + 旧值参考）。"""
    out: list[dict] = []
    for f in features:
        code = f["feature_code"]
        la = legacy_attrs.get(code, {})
        out.append({
            "feature_code": code,
            "name": f.get("name", ""),
            "catalog_section": f.get("catalog_section", ""),
            "definition_raw": (f.get("definition_raw", "") or "")[:400],
            "has_activation_doc": f.get("has_activation_doc", False),
            "rule_initial_category": f.get("feature_category", ""),
            "rule_initial_config_relevance": f.get("config_relevance", ""),
            "legacy_feature_type": la.get("feature_type", ""),
            "legacy_config_required": la.get("config_required", ""),
        })
    return out


def build_prompt(batch: list[dict], legacy_attrs: dict) -> str:
    input_data = build_agent_input(batch, legacy_attrs)
    return CATEGORIZE_PROMPT.format(
        n=len(batch),
        first_code=batch[0]["feature_code"] if batch else "",
        input_json=json.dumps(input_data, ensure_ascii=False, indent=2),
    )


def parse_agent_output(raw_text: str, batch: list[dict]) -> dict:
    """解析 Agent 输出 → {feature_code: {feature_category, config_relevance, reason}}。

    输出可为 dict 或含 JSON 的文本。
    """
    if isinstance(raw_text, dict):
        data = raw_text
    else:
        m = re.search(r'\{.*\}', raw_text, re.DOTALL)
        if not m:
            return {}
        data = json.loads(m.group())
    return {code: data.get(code, {}) for code in [f["feature_code"] for f in batch]}
