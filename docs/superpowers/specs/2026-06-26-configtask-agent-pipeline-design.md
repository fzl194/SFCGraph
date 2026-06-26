# ConfigTask Agent Pipeline 详细设计

> 日期：2026-06-26
> 状态：待用户审阅
> 前置：PIPELINE_DESIGN.md（架构）+ 语料精读追踪.md（实证）+ CONFIGTASK_SCHEMA.md（字段定义）

---

## 0. 设计约束（用户 5 点要求）

1. **统一 pipeline**：scan_corpus + extract_steps + Agent 步骤全部整合到 build_all.py + pipeline.yaml
2. **对齐 CommandGraph**：pipeline.yaml 配置驱动，换网元/版本只改配置
3. **命令图谱作输入参数**：command_graph_dir 在 pipeline.yaml 里配置，内网改路径即可
4. **TDD + 不遗漏 + 可重跑**：Agent 产出必须通过代码核查；progress/ 目录跟踪进度；失败文档自动重跑
5. **Agent 调用最小化**：3 次 Agent（拆 / 合+字段 / 规则+决策），每次做尽可能多的事

---

## 1. Pipeline 结构

### 1.1 目录

```
ConfigTask/
├── pipeline.yaml                ← 唯一配置入口
├── build_all.py                  ← 编排入口
├── builder/
│   ├── core/
│   │   ├── md_reader.py          ← 已有
│   │   └── commands.py           ← 已有
│   ├── constants.py              ← 已有
│   ├── agent/
│   │   ├── prompts.py            ← 3 个 Agent 的 prompt 模板
│   │   └── runner.py             ← Agent 调用 + 输出解析 + 进度管理
│   ├── verify/
│   │   ├── completeness.py       ← 完整性核查
│   │   ├── contiguity.py         ← 连续性核查
│   │   └── object_family.py      ← 对象族核查
│   └── steps/
│       ├── scan.py               ← 代码：语料扫描
│       ├── extract_steps.py      ← 代码：步骤三元组
│       ├── split_tasks.py        ← Agent-1：拆 task
│       ├── verify_split.py       ← 代码：核查拆分
│       ├── cluster.py            ← 代码：命令集聚类
│       ├── merge_fields.py       ← Agent-2：合并+字段
│       ├── verify_merge.py       ← 代码：核查合并
│       ├── extract_rules.py     ← Agent-3：规则+决策
│       ├── verify_rules.py      ← 代码：核查规则
│       └── assemble.py          ← 代码：组装最终 JSONL
├── data/
│   ├── corpus_manifest.csv      ← Step 0 产出（已有）
│   ├── doc_steps.jsonl          ← Step 1 产出（已有）
│   ├── task_candidates.jsonl    ← Agent-1 产出
│   ├── task_clusters.jsonl      ← 聚类产出
│   ├── config_tasks.jsonl       ← Agent-2 产出
│   ├── task_rules.jsonl         ← Agent-3 产出
│   ├── decision_points.jsonl    ← Agent-3 产出
│   ├── progress/                ← 断点续跑
│   │   ├── split_tasks.json     ← {doc_path: "ok"/"fail", ...}
│   │   ├── merge_fields.json
│   │   └── extract_rules.json
│   └── assets/{nf}/{version}/   ← 最终产物（前端消费）
└── tests/
    ├── test_verify_completeness.py
    ├── test_verify_contiguity.py
    └── test_verify_object_family.py
```

### 1.2 pipeline.yaml

```yaml
assets_root: data/assets
project_root: ..

ne:
  UDG:
    20.15.2:
      corpus_root: output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南
      command_graph_dir: CommandGraph/data/assets/UDG/20.15.2
      steps: [scan, extract_steps, split_tasks, verify_split,
              cluster, merge_fields, verify_merge,
              extract_rules, verify_rules, assemble]
      agent_batch_size: 5
  UNC:
    20.15.2:
      corpus_root: output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南
      command_graph_dir: CommandGraph/data/assets/UNC/20.15.2
      steps: [scan, extract_steps, split_tasks, verify_split,
              cluster, merge_fields, verify_merge,
              extract_rules, verify_rules, assemble]
      agent_batch_size: 5
```

