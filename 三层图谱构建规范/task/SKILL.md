---
name: task-layer-build
description: 把命令层+特性层资产构建成 task 层资产（atom/compound/feature_task）。Procedure 体裁：agent 读已构建的命令/特性资产+原始文档，理解后梳理出"动态配置方法"，自己写 md。命令/特性层承载静态知识（原文 verbatim），task 层承载动态配置方法。
sop_version: 0.1.0
---

# Task 层构建 SKILL

> task 层在命令层、特性层之上，把"静态知识"转化为"动态配置方法"。
> **体裁：Procedure**——agent 理解输入自己写 md（命令/特性层是 Spec，代码构建）。
> **静态/动态拆分（本层存在的根因）**：一条命令既有命令层 md（静态：功能/参数表/规格/notes，原文 verbatim），又有 atom md（动态：这条命令有哪些合法配置方法、配置生成时怎么选）。task 层不重复静态知识，承载动态配置方法。

## 三类对象总览

| 对象 | Type | 存储 | ref 指向 | 回答 | 状态 |
|---|---|---|---|---|---|
| atom | `AtomTask` | `AtomTask/{nf}/{ver}/` | `MMLCommand` | 这条命令有哪些配置方法（配置方法字典） | ✅ 本 SOP |
| compound | `CompoundTask` | `CompoundTask/{nf}/{ver}/` | `null` | 这个多命令步骤怎么配（可复用模块） | ✅ 本 SOP |
| feature_task | `FeatureTask` | `FeatureTask/{nf}/{ver}/` | `Feature` | 这个特性怎么配（编排+DP） | ✅ 本 SOP |

**统一约定**（同命令/特性层）：资产 = YAML(最小抽取) + 正文 + `## 边`；ID 三段 `{nf}@{Type}@{local}`，文件名=ID，version 只在 YAML+路径；引用 `[[{nf}@{Type}@{local}]]` 双方括号，**引用粒度 = md 级（一个逻辑ID = 一个 md，无 md 内部章节锚）**——故 DP/约束不编号；无证据段。

## 边的规定（task 层全局）

Task 的 `## 边` **只允许指向以下四类对象**：

- **命令**（`MMLCommand`）—— atom 对应命令
- **特性**（`Feature`）—— feature_task 对应特性
- **Task**（atom/compound/feature_task 之间）—— Task↔Task 引用（compound/feature_task 阶段建立）
- **业务方案**（`ConfigurationSolution`）—— 上层方案引用 Task

**禁止**：Task 不直接关联 `ConfigObject` / `License` / `CommandParameter` 等命令层/特性层内部对象——那些静态结构在各自层内，Task 通过"命令/特性"间接关联（静态/动态拆分）。

> atom 阶段：边只有 `对应命令`（命令）。Task↔Task、Task↔特性、Task↔方案 在 compound/feature_task 阶段才建立。

## 构建顺序（整层）

```
1. atom 全建（所有命令，分批次）
2. 逐批次：feature_task + compound_task 同步构建（per 特性）
```

atom 是最底层，必须先全建。compound/feature 在 atom 之上，按特性批次同步（compound 是 feature 构建时"多命令反复出现"聚合出来的）。

---

# Part A · atom 构建

## A.1 定位（静态/动态拆分）

- 命令层 md（`Command/.../{nf}@MMLCommand@{命令}.md`）= **静态知识**：功能、参数真相表、规格、notes，原始手册 verbatim。
- atom md = **动态配置方法**：这条命令有哪些合法配置方法（配置维度 + 各取值 + 作用）、配置生成时怎么选。
- atom **不重复静态知识**：引子链命令层，参数真相表/规格不抄进来；通过**理解命令层 md 梳理出**动态配置信息。
- 一条命令一个 atom（1:1），atom ID 用命令名做锚（弃编号）。

## A.2 范围与批次

**所有命令都建 atom**，结构一致（配置方法字典 + 决策点 + 约束 + 边，该有的都要）。
按"特性资产里是否有该命令的配置示例"分两类——**只影响输入源，不影响 atom 的结构要求**：

