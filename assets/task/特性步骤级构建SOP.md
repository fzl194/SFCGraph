# 特性/步骤级 Task Wiki 构建SOP（核心准则）

> 作用：指导 Agent 在 `assets/task/` 下**逐特性**构建 `feature(2-) → compound(1-) → atom(0-)` 三层 task wiki。
> 这是命令级 atom wiki（187+）之上的**特性级/步骤级**构建准则。
> 首个完整范本：**GWFD-110311**（`2-00001` + `1-00001~1-00006` + `0-00284~0-00289`）。
> 配套：`assets/CLAUDE.md`（总维护准则，§5.7 task编号检索）、`assets/task/UDG/20.15.2/index.md`（compound 复用库 + 全景）。

---

## 0. 产物层级与定位

| 层 | 编号 | 回答的问题 | ref 指向 |
|---|---|---|---|
| **feature (2-)** | `2-00001~` | 这个特性**怎么配**（编排哪些步骤、多种场景如何选） | `Feature` |
| **compound (1-)** | `1-00001~` | 这个业务**步骤**怎么配（多命令组合，**可跨特性复用**） | `null` |
| **atom (0-)** | `0-00001~` | 这条**命令**怎么配（叶子） | `MMLCommand` |

关系链：`feature →(编排)→ 步骤 →(ref)→ MMLCommand`，其中**步骤 = compound（多命令可复用模块）或 atom（单命令）**。

**编排原则**：feature 由若干"步骤"组成——多命令的可复用小模块 → 建 **compound** 承载（便于跨特性复用，如过滤链、计费三件套、BWM 控制器族）；单命令步骤 → **直接复用 atom**。即 **feature 可直接含 atom，compound 仅为"可复用多命令模块"而建，不是 feature→atom 的必经层**。

---

## 1. 编号（遵守 CLAUDE.md §5.7）

- task wiki **用编号命名**（不用命令名）：文件名 `{编号}.md`，id `{nf}@{version}@Task@{编号}`（atom `0-`/compound `1-`/feature `2-`）。
- `assets/task/` 独立编号，不接 ConfigTask。feature `2-00001~`、compound `1-00001~` 按顺序自增。
- **atom 编号**：沿用 ConfigTask assert yaml 编号（权威，`_numbering.json` 为准）；atom 不全时，未建部分按命令名排序接续（见 `assets/scripts/renumber_unc_tasks.py`）。**UDG 现场手动补建**沿用已分配编号（`_numbering.json` 为准，不必严格命令名排序）；批量 renumber 场景（如 UNC pre-build）才按命令名排序接续。
- **`_numbering.json`**（每个 `task/{nf}/{version}/` 下）：`{命令名→atom编号}` 映射，是命令级 task 的**快速检索表**。compound/feature 引用某命令的 atom 时查此表拿编号 → 写 `[cmd](task/{nf}/{version}/{编号}.md)`，无需扫文件。
- feature/compound **不建映射表**（按顺序自增即可；atom 需要表是因为命令名是稳定锚）。

---

## 2. 单特性构建流程（一次 pass）

**输入**：`feature_code` → `FeatureGraph/data/legacy/UDG_feature_files.csv` 映射 → 原始 md 清单（主源 = 「激活/部署」md，含数据规划表 + 任务示例脚本；辅源 = 概述/原理/调测）。

