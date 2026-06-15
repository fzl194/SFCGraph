---
name: charging-config-generation
description: |
  计费场景配置生成 — 覆盖离线计费、在线计费、融合计费全流程。
  关键词: 计费 / 业务感知 / DPI / 内容计费 / PCC / FUP / 达量限速 / 配额管理 /
  SMF / UPF / UDG / UNC / CHF / OCS / 三件套 / MML配置脚本
  基于三层图谱和统一知识库，从用户需求到可执行MML配置脚本的完整7阶段工作流
---

# 计费场景配置生成 SOP

## 1. 定位

本 SOP 是 Agent 执行"计费场景配置生成"的工作流指令。

Agent 根据用户的需求描述和现网配置脚本，经过需求理解、图谱匹配、参数收集、配置生成与全量核查，输出可直接执行的 MML 配置脚本。

本 SOP 仅覆盖**计费场景**（NS-01），不覆盖带宽控制、访问限制、本地分流等其他场景。

## 2. 知识源

### 2.1 核心知识（始终加载）

| 知识源 | 路径 | 用途 |
|--------|------|------|
| 三层图谱总览 | `knowledge/00-overview.md` | 五层架构导航、对象计数、端到端链路 |
| 业务图谱 | `knowledge/01-business-graph.md` | 场景/方案/决策点/业务规则/语义对象 |
| 特性图谱 | `knowledge/02-feature-graph.md` | 14个特性依赖、License、特性规则 |

### 2.2 知识库（按章节按需加载）

统一知识库已按18章拆分为独立文件，位于 `knowledge/kb/` 目录：

| 文件 | 主题 | 编号段 | 典型加载时机 |
|------|------|--------|------------|
| `kb/01-计费系统架构.md` | 计费演进、网元角色、接口体系 | K001-K012 | Phase 1 场景识别 |
| `kb/02-计费方式与维度.md` | 离线/在线/融合、计费维度 | K013-K019 | Phase 1 决策点 |
| `kb/03-核心术语定义.md` | URR/RG/SID/三件套等术语 | K020-K027 | Phase 1 理解用户需求 |
| `kb/04-Gy接口与DCC协议.md` | Gy信元、DCC模板、CCR/CCA | K028-K048 | Phase 5 在线计费 |
| `kb/05-Ga接口与CG.md` | Ga信元、CG话单格式 | K049-K057 | Phase 5 离线计费 |
| `kb/06-会话流程中的计费交互.md` | PDU/会话建立释放流程 | K058-K062 | Phase 1 理解业务流程 |
| `kb/07-Nchf融合计费服务.md` | N40接口、融合计费四操作 | K101-K121 | Phase 5 融合计费 |
| `kb/08-PFCP-N4接口与URR.md` | PFCP信元、URR上报机制 | K122-K135 | Phase 3/5 URR参数 |
| `kb/09-Gx-PCC策略与计费.md` | Gx接口、PCC规则、ADC | K136-K146 | Phase 5 PCC配置 |
| `kb/10-规则匹配与业务识别.md` | FLOWFILTER、L7匹配、优先级 | K147-K161 | Phase 3/5 匹配配置 |
| `kb/11-Usage-Monitoring与FUP.md` | Usage Monitoring、配额管理 | K162-K168 | Phase 5 FUP/达量限速 |
| `kb/12-融合计费配置全景.md` | 五层嵌套、三件套全景、PCF | K201-K213 | Phase 5 配置全景 |
| `kb/13-计费三件套配置.md` | URR/URRGROUP/PCCPOLICYGRP | K214-K223 | Phase 3/5 参数收集 |
| `kb/14-PCF策略配置.md` | PCF策略绑定 | K225, K228 | Phase 5 PCF场景 |
| `kb/15-方案设计知识.md` | 多业务方案、ULCL、配置模板 | K229-K234 | Phase 1 方案匹配 |
| `kb/16-特殊场景.md` | 不对称计费、多APN、预付费 | K235-K241 | Phase 5 特殊场景 |
| `kb/17-故障案例与运维.md` | 14个故障案例、排查经验 | K242-K255 | Phase 6 故障核查 |
| `kb/18-SMF侧对象体系与协同约束.md` | SMF侧命令体系、跨侧一致性 | K256-K261 | Phase 3/5 SMF侧配置 |

### 2.3 深度查证知识（需要时加载）

| 知识源 | 路径 | 用途 |
|--------|------|------|
| 任务层 | `knowledge/03-task-layer.md` | 28个配置任务、任务规则、执行顺序 |
| 命令图谱 | `knowledge/04-command-graph.md` | 87条MML命令、55个配置对象、14条命令规则 |
| 跨层映射 | `knowledge/05-cross-layer-mapping.md` | CS↔Feature/Task/DP/BR/SO 完整映射 |
| 证据索引 | `knowledge/06-evidence-index.md` | 32份证据源，含协议知识 |
| 三层图谱Schema | `knowledge/三层图谱Schema.md` | Schema定义与关系 |
| 本体标准定义 | `knowledge/三层图谱本体标准定义.md` | 对象类型、关系类型标准定义 |

