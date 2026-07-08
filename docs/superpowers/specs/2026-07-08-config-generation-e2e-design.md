# 端到端方案：类型化的 LLM Wiki —— 配置生成知识体系

> 版本：v2（2026-07-08）。v1 见 commit `0021141`。
> v2 变更：吸收 Karpathy LLM Wiki 内核（编译/Ingest/Query/Lint、index+log、LLM 维护+人审、复利回填），并明确本体系的核心定位 = **类型化的 LLM Wiki（有预定义 Schema 约束的 LLM Wiki）**。
> 性质：整体大需求对齐文档。实施级细节（REST 契约、评分权重、typed 页模板字段）见 §10 待定项。
> 关联：`改进后三层图谱定义.md`（Schema 权威）、`业务图谱体系/配置生成SKILL/SKILL.md`（配置 SOP）、`ConfigTask/task-build-skill/SKILL.md`（任务层构建）

---

## 0. 核心定位

> **我有大量产品文档 + 已抽取的结构化字段 + 任意知识 → 编译成最终资产（typed wiki）→ 服务化接口取一个子集 → 给 SKILL 做具体场景的配置生成。**

本体系 = **类型化的 LLM Wiki（Typed LLM Wiki）**：继承 Karpathy LLM Wiki 的内核，但页面不是随意的，而是按预定义 Schema 类型化的。

| 维度 | Karpathy LLM Wiki | 本体系（Typed LLM Wiki） |
|---|---|---|
| 页面类型 | LLM 即兴决定（entity/concept/comparison/synthesis…） | **预定义对象类型**：业务域/场景/方案/特性/License/命令/Task… |
| 关系 | 松散、即兴 | **预定义关系类型**：contains/uses_feature/operates_on/ref/precedes…（Schema 边） |
| 页面内部结构 | 自由演化 | **由 Schema 的对象定义约束**（字段/标题） |
| `[[wiki 链接]]` | 任意互链 | = Schema 的关系边（每种链接对应一种关系类型） |

**一句话**：**md 是载体，Schema 是约束。** 每个 md 是某个预定义对象类型的实例——内部结构遵循 Schema 对象定义，`[[wiki]]` 承载 Schema 关系。结构化的"类型约束"与 LLM Wiki 的"md 形态"在此统一，不再二选一。

**继承自 LLM Wiki 的内核**（这些是我们的工作范式）：
- **编译，不是查询时检索**：知识预先编译进持久 wiki，查询时读已编译层，不每次重推导。
- **持久 + 复利**：wiki 越用越厚；好的综合回填，新源更新旧页、揭矛盾、标过时。
- **LLM 是 writer/maintainer，人是 sourcer/reviewer/editor**。
- **三操作**：Compile/Ingest · Query · Lint。
- **两基建**：`index.md` · `log.md`。

---

## 1. 整体闭环架构

```
┌──────────── Raw Sources（immutable，真相之源）────────────┐
│  · 产品文档 output/**（命令手册/特性指南/…）               │
│  · 已抽取结构化字段 CommandGraph/data + FeatureGraph/data  │
│  · 任意知识（外部资料/专家补充/历史脚本）                    │
└─────────────────────┬─────────────────────────────────────┘
                      │  Compile / Ingest（LLM 维护，人审）
                      │  · 命令/特性层：结构化原料 → 投影成 typed md
                      │  · 业务/任务层：非结构化原料 → LLM 按 Schema 凝练
                      ▼
┌──────────── assets/ （Typed LLM Wiki，唯一对外面）──────────┐
│  typed md 页面（对象类型实例）+ [[wiki 关系边]]             │
│  command/ feature/ license/ business/ task/ skill/ schema   │
│  + index.md（内容目录）  + log.md（演进时间线）             │
│  + 维护准则 CLAUDE.md（ingest/lint/query 工作流）           │
└─────────────────────┬─────────────────────────────────────┘
        ┌─────────────┴──────────────┐
        ▼ Query (服务化)             ▼ Lint (静态健康检查)
┌───────────────────────────┐   ┌──────────────────────────┐
│ 服务化接口（platform-next）│   │ 矛盾/孤立页/缺页/         │
│ GET 子场景知识子集         │   │ 缺引用/过时声明           │
│ （先读 index 定位→按需取） │   │ → 触发 Compile 修复       │
└─────────────┬─────────────┘   └──────────────────────────┘
              │
              ▼
  用户需求 → [配置生成 SKILL(SOP, Phase0-7+3GATE)]
           → Agent 取「子场景知识子集」→ 生成 MML
              │                       │
              │  ┌────────────────────┘  好的综合回填（复利）
              │  ▼
              │  assets/ 新增/更新页
              ▼
  输出结果 → test tool(评分, 动态) → debug tool(定位层/对象 → 改源 → 重 Compile → 重测)
```

