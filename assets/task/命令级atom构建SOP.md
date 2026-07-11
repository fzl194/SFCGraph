# 命令级 Atom 构建 SOP（核心准则）

> 作用：指导 Agent 构建 `assets/task/{nf}/{version}/0-XXXXX.md`（命令级 atom task wiki）。
> 这是 feature(2-)/compound(1-) 之下的**最底层** task wiki 准则。
> 上游：原始命令 md（`output/{nf}_Product_Documentation_CH_{version}/OM参考/命令/...`）+ 各特性激活 md（`output/{nf}_Product_Documentation_CH_{version}/特性部署/...`）。
> 配套：`assets/task/特性步骤级构建SOP.md`（上层 SOP，§3.6 backbone 对齐、§4 模板）、`assets/task/特性task_wiki审视流程.md`（R1 审视）、`assets/CLAUDE.md`（§5 ID 规范、§7 自包含、§9 边界）、`assets/scripts/aggregate_command_summary.py`（汇总脚本）。

---

## 0. 定位与范围

- **本文规范**：单条 MML 命令（如 `ADD URR`）如何在 `assets/task/{nf}/{version}/0-XXXXX.md` 中写一份**命令配置方法字典**视角的 atom task wiki。
- **核心定位**：**atom = 命令的配置空间**（这命令有几种配置方法/参数维度，各自作用是什么）；**feature = 特性在配置空间里的取值点**（该特性下用哪种配法、具体取什么值）。**逐特性配置不放在 atom 里**，那属于 feature。
- **不重复**：命令静态知识（参数真相表、命令功能描述、规格 notes）写在 `assets/command/{nf}/{version}/{CMD}.md`，atom md 通过 wiki 链接引用。
- **核心价值**：配置生成器拿一份 atom md 就能知道"该命令有哪些合法的配置方法"，再结合所属 feature 的编排，就知道"该特性下用哪种配法、具体值"。

---

## 1. 三个产物

| 产物 | 路径 | 性质 | 是否资产 |
|---|---|---|---|
| **A. 汇总 md** | `assets/_intermediates/command-summary/{nf}/{version}/{CMD}.md` | **中间态数据**——Atom 构建脚本的输入，不入 wiki 引用，不入证据 | ❌ **非资产**（git 已 ignore） |
| **B. 命令 wiki** | `assets/command/{nf}/{version}/{CMD}.md` | 命令静态知识（功能/参数/规格/notes） | ✅ 资产 |
| **C. atom task md** | `assets/task/{nf}/{version}/0-XXXXX.md` | **本文规范的核心产物**——配置生成视角 | ✅ 资产 |

> **A 不是资产、不是证据、不被 wiki 引用**。它只是 Agent 写 C 时的"工作底稿"，生成 C 后可删可留。`source_evidence_ids` 必须指向 B（命令 wiki）或拷到 `assets/evidence/{nf}/{version}/` 下的特性激活证据，**不**指向 A。

---

## 2. 输入源（**主线：汇总 md + 原始命令 md**）

构建一条命令的 atom 时，**主线证据是 `assets/_intermediates/command-summary/` 下的汇总 md**（SOP §3 汇总脚本从原始产品文档扫出，含命令真相 + 各特性配置范式 + 差异汇总）。命令原始产品文档 md 是权威源（遇分歧以原始 md 为准）。

### 2.1 主线证据：汇总 md