### 2.4 特性级深度知识（需要时加载）

| 知识源 | 路径 | 用途 |
|--------|------|------|
| 特性知识文件 | `knowledge/feature/GWFD-*.md` / `WSFD-*.md` | 单个特性的详细配置知识 |
| 特性交叉分析 | `knowledge/feature/cross-feature-analysis.md` | 14特性间交叉依赖分析 |

**优先级规则**：统一知识库特殊规则 > 业务图谱约束 > 命令图谱参数约束 > 通用规则

## 3. 整体流程

```
Phase 1: 需求理解与图谱匹配
  输入: 用户需求描述 + 现网配置脚本文件路径(必须)
  输出: 方案上下文 + 网元范围(DP-CH-02) + 现网对象清单
  交互: 追问缺失的决策信息
  阻塞: 未提供现网脚本 → 停止，要求提供
  ↓
Phase 2: 方案确认（用户审核①）【GATE-3 STOP等用户确认】
  ↓
Phase 3: 参数收集
  输出: 完整参数表(LLD) + 优先级分析（必须用户确认）
  ↓
Phase 4: 参数确认（用户审核②）【GATE-4 STOP等用户确认】
  ↓
Phase 5: 配置生成
  输出: MML配置脚本(按依赖顺序)
  ↓
Phase 6: 配置核查（循环修正）
  输出: 核查通过的脚本
  ↓
Phase 6.5: 配置确认（用户审核③）【GATE-5 STOP等用户确认】
  ↓
Phase 7: 输出交付
```

## 3.5 用户交互规则

### 交互语气
- 使用专业但平实的语言，避免过度技术化
- 展示匹配结果和参数表时，用表格形式便于用户阅读
- 追问时说明"为什么需要这个信息"和"各选项的实际影响"

### 交互示例

**Phase 1 要求提供现网脚本**：
```
感谢您的需求描述。为了准确生成配置，我需要您提供现网配置脚本文件。

请提供以下文件的路径：
- UPF(UDG) 侧配置导出文件
- SMF(UNC) 侧配置导出文件（如需配置SMF侧）

支持 .txt .cfg .mml 等文本格式。提供后我会分析现网已有的计费对象。
```

**Phase 1 追问决策点**：
```
为了确定配置方案，我需要确认以下几点：

1. **计费方式**（计费信息如何上报）：
   - 离线计费：话单生成后批量发送给CG，适合后付费
   - 在线计费：实时通过OCS进行信用控制，适合预付费/配额管理
   - 融合计费：同时支持离线和在线，5G推荐方式

2. **配置网元**：
   - UPF+SMF两侧都配置（默认，推荐）
   - 只配置UPF(UDG)侧
   - 只配置SMF(UNC)侧

请告诉我您的选择，或描述您的具体需求我来帮您判断。
```

**Phase 2 方案确认**：
```
请确认以上匹配结果：
- 回复"确认"或"可以"→ 继续进入参数收集
- 指出需要修正的部分 → 我会重新匹配
- 回复"重选方案" → 回到方案选择步骤
```

**Phase 4 参数确认**：
```
参数校验已通过。请检查以下参数表，确认无误后回复"确认"。
如有需要修改的参数，请直接告知修改内容。
```

**Phase 6.5 配置确认**：
```
配置脚本已通过全量核查。以下是生成的配置脚本和核查报告，请确认：

[配置脚本内容]

[核查报告摘要]

- 回复"确认" → 输出最终交付物
- 指出需要修改的部分 → 回到对应阶段修正
```

### 用户中途退出

用户在任何 Phase 都可以说：
- "暂停" / "等一下" → 暂停当前流程，保留已有结果，等待用户继续
- "重新开始" → 清除所有结果，回到 Phase 1
- "换个场景" → 提醒用户本 SOP 仅覆盖计费，回到 Phase 1 重新识别
- "到此为止" → 基于当前已有结果生成交付物（可能不完整）

---

## 4. Phase 1: 需求理解与图谱匹配

⚠ **本阶段约束**：完成后必须 STOP 等用户在 Phase 2 确认。禁止在本阶段生成任何 MML 命令。

### 4.0 进入本阶段前的强制加载

**必须先使用 Read 工具读取以下文件，再进行任何业务逻辑（包括 §4.1 的检查）**：

```
必须读取：
1. knowledge/01-business-graph.md          — 业务图谱（场景/方案/决策点/规则）
2. knowledge/kb/01-计费系统架构.md          — 计费架构知识
3. knowledge/kb/03-核心术语定义.md          — 术语知识

按需读取：
4. knowledge/04-command-graph.md           — 现网对象解析时需要
5. knowledge/05-cross-layer-mapping.md     — 差异分析时需要
```

**读取完成后告知用户："已加载 Phase 1 参考文件。"** 然后继续执行 §4.1。

### 4.1 前置条件检查（必须在 §4.0 加载完成后执行）

在执行 §4.2 任何步骤之前，**必须按顺序完成以下两个检查**。任一检查未通过则**立即停止，输出提示，等待用户下一条消息**。

**【GATE-1】用户是否已提供现网配置脚本文件路径？**

