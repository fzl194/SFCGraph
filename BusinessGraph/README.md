# BusinessGraph · 业务层 YAML 资产

把 `business-graph/{计费,带宽控制,访问限制}场景/three-layer-graph/01-business-graph.md`
里的**业务层对象**（业务域 / 场景 / 方案 + 嵌套决策点）抽成 ConfigTask 风格的 YAML：
**一个 yaml = 一个对象，关系承载在字段里**。

源数据三场景共享同一根对象「业务感知」，故业务域统一为一个对象。

## 目录结构

```
BusinessGraph/
├── README.md                         # 本文件
├── scripts/
│   └── gen_from_business_graph.py    # 生成器（改源 md 后重跑）
├── business_domains/
│   └── bd-business-awareness.yaml    # 业务域（业务感知，三场景共享）
└── scenarios/
    ├── charging/                     # 计费场景
    │   ├── ns-charging.yaml          # 场景（NS-CH-01，嵌 5 个场景级 DP）
    │   └── solutions/                # 7 个方案
    │       ├── cs-ch-01-offline.yaml
    │   ...
    ├── bandwidth/                    # 带宽控制场景（NS-BW-01 + 7 方案）
    └── access-control/               # 访问限制场景（NS-AC-01 + 9 方案，含 CS-AC-02 头增强）
```

共 **27 个 yaml**：1 BD + 3 NS + 23 CS（计费 7 + 带宽 7 + 访问限制 9）。

## 对象 Schema

### BusinessDomain（`business_domains/`）
| 字段 | 说明 |
|---|---|
| `domain_id` | 统一 ID `BD-BSA-01` |
| `domain_name` / `domain_summary` | 业务感知 / 域概述 |
| `alias_ids` | 源数据三场景各自的 BD ID（BD-CH-01 / BD-BW-01 / BD-AC-01） |
| `contains_scenarios` | 挂在域下的场景 ID 列表 |
| `source_evidence_ids` | 证据 |

### NetworkScenario（`scenarios/<dir>/ns-*.yaml`）
| 字段 | 说明 |
|---|---|
| `scenario_id` / `scenario_name` | NS-CH-01 等 |
| `belongs_to_domain` | 反指 BD |
| `scenario_summary` / `judgment_basis` / `typical_outcome` | 场景三件 |
| `coverage` / `non_coverage` | 场景边界（覆盖维度 / 相邻场景） |
| `contains_solutions` | 包含的方案 ID 列表 |
| `decision_points` | **嵌套**：场景级决策点（见下） |

### ConfigurationSolution（`scenarios/<dir>/solutions/cs-*.yaml`）
| 字段 | 说明 |
|---|---|
| `solution_id` / `solution_name` | CS-CH-01 等 |
| `belongs_to_scenario` | 反指 NS |
| `solution_summary` / `design_intent` / `core_mechanism_combo` | 方案三件 |
| `scopes` | 作用粒度（subscriber / subscription / service_selection …） |
| `participants` | 参与方（name / role / layer=user_plane\|control_plane\|external_system） |
| `uses_feature` | 引用的特性 ID（仅 ID，不展开——特性已有 jsonl 结构化字段） |
| `selected_by_decision` | 反指选出本方案的 DP ID 列表 |
| `decision_points` | **嵌套**：单 CS 独占的决策点（如有） |
| `applies_decision_refs` | 影响本 CS 但嵌在别处（NS）的 DP ID 列表 |

### DecisionPoint（**不单独建 yaml**，嵌套在 NS 或 CS 里）
| 字段 | 说明 |
|---|---|
| `decision_id` / `decision_name` / `decision_question` | 决策三件 |
| `trigger_condition` / `option_set` | 触发条件 / 选项列表 |
| `impact_summary` | 影响摘要 |
| `selects_solutions` | 该 DP 选出哪些 CS（仅 NS 级 DP 带） |
| `owner_solutions` | 该 DP 还影响哪些 CS（仅 NS 级 DP 带） |

## 决策点（DP）落位规则

源数据里 DP 归属有两个信号且不一致：DP 表 `owner_ref` 全是场景级，关系边 `has_decision`
却显示很多 DP 挂在具体方案下。**以 `has_decision` 边为权威**，规则：

- 单 CS 独占且无 NS 归属 → 全量嵌在该 **CS** yaml
- 多 CS 共享 / NS 归属 / NS-CS 冲突 → 全量嵌在 **NS** yaml，CS 侧用 `applies_decision_refs` 回指

每个 DP 全量只出现一次（已校验：24 个 DP = 8×3，无重复）。

| 场景 | NS 下嵌套 | CS 下嵌套 |
|---|---|---|
| 计费 | DP-CH-01,02,04,05,07（5） | CS-CH-03←DP-08 · CS-CH-04←DP-03 · CS-CH-05←DP-06 |
| 带宽 | DP-BW-01,04,07,08（4） | CS-BW-01←DP-02,05 · CS-BW-02←DP-03,06 |
| 访问限制 | DP-AC-01,03,04,05,06,07,08（7） | CS-AC-01←DP-02 |

## 有意不输出

按需求，以下源对象**不**生成（业务层只保留 BD/NS/CS）：
- `BusinessRule`（BR）—— CS 不带 `constrained_by`
- `SemanticObject`（SO）—— CS 不带 `uses_semantic_object`
- Feature 不向下展开（仅 `uses_feature` 引用 ID）

## 重新生成

源 md 更新后：

```bash
python BusinessGraph/scripts/gen_from_business_graph.py
```

CS 文件名英文 slug 在 `CS_SLUGS` 字典维护；新增 CS 时补一条即可，缺失则回退纯 ID 命名。
