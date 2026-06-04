---
name: charging-config-generation
description: |
  计费场景配置生成 — 覆盖离线计费、在线计费、融合计费全流程。
  关键词: 计费 / 业务感知 / DPI / 内容计费 / PCC / FUP / 达量限速 / 配额管理 /
  SMF / UPF / UDG / UNC / CHF / OCS / 三件套 / MML配置脚本
  基于业务图谱和知识库，从用户需求到可执行MML配置脚本的完整7阶段工作流
version: 1.0.0
source: manual-creation
domain: charging
---

# 计费场景配置生成 SOP

## 1. 定位

本 SOP 是 Agent 执行"计费场景配置生成"的工作流指令。

Agent 根据用户的需求描述和现网配置脚本，经过需求理解、图谱匹配、参数收集、配置生成与全量核查，输出可直接执行的 MML 配置脚本。

本 SOP 仅覆盖**计费场景**（NS-01），不覆盖带宽控制、访问限制、本地分流等其他场景。

## 2. 知识源

| 知识源 | 路径 | 用途 | 优先级 |
|--------|------|------|--------|
| 计费知识库 | `knowledge/计费知识库.md` | 特殊规则、参数推导、经验约束 | **最高** |
| 计费场景图谱 | `knowledge/计费场景业务图谱.md` | 计费场景子图实例 | **最高** |
| 业务感知图谱 | `knowledge/业务感知业务图谱.md` | 场景/方案/决策点/任务编排 | 高 |
| 业务图谱Schema | `knowledge/business-graph-schema.md` | Schema定义与关系 | 参考 |
| 原理知识 | `knowledge/原理-架构与术语.md` | 计费架构、术语定义、规则匹配原理 | 深度查证 |
| 协议知识(Ga/Gy) | `knowledge/协议知识-Ga-Gy-DCC.md` | Gy/DCC/Ga协议信元、会话流程 | 深度查证 |
| 协议知识(N40/PFCP) | `knowledge/协议知识-N40-PFCP-Gx.md` | N40/N4/Gx接口信元与流程 | 深度查证 |
| 方案设计 | `knowledge/方案设计-配置全景.md` | 融合计费配置全景、三件套、PCF、ULCL | 深度查证 |
| 故障案例 | `knowledge/故障案例与运维.md` | 故障排查案例与运维经验 | 故障定位 |

**优先级规则**：知识库特殊规则 > 业务图谱约束 > 命令文档参数约束 > 通用规则

## 3. 整体流程

```
Phase 1: 需求理解与图谱匹配
  输入: 用户需求描述 + 现网配置脚本文件路径(必须)
  输出: 方案上下文 + 网元范围(DP-00) + 现网对象清单
  交互: 追问缺失的决策信息
  注: 现网脚本按对象类型分批提取，不全量读取
  ↓
Phase 2: 方案确认（用户审核①）
  输入: Phase 1 输出
  输出: 用户确认的方案路径
  交互: 用户确认/修正匹配结果
  ↓
Phase 3: 参数收集
  输入: 确认方案 + 现网对象清单
  输出: 完整参数表(LLD)
  交互: 列出缺失参数要求用户提供
  ↓
Phase 4: 参数确认（用户审核②）
  输入: 用户填写的参数
  输出: 确认的LLD
  交互: 用户确认/修正参数值
  ↓
Phase 5: 配置生成
  输入: 确认的LLD
  输出: MML配置脚本(按依赖顺序)
  交互: 无
  ↓
Phase 6: 配置核查（循环修正）
  输入: 配置脚本 + 现网配置
  输出: 核查通过的脚本
  交互: 发现问题则自动修正并告知用户
  ↓
Phase 7: 输出交付
  输入: 核查通过的脚本
  输出: 可下载的配置文件 + 校验脚本 + 变更摘要
```

## 4. Phase 1: 需求理解与图谱匹配

### 4.1 输入

- 用户自然语言需求（计费相关意图）
- **现网配置脚本文件路径（必须）**：用户提供现网配置脚本文件路径（而非粘贴内容）

如果用户未提供现网配置，提醒：
> "配置生成需要基于现网配置进行。请提供现有配置脚本文件路径。"

### 4.1.1 现网脚本处理策略

> **问题**：现网脚本通常数万至数十万行 MML 命令，无法全量读取。
> **策略**：按对象类型分批提取计费相关命令，构建结构化清单。

**执行方法**：使用 grep/Grep 工具按关键词提取，分三轮扫描：

**第1轮：UPF(UDG)侧计费对象提取**

```bash
# 提取计费相关命令行（ADD/SET/MOD/RMV）
grep -E "^(ADD|SET|MOD|RMV) +(URR|URRGROUP|PCCPOLICYGRP|PCCACTIONPROP|RULE|RULEBINDING|URRGRPBINDING|USERPROFILE|FLOWFILTER|FLOWFILTERGRP|FLTBINDFLOWF|PROTBINDFLOWF|FILTER|L7FILTER|IPLIST|REFRESHSRV)" {file}
```

**第2轮：SMF(UNC)侧计费对象提取**（当 DP-00 包含 SMF 时）