- 未提供 → **STOP**。输出以下提示后停止执行，等待用户回复：
  ```
  我需要您提供现网配置脚本才能继续。请提供 UPF(UDG) 和/或 SMF(UNC) 侧的
  配置导出文件路径（支持 .txt .cfg .mml 等文本格式）。
  提供后我会分析现网已有的计费对象，避免冲突和重复配置。
  ```

**【GATE-2】验证现网脚本文件实际存在且可读取。**

收到用户提供的路径后，使用 **Glob 工具** 或 **Bash `ls`** 验证每个文件：
- 文件不存在 → **STOP**。告知用户具体路径错误，等待用户回复。
- 文件存在但为空或无法读取 → **STOP**。告知用户具体错误，等待用户回复。
- 验证通过 → 告知用户："已收到现网配置脚本（UPF: {文件名}, SMF: {文件名}），共 {n} 个文件，开始分析。"后继续执行 §4.2。

### 4.2 步骤

1. **场景识别**：从用户需求提取关键词，匹配业务图谱的 NetworkScenario (NS-01)
   - 引用已加载的 `01-business-graph.md` 中 NS/CS 定义

2. **网元与决策点解析**：提取 DP-CH-01~08 的答案，缺失时必须追问
   - 引用已加载的 `01-business-graph.md` 中 DecisionPoint 完整定义
   - 追问时引用图谱中各选项的含义，不可凭记忆

3. **现网配置解析**：按对象类型分批提取计费相关命令，构建结构化对象清单

   第1轮 UPF(UDG)侧，**每个命令类型单独 Grep 一次**，共16次查询：
   ```
   逐条查询（每次只查一个命令类型）：
   Grep: ^(ADD|SET|MOD|RMV) +URR
   Grep: ^(ADD|SET|MOD|RMV) +URRGROUP
   Grep: ^(ADD|SET|MOD|RMV) +PCCPOLICYGRP
   Grep: ^(ADD|SET|MOD|RMV) +PCCACTIONPROP
   Grep: ^(ADD|SET|MOD|RMV) +RULE
   Grep: ^(ADD|SET|MOD|RMV) +RULEBINDING
   Grep: ^(ADD|SET|MOD|RMV) +URRGRPBINDING
   Grep: ^(ADD|SET|MOD|RMV) +USERPROFILE
   Grep: ^(ADD|SET|MOD|RMV) +FLOWFILTER
   Grep: ^(ADD|SET|MOD|RMV) +FLOWFILTERGRP
   Grep: ^(ADD|SET|MOD|RMV) +FLTBINDFLOWF
   Grep: ^(ADD|SET|MOD|RMV) +PROTBINDFLOWF
   Grep: ^(ADD|SET|MOD|RMV) +FILTER
   Grep: ^(ADD|SET|MOD|RMV) +L7FILTER
   Grep: ^(ADD|SET|MOD|RMV) +IPLIST
   Grep: ^(ADD|SET|MOD|RMV) +REFRESHSRV
   ```

   第2轮 SMF(UNC)侧（当 DP-CH-02 包含 SMF 时），**同样每个命令类型单独 Grep**：
   ```
   系统级（逐条查询）：
   Grep: ^(ADD|SET|MOD) +PCCFUNC
   Grep: ^(ADD|SET|MOD) +CHGMODE
   Grep: ^(ADD|SET|MOD) +APNPCCFUNC
   Grep: ^(ADD|SET|MOD) +APNCHGMODE
   Grep: ^(ADD|SET|MOD) +CHARGECHAR
   Grep: ^(ADD|SET|MOD) +OCS
   Grep: ^(ADD|SET|MOD) +OCSGROUP
   Grep: ^(ADD|SET|MOD) +CCT

   业务级（逐条查询）：
   Grep: ^(ADD|SET|MOD) +URR
   Grep: ^(ADD|SET|MOD) +URRGROUP
   Grep: ^(ADD|SET|MOD) +PCCPOLICYGRP
   Grep: ^(ADD|SET|MOD) +RULE
   Grep: ^(ADD|SET|MOD) +RULEBINDING
   Grep: ^(ADD|SET|MOD) +URRGRPBINDING
   Grep: ^(ADD|SET|MOD) +USERPROFILE
   ```

   第3轮结构化：将提取结果按 ConfigObject 分类存储。

   **禁止将多个命令类型合并为一条 Grep 查询，每次 Grep 只能查一个命令类型。现网脚本过大，合并查询会导致结果溢出。**

4. **差异分析**：对每个 ConfigObject 判断执行类型

   | 执行类型 | 判断条件 | 生成动作 |
   |----------|----------|----------|
   | 复用(reuse) | 现网存在同名同参数对象 | 不生成命令，直接引用 |
   | 修改(modify) | 现网存在同名对象但参数需变更 | 生成 MOD 命令 |
   | 新建(create) | 现网无此对象 | 生成 ADD 命令 |
   | 删除(delete) | 方案不再需要的对象 | 生成 RMV 命令（先解绑上层） |

### 4.3 输出

向用户展示匹配结果，格式如下：