| 类型 | 路径 | 覆盖 | 内容 |
|---|---|---|---|
| **汇总 md**（主线） | `assets/_intermediates/command-summary/{nf}/{ver}/{CMD}.md` | UDG 299 / UNC 686 = **985 命令**（有特性命中） | ①命令真相（来自 OM参考 原始命令 md）+ ②各特性的配置范式（数据规划行/任务示例/操作步骤上下文）+ ③配置方法差异汇总（自动派生参数取值分布） |
| **原始命令 md**（权威源） | UDG: `output/UDG_Product_Documentation_CH_{ver}/OM参考/命令/UDG MML命令/.../{中文}（{CMD}）_{id}.md`<br>UNC: `output/UNC {ver} 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/...` | **全量 11143 命令** | 命令真相权威源（功能/notes/参数表/使用实例）。**遇分歧以原始 md 为准**——汇总 md 是汇总脚本抽取结果，可能丢细节 |
| **特性激活 md**（可选） | UDG: `特性部署/特性指南/UDG特性指南/...`<br>UNC: `网络部署/特性部署/UNC特性指南/...` | 全量特性树 | 汇总脚本已基于此扫出汇总 md，**通常不需直接读**；仅在汇总 md 信息不足时回查（如某特性数据规划表行被汇总脚本误折叠） |

> **为何汇总 md 升为主线**：
> - ConfigTask 抽取的证据包仅覆盖 396 命令（3.6%），不全
> - 汇总脚本是 SOP §3 的产物，**从原始产品文档全量扫**（覆盖 985 命令有特性命中），每个汇总 md 自含"命令真相 + 特性配置范式 + 差异汇总"三段
> - 实战（批次 1+2 10 条 atom 重构验证）：汇总 md + 原始命令 md 双源并用最准

### 2.2 ConfigTask 证据包：仅作辅助参考

| 路径 | 用途 |
|---|---|
| `ConfigTask/assert/{nf}/{ver}/command-evidence/0-XXXXX.md`（UDG）<br>`ConfigTask/assert/{nf}/{ver}/command-evidence/{CMD}.md`（UNC） | **辅助**——若汇总 md 缺失或不完整时可参考（但 396 命令覆盖，且路径含只读区）。不作为主证据 |

### 2.3 构建决策树

```
给定命令 CMD：
1. 查 assets/_intermediates/command-summary/{nf}/{ver}/{CMD}.md 是否存在？
   ├─ 有（有特性命中）→ 汇总 md + 原始命令 md 并用重建 atom
   │       （汇总 md：命令真相 + 特性配置范式 + 差异汇总；原始 md：遇分歧时核对）
   └─ 无（0 特性命中，工程/查询命令）→ ↓
2. 仅原始命令 md 重建 atom，配置方法段照抄使用实例（精简版）

可选：参考 ConfigTask/assert/.../command-evidence/{CMD}.md（如存在，UDG 187 / UNC 209 覆盖）
```

### 2.4 路径差异（UDG vs UNC）

| 项 | UDG | UNC |
|---|---|---|
| 产品文档根 | `output/UDG_Product_Documentation_CH_{ver}/` | `output/UNC {ver} 产品文档(裸机容器) 05/` |
| 特性激活树（汇总脚本扫） | `特性部署/特性指南/UDG特性指南/` | `网络部署/特性部署/UNC特性指南/`（多一层 `网络部署/`，无中间 `特性指南`） |
| 汇总 md 输出路径 | `assets/_intermediates/command-summary/UDG/{ver}/` | `assets/_intermediates/command-summary/UNC/{ver}/` |

### 2.5 辅助资产

- `FeatureGraph/data/legacy/l1_*.csv` —— 特性清单（可选）
- `CommandGraph/data/.../mml_commands.jsonl` —— 命令清单 + 适用 NF（可选）
- `assets/task/{nf}/{version}/_numbering.json` —— 命令名→atom 编号映射，**必读**（去重 + 编号分配）

---

## 3. 汇总算法（生成**主线证据**汇总 md）

> **汇总 md 地位**：每条命令的 atom 构建**主线输入**（见 §2.1）。汇总脚本从原始产品文档扫，产出"命令真相 + 各特性配置范式 + 差异汇总"三段。无汇总 md 的命令走 §2.3 决策树第 2 步（仅原始 md 兜底）。

### 3.1 入口命令