```bash
# SMF 系统级
grep -E "^(ADD|SET|MOD) +(PCCFUNC|APNPCCFUNC|CHGMODE|APNCHGMODE|CHARGECHAR|TNFINS|TNFGRP|TNFBINDGRP|SELECTCHFGBYCC|GLBDFTCHFGROUP|OCS|OCSGROUP|CCT|SELECTCCTBYCC|DCCTEMPLATE|PDUTRIGGER|RGTRIGGER)" {file}

# SMF 业务级
grep -E "^(ADD|SET|MOD) +(URR|URRGROUP|PCCPOLICYGRP|RULE|RULEBINDING|URRGRPBINDING|USERPROFILE)" {file}
```

**第3轮：提取结果结构化**

将提取的命令行解析为结构化对象表，按 ConfigObject 分类存储（见 §4.4）。
提取结果通常在 200-500 行范围内，可以全量处理。

**注意**：
- 如果脚本文件在本地路径，使用 Grep 工具（pattern 指定命令类型）直接搜索
- 如果用户粘贴了内容，先用 bash 过滤再处理
- 提取后告知用户："已从现网脚本中提取 {n} 条计费相关命令（总计 {total} 行）"

### 4.2 步骤 1: 场景识别

从用户需求中提取计费相关关键词，匹配到业务图谱的 NetworkScenario。

**查阅知识文件**：
- `knowledge/计费场景业务图谱.md` — 匹配场景节点(NS-01)和方案(DS-xx)
- `knowledge/原理-架构与术语.md` Ch2(计费方式与维度) — 理解用户提到的计费方式术语
- `knowledge/计费知识库.md` §1(计费特性体系) — 确认所需License是否已开启

**计费场景关键词**：
- 在线计费、离线计费、融合计费、Gy、Ga、Nchf
- 计费、收费、费率、单价、免费、配额、额度
- 按流量、按时长、按事件、差异化计费
- 配额耗尽、BLOCK、阻断、门控

如果匹配到计费场景（NS-01），继续。如果同时涉及其他场景（如带宽控制），提醒用户本 SOP 仅处理计费部分。

### 4.3 步骤 2: 网元与决策点解析

**网元识别**：计费配置涉及 UPF（UDG）和 SMF（UNC）两个网元，需从用户描述判断配置范围。

> **查阅知识文件**：`knowledge/计费知识库.md` §11(UNC/SMF侧协同)、§21(SMF侧配置顺序)

沿业务图谱查找计费相关的 DecisionPoint，从用户描述中提取答案：

| 决策点 | 问题 | 答案选项 | 影响 |
|--------|------|---------|------|
| **DP-00** | **配置网元** | UPF+SMF（默认）/ UPF only / SMF only | 决定生成哪套 MML 命令 |
| DP-01 | 计费方式 | 离线计费 / 在线计费 / 融合计费 | URR.USAGERPTMODE 参数 |
| DP-02 | 配额耗尽后动作 | BLOCK / REDIRECT / FORWARD | 是否需要 PCCACTIONPROP |
| DP-03 | 匹配层次 | L34 only / L7 URL / L7 协议 / 混合 | 是否需要 L7FILTER / PROTBINDFLOWF |

**DP-00 判断规则**：
- 用户同时提到两侧配置需求（如"帮我配置5G融合计费"）→ **UPF+SMF**
- 用户只提到 UPF/UDG 相关命令 → **UPF only**
- 用户只提到 SMF/UNC 相关命令（CHF/CCT/DCC/Trigger）→ **SMF only**
- **无法判断时默认 UPF+SMF**，因为实际部署通常需要两侧配合

**规则**：
- 用户描述中缺少决策信息时，**必须追问**
- 追问时说明各选项的含义和影响

### 4.4 步骤 3: 现网配置解析

基于 §4.1.1 提取的命令行，构建现网对象清单。

```
解析规则:
- ADD XXX:... → 新建对象 XXX
- SET XXX:... → 修改对象 XXX
- LST XXX:... → 查询(忽略)
```

按 ConfigObject 分类存储，区分 UPF(UDG) 和 SMF(UNC) 两侧：

> **查阅知识文件**：`knowledge/计费知识库.md` §2(配置对象体系)、§11(UNC/SMF侧协同)、§20(SMF侧完整命令体系)

**UPF(UDG)侧对象**：