### 1.3 build_all.py

```bash
# 全量跑
python build_all.py UDG 20.15.2

# 只跑某个 step（续跑/调试）
python build_all.py UDG 20.15.2 split_tasks

# 重跑某个文档
python build_all.py UDG 20.15.2 split_tasks --rerun GWFD-020301
```

### 1.4 断点续跑 + 不遗漏

每个 Agent step 的执行逻辑：
1. 读全量输入清单（doc_steps.jsonl 里所有文档）
2. 读 progress/{step}.json（已处理的文档 + 状态）
3. 过滤出 todo = 全量 - 已成功
4. 分批调 Agent（每批 agent_batch_size 份）
5. 每批结果过核查 → 通过则标记 "ok"，不通过标记 "fail"
6. 失败的文档下轮自动重试
7. 最终断言：成功数 == 全量数

---

## 2. Agent-1：拆 Task（split_tasks）

### 2.1 输入（每批 5 份文档）

从 `doc_steps.jsonl` 取 5 份文档，每份含：
```json
{
  "doc_path": "output/.../部署UPF_28493406.md",
  "feature_id": "GWFD-020301",
  "doc_type": "standard",
  "has_operation_flow": true,
  "steps": [
    {"step_num": 1, "step_desc": "配置使用量上报规则组属性", "commands": ["ADD URR", "ADD URRGROUP"], "raw_text": "..."},
    {"step_num": 2, "step_desc": "配置PCC策略组", "commands": ["ADD PCCPOLICYGRP"], "raw_text": "..."},
    ...
  ]
}
```

### 2.2 Agent Prompt

```
你是 ConfigTask 拆分 Agent。下面是 {N} 份配置文档的步骤清单，请逐份拆分成 task candidate。

【task 定义】一个 task = 一组连续步骤，共同完成一个可命名的配置动作（如"配置计费动作链"）。

【拆分信号】（按优先级）
1. 配置对象族切换：命令操作的对象从 URR 族变成 FILTER 族 = 不同 task
   对象族参考：URR族={URR,URRGROUP,PCCPOLICYGRP} / FILTER族={FILTER,L7FILTER,FLOWFILTER,FLTBINDFLOWF,PROTBINDFLOWF} / RULE族={RULE} / PROFILE族={USERPROFILE,RULEBINDING} / POOL族={POOL,SECTION,POOLGROUP,POOLBINDGROUP} / VPN族={VPNINST,L3VPNINST,VPNINSTAF} / OSPF族={OSPF,OSPFAREA,OSPFNETWORK} / BWM族={BWMCONTROLLER,BWMRULE,BWMUSERGROUP} / 其他命令各成一族
2. step_desc 语义切换：描述从"配置过滤条件"变成"添加规则" = 不同 task
3. 收尾命令：SET REFRESHSRV / SET LICENSESWITCH 不单独成 task，并入相邻段
4. 可选步骤：扩展前段语义 → 并入；独立功能 → 单独

【输出格式】对每份文档，输出 JSON：
{
  "doc_path": "...",
  "candidates": [
    {
      "step_range": [1, 2],
      "candidate_desc": "配置计费动作链",
      "commands": ["ADD URR", "ADD URRGROUP", "ADD PCCPOLICYGRP"]
    },
    ...
  ]
}

【关键规则】
- 所有步骤必须被覆盖（step_range 的并集 = [1, 总步数]，不遗漏不重叠）
- SET LICENSESWITCH 并入第一个实际配置 task
- SET REFRESHSRV 并入前一个 task
- 1-2 步的简单文档通常就是 1 个 task
- 纯 RMV 删除类如果意图一致，合成 1 个 task

【输入数据】
{5份文档的JSON}
```

### 2.3 输出格式