| 类别 | 输入 | 配置方法字典梳理依据 | 批次 |
|---|---|---|---|
| 有特性配置示例 | 命令层md + 特性资产配置示例（代码汇总）+ 命令原文 | 参数表/notes + 真实配置范式（数据规划取值/场景佐证） | 第一批 |
| 无特性配置示例 | 命令层md | 参数表/notes/使用实例——agent 读命令层 md **理解后梳理** | 后续批 |

> 两类都要完整的 **配置方法字典 + DP + 约束**（从命令层 notes/参数梳理）。
> **无特性配置示例的命令不是"精简/引用实例"**，而是 agent 直接读命令层 md 理解后，梳理出同样完整的配置信息。DP 和约束该有就有（用法单一则 DP 显式说明"无分支"）。

## A.3 输入

**前置依赖**：Command 层 + Feature 层已构建。

| 输入 | 来源 | 用途 | 适用 |
|---|---|---|---|
| 命令真相（功能/参数表/规格/notes） | `三层图谱资产/Command/{nf}/{ver}/{nf}@MMLCommand@{命令}.md` | 静态知识源（引子链 + 配置方法/约束梳理源） | ✅ 所有 atom |
| 命令配置示例（数据规划行/任务脚本/操作步骤） | `三层图谱资产/Feature/{nf}/{ver}/{nf}@Feature@{code}/*.md` | 配置方法字典佐证 + DP 派生 | ⬠ 仅第一批 |
| 命令原始产品文档 | 产品文档归档 | 资产原文被汇总截断时回查核对 | 可选 |

## A.4 输出

`三层图谱资产/AtomTask/{nf}/{ver}/{nf}@AtomTask@{命令}.md`（每命令一个，文件名=完整ID）

## A.5 构建流程

### 第一步·代码筛选整合（仅"有特性配置示例"的命令）

脚本 `task/scripts/collect_command_examples.py`，输入源 = 已构建资产（非原始文档树）：

```
输入：三层图谱资产/Command + 三层图谱资产/Feature
扫 Feature 资产所有 md，按命令名命中判定（任一即记入该特性）：
  (a) 操作步骤 "**{命令}**" 粗体引用
  (b) 数据规划表行 | {命令} | 参数 | 取值 | 说明 |
  (c) 任务示例脚本 {命令}:...; 或 {命令} ...;
  (d) 段落 "通过**{命令}**" 弱信号（补充）
每命中特性提取：数据规划行 + 任务脚本 + 操作步骤上下文(±2行)
+ 提取 Command 资产的命令真相/参数表/notes
+ 派生：配置方法差异汇总（每参数取值分布）
输出（中间态·非资产）：三层图谱资产/_intermediates/atom-input/{nf}/{ver}/{命令}.md
```

中间态是 agent 工作底稿（命令真相 + 各特性配置范式 + 差异），**不进 atom md**（atom 无证据），git ignore。

### 第二步·agent 理解梳理（所有命令 · Procedure 核心）

agent 读：命令层 md（必有）+ 第一步中间态（若有）。

- **配置方法字典**：理解命令功能/参数表，梳理配置维度（每参数的枚举/取值域 = 一种配置方法），列取值+作用；有配置示例的用真实场景佐证
- **决策点（DP）**：从配置维度派生选择点（多配置方法时必建 DP，每个 option 影响全记；命令用法单一则显式说明"本命令无分支"）
- **约束（rule）**：从 notes 梳理（规格上限/生效时延/唯一性/互斥等），编号化

### 第三步·写 atom md

按 [template/atom.md.tpl](template/atom.md.tpl)，字段见 [字段定义](字段定义.md)。

## A.6 规范要点

- YAML 8 字段（id/type/name/name_zh/nf/version/ref/status）
- 正文：`# {配置动作名}（{命令}）` + 引子（链命令层）+ `## 配置方法`(字典) + `## 决策点` + `## 约束`
- `## 边`：只 `- 对应命令: [[{nf}@MMLCommand@{命令}]]`（单向；静态信息如操作对象在命令层，不重复）
- **无证据**：不写 source_evidence_ids、不写 `## 证据` 段
- 引用统一 `[[逻辑ID]]`
- 配置方法字典讲"命令有哪些合法配置方法"，**不逐特性罗列取值**（逐特性是 feature_task 的事）
- **决策点/约束该有都有**（无论命令是否有配置示例；无分支/无约束则显式说明）；DP/约束**不编号**（引用只到 md 级，无章节锚）