| 层级 | ConfigObject | 关键参数 | 依赖 |
|------|-------------|---------|------|
| 底层 | FILTER | FILTERNAME, L34PROTOCOL | 可引用 IPLIST |
| 底层 | L7FILTER | L7FILTERNAME, URL | 无 |
| 中间 | FLOWFILTER | FLOWFILTERNAME | 引用 FILTER |
| 中间 | FLTBINDFLOWF | FLOWFILTERNAME, FILTERNAME | 绑定关系 |
| 中间 | PROTBINDFLOWF | FLOWFILTERNAME, PROTOCOLNAME, L7FILTERNAME | 绑定关系 |
| 策略 | URR | URRNAME, URRID, USAGERPTMODE, ONLMETERINGTYPE/OFFMETERINGTYPE, RG | 无 |
| 策略 | URRGROUP | URRGROUPNAME, UPURRNAME1, DOWNURRNAME1 | 引用 URR |
| 策略 | PCCPOLICYGRP | PCCPOLICYGRPNM, URRGROUPNAME, PCCACTPROPNAME | 引用 URRGROUP |
| 策略 | PCCACTIONPROP | PCCACTPROPNM, GATINGSTATUS | 无 |
| 汇聚 | RULE | RULENAME, FLOWFILTERNAME, PRIORITY, POLICYNAME | 引用 FLOWFILTER + PCCPOLICYGRP |
| 顶层 | USERPROFILE | USERPROFILENAME | 无 |
| 顶层 | RULEBINDING | USERPROFILENAME, RULENAME | 绑定 RULE→USERPROFILE |
| 顶层 | URRGRPBINDING | USERPROFILENAME, DFTURRGRPNAME | 绑定 URRGROUP→USERPROFILE |

**SMF(UNC)侧对象**（当 DP-00 包含 SMF 时解析）：

| 类别 | ConfigObject | 关键参数 | 说明 |
|------|-------------|---------|------|
| **系统级（一次性）** | | | |
| 功能开关 | SET PCCFUNC | HOMEPCCSWITCH, ROAMPCCSWITCH | PCC全局开关 |
| 功能开关 | SET APNPCCFUNC | DNN, PCCSWITCH | APN级PCC开关 |
| 接口模式 | SET CHGMODE | FORCED, TMACCTYPE | 全局计费接口(N40/GaGy) |
| 接口模式 | ADD APNCHGMODE | DNN, FORCED | APN级计费接口 |
| 计费属性 | ADD CHARGECHAR | CCVALUE, CCNAME | CC实例 |
| CC绑定 | SET GLBCHARGECHAR / SET USRPROFCHARGE / SET APNCHARGECTRL | CCVALUE | CC绑定粒度 |
| CHF连接 | ADD TNFINS + ADD TNFINSIP | TNFINSID, FQDN | CHF实例 |
| CHF组 | ADD TNFGRP + ADD TNFBINDGRP | TNFGRPID | CHF组 |
| CHF选择 | ADD SELECTCHFGBYCC / SET GLBDFTCHFGROUP | CCVALUE, TNFGRPID | CHF选择策略 |
| OCS连接 | ADD OCS + ADD DIAMPEERADDR | OCSID | OCS信息 |
| CCT模板 | ADD CCT | CCTNAME | 融合计费CCT模板 |
| CCT选择 | ADD SELECTCCTBYCC | CCVALUE, CCTNAME | 按CC选CCT |
| DCC模板 | ADD DCCTEMPLATE | DCCTEMPLATEID | 在线计费DCC模板 |
| Trigger | ADD PDUTRIGGER / ADD RGTRIGGER | TRIGGERID | 计费触发条件 |
| **业务级（每业务）** | | | |
| 策略 | ADD URR | URRNAME, URRID, USAGERPTMODE, RG, COMPOUNDTYPE | 需与UPF侧URRID/RG一致 |
| 策略 | ADD URRGROUP | URRGROUPNAME, UPURRNAME1/2 | 需与UPF侧一致 |
| 策略 | ADD PCCPOLICYGRP | PCCPOLICYGRPNM, URRGROUPNAME | 需与UPF侧一致 |
| 汇聚 | ADD RULE | RULENAME, POLICYTYPE, POLICYNAME | 需与UPF侧一致 |
| 绑定 | ADD USERPROFILE | USERPROFILENAME | 需与UPF侧一致 |
| 绑定 | ADD RULEBINDING | USERPROFILENAME, RULENAME | 绑定RULE→USERPROFILE |
| 默认组 | SET URRGRPBINDING | USERPROFILENAME, DFTURRGRPNAME | 默认计费组 |

### 4.5 步骤 4: 差异分析

对每个 ConfigObject 判断执行类型：

| 执行类型 | 判断条件 | 生成动作 |
|----------|----------|----------|
| 复用(reuse) | 现网存在同名同参数对象 | 不生成命令，直接引用 |
| 修改(modify) | 现网存在同名对象但参数需变更 | 生成 SET 命令 |
| 新建(create) | 现网无此对象 | 生成 ADD 命令 |
| 删除(delete) | 方案不再需要的对象 | 生成 RMV 命令（先解绑上层） |

### 4.6 输出

向用户展示匹配结果，格式如下：

```markdown
## 匹配结果

**场景**: NS-01 计费场景
**方案**: DS-01 差异化计费组合方案

**决策点**:
- DP-00 配置网元: {UPF+SMF / UPF only / SMF only}
- DP-01 计费方式: {答案}
- DP-02 配额耗尽动作: {答案}
- DP-03 匹配层次: {答案}

**现网分析**:
- 现有 UserProfile: {列表}
- 现有 RULE: {列表}
- 现有 URR/URRGROUP/PCCPOLICYGRP: {列表}
- 可复用对象: {列表}

**任务编排**:
{按顺序列出需要执行的 Task}
```

## 5. Phase 2: 方案确认（用户审核①）

