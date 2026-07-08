# 端到端方案：配置生成知识体系（LLM Wiki + 服务化 + 评测闭环）

> 状态：设计对齐稿（2026-07-08）
> 性质：整体大需求对齐文档。实施级细节（md 内部模板、REST 契约、评分权重等）见 §6 待定项，留具体实施时定。
> 关联：`业务图谱体系/配置生成SKILL/SKILL.md`（SOP）、`ConfigTask/task-build-skill/SKILL.md`（任务层构建）、`改进后三层图谱定义.md`（Schema）

---

## 0. 背景与目标

### 0.1 现状
配置生成知识体系由"三层静态图谱 + 一层动态任务层"构成，但资产**分散在多个目录、形态不一**：

| 层 | 位置 | 形态 | 体量 |
|---|---|---|---|
| 命令层 | `CommandGraph/data/assets/{nf}/{ver}/*.jsonl` | jsonl（机器抽取） | 33,121 条（UDG+UNC） |
| 特性层 | `FeatureGraph/data/{nf}/{ver}/*.jsonl` | jsonl（机器抽取） | 2,897 条 |
| 业务层 | `business-graph/**/*.md` + `BusinessGraph/*.yaml`（派生） | md（源）+ yaml（派生） | 3 套并存，含 1 套冗余副本 |
| 任务层 | `ConfigTask/assert/{nf}/{ver}/*.yaml` | yaml（半自动 pipeline） | UDG 206 task+27dp+55rule；UNC 基本空 |
| SOP | `业务图谱体系/配置生成SKILL/` | md（手写） | — |
| 后端 | `platform-next/` FastAPI | — | 业务层解析 md；命令/特性读 jsonl |

**痛点**：
1. 业务专家难以评价/修改结构化（yaml/jsonl）资产；关系复杂的任务层尤其难审。
2. 资产形态不一，无法统一"按需索取"。
3. 配置生成 SKILL 目前直接 Read md 文件作 reference，**核心资产有外泄风险**。
4. 无评测手段——图谱质量无法客观衡量、无法定位改进点。

### 0.2 目标
构建一个**闭环的端到端配置生成体系**：
- **统一资产面**：所有层资产统一为 LLM Wiki 形态（一对象一 md，人可读改，关系 wiki 串联）。
- **服务化按需返回**：配置生成 Agent 通过服务化接口按子场景取"知识包"，**核心资产不外泄**。
- **评测闭环**：test tool 反向评价图谱质量、debug tool 定位并改进图谱，形成自校正回路。

---

## 1. 整体闭环架构

```
┌──────────────── 源（不动）─────────────────┐
│ CommandGraph/data/*.jsonl   (命令层源)      │
│ FeatureGraph/data/*.jsonl   (特性层源)      │
│ ConfigTask/assert/*.yaml    (任务层源/线索) │
│ business-graph/**/*.md      (业务层源/线索) │
│ output/**                   (产品文档·凝练原料) │
└──────────────┬─────────────────────────────┘
               │ 生成器（每层一个）
               │  · 命令/特性层：转换已有结构化资产
               │  · 业务/任务层：读产品文档重新凝练
               ▼
┌──────────────── assets/ （LLM Wiki 聚合层）──────────┐
│ 一对象一 md  +  [[wiki 链接]] 承载关系                │
│ command/ feature/ license/ business/ task/ skill/ schema │
└──────────────┬──────────────────────────────────────┘
               │ 服务化接口（platform-next 扩展）
               │ GET /knowledge-package/{域}/{场景}  · 一次性返回子场景裁剪子图
               ▼
   用户需求 → [配置生成 SKILL(SOP, Phase0-7+3GATE)] → Agent 取「子场景知识包」→ 生成 MML
       ▲                                                       │
       │ 反哺                                                   ▼
   debug tool ←── 定位层/对象 ────── test tool(评分) ←── 输出结果 ───┘
```

**关键边界**：`assets/` 是**唯一对外暴露面**。源留在 builder 目录不外泄；Agent 通过服务化接口取知识包，不直接读源文件。

---

## 2. 资产层（assets/）设计

### 2.1 统一原则：LLM Wiki
- **一个对象 = 一个 md**：md 内聚该对象所有知识，关联关系用 `[[wiki 链接]]` 互引。
- **文件名 = 对象唯一 ID**（沿用现有编号：`BD-BSA-01` / `NS-CH-01` / `CS-CH-03` / `GWFD-010171` / 命令名 / `task-1-00003`）。
- 灵感：LLM Wiki——每个 md 是一个小的知识概念，通过 wiki 链接把知识穿起来。

### 2.2 各层对象粒度