**三重质量回路**：① Lint（静态，主动）② test（动态，端到端）③ debug（定位 + 改图）。**两条资产增长回路**：① Compile/Ingest（喂新原料）② Query 回填（配置生成副产物复利）。

---

## 2. 三层架构（对应 Karpathy 三层）

### 2.1 Raw Sources（immutable，只读，真相之源）
- 产品文档：`output/**`（命令手册 13,075 + 特性 ~900 + …）
- 已抽取结构化字段：`CommandGraph/data/*.jsonl`、`FeatureGraph/data/*.jsonl`（机器抽取的"已加工原料"）
- 任意知识：外部资料、专家补充、历史配置脚本
- **LLM 读不改**。

### 2.2 Wiki（assets/，LLM 完全拥有，人读 LLM 写）
- typed md 页面：每个 md = 一个 Schema 对象类型实例。
- `[[wiki 链接]]` = Schema 关系边。
- LLM 创建页、新源到来时更新、维护交叉引用、保持一致、回填好综合。**人审，LLM 写**。

### 2.3 Schema 层（约束 + 维护准则，人机共演化）
两层：
- **对象/关系 Schema**：`改进后三层图谱定义.md`（权威）——定义对象类型、字段、关系类型。wiki 页面和链接必须符合它。
- **维护准则**（`assets/CLAUDE.md`，待建）：告诉 Agent 怎么 Compile/Ingest/Query/Lint、页面约定、index/log 维护规则。这是让 Agent 成为"有纪律的 wiki 维护者"而非通用 chatbot 的关键，随实践和 Agent 共演化。

---

## 3. 核心操作

### 3.1 Compile / Ingest（编译：raw → typed wiki）
统一操作，难度因原料结构化程度而异：

| 原料 | 编译方式 | 谁做 |
|---|---|---|
| 命令层/特性层 jsonl（已结构化、已对齐 Schema） | **投影**成 typed md（代码转换器） | 代码 + LLM 校验 |
| 产品文档 / 任意知识（非结构化） | LLM **按 Schema 凝练**对象与关系 → typed md → **人审** | LLM 写 + 人审 |
| 现有 `business-graph` md / `ConfigTask` yaml | 仅作**参考线索**，不直接转换；按 Schema 重新凝练 | LLM + 人审 |

> 这是 v2 对 v1 §2.4 的修正：业务/任务层不是"人读文档写 md"，而是 **LLM（Ingest）读文档按 Schema 凝练、业务专家审改**。

### 3.2 Query（查询：服务化取子集 → SKILL 配置生成 → 回填）
- Agent 先读 `index.md`（或子场景子 index）定位相关页 → 按需取（或一次性取子场景裁剪子集）。
- 配置生成过程中产出的**好综合**（方案对比、决策理由、踩坑、新发现的连接）**回填** assets/ 为新页或更新现有页 → 体系复利增长。

### 3.3 Lint（静态健康检查）
定期让 LLM 体检 assets/：
- 页面间**矛盾**、被新源**过时**的声明
- **孤立页**（无入链）、**缺页**（重要概念被引用但无独立页）
- **缺交叉引用**、Schema 不合规的 typed 页
- 可用新原料填的**数据缺口**
→ 触发 Compile 修复。

---

## 4. 基建文件

- **`assets/index.md`**（内容导向）：整个 wiki 目录，每页一行（链接 + 一句话摘要 + 类型 + 元数据），按类别组织。Query 时先读它定位。中等规模避免 embedding RAG 基建。
- **`assets/log.md`**（时间导向）：append-only，记录 Compile/Ingest/Query 回填/Lint。一致前缀（`## [日期] ingest | <源>`）便于 grep。给演进时间线，帮 Agent 理解近期变更。

