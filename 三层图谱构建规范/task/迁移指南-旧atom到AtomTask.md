# 迁移指南：旧 atom task → 新版 AtomTask

> **这是一次性迁移工程文档，不是 SOP。** SOP 讲"从0构建"，本文讲"把已建好的旧 atom 转成新格式"。两者无关。
> 目标读者：执行批量迁移的 Agent。读本文 + 附录映射表即可逐个迁移，无需读 SOP、无需读命令层/特性层资产、无需理解业务。

---

## 0. 任务定义

把旧版本命令级 task（**atom**，`assets/task/UDG/20.15.2/0-*.md`，共 **237** 个）转换成新版本 AtomTask md 格式。

- **纯格式转换**：不重新理解业务、不读命令层 md、不补内容。旧 atom 写了什么就转什么。
- **不用代码**：Agent 读旧文件、手写新文件。
- **范围**：只迁 atom（`0-` 前缀）。compound（`1-`）/ feature（`2-`）不在本批。
- **一对一**：237 个 atom 各有唯一**主命令名**（已验证无碰撞），新格式用命令名做文件名不会重名。
  > **聚合 atom**：个别 atom 是"聚合 atom"——1 个 atom 物理上合并了多条命令（如 `0-00147` 合并 SET BGP + ADD BGPVRF + ADD IMPORTROUTE），以**主命令**做文件名/ref，其余命令在正文标"待补"。按"只改格式不改内容"**原样保留聚合结构**，不拆分。

---

## 1. 输入 / 输出

| | 旧 | 新 |
|---|---|---|
| 路径 | `assets/task/UDG/20.15.2/0-00007.md` | `三层图谱资产/AtomTask/UDG/20.15.2/UDG@AtomTask@ADD FLOWFILTER.md` |
| 文件名 | 编号 `0-00007` | 完整 ID `UDG@AtomTask@ADD FLOWFILTER`（= 命令名锚）|
| 总数 | 237 | 237 |

**命令名从哪来**：旧文件 YAML 的 `ref` 字段末段。如 `ref: UDG@20.15.2@MMLCommand@ADD FLOWFILTER` → 命令名 = `ADD FLOWFILTER`。

> ⚠ 输出目录 `三层图谱资产/` 当前被 `.gitignore` 忽略（它是命令/特性层脚本构建产物目录）。迁移产物是否进 git、是否改放别处，**由用户定**（见文末"待用户确认"）。迁移本身不受影响——先按此路径产出。

---

## 2. 总原则（先记这三条）

1. **只改格式，不改内容**：配置方法字典 / 决策点 / 约束的业务内容**原样保留**。只动：ID 体系、引用形式、段落结构、删证据。
2. **编号全废（仅限三套）**：只删 atom `0-XXXXX`、`DP 0-XXXXX`、`rule-0-XXXXX` 这三套旧编号，改用命令名。
   - **不删 · 特性编号**：正文里的 feature 层引用（如 `GWFD-110311`、`110311`、`020354`、`IPFD-014001`）——这些标明"哪个特性用了这个配置范式"，是有用信息，**原样保留**。
   - **不删 · 规格数值/枚举值**：如 `100000`、`60s`、`TOS`、`URL` 等参数取值/规格，原样保留。
   - 一句话：只动带 `0-`/`DP 0-`/`rule-0-` 前缀的旧 task 编号，其余数字一律不动。
3. **三删**：删证据、删配置对象链接、删 Task↔Task / 被引用于编排链接。

---

## 3. YAML 字段转换

新 YAML 共 8 字段，固定顺序：

```
id / type / name / name_zh / nf / version / ref / status
```

| 旧字段 | → 新字段 | 规则 |
|---|---|---|
| `id: UDG@20.15.2@Task@0-00007` | `id: UDG@AtomTask@ADD FLOWFILTER` | 三段式 `{nf}@AtomTask@{命令}`，去 version、去编号 |
| `type: Task` | `type: AtomTask` | 改细分类型 |
| `task_layer: atom` | **删** | `type: AtomTask` 已隐含 |
| `task_logical_name: 配置流过滤器` | `name_zh: 配置流过滤器` | 改字段名，值不变（旧无则从 H1 `# {配置动作名}（{命令}）` 取配置动作名）|
| （旧无） | `name: ADD FLOWFILTER` | **新增**，= 命令名（= id 的 local 段）|
| `ref: UDG@20.15.2@MMLCommand@ADD FLOWFILTER` | `ref: UDG@MMLCommand@ADD FLOWFILTER` | 三段式，去 version |
| `nf: UDG` | `nf: UDG` | 原样 |
| `version: 20.15.2` | `version: 20.15.2` | 原样 |
| `status: draft` | `status: draft` | 原样 |
| `task_intent: ...` | **删** | 其内容若正文未覆盖，补一句进引子（见 §4.2）|
| `source_evidence_ids: [...]` | **删** | task 层无证据概念 |

