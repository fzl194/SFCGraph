# ConfigTask/builder/agent/prompts.py
"""Agent prompt 模板。"""

SPLIT_TASKS_PROMPT = """你是 ConfigTask 拆分 Agent。下面是 {n_docs} 份配置文档的步骤清单，请逐份拆分成 task candidate。

【task 定义】一个 task = 一组连续步骤，共同完成一个可命名的配置动作（如"配置计费动作链"）。

【拆分信号】（按优先级）
1. 配置对象族切换：命令操作的对象从 URR 族变成 FILTER 族 = 不同 task
   对象族参考：URR族={{URR,URRGROUP,PCCPOLICYGRP}} / FILTER族={{FILTER,L7FILTER,FLOWFILTER,FLTBINDFLOWF,PROTBINDFLOWF}} / RULE族={{RULE}} / PROFILE族={{USERPROFILE,RULEBINDING}} / POOL族={{POOL,SECTION,POOLGROUP,POOLBINDGROUP}} / VPN族={{VPNINST,L3VPNINST,VPNINSTAF}} / OSPF族={{OSPF,OSPFAREA,OSPFNETWORK,OSPFV3,...}} / BWM族={{BWMCONTROLLER,BWMRULE,BWMUSERGROUP}}
2. step_desc 语义切换：描述从"配置过滤条件"变成"添加规则" = 不同 task
3. 收尾命令：SET REFRESHSRV / SET LICENSESWITCH 不单独成 task，并入相邻段
4. 可选步骤：扩展前段语义 → 并入；独立功能 → 单独

【输出格式】严格输出 JSON（不要 markdown 代码块包裹，直接输出 JSON）：
{{
  "{doc_key}": [
    {{
      "step_range": [1, 2],
      "candidate_desc": "配置计费动作链",
      "commands": ["ADD URR", "ADD URRGROUP", "ADD PCCPOLICYGRP"]
    }}
  ]
}}

如果有多份文档，每份一个 key（doc_path）。所有步骤必须被覆盖（step_range 并集 = [1, 总步数]，不遗漏不重叠）。

【输入数据】
{input_json}
"""


MERGE_FIELDS_PROMPT = """你是 ConfigTask 合并 Agent。下面是一个 task 簇（{n_members} 个配置案例），请确证合并并抽取字段。
（详细 prompt 见 spec §4.2）
"""


EXTRACT_RULES_PROMPT = """你是 ConfigTask 规则抽取 Agent。下面是一个 ConfigTask + 命令图谱 notes，请抽取 TaskRule 和 DecisionPoint。
（详细 prompt 见 spec §5.2）
"""