```markdown
## 匹配结果

**场景**: {NS-01 计费场景}
**方案**: {CS-xx 方案名称}

**决策点**:
- DP-CH-01 计费方式: {答案}
- DP-CH-02 配置网元: {答案}
- DP-CH-03 匹配层次: {答案}
- DP-CH-04 配额耗尽动作: {答案}
- {DP-CH-05~08 按实际情况补充}

**现网分析**:
- 现有 UserProfile: {列表}
- 现有 RULE: {列表}
- 现有 URR/URRGROUP/PCCPOLICYGRP: {列表}
- 可复用对象: {列表}

**任务编排**:
{按顺序列出需要执行的 Task，引用 03-task-layer.md 中的 ConfigTask ID}
```

### 4.4 注意事项

- 现网脚本通常数万至数十万行，**严禁全量读取**，必须按 §4.2 Step 3 的 grep pattern 分批提取
- 对象分类时参考 `04-command-graph.md` 中 ConfigObject 的层次关系（底层→中间→策略→顶层）
- 差异分析时加载 `05-cross-layer-mapping.md` 确认跨层映射关系，避免遗漏依赖

---

## 5. Phase 2: 方案确认（用户审核①）

**【GATE-3】方案确认审核点。**

将 Phase 1 的匹配结果展示给用户。展示后 **STOP**，输出以下提示后停止执行，等待用户下一条消息：

```
请确认以上匹配结果。确认后进入参数收集阶段。如有问题请指出。
```

- 用户回复确认类（"确认"/"可以"/"同意"）→ 进入 Phase 3
- 用户提出修正 → 回到 Phase 1 对应步骤重新匹配
- 用户要求换方案 → 展示其他 CS-xx 方案供选择
- 在用户明确确认之前：**不得执行 Phase 3 的任何步骤，不得收集任何参数，不得生成任何配置命令。**

---

## 6. Phase 3: 参数收集

⚠ **本阶段约束**：用户必须已确认方案（通过 GATE-3）。完成后必须 STOP 等用户在 Phase 4 确认。禁止在本阶段生成任何 MML 命令。

### 6.0 进入本阶段前的强制加载

```
必须读取：
1. knowledge/04-command-graph.md           — CommandParameter 定义（枚举值、约束）
2. knowledge/kb/08-PFCP-N4接口与URR.md     — URRID、RG、计量方式参数语义
3. knowledge/kb/13-计费三件套配置.md        — 三件套参数推导规则

按需读取（DP-CH-02 包含 SMF 时）：
4. knowledge/kb/18-SMF侧对象体系与协同约束.md — SMF侧参数差异
```

### 6.1 步骤

1. **从需求和现网推断参数**：尽可能从用户需求、现网命名规律、图谱方案示例、知识库默认值自动推断
   - 现网命名规律：如果现网 FILTER 命名为 `filter_xxx`，新 FILTER 用相同前缀
   - 参数枚举值必须从 `04-command-graph.md` 的 CommandParameter 定义中获取

2. **列出参数表**：按以下模板展示

   **业务参数表**：
   ```markdown
   ### 业务 {N}: {业务名称}

   | 参数项 | UPF(UDG)侧 | SMF(UNC)侧 | 来源 | 状态 |
   |--------|-----------|-----------|------|------|
   | **识别条件** | | | | |
   | 匹配方式 | {L34/L7 URL/L7协议} | — | 需求/推断 | 已知/待确认 |
   | L34协议 | {ANY/TCP/...} | — | 需求 | 已知/待确认 |
   | L7 URL/协议 | {具体值} | — | 需求 | 已知/待确认 |
   | **计费参数** | | | | |
   | 计费方式 | {值} | 同UPF | DP-CH-01 | 已知 |
   | URRID | {数值} | **必须与UPF一致** | 需用户提供 | **待提供** |
   | RG(费率组) | {数值} | **必须与UPF一致** | 需用户提供 | **待提供** |
   | 计量方式 | {值} | **必须与UPF一致** | 需求/推断 | 已知/待确认 |
   | **命名** | | | | |
   | FILTER名 | {建议值} | — | 推断 | 已知/待确认 |
   | URR名 | {建议值} | {建议值} | 推断 | 已知/待确认 |
   | RULE名 | {建议值} | **必须与UPF一致** | 推断 | 已知/待确认 |
   | **其他** | | | | |
   | 优先级 | {数值} | {数值} | 见优先级分析 | 已知/待确认 |
   ```

   **全局参数表**：
   ```markdown
   ### 全局参数

   | 参数项 | UPF(UDG)侧 | SMF(UNC)侧 | 来源 | 状态 |
   |--------|-----------|-----------|------|------|
   | UserProfile名 | {值} | **必须与UPF一致** | 现网/需求 | 已知/待确认 |
   | 默认URR组 | {值} | {值} | 现网/推断 | 已知/待确认 |
   | 配额耗尽动作 | {值} | — | DP-CH-04 | 已知 |
   | SMF系统级参数 | — | {值} | 现网/推断 | 已知/待确认 |
   ```