```
0. 收集资产
   - 原始 md 清单（CSV 按 feature_id 过滤）
   - 已有特性知识 md（业务图谱体系/{场景}/feature-knowledge/，仅参考）
   - 该特性涉及的已有 atom（查 _numbering.json 拿命令→编号）
1. 理解特性：核心对象模型 + 通用配置流程 + 多配置方法(场景)的差异维度
   ★ 以原始产品文档「操作步骤」章节为准（非凝练版特性知识 md）
2. 补缺失 atom：特性用到但无 atom 的命令 → 补建（读命令 wiki + 证据，编号按§1，写入 _numbering.json）
3. 设计 compound 拆分（核心，§3 复用优先 + §3.5 存在前提）：
   - 通用骨架 compound（所有场景共享，带「场景差异」小节）
   - 多命令特化 compound（按场景挂）
   - 单命令+参数增量 → 不建 compound（§3.5）
   - 每个候选 compound 先查复用库（§3），能复用的引用不新建
4. 建 compound wiki（模板 §4）
5. 建 feature wiki：编排 compound + 特性级 DP 场景影响表（§5，必全）
6. 拷证据：激活方法 md → assets/evidence/UDG/20.15.2/（自包含，§6）
7. 双向链接回填（§6）：atom 回指 compound/feature；被复用 compound 的"被引用于"追加本 feature
8. 更新 index.md（compound 复用库 + feature/atom 段）+ _numbering.json（新 atom 入表）
```

---

## 3. compound 复用机制（★核心★）

compound 是**可跨特性复用的步骤**。后续特性的很多步骤（前置 License、过滤链、刷新生效、各种"三件套"）已在前面特性建过——**必须先查复用库，能复用的引用不新建**。

### 3.1 复用层级

| 层级 | 复用范围 | 示例（GWFD-110311 范本） |
|---|---|---|
| **全通用** | 跨一切特性 | License 前置、刷新生效（SET REFRESHSRV） |
| **域通用** | 业务域内多特性 | 过滤链（L7FILTER→FLOWFILTER→PROTBINDFLOWF）、BWM 控制器族、计费三件套 |
| **特性专属** | 单特性 | 切片绑定、时间段控制 |

### 3.2 复用判定（建 compound 前必查）

对每个候选步骤：
1. **扫 index.md 的 compound 复用库段**，按命令集签名找候选。
2. **双闸判定**（沿用 ConfigTask SKILL §7.1）：
   - 命令集 Jaccard ≥ 0.75 **且** 相位/用途同义 → **复用**（feature 编排链接已有 compound，不新建）
   - 0.4–0.75 或相位近义 → **reference**（新建，但共享子 atom）
   - < 0.4 或相位不同 → **新建**
3. 复用时：feature 编排链接已有 compound；**该 compound 关联节"被引用于"追加本 feature**（双向）。

### 3.3 compound 归属语义（重要）

- compound 关联节写 **"被引用于：[feature 集合]"**，**不是**"归属 feature"。
- 通用/域通用 compound 被**多 feature 引用是常态**；特性专属 compound 当前只被 1 feature 引用，后续若被复用则追加。
- 范本注：GWFD-110311 的 compound（`1-00001~1-00006`）当前"被引用于"= {2-00001}。后续带宽其他特性构建时，`1-00002`/`1-00003` 等会被复用，届时追加。

### 3.4 复用库（index.md compound 段）

每个 compound 条目含：`编号 · 名称 — cmd:命令集签名 | 用于:feature列表 | 层级`。建 feature 前先查此段。

### 3.5 compound 存在前提（★可复用多命令模块★）

**compound = 可复用的多命令小模块**。它是"模块化复用单元"，**不是 feature→atom 的必经层**：

| 步骤性质 | 处理 |
|---|---|
| 多命令组合 + 可跨特性复用（过滤链/计费三件套/BWM控制器族/PCC链/切片链） | ✅ 建 compound（复用价值高，跨特性共享） |
| **单命令步骤** | 直接复用 atom，feature 编排直接引（不必建 compound） |
| 多命令但仅本特性、无复用价值 | 视复杂度：阶段内聚明显→建 compound；否则 feature 直接编排其 atom |

