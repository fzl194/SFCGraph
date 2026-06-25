# Phase 3 参考文件：参数收集

## ⚠ 阶段执行约束（必须遵守）

**本文件仅用于 Phase 3。执行本文件内容前必须满足以下前置条件，否则 STOP：**

1. **用户必须已确认方案**：必须已通过 GATE-1（用户在 Phase 2 明确确认了匹配结果）。如果用户未确认方案，**STOP**，回到 Phase 2 等待用户确认。
2. **本阶段完成后必须 STOP**：执行完 §1~§4 后，**必须生成并展示 `xxxLLD.md` 后停止执行**，等待用户在 Phase 4（GATE-2）确认。`LLD` 就是 markdown 形式的规划数据表，不再拆成第二份同义文档。不得自动进入配置生成。
3. **禁止在本阶段生成任何 MML 配置命令**：本阶段只收集和推断参数，不生成配置。
4. **禁止与方案同轮输出**：如果当前轮 assistant 刚展示过 `xxx方案.md` 并请求 GATE-1 确认，则本轮不得进入本文件内容；只有用户在下一条消息中明确确认方案后，才能开始生成 `xxxLLD.md`。

---

> 本文件定义 Phase 3 的 pipeline 要求、输出模板和操作规则（带宽控制场景专属）。
> 业务知识（参数语义、默认值、推导规则）由 Agent 从图谱和知识库动态加载。

---

## 1. Pipeline 步骤

### Step 1: 从需求和现网中推断参数

**操作**：尽可能从以下来源自动推断参数值：
- 用户需求描述（业务名、控制目标带宽、控制机制、套餐配额等）
- 现网配置（命名规律、已有参数值、License 开启状态）
- 业务图谱中的方案示例（`01-business-graph.md` §10 端到端链路）
- 知识库中的默认值与参数语义

**必须加载**：
- `kb/02-CAR限速参数.md` + `kb/04-令牌桶与三色标记.md` — CIR/PIR/CBS/PBS 语义与推导
- `kb/03-Shaping整形.md` — RATE/QUEDEPTH、智能 Shaping 参数
- `kb/05-FUP配额降速.md` — URR.USAGERPTMODE / VOLUMETHRESHOLD / Monitoring-Level
- `kb/06-GBR带宽保证.md` — QOSPROP 的 5QI/QCI/MBR/GBR/ARP
- `04-command-graph.md` §5 — 读取 CommandParameter 定义，确认参数枚举值和约束

**核心参数推导规则**（按控制机制分支）：

| 控制机制 (DP-BW-01) | 核心参数 | 推导要点 |
|---------------------|---------|---------|
| CAR限速 | CIR / PIR / CBS / PBS + GREENACT/YELLOWACT/REDACT | CIR=承诺速率、PIR=峰值；CBS/PBS 建议按 `CIR(ms)×时间窗口` 推导；动作按业务价值定（低价值 DISCARD，高价值 REMARK） |
| Shaping整形 | RATE / QUEDEPTH | RATE=整形目标速率；QUEDEPTH 按抖动容忍度推导（视频大、P2P 小） |
| 智能Shaping | RATE/QUEDEPTH + SRVLEVELSPEC/WORKMODE/USERFAIREN/MAXPKTLOSTRATE | AUTO 模式需配 MAXPKTLOSTRATE + PKTLOSTRATEDTL；按 ServiceLevel 配 BCSRVLEVELPLY |
| FUP降速 | URR.VOLUMETHRESHOLD + 降速后 MBR | 会话级=ONLINE/MONITORINGKEY，业务级=MONITORINGKEY；阈值=套餐配额字节数；降速靠 PCRF 下发高优先级新 QoS |
| GBR保证 | QOSPROP.GBRUL/GBRDL + 5QI/QCI + ARP | 5G 用 FQI(QOS_FLOW_PARA)，2/3/4G 用 QCIVALUE(QOS_BEARER_PARA)；GBR=保证下限 |

**推断规则**（现网命名规律）：
- 如果现网 BWMSERVICE 命名为 `xxx_svc`，则新建建议用相同后缀
- 如果现网 BWMCONTROLLER 命名为 `xxx_car` / `xxx_shaping`，按 CTRLTYPE 保持一致
- BWMRULEPRI / RULE.PRIORITY 参考现网分布，保持合理间距（见 §3 优先级分析）

### Step 2: 列出参数表

**操作**：对每条业务按模板展示参数，标注所有"待提供"和"待确认"项。

**必须加载**：
- `04-command-graph.md` §5 — 读取各核心命令的参数列表（BWMCONTROLLER/BWMRULE/RULE/URR/QOSPROP/ADCPARA）
- `01-business-graph.md` §5 — 读取 SemanticObject 定义（SO-BW-01~08），确认两侧参数差异

### Step 3: 全局参数