---

## 4. 正文转换（逐段）

> **迁移只转旧 atom 已有的段，不补缺段**：旧 atom 没有 `## 决策点` 就不写决策点段（**不强补**"本命令无分支"）；没有 `## 约束` 就不写。缺段属 SOP 合规问题，不属迁移——迁移只做格式转换，不做内容补全。

### 4.1 H1
**原样保留**：`# 配置流过滤器（ADD FLOWFILTER）`

### 4.2 引子（H1 下的 blockquote）
- 命令层链接转双方括号：
  - 旧：`[ADD FLOWFILTER](command/UDG/20.15.2/ADD-FLOWFILTER.md)`
  - 新：`[[UDG@MMLCommand@ADD FLOWFILTER]]`
- 若旧 `task_intent` 含正文未覆盖的配置维度概述，补一句进引子；否则丢弃 `task_intent`。
- 其余引子文字原样。

### 4.3 `## 配置方法`（及 `### 配置维度 N` 子节）
**业务内容原样保留**。只把正文里出现的 markdown 链接按 §5 总表转换。代码块（` ``` ` 包裹的命令脚本）**不动**。

**纯文本里的旧编号注释要删**：正文常出现"命令名(编号)"形式的行内注释，如 `ADD BWMRULE(0-00037)`、`产出 BWMSERVICENAME 被 ADD BWMRULE(0-00037) 引用`。这里的 `(0-XXXXX)` 是旧 atom 编号注释，**删编号、留命令名** → `ADD BWMRULE`。
- 判定：括号内**含** `0-数字`（atom 编号）就把这段数字删掉，括号里其余文字保留。
  - `ADD BWMRULE(0-00037)` → `ADD BWMRULE`（括号只剩编号 → 整个括号删）
  - `ADD SNSSAIUPINTF（0-00285 切片绑逻辑接口）` → `ADD SNSSAIUPINTF（切片绑逻辑接口）`（删编号、留业务描述）
  - `（见 0-00032）` → 整括号删（只剩"见+编号"，无信息）
- 括号里**不含** `0-数字`（如 `（默认）`、`（critical）`、`（GWFD-110311）`、`（必选）`）**不动**。

> **与 §5 的边界**：本规则只管"括号内是**纯文本 `0-数字`**"。若括号内是 **markdown 链接**（含 `[...](...)`，如 `（[0-00032](task/...)）`），**不归本规则**——按 §5 转 `[[...]]`，外层中文括号保留。

### 4.4 `## 决策点`
- **去 DP 编号**：标题 `## 决策点：Tethering 检测开关（DP 0-00057）` → `## 决策点：Tethering 检测开关`（删 `（DP 0-XXXXX）`）。
- 正文里"DP 0-XXXXX"引用：删编号、留语义。
  - 例：`另存演进 DP 0-00019（FLOWFILTERTYPE 普通/EXTEROTTDB）` → `另存一个演进决策（FLOWFILTERTYPE 普通/EXTEROTTDB）`
  - 例：`仅在 DP 0-00019 标注` → `仅在决策点标注`
- 选项表内容原样保留。

### 4.5 `## 约束`
- **去 rule 编号 + 去来源标记**，只留 severity：
  - `（critical，rule-0-00123）` → `（critical）`
  - `（critical，隐含）` → `（critical）`
  - `（warning，rule-0-00334）` → `（warning）`
- 约束文本原样保留。

### 4.6 `## 关联` → `## 边`（整段重构）
旧 `## 关联` 段**整体拆解**，只保留"命令 wiki"一项转成边，其余全删：

> **优先级**：本段整段删**优先于** §5 单链接转换。关联段里不管链接形式是 `(task/.../X.md)`、裸相对路径 `(X.md)`、还是旧 wiki 占位 `[[UDG@20.15.2@...]]`，一律按本表整段拆解（只留命令 wiki 进 `## 边`），**不逐条转**。