> **单命令步骤的参数增量**（如分级场景的 SRVLEVELSPEC/SERVICELEVEL/USERGLEVRULESW）虽不建 compound，须在 feature DP 影响表 + 通用骨架 compound 的「场景差异」小节**详尽记录**。
>
> **判定依据追溯原始产品文档「操作步骤」章节**：看每步是"多命令可复用模块"还是"单命令"。**单命令直接用 atom 是正常编排（非例外）**。
>
> 范本：GWFD-110311 的 compound（`1-00001~06`）都是多命令可复用模块；分级(BCSRVLEVELPLY)/三级(BWMRULEGLOBAL)是单命令步骤，feature 直接引 atom（`0-00108`/`0-00289`），参数增量记 DP 表 + 场景差异。（初版误把这俩单命令建成 compound 已纠正。）

> **★ 复用差异双向回填（硬约束，防假通用）**：feature 复用某 compound 时，若该 feature 引入了 compound「场景差异」**未记录**的差异维度（参数变种/专属命令/组装方式/约束），**必须**将该差异**同步追加到 compound 场景差异**，不能只写进 feature DP。否则 compound 对多特性是"假通用"——命令集覆盖但差异抹平，复用者点开 compound 看不到特性差异。
>
> **判定**：逐 feature 核对——feature 有的核心差异维度，compound 场景差异是否有对应条目？无 → 假通用（须补 compound）。
>
> 实战教训（计费族）：7 特性复用 1-00010 计费三件套，但融合双URR/RGAPPLIED、离线 OFFMETERINGTYPE 8 种、METERINGTYPE 三变种（VOLUME/DURATION/EVENT）只写进各 feature DP，1-00010 场景差异仅 3 条泛化项 → 假通用。审视见 `特性task_wiki审视流程.md` R1.2。
>
> **★ 族通用 compound 的"命令多带"陷阱（2026-07-10 QoS 族实战）**：族通用 compound 命令集是族内多特性**并集**，个别 feature 只用子集（如 1-00017 QoS专有承载链=QOSPROP+SADEDICBEARER，但 2-00030 视频承载仅 QOSPROP 无 SADEDICBEARER）。**配置生成按 compound 典型脚本盲目套用会误产出 feature 不用的命令**。防法（构建侧）：① compound 场景差异表**逐 feature 列命令子集**（执行哪些/省略哪些 + 参数变种），不并集泛化；② compound 加★复用警示「勿按典型脚本盲目套用 X 场景，X 场景不执行 Y 段」；③ feature 配置流程复用 compound 时，对省略的段加脚注「本特性不执行 compound 的 Y 段」。审视侧见 R1.2 第 5 条。

> **★ 防平铺：跨特性复用预判（2026-07-11 APN 域实战教训）**：建 feature 时若某步骤是"多命令阶段模块"（≥3 条命令、阶段内聚明显），**必须预判跨特性复用潜力**——即便当前只 1 个 feature 用，只要同族/同域其他特性（含待建）也会用，就**先抽 compound 再建 feature**。禁止把多命令阶段模块直接平铺成 feature 内的 atom 列表。
>
> **典型平铺反例（APN 域首批，已记债）**：
> - **"APN 接入域基础设施"**（`ADD L3VPNINST`+`ADD VPNINSTAF`+`ADD VPNINST`+`ADD APN`+`SET APNADDRESSATTR`）在 6 个地址分配特性里**全部平铺重复**——应抽 1 个共享 compound。
> - **"主备 UDG + GRE 隧道冗余保护"**（`ADD REDUNDRDTIP`+`ADD INTERFACE`+`ADD IPBINDVPN`+`ADD GRETUNNEL`+`ADD SRROUTE`+`MOD OSPFIMPORTROUTE COST`+`SET REDUNDUSER`，2-00038 步骤 7-14 共 8 步）整段平铺——应抽 1-2 个可靠性 compound，未来其他可靠性场景可复用。
>
> **判定流程**（建 feature 前对每个多命令步骤走一遍）：
> 1. 该步骤是否 ≥3 条命令且阶段内聚？→ 否 → 直接引 atom（合法）
> 2. 该步骤是否会被同族/同域≥2 个特性用到（含待建）？→ 是 → **必须抽 compound**
> 3. 该步骤是否是"配置生成关键阶段"（如接入域基础设施、可靠性体系、路由发布）？→ 是 → **必须抽 compound**
> 4. 命令集与已有 compound 重合 ≥0.75 且相位同义？→ 是 → 复用（不新建，双向回填）
>
> **防平铺自检**：feature 配置流程里若出现连续 ≥3 个 atom 引用且无 compound 承载，**强制停手评估抽 compound**。

