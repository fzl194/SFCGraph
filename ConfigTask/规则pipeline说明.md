# ConfigTask 规则抽取 pipeline 说明（审查版）

> 这份文档讲清楚：规则 pipeline 怎么把一份特性配置文档变成 ConfigTask 骨架（`config_tasks.skeleton.jsonl`）。
> 不涉及代码细节，只讲"每步做什么、每个字段从哪来"，供审查。
> 当前状态：**规则步已实现并验证（内容计费 5 task 边界全对）**；语义字段（起名/意图/参数分类）留给后续 Agent，本文不涉及。

---

## 一、准备工作（跑之前要有什么）

| 准备项 | 是什么 | 当前状态 |
|---|---|---|
| **语料清单** `ConfigTask/data/{UDG,UNC}_feature_files.csv` | 特性→文档路径的映射表（哪些特性、配置文档在哪） | ✅ 已就位 |
| **原始配置 md** | 部署/激活/配置 文档（产品文档，内容全） | ✅ 在 `output/.../` |
| **配置文件** `ConfigTask/pipeline.yaml` | 声明 UDG/UNC 各版本的语料清单路径 + 要跑哪些步骤 | ✅ 已写 |
| **命令图谱**（可选） | `CommandGraph/.../mml_commands.jsonl`，仅用于可选的命令名校验 | 可不要，pipeline 不依赖 |

**怎么跑**（单特性，迭代验证用）：
```
cd ConfigTask
python build_all.py UDG 20.15.2 GWFD-020301      # 跑内容计费
```
省略 `GWFD-020301` 则跑该网元版本下全部可配置特性。

**产出**：`ConfigTask/data/assets/UDG/20.15.2/config_tasks.skeleton.jsonl`（每行一个 task 骨架）。

---

## 二、pipeline 流程（6 步，顺序执行）

对每个选中的特性配置文档，依次做：

### 步骤 1 · select（选文档）
- 读语料清单 CSV，**只留配置类文档**（文件名以"部署/激活/配置"开头的，排除"概述/实现原理/参考信息"）。
- 若指定了 `feature_id`，只留该特性的文档。
- 产出：要处理的文档列表（内容计费 → 1 份 `部署UPF.md`）。

### 步骤 2 · cut_boundaries（切 task 边界）—— 最关键
- 读配置 md，按标题切出 **4 段**：操作流程 / 操作步骤 / 任务示例 / 数据规划表（注：数据规划表在"必备事项→数据"下）。
- **有"操作流程"段**（内容计费/IPSec）：解析里面的"阶段"列表 + 每个"阶段"对应的步骤范围（如阶段①对应步骤1-2）。**每个阶段 = 一个 task**。没被任何阶段覆盖的步骤（如内容计费步骤10-11），按连续性归到前一个 task。
- **没有"操作流程"段**（接入控制/eDRX）：产 **1 个"待 Agent 分组"的候选 task**（整段命令序列先放一起，等 Agent 来拆）。
- 产出：task 列表，每个 task 带它负责的步骤范围 + 阶段名。

> 内容计费结果：5 个 task，步骤范围 (1-2)/(3-5)/(6)/(7-8)/(9-11)，与手建样例边界一致。

### 步骤 3 · commands（抽命令）
- 对每个 task，按它的步骤范围，从"操作步骤"段抽出 MML 命令（按出现顺序，含子步骤里的命令）。
- 每个命令构造实例键 `UDG@20.15.2@MMLCommand@ADD URR`。
- 产出：每个 task 的有序命令列表。

### 步骤 4 · params（抽参数）
- 从"数据规划表"段解析参数表（格式统一：类别=命令 / 参数名称=中文(CODE) / 获取方法）。
- 对每个命令，把它名下的参数挂上去，构造实例键 `UDG@20.15.2@CommandParameter@ADD URR:URRNAME`。
- **标 reference_hint**：参数表"获取方法"列含"已配置数据中获取" → 标 True（表示这个参数的值来自已有配置，是引用类）。跨多表（内容计费表1-4）按命令+参数去重。
- 产出：每个命令的参数列表（含实例键 + reference_hint）。**不分类 fixed/variable/reference**（留给 Agent）。