## A.7 规范引用

- 字段：[字段定义](字段定义.md) · 骨架：[template/atom.md.tpl](template/atom.md.tpl)
- 核查：[check.md](check.md)
- 命名/ID/存储统一约定：同命令/特性层（见顶层 [conventions/命名规范-建议](../conventions/命名规范-建议.md)）

## A.8 核查（构建后必做）

产出交 [check.md](check.md)：字段必填 / ID 三段 / 文件名=ID / 正文5段 / 边只有对应命令且引用真实命令 / 无证据段残留 / 配置方法字典非逐特性罗列 / DP 与约束齐（无则显式说明）。

---

# Part B · compound + feature_task 一并构建

## B.0 一并构建总览

compound 和 feature_task **必须一并构建**，构建单元 = **特性**（不是命令，也不能分两次）。理由：① compound 的边界由 feature_task 的步骤拆分决定，无法预枚举；② feature_task 配置流程直接引用 compound，必须同时存在；③ compound 复用库（`_index`）逐特性增量积累。

构建顺序两级：
```
第 1 级：atom 全建（单元=命令，前置，Part A）
第 2 级：compound + feature_task 一并构建（单元=特性，本 Part）
```

每构建一个特性 = 一个完整 pass（拆步骤 → 建/复用 compound → 迭代步骤合理性 → 成文）。

### 输入（前置：atom 层全建 ✓ + 特性层已建 ✓）

| 输入 | 来源 | 用途 |
|---|---|---|
| 特性静态知识（操作步骤/数据规划表/任务脚本） | `Feature/{nf}/{ver}/{nf}@Feature@{code}/*.md` | feature_task 配置流程依据 |
| atom 配置方法字典 | `AtomTask/{nf}/{ver}/{nf}@AtomTask@{cmd}.md`（本特性涉及的命令，已全建） | feature 引用 atom / compound 组成 atom |
| compound 复用库 | `CompoundTask/{nf}/{ver}/_index.md` | compound 复用判定（Jaccard） |
| 命令原始产品文档 | 产品文档归档 | 特性资产原文不足时回查 |

### 输出（一个特性 pass）

| 输出 | 路径 | 数量 |
|---|---|---|
| feature_task md | `FeatureTask/{nf}/{ver}/{nf}@FeatureTask@{code}.md` | 1/特性 |
| compound md（新建） | `CompoundTask/{nf}/{ver}/{nf}@CompoundTask@{英文名}.md` | 0~N/特性 |
| `_index` 更新 | `CompoundTask/{nf}/{ver}/_index.md` | 新 compound 入库 + 复用 compound 引用计数 +1 |

## B.1 compound 对象规范

- Type `CompoundTask`，ID `{nf}@CompoundTask@{英文名}`（英文名 Agent 取，kebab-case，稳定不变）
- ref: **null**（compound 无上层对象）
- YAML：`id/type/name/name_zh/nf/version/command_set/status`
  - `command_set`：命令名列表（如 `["ADD URR","ADD URRGROUP","ADD PCCPOLICYGRP"]`），**复用判定 + 快速查询的核心字段**
- 正文：`# {中文名}` + 引子(定位+被引用于) + `## 配置方法`(单表格:步骤/命令/关键参数 + 典型脚本 + 步骤位置) + `## 场景差异`(每引用方一行) + `## 决策点` + `## 约束` + `## 边`
- 边：`组成 → [[atom...]]`（compound→atom）；`被引用于 → [[feature_task...]]`（反向，逐特性回填）；可选 上游/下游 compound
- compound 不重复 atom 的命令配置方法（atom 讲命令怎么配，compound 讲多命令怎么组装成步骤）

## B.2 feature_task 对象规范