### 5.1 动作

将 Phase 1 的匹配结果展示给用户，等待用户确认。

### 5.2 交互规则

- 如果用户对场景/方案/决策点有修正，回到 Phase 1 重新匹配
- 如果用户确认，进入 Phase 3
- 明确告知用户："请确认以上匹配结果，如有问题请指出。确认后将进入参数收集阶段。"

## 6. Phase 3: 参数收集

### 6.1 目标

为每条业务列出完整的配置参数，要求用户提供缺失的值。

### 6.2 工作步骤

**Step 1: 从需求和现网中推断参数**

尽可能从以下来源自动推断：
- 用户需求描述（业务名、匹配条件、计费方式等）
- 现网配置（命名规律、已有参数值）
- 业务图谱中的套餐示例
- 知识库中的默认值

> **查阅知识文件**：
> - `knowledge/计费知识库.md` §6(URRID vs RG vs SID) — 参数语义解释
> - `knowledge/计费知识库.md` §7(常见配置模式) — 默认参数组合
> - `knowledge/计费知识库.md` §11.2(UNC URR特有参数) — SMF侧参数差异

**Step 2: 列出每条业务的参数表**

对每条业务，按以下维度展示参数：

```markdown
### 业务 {N}: {业务名称}

| 参数项 | UPF(UDG)侧 | SMF(UNC)侧 | 来源 | 状态 |
|--------|-----------|-----------|------|------|
| **识别条件** | | | | |
| 匹配方式 | {L34/L7 URL/L7协议} | — | 需求/推断 | 已知/待确认 |
| L34协议 | {ANY/TCP/...} | — | 需求 | 已知/待确认 |
| L7 URL/协议 | {具体值} | — | 需求 | 已知/待确认 |
| **计费参数（两侧共用）** | | | | |
| 计费方式 | USAGERPTMODE={OFFLINE/ONLINE} | 同UPF | DP-01 | 已知 |
| URRID | {数值} | **必须与UPF一致** | 需用户提供 | **待提供** |
| RG(费率组) | {数值} | **必须与UPF一致** | 需用户提供 | **待提供** |
| 计量方式 | ONLMETERINGTYPE/OFFMETERINGTYPE | **必须与UPF一致** | 需求/推断 | 已知/待确认 |
| **SMF特有参数** | | | | |
| 复合类型 | — | OFFCOMPOUNDTYPE/ONLCOMPOUNDTYPE | 推断(默认ONLYRG) | 已知/待确认 |
| 配额阈值 | — | TIMERSUVALUE/VOLUMERSUVALUE | 需用户提供 | 待提供(仅在线) |
| **命名** | | | | |
| FILTER名 | {建议值} | — | 推断 | 已知/待确认 |
| L7FILTER名 | {建议值} | — | 推断 | 已知/待确认 |
| FLOWFILTER名 | {建议值} | — | 推断 | 已知/待确认 |
| URR名 | {建议值} | {建议值} | 推断 | 已知/待确认 |
| RULE名 | {建议值} | **必须与UPF一致** | 推断 | 已知/待确认 |
| **其他** | | | | |
| 优先级 | {数值} | {数值} | 推断 | 已知/待确认 |
```

**Step 3: 全局参数**

```markdown
### 全局参数

| 参数项 | UPF(UDG)侧 | SMF(UNC)侧 | 来源 | 状态 |
|--------|-----------|-----------|------|------|
| UserProfile名 | {值} | **必须与UPF一致** | 现网/需求 | 已知/待确认 |
| 默认URR组(DFTURRGRPNAME) | {值} | {值} | 现网/推断 | 已知/待确认 |
| 配额耗尽动作 | {BLOCK/...} | — | DP-02 | 已知 |
| **SMF系统级参数**（仅DP-00含SMF时） | | | | |
| 计费接口模式 | — | SET CHGMODE: FORCED=? | 需求/推断 | 已知/待确认 |
| CC属性 | — | ADD CHARGECHAR: CCVALUE=? | 需用户提供 | **待提供** |
| CHF/OCS连接 | — | 已配置/未配置 | 现网 | 已知/待确认 |
| CCT/DCC模板 | — | 已配置/未配置 | 现网 | 已知/待确认 |
```

### 6.3 推断规则

从现网配置中推断命名规律：
- 如果现网 FILTER 命名为 `filter_xxx`，则新 FILTER 建议用相同前缀
- 如果现网 URR 命名为 `urr_xxx`，则新 URR 建议用相同前缀
- 优先级：参考现网已有 RULE 的 PRIORITY 分布，保持合理间距

从知识库推断默认值：
- URRID: 建议与 RG 保持一致
- DFTSIGURRGNAME: 与 DFTURRGRPNAME 保持一致
- UPURRNAME1 / DOWNURRNAME1: 在线计费时通常相同

### 6.4 输出

将参数表展示给用户，标注所有"待提供"和"待确认"项，要求用户补充。

## 7. Phase 4: 参数确认（用户审核②）

### 7.1 动作

用户填写或修正参数后，进行参数合理性校验。

### 7.2 校验规则

