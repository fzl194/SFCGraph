# ConfigTask 层构建方案（Typed LLM Wiki · P5）· v2 Agent 构建

> 2026-07-09 · 基于 2 Agent 全量摸底（463 yaml）+ 用户定调。
> v1「纯投影」**废弃**——用户明确：这一层用 **Agent 读已有资产+原始 md 重写**，不是编码投影。
> 上游 spec：`docs/superpowers/specs/2026-07-08-config-generation-e2e-design.md`；准则：`assets/CLAUDE.md`。

---

## 0. 核心定位（用户强调，必须吃透）

**命令级别 task wiki ≠ 命令 wiki**：

| | 命令 wiki（已建，`assets/command/`） | 命令级别 task wiki（本次建，`assets/task/`） |
|---|---|---|
| 回答 | 这条命令**是什么**、语法长什么样 | 配置生成实例化时**怎么用**这条命令 |
| 知识性质 | 产品文档**静态字段**（功能/参数表/注意事项全文） | 面向**用户意图实例化**的动作知识（基础信息+rule+决策点） |
| 时机 | 产品理解 | 真正实例化（配置生成）时 |
| 形态 | 原始产品文档描述 | 参数值**从哪来/怎么定**、受什么约束、关键决策分支 |

**硬规则**：task wiki **不复述**命令静态字段（参数表/功能/注意事项全文已在命令 wiki），只链接。task wiki 聚焦"实例化时参数取值来源、决策点联动、约束规则、配置原则"。

## 1. 范围与边界

- **只构建命令级别 task（atom，187 个）**。compound（步骤）/feature（特性）级别 task **后续再建**。
- **只构建 assert 里已有的**（187 atom，半自动流水线已构建完），不新造。
- **围绕场景构建**（计费场景先行，再扩）。
- **仅 UDG@20.15.2**。UNC 残缺（27 孤立 atom 无树），不做。
- **双向**：task ↔ 命令 wiki（建）。task ↔ task（编排/跨 task 约束）**暂缓预留**，等 compound/feature 级别构建时同步建。

## 2. 摸底结论（Agent 全量统计，供构建复用）

- **atom 187**，每个 `ref = MMLCommand`（1:1 对应 187 命令），持 `parameter_bindings[]`（846 个绑定，平均 4.5/atom）。
- **rule 206**：`owner_task_ref` 100% 非空；149 条跨 task 约束（target≠owner）。atom 持 187 rule。
- **dp 55**：`owner_task_ref` 100% 非空；49 atom 持 dp。options 2~5 个，impacts 392 处（347 指参数、41 指 task）。
- **零悬空 ref**（atom→命令、参数绑定→CommandParameter、dp→参数/task 全命中）。
- **构建依据**：用 rule/dp 的 `owner_task_ref` 反查归属（绕开 atom 上 `rules`/`task_rules_ref` 双命名字段）。
- **证据**：148 个，按 stem 去重 61.3% 已在特性层 evidence/，48 个新拷。

## 3. 构建方式（Agent 驱动，非投影）

### 3.1 构建单元
**一个 atom task = 一个 Agent 任务**（或一个 Agent 处理同场景若干 atom）。Agent 读输入 → 凝练 → 写一个 task md。

### 3.2 每个 Agent 任务的输入
1. 该 atom task 的 yaml（`ConfigTask/assert/UDG/20.15.2/tasks/task-{local}.yaml`）—— `task_intent`/`ref`/`parameter_bindings`/`notes`
2. owner=本 task 的全部 rule yaml（`task_rules/rule-*.yaml`）—— 实例化约束
3. owner=本 task 的全部 dp yaml（`decision_points/dp-*.yaml`）—— 实例化决策
4. 命令 wiki md（`assets/command/UDG/20.15.2/{CMD}.md`）—— **只读链接，不复述**
5. 证据（`assets/evidence/UDG/20.15.2/{stem}.md`，按需读）—— 实例化原则/踩坑来源

### 3.3 task wiki md 内容规范（写什么 / 不写什么）

**写**（面向配置生成实例化）：
- front matter：`id`/`type: Task`/`task_layer: atom`/`ref`(命令 id)/`task_intent`/`task_logical_name`/`status`
- **一句话定位**：这条命令在配置生成时干什么（task_intent 展开）
- **参数取值来源表**（实例化核心）：`参数 | 绑定类型 binding_type | 取值来源 variable_source | 必选条件 requiredness | 决策/约束指向`。每个参数说清"值从哪来/怎么定"（如 URRNAME=decision_driven：内容计费全网规划、在线计费本端规划）。
- **关键决策点**（dp）：每个 dp 一段——问什么、选项、选了之后哪些参数怎么联动（option→impacts 叙述，不是字段堆砌）。
- **实例化约束**（rule）：每条 rule——约束什么、severity、违反后果、实例化时怎么遵守。
- **配置原则/踩坑**：从 notes/证据/parameter_bindings 注释提炼的实例化经验（如"URRID 从1000起始全网唯一分配"、"在线计费配默认配额取4294967295"）。
- **链接**：命令 wiki（基础信息）、证据、相关特性（若 evidence 来自特性数据规划表）。

**不写**：命令静态参数表全文、功能描述全文、注意事项全文（→ 链接命令 wiki）。

### 3.4 链接规范（CLAUDE.md §5.5）
- 命令 wiki：`[ADD URR](command/UDG/20.15.2/ADD-URR.md)`
- 证据：`[部署UPF](evidence/UDG/20.15.2/部署UPF_28493406.md)`
- 参数引用：链到命令 wiki（参数内聚在命令 md，不直达锚点也行——v1 的参数锚点基建**不做**，退化命令级链接）
- 产物路径：`assets/task/UDG/20.15.2/{local}.md`（如 `0-00001.md`）

## 4. 双向链接与回填
- **task → 命令 wiki**：task md「命令」节链接（Agent 写）。
- **命令 wiki → task**：命令 md「关联任务」节的 `[[Task ID]]` 占位回填为 `[配置URR](task/UDG/20.15.2/0-00001.md)`（task md 落地后，改 compile_commands.py 的 load_task_refs 判定已建 + 重跑，或 Agent 批量回填）。
- **task ↔ task**（编排、跨 task 约束）：**预留**，本次不建，等 compound/feature 级别构建时同步。

## 5. 实施计划
1. **Pilot**（先做）：Agent 写 `0-00001 配置URR`（ADD URR，3 rule + 1 dp + 8 绑定 + decision_driven，最能体现实例化知识）→ 用户审**内容定位**对不对。
2. **定调后放量**：围绕计费场景批量（0-00001~0-00018 三件套+过滤链），再扩其他场景。批处理粒度（1 Agent 几个 task）pilot 后定。
3. **回填命令 wiki 占位** + 更新 index/log/PROGRESS/memory + commit。

## 6. 待用户确认（Pilot 后）
- 内容定位是否准确（实例化导向、不复述静态、链接命令 wiki）
- 批处理粒度（1 Agent / 1 task？1 Agent / 1 场景 N task？）
- 起点场景（计费？）
