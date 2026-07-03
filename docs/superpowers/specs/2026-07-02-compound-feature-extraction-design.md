# compound / feature 层稳定抽取管线 — 设计文档 (spec)

> 日期:2026-07-02
> 状态:设计稿 v1(brainstorming 产出,待 spec-review + 人工评审 → writing-plans)
> 权威 schema:根目录 `改进后三层图谱定义.md` §4-§8
> 构建准则基:`ConfigTask/task-build-skill/SKILL.md` v2
> 前作:SKILL §5 step2 / §7.1(compound 抽取与合并判据)。本设计在其基础上补四件事:① per-DP-分支覆盖硬闸;② canonical compound 登记表;③ 事件驱动攒批人审;④ A/B 两段工作流。

---

## 1. 目标与非目标

### 1.1 目标
在 atom 层(命令 task + atom 挂 rule/DP)已审查锁定的前提下,为 **compound(步骤)** 与 **feature** 层建立一套 **人 + AI 协作、增量式、不丢命令** 的稳定抽取管线。解决现状痛点:"多数特性 feature→atom 一把梭、步骤未抽、跨特性复用未识别"(P1-REFACTOR-TRACKER:90 特性 = 17 STEP-OK / 58 ATOM-CHAIN / 13 SINGLE / 2 EMPTY,那 58 个直挂是主工作面)。

核心特性:
- **per-DP-分支覆盖不变量** 作硬闸,自动挡住"少抽 / 多抽 / 串命令"
- **特性逐个驱动 + 强制复用闸**(增量式)
- **复用签名双闸**(命令集 Jaccard + 相位/用途)挡住"同命令不同用途"误并
- **canonical compound 登记表** 作复用库 + 受控相位词表
- **事件驱动攒批人审**(不频繁,但不漏结构变更)
- **A/B 两段工作流**(特性内抽取 / 域级泛化 隔离)

### 1.2 非目标 (YAGNI)
- 不重建 atom 层(命令 task + atom 挂 rule/DP **保留不动**)
- 不动已合理的 17 STEP-OK(作复用库种子;**不重抽步骤,但参与演进连锁覆盖复审**)、13 SINGLE、2 EMPTY
- 不改权威 schema(5 类对象字段不变;`variable_source` 等已落 schema 字段沿用)
- 不引入新对象类型
- 本期仅 UDG(UNC 同法后续)

---

## 2. 边界规则

| 目录 | 权限 | 用途 |
|---|---|---|
| `ConfigTask/` | 可读写(工作目录) | Skill、资产、registry、review 队列 |
| 根 `改进后三层图谱定义.md` | 只读 | schema 权威 |
| `FeatureGraph/data/legacy/` | 只读 | 特性 → md 清单 |
| `CommandGraph/data/assets/` | 只读 | mml_commands 命令真相 |
| `output/…产品文档…/` | 只读 | 激活 md 真源 |

---

## 3. 工作面与前置

- **主工作面**:58 个 ATOM-CHAIN feature
- **复用库种子**:backbone `1-00001 计费三件套 / 1-00002 过滤链 / 1-00003 规则绑定 / 1-00004 收尾` + P1 现有 24 个 compound
- **前置数据卫生(开工前一次性)**:
  - 修复 12 个丢失 `task_layer` 字段的 atom 文件(`task-0-00109/110/149/150/153/154/155/156/174/175/177/199.yaml`——内容完整,仅缺 `task_layer: atom`,命令级审查 2026-07-02 重写时漏掉)。**注**:这 12 个是孤立末梢 atom(被 0 个 compound/feature 引用),修它们是 hygiene,不影响覆盖校验,只影响 index.json 完整性与 review-ui 可见性
  - 重建 `index.json`:atom 计数已正确(187),过期的是 **dp(39→80)/ rule(98→281)** 段

---

## 4. 硬不变量:per-DP-分支覆盖

### 4.1 定义
一个 feature F 的命令集**不是单一集合**,而是随其决策点分叉的**一族集合**(激活案例本身就有在线/离线/融合、URL/IMS/any 等多种配法,DP 经 `adds/skips/excludes/changes_command_set` 动态增删子 task)。

对 F 作用域内每一个合法 DP option 组合(每一个"配法变体" V):
> **`active_atoms(F, V) == md_required(F, V)`**