### 3.6 跨域通用 compound 对齐 ConfigTask backbone（★）

跨域通用 compound（多特性复用）的**划分/命名/边界**必须**对齐 ConfigTask 已验证的 backbone**，不要自己发明：

| assets/task compound | 对齐 ConfigTask backbone | 命令集 |
|---|---|---|
| 计费三件套 | 1-00001 | URR+URRGROUP+PCCPOLICYGRP |
| 过滤链 | 1-00002 | FILTER+FILTERIPV6+L7FILTER+FLOWFILTER+FLTBINDFLOWF+PROTBINDFLOWF（全集，DP 驱动子集） |
| 规则与用户模板绑定 | 1-00003 | RULE+USERPROFILE+RULEBINDING |
| 收尾 | 1-00004 | SPECURRGRPLIST+REFRESHSRV+URRGRPBINDING |

> **UNC 族复用模式（2026-07-10 实战）**：UNC 计费族 `1-00001~04`（离线骨架：OFCTemplate 模板参数 + 3 绑定层次）→ 热计费复用（参数变种）/ 融合新建 `1-00005~11`（CCT/CHF/Trigger/费率链/异常/缓存专属）/ 内容复用费率链 `1-00009`；PCC 族 `1-00012~14`（PCRF对接/选择/开关）跨计费+带宽复用。带宽族 ADC `1-00015/16` + QoS `1-00017`（**reference 1-00009 非复用**，PCCPOLICYGRP 语义不同：计费绑 URRGROUP vs QoS 绑 QOSPROP）+ BWM `1-00018` + 位置链 `1-00019` 各专属。纯被动型特性（接入点策略/小区负荷）无新建 compound，仅 License + 引 PCC。
>
> **UNC vs UDG C/U 分工经验**：UNC=控制面中转（BWM/小区负荷/接入点策略等仅 License + 规则承载 + 透传，**不执行限速**；限速在 UDG/PGW-U），UDG=用户面执行。建 UNC 特性时**勿照搬 UDG 范本**（UDG BWM 9场景/BWM 控制器族 vs UNC BWM 仅规则承载 POLICYTYPE=BWM）——两侧命令族不同，UNC 常是轻量中转。

> ConfigTask backbone 是计费场景验证、8-9 特性复用的成熟拆法。assets/task 建 compound 时**先查 `ConfigTask/assert/{nf}/{ver}/canonical-compounds.md`**，能对齐的对齐（命名/边界一致），只对特性专属部分（如 BWM 控制器族、URL过滤 ICAP/CF 链）新建。
>
> 范本教训：GWFD-110311 的 `1-00004`（PCC链）混了过滤链(L7部分)+规则绑定(RULE)，没对齐 backbone，后续优化。URL过滤已对齐（`1-00009`过滤链/`1-00010`计费三件套/`1-00011`规则绑定）。

### 3.7 能力型底座特性范式（★APN 域实战，2026-07-11 GWFD-010101 会话管理首建）

**判定**：当一个特性具备以下所有特征时，属"**能力型底座特性**"——
1. 原始文档**无 MML 命令清单、无参考信息、无激活步骤、无调测文档**（16 文件全是特性概述+实现原理）
2. 特性概述明确"**本特性无需配置即可使用**"或"**无需 License**"
3. 网元在该特性中扮演**被动响应角色**（如 UPF 接收 SMF 的 PFCP 信令执行转发，不发起会话管理）
4. "配置生成"在该特性上**无内容可生成**——无命令、无参数、无场景差异

