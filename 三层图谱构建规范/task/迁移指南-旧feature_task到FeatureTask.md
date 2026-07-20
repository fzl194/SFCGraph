# 迁移指南：旧 feature_task → 新版 FeatureTask

> **一次性迁移工程文档，非 SOP。** 把旧特性级 task（`2-XXXXX`）转成新格式。
> 配套脚本：`task/scripts/migrate_old_feature_tasks.py`。

---

## 0. 任务定义

把旧特性级 task（**feature_task**，`assets/task/{nf}/20.15.2/2-*.md`，UDG 46 + UNC 37 = **83** 个）转成 FeatureTask。

- feature_task = **特性级配置编排**（ref→Feature，编排 compound/atom + DP 场景）。
- **feature_task↔Feature 严格 1:1**（已验证 UDG46/UNC37 全 1:1）→ **feature_code 是天然锚**（像 atom 命令名），从 ref 末段现场读，**不需 slug 表**。
- 纯格式转换，不改业务内容，不补缺段。

---

## 1. 输入 / 输出

| | 旧 | 新 |
|---|---|---|
| 路径 | `assets/task/UDG/20.15.2/2-00003.md` | `三层图谱资产/FeatureTask/UDG/20.15.2/UDG@FeatureTask@GWFD-020301.md` |
| 文件名 | 编号 `2-00003` | `UDG@FeatureTask@GWFD-020301`（feature_code 锚）|

**feature_code 从哪来**：旧 YAML `ref` 末段。如 `ref: UDG@20.15.2@Feature@GWFD-020301` → `GWFD-020301`。

---

## 2. 总原则（对齐 atom/compound）

1. 只改格式不改内容。2. 编号三删（`2-`/`1-`/`0-`/`DP 0-`/`rule-0-`），特性编号/数值/字母后缀豁免。3. CS/business 跨层删链接留文字。

---

## 3. YAML 8 字段（固定顺序）

```
id / type / name / name_zh / nf / version / ref / status
```

| 旧字段 | → 新字段 | 规则 |
|---|---|---|
| `id: UDG@20.15.2@Task@2-00003` | `id: UDG@FeatureTask@GWFD-020301` | 三段式，feature_code 锚 |
| `type: Task` | `type: FeatureTask` | |
| `task_layer: feature` | **删** | |
| `task_logical_name: 内容计费基本功能` | `name_zh: 内容计费基本功能` | |
| （旧无） | `name: GWFD-020301` | **新增** = feature_code |
| `ref: UDG@20.15.2@Feature@GWFD-020301` | `ref: UDG@Feature@GWFD-020301` | 去 version |
| `nf`/`version`/`status` | 原样（status 保留源值如 foundation）| |
| `task_intent`/`source_evidence_ids` | **删** | |

---

## 4. 正文转换（逐段）

不补缺段。H1/引子/配置概览/配置流程/决策点/约束/场景差异 原样，只转链接。DP 标题去 `（DP 0-XXXXX）`；约束去 `rule-0-XXXXX` 留 severity。代码块不动。

---

## 5. 引用转换总表

| 旧 | 新 |
|---|---|
| `[2-00001](task/...)` | `[[{nf}@FeatureTask@{feature_code}]]`（本批迁，查 feature_map）|
| `[1-00002](task/...)` | `[[{nf}@CompoundTask@{slug}]]`（查 compound slug 表 UDG34/UNC38）|
| `[0-00020](task/...)` | `[[{nf}@AtomTask@{cmd}]]`（查 atom 命令表，现场读 0-*.md ref）|
| `[GWFD-020301](feature/...)` | `[[{nf}@Feature@GWFD-020301]]` |
| `[ADD URR](command/...)` | `[[{nf}@MMLCommand@ADD URR]]` |
| `[...](configobject/...)` / `(evidence/...)` | **删** |
| `[CS@x](task/...)` / `[BWM-CS](business/...)` | **删链接留文字** |
| `[SOP](task/特性步骤级构建SOP.md)` | **删链接留文字**（SOP 文档非 task 对象）|
| 旧 wiki4 占位 / 纯文本括号编号 | 同 atom/compound |