| 旧关联项 | 处置 |
|---|---|
| `命令 wiki: [ADD FLOWFILTER](command/...)` | → `## 边` 的 `- 对应命令: [[UDG@MMLCommand@ADD FLOWFILTER]]` |
| `配置对象: [FLOWFILTER](configobject/...)` | **删**（atom 禁止指向 ConfigObject）|
| `配套组: [配置...](task/.../0-XXXXX.md)` | **删**（atom 不建 Task↔Task 边）|
| `被引用于: [1-00009](task/...)` / feature / CS | **删**（上层 compound/feature 迁移时重建）|
| `证据: [...](evidence/...)` | **删**（task 无证据）|

新文件末尾只剩：
```
## 边
- 对应命令: [[UDG@MMLCommand@ADD FLOWFILTER]]
```

**关于"配套组/被引用于"行的附加业务说明**：这些行常带括号说明（如"FILTERNAME/L7FILTERNAME 被引用"、"BWMCNAME 被引用于 UPBWMCTRLNAME1~4"）。**随整行删除，默认不抢救**。理由：① 编排依赖按新格式属 compound/feature 层，不进 atom；② 关键依赖通常已在正文（配置方法"铁律/步骤位置"段、约束段）叙述过，删了不丢；③ 迁移只转格式，不重新组织内容。
- 若迁移者认为某条附加说明含**正文完全未覆盖**的关键业务依赖，**可选**在 `## 边` 段后加一行 HTML 注释备查：`<!-- 迁移备注：原关联段提到 X，正文未覆盖，待人工判断 -->`。可选，不强制，不进正文语义。多数情况下直接删即可。

---

## 5. 正文引用转换总表（最关键，逐条对照）

正文中所有 markdown 相对路径链接，按下表转成双方括号逻辑 ID：

| 旧形式 | 新形式 | 说明 |
|---|---|---|
| `[ADD FLOWFILTER](command/UDG/20.15.2/ADD-FLOWFILTER.md)` | `[[UDG@MMLCommand@ADD FLOWFILTER]]` | 命令层链接，命令名直接取 |
| `[FLOWFILTER](configobject/UDG/20.15.2/FLOWFILTER.md)` | **删整条** | 配置对象，atom 不引 |
| `[配置流过滤器](task/UDG/20.15.2/0-00007.md)` | `[[UDG@AtomTask@ADD FLOWFILTER]]` | task 链接，**查附录映射**：0-00007→ADD FLOWFILTER |
| `[0-00037](task/UDG/20.15.2/0-00037.md)` | `[[UDG@AtomTask@ADD BWMRULE]]` | 显示文字是编号，**查附录映射** |
| `[ADD FLOWFILTER](task/.../0-00007.md)` | `[[UDG@AtomTask@ADD FLOWFILTER]]` | 显示文字=命令名，直接用命令名 |
| `[1-00009](task/.../1-00009.md)` / `[2-00001](task/...)` | **删链接**：显示文字是中文动作名→留纯文本；是裸编号→整条删 | compound(`1-`)/feature(`2-`) task 本批未迁，无法转 `[[...]]`；只在"被引用于"里的直接整条删（§4.6） |
| `[...](evidence/...)` | **删整条** | 证据 |

> **task 链接按编号前缀分流**：链接目标文件名以 `0-` 开头（atom）→ 转 `[[UDG@AtomTask@{命令}]]`（查附录A）；以 `1-`/`2-` 开头（compound/feature，本批未迁）→ 删链接。
>
> **链接形式多样**：旧文件链接可能是 `(task/UDG/20.15.2/0-00007.md)`、`(0-00007.md)` 裸相对路径、或下方 §5.1 的旧 wiki 占位。识别看**目标文件名/对象local 是否 `0-/1-/2-XXXXX`**，不只看 `task/` 前缀。

### 5.1 旧四段式 wiki 占位转换（重要）

旧 atom 正文里除了 markdown 相对路径，还可能用**旧四段式 wiki 占位** `[[UDG@20.15.2@{Type}@{local}]]`（带 version）引用对象。一律按下表处置：