- `active_atoms(F, V)`:以 F 为根,沿 `contains/expands_to` 求 DAG 闭包得本特性全部 compound→atom(atom 被多 feature 共享不影响单 F 闭包),再按 V 的 DP impacts **target_type ∈ {task, command}** 者(无论 effect_type 字面值)增删后的命令集
  - **判定 key 在 target_type,不在 effect_type 名**:凡 impact 的 target 是 task/command 即视为该变体改命令集(实测 80 个 DP 中 `changes_command_set` 0 用例,真实分叉多用 `adds/excludes` + target=task/command 表达;`sets_value_pattern/sets_value` 等纯参数 impact 不算)
  - **容忍非标 effect_type**:存量数据有 `sets_value/sets_requiredness/requires_conditional/optional_enable/correlates/note` 等 schema 外值,脚本按 target_type 兜底分类,不报错
  - **环检测**:`contains/precedes` 边出现环视为数据 bug,覆盖脚本检测到环即报错回炉
- `md_required(F, V)`:F 的激活/部署 md 在该配法变体下要求的命令集(由步骤 ① 与分段同源抽出,属 Agent 推理产物,非 ground truth)

**任一变体不等 → 覆盖失败 → 回炉**。回炉路径含 ① 重核 md_required(覆盖失败可能因 md_required 抽错,非编排错)、②~④ 重抽。

### 4.2 变体枚举的界(防组合爆炸 + 防 A/B 段互扰)
- **影响命令集的 DP** = F 作用域内含 `target_type ∈ {task, command}` impact 的 DP(见 §4.1)。纯参数 impact(target=parameter)不参与枚举
- **例外**:`sets_value_pattern` 虽 target=parameter,若 md 明示该取值模式连带改变某命令的出现/缺失,则升级为枚举 DP
- **按 md 收口(关键)**:枚举这些 DP 的 option 笛卡尔积,**只保留 md 有对应示例的变体**(md_required(F,V) 非空)。md 无示例的组合不是 F 支持的变体,丢弃。这同时解决:A 段不被 B 段(作用域外)的 `selects_option` 约束——A 段按 F 自身 md 的变体集枚举;某 atom DP 跨多 feature 共享时,各 feature 按各自 md 支持的 option 子集枚举(如 2-00002 只 ONLINE、2-00001 全 3 种)
- **作用域内父子传播去重**:F 作用域内 `DP_parent selects_option DP_child` 时,DP_child 固定,不独立展开
- F 无影响命令集的 DP → 退化为单变体(扁平并集校验:Σ compound 命令集 ∪ 直挂 atom == md 全部命令)

### 4.3 作用域
A 段(特性抽取)只校验 **F 作用域内**(feature 及以下)的 DP。跨特性 DP(generalized / solution 层,如计费方式选特性)在 **B 段** 校验。

---

## 5. 层级职责与 DP 放置

- **feature 及以下** = 本特性**内部**(步骤取舍、参数取值分叉)
- **generalized 层(再拔高一层)** = **特性之间的关系**(选哪些 feature 组合、特性间顺序/互斥/依赖)
- **DP 放置默认往下**:本地分叉只要底层(命令参数)能 cover,就不上挂
- **语义同名(非字面同名)决策可在多层共存、不合并**:判定= `decision_question` 重合(可跨层)。用 `selects_option` 父子传播(父锁子,单向)串起。高层管"**选谁**"(如计费方式选特性)、底层管"**参数取什么值**"(如 ADD URR.USAGERPTMODE=ONLINE)——服务两种消费场景:纯意图**自顶向下**分解 / 只盯单命令**自底向上**

---

## 6. 两段工作流

### 6.1 A 段·特性抽取(主线)
逐个 ATOM-CHAIN feature,6 步(见 §7)。产出:该 feature 的 compound 编排 + feature 及以下 DP + 覆盖校验通过 + 事件入队。

### 6.2 B 段·域级泛化(本域特性都过完 A 段后)
- 建 generalized / solution task(样板:`4-00001` 计费配置):跨特性 `task_relations` + 特性选择型 DP(如 `0-00004` 计费方式)+ `selects_option` 向下传播链(链到 A 段建的 feature/atom DP)
- **域级覆盖校验(形式化在 writing-plans 阶段补全,本期 A 段先行)**:形状与 A 段对偶——`active_features(S, V)` = 以 generalized task S 为根沿 contains/expands_to 求闭包 + 跨特性 DP(target=feature/task)按变体 V 增删;`md_required(S, V)` = md 解决方案级示例要求的 feature 集(+ 传播下的关键参数锁)。断言 per 跨特性变体相等。本期只建 A 段 `check_feature_coverage.py`,B 段脚本后建