**处置（骨架占位）**：
- **建 1 个 feature (2-XXXXX)**，`status: foundation`（区别于 `draft` 标识骨架类型）；front matter `task_intent` 显式标 "**本特性无独立配置，靠被依赖特性配置完成能力启用**"
- **建 1~N 个骨架 compound (1-XXXXX)**，每个对应**一个被依赖特性维度**（如"会话建立→地址分配依赖"指向 GWFD-010105；"会话建立→PCC 策略依赖"指向 GWFD-020351；"会话建立→N4 接口依赖"指向 GWFD-010224），**这些 compound 的"配置方法"段直接描述依赖关系而非本步骤的命令**
- **不建 atom**——本特性无独立命令
- **关联段**：明确指向被依赖特性的 task wiki（后续构建）；证据指向原始 md
- **决策点**：场景差异由"接入制式（5G PDU会话/4G EPS承载/2-3G PDP上下文）× 流程类型（建立/修改/释放）× 发起方"3 维驱动，但**每个 option 的"走法"列填"依赖 {被依赖特性 task}"** 而非本特性命令

**为什么仍要建**（vs 跳过）：
- 业务图谱中本特性是其他特性的**底座**（PDU 会话是地址分配/PCC/接入控制的载体）；task wiki 提供"被依赖关系"的可追溯锚点，避免后续特性建完后回看不知道"会话承载"是 GWFD-010101 提供
- 审查/配置生成 Agent 可一眼看到"此特性为底座，配置查找请到被依赖特性"
- 资源浪费很小（1 个 feature + 1-2 个 compound ≈ 100 行）；信息密度高

**SOP §R1.1 子规则补注**：
- activation 空缺型特性**不再是单一类型**，拆 2 类：
  - **配置型 activation 空缺**（如 SA特征库更新/会话级 FUP）：有原始 activation 文档但主文档空，仅靠参考信息 MML 清单 + 特性知识补；按 SOP §R1.1 规则核证据链
  - **能力型 activation 空缺**（如 GWFD-010101 会话管理）：原始 16 文件全为描述性，无 activation/无 MML；按 §3.7 骨架占位范式处置

> 实战教训（2026-07-11）：APN 域首批特性 GWFD-010101 会话管理首建即遇此类型，按 §3.7 范式产出 feature (2-XXXXX, status:foundation) + 3 个骨架 compound（指向地址分配/PCC/N4接口）。此范式可推广到 APN 域其他能力型特性（如 4G EPS 承载管理、2/3G PDP 上下文会话管理——属同 1 个 feature_code 的不同接入制式，可统一入本骨架）。

---

## 4. wiki 模板（★统一格式：人能看懂、好审查）

### feature（2-）— 特性级
- front matter：`id / type:Task / task_layer:feature / task_logical_name / ref→Feature / task_intent / status`
- 正文：
  - `# {特性名}（{feature_code}）`
  - `> 特性静态知识见 [{feature_code}](feature/...md)。本页讲配置生成实例化时怎么配。`
  - `## 配置概览`：对象链 + 场景骨架（1-2 段）
  - `## 配置流程`：**每步必须显示"干啥 + 含哪些命令"**（人不点链接就懂每步配啥）：
    ```
    1. **{步骤名}**（{一句话干啥}）：`{命令1}` + `{命令2}` → [{compound/atom-id}](链接)
       - 子分支（按 DP 选，可空）：`{命令}` → [{id}](链接)
    ```
  - `## 决策点`：场景影响表（§5）
  - `## 约束`：bullet（统一格式见下）
  - `## 关联`：特性wiki / 编排compound（带命令提示）/ 直接atom / 证据