| 旧 wiki 占位 | 新形式 | 说明 |
|---|---|---|
| `[[UDG@20.15.2@MMLCommand@ADD URR]]` | `[[UDG@MMLCommand@ADD URR]]` | 去 version 段 |
| `[[UDG@20.15.2@Task@0-00007]]` | `[[UDG@AtomTask@ADD FLOWFILTER]]` | 查附录A：0-00007→命令名 |
| `[[UDG@20.15.2@Feature@GWFD-110311]]` | `[[UDG@Feature@GWFD-110311]]` | 去 version 段（feature 引用保留）|
| `[[UDG@20.15.2@DecisionPoint@0-XXXXX]]` | **删占位**，周围文字保留语义 | DP 是 atom 内嵌对象，**不单独建 wiki**。如 `**[[UDG@20.15.2@DecisionPoint@0-00284]]**（single_choice，SD 是否带值）` → `（single_choice，SD 是否带值）` |
| `[[UDG@20.15.2@ConfigObject@XXX]]` | **删** | atom 不引 ConfigObject |

**通则**：旧 wiki 占位 `[[UDG@20.15.2@{Type}@{local}]]` → 去掉 `20.15.2@` 段；`Task` 类再按附录A换命令名锚；`DecisionPoint`/`ConfigObject` 类删占位。

**查表方法**：附录 A 给出全部 237 条 `编号→命令名`。也可现场读 `assets/task/UDG/20.15.2/{编号}.md` 的 `ref` 字段获取命令名。

**显示文字处理**：新 `[[逻辑ID]]` 没有 alias 语法。
- 旧显示文字是命令名或编号 → 转换后直接用 `[[...]]`，文字丢失无妨（逻辑 ID 含命令名）。
- 旧显示文字是中文动作名（如"配置流过滤器"）且对理解重要 → 写成 `配置流过滤器（[[UDG@AtomTask@ADD FLOWFILTER]]）`，保留中文 + 加引用。
- 旧显示文字是 feature 编号（如 `2-00001`）→ 见 §4.6，这类在"被引用于"里，**整条删**，不转。

---

## 6. 校验清单（每个 atom 迁移完自检）

- [ ] 输出路径 = `三层图谱资产/AtomTask/UDG/20.15.2/UDG@AtomTask@{命令}.md`
- [ ] YAML 8 字段齐全且顺序：id/type/name/name_zh/nf/version/ref/status
- [ ] `id` = `UDG@AtomTask@{命令}`，三段式，**无 version、无编号**
- [ ] `name` = 命令名；`name_zh` = H1 的配置动作名 = 旧 `task_logical_name`
- [ ] `ref` = `UDG@MMLCommand@{命令}`（三段式）
- [ ] 正文 5 段：H1 / 引子 / `## 配置方法` / `## 决策点` / `## 约束`
- [ ] **全文无 `DP 0-XXXXX` 残留**
- [ ] **全文无 `rule-0-XXXXX` 残留**
- [ ] **全文无 `0-XXXXX` 编号残留**（id、链接都已转命令名）
- [ ] **无 `source_evidence_ids` 字段、无 `## 证据` 段**
- [ ] **无 `configobject/` 链接**
- [ ] **无 `evidence/` 链接**
- [ ] **无 `task_layer` / `task_intent` / `task_logical_name` 旧字段**
- [ ] `## 边` 只有 `- 对应命令: [[UDG@MMLCommand@{命令}]]` 一行
- [ ] 所有引用是 `[[...]]` 双方括号，**无 markdown 相对路径** `[..](..md)` 残留

> 最快核验：迁移完后对产出文件搜 `0-`、`rule-`、`evidence`、`configobject`、`source_evidence`、`(command/`、`(task/`、`task_layer`、`task_intent`、`@20.15.2@`（旧四段式占位残留），应**全部零命中**。
>
> 注意：`0-` 指 atom 编号 `0-XXXXX`（**5 位数字**）。数值范围如 `0-9`、`0-63`、`0-255`（1~3 位）**不是**违规，勿误报——可用 `0-\d{5}` 精确匹配 atom 编号。
>
> **字母后缀豁免**：`0-XXXXX` 后接字母（如 `0-00147a`/`0-00147b`/`0-00147c`，CONVERGENCE-BACKLOG 演进规划占位）**不属删除范围，原样保留**（删了会破坏"拆分为三 atom"建议的指代）。自检 regex 用 `0-\d{5}(?![a-zA-Z0-9])`（后不跟字母数字）避免误报。

---

## 7. 完整范例（before → after）

**样本：`0-00007` ADD FLOWFILTER**（覆盖全部转换点：DP 编号 / rule 编号 / 跨命令引用 / 配置对象 / 配套组 / 被引用于 / 证据）。