---

## 7. A 段·单特性抽取管线(6 步)

```
复用库 canonical compound 登记表 (1-00001~04 backbone + P1 现有24个 + 后续人审通过的新增)
                                                  │ 查
                                                  ▼
取一个 ATOM-CHAIN feature (激活 md = 真源)
① md 操作步骤分段 → 候选 compound 列表(每段 = 命令子集 + 相位角色)
② 每段过【复用签名闸】(命令集 Jaccard + 相位/用途 双闸,见 §8):
   • ≥0.75 且相位同义 → 复用;参数/配法分叉 → 加 DP option / 演进      [事件:复用/演进]
   • 0.4–0.75 或相位近义 → reference(新建,共享子 atom)              [事件:新建]
   • <0.4 或相位不同 → 独立新建                                     [事件:新建]
   • 候选 ≤2 命令 且 无复用命中 → 降级 feature→atom 直挂            [无事件]
③ 变体表达:md 有多种合法配法 → 挂 DP(能区分该分叉的最底层;A 段只挂 feature 及以下,见 §9)
④ 编排 feature 的 task_relations(compound contains/precedes/expands_to + 直挂 atom + DP 裁剪边)
⑤ 【per-DP-分支 覆盖校验·自动硬闸】(见 §4):不等 → 回炉 ②~④
⑥ 【事件分流】:纯复用→自动放行;新建→【待审·新建】;演进→【待审·变更】(高优先)
```

---

## 8. 复用签名闸

### 8.1 双闸签名
`match(C, X) = (Jaccard(cmdset(C), cmdset(X)) ≥ 阈值) ∧ (phase(C) 同义 phase(X))`
- `cmdset`:compound 的 atom 对应命令集合
- `phase`:compound 的"相位/用途角色"(逻辑阶段,如"费率→策略组绑定"),取自 canonical 登记表的 intent
- **两闸齐过才算复用命中;只命中一边不算**(挡"同命令不同用途"误并——正是 atom 层 ADD LOGICINF 被拆 4 份的同类坑的预防)

### 8.2 Jaccard 分档与动作
> **本节取代 SKILL §7.1 的 Jaccard 判据**(SKILL §7.1 同步改为引用本节双闸签名)。取值依据:旧 §7.1 单闸 0.7/0.3 → 本节双闸(加相位闸)后,命令集闸可收紧到 0.75/0.4(相位闸已挡"同命令不同用途",命令集闸不必再松)。**SKILL §7.1 "Jaccard 判据不适用 atom 层"的豁免保留**(atom 层一命令一 atom,只演进不合并)。

| Jaccard | 且相位 | 动作 | 事件 |
|---|---|---|---|
| ≥ 0.75 | 同义 | 复用 X;参数/配法分叉 → 加 DP option / 演进 X | 复用/演进 |
| 0.4–0.75 | 或近义 | reference:新建 C',共享子 atom,差异独立 | 新建 |
| < 0.4 | 或不同义 | 独立新建 C' | 新建 |
| 候选 ≤2 命令 且 无复用命中 | — | 降级 feature→atom 直挂 | 无事件 |

> 例:候选 `{URR, URRGROUP, PCCPOLICYGRP, URRFAILACTION}` vs `1-00001 {URR, URRGROUP, PCCPOLICYGRP}` → Jaccard = 3/4 = 0.75 + 相位同义 → **复用 1-00001 + 演进**(URRFAILACTION 作在线专属挂条件)。这正是 2-00002 在线计费该有的样子。

### 8.3 canonical compound 登记表
- 字段:`{compound_id, logical_name, phase(相位名), intent(一句话), command_set(atom 短 id 集 → 命令名集), domain}`
- 种子:现有 24 个 compound(backbone + P1),由 `build_index.py` 派生 + 人工补 phase
- 维护:**人审通过的新 compound 自动入表**
- 用途:② 复用检索(按 intent/phase 命中 → Jaccard 验命令集);同时作"受控相位词表"

### 8.4 Agent 证据表(供人审)
每个候选给 top-3 匹配:`{现有 compound, Jaccard, phase intent 比对, 参数差量, 推荐动作}`。**复用/合并人审拍板**;新建 Agent 可自决,但仍进待审队列。

---

## 9. DP 放置与变体表达
- 默认挂能 cover 该分叉的**最底层** task(atom 优先,其次 compound,其次 feature)
- 同一决策概念若同时驱动上层选择 → 在上层补同名 DP + `selects_option` 传播链(**不合并**)
- **A 段只挂 feature 及以下**;跨特性 DP 归 B 段