| 层 | 每个对象一个 md | 关系承载方式 |
|---|---|---|
| **业务层** | 业务域 / 场景 / 方案 各一 md | CS `[[方案]]` ↔ NS `[[场景]]` ↔ BD；决策点用标题内嵌 |
| **特性层** | 特性（**扁平、无子特性**）/ License 各一 md | 特性 `[[License]]` wiki 引用 |
| **命令层** | 每命令一 md（参数信息内聚进去，不拆三对象） | 命令级 Task wiki→ 命令 md |
| **任务层** | 每 Task 一 md（rule + 决策点用标题内嵌，不拆三对象） | 步骤级 Task wiki→ 子 Task；命令级 Task wiki→ 命令 md |

### 2.3 目录骨架（已对齐）
按层分，层内按各自天然维度：

```
assets/
├─ command/{nf}/{version}/<command>.md          # 如 command/UDG/20.15.2/ADD-URR.md
├─ feature/{nf}/{version}/<feature_code>.md
├─ license/{nf}/{version}/<license>.md
├─ business/{domain}/{scenario}/<id>.md         # 如 business/business-awareness/charging/CS-CH-03.md
│                                              #   + 域根下 bd-<domain>.md
├─ task/{nf}/{version}/<task-id>.md
├─ skill/SKILL.md
└─ schema/                                      # 三层图谱 Schema 定义
```

> 命令/特性/任务层按 `nf/version`（UDG/UNC × 20.15.2）；业务层按 `域/场景`。新目录暂名 `assets/`，可换。

### 2.4 各层 md 产出方式（关键区分）

| 层 | 产出方式 | 说明 |
|---|---|---|
| **命令层 / 特性层** | **转换已有结构化资产** | jsonl 已由 builder 抽取就绪，写转换器一键生成 md。机器资产，人不改。 |
| **业务层 / 任务层** | **读产品文档重新凝练** | 现有 `business-graph` md / `ConfigTask` yaml **仅作参考线索，不直接转换**。需重新读 `output/` 产品文档凝练成知识 md。 |

> 这是本次对齐的关键澄清：业务层/任务层不是"搬现有结构化数据"，而是"以现有资产为线索、重新凝练知识"。这也意味着这两层工作量大于命令/特性层。

### 2.5 与源的关系：聚合层（源不动）
- 4 层源仍留在各自 builder 目录（`CommandGraph/data`、`FeatureGraph/data`、`ConfigTask/assert`、`business-graph`），builder / platform-next 基本不改。
- `assets/` 是**聚合 / 对外 / 消费面**，由生成器从源产出。
- 风险最低、可增量落地、可回退。

### 2.6 md 内部格式
**待实施时定**（候选方向：YAML front matter 放自身属性+路由维度，markdown 正文放人读叙述，`[[wiki]]` 承载关系）。共享对象（如 ConfigObject 被多命令引用）是独立 md 还是内聚，留实施时定。**本设计不锁死。**

---

## 3. 四大支柱

### 3.1 服务化接口（platform-next 扩展）
- 新增"知识包"接口：`GET /knowledge-package/{域}/{场景}`（精确契约待定）。
- **输入** = 已锁定的 `{域}/{场景}`（Phase 0 识别仍由 Agent 做，符合现有 SKILL 设计）。
- **输出** = 该子场景**裁剪过的子图全量 md 包**：BD/NS/CS + 关联特性 + 关联命令 + 对应任务，**一次性返回**。
- Agent 通过工具调用取包，不直接读源文件 = **资产不外泄**。

### 3.2 配置生成 SKILL 切换
- `SKILL.md` 的知识加载从 `Read knowledge/{域}/{场景}/*.md` → **调知识包接口**。
- SOP 主体（Phase 0-7 + 3 个 GATE / 强制契约）**不动**。
- 目标态即 SKILL.md §2.2/§14 已写的"将来迁移后端：路径换接口调用"。

### 3.3 test tool（反向评价图谱质量）
- **测试集** = `(用户原始需求, 现网脚本, 期望方案/LLD/MML)`，进 git，标 `域/场景/方案`。
- **评分** = AI MML 核查通过率 + 黄金集 diff + 人工抽检。
- 评分维度映射回图谱层（哪个 Phase 失败 → 哪层资产有问题）。

### 3.4 debug tool（定位 + 改图谱回路）
- 失败 → 沿 `输出 → SKILL Phase → 知识包 md → 源对象` 回溯，定位到**层 / 对象**。
- 给修改建议（改源 md / yaml / jsonl）→ 重生成 assets md → 重测，闭环。

---

## 4. 关键决策记录（本次对齐结论）