3. **优先级分析（必须独立执行并用户确认）**：

   **核心规则：PRIORITY 数字越小，优先级越高。不可更改。**

   **关键映射规则**：
   - 用户说"第1优先" = 最高优先级 = PRIORITY 数值**最小**
   - 用户说"第2优先" = 第二高 = PRIORITY 数值**第二小**
   - 用户说"第N优先" = 第N高 = PRIORITY 数值**第N小**
   - **第N优先的 PRIORITY 数值必须大于第(N-1)优先的数值，小于第(N+1)优先的数值**

   **正确示例**：
   ```
   现网 RULE:
   - l_tk_nu_1265      PRIORITY=2121  (用户要求第1优先)
   - l_rs_s12mbilled   PRIORITY=2130  (用户要求第2优先)
   - L_TKRS_Nu_1800    新建           (用户要求第3优先)  ← 应提议 2140（2130+10，在2130之后）
   - l_im_nu_100        PRIORITY=2299  (用户要求第4优先)

   ✗ 错误：L_TKRS_Nu_1800 建议 PRIORITY=2125（插在2121和2130之间）
     → 这会让新规则变成第2优先级，与用户要求的第3优先矛盾
   ✓ 正确：L_TKRS_Nu_1800 建议 PRIORITY=2140（在2130之后、2299之前）
     → 符合用户要求的第3优先级
   ```

   步骤：
   1. 从现网配置中用 Grep 提取**所有 RULE 的 PRIORITY 值**（包括非计费 RULE，必须提取全部）
   2. 将所有 RULE 按 PRIORITY 数值**从小到大排序**
   3. 将用户描述的优先级（"第N优先"）映射到排序位置：第1优先=排序第1（数值最小），第2优先=排序第2...
   4. 根据映射位置，计算新规则 PRIORITY（间距取10的倍数）
   5. 输出分析表，**STOP 等待用户确认**

   输出格式：
   ```
   ## 优先级分析

   **规则**：数字越小优先级越高（固定规则）

   **现网 PRIORITY 分布（全部 RULE，按数值从小到大排序）**：
   | RULE 名称 | PRIORITY | 优先级排名 | 说明 |
   |-----------|----------|-----------|------|
   | 现网rule1 | 21 | 第1（最高） | {业务描述} |
   | 现网rule2 | 31 | 第2 | {业务描述} |
   | **新rule_xxx** | **{拟提议值}** | **第N（按用户要求）** | **{新业务描述}** |

   **请确认新规则的优先级设置是否合理。如需调整请告知。**
   ```

   **禁止事项**：
   - **禁止**自行假设优先级顺序，必须先从现网提取全部 RULE 的 PRIORITY
   - **禁止**只提取计费 RULE，必须提取现网所有 RULE
   - **禁止**在用户未确认优先级前生成任何带 PRIORITY 的 RULE 命令
   - **禁止**将"第N优先"的新规则插在比它更高优先级的现网规则前面（数值上不能更小）

### 6.2 输出

将参数表（含优先级分析结果）展示给用户，标注所有"待提供"和"待确认"项，要求用户补充。

### 6.3 注意事项

- 参数表中每个字段都应标注"来源"（需求/现网/推断/图谱/知识库）和"状态"（已知/待确认/待提供）
- 两侧共用参数（URRID、RG、USAGERPTMODE 等）必须标注"**必须与UPF一致**"
- SMF侧参数差异需要从 `kb/18-SMF侧对象体系与协同约束.md` 确认，不要凭记忆填写
- 遇到不确定的参数语义，加载 `04-command-graph.md` 中对应的 CommandParameter 定义确认

---

## 7. Phase 4: 参数确认（用户审核②）

**【GATE-4】参数确认审核点。**

用户填写或修正参数后，进行参数合理性校验。校验通过后，将完整参数表展示给用户。展示后 **STOP**，输出以下提示后停止执行，等待用户下一条消息：

```
参数校验已通过。请检查以上参数表，确认无误后回复"确认"。
如有需要修改的参数，请直接告知修改内容。
```

- 用户回复确认类 → 进入 Phase 5
- 用户要求修改 → 修正参数后重新校验，再次等待用户确认
- 在用户明确确认之前：**不得执行 Phase 5 的任何步骤，不得生成任何 MML 命令。**

---

## 8. Phase 5: 配置生成

⚠ **本阶段约束**：必须已通过 GATE-4（用户已在 Phase 4 明确确认参数表）。未通过则 STOP 退回 Phase 4。无例外。

### 8.0 进入本阶段前的强制加载

```
必须读取：
1. knowledge/04-command-graph.md           — MMLCommand + CommandParameter + CommandRule
2. knowledge/kb/12-融合计费配置全景.md       — 融合/在线/离线场景差异
3. knowledge/kb/13-计费三件套配置.md        — 三件套参数组合规则

按需读取（排序依赖确认）：
4. knowledge/03-task-layer.md              — command_order 依赖链

按需读取（DP-CH-02 包含 SMF 时）：
5. knowledge/kb/18-SMF侧对象体系与协同约束.md — SMF侧参数差异
```

### 8.1 步骤