---

## 10. 人审机制(事件驱动·攒批)

### 10.1 不每 feature 审
按"对复用库的结构性变更"事件分流(对应"一个 feature 构建会引入新步骤 / 修改已有 / 复用已有"):
- **原样复用** → 自动放行(覆盖校验已把关)
- **新建 compound** → 【待审·新建】队列
- **演进已有 compound** → 【待审·变更】队列(高优先,爆炸半径——别的 feature 已在引用它)

### 10.2 攒批节奏
- 每个业务域(批次)收尾审一次
- 演进事件即时打标记,可攒到下次批审,但不漏
- 审什么:新建/合并/演进是否合理、签名判定与证据表是否扎实、覆盖校验是否真过

### 10.3 状态流转
覆盖 ✓ + 人审 ✓ → `active`;演进触发对引用方的连锁复审(SKILL §7.2)。

---

## 11. 稳定保证(为什么这套不会越做越乱)
1. **覆盖校验是硬闸**:抽错(缺/多/串命令)自动回炉,进不了 active
2. **复用库只进不乱**:新建/演进必经人审 + 双闸签名;原样复用自动但不改库
3. **status 流转 + 连锁复审**:演进触发引用方复审
4. **A/B 两段隔离**:单特性阶段绝不碰跨特性关系;跨特性关系只在 B 段、本域特性齐了之后做

---

## 12. 落地工件(供 writing-plans)

| 工件 | 类型 | 说明 |
|---|---|---|
| `task-build-skill/procedures/compound-extraction.md` | NEW | A 段 6 步流程细则(§7)+ 复用闸(§8)+ 覆盖(§4);SKILL §5 step2 引用 |
| `task-build-skill/SKILL.md` | MODIFY | §5/§7.1 指向新 procedure;§8.1 加 per-DP-分支覆盖为硬闸;§8 加事件驱动攒批人审 |
| `task-build-skill/scripts/check_feature_coverage.py` | NEW | 实现 §4:per-feature per-variant 集合相等校验,emit pass/fail + diff |
| `task-build-skill/scripts/build_index.py` | MODIFY | 现状已有 `by_command/by_feature/atom_usage` 段但无 compounds 段。加 `compounds` 段(compound_id → {logical_name, phase(从 logical_name 派生), intent, command_set(从 task_relations 解析 atom), features_using(反查 atom_usage)}) |
| `task-assets/UDG/20.15.2/canonical-compounds.md` | NEW | 人工可读登记表,种子 = 现有 24 个 compound |
| `task-assets/UDG/20.15.2/review/compound-review-queue-{domain}.md` | NEW | 每域待审事件队列 + 人审记录 |
| `task-build-skill/UDG-FULL-BUILD-RUNBOOK.md` | MODIFY | 加 A/B 两段 + 覆盖硬闸为强制步骤 |

---

## 13. 开放项(待 writing-plans 或人工定)
1. **Jaccard 阈值**(0.75 / 0.4)与"近义/同义"判据——Agent 判 + 人审,是否要 embedding 辅助?(默认:no,靠 intent 文本 + 人)
2. **canonical 登记表的 phase 字段**:人工补还是从 logical_name 派生?(默认:派生为主,人工校)
3. **B 段域级覆盖校验脚本**是否本期建?(默认:本期只建 A 段 `check_feature_coverage.py`;B 段 manual / 后建)
4. **演进连锁复审**(SKILL §7.2)的自动化程度?(默认:`check_feature_coverage.py` 对引用方自动重跑覆盖)

---

## 14. 验收判据
- 选 1 个 ATOM-CHAIN feature 跑通 A 段全 6 步(含覆盖校验通过 + 事件入队)
- 选 1 个已有 backbone 复用场景验证复用闸命中(如候选 ≈ 1-00001,Jaccard 0.75 + 相位同义 → 复用)
- **覆盖校验单测**(fixture 造错数据):故意少抽 1 命令 → 报"缺 {X}";故意多抽 1 命令 → 报"多 {Y}";含环 → 报"环,回炉"
- **演进连锁复审**:演进 1-00001 后,引用它的 2-00002/2-00003 等覆盖校验自动重跑,状态正确回 `inferred`
- 人审队列正确分流 new / evolve / reuse
- 前置数据卫生:12 个 atom 恢复 task_layer;index.json 重建后 **dp=80 / rule=281 / atom=187(已正确,保持)**