| 校验项 | 规则 | 知识来源 |
|--------|------|---------|
| URRID 唯一性 | 同一 UserProfile 下 URRID 不能重复 | 命令文档 |
| RG 范围 | 数值范围需合理 | 命令文档 |
| 命名冲突 | 不能与现网同名对象冲突（除非是修改） | 通用规则 |
| 计量方式一致性 | USAGERPTMODE 与 ONLMETERINGTYPE/OFFMETERINGTYPE 匹配 | 知识库 |
| FILTER必要性 | 每条业务至少有一个匹配条件 | 图谱规则 |
| 三件套完整性 | 每条业务必须有 URR + URRGROUP + PCCPOLICYGRP | 知识库 |
| 优先级间距 | 同类型 RULE 之间优先级有间距，便于后续插入 | 经验规则 |

### 7.3 交互规则

- 校验通过：进入 Phase 5
- 校验不通过：列出问题，要求用户修正后重新校验
- 用户可以调整任何参数值

## 8. Phase 5: 配置生成

### 8.1 目标

根据确认的 LLD 参数表，按依赖顺序生成完整的 MML 配置脚本。
根据 DP-00 决策，生成 UPF(UDG)侧、SMF(UNC)侧或两侧的命令。

> **查阅知识文件**：
> - `knowledge/计费知识库.md` §2(配置对象体系)、§3(计费动作链) — UPF侧对象层次
> - `knowledge/计费知识库.md` §8(命令执行顺序)、§21(SMF侧配置顺序) — 两侧命令排序
> - `knowledge/计费知识库.md` §11-20 — SMF侧各子系统命令详情
> - `knowledge/方案设计-配置全景.md` Ch12-13 — 融合计费配置全景和三件套

### 8.2 命令生成模板 — UPF(UDG)侧

每条业务按以下模板生成命令（按依赖顺序）：

```
!-- 1. 底层过滤条件 (如需新建)
ADD FILTER:FILTERNAME="{filter_name}",L34PROTTYPE=STRING,L34PROTOCOL={l34_protocol};
ADD L7FILTER:L7FILTERNAME="{l7_name}",URLTYPE=URL,URL="{url}";  (仅L7 URL场景)

!-- 2. 流过滤器与绑定
ADD FLOWFILTER:FLOWFILTERNAME="{ff_name}";
ADD FLTBINDFLOWF:FLOWFILTERNAME="{ff_name}",FILTERNAME="{filter_name}";
ADD PROTBINDFLOWF:FLOWFILTERNAME="{ff_name}",PROTOCOLNAME="{protocol}",L7FILTERNAME="{l7_name}";  (仅L7场景)

!-- 3. 计费三件套
ADD URR:URRNAME="{urr_name}",URRID={urrid},USAGERPTMODE={mode},ONLMETERINGTYPE={metering},RG={rg};
ADD URRGROUP:URRGROUPNAME="{urrg_name}",UPURRNAME1="{urr_name}",DOWNURRNAME1="{urr_name}";
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="{ppg_name}",URRGROUPNAME="{urrg_name}";

!-- 4. 规则
ADD RULE:RULENAME="{rule_name}",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="{ff_name}",PRIORITY={priority},POLICYNAME="{ppg_name}";
```

### 8.3 命令生成模板 — SMF(UNC)侧

当 DP-00 包含 SMF 时，额外生成以下命令。

> **查阅知识文件**：`knowledge/计费知识库.md` §21(SMF侧配置顺序)、§16(CCT模板)、§18(DCC模板)

**8.3.1 SMF 系统级命令（仅需检查，已配置则跳过）**

```
!-- 0. 系统级前置（如现网已有则跳过）
SET PCCFUNC:HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE;
SET CHGMODE:FORCED=NchfMode;  (融合计费) / SET CHGMODE:FORCED=GaGyMode;  (在线+离线)
ADD CHARGECHAR:CCVALUE=0x0800,CCNAME="normal";  (按需)
!-- CHF/OCS连接、CCT/DCC模板等通常已在系统部署时完成
```

**8.3.2 SMF 业务级命令（每条业务执行，需与 UPF 侧参数一致）**

```
!-- 1. URR（每业务每计费方式一个）
!-- 离线
ADD URR:URRNAME="{smf_offline_urr}",URRID={urrid},USAGERPTMODE=OFFLINE,
     OFFCOMPOUNDTYPE=ONLYRG,RG={rg},OFFMETERINGTYPE={metering};
!-- 在线
ADD URR:URRNAME="{smf_online_urr}",URRID={urrid},USAGERPTMODE=ONLINE,
     ONLCOMPOUNDTYPE=ONLYRG,ONLINERG={rg},ONLMETERINGTYPE={metering};
!-- 融合：创建 ONLINE + OFFLINE 两个 URR

!-- 2. URRGROUP
ADD URRGROUP:URRGROUPNAME="{smf_urrg}",
     UPURRNAME1="{smf_online_urr}",DOWNURRNAME1="{smf_online_urr}",    // 1号位=ONLINE
     UPURRNAME2="{smf_offline_urr}",DOWNURRNAME2="{smf_offline_urr}";  // 2号位=OFFLINE

!-- 3. PCC策略组
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="{smf_ppg}",URRGROUPNAME="{smf_urrg}";

!-- 4. RULE（需与UPF侧RULENAME、POLICYTYPE、POLICYNAME一致）
ADD RULE:RULENAME="{rule_name}",POLICYTYPE=PCC,PRIORITY={priority},POLICYNAME="{smf_ppg}";

!-- 5. 绑定
ADD RULEBINDING:USERPROFILENAME="{userprofile}",RULENAME="{rule_name}";
```