### 7.1 旧文件（`assets/task/UDG/20.15.2/0-00007.md`）节选

```yaml
---
id: UDG@20.15.2@Task@0-00007
type: Task
task_layer: atom
task_logical_name: 配置流过滤器
ref: UDG@20.15.2@MMLCommand@ADD FLOWFILTER
task_intent: 配置 FLOWFILTER（聚合三四层/七层过滤条件的业务流过滤器）；按"流过滤器类型 × Tethering检测开关 × 命名约定" 3 维度组织配置空间
status: draft
source_evidence_ids:
- 增加流过滤器（ADD FLOWFILTER）_82837361.md
- GWFD-020301/部署UPF_28493406.md
- ...
---

# 配置流过滤器（ADD FLOWFILTER）

> 命令静态知识见 [ADD FLOWFILTER](command/UDG/20.15.2/ADD-FLOWFILTER.md)。本页只讲...

## 配置方法
...（维度 1/2/3 表格，正文里出现"仅在 DP 0-00019 标注"）...

## 决策点：Tethering 检测开关（DP 0-00057）
...
> 另存演进 DP 0-00019（FLOWFILTERTYPE 普通/EXTEROTTDB）...

## 约束
- **ADD FLOWFILTER 立即生效与记录数上限**（critical，rule-0-00123）：...
- **FLOWFILTERNAME 全网唯一**（critical，隐含）：...

## 关联
- 命令 wiki：[ADD FLOWFILTER](command/UDG/20.15.2/ADD-FLOWFILTER.md)
- 配置对象：[FLOWFILTER](configobject/UDG/20.15.2/FLOWFILTER.md)
- 配套组：[配置七层过滤器](task/UDG/20.15.2/0-00006.md)、...
- 被引用于：[1-00009](task/UDG/20.15.2/1-00009.md)；下游 feature [2-00001](...)、...
- 证据：[增加流过滤器...](evidence/UDG/20.15.2/...)、...
```

### 7.2 新文件（`三层图谱资产/AtomTask/UDG/20.15.2/UDG@AtomTask@ADD FLOWFILTER.md`）

```yaml
---
id: UDG@AtomTask@ADD FLOWFILTER
type: AtomTask
name: ADD FLOWFILTER
name_zh: 配置流过滤器
nf: UDG
version: 20.15.2
ref: UDG@MMLCommand@ADD FLOWFILTER
status: draft
---

# 配置流过滤器（ADD FLOWFILTER）

> 命令静态知识见 [[UDG@MMLCommand@ADD FLOWFILTER]]。本页只讲配置生成实例化时这条命令**怎么配**——按配置维度组织成"字典"，**不**逐特性罗列取值。

## 配置方法

（配置方法正文 + 维度 1/2/3 表格 **原样保留**；正文里的"仅在 DP 0-00019 标注"改为"仅在决策点标注"）

## 决策点：Tethering 检测开关

（选项表原样；底部 "> 另存演进 DP 0-00019（FLOWFILTERTYPE 普通/EXTEROTTDB）" 改为 "> 另存一个演进决策（FLOWFILTERTYPE 普通/EXTEROTTDB）"）

## 约束

- **ADD FLOWFILTER 立即生效与记录数上限**（critical）：执行后立即生效；FlowFilter 最大记录数 100000，超规格 90% 上报 ALM-135602215；FLOWFILTER 必须至少绑一个 filter 或 l7filter — 后果：...
- **FLOWFILTERNAME 全网唯一**（critical）：不同流过滤器之间 FLOWFILTERNAME 不能重复 — 后果：重复新增失败

## 边
- 对应命令: [[UDG@MMLCommand@ADD FLOWFILTER]]
```

**要点回顾**：
- 配置对象 `FLOWFILTER`、配套组 `0-00006 等`、被引用于 `1-00009/2-*`、证据 —— **全删**。
- 命令 wiki 链接 → `## 边` 的 `对应命令`。
- DP/rule 编号全去，severity 保留。
- `task_intent` 内容已被正文"## 配置方法"覆盖 → 丢弃，不补。

---

## 8. 批量执行建议