```bash
# 单命令（缺汇总时补）
python assets/scripts/aggregate_command_summary.py \
  --nf UDG --version 20.15.2 --cmd "ADD URR"

# 全量发现（面向新建 atom，扫 OM参考/命令/{nf} MML命令/ 全量）
python assets/scripts/aggregate_command_summary.py --nf UDG --version 20.15.2 --all

# 仅已建 atom（对账/补建）
python assets/scripts/aggregate_command_summary.py --nf UDG --version 20.15.2 --numbering-only
```

输出默认到 `assets/_intermediates/command-summary/{nf}/{ver}/{CMD}.md`（git 已 ignore）。

### 3.2 算法伪代码

```
输入：nf, version, cmd (命令全名)
输出：汇总 md 写到 output_path

1. 定位 B（命令原始 md）
   - 搜 output/{nf}_Product_Documentation_CH_{version}/OM参考/命令/ 下匹配 *{cmd}* 的 md
   - 取功能描述、notes、参数真相表三段（不删改）

2. 扫 C'（特性激活 md 树）
   - rglob output/{nf}_Product_Documentation_CH_{version}/特性部署/特性指南/{nf}特性指南/ 下所有 *.md
   - 提取 feature_id：路径中匹配 (GWFD|WSFD|IPFD)-\d+ 的段
   - 跳过无 feature_id 的 md

3. 命中判定（任一即记入该特性）
   (a) 操作步骤中"**CMD**" 粗体引用
   (b) 数据规划表行: | **CMD** | 参数 | 取值 | 说明 |
   (c) 任务示例脚本: `CMD:...;` 或 `CMD ...;`
   (d) 段落中"通过**CMD**命令"/"使用**CMD**"——弱信号，仅作补充

4. 提取证据（每个命中特性）
   - 数据规划表行：按 (b) 抽取完整行
   - 任务示例脚本：按 (c) 抽取完整命令行
   - 操作步骤上下文：按 (a) 抽 ±2 行原文 + 行号（与 ConfigTask 一致）

5. 派生：③ 配置方法差异汇总
   - 扫所有特性的数据规划表行，统计每个参数列的取值分布
   - 输出表 | 参数 | 取值分布 |

6. 拼装汇总 md（4 段模板见 §3.3）
```

### 3.3 汇总 md 结构（A 中间态模板）

```markdown
# 命令配置方法汇总：{cmd} ({nf} {version})
> 命令名: {cmd} | 引用该命令的特性数: {N} | 扫描特性总数: {M}
> 原始命令 md: {B_path}
> 扫描覆盖: 特性部署/特性指南/{nf}特性指南/ 全树
> 工具: assets/scripts/aggregate_command_summary.py
> 生成时间: {ISO ts}

## ① 命令真相（来自 OM参考/{nf} MML命令/...）
{直接复制 B 的「功能」「notes」「参数真相表」三段，不删改}
- 适用 NF
- 功能描述
- notes（规格/上限/告警，**应投影为 atom rule**）
- 参数真相表

## ② 各特性的配置范式（来自特性部署）
### 特性 N: GWFD-XXXXX 特性名
**md: {path}**
- 数据规划表行（该命令的参数行）：
  | 命令 | 参数 | 取值 | 说明 |
  |---|---|---|---|
  | {cmd} | {param} | {value} | {note} |
- 任务示例脚本（该命令行）：
  ```
  CMD:...;
  ```
- 操作步骤上下文（±2 行原文 + 行号）：
  L{n}:
    > {原文}

### 特性 N+1: ...

## ③ 配置方法差异汇总（自动派生）
| 维度（参数列） | 取值分布 |
|---|---|
| USAGERPTMODE | OFFLINE x 5, ONLINE x 4, QOS x 1 |
| OFFMETERINGTYPE | VOLUME x 4, EVENT x 2, FREE x 1 |
| ... | ... |

## ④ 数据源
- 命令真相源: {B_path}
- 特性激活源: 特性部署/特性指南/{nf}特性指南/ 全树（rglob）
- 扫描时间: {ISO ts}
- 工具: assets/scripts/aggregate_command_summary.py
```