- Type `FeatureTask`，ID `{nf}@FeatureTask@{feature_code}`（1:1 特性）
- ref → `{nf}@Feature@{feature_code}`（静态/动态拆分：Feature 层=静态知识，feature_task=动态配置编排，同构 atom→command）
- YAML：`id/type/name/name_zh/nf/version/ref/status`
- 正文：`# {特性名}（{code}）` + 引子(链特性层) + `## 配置概览`(对象链+场景骨架) + `## 配置流程`(步骤+单命令混合编排) + `## 决策点` + `## 约束` + `## 边`
- 配置流程形态（**混合编排**，步骤≥2命令→compound，单命令→直接 atom）：
  ```
  1. **步骤A**（一句话）：`CMD1` + `CMD2` → [[UDG@CompoundTask@step-a]]
     - 关键参数：P1=<值>
  2. **命令B**（一句话）：`CMDB` → [[UDG@AtomTask@command-b]]
     - 关键参数：P3=<值>
  ```
- 边：`对应特性 → [[UDG@Feature@{code}]]`；`编排 → [[compound/atom...]]`

## B.3 逐特性构建流程（pass）

```
1. 读特性资产 + 该特性涉及的 atom（查 AtomTask 文件存在）
2. 理解特性配置流程（以特性资产「操作步骤」章节为准）
3. 拆 步骤 + 单命令：
   - ≥2 命令 + 高频/经典/可复用 → compound 候选
     · 查 _index 复用库：command_set 签名 + Jaccard 判定 → 复用 / reference / 新建
     · 新建：Agent 取英文名，写 compound md（command_set 必填）
   - 单命令 → 直接引 atom（合法，非例外）
4. 迭代步骤合理性（多次审视，§B.5 硬规则）：防平铺 / 重复识别 / 防假通用
5. 写 feature_task md（配置流程=步骤+单命令混合）+ compound md（新建）
6. 更新 _index（新 compound 入库 + 复用 compound 引用计数）
```

## B.4 compound 复用机制

**复用层级**：全通用（跨一切特性：License前置/刷新生效）/ 域通用（业务域内多特性：过滤链/计费三件套/BWM控制器族）/ 特性专属（单特性）

**复用判定**（建 compound 前必查 `_index`，按 command_set 算 Jaccard）：
- 命令集 Jaccard ≥ 0.75 **且** 相位同义 → **复用**（feature 编排引已有 compound，不新建）
- 0.4–0.75 或相位近义 → **reference**（新建但共享子 atom）
- < 0.4 或相位不同 → **新建**

**compound 归属**：被多 feature 引用是常态，`被引用于` 列引用方 feature_task（逐特性回填）。

## B.5 迭代硬规则

- **防平铺**：feature_task 配置流程连续 ≥3 atom 无 compound → 强制评估抽 compound
- **重复识别**：≥3 命令阶段内聚 + 本族 ≥2 特性共用 → 必须抽 compound
- **防假通用（R1.2）**：复用 compound 时，本 feature 引入的差异（参数变种/专属命令/组装方式/约束）必须**双向回填**到 compound「场景差异」，不能只写进 feature DP
- **族通用 compound 命令多带陷阱**：族通用 compound 命令集是族内并集，个别 feature 只用子集 → compound「场景差异」**逐 feature 列命令子集**（执行/省略），不并集泛化；feature 编排时对省略段加脚注

## B.6 规范要点（compound + feature_task 共用）

- **调测剥离**：配置流程/配置方法只含配置类命令（`ADD/MOD/SET/DEL/RMV/LOD/STR持久化`），调测/查询/导出（`DSP/LST/EXP/STP/STR探测`）不入
- **DP 规范**：多配置方法差异用 DP 组织（不建多套流程），每 option 影响全记；多 DP 按差异独立轴（≥2 轴才分表）；DP/约束**不编号**（md 级引用）
- **无证据**：不写 source/source_evidence_ids、不写 `## 证据`；配置流程参数依据 = atom 配置方法字典（feature 只能从 atom 字典选合法取值，check 校验参数在 atom 内）
- **能力型底座特性**：无命令的被动响应特性（如会话管理），建骨架 feature_task（status=`foundation` + 配置概览说明"本特性无独立配置，靠被依赖特性"）+ 指向被依赖特性的 compound；不建配置流程
- **族内构建顺序**：族内多特性先建最复杂（差异最全），通用 compound 场景差异一次补齐，后续简单特性复用