- **逐个迁移**：一个 atom 产出一个新 md。可多 Agent 并行认领不同编号段（如 Agent 甲迁 0-00001~0-00050，乙迁 0-00051~0-00100…）。
- **每个迁完跑 §6 校验清单**（尤其"禁词零命中"那行最快）。
- **附录 A 映射表**是跨命令引用反查的唯一依据，每个 Agent 手头备一份。
- 顺序无关（atom 之间在新格式里无 Task↔Task 边，互不依赖）。

---

## 9. 待用户确认（不影响迁移执行）

1. **输出位置 git 策略**：`三层图谱资产/` 当前 gitignore。迁移产物是否进 git？选项：(a) 为 `三层图谱资产/AtomTask/` 单独放行；(b) 整个 `三层图谱资产/` 放行；(c) 产物改放 `assets/` 体系下新目录。
2. **查询类 atom**（附录末尾 `DSP POOLUSAGE`/`LST POOL`/`EXP MML` 等）：旧体系也给它们建了 atom。本批仍按 237 全迁（只转格式）；是否保留属范围决策，不在本指南处理。

---

## 附录 A：编号 → 命令名映射表（237 条，atom 迁移引用反查用）

> 迁移正文里 `(task/.../{编号}.md)` 链接时，按此表把编号换成命令名，生成 `[[UDG@AtomTask@{命令}]]`。