### 步骤 5 · assemble（拼骨架）
- 把每个 task 拼成完整骨架 dict：填身份字段（task_id 编号）、来源字段（文档路径）、raw_steps_text_raw（该 task 步骤范围的原文切片）。
- **语义字段留空**（task_logical_name / task_goal / task_summary）——交给 Agent。
- 产出：task 骨架列表。

### 步骤 6 · emit_skeleton（写文件）
- 把骨架列表写成 `config_tasks.skeleton.jsonl`，每行一个 task。

---

## 三、每个字段怎么抽（速查）

骨架里每个字段，当前是规则填了还是留给 Agent：

| 字段 | 谁填 | 怎么来 | 内容计费例子 |
|---|---|---|---|
| `task_id` | 规则（assemble）| `网元@版本@ConfigTask@编号`，编号顺序递增 | `UDG@20.15.2@ConfigTask@00001` |
| `task_logical_name` | **Agent（待）** | 当前空。Agent 把阶段名归一化为可复用名 | （待填，如"配置计费动作链"）|
| `nf` / `version` | 规则（assemble）| 来自运行上下文 | `UDG` / `20.15.2` |
| `raw_steps_text_raw` | 规则（assemble）| 该 task 步骤范围的"操作步骤"原文切片 | "1.配置URR…ADD URR…2.URR组…ADD URRGROUP…" |
| `task_goal` | **Agent（待）** | 当前空 | （待填）|
| `task_summary` | **Agent（待）** | 当前空 | （待填）|
| `commands[].command_ref` | 规则（commands）| 操作步骤的命令名 → 构造键 | `…@MMLCommand@ADD URR` |
| `commands[].parameters[].parameter_ref` | 规则（params）| 数据规划表的参数名 → 构造键 | `…@CommandParameter@ADD URR:URRNAME` |
| `commands[].parameters[].reference_hint` | 规则（params）| 数据规划表"获取方法"含"已配置数据中获取"→True | UPURRNAME1=True（引用离线URR）|
| `commands[].parameters[].binding_type` | **Agent（待）** | 当前未填。Agent 分类 fixed/variable/reference | （待填）|
| `task_category` | 规则（assemble）| =配置（来自配置类文档）| `配置` |
| `status` | 规则（assemble）| =active | `active` |
| `source_evidence_ids` | 规则（assemble）| 该配置文档的路径 | `[…/部署UPF_28493406.md]` |

**额外 hint 字段**（给 Agent 用，最终产物会清掉）：
- `_phase_hint`：阶段名（如"配置业务费率"），Agent 据此起 task_logical_name。
- `_boundary_source`：`flow`（操作流程切的）或 `agent_pending`（无操作流程，待 Agent 分组）。
- `_feature_id`：所属特性。

---

## 四、规则 vs Agent 的分工（一句话）

- **规则**（已实现）：定 task 边界（操作流程）、抽命令/参数名并构造实例键、标 reference_hint、填身份/来源字段。**可复现、不依赖命令图谱未完成资产**。
- **Agent**（待协同规划）：给 task 起可复用名（task_logical_name）、写意图（goal/summary）、把参数分 fixed/variable/reference、把 raw_steps_text 压缩成指令式、对"无操作流程"的 task 做语义分组。**Agent 输入会追溯到原始 md**（不只看骨架字段）。

---

## 五、当前验证状态

- **内容计费**（有操作流程）：跑通，5 task，边界 (1-2)/(3-5)/(6)/(7-8)/(9-11)，命令/参数/reference_hint 与手建样例一致。✅
- **27 个 pytest 全过**（覆盖每个规则步的核心逻辑）。
- **待验证泛化**：IPSec（多场景同骨架→应 1 task）、接入控制/eDRX（无操作流程→应 1 个 agent_pending candidate）。
- **待协同规划**：Agent 语义回填部分。