**操作**：列出不属于单条业务的全局参数（License、BWM 全局使能、SA 特征库、UNC 侧 PCRF/PCCFUNC 等）。

**必须加载**（当 DP-BW-08 包含 UNC 时）：
- `kb/09-UNC控制面协同.md` — UNC 侧 PCRF 组/PCCFUNC/故障定时器/N7 属性参数
- `kb/08-License前置门控.md` — UDG/UNC 各特性的 License 编号

---

## 2. 输出格式模板

### 业务参数表（BWM 限速/整形场景，CS-BW-01）

```markdown
### 业务 {N}: {业务名称}

| 参数项 | UDG(UDG)侧 | UNC(UNC)侧 | 来源 | 状态 |
|--------|-----------|-----------|------|------|
| **业务识别** | | | | |
| SVC/APP 类型 | {值} | — | 需求 | 已知/待确认 |
| CATEGORYPROP | {建议值} | — | 推断 | 已知/待确认 |
| **BWM 服务** | | | | |
| BWMSERVICE 名 | {建议值} | — | 推断 | 已知/待确认 |
| BWMSERVICETYPE | {NONTOS/...} | — | 需求 | 已知/待确认 |
| PROTOCOLNAME | {bittorrent/...} | — | 需求 | 已知/待确认 |
| **BWM 控制器 (DP-BW-05)** | | | | |
| BWMCNAME | {建议值} | — | 推断 | 已知/待确认 |
| CTRLTYPE | {CAR/SHAPING} | — | DP-BW-05 | 已知 |
| CIR/PIR/CBS/PBS | {kbps/bytes} | — | 需求+推导 | 待确认 |
| 或 RATE/QUEDEPTH | {kbps/packets} | — | 需求+推导 | 待确认 |
| GREENACT/YELLOWACT/REDACT | {PASS/REMARK/DISCARD} | — | kb/04 | 待确认 |
| **BWM 用户组与规则** | | | | |
| USERGROUPNAME | {建议值} | — | 推断 | 已知/待确认 |
| BWMRULETYPE | {SUBSCRIBER_SPECIFIC/GROUP_SPECIFIC/GLOBAL} | — | DP-BW-02 | 已知 |
| BWMRULEPRI | {数值} | — | 见 §3 优先级 | 待确认 |
| **UNC 侧规则 (双产品协作时)** | | | | |
| RULENAME | {建议值} | **必须与 UDG 一致** | 推断 | 待确认 |
| POLICYTYPE | BWM | BWM | 固定 | 已知 |
| PRIORITY | {数值} | **必须与 UDG 一致** | 见 §3 | 待确认 |
```

### 业务参数表（FUP 降速场景，CS-BW-02）

```markdown
### 业务 {N}: {业务名称}（FUP 降速）

| 参数项 | UDG(UDG)侧 | UNC(UNC)侧 | 来源 | 状态 |
|--------|-----------|-----------|------|------|
| **URR 配置** | | | | |
| URRID | {数值} | {数值} | 需用户提供 | **待提供** |
| USAGERPTMODE | {ONLINE/MONITORINGKEY} | {同 UDG} | DP-BW-06 | 已知 |
| MEASUREMENTMETHOD | {VOLUME/DURATION} | {同 UDG} | 需求 | 已知/待确认 |
| VOLUMETHRESHOLD | {bytes} | {同 UDG} | 套餐配额 | **待提供** |
| **URR 组/策略组** | | | | |
| URRGROUPNAME | {建议值} | {建议值} | 推断 | 待确认 |
| PCCPOLICYGRP | {建议值} | {建议值} | 推断 | 待确认 |
| **降速后 QoS（PCRF 下发）** | | | | |
| 降速 MBR | {kbps} | {kbps} | 需求 | **待提供** |
| 降速规则 PRIORITY | {最高优先级} | {最高优先级} | BR-BW-02 | 已知 |
```

### 业务参数表（GBR 保证场景，CS-BW-03）

```markdown
### 业务 {N}: {业务名称}（GBR 保证）

| 参数项 | UDG(UDG)侧 | UNC(UNC)侧 | 来源 | 状态 |
|--------|-----------|-----------|------|------|
| **URR (QoS 事件上报)** | | | | |
| URRID | {数值} | {数值} | 需用户提供 | **待提供** |
| USAGERPTMODE | QOS | QOS | TR-BW-04 | 已知 |
| **QoS 属性 (DP-BW-04)** | | | | |
| QOSPROPNAME | {建议值} | {建议值} | 推断 | 待确认 |
| QOSTYPE | {QOS_FLOW_PARA(5G) / QOS_BEARER_PARA(4G)} | 同 UDG | DP-BW-04 | 已知 |
| FQI (5G) | {0-255} | {同 UDG} | 需求 | 待确认 |
| QCIVALUE (4G) | {1-9} | {同 UDG} | 需求 | 待确认 |
| MBRUL/MBRDL | {kbps} | {同 UDG} | 需求 | 待确认 |
| GBRUL/GBRDL | {kbps} | {同 UDG} | 需求 | **待提供** |
| ARP | {1-15} | {同 UDG} | 需求 | 待确认 |
```

