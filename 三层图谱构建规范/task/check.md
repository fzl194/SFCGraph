# Task 层核查（check）

> task 层产出的独立质量审查。**只审不建**，与 @Task构建师分离。

## 审查角色纪律

- **怀疑主义**：只认证据，默认产物有问题
- 问题必须可定位（对象 ID + 规则）
- 区分"产物问题"（回构建师返工）和"SKILL 缺口"（提 change-request）

## 审查输入

- task 层构建产物（atom md）
- [字段定义](字段定义.md)（字段权威）
- 命令层资产（核 `ref` 真实性）

## 审查输出

核查报告：`{通过/不通过, 问题清单[{对象, 问题类型, 严重级, 归属}]}`

## 审查项（atom）

| 类别 | 检查点 |
|---|---|
| 字段必填 | `id/type/name/name_zh/nf/version/ref/status` 不空 |
| ID 格式 | 三段 `{nf}@AtomTask@{命令名}`（命令名做锚、无编号；local 保留空格；不含 version） |
| 文件名 ↔ ID | 文件名 = 完整 ID（`UDG@AtomTask@ADD URR.md`） |
| ref 真实 | `ref` 指向的命令层对象存在（`Command/{nf}/{ver}/{nf}@MMLCommand@{命令}.md`） |
| 结构统一 | 每资产 = YAML + 正文 + `## 边`；关系只在 `## 边`，正文不重复 |
| 正文 5 段 | `# 标题` + 引子(链命令层) + `## 配置方法` + `## 决策点` + `## 约束` |
| 静态不重复 | 参数真相表 / 规格 / 命令功能 **不抄进 atom**（引命令层）；atom 只讲动态配置方法 |
| 配置方法字典 | 讲"命令有哪些合法配置方法"（维度+取值+作用），**不逐特性罗列取值** |
| DP / 约束齐 | DP 每个 option 影响全记；**DP/约束不编号**（引用只到 md 级）；无分支 / 无约束**显式说明**（不能空着） |
| **边的规定** | `## 边` 只指向 命令/特性/Task/方案；**atom 阶段只有 `对应命令`**；**禁止指向 ConfigObject/License/CommandParameter** |
| 无证据 | 无 `source` / `source_evidence_ids`、无 `## 证据` 段残留 |
| 引用形式 | 全部 `[[{nf}@{Type}@{local}]]` 双方括号（**非** markdown 相对路径）；**引用只到 md 级，无 `#章节` 锚点** |

## 交接

- 通过 → 收口
- 不通过 + 产物问题 → 回 **@Task构建师** 返工
- 不通过 + SKILL 缺口 → 提本层 `change-requests/`

---

## 审查项（compound）

| 类别 | 检查点 |
|---|---|
| 字段必填 | `id/type/name/name_zh/nf/version/command_set/status` 不空；ref 缺省 null |
| ID 格式 | 三段 `{nf}@CompoundTask@{英文名}`（英文名 kebab-case，无编号；不含 version） |
| 文件名 ↔ ID | 文件名 = 完整 ID |
| command_set | 非空；命令名与 `组成` 边引用的 atom 一致；各命令的 AtomTask 文件存在 |
| 边规定 | `组成`→atom、`被引用于`→feature_task；不指向 ConfigObject/License |
| 场景差异 | 被多 feature 引用时，每引用方差异已回填（防假通用 R1.2） |
| 调测剥离 | 配置方法/典型脚本只含配置类命令（无 DSP/LST/EXP/STP） |
| 无证据 | 无 source/source_evidence_ids、无 `## 证据` 段 |

## 审查项（feature_task）

| 类别 | 检查点 |
|---|---|
| 字段必填 | `id/type/name/name_zh/nf/version/ref/status` 不空 |
| ID 格式 | 三段 `{nf}@FeatureTask@{feature_code}`（1:1 特性；不含 version） |
| 文件名 ↔ ID | 文件名 = 完整 ID |
| ref 真实 | `ref` 指向特性层对象存在 |
| 配置流程 | 步骤+单命令混合编排；每步链 compound 或 atom（`[[逻辑ID]]`）；引用的 compound/atom 文件存在；参数在对应 atom 配置方法字典内 |
| 防平铺 | 连续 ≥3 atom 无 compound → 警告（评估抽 compound） |
| 边规定 | `对应特性`→Feature、`编排`→compound/atom；不指向 ConfigObject |
| 调测剥离 | 配置流程只含配置类命令 |
| DP / 约束 | DP option 影响全记；无分支显式说明；不编号（md 级引用） |
| 无证据 | 无 source/source_evidence_ids、无 `## 证据` 段 |