1. **按模板生成命令**：

   **UPF(UDG)侧**（每条业务按依赖顺序）：
   ```mml
   !-- 1. 底层过滤条件 (如需新建)
   ADD FILTER:FILTERNAME="{filter_name}", ...;
   ADD L7FILTER:L7FILTERNAME="{l7_name}", ...;  (仅L7 URL场景)

   !-- 2. 流过滤器与绑定
   ADD FLOWFILTER:FLOWFILTERNAME="{ff_name}";
   ADD FLTBINDFLOWF:FLOWFILTERNAME="{ff_name}",FILTERNAME="{filter_name}";
   ADD PROTBINDFLOWF:FLOWFILTERNAME="{ff_name}", ...;  (仅L7场景)

   !-- 3. 计费三件套
   ADD URR:URRNAME="{urr_name}", ...;
   ADD URRGROUP:URRGROUPNAME="{urrg_name}", ...;
   ADD PCCPOLICYGRP:PCCPOLICYGRPNM="{ppg_name}", ...;

   !-- 4. 规则
   ADD RULE:RULENAME="{rule_name}", ...;
   ```

   **SMF(UNC)侧**（当 DP-CH-02 包含 SMF 时）：
   ```mml
   !-- 系统级前置（已配置则跳过）
   SET PCCFUNC:...;
   SET CHGMODE:...;

   !-- 业务级三件套
   ADD URR:URRNAME="{smf_urr}", ...;  (注意: SMF侧有 OFFCOMPOUNDTYPE/ONLCOMPOUNDTYPE 特有参数)
   ADD URRGROUP:URRGROUPNAME="{smf_urrg}", ...;
   ADD PCCPOLICYGRP:PCCPOLICYGRPNM="{smf_ppg}", ...;

   !-- 规则与绑定
   ADD RULE:RULENAME="{rule_name}", ...;
   ADD RULEBINDING:...;
   ```

   参数值必须从 `04-command-graph.md` 的 CommandParameter 定义中获取枚举值，**禁止凭记忆填写**。

2. **按排序规则排列命令**：

   UPF(UDG)侧（严格顺序）：
   ```
   1.  FILTER / L7FILTER               (底层)
   2.  FLOWFILTER                       (中间)
   3.  FLTBINDFLOWF / PROTBINDFLOWF     (绑定)
   4.  URR / PCCACTIONPROP              (策略动作)
   5.  URRGROUP / PCCPOLICYGRP          (策略组合)
   6.  RULE                              (汇聚)
   7.  USERPROFILE                       (容器, 仅新建时)
   8.  URRGRPBINDING                     (默认计费组绑定)
   9.  RULEBINDING                       (规则绑定)
   10. REFRESHSRV                        (刷新生效, 必须最后)
   ```

   SMF(UNC)侧：
   ```
   1. 系统级命令（仅检查，已存在则跳过）
   2. 业务级三件套 + 规则 + 绑定
   3. 无 REFRESHSRV
   ```

3. **配置决策指南**（需要时从图谱/知识库加载规则后决策）：

   **OR 条件：FLOWFILTERGRP vs 多 RULE**

   | 方案 | 适用场景 |
   |------|---------|
   | FLOWFILTERGRP | 多个条件执行**完全相同**的动作 |
   | 多 RULE | 需要不同优先级或后续可能分化 |

   **默认**：使用 FLOWFILTERGRP（更简洁）。

   **兜底规则**

   | 机制 | 命令 | 触发条件 |
   |------|------|---------|
   | 默认URR组 | SET URRGRPBINDING:DFTURRGRPNAME | 流量未命中任何 RULE |
   | 显式兜底RULE | ADD RULE(FILTER=ANY, 低PRIORITY) | 流量命中兜底 RULE |

   两者应指向同一计费组。详细约束加载 `01-business-graph.md` BusinessRule BR-CH-06 确认。

   **URL 匹配协议绑定**：当用户提到"访问某网站"时，HTTP 和 HTTPS 都需要绑定：
   ```mml
   ADD PROTBINDFLOWF:FLOWFILTERNAME="ff_xxx",PROTOCOLNAME="http",L7FILTERNAME="l7_xxx";
   ADD PROTBINDFLOWF:FLOWFILTERNAME="ff_xxx",PROTOCOLNAME="https",L7FILTERNAME="l7_xxx";
   ```

   **融合计费**：UPF侧创建**两个独立 URR**（一个OFFLINE一个ONLINE），放入同一 URRGROUP。详细参数组合规则必须加载 `kb/12-融合计费配置全景.md` 确认。

### 8.2 注意事项

- 每个参数的枚举值必须从 `04-command-graph.md` CommandParameter 获取，不可自行推断
- 融合/在线/离线的参数差异很大，必须加载 `kb/` 对应章节文件确认
- 排序错误会导致配置失败，REFRESHSRV 必须在最后（仅UPF侧）
- 三件套（URR→URRGROUP→PCCPOLICYGRP）每条业务独立，不可跨业务复用
- 两侧共用参数（URRID、RG、RULENAME、USERPROFILENAME）必须一致
- SMF侧参数差异必须从 `kb/18-SMF侧对象体系与协同约束.md` 确认，两侧共用参数必须一致