写入 `task_candidates.jsonl`，每行一个 candidate：
```json
{
  "doc_path": "output/.../部署UPF_28493406.md",
  "feature_id": "GWFD-020301",
  "candidate_id": "GWFD-020301#001",
  "step_range": [1, 2],
  "candidate_desc": "配置计费动作链",
  "commands": ["ADD URR", "ADD URRGROUP", "ADD PCCPOLICYGRP"],
  "boundary_source": "agent"
}
```

### 2.4 核查标准（verify_split，代码实现）

| 维度 | 级别 | 检查内容 | 失败处理 |
|---|---|---|---|
| **完整性** | 硬约束 | 每份文档的所有命令都出现在且仅出现在一个 candidate 中 | 标记 fail，重跑 |
| **连续性** | 硬约束 | step_range 覆盖 [1, N] 无重叠无缺口 | 标记 fail，重跑 |
| **非空** | 硬约束 | 每个 candidate 至少有 1 条命令 | 标记 fail，重跑 |
| **对象族** | 软约束 | 一个 candidate 内最大对象族占比 ≥ 50% | 标记 warning，放行 |
| **收尾命令** | 软约束 | REFRESHSRV/LICENSESWITCH 不是 candidate 的唯一命令 | 标记 warning，放行 |
| **粒度** | 软约束 | candidate 命令数 ≤ 20 | 标记 warning，放行 |

**TDD 实现**：先写核查测试用例（包括正确样例 + 错误样例），再实现核查代码。

---

## 3. 代码聚类（cluster）

### 3.1 输入

`task_candidates.jsonl`（Agent-1 产出，~1500-2000 个 candidate）

### 3.2 算法

```python
# 1. 提取每个 candidate 的核心命令骨架（去掉 SET LICENSESWITCH / SET REFRESHSRV）
def core_commands(candidate):
    OPTIONAL = {"SET LICENSESWITCH", "SET REFRESHSRV", "MOD USERPROFILE"}
    return [c for c in candidate["commands"] if c not in OPTIONAL]

# 2. 按核心命令集的精确匹配聚类（第一轮）
# 同一组核心命令的 candidate → 同一簇
clusters = group_by(core_commands_frozenset, all_candidates)

# 3. 对大小为 1 的孤立簇，尝试与最近的簇合并（第二轮）
# Jaccard 相似度 > 0.8 → 合并
for singleton in singletons:
    best = find_most_similar(singleton, clusters, threshold=0.8)
    if best:
        merge(singleton, best)
```

### 3.3 输出

`task_clusters.jsonl`：
```json
{
  "cluster_id": "cluster-001",
  "core_commands": ["ADD RULE"],
  "member_count": 23,
  "members": [
    {"candidate_id": "GWFD-020301#003", "doc_path": "...", "feature_id": "...", "commands": ["ADD RULE"]},
    {"candidate_id": "GWFD-020351#002", "doc_path": "...", "feature_id": "...", "commands": ["ADD RULE"]},
    ...
  ]
}
```

### 3.4 核查

- 每个候选必须属于且仅属于一个簇
- 簇数合理（10-200 个之间，太多 = 欠合并，太少 = 过合并）

---

## 4. Agent-2：合并确证 + ConfigTask 字段（merge_fields）

### 4.1 输入（每簇 1 次）

```
簇信息：
  cluster_id: cluster-001
  core_commands: ["ADD RULE"]
  members: [23 个 candidate，来自不同文档]

每个 member 的信息：
  - candidate_id, doc_path, feature_id
  - step_range, candidate_desc, commands
  - 原文 md 路径（供 Agent 追溯）

命令图谱 notes（从 command_graph_dir/mml_commands.jsonl 提取）：
  ADD RULE 的 notes 原文
  ADD RULE 的 parameter_description 原文
```

### 4.2 Agent Prompt