```
0-00001 -> ADD URR              0-00002 -> ADD URRGROUP         0-00003 -> ADD PCCPOLICYGRP
0-00004 -> ADD FILTER           0-00005 -> ADD FILTERIPV6       0-00006 -> ADD L7FILTER
0-00007 -> ADD FLOWFILTER       0-00008 -> ADD FLTBINDFLOWF     0-00009 -> ADD PROTBINDFLOWF
0-00010 -> ADD RULE             0-00011 -> ADD USERPROFILE      0-00012 -> ADD RULEBINDING
0-00013 -> SET URRGRPBINDING    0-00014 -> ADD SPECURRGRPLIST   0-00015 -> SET REFRESHSRV
0-00016 -> SET UPDEFAULTQUOTA   0-00017 -> SET UPGLBCHGPARA     0-00018 -> SET URRFAILACTION
0-00019 -> SET LICENSESWITCH    0-00020 -> ADD APN              0-00021 -> ADD ABNTRAFFICDT
0-00022 -> ADD EXTENDEDFILTER   0-00023 -> ADD REDIRAPPENDINFO  0-00024 -> SET GYONESHOT
0-00027 -> LOD SIGNATUREDB      0-00028 -> ADD PCCACTIONPROP    0-00029 -> ADD SERVICEPROP
0-00030 -> ADD SRVPBINDPCCPG    0-00031 -> ADD ADCPARA          0-00032 -> ADD CATEGORYPROP
0-00033 -> ADD BWMUSERGROUP     0-00034 -> ADD BWMSERVICE       0-00035 -> ADD APNBINDBWMUSRG
0-00036 -> ADD BWMCONTROLLER    0-00037 -> ADD BWMRULE          0-00038 -> ADD QOSPROP
0-00039 -> ADD WELLKNOWNPORT    0-00040 -> ADD SADEDICBEARER    0-00041 -> ADD VPNINST
0-00042 -> ADD POOLGROUP        0-00043 -> ADD POOL             0-00044 -> ADD SECTION
0-00045 -> ADD POOLBINDGROUP    0-00046 -> SET APNADDRESSATTR   0-00047 -> ADD POOLGRPMAP
0-00048 -> STR PDNROUTETST      0-00049 -> SET APNQOSATTR       0-00050 -> SET APNACCESSWAL
0-00051 -> SET UPGTPPATH        0-00052 -> SET UPN4UPATH        0-00053 -> SET UPPFCPPATH
0-00054 -> ADD ECHOIPLIST       0-00055 -> ADD REDUNDRDTIP      0-00056 -> ADD INTERFACE
0-00057 -> ADD IPBINDVPN        0-00058 -> ADD IFIPV4ADDRESS    0-00059 -> ADD GRETUNNEL
0-00060 -> SET IFIPV6ENABLE     0-00061 -> ADD IFIPV6ADDRESS    0-00062 -> ADD SRROUTE
0-00063 -> ADD SRROUTE6         0-00064 -> SET REDUNDUSER       0-00065 -> SET SRVCOMMONPARA
0-00066 -> ADD QOSDIFFERSERV    0-00067 -> SET QOSBA            0-00068 -> ADD QOSIFTRUST
0-00069 -> SET QOSPHB           0-00070 -> SET QOSCAR           0-00071 -> ADD L3VPNINST
0-00072 -> ADD VPNINSTAF        0-00073 -> SET BFD              0-00074 -> ADD OSPF
0-00075 -> ADD OSPFAREA         0-00076 -> ADD OSPFNETWORK      0-00077 -> ADD OSPFIMPORTROUTE
0-00078 -> ADD OSPFV3           0-00079 -> ADD OSPFV3AREA       0-00080 -> ADD OSPFV3IMPORTROUTE
0-00082 -> ADD BFDSESSION       0-00083 -> ADD LOGICINF         0-00084 -> SET DDOS
0-00085 -> SET IOTCAPABILITY    0-00086 -> SET IPFARMGLOBAL     0-00087 -> ADD IPFARM
0-00088 -> ADD IPFARMSERVER     0-00089 -> ADD ERRORCODE        0-00090 -> ADD DNSOVERWRITING
0-00091 -> ADD SMARTHTTPREDIR   0-00092 -> LOD EXTERNALDB       0-00093 -> SET EXTOTTMATCHSW
0-00106 -> SET BANDWIDTHMNG     0-00107 -> SET APNOSLELBWMSW    0-00108 -> ADD BCSRVLEVELPLY
0-00109 -> SET FPIFUNC         0-00110 -> SET APNREPORTATTR    0-00111 -> ADD ROUTEPOLICY
0-00112 -> ADD ROUTEPOLICYNODE 0-00113 -> ADD MATCHROUTETYPE   0-00114 -> MOD INTERFACE
0-00115 -> ADD ETHSUBIF        0-00116 -> ADD IPV6PATHMTU      0-00117 -> ADD OSPFV3INTERFACE
0-00131 -> SET GLOBALL2TP      0-00132 -> SET APNL2TPATTR      0-00133 -> ADD L2TPGROUP
0-00134 -> ADD L2TPRDSCLIENT   0-00135 -> ADD L2TPCLIENTIP     0-00137 -> SET SOFTPARAOFBIT
0-00138 -> SET PPPCFG          0-00139 -> SET APNPPPACCESS     0-00140 -> SET L2TPN4KEY
0-00141 -> ADD AUTOSCALINGSERVICE  0-00142 -> ADD AUTOSCALINGSRROUTE  0-00143 -> ADD AUTOSCALINGBFD
0-00144 -> ADD AUTOSCALINGSRBFD 0-00145 -> MOD VPNINSTAF       0-00146 -> ADD VPNTARGET
0-00147 -> SET BGP             0-00149 -> SET APNHTTP2DGRD     0-00150 -> MOD PCCPOLICYGRP
0-00151 -> ADD HOST            0-00152 -> LOD PARSERDB         0-00153 -> ADD USRRELATEIDEN
0-00154 -> SET SACOMMONPARA    0-00155 -> ADD APNIMSSIGFLTR    0-00156 -> SET APNIMSATTR
0-00171 -> SET FASTRECOVERY    0-00172 -> SET GLBDLBUFTIME     0-00173 -> SET GLBDLLTBUFFER
0-00174 -> SET APNDLBUFTIME    0-00175 -> SET APNDLLTBUFFER    0-00177 -> SET APNNONIPFUNC
0-00178 -> MOD GRETUNNEL       0-00197 -> ADD ACLGROUP         0-00198 -> ADD ACLRULEADV4
0-00199 -> ADD MQCBEHAVIOR     0-00200 -> ADD QOSACTRDRNHP      0-00201 -> ADD MQCCLASSIFIER
0-00202 -> ADD QOSRULEACL      0-00203 -> ADD MQCPOLICY         0-00204 -> ADD QOSAPPLICATION
0-00207 -> ADD ACLRULEBAS4     0-00208 -> ADD ACLRULEETH        0-00209 -> ADD ACLGROUP6
0-00210 -> ADD L3VPNINSTIPSEC  0-00211 -> ADD ACLGROUPIPSEC     0-00212 -> ADD IPSECPROPOSALIPSEC
0-00213 -> ADD IKEPROPOSAL     0-00214 -> ADD IKEPEER           0-00215 -> ADD IPSECPOLICY
0-00216 -> ADD IPSECINTFCFG    0-00217 -> SET IKEGLOBALCONFIG   0-00218 -> SET PFCPLOADRPT
0-00219 -> SET CPTEIDUALOC     0-00220 -> SET SESSCHKFUNC       0-00222 -> SET APNFLOWMAXNUM
0-00224 -> ADD TWAMPVPNINST    0-00225 -> ADD TWAMPLOGICINF     0-00226 -> ADD TWAMPRESPONDER
0-00227 -> ADD TWAMPCLIENT     0-00228 -> ADD TWAMPSENDER       0-00229 -> SET TCPKEEPALIVECFG
0-00230 -> SET LINKALMCFG      0-00231 -> ADD IPSQMSHAPING      0-00232 -> SET IPSQMQDEPTH
0-00233 -> SET IPSQMADJUST     0-00234 -> ADD IPSQMVIPLIST      0-00248 -> ADD NTPSVR
0-00249 -> SET DATAPLANEINFMODE 0-00250 -> SET IPALLOCRULE      0-00251 -> SET APNCFFUNC
0-00252 -> ADD CFPROFILE       0-00253 -> ADD CFTEMPLATE        0-00254 -> SET APNCFTEMPLATE
0-00255 -> ADD CFPROFBINDCFT   0-00256 -> ADD CONTCATEGROUP     0-00257 -> ADD CONTCATEGBIND
0-00258 -> SET CFCACHEPARA     0-00259 -> ADD ICAPSERVER        0-00260 -> ADD ICAPSVRGRP
0-00261 -> ADD ICAPSVRBINDISG  0-00262 -> ADD ICAPLOCALINFO     0-00279 -> SET FLOWLETPARA
0-00280 -> SET NETYPE          0-00281 -> ADD FINGERIDENT       0-00282 -> SET IMSBYPASS
0-00283 -> SET RTSDNNPARA      0-00284 -> ADD SNSSAI            0-00285 -> ADD SNSSAIUPINTF
0-00286 -> ADD SNSSAIBWMUSRG   0-00287 -> ADD TIMERANGE         0-00288 -> ADD PERITIMERANGE
0-00289 -> ADD BWMRULEGLOBAL   0-00290 -> SET SPECTRAFURRGRP    0-00291 -> ADD HEADEN
0-00292 -> ADD TLSHEADEN       0-00293 -> ADD BLACKLISTRULE     0-00294 -> ADD FLOWFILTERGRP
0-00295 -> SET ABNTRADTTHR     0-00296 -> MOD USERPROFILE       0-00297 -> SET UPGLBPMPARA
0-00298 -> ADD ACLRULEADV4IPSEC 0-00299 -> ADD ADRLOCWHITELST   0-00300 -> ADD ATTACHIKEPEER
0-00301 -> ADD CONFLICTIP      0-00302 -> ADD CONFLICTIPV6      0-00303 -> ADD CPNODEID
0-00304 -> ADD IFIPV4ADDRESSIPSEC 0-00305 -> ADD INTERFACEIPSEC 0-00306 -> ADD IPBINDVPNIPSEC
0-00307 -> ADD IPSECINTFCFGIPSEC 0-00308 -> ADD IPSECPROPOSAL  0-00309 -> ADD L2TPLNSINFO
0-00310 -> ADD LACGROUP        0-00311 -> ADD LACID            0-00312 -> ADD N2TACID
0-00313 -> ADD OSPFINTERFACE   0-00314 -> ADD PROPATTACHIPSECPROPOSAL  0-00315 -> ADD S1TACID
0-00316 -> ADD TACGROUP        0-00317 -> ADD VPNINSTAFIPSEC    0-00318 -> SET ADDRESSATTR
0-00319 -> SET APNIPALLOCRULE  0-00320 -> SET APNREDUNDUPSW     0-00321 -> SET IPALLOCBYLOCGLBSW
0-00322 -> SET IPALLOCBYLOCSW  0-00323 -> SET IPALLOCBYSMFGLBSW 0-00324 -> SET IPALLOCBYSMFSW
0-00325 -> DSP POOLUSAGE       0-00326 -> DSP SECTIONUSAGE      0-00327 -> DSP SESSIONINFO
0-00328 -> LST POOL            0-00329 -> LST POOLGROUP         0-00330 -> LST APN
0-00331 -> LST VPNINST         0-00332 -> LST CPNODEID          0-00333 -> EXP MML
```

（如需机器可读副本：每个 atom 的命令名 = 其源文件 YAML `ref` 字段的末段，可由 `assets/task/UDG/20.15.2/0-*.md` 现场读出。）