---

## 9. Phase 6: 配置核查（循环修正）

⚠ **本阶段约束**：必须有 Phase 5 生成的配置脚本。核查完成后必须 STOP 等用户在 Phase 6.5 确认。

### 9.0 进入本阶段前的强制加载

```
必须读取：
1. knowledge/01-business-graph.md           — BusinessRule (BR-CH-01~16) 逐条核查
2. knowledge/04-command-graph.md            — CommandRule (CR-CH-01~14) + CommandParameter
3. knowledge/03-task-layer.md               — TaskRule (TR-CH-01~06) + command_order 依赖

按需读取（DP-CH-02 包含 SMF 时）：
4. knowledge/kb/18-SMF侧对象体系与协同约束.md — 跨网元一致性参数
```

> **核查依据必须是图谱中定义的规则实例（BR-CH-xx / CR-CH-xx / TR-CH-xx），不可凭记忆。**

### 9.1 核查步骤

1. **执行图谱规则核查**：引用已加载的 BusinessRule / CommandRule / TaskRule，逐条检查并记录通过/违反项
   - 业务约束：决策点一致性、三件套独立性、兜底规则
   - 配置依赖：引用完整性、绑定完整性、三件套闭合
   - 命令约束：REFRESHSRV位置、参数枚举合法性、跨网元名称一致

2. **执行 SKILL 独有操作安全检查**：

   | 核查项 | 规则 | 严重级别 |
   |--------|------|---------|
   | 同名冲突 | 新增对象名是否与现网已有对象同名 | HIGH |
   | 参数覆写 | SET/MOD 命令是否覆盖了现网中仍在使用的参数 | HIGH |
   | 共享对象影响 | 修改被多个 RULE 引用的共享对象时，是否评估影响范围 | HIGH |
   | 删除安全 | RMV 命令是否先解绑了上层引用 | CRITICAL |

3. **跨网元一致性核查**（仅 DP-CH-02 包含 UPF+SMF 时）
   - CR-CH-08（跨网元名称一致性）、CR-CH-02（RG值跨侧一致性）逐条核查

### 9.2 修正规则

- 自动修正问题并告知用户
- 无法自动修正 → 暂停要求用户决策
- 修正后重新核查，直到全部通过

### 9.3 输出

```markdown
## 核查报告

### 核查结果: {通过 / 已修正}

| 维度 | 规则来源 | 检查项数 | 通过 | 修正 | 待确认 |
|------|---------|---------|------|------|--------|
| BusinessRule | 01-business-graph.md | {n} | {n} | {n} | {n} |
| CommandRule | 04-command-graph.md | {n} | {n} | {n} | {n} |
| TaskRule | 03-task-layer.md | {n} | {n} | {n} | {n} |
| 操作安全 | §9.1.2 | {n} | {n} | {n} | {n} |

### 修正日志
1. [{规则ID}] {问题描述} → {修正动作}
```

### 9.4 注意事项

- 每条违反项必须标注对应的规则 ID（BR-CH-xx / CR-CH-xx / TR-CH-xx），不可笼统描述
- 图谱规则是业务准确性的保障，必须从图谱原文加载执行，不可省略或简化
- 操作安全检查（§9.1.2）是图谱未覆盖的生产环境保护，同样不可跳过
- 跨网元一致性检查中，7项参数均为 CRITICAL 级别，任一不一致都必须修正

### 9.5 用户确认（用户审核③）

**【GATE-5】配置确认审核点。**

核查通过后，将核查报告和生成的配置脚本一并向用户展示。展示后 **STOP**，输出以下提示后停止执行，等待用户下一条消息：

```
以上配置脚本已通过全量核查。请确认脚本内容无误后回复"确认"，我将输出最终交付物。
如有问题请指出。
```

- 用户回复确认类 → 进入 Phase 7
- 用户要求修改 → 回到对应 Phase 修正，修正后重新核查，再次等待用户确认
- 在用户明确确认之前：**不得输出最终交付物。**

---

## 10. Phase 7: 输出交付

### 10.1 交付物

| 文件 | 内容 | 格式 |
|------|------|------|
| UPF(UDG)配置脚本 | 可执行MML命令，按依赖顺序排列 | `.mml` / 代码块 |
| SMF(UNC)配置脚本 | 可执行MML命令，系统级+业务级分开 | `.mml` / 代码块 |
| 校验脚本 | LST/DSP 校验命令 + 预期结果（两侧各一套） | `.mml` / 代码块 |
| 变更摘要 | 新建/修改/复用/删除的对象清单 | markdown |

### 10.2 配置脚本格式

**UPF(UDG)侧脚本**：