```
你是 ConfigTask 合并 Agent。下面是一个 task 簇（{N} 个来自不同特性的配置案例），请确证合并并抽取字段。

【你的任务】
1. 确认这 {N} 个 candidate 是否真的是同一个 task？
   - 如果是 → 合并为 1 个 ConfigTask
   - 如果有明显不同（命令集差异大）→ 拆成 2 个 ConfigTask
2. 为合并后的 ConfigTask 填字段

【需填字段】
- task_logical_name：跨特性可复用的语义名（如"配置规则"）
- task_goal：一句话配置意图
- task_summary：一句话说明
- commands：有序命令列表，每个命令带参数列表
- 参数 binding_type：
  - fixed：跨所有案例都稳定不变（给 fixed_value）
  - variable：有变化（给 variable_source: identifier/site_data/enum_choice/peer_negotiated）
  - reference：值来自已有配置
  - 如果某参数在不同案例里取值不同 → 标 variable + variable_source=decision_driven（暗示有 DecisionPoint）

【参数来源说明】
- 命令图谱"数据来源"只有 3 值：本端规划/全网规划/对端规划（权威）
- "已配置数据中获取" → reference（不是 variable_source）
- 跨案例取值不同 → decision_driven（如 POLICYTYPE=PCC vs ADC）

【关键规则】
- 参数分类以"跨所有案例是否变化"为准，不只看单个案例
- commands 里包含该 task 的完整命令序列
- 命令图谱 notes 里的参数约束记录下来，留给 Agent-3 抽 TaskRule

【输出 JSON】
{
  "confirmed_tasks": [
    {
      "task_logical_name": "配置规则",
      "task_goal": "将费率与匹配条件绑定为策略规则",
      "task_summary": "把 FLOWFILTER + PCCPOLICYGRP 绑定为 RULE",
      "commands": [
        {"command_ref": "ADD RULE", "parameters": [
          {"parameter_ref": "RULENAME", "binding_type": "variable", "variable_source": "identifier"},
          {"parameter_ref": "POLICYTYPE", "binding_type": "variable", "variable_source": "decision_driven"},
          {"parameter_ref": "FILTERINGMODE", "binding_type": "fixed", "fixed_value": "FLOWFILTER"},
          ...
        ]}
      ]
    }
  ],
  "split_notes": ""  // 如果拆了，说明原因
}

【输入数据】
{簇信息 + candidate 列表 + 命令图谱 notes}
```

### 4.3 输出

`config_tasks.jsonl`：
```json
{
  "task_id": "UDG@20.15.2@ConfigTask@00001",
  "cluster_id": "cluster-001",
  "task_logical_name": "配置规则",
  "task_goal": "...",
  "task_summary": "...",
  "nf": "UDG", "version": "20.15.2",
  "commands": [...],
  "source_member_docs": ["doc_path1", "doc_path2", ...],
  "status": "active"
}
```

### 4.4 核查标准（verify_merge）

| 维度 | 级别 | 检查内容 |
|---|---|---|
| **命令覆盖** | 硬约束 | ConfigTask 的 commands 覆盖簇内所有 member 的核心命令 |
| **参数完整** | 硬约束 | 每条命令的参数列表非空（至少有标识参数）|
| **binding 覆盖** | 硬约束 | 每个参数都有 binding_type |
| **decision_driven 验证** | 软约束 | 标了 decision_driven 的参数，确实在不同 member 中有不同取值 |
| **task 数量** | 软约束 | 1 个簇通常产出 1 个 task；拆成 2+ 个需有 split_notes |

---

## 5. Agent-3：TaskRule + DecisionPoint（extract_rules）

### 5.1 输入（每簇 1 次）

```
ConfigTask 信息（Agent-2 产出）：
  task_logical_name, task_goal, commands + parameters

命令图谱 notes（权威约束源）：
  簇内每条命令的 notes 原文
  簇内每条命令的 parameter_description 原文

特性概述（可选，FeatureRule 参考）：
  簇内涉及的特性概述路径
```

### 5.2 Agent Prompt