### 8.4 参数映射规则

**UPF(UDG)侧**：

| 规划参数 | 目标命令 | 参数名 | 映射规则 |
|---------|---------|--------|---------|
| 计费方式=离线 | ADD URR | USAGERPTMODE | OFFLINE |
| 计费方式=在线 | ADD URR | USAGERPTMODE | ONLINE |
| 计费方式=融合 | ADD URR x2 | USAGERPTMODE | 一个OFFLINE + 一个ONLINE（双URR，见§12.4） |
| 计量方式=流量 | ADD URR | ONLMETERINGTYPE / OFFMETERINGTYPE | VOLUME |
| 计量方式=时长 | ADD URR | ONLMETERINGTYPE / OFFMETERINGTYPE | DURATION |
| 计量方式=免费 | ADD URR | OFFMETERINGTYPE | FREE |
| 配额动作=BLOCK | ADD PCCACTIONPROP | GATINGSTATUS | CLS |
| 匹配=L34 ANY | ADD FILTER | L34PROTOCOL | ANY |
| 匹配=L7 URL | ADD L7FILTER + PROTBINDFLOWF | URLTYPE+URL+L7FILTERNAME | 见知识库URL匹配模式 |
| 匹配=L7 协议 | PROTBINDFLOWF | PROTOCOLNAME | 不带 L7FILTERNAME |

**SMF(UNC)侧特有映射**：

| 规划参数 | 目标命令 | 参数名 | 映射规则 |
|---------|---------|--------|---------|
| 计费接口=融合 | SET CHGMODE | FORCED | NchfMode |
| 计费接口=在线+离线 | SET CHGMODE | FORCED | GaGyMode |
| 复合类型(离线) | ADD URR | OFFCOMPOUNDTYPE | 默认 ONLYRG |
| 复合类型(在线) | ADD URR | ONLCOMPOUNDTYPE | 默认 ONLYRG |
| 在线配额-流量 | ADD URR | VOLUMERSUVALUE | 字节，需用户提供 |
| 在线配额-时长 | ADD URR | TIMERSUVALUE | 秒，需用户提供 |
| CC属性 | ADD CHARGECHAR | CCVALUE | 0x0800=普通计费(默认) |

### 8.5 特殊场景处理

**融合计费（DP-01=融合）**：
- UPF侧：创建**两个独立URR**，一个OFFLINE一个ONLINE，放入同一URRGROUP
- SMF侧：同样创建两个URR，OFFCOMPOUNDTYPE/ONLCOMPOUNDTYPE分别配置
- **注意**：UDG ADD URR 的 USAGERPTMODE 枚举值只有 OFFLINE/ONLINE/MONITORINGKEY/QOS，无 OFFLINE_AND_ONLINE

**配额耗尽BLOCK（DP-02=BLOCK）**：
- UPF侧：额外创建 PCCACTIONPROP 对象，绑定到默认业务的 PCCPOLICYGRP
- SMF侧：SET FAILHANDLING 配置超时处理动作

**多业务共用 FILTER**：
- UPF侧：底层 FILTER 可复用，但 URR/URRGROUP/PCCPOLICYGRP 每条业务独立（三件套原则）
- SMF侧：RULE/POLICYNAME 按业务独立

### 8.6 排序规则

**UPF(UDG)侧执行顺序**（严格）：

```
1. FILTER                    (底层)
2. L7FILTER                  (底层)
3. FLOWFILTER                (中间)
4. FLTBINDFLOWF / PROTBINDFLOWF (绑定)
5. URR / PCCACTIONPROP       (策略动作)
6. URRGROUP / PCCPOLICYGRP   (策略组合)
7. RULE                      (汇聚)
8. USERPROFILE               (容器, 仅新建时)
9. URRGRPBINDING             (默认计费组绑定)
10. RULEBINDING              (规则绑定)
11. REFRESHSRV               (刷新生效, 必须最后)
```

**SMF(UNC)侧执行顺序**：
- 系统级命令在前（仅检查，已存在则跳过）
- 业务级命令参照 UPF 侧三件套顺序
- 无 REFRESHSRV

## 9. Phase 6: 配置核查（循环修正）

### 9.1 目标

对生成的配置脚本进行全量核查，发现并修正问题，循环直到全部通过。

> **查阅知识文件**：
> - `knowledge/计费知识库.md` §9(配置生效时机) — REFRESHSRV 和生效时机
> - `knowledge/计费知识库.md` §10(常见陷阱) — 典型配置错误
> - `knowledge/计费知识库.md` §22(补充隐性规则) — RGAPPLIED约束、跨网元一致性
> - `knowledge/故障案例与运维.md` — 已知故障模式参考