### 全局参数表

```markdown
### 全局参数

| 参数项 | UDG(UDG)侧 | UNC(UNC)侧 | 来源 | 状态 |
|--------|-----------|-----------|------|------|
| License 项 | {LKV3G5SABS01/PCCB01/TCSA01...} | {LKV3TCBSA01...} | kb/08 | 已知/待确认 |
| BWM 全局使能 | SET BANDWIDTHMNG:SWITCH=ENABLE | — | 现网/需求 | 待确认 |
| SA 特征库 | LOD SIGNATUREDB/PARSERDB | — | 现网 | 待确认 |
| PCRF 组 | — | {PCRFGROUPNAME/SELECTMODE} | 现网/推断 | 待确认 |
| PCCFUNC | — | {MKPARSEFORMAT/FUPSESSIONEXC} | DP-BW-04 | 待确认 |
```

---

## 3. 优先级分析流程（必须独立执行，必须用户确认）

> **核心规则**：**数字越小，优先级越高**。不可更改。该规则与 `../业务感知域规则.md §3` 一致。

### 步骤

1. 从现网配置中提取**所有 RULE 的 PRIORITY 值**和**所有 BWMRULE 的 BWMRULEPRI 值**（两套优先级独立），用 Grep 搜索 `PRIORITY` 和 `BWMRULEPRI`
2. 分析现网优先级分布规律（现网数据是最权威判断依据）
3. 根据用户描述的业务优先级关系，计算新规则 PRIORITY / BWMRULEPRI（间距取 10 的倍数）
4. 输出分析表（含现网分布 + 新规则拟插入位置）
5. **STOP。将分析表展示给用户，等待用户确认优先级值。**

### FUP 降速优先级特殊规则（BR-BW-02）

FUP 降速规则必须使用**最高优先级**（PRIORITY 数值最小），且 FlowFilter 必须**完全覆盖**原保障规则（端口号范围一致），否则部分流量降速、部分不受影响。

### STOP 条件

**完成分析表后必须 STOP，明确要求用户确认优先级。在用户确认之前：**

- **禁止**生成带 PRIORITY 的 RULE 命令、带 BWMRULEPRI 的 BWMRULE 命令
- **禁止**进入 Phase 5 配置生成
- 用户要求调整 → 重新计算，再次等待确认

### 输出格式

```
## 优先级分析

**规则**：数字越小优先级越高（固定规则）

**现网 RULE.PRIORITY 分布（全部 RULE，按 POLICYTYPE 分组）**：
| RULE 名称 | POLICYTYPE | PRIORITY | 说明 |
|-----------|-----------|----------|------|
| 现网rule1 | BWM | 21 | {...} |
| 现网rule2 | QOS | 31 | {...} |
| **新rule_xxx** | **{类型}** | **{拟提议值}** | **{新业务}** |

**现网 BWMRULE.BWMRULEPRI 分布**：
| BWMRULE 名 | BWMRULETYPE | BWMRULEPRI | 说明 |
|------------|-------------|-----------|------|
| ... | ... | ... | ... |

**请确认新规则的优先级设置是否合理。如需调整请告知。**
```

### 禁止事项

- **禁止**自行假设优先级顺序，必须先从现网提取全部 RULE/BWMRULE 的优先级数据
- **禁止**只提取带宽相关 RULE，必须提取现网所有 RULE 的 PRIORITY 分布
- **禁止**在用户未确认优先级前生成任何带 PRIORITY / BWMRULEPRI 的命令

---

## 4. 注意事项

- 参数表中每个字段都应标注"来源"（需求/现网/推断/图谱/知识库）和"状态"（已知/待确认/待提供）
- 两侧共用参数（RULENAME、PRIORITY、URRID、VOLUMETHRESHOLD 等）必须标注"**必须与 UDG 一致**"（CR-BW-05、BR-BW-01）
- UNC 侧参数差异需要从 `kb/09-UNC控制面协同.md` 确认，不要凭记忆填写
- CTRLTYPE 决定 BWMCONTROLLER 参数集（CR-BW-02）：CAR 用 CIR/PIR/CBS/PBS，SHAPING 用 RATE/QUEDEPTH，**两者参数集互斥**，不要同时填
- CAR 与 Shaping 不可同对象叠加（CR-BW-03）：同一 BWMSERVICE 不能同时绑 CAR 控制器和 Shaping 控制器
- 遇到不确定的参数语义，加载 `04-command-graph.md` §5 对应命令的 CommandParameter 定义确认