```
你是 ConfigTask 规则抽取 Agent。下面是一个已确认的 ConfigTask + 命令图谱 notes，请抽取 TaskRule 和 DecisionPoint。

【TaskRule 抽取】
从命令图谱 notes + 参数描述中找"跨命令协同约束"：
- binding_rule：FLOWFILTER 必须绑定 filter 否则无效
- consistency_rule：URRGROUP 必须同时配在线+离线 URR
- conditional_param_rule：需计费→URRGROUPNAME 必填
- relative_value_rule：RULE 优先级相对约束
- 其他你发现的约束

只抽 task 内部、跨多条命令的约束。单命令语法不入 TaskRule。

【DecisionPoint 抽取】
分两类：
1. 文档内显式决策：在线/离线、IPv4/IPv6、主备等
2. 跨文档聚合决策：参数在不同案例里取值不同（如 POLICYTYPE=PCC/ADC/SMARTREDIRECT）

每个 DecisionPoint 输出 options[].impacts[]。

【输出 JSON】
{
  "task_rules": [
    {
      "rule_name": "FLOWFILTER 必须绑定 filter",
      "rule_type": "binding_rule",
      "rule_logic": "ADD FLOWFILTER 之后必须用 ADD FLTBINDFLOWF/ADD PROTBINDFLOWF 绑定过滤条件，否则 Rule 无效",
      "violation_effect": "Rule 无效配置",
      "severity": "critical"
    },
    ...
  ],
  "decision_points": [
    {
      "decision_name": "策略类型选择",
      "decision_question": "采用哪种策略类型？",
      "options": [
        {"option_name": "PCC", "impacts": [
          {"target_layer": "parameter", "target_ref": "POLICYTYPE", "effect_type": "sets_value_pattern", "effect_detail": "=PCC"}
        ]},
        {"option_name": "ADC", "impacts": [
          {"target_layer": "parameter", "target_ref": "POLICYTYPE", "effect_type": "sets_value_pattern", "effect_detail": "=ADC"}
        ]},
        ...
      ]
    },
    ...
  ]
}

【输入数据】
{ConfigTask JSON + 命令图谱 notes}
```

### 5.3 输出

`task_rules.jsonl` + `decision_points.jsonl`，每个 task_ref 指回 ConfigTask。

### 5.4 核查标准（verify_rules）

| 维度 | 级别 | 检查内容 |
|---|---|---|
| **规则来源** | 硬约束 | 每条 TaskRule 必须能在命令 notes 或参数描述中找到原文依据 |
| **DecisionPoint 覆盖** | 软约束 | Agent-2 标了 decision_driven 的参数，应该有对应的 DecisionPoint |
| **impacts 非空** | 硬约束 | 每个 option 至少有 1 个 impact |
| **severity 合法** | 硬约束 | severity ∈ {critical, warning, info} |

---

## 6. 组装（assemble）

代码步骤，合并 config_tasks + task_rules + decision_points → `assets/{nf}/{version}/` 下的最终 JSONL。

格式对齐 CONFIGTASK_SCHEMA.md：
- `config_tasks.full.jsonl`：ConfigTask 对象（含 commands + params）
- `task_rules.jsonl`：TaskRule 对象（task_ref 指向 ConfigTask）
- `decision_points.jsonl`：DecisionPoint 对象（owner_ref 指向 ConfigTask）

---

## 7. TDD 实现策略

### 7.1 核查代码先行（TDD）

每个 Agent step 之前，**先写核查代码 + 测试用例**：

```python
# tests/test_verify_split.py
def test_completeness_pass():
    """正确样例：所有命令都被覆盖"""
    doc_steps = {"commands": ["ADD URR", "ADD RULE"]}
    candidates = [{"commands": ["ADD URR"]}, {"commands": ["ADD RULE"]}]
    assert verify_completeness(doc_steps, candidates) == []

def test_completeness_fail_missing():
    """错误样例：遗漏命令"""
    doc_steps = {"commands": ["ADD URR", "ADD RULE", "ADD FILTER"]}
    candidates = [{"commands": ["ADD URR"]}, {"commands": ["ADD RULE"]}]  # 漏 FILTER
    errors = verify_completeness(doc_steps, candidates)
    assert len(errors) == 1
    assert "ADD FILTER" in errors[0]
```