### compound（1-）— 步骤级
- front matter：`id / type:Task / task_layer:compound / task_logical_name / ref:null / task_intent / status`
- 正文：
  - `# {步骤名}`
  - `> {定位一句话}。被引用于 {features}。`
  - `## 配置方法`：**统一步骤表 + 典型脚本**：
    ```
    | 步骤 | 命令 | 关键参数 |
    |---|---|---|
    | {步骤} | {命令} | {参数} |
    **典型脚本**：{脚本}
    ```
  - `## 场景差异`（可选）：bullet，各场景对本步骤的参数增量
  - `## 决策点`：选项影响表（统一格式见下）
  - `## 约束`：bullet（统一格式见下）
  - `## 关联`：上游 / 含atom / 下游 / 被引用于 / 证据

### atom（0-）— 命令级（已有范式，参考 `0-00033`）
- front matter：`id / type:Task / task_layer:atom / task_logical_name / ref→MMLCommand / task_intent / status`
- 正文：`# 标题` → `> 命令静态知识见 [ADD XXX](command/...)` → `## 配置方法(取值样例表+典型脚本+步骤位置)` → `## 决策点` → `## 约束` → `## 关联(命令wiki+上下游atom+被引用于compound/feature+证据)`

### 决策点统一格式（feature/compound 通用）
表格 `| 选项/场景 | 影响（参数/命令/联动） |`，每 option 影响必填（§5）。

### 约束统一格式
bullet `- **{规则名}**（{severity}）：{约束} — {后果}`，severity 用 `critical`/`warning`/`info`。

---

## 5. 决策点记录规范（硬约束）

- 多配置方法（场景）的差异**必须用 DP 组织**，**不建多套流程**。
- DP 每个 option 的影响**必须全记**——否则实际编排时不知该编哪条路径。
- 影响维度（按需列全）：控制层级 / 业务识别方式 / 规则类型 / **走法(骨架+特化compound vs 骨架+直接atom)** / 是否需某命令 / 接入域类型 / 关键联动参数 / 是否刷新。
- **feature 用一张场景影响表**（范本：GWFD-110311 `2-00001` 的 9 场景表，含"走法"列区分多命令 compound vs 单命令 atom）。
- compound 内的 DP 记阶段级选择，并标注与上层 feature DP 的联动关系。

---

## 6. 硬约束（构建完整，非 MVP）

- **缺失命令的 atom 必须补建**（不空占位）+ **写入 `_numbering.json`**；能复用已有 atom 就复用。
- **证据 md 拷进 `assets/evidence/`**（自包含，CLAUDE.md §7 可剥离）。
- **双向链接闭环**：atom ↔ compound ↔ feature，无断链。Grep 确认新文件无 `[[` 残留占位、无指向已删对象的断链。
- **构建完整**：一个特性建到能端到端编排（所有该建的 compound 建出，DP 影响全）。
- 引用规则（CLAUDE.md §5.5）：已建 `[..](.md)` 带 .md；未建 `[[ID]]` 占位。
- **activation 模板复用识别**：产品文档常对相似特性复用同一份 activation 部署模板（实战：时长/流量/事件计费 activation md5 相同，都演示 VOLUME）。若本特性 activation 与他特性雷同，feature 声称的差异化参数（如 DURATION/EVENT）须核实是否在该特性 activation 有演示；**无演示 = 零证据差异**，必须标真实来源（特性概述/实现原理/命令 wiki 的 evidence）+ 配置流程脚注注明"activation 未演示，取值来自 XXX"。
- **配置流程参数证据链**：feature「配置流程」是配置生成的**可执行蓝图**（非知识叙述）。写进的**每个命令+参数**必须可追溯到 evidence（activation 脚本/命令 wiki/数据规划表）。**无证据的参数必须移除或改为"UDG 侧不配/由上层决定"**，否则配置生成编造参数（critical）。实战教训：事件计费曾写"PCCPOLICYGRP 可配计费点 REQUEST/RESPONSE/FINISH"但命令 wiki 无此参数。
- **可选步骤处理一致**：同类可选全局开关步骤（如在线计费的 UPDEFAULTQUOTA/UPGLBCHGPARA/URRFAILACTION）要么都列要么都不列，不能选择性遗漏。
- **冗余特性标关系**：若本特性与已建特性 activation 高度雷同、配置结构零差异（如流量计费 ≈ 内容计费 VOLUME 特化），必须在 front matter 或配置概览显式标关系（"本特性 = X 的 Y 特化"），避免配置生成产出雷同脚本。
- **★ 调测剥离（2026-07-11 APN 域实战教训，critical）**：feature/compound 的「配置流程」是配置生成的**可执行蓝图**，**只含配置类命令**（`ADD`/`MOD`/`SET`/`DEL`/`RMV`/`LOD`/`STR 持久化`）。**调测/查询/导出类命令（`DSP`/`LST`/`EXP`/`STP`/`STR 探测`）禁止出现在配置流程**。
  - **三场景范本**（2-00001/03/06/10/18/19/26 等）配置流程 0 调测——这是既有规范。
  - 处置：调测内容**只在关联段「证据」列表把"调测xxx.md"作为证据链接**（如 `[调测融合计费](evidence/.../调测xxx.md)`），**不展开命令、不单列"调测atom"段、配置概览表不列"调测"行**。
  - 反例（APN 域首批，已记债）：2-00034/35/39/40 把"调测"作为配置流程最后一步 + 概览表列"调测"行 + 关联段列"调测 atom（9 条）"——全部需剥离。
  - **诊断/运维型特性例外**（如 GWFD-010108 用户面地址自动检测，零配置命令、纯 STR/DSP 运维）：按 §3.7 能力型/运维型骨架处置，不建配置流程，直接指向原始特性信息。