### 9.2 核查维度

#### 9.2.1 图谱规则核查

| 核查项 | 规则 | 来源 |
|--------|------|------|
| Task编排正确性 | 命令顺序是否符合图谱定义的依赖链 | 业务图谱 |
| 决策点一致性 | DP-01/02/03 的答案是否在参数中正确体现 | 业务图谱 |
| 三件套独立性 | 每条业务的 URR/URRGROUP/PCCPOLICYGRP 是否独立 | 知识库 |

#### 9.2.2 配置依赖核查

| 核查项 | 规则 |
|--------|------|
| 引用完整性 | RULE 引用的 FLOWFILTERNAME 和 POLICYNAME 是否存在 |
| 绑定完整性 | FLOWFILTER 是否绑定了 FILTER（通过 FLTBINDFLOWF） |
| 三件套闭合 | PCCPOLICYGRP 是否引用了存在的 URRGROUP，URRGROUP 是否引用了存在的 URR |
| 绑定一致性 | RULEBINDING 的 POLICYTYPE 是否与 RULE 一致 |
| 默认组存在 | URRGRPBINDING 的 DFTURRGRPNAME 是否指向存在的 URRGROUP |

#### 9.2.3 知识库规则核查

| 核查项 | 规则 | 来源 |
|--------|------|------|
| REFRESHSRV 最后 | 刷新命令必须在所有配置命令之后 | 知识库 §2 |
| 计量方式匹配 | USAGERPTMODE 与 METERINGTYPE 参数组合是否合法 | 知识库 §3 |
| URL匹配双协议 | URL 匹配场景默认绑定 HTTP + HTTPS | 知识库 §12 |
| 命名规范 | 对象命名是否符合现网规律 | 推断 |
| 兜底规则 | 是否有 FILTER=ANY 的兜底 RULE | 知识库 §7.5 |
| 双重兜底一致 | 显式兜底 RULE 的计费组与 DFTURRGRPNAME 是否一致 | 知识库 §5.2 |

#### 9.2.4 现网冲突核查

| 核查项 | 规则 |
|--------|------|
| 同名冲突 | 新增对象名是否与现网已有对象同名 |
| 参数覆盖 | SET 命令是否覆盖了现网中仍在使用的参数 |
| 共享对象影响 | 修改被多个 RULE 引用的共享对象时，是否评估影响范围 |
| 删除安全性 | RMV 命令是否先解绑了上层引用 |

#### 9.2.5 跨网元一致性核查（仅 DP-00 包含 UPF+SMF 时）

> **查阅知识文件**：`knowledge/计费知识库.md` §22.2(跨网元名称一致性汇总)

| 核查项 | 规则 | 严重级别 |
|--------|------|---------|
| USERPROFILENAME 一致 | UPF 和 SMF 的 USERPROFILENAME 必须相同 | CRITICAL |
| RULENAME 一致 | UPF 和 SMF 的 RULE.RULENAME 必须相同 | CRITICAL |
| POLICYTYPE+POLICYNAME 一致 | UPF 和 SMF 的 RULE.POLICYTYPE+POLICYNAME 必须相同 | CRITICAL |
| URRID 一致 | UPF URR.URRID 和 SMF URR.URRID 必须相同 | CRITICAL |
| USAGERPTMODE 一致 | UPF URR.USAGERPTMODE 和 SMF URR.USAGERPTMODE 必须相同 | CRITICAL |
| METERINGTYPE 一致 | UPF URR.METERINGTYPE 和 SMF URR.METERINGTYPE 必须相同 | CRITICAL |
| RG 一致 | UPF URR.RG 和 SMF URR.RG/ONLINERG 必须相同 | CRITICAL |
| SMF系统级前置 | PCCFUNC、CHGMODE、CHF/OCS连接是否已配置 | HIGH |

### 9.3 修正规则

- 发现问题时，**自动修正**并在输出中告知用户修正内容
- 无法自动修正的问题，**暂停并要求用户决策**
- 修正后重新进入核查，直到全部通过
- 每轮核查记录修正日志

### 9.4 核查输出

```markdown
## 核查报告

### 核查结果: {通过 / 已修正}

| 维度 | 检查项数 | 通过 | 修正 | 待确认 |
|------|---------|------|------|--------|
| 图谱规则 | {n} | {n} | {n} | {n} |
| 配置依赖 | {n} | {n} | {n} | {n} |
| 知识库规则 | {n} | {n} | {n} | {n} |
| 现网冲突 | {n} | {n} | {n} | {n} |
| 跨网元一致 | {n} | {n} | {n} | {n} |

### 修正日志
1. {问题描述} → {修正动作}
2. ...
```

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

**SMF(UNC)侧脚本**（当 DP-00 包含 SMF 时）：

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
- 决策: DP-00={}, DP-01={}, DP-02={}, DP-03={}

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

### 复用现网对象清单
| ConfigObject | 对象名 | 说明 |
|-------------|--------|------|
| FILTER | {name} | 现网已有，直接引用 |