---

## 4. atom md 构建流程（生成 C 资产）

### 4.1 输入

- A 汇总 md（§3 产出）
- B 命令 wiki（已存在或新建）
- `_numbering.json`（已存在该命令编号则复用，否则分配新 0-XXXXX）
- 现有反向链接（查 _numbering.json 反查谁引用了该命令的 atom）

### 4.2 流程（证据三级分支）

```
0. 必读：OM参考 命令原始 md（命令真相权威源，所有级别都要读）
1. 定特性配置范式证据源（§2.2 决策树）：
   ① 查 ConfigTask/assert/{nf}/{ver}/command-evidence/ 有无该命令证据包？
      UDG: 0-XXXXX.md（编号）；UNC: {CMD}.md（命令名）
      ├─ 有 → 特性范式证据 = 证据包（atom yaml + DP/rule + 各特性配置范式 + 自动比对）
      │        ★ 证据包与原始命令 md 并用：遇分歧（参数细节/notes 完整度）以原始 md 为准
      └─ 无 → ↓
   ② 查 assets/_intermediates/command-summary/{nf}/{ver}/{CMD}.md 有无汇总？
      ├─ 有（有特性命中）→ 特性范式证据 = 汇总 md（跑过 --all 则已存在；否则单跑 --cmd）
      └─ 无（0 特性命中）→ 无特性范式证据，atom 精简（仅基于原始命令 md）
2. 准备 B：命令 wiki 必须存在（CLAUDE.md §5.5）；若缺，Compile 优先
3. 查 _numbering.json：
   - 已有 {cmd} → 编号 → 复用现有 atom md（如 0-00001.md），进入补强/审视
   - 无 {cmd} → 分配新 0-XXXXX（沿用 ConfigTask 编号，UNC pre-build 按命令名排序接续）
4. 起草 atom md（按 §5/§6/§7/§8 模板，原始命令 md + 特性范式证据共同填内容）
5. 拷证据（如需）：相关特性激活 md 拷到 assets/evidence/{nf}/{version}/{feature_id}/ 下
6. 双向链接：
   - atom → 命令 wiki、配置对象、配套 atom
   - atom → 被引用于（反向）：grep `task/{nf}/{version}/1-*.md` 与 `2-*.md` 找引用
7. 写 _numbering.json（如新增）
8. 更新 index.md
```

### 4.3 各证据源的 atom 填充要点

**① 证据包 + 原始命令 md 并用为主证据时**（396 命令）：
- 原始命令 md → 命令真相权威源（功能/notes/参数表/使用实例的完整版，填配置方法段命令真相部分）
- 证据包 atom yaml（task_intent/parameter_bindings）→ 填 frontmatter + 配置方法段参数列
- 证据包 DP yaml → 填决策点段（直接用 decision_id 编号）
- 证据包 rule yaml → 填约束段（直接用 rule_id 编号）
- 证据包各特性配置范式段 → 填配置方法段的多场景表格
- ★ 遇分歧（证据包抽取的参数说明/notes 截断 vs 原始 md 完整）**以原始命令 md 为准**

**② 汇总 md 为主证据时**（无证据包 + 多特性复用，约 589 命令）：
- ①命令真相 → 配置方法段（功能/notes/参数表）；notes 投影为约束
- ②各特性的配置范式 → 配置方法段的多场景表格（按计费轨道/参数变种分列）
- ③配置方法差异汇总 → 决策点段（DP）选项
- 数据规划行 → 参数列真实取值（不凭命令 wiki 默认值）

**③ 原始命令 md 为主证据时**（0 特性命中，约 10158 命令）：
- 功能/notes/参数表/使用实例 → atom 内容精简（配置方法段照抄使用实例）
- 这类命令多为工程/查询命令（SET LICENSESWITCH 除外，它是特例高频），atom 可简：
  - 配置方法段：照抄命令 md 的"使用实例"
  - 决策点段：通常无（命令用法单一）
  - 约束段：从 notes 投影

