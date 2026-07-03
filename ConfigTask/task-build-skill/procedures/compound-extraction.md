# compound / feature 层抽取流程(A 段)— Agent 操作手册

> 依据:`docs/superpowers/specs/2026-07-02-compound-feature-extraction-design.md`;SKILL.md §5 step2 / §7.1 / §8 指向此处。
> **触发**:重建一个 feature 的 compound/feature 层(feature task `2-XXXXX`)。
> **硬边界**:atom 层(命令 task + atom 挂 rule/DP)**冻结,只读不改**。本流程只动 compound / feature task 及其挂载的 rule/DP。
> **形态**:feature 重建 = 参照现有结构按本流程校准/演进,**不是推翻**。

---

## 0. 输入(每个 feature)

| 输入 | 来源 |
|---|---|
| 该 feature 的**全部** md | `feature-graph/data/UDG_feature_files.csv` 按 feature_id 过滤(主配置/参考信息/数据规划/实现原理/部署 UPF) |
| 涉及命令的 mml 真相 | `CommandGraph/data/assets/UDG/20.15.2/mml_commands.jsonl`(parameter_description / notes) |
| 现有该 feature 的 task | `task-assets/UDG/20.15.2/tasks/task-2-XXXXX.yaml` + 其引用的 compound + atom |
| canonical 复用登记表 | `task-assets/UDG/20.15.2/canonical-compounds.md`(复用查找;重跑 build_index.py 刷新) |
| 现有 feature挂/compound挂 rule·DP | `task_rules/` + `decision_points/`(owner_task_ref 命中) |

> **必读全特性 md**:一个 feature 含 3~11 个 md(主配置/参考信息/数据规划/实现原理/部署),都必须读,不能只读主配置。

---

## 1. 步骤① md 操作步骤分段

读全部 md,聚焦主配置 md 的「操作步骤」+「数据规划表(获取方法列)」。按 md 操作步骤的自然分段 → **候选 compound 列表**,每段记录:
- `命令子集`(该步骤涉及的命令)
- `相位角色`(从步骤标题/语义归纳,如"费率→策略组绑定""过滤条件组装""收尾刷新")

**单命令步骤不成为候选**(直接进 ④ feature→atom 直挂)。

---

## 2. 步骤② 复用签名闸(双闸)

对每个候选 compound C(命令集 `cmdset_C`、相位 `phase_C`):

1. 查 `canonical-compounds.md`,按 **intent/phase 检索同义** compound X(backbone 1-00001~04 优先)
2. 算 `Jaccard(cmdset_C, command_set_X) = |交集| / |并集|`
3. 分档(spec §8.2):

| Jaccard | 且相位 | 动作 | 事件 |
|---|---|---|---|
| ≥ 0.75 | 同义 | **复用** X;C 的差异(多出的命令/参数分叉)→ 挂 DP option 或演进 X | 复用/演进 |
| 0.4–0.75 | 或近义 | **reference**:新建 C',共享子 atom,差异独立 | 新建 |
| < 0.4 | 或不同义 | **独立新建** C' | 新建 |
| 候选 ≤2 命令 且 无命中 | — | **降级** feature→atom 直挂 | 无事件 |

4. 产 **top-3 证据表**(供人审):`{现有 compound, Jaccard, phase intent 比对, 参数/命令差量, 推荐动作}`

> **双闸,缺一不算**:Jaccard 达标 **且** 相位同义 才复用。"同命令不同用途"(如 ADD APN 接入 vs 速率控制)靠相位闸挡掉。

---

## 3. 步骤③ 变体表达(DP 放置)

md 示例有多种合法配法(计费方式 在线/离线/融合;过滤模式 URL/IMS/any;ADC 双路径…)→ 挂 DecisionPoint:

- **挂在能区分该分叉的最底层**(atom 优先 → compound → feature)
- **A 段只挂 feature 及以下**;跨特性 DP(如计费方式选特性)归 B 段 generalized
- **语义同名决策**(decision_question 重合)若已在上层(generalized)有 → 用 `selects_option` 父子传播链串起(**不合并**);本特性内部只需挂最底层那个

---

## 4. 步骤④ 编排 task_relations

- 建复用 compound 的 `contains / precedes / expands_to`(compound→atom,compound→compound 编排序)
- `feature → atom` 直挂边(单命令步骤或降级段)
- DP 裁剪的条件关系:`condition_ref` 指向对应 DP

---

## 5. 步骤⑤ per-DP-分支覆盖校验(硬闸)

1. 写 `review/{feature_id}-variants.yaml`——列出 **md 证实的每个变体** + 其 `dp_options` + `md_required_commands`(从 md 各场景示例/步骤抽):

```yaml
feature_task_id: UDG@20.15.2@Task@2-XXXXX
feature_id: GWFD-XXXXX
md_source_files:
  - 配置XXX_<hash>.md
variants:
  - name: 基础(无特定计费方式)
    dp_options: {}                     # 无 DP 分支时空
    md_required_commands: [ADD URR, ADD URRGROUP, ADD PCCPOLICYGRP]
  - name: 在线计费
    dp_options: {0-00001: opt-online}  # dp_short → option_id
    md_required_commands: [ADD URR, ..., ADD URRFAILACTION]
```

2. 跑:`python task-build-skill/scripts/check_feature_coverage.py <feature_task_short 如 2-00001>`
3. **不等 → 回炉**:报"缺 X"→ 编排漏(②~④ 重抽);报"多 Y"→ 编排塞了 md 没有的;也可能 ① 的 md_required 抽错(重核)。

> 覆盖校验是硬闸:过不了不进 ⑥、不进 active。它兜住"10 条命令抽 3 步、并集 ≠ 10"。

---

## 6. 步骤⑥ 事件分流(人审攒批)

把本 feature 触发的"复用库结构变更"写入 `review/compound-review-queue-{业务域}.md`:

- **纯复用 as-is** → 自动放行(覆盖已把关),不入队
- **新建 compound** → 【待审·新建】(附 top-3 证据表 + intent + command_set)
- **演进已有 compound** → 【待审·变更】(标影响哪些 feature——爆炸半径)

人审攒批:每个业务域批收尾审一次;演进优先。

---

## 7. co-build rule / DP(别忘了)

- **feature 级**:feature 挂 rule(`consistency_rule` / `dependency_rule`)+ DP(特性级选择,如计费方式)
- **compound 级**(若新建/演进):compound 挂 rule(`cardinality_rule` / `uniqueness_rule` / `consistency_rule`)
- **atom 层 rule/DP 只读**(命令级审查已闭环),不改

rule_type 用 SKILL §5 的 12 canonical 值;DP impacts 的 `target_type` 决定是否影响命令集(覆盖校验据此算)。

---

## 8. 收尾(每个 feature)

- 写 `review/{feature_id}-pass-{N}.md`:`## 自审发现 / ## 改动记录 / ## 复用判定证据 / ## 缺口`
- **不动** atom task / atom 挂 rule / atom 挂 dp
- 新建/改动的 compound/feature/feature挂rule·DP / compound挂rule·DP → status = `inferred`(等人审 → active)

---

## 边界与禁忌

- atom 层冻结(命令 task / atom 挂 rule / atom 挂 DP 只读)
- A 段不碰跨特性关系(generalized / solution 归 B 段,本域特性齐了再做)
- feature 重建 = 参照现有校准/演进,不推翻已有的合理结构
- 覆盖校验过不了,绝不放行