### 注意事项
- {需人工确认的事项}
```

## 11. Agent 执行约束

1. **现网配置为必须**：所有动网信息基于现网配置构建
2. **严格按依赖顺序**：不可跳过底层对象直接配置上层
3. **REFRESHSRV 必须最后**：所有配置完成后才刷新（仅UPF侧）
4. **三件套独立原则**：每条业务的 URR/URRGROUP/PCCPOLICYGRP 彼此独立
5. **追问而非猜测**：缺失决策信息或参数时必须追问，不可自行推断必填参数的值
6. **动网保守原则**：对现网对象的修改必须有明确的用户确认
7. **知识库优先**：知识库中的特殊规则优先于通用规则
8. **命名遵循现网**：新对象命名尽量遵循现网已有的命名规律
9. **跨网元一致**：UPF 和 SMF 两侧的 URRID/RG/USAGERPTMODE/RULENAME/USERPROFILENAME 必须一致
10. **SMF 系统级检查**：SMF 侧系统级配置（PCCFUNC/CHGMODE/CHF连接）通常已部署，仅检查确认

## 12. 常见配置模式

### 12.1 OR 条件：FLOWFILTERGRP vs 多 RULE

当多个匹配条件之间是"或"关系时：

| 方案 | 实现方式 | 适用场景 |
|------|---------|---------|
| FLOWFILTERGRP | 多个 FLOWFILTER 编入同一组，一条 RULE 引用 | 多个条件执行**完全相同**的动作 |
| 多 RULE | 每个条件一个 RULE，各自引用相同 POLICYNAME | 需要不同优先级或后续可能分化 |

**默认**：使用 FLOWFILTERGRP，更简洁。

### 12.2 URL 匹配的协议绑定

当用户提到"访问某网站"时，HTTP 和 HTTPS 都需要匹配：

```mml
ADD PROTBINDFLOWF:FLOWFILTERNAME="ff_xxx",PROTOCOLNAME="http",L7FILTERNAME="l7_xxx";
ADD PROTBINDFLOWF:FLOWFILTERNAME="ff_xxx",PROTOCOLNAME="https",L7FILTERNAME="l7_xxx";
```

如果用户明确只关注某种协议，则只绑定该协议。

### 12.3 兜底规则设计

| 机制 | 命令 | 触发条件 |
|------|------|---------|
| 默认URR组 | SET URRGRPBINDING:DFTURRGRPNAME=... | 流量未命中任何 RULE |
| 显式兜底RULE | ADD RULE(FILTER=ANY, 低PRIORITY) | 流量命中 FILTER=ANY 的 RULE |

**规则**：两者应指向同一计费组，保持双路径一致。

### 12.4 计费方式参数组合

| DP-01 | USAGERPTMODE | 需配置的计量参数 |
|-------|-------------|----------------|
| 离线 | OFFLINE | OFFMETERINGTYPE |
| 在线 | ONLINE | ONLMETERINGTYPE |
| 融合 | 双URR: 一个OFFLINE + 一个ONLINE | OFFLINE URR→OFFMETERINGTYPE；ONLINE URR→ONLMETERINGTYPE |

### 12.5 PROTBINDFLOWF 绑定模式

| 匹配方式 | PROTBINDFLOWF 参数 | 说明 |
|---------|-------------------|------|
| L34 only | 不需要 PROTBINDFLOWF | 仅 FILTER 层匹配 |
| L7 URL | PROTOCOLNAME="http/https" + L7FILTERNAME | URL 匹配 |
| L7 协议 | PROTOCOLNAME="{协议名}" | 不带 L7FILTERNAME |
| L7 协议组 | 逐个绑定组内协议 | 需确认组内协议列表 |

## 13. 参数语义说明

### 13.1 URRID 与 RG

| 参数 | 含义 | 说明 |
|------|------|------|
| URRID | PFCP Session Report 中的使用量上报规则标识 | 用于关联计费记录 |
| RG | 3GPP 定义的费率分组标识(Rating Group) | CHF/CG 用此值匹配费率策略 |

**规则**：URRID 和 RG 独立，但建议保持一致的映射关系便于运维。

### 13.2 DFTURRGRPNAME 与显式兜底

| 机制 | 命令 | 适用 |
|------|------|------|
| 默认URR组 | SET URRGRPBINDING:DFTURRGRPNAME | 没有显式兜底 RULE 时必须配置 |
| 显式兜底RULE | ADD RULE(FILTER=ANY, 低PRIORITY) + ADD RULEBINDING | 更灵活，可同时指定策略动作 |

DFTSIGURRGNAME 与 DFTURRGRPNAME 保持一致。

### 13.3 FILTER 三种匹配模式

| 模式 | 配置方式 | 场景 |
|------|---------|------|
| L34 ANY | L34PROTOCOL=ANY | 兜底/默认业务 |
| L34 精确 | L34PROTOCOL=TCP + 端口/IP | 基于IP/端口匹配 |
| L7 URL | PROTBINDFLOWF + L7FILTER | 基于URL匹配 |
| L7 协议 | PROTBINDFLOWF(不带L7FILTERNAME) | 基于协议识别匹配 |