---

## 5. atom md frontmatter 规范（6 字段硬约束）

```yaml
---
id: {nf}@{version}@Task@{编号}        # 如 UDG@20.15.2@Task@0-00001
type: Task                              # 固定
task_layer: atom                        # 固定
task_logical_name: {配置对象}           # 必填！如"配置URR"（UNC 全量目前缺，必须补）
ref: {nf}@{version}@MMLCommand@{cmd}    # 如 UDG@20.15.2@MMLCommand@ADD URR
task_intent: {一句话描述命令干什么+该命令在不同特性下的核心变体}  # 必填，可含 DP 维度的关键枚举
status: draft                           # 仅 draft / active / stale 三值（CLAUDE.md §10）
---
```

| 字段 | 必填 | 规范 |
|---|---|---|
| `id` | ✅ | 严格 `{nf}@{version}@Task@{编号}`，与文件名 `{编号}.md` 一致 |
| `type` | ✅ | 固定 `Task` |
| `task_layer` | ✅ | 固定 `atom` |
| `task_logical_name` | ✅ | 中文短语，**不**含命令名（命令名已在 `ref` 字段）；如"配置URR"/"设置UP默认配额" |
| `ref` | ✅ | 严格 `{nf}@{version}@MMLCommand@{cmd 全名}`（命令名空格保留） |
| `task_intent` | ✅ | 1-2 句话，含"该命令干什么 + 该命令在不同特性下的核心变体维度"（变体维度对应 DP 选项） |
| `status` | ✅ | 仅 `draft`（人审过改 `active`，Lint 标记改 `stale`）；**禁**用 `inferred`/`evidence_only` 等自定义值 |

---

## 6. atom md 正文结构（5 章节硬约束）

```markdown
# {task_logical_name}（{cmd}）           # 命名规范：UDG 风格权威

> 命令静态知识见 [{cmd}](command/{nf}/{version}/{CMD-sanitized}.md)。本页只讲配置生成实例化时这条命令**怎么配**。

## 配置方法
（必填，结构见 §6.1）

## 决策点：{DP 名称}（DP 0-XXXXX）     # 编号化（§7）
（DP 表格，可多个 H2 段）

## 约束                                    # 编号化（§7）
（约束 bullet 列表）

## 关联                                    # 4 项硬性（§8）
（命令 wiki / 配置对象 / 配套组 atom / 被引用于 反向链接）

## （可选）其他
（如有版本差异、典型场景等）
```

### 6.1 配置方法段结构（**配置方法字典**，非逐特性配置表）

> **★ 核心定位**：本段展示**该命令有哪些合法的配置方法（配置维度 + 各取值 + 作用）**，**不**逐特性罗列"哪个特性配什么值"。具体特性怎么用这条命令是 feature wiki 的事。

```markdown
## 配置方法

{1-2 段叙述：命令做什么 + 它的核心配置维度有哪些}

### 配置维度 1：{维度名，如"上报模式"}（参数 {PARAM}）
| 取值 | 作用 | 配套必选参数 | 典型场景 |
|---|---|---|---|
| OFFLINE | 离线计费，话单上报 CG | OFFCOMPOUNDTYPE/OFFMETERINGTYPE/RG(+SID) | Ga 接口 |
| ONLINE | 在线计费，实时配额申请 | ONLCOMPOUNDTYPE/ONLMETERINGTYPE/ONLINERG(+ONLINESID) | Gy/N40 接口 |
| MONITORINGKEY | 流量累计监控（不产生费用） | MONITORINGKEY | FUP 策略控制 |
| QOS | QoS 保证标记 | 仅三参 | 业务触发 QoS |

### 配置维度 2：{维度名，如"统计类型"}（参数 OFF/ONLMETERINGTYPE）
| 取值 | 作用 | 适用上报模式 |
|---|---|---|
| VOLUME | 按流量统计 | OFFLINE/ONLINE |
| TIME | 按时长统计 | OFFLINE/ONLINE |
| EVENT | 按事件统计 | OFFLINE/ONLINE（典型防欺诈场景配 FREE） |
| FREE | 免费标记 | OFFLINE/ONLINE（防欺诈判断） |

### 配置维度 3：{维度名，如"费率标识组成类型"}（参数 {COMPOUNDTYPE}）
| 取值 | 作用 |
|---|---|
| ONLYRG | 仅用 RG 作为费率标识 |
| RGSID | RG + SID 二级费率标识 |

**步骤位置**：（在所属 feature 编排中通常是哪一步——只是定位说明，不展开多特性差异）
```