```mml
!-- =============================================
!-- 计费场景配置脚本 — UPF(UDG)侧
!-- 方案: {方案名称}
!-- 网元: UPF/UDG
!-- 生成时间: {timestamp}
!-- =============================================

!-- [T-EXEC-002] 三四层过滤条件
ADD FILTER:...;

!-- [T-EXEC-003] 七层过滤条件
ADD L7FILTER:...;

!-- [T-EXEC-004] 流过滤器与绑定
ADD FLOWFILTER:...;
ADD FLTBINDFLOWF:...;
ADD PROTBINDFLOWF:...;

!-- [T-EXEC-005] 计费三件套
ADD URR:...;
ADD URRGROUP:...;
ADD PCCPOLICYGRP:...;

!-- [T-EXEC-008] 规则配置
ADD RULE:...;

!-- [T-EXEC-010] UserProfile与绑定
ADD USERPROFILE:...;
SET URRGRPBINDING:...;
ADD RULEBINDING:...;
SET REFRESHSRV:REFRESHTYPE=ALL;
```

**SMF(UNC)侧脚本**（当 DP-CH-02 包含 SMF 时）：

```mml
!-- =============================================
!-- 计费场景配置脚本 — SMF(UNC)侧
!-- 方案: {方案名称}
!-- 网元: SMF/UNC
!-- 生成时间: {timestamp}
!-- =============================================

!-- [系统级] 前置检查（已配置则跳过）
SET PCCFUNC:...;
SET CHGMODE:...;

!-- [业务级] 计费三件套
ADD URR:...;
ADD URRGROUP:...;
ADD PCCPOLICYGRP:...;

!-- [业务级] 规则与绑定
ADD RULE:...;
ADD RULEBINDING:...;
```

### 10.3 校验脚本格式

```mml
!-- License 开关验证
LST LICENSESWITCH:LICITEM="LKV3G5SABS01";
!-- 预期: ENABLE

!-- 配置链逐层回查
LST RULEBINDING:USERPROFILENAME="{up_name}";
!-- 预期: {n}条绑定
LST RULE:RULENAME="{rule_name}",POLICYTYPE=PCC;
!-- 预期: FLOWFILTERNAME={ff_name}, PRIORITY={pri}, POLICYNAME={ppg_name}
LST PCCPOLICYGRP:PCCPOLICYGRPNM="{ppg_name}";
!-- 预期: URRGROUPNAME={urrg_name}
LST URR:URRNAME="{urr_name}";
!-- 预期: URRID={id}, USAGERPTMODE={mode}, ...
```

### 10.4 变更摘要格式

```markdown
## 配置变更摘要

### 方案信息
- 场景: NS-01 计费场景
- 方案: {方案名称}
- 决策: DP-CH-01={}, DP-CH-02={}, DP-CH-03={}, DP-CH-04={}

### 变更统计
| 操作类型 | 对象数量 |
|---------|---------|
| 新增(ADD) | {n} |
| 修改(SET) | {n} |
| 复用(不生成命令) | {n} |
| 删除(RMV) | {n} |

### 新增对象清单
| ConfigObject | 对象名 | 关联业务 | 说明 |
|-------------|--------|---------|------|
| FILTER | {name} | {biz} | {desc} |

### 注意事项
- {需人工确认的事项}
```

---

## 11. Agent 执行约束

1. **禁止跳过任何 Phase**：7 个 Phase 必须严格按顺序执行。即使用户一次性提供了完整需求和所有参数，也**绝对不允许**跳过 Phase 2（方案确认）和 Phase 4（参数确认）。
2. **用户审核点必须 STOP**：Phase 2、Phase 4、Phase 6.5 是用户审核点。到达审核点时，Agent **必须输出审核内容后立即停止执行**，等待用户下一条消息。在收到用户的明确确认之前，**不得执行下一个 Phase 的任何步骤**。
3. **现网配置为必须**：未验证现网脚本存在之前，不得进入 §4.2 任何步骤。
4. **严格按依赖顺序**：不可跳过底层对象直接配置上层
5. **REFRESHSRV 必须最后**：所有配置完成后才刷新（仅UPF侧）
6. **三件套独立原则**：每条业务的 URR/URRGROUP/PCCPOLICYGRP 彼此独立
7. **追问而非猜测**：缺失决策信息或参数时必须追问，不可自行推断必填参数的值
8. **动网保守原则**：对现网对象的修改必须有明确的用户确认
9. **知识库优先**：知识库中的特殊规则优先于通用规则
10. **命名遵循现网**：新对象命名尽量遵循现网已有的命名规律
11. **跨网元一致**：UPF 和 SMF 两侧的 URRID/RG/USAGERPTMODE/RULENAME/USERPROFILENAME 必须一致
12. **SMF 系统级检查**：SMF 侧系统级配置（PCCFUNC/CHGMODE/CHF连接）通常已部署，仅检查确认
13. **图谱为业务准确性保障**：所有业务事实必须从图谱/知识库动态加载，禁止凭记忆填写
14. **强制文件加载**：每个 Phase 标注了必须读取的文件，Agent 必须在执行该 Phase 业务逻辑**之前**使用 Read 工具读取
15. **优先级必须用户确认**：必须提取现网全部 RULE 的 PRIORITY 分布，分析后 STOP 等用户确认，确认前禁止生成 RULE 命令。**"第N优先"= 第N高优先级 = PRIORITY数值第N小，第N优先的数值必须大于第(N-1)优先的数值。**