---

## 5. 人与 Agent 的分工（核心原则）

| 角色 | 职责 |
|---|---|
| **人（业务专家等）** | sourcing（喂原料/指出文档）、问对问题、**review/editor**（审 LLM 凝练的页、纠正、引导强调点）、judgment |
| **Agent（LLM）** | Compile/Ingest（读原料→凝练/投影→写 typed md）、维护交叉引用、Lint、Query 检索、回填 |

> "Obsidian 是 IDE，Agent 是程序员，wiki 是代码库。" 业务专家的负担从"写/改结构化资产"降到"**审 Agent 凝练的成果 + 喂原料**"——这是 LLM Wiki 解决"PKM 因维护成本高而失败"的核心价值，也是我们体系可持续的关键。

---

## 6. 各层 typed 页面（对象类型 + 粒度）

每个对象一个 md，文件名 = 对象唯一 ID：

| 层 | 对象类型（每类一个 md） | 关键关系（wiki 边） |
|---|---|---|
| **业务层** | 业务域 / 场景 / 方案 | contains / selected_by / uses_feature；决策点内嵌 |
| **特性层** | 特性（扁平无子特性）/ License | requires_license |
| **命令层** | 命令（参数内聚，不拆三对象） | operates_on / has_parameter；命令级 Task ←→ 命令 |
| **任务层** | Task（rule + 决策点内嵌标题，不拆三对象） | precedes / contains / ref→命令；步骤级 Task ←→ 子 Task |

**目录骨架**（已对齐）：`assets/{层}/{天然维度}/<id>.md`
- `command|feature|license/{nf}/{version}/<id>.md`
- `business/{domain}/{scenario}/<id>.md`（+ 域根 `bd-<domain>.md`）
- `task/{nf}/{version}/<task-id>.md`
- `skill/` · `schema/`

**md 内部格式**：由 Schema 对象定义约束（typed 页模板），实施时按 `改进后三层图谱定义.md` 落地。**候选方向**：YAML front matter（自身属性 + 路由维度）+ markdown 正文（人读叙述 + 表格）+ `[[wiki]]`（Schema 关系边）。共享对象（ConfigObject 被多命令引用）独立 md vs 内聚，留实施定。

---

## 7. 服务化接口（Query）

- platform-next 扩展知识子集接口：`GET /knowledge-package/{域}/{场景}`（契约待定）。
- **输入** = 已锁定 `{域}/{场景}`（Phase 0 识别仍由 Agent 做）。
- **输出** = 子场景**裁剪过的 typed md 子集**（BD/NS/CS + 关联特性 + 关联命令 + 对应任务），一次性返回。
- 走"先 index 定位 → 按需取/打包"。
- Agent 工具调用取子集，**不直接读源 = 资产不外泄**。

## 8. 配置生成 SKILL 切换

- `SKILL.md` 知识加载从 `Read knowledge/{域}/{场景}/*.md` → **调知识子集接口**。
- SOP 主体（Phase 0-7 + 3 GATE + 强制契约）**不动**。
- 配置生成中的好综合按 §3.2 回填 assets/。

---

## 9. 评测与改进闭环

- **test tool（动态）**：测试集 = `(需求, 现网脚本, 期望方案/LLD/MML)`，进 git，标 `域/场景/方案`。评分 = AI MML 核查通过率 + 黄金集 diff + 人工抽检。
- **Lint（静态）**：见 §3.3，主动、不依赖失败触发。
- **debug tool（定位改图）**：test 失败 → 沿 `输出 → SKILL Phase → 知识子集 md → 源对象` 回溯定位层/对象 → 改源（raw 或参考线索）→ 重 Compile → 重测。

---

## 10. 关键决策记录