> **跨网元引用（关键）**：UNC feature_task 引用 UDG 特性时（href 含 `task/UDG/`、`feature/UDG/`，或 wiki4 `[[UDG@20.15.2@...]]`），脚本**从 href/wiki4 提 nf → 用 UDG 的 map** → 生成 `[[UDG@Feature@...]]` / `[[UDG@FeatureTask@...]]`（不是 UNC）。UDG 不引用 UNC（单向）。未提 nf 的裸编号用本 nf。源端坏链（如 href 以 `|` 结尾未闭合）原样保留为纯文本，不形成嵌套 wiki。

---

## 6. 关联段 → `## 边`（含双向链接，关键）

### 6.1 feature_task 自身边
删 `## 关联` 段，**白名单标签行提取**：
- `编排 compound` 行 → `- 编排 compound: [[{nf}@CompoundTask@{slug}]]`
- `直接引用 atom` 行 → `- 直接引用 atom: [[{nf}@AtomTask@{cmd}]]`
- 其余（特性 wiki/被引用于/证据/配置对象）随段删。

### 6.2 对应特性正向边（每个 feature_task 必有，1:1）
`- 对应特性: [[{nf}@Feature@{feature_code}]]` —— 即使 ref 已指 Feature，**边里也显式建**（引用规范一致）。

### 6.3 Feature 反向边回填（双向链接，assets/CLAUDE.md §5.6）
迁移后**回填 Feature 概述 md** `## 边` 加 `- 对应特性task: [[{nf}@FeatureTask@{feature_code}]]`（幂等：已有则跳过）。

**边顺序**：对应特性 > 编排 compound > 直接引用 atom。

> **特性层引用规范一致性**：特性层 Feature md 已是双方括号 `[[...]]`（feature 层构建时建立）。feature_task 迁移补 `feature_task↔Feature` 双向边（正向对应特性 + 反向对应特性task），使特性层与 task 层引用规范一致。

---

## 7. 校验清单

- [ ] 路径 `FeatureTask/{nf}/{ver}/{nf}@FeatureTask@{feature_code}.md`
- [ ] YAML 8 字段；`id={nf}@FeatureTask@{code}`、`name=code`、`ref={nf}@Feature@{code}`
- [ ] 禁词零命中（`2-`/`1-`/`0-`/`DP 0-`/`rule-0-`/`(evidence/`/`(configobject/`/`@20.15.2@`/`task_layer`/`task_intent`/`## 关联`）
- [ ] `## 边` 必有 `- 对应特性:` 且类型仅 `对应特性/编排 compound/直接引用 atom`
- [ ] Feature 概述 md 有 `- 对应特性task:` 反向边

---

## 8. 范例（2-00003 内容计费 → GWFD-020301）

```yaml
id: "UDG@FeatureTask@GWFD-020301"
type: "FeatureTask"
name: "GWFD-020301"
name_zh: "内容计费基本功能"
nf: "UDG"
version: "20.15.2"
ref: "UDG@Feature@GWFD-020301"
status: "draft"
---
# 内容计费基本功能（GWFD-020301）
> 特性静态知识见 [[UDG@Feature@GWFD-020301]]。...
## 配置概览 / 配置流程 / 决策点 / 约束 ...
## 边
- 对应特性: [[UDG@Feature@GWFD-020301]]
- 编排 compound: [[UDG@CompoundTask@charging-core-trio]]
- 编排 compound: [[UDG@CompoundTask@filter-chain]]
- 编排 compound: [[UDG@CompoundTask@rule-userprofile-bind]]
- 编排 compound: [[UDG@CompoundTask@charging-tail]]
- 直接引用 atom: [[UDG@AtomTask@SET LICENSESWITCH]]
```
Feature GWFD-020301 概述 md 同步加：`- 对应特性task: [[UDG@FeatureTask@GWFD-020301]]`。