> **来源**：配置维度表从 **命令原始产品文档 md** 的参数表/notes 抽取（每个枚举值是一个"配置方法"），从 **证据包/汇总的 DP yaml** 归纳决策结构。**不**从各特性的数据规划表抽取值（那是 feature 的事）。
> 
> **为什么这样**：配置生成器看到 atom → 知道"ADD UURR 有 4 种上报模式 × N 种统计类型 × N 种费率标识 = 多个配置组合"；再看到 feature → 知道"内容计费特性选了 OFFLINE+VOLUME+ONLYRG 那个组合、URRID=12500"。两个层次清晰分工。

---

## 7. 决策点（DP）与约束（rule）编号化

### 7.1 DP 编号

- 格式：`## 决策点：{决策名}（DP 0-XXXXX）`
- **DP 编号独立流水**（与 atom 编号共用 0-XXXXX 段，但 DP 不进 _numbering.json，按 YAML 内嵌）
- DP 选项表：`| 选项 | 联动参数 | 适用场景 |`
- 无 DP 时写 `## 决策点\n（无。本命令在所有特性下用法一致，无分支。）`
- **禁**写"## 决策点（若有）"模糊标题——要么有 DP（命名具体），要么无 DP（显式说明）

### 7.2 rule 编号

- 格式：`- **{rule_name}**（{severity}，{rule_id}）：{约束} — {后果}`
- `{rule_id}` 格式：`rule-0-XXXXX`（与 DP 共用 0-XXXXX 段，按 UDG/UNC 已有 yaml 编号复用；UNC pre-build 无 yaml 时按现场编号）
- severity：`critical` / `warning` / `info`（与 SOP §5 已有规范一致）
- **禁**写 `severity=critical` 行内格式——必须编号化以便工具层 grep
- 已有 UDG yaml rule 编号示例：`**rule-0-00003**（critical）...`、`**rule-0-00110**（warning）...`

---

## 8. 关联段 4 项硬性

```markdown
## 关联
- 命令 wiki: [{cmd}](command/{nf}/{version}/{CMD-sanitized}.md)
- 配置对象: [{config_object}](configobject/{nf}/{version}/{object}.md)
- 配套组: [{atom-id-1}](task/{nf}/{version}/{编号}.md), [{atom-id-2}](...)
- 被引用于: [{compound-id-1}](task/{nf}/{version}/{1-XXXXX}.md), [{feature-id-1}](task/{nf}/{version}/{2-XXXXX}.md), ...
- 证据: [特性激活路径1](evidence/{nf}/{version}/{feature_id}/{filename}.md), ...
```

| 项 | 必有 | 备注 |
|---|---|---|
| 命令 wiki | ✅ | 必有；如命令 wiki 缺，先 Compile |
| 配置对象 | ✅ | 必有；至少一个 ConfigObject |
| 配套组 | ✅ | 列出该命令所在 backbone 的其他 atom（如 `ADD URR` 必列 `ADD URRGROUP`/`ADD PCCPOLICYGRP`） |
| 被引用于 | ✅ | **反向链接硬性**——grep `1-*.md` 与 `2-*.md` 中引用该 atom 的所有编号 |
| 证据 | ⚠️ | 仅在配置方法段引用了具体 evidence 时列出 |