| # | 决策 | 选择 |
|---|---|---|
| D1 | 新目录 vs 现有目录 | **聚合层（源不动）**——builder/platform-next 基本不改 |
| D2 | 资产形态 | **类型化 LLM Wiki（typed md + wiki 边）**——md 载体 + Schema 约束 |
| D3 | 目录骨架 | 按层分 + 层内按天然维度 |
| D4 | 核心定位 | **Typed LLM Wiki**：继承 LLM Wiki 内核 + 预定义 Schema 类型约束 |
| D5 | wiki 的 writer | **Agent 写维护，人 sourcer/reviewer/editor**（R1 反转） |
| D6 | 编译（Compile） | 统一操作：结构化原料投影 / 非结构化原料 LLM 凝练+人审 |
| D7 | 业务/任务层 md 来源 | **LLM 读产品文档按 Schema 凝练，人审**（现有 yaml/大 md 仅线索） |
| D8 | 命令/特性层 md 来源 | 从 jsonl 投影转换 |
| D9 | 三操作 | Compile/Ingest · Query（+回填）· Lint |
| D10 | 两基建 | index.md + log.md |
| D11 | 质量回路 | Lint（静态）+ test（动态）+ debug（定位改图） |
| D12 | 服务化返回 | 子场景裁剪子集，先 index 定位 |
| D13 | SKILL 切换 | Read md → 调接口，SOP 主体不动 |
| D14 | md 内部模板 | 由 Schema 对象定义约束（实施时落地） |

---

## 11. 演进路线

| 阶段 | 内容 | 产出 |
|---|---|---|
| **P1** | `assets/` 骨架 + index.md/log.md + 维护准则 CLAUDE.md 草案 | wiki 容器就位 |
| **P2** | 命令/特性层 Compile 器（jsonl→typed md） | 命令/特性 md 进 assets/（最快见效，验证范式） |
| **P3** | 服务化 Query 接口（基于 P2 + 现有业务层先接） | `GET /knowledge-package` 可用 |
| **P4** | 业务层 Compile（LLM 读产品文档按 Schema 凝练 + 人审） | business/ typed md |
| **P5** | 任务层 Compile（同 P4 方法） | task/ typed md |
| **P6** | 配置生成 SKILL 切换到接口 + Query 回填回路 | 端到端可跑 |
| **P7** | test tool | 测试集 + 评分 |
| **P8** | Lint + debug tool | 静态体检 + 定位改图闭环 |

> Lint 可在 P4/P5 早期就用"黄金集"反向校验 typed md 质量；不必严格等 P7。

---

## 12. 待定项（实施时定，不阻塞）

- typed 页模板：每个对象类型的具体 front matter 字段 + 标题组织（按 `改进后三层图谱定义.md` 落地）。
- ConfigObject 等共享对象：独立 typed md vs 内聚进命令 md。
- 业务层 DP（方案/场景级）与任务层 DP（命令配法级）精确边界与去重。
- 服务化 REST 契约、子集打包格式。
- test 评分权重、黄金集来源与标注。
- Lint 规则集、debug 定位归因算法。
- `assets/` 最终命名、维护准则 CLAUDE.md 的具体条目。
- 业务层 3 套冗余（business-graph md / BusinessGraph yaml / 业务图谱体系副本）归档时序。

---

## 13. 附录：现状资产盘点

| 层 | 位置 | 形态 | 体量 |
|---|---|---|---|
| 命令层 | `CommandGraph/data/assets/{nf}/{ver}/` | jsonl | UDG 8文件 12,526条 + UNC 3文件 20,595条 |
| 特性层 | `FeatureGraph/data/{nf}/{ver}/` | jsonl | UDG 939 + UNC 1,958 条 |
| 业务层 | `business-graph/{场景}/.../01-business-graph.md` | md（场景级大 md） | 1,550 行（源/线索） |
| · 派生 | `BusinessGraph/*.yaml` | yaml | 27 个（线索） |
| · 副本 | `业务图谱体系/.../01-business-graph.md` | md | 1,550 行（冗余） |
| 任务层 | `ConfigTask/assert/{nf}/{ver}/` | yaml | UDG 206task+27dp+55rule；UNC 基本空 |
| SOP | `业务图谱体系/配置生成SKILL/SKILL.md` | md | 449 行 |
| Schema | `改进后三层图谱定义.md` | md | 权威对象+关系定义 |
| 产品文档 | `output/` | md | 命令手册 13,075 + 特性 ~900（Compile 原料） |

**注册表现状**：2 域（业务感知、APN 接入）× 4 子场景（计费、带宽控制、访问限制、APN 开通）。
**已知缺口**：无反向 md 生成器（数据流单向）；任务层 UNC 空白；场景闭包层（closures/+docs/）未建。
