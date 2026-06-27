# FeatureGraph/builder/agent/prompts.py
"""Agent prompt 模板。"""

CATEGORIZE_PROMPT = """你是 FeatureGraph 特性分类 Agent。下面是 {n} 个特性，请为每个推断 feature_category 和 config_relevance。

【feature_category 枚举】（schema §2.1，5 选 1）
- base: 基础能力（架构、协议底座，如云化分布式软件架构、SA-Basic）
- enhanced: 增强能力（基础上的扩展，如内容计费、智能Shaping、QoS）
- integration: 集成能力（跨特性组合或第三方接入，如 SFIP 第三方应用）
- operations: 运维能力（可靠性、扩缩容、自愈，如 SFFD-* 系列、License 类）
- protocol: 协议能力（协议接入、地址分配、隧道、双栈）

【config_relevance 枚举】（4 选 1）
- required: 需要配置（有明确激活/配置文档）
- indirect: 间接配置（经其他特性配置触发，自身无独立配置动作）
- none: 无需配置（协议底座或自动生效）
- ops_only: 仅运维触发（License 开关、可靠性类，无业务配置）

【判定依据】
- catalog_section + definition_raw 是 feature_category 主依据
- has_activation_doc（是否有激活/配置文档）是 config_relevance 最强信号：true→优先 required/ops_only；false+定义含"无需配置/自动"→none
- rule_initial_* 是规则初值（可能不准，仅参考）；legacy_* 是旧抽取值（覆盖率低，仅参考）

【输出格式】严格输出 JSON（不要 markdown 代码块包裹，直接输出 JSON）：
{{
  "{first_code}": {{"feature_category": "enhanced", "config_relevance": "required", "reason": "计费增强能力，有激活配置文档"}},
  "<其他feature_code>": {{"feature_category": "...", "config_relevance": "...", "reason": "..."}}
}}

每个特性都要输出，feature_code 作为 key。

【输入数据】
{input_json}
"""