---

## 9. 自检清单

构建完成前自检：

- [ ] frontmatter 7 字段齐（`task_logical_name`/`status: draft` 必填且规范）
- [ ] 主标题格式 `# {task_logical_name}（{cmd}）`
- [ ] 静态知识引命令 wiki（不重复命令真相表/参数表）
- [ ] 配置方法段是**配置方法字典**（按配置维度组织，每个维度列取值+作用），**不**逐特性罗列
- [ ] 决策点章节命名 `## 决策点：{名}（DP 0-XXXXX）`（无 DP 显式说明）
- [ ] 约束 bullet 格式 `- **{名}**（{severity}，{rule_id}）：{约束} — {后果}`
- [ ] 关联段 4 项硬性齐：命令 wiki + 配置对象 + 配套组 atom + **被引用于**
- [ ] 反向链接 grep 验证：`grep -l "task/{nf}/{version}/{编号}" assets/task/{nf}/{version}/[12]-*.md` 应非空
- [ ] _numbering.json 已写
- [ ] index.md 已更新（新增 atom 段）
- [ ] A 汇总 md 可保留（不删，下次重构可复用），但**不**被 source_evidence_ids 引用

---

## 10. 验收

- [ ] §9 自检清单全通过
- [ ] 一份 atom md 拿出来，人能直接看懂"该命令有哪些配置方法、各自作用是什么"（**不**问"特性下怎么配"——那是 feature）
- [ ] 配置生成器拿 atom md（配置方法字典）+ feature wiki（特性编排 + 具体取值），能产出对应特性下的合规 MML 脚本
- [ ] 反向链接完整：compound/feature 引 atom，atom 必反引
- [ ] 抽查 UDG/UNC 同名 atom（应字段一致、章节结构一致、DP/rule 编号机制一致）

---

## 11. 与已有 SOP 的关系

| 上游 SOP | 关系 |
|---|---|
| `特性步骤级构建SOP.md` §3.6 backbone | atom 配套组结构对齐 backbone |
| `特性步骤级构建SOP.md` §4 atom 模板（隐式） | 本文是该模板的**显式独立化**，并补充 DP/rule 编号化等 |
| `特性步骤级构建SOP.md` §5 决策点记录 | DP 表格格式一致 |
| `特性步骤级构建SOP.md` §6 硬约束 | "无证据不写"原则同样适用于 atom（用 A 汇总的 evidence 切片） |
| `特性task_wiki审视流程.md` R1.5 | atom 配置方法段的每个参数须有 A 汇总 evidence 支撑 |
| `assets/CLAUDE.md` §5 ID/文件名 | 7 字段 frontmatter、wiki 链接、task 编号 |
| `assets/CLAUDE.md` §7 自包含 | atom md 的 source_evidence_ids 指向 `evidence/`，不指 `output/`/`_intermediates/` |
| `assets/CLAUDE.md` §9 边界 | `assets/_intermediates/` 中间态（在本 SOP 范围下可写，不算破例） |

---

## 12. 待补

- [ ] `assets/scripts/aggregate_command_summary.py` 实际编写（§3 算法 + §3.3 模板）
- [ ] 工具入口 CLI：参数 `--nf/--version/--cmd/--output`，对单条命令生成汇总
- [ ] 工具批量模式：`--all` 扫 `_numbering.json` 全部 atom 对应命令
- [ ] UNC pre-build 场景：`_numbering.json` 无 yaml①，工具需从 mml_commands.jsonl + `command/{nf}/{version}/` 推导命令清单
- [ ] UNC 现有 212 个 atom 的 bulk 修复脚本（按 §5/§6/§7/§8 规范批量改）
- [ ] Lint 脚本：UDG/UNC 同名 atom 一致性检查（frontmatter/章节/DP/rule 编号机制）