- **★ 防平铺（2026-07-11 APN 域实战教训，critical）**：feature 配置流程里**连续 ≥3 个 atom 引用且无 compound 承载**时，强制按 §3.5「跨特性复用预判」评估抽 compound。多命令阶段模块（接入域基础设施/可靠性体系/路由发布/隧道族）禁止平铺成 atom 列表。

---

## 7. 验收清单（单特性 pass 完成自检）

- [ ] feature 1 个 + compound（通用骨架带场景差异 + 多命令特化）+ 缺失 atom 补齐入 `_numbering.json`
- [ ] 单命令步骤直接用 atom（非 compound）；多命令可复用模块才建 compound（§3.5）
- [ ] 特性级 DP 影响表完整（每 option 影响全记，含"走法"列）
- [ ] compound 复用已查：该引用的引用，新建的入复用库（index 同步）
- [ ] 证据拷入 `assets/evidence/`
- [ ] 双向链接闭环（Grep 新文件无 `[[`、无断链；atom 回指 compound/feature）
- [ ] index.md 同步（feature/compound 复用库/atom 段 + 被引用于更新）+ `_numbering.json` 同步

---

## 8. 待铺开范围

首批四场景 UDG 特性去重 **38 个**（计费 9 / 带宽 16 / 访问限制 12 / APN 14；注：ConfigTask 全量"94 可建特性"是另一口径，本 SOP 用四场景去重数）。GWFD-110311 是带宽首个范本。同法铺其余——**每建一个特性，优先复用已有 compound，逐步沉淀全通用/域通用 compound 库**。

> **族内构建顺序（经验）**：同族多特性（如计费族 7 特性）构建时，**先建差异最全的最复杂特性**（计费族=融合计费，含双URR/RGAPPLIED/最全场景），把通用 compound 的「场景差异」一次性补到位；再建简单特性（纯参数变种）复用即可。避免先建简单特性（单视角）导致 compound 场景差异欠债、后续不断回头补（实战教训：先建内容计费→1-00010 场景差异不足→7 特性建完才补）。
>
> **每批后自审**：每完成一族（或一批）特性，按 `特性task_wiki审视流程.md` R1 审视（覆盖度/复用合理性/假通用/activation 模板复用/参数证据链），critical 即修，经验回填本 SOP。

> 构建中如发现本 SOP 有缺陷，挖审查意见 → 修正本文件 → 版本号 +1。准则稳定判据：连续 2 个新特性 pass 人工免改或仅微调。