| # | 决策 | 选择 | 理由 |
|---|---|---|---|
| D1 | 新目录 vs 现有目录关系 | **聚合层（源不动）** | 风险最低，builder/后端基本不改，可增量 |
| D2 | 资产形态 | **LLM Wiki（一对象一 md + wiki 链接）** | 人可读改 + Agent 可读 + 关系可解析 |
| D3 | 目录骨架 | **按层分 + 层内按天然维度** | 各层维度不同（nf/version vs 域/场景），各自归位 |
| D4 | 业务/任务层 md 来源 | **读产品文档重新凝练（非转换现有）** | 现有 yaml/大 md 仅作线索；这两层是知识层，要重凝练 |
| D5 | 命令/特性层 md 来源 | **转换已有 jsonl** | 机器资产已就绪，人不改 |
| D6 | 任务层对象粒度 | **Task 一 md（rule+决策点内嵌，不拆三对象）** | 知识 md 视角，一个概念一个 md |
| D7 | 服务化返回粒度 | **一次性返回子场景裁剪子图全量包** | 用户明确要求"最好一次性返回" |
| D8 | md 内部模板 | **待定（实施时定）** | 不过早细化 |

---

## 5. 演进路线（阶段，可调整）

| 阶段 | 内容 | 产出 | 依赖 |
|---|---|---|---|
| **P1** | `assets/` 骨架 + 命令层/特性层 md 转换器 | 命令/特性 md 进 assets/（最快见效，验证 LLM Wiki 范式） | 无 |
| **P2** | 服务化知识包接口（基于 P1 + 现有业务层先接） | `GET /knowledge-package` 可用 | P1 |
| **P3** | 业务层 md 重新凝练（读产品文档） | business/ 下对象 md | P1 骨架 |
| **P4** | 任务层 md 重新凝练 | task/ 下对象 md | P1 骨架 |
| **P5** | 配置生成 SKILL 切换到接口 | SKILL 不再 Read md，走接口 | P2/P3/P4 |
| **P6** | test tool | 测试集 + 评分 | P5（需端到端可跑） |
| **P7** | debug tool | 定位 + 改图回路 | P6 |

> test/debug 也可在 P3/P4 凝练时用"黄金集"提前反向校验资产质量，不必严格等 P5。

---

## 6. 待定项（实施时再定，不阻塞本设计）

- md 内部模板：front matter 字段范围、标题组织、ConfigObject 等共享对象是否独立 md。
- 业务层 DP（方案/场景级）与任务层 DP（命令配法级）的精确边界与去重。
- 服务化接口的 REST 契约、知识包格式（单文件打包 / md 集合 + manifest）。
- test 评分权重、黄金集来源与标注流程。
- debug 定位算法（失败 → 层/对象的归因规则）。
- `assets/` 目录最终命名。
- 业务层 3 套冗余（business-graph md / BusinessGraph yaml / 业务图谱体系副本）的归档时序。

---

## 7. 附录：现状资产盘点

| 层 | 位置 | 形态 | 体量 | 服务化现状 |
|---|---|---|---|---|
| 命令层 | `CommandGraph/data/assets/{nf}/{ver}/` | jsonl（8 类对象 + 边） | UDG 8 文件 12,526 条 + UNC 3 文件 20,595 条 | platform-next 读 jsonl |
| 特性层 | `FeatureGraph/data/{nf}/{ver}/` | jsonl（4 类） | UDG 939 + UNC 1,958 条 | platform-next 读 jsonl |
| 业务层 | `business-graph/{场景}/three-layer-graph/01-business-graph.md` | md（场景级大 md） | 1,550 行（源） | platform-next **解析 md** |
| · 派生 | `BusinessGraph/*.yaml` | yaml（对象级） | 27 个 | 未接 |
| · 副本 | `业务图谱体系/.../01-business-graph.md` | md | 1,550 行（冗余） | — |
| 任务层 | `ConfigTask/assert/{nf}/{ver}/` | yaml | UDG 206 task+27dp+55rule+task-index；UNC 3 task+30dp | task_graph router 雏形 |
| SOP | `业务图谱体系/配置生成SKILL/SKILL.md` | md | 449 行 | — |
| 产品文档 | `output/` | md | 命令手册 13,075 + 特性 ~900 | 凝练原料 |

**业务域注册表现状**：2 域（业务感知、APN 接入）× 4 子场景（计费、带宽控制、访问限制、APN 开通）。

**已知缺口**：
- 全仓库无 jsonl/yaml → md 反向生成器（数据流单向）。
- 任务层 UNC 基本空白；UDG 也无完整人审 md 视图。
- task-build-skill §12.4 的场景闭包层（closures/ + docs/）未建。