### 7.2 验收基准

用已有的 `样例-内容计费@20.15.2-任务层实例.md` 作为 Agent-1 的验收基准：
- 内容计费应该拆出 5 个 candidate
- candidate 边界与样例一致（步骤 1-2 / 3-5 / 6 / 7-8 / 9-11）
- 命令列表与样例一致

### 7.3 批量执行 + 不遗漏

```python
# builder/agent/runner.py
def run_agent_step(ctx, step_name, agent_fn, verify_fn, input_docs):
    progress = load_progress(ctx, step_name)
    results = []
    
    todo = [d for d in input_docs if progress.get(d["id"]) != "ok"]
    for batch in chunks(todo, ctx["agent_batch_size"]):
        agent_output = agent_fn(batch)          # 调 Agent
        errors = verify_fn(batch, agent_output)  # 代码核查
        
        for doc, error in errors.items():
            if error:  # 硬约束失败
                progress[doc["id"]] = "fail"
                log.warning(f"{doc['id']}: {error}")
            else:
                progress[doc["id"]] = "ok"
                results.append(agent_output[doc["id"]])
        
        save_progress(ctx, step_name, progress)  # 每批保存进度
    
    # 断言不遗漏
    ok_count = sum(1 for v in progress.values() if v == "ok")
    fail_count = sum(1 for v in progress.values() if v == "fail")
    total = len(input_docs)
    
    if fail_count > 0:
        log.warning(f"{step_name}: {fail_count} 文档失败，下轮自动重试")
    if ok_count + fail_count < total:
        log.error(f"{step_name}: {total - ok_count - fail_count} 文档未处理（遗漏！）")
    
    return results
```

---

## 8. 实施顺序

| 阶段 | 内容 | 预计 Agent 调用 |
|---|---|---|
| Phase 1 | pipeline 结构 + scan/extract_steps 整合 + pipeline.yaml | 0（纯代码）|
| Phase 2 | verify_split 核查代码 + 测试（TDD） | 0（纯代码）|
| Phase 3 | Agent-1 prompt + runner，跑 5 份验证 | ~1 |
| Phase 4 | Agent-1 全量跑（655 文档 ÷ 5/批） | ~131 |
| Phase 5 | cluster 代码 | 0（纯代码）|
| Phase 6 | verify_merge 核查代码 + 测试 | 0（纯代码）|
| Phase 7 | Agent-2 prompt + runner，跑验证 | ~1 |
| Phase 8 | Agent-2 全量跑（~50-100 簇） | ~50-100 |
| Phase 9 | verify_rules + Agent-3 | ~50-100 |
| Phase 10 | assemble + 最终验收 | 0（纯代码）|

---

## 9. 与现有资产的关系

| 现有资产 | 在新 pipeline 中的角色 |
|---|---|
| `scripts/scan_corpus.py` | 迁移到 `builder/steps/scan.py` |
| `scripts/extract_steps.py` | 迁移到 `builder/steps/extract_steps.py` |
| `builder/core/md_reader.py` | 保留 |
| `builder/core/commands.py` | 保留 |
| `builder/constants.py` | 保留 |
| `data/corpus_manifest.csv` | Step 0 产出（已有）|
| `data/doc_steps.jsonl` | Step 1 产出（已有）|
| `CONFIGTASK_SCHEMA.md` | 字段定义参照 |
| `语料精读追踪.md` | 实证依据（参数分类/TaskRule/文档结构）|
| `样例-内容计费/IPSec` | Agent-1 验收基准 |
| `CommandGraph/data/assets/*/mml_commands.jsonl` | Agent-2/3 输入（命令 notes）|
