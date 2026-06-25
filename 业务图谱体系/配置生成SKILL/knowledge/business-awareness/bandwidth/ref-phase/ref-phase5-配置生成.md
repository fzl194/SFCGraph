# Phase 5 参考文件：配置生成

## ⚠ 阶段执行约束（必须遵守）

**本文件仅用于 Phase 5。执行本文件内容前必须满足以下前置条件，否则 STOP：**

1. **用户必须已确认参数表**：必须已通过 GATE-2（用户在 Phase 4 明确确认了参数表）。如果用户未确认参数，**STOP**，回到 Phase 4 等待用户确认。没有例外。
2. **方案和参数必须已确定**：必须有 Phase 1 输出的匹配结果（场景/方案/决策点）、Phase 2 产出的 `xxx方案.md`，以及 Phase 3 产出的完整 `xxxLLD.md`（必要时附 `xxx规划数据表.md`）。缺少任何一个，**STOP**，回到对应阶段补全。
3. **本阶段完成后进入 Phase 6 核查**：生成配置后必须经过 Phase 6 核查和 Phase 6.5 用户确认（GATE-3），不得直接交付给用户。

---

> 本文件定义 Phase 5 的 pipeline 要求、输出模板和排序规则（带宽控制场景专属）。
> 业务知识（参数映射、特殊场景处理规则、参数语义）由 Agent 从图谱和知识库动态加载。
> **跨场景共享时序与一致性规则见 `../业务感知域规则.md`（REFRESHSRV 时序、配置链依赖、RULE PRIORITY、三网元一致、SA 前置），本文件不复述。**

---

## 1. Pipeline 步骤

### Step 1: 加载配置规则

**必须加载**：
- `04-command-graph.md` §1 — 读取 MMLCommand 定义（55 条：UDG 30 + UNC 25）
- `04-command-graph.md` §5 — 读取各核心命令的 CommandParameter，确认参数枚举值
- `04-command-graph.md` §4 — 读取 CommandRule (CR-BW-01~05)，了解命令级约束
- `../业务感知域规则.md` — **域共享规则**（执行时序 §1、跨网元一致性 §2、RULE PRIORITY §3、策略链独立 §4、SA 前置 §5）

**按方案闭包分支加载 kb**：
- CS-BW-01 SA-BWM → `kb/01-BWM控制体系.md` + `kb/02-CAR限速参数.md` + `kb/04-令牌桶与三色标记.md`
- CS-BW-01 Shaping 子分支 → 追加 `kb/03-Shaping整形.md`
- CS-BW-02 FUP降速 → `kb/05-FUP配额降速.md`
- CS-BW-03 GBR保证 → `kb/06-GBR带宽保证.md`
- CS-BW-04 ADC动态带宽 → `kb/07-ADC应用感知.md`
- CS-BW-06 位置区域 → `kb/10-位置区域带宽.md`
- CS-BW-05 小区负荷 → `kb/11-小区负荷动态带宽.md`
- CS-BW-07 无线优化标记 → `kb/12-无线资源优化标记.md`
- 全部方案 → `kb/08-License前置门控.md`（License 必须最先配）
- DP-BW-08 含 UNC → `kb/09-UNC控制面协同.md`

### Step 2: 按模板生成命令

根据 DP-BW-01（控制机制）+ DP-BW-08（产品面分工）决定生成范围与模板分支。

### Step 3: 按排序规则排列命令

见 §4 排序规则（基于 `../业务感知域规则.md §1.2` 配置链依赖顺序）。

### Step 4: 自检

**必须加载**：
- `01-business-graph.md` §4 — 读取 BusinessRule (BR-BW-01~06)，确认业务约束已满足
- `04-command-graph.md` §4 — 读取 CommandRule (CR-BW-01~05)，确认命令级约束已满足
- `03-task-layer.md` §8 — 读取 TaskRule (TR-BW-01~06)，确认任务级依赖已满足

---

## 2. UDG(UDG)侧输出模板

### 2.1 BWM 基础限速/整形（CS-BW-01，按依赖顺序）

```mml
!-- 0. 基础门控（首次配置或未开启时）
SET LICENSESWITCH:LICITEM="{license_item}",SWITCH=ENABLE;
LOD SIGNATUREDB:SAFILE="{signature_db_file}";      (首次或特征库升级时)
LOD PARSERDB:PRFILE="{parser_db_file}";
SET BANDWIDTHMNG:SWITCH=ENABLE;                     (BWM 全局使能)

!-- 1. 业务分类与识别（底层）
ADD CATEGORYPROP:...;                               (按需)
ADD FILTER:FILTERNAME="{filter_name}",...;          (L3/L4 场景)
ADD L7FILTER:L7FILTERNAME="{l7_name}",...;          (L7 场景，依赖 SA)

!-- 2. 流过滤器与绑定
ADD FLOWFILTER:FLOWFILTERNAME="{ff_name}";
ADD FLTBINDFLOWF:FLOWFILTERNAME="{ff_name}",FILTERNAME="{filter_name}";

!-- 3. BWM 三级控制链（核心：BWMSERVICE → BWMCONTROLLER → BWMUSERGROUP → BWMRULE）
ADD BWMSERVICE:NAME="{svc_name}",BWMSERVICETYPE={type},PROTOCOLNAME="{proto}";
ADD BWMCONTROLLER:BWMCNAME="{ctrl_name}",CTRLTYPE={CAR|SHAPING},...;   (CAR: CIR/PIR/CBS/PBS; SHAPING: RATE/QUEDEPTH)
ADD BWMUSERGROUP:USERGROUPTYPE={SPECIFIC_GROUP|GLOBAL},USERGROUPNAME="{ug_name}",USERGROUPPRI={n},USERLEVSRVTYPE={type};
ADD BWMRULE:BWMRULETYPE={SUBSCRIBER_SPECIFIC|GROUP_SPECIFIC|GLOBAL},
  BWMSERVICENAME="{svc_name}",UPBWMCTRLNAME1="{ctrl_name}",DNBWMCTRLNAME1="{ctrl_name}",
  BWMRULEPRI={pri};

!-- 3a. 智能 Shaping 子分支（CS-BW-01 + 智能Shaping，CTRLTYPE=SHAPING 时追加）
ADD BCSRVLEVELPLY:BWMCNAME="{ctrl_name}",SERVICELEVEL={n},SHAPRATE={pct};  (每个 ServiceLevel 一条)

!-- 3b. APN 绑定（按 APN/DNN 生效时）
ADD APNBINDBWMUSRG:APNNAME="{apn}",BWMUSERGROUPNAME="{ug_name}";

!-- 4. PCC 规则（仅当双产品协作且需 UDG 侧本地规则时）
ADD RULE:RULENAME="{rule_name}",POLICYTYPE=BWM,PRIORITY={pri},...;

!-- 5. 刷新生效（必须最后，仅 UDG 侧）
SET REFRESHSRV;
```

> **参数值必须从 `04-command-graph.md §5` 的 CommandParameter 定义中获取枚举值和格式要求，禁止凭记忆填写。**

### 2.2 FUP 配额降速（CS-BW-02）

```mml
!-- FUP 三件套（URR → URRGROUP → PCCPOLICYGRP，TR-BW-03 必须按序）
ADD URR:URRID={id},USAGERPTMODE={ONLINE|MONITORINGKEY},
  MEASUREMENTMETHOD={VOLUME|DURATION},VOLUMETHRESHOLD={bytes};
ADD URRGROUP:URRGROUPNAME="{urrg_name}",UPURRNAME1="{urr_name}";
ADD PCCPOLICYGRP:PCCPOLICYGRPNAME="{ppg_name}",URRGROUPNAME="{urrg_name}";

!-- 规则汇聚（POLICYTYPE=PCC，FUP 场景）
ADD RULE:RULENAME="{rule_name}",POLICYTYPE=PCC,PRIORITY={pri},
  FLOWFILTERNAME="{ff_name}",POLICYNAME="{ppg_name}";

SET REFRESHSRV;   (最后)
```

> **降速动作本身不在 UDG 配置**：URR 只负责流量累计上报，配额耗尽后由 PCRF/PCF 下发高优先级新 QoS（MBR 降低）覆盖原规则（BR-BW-02）。

### 2.3 GBR 带宽保证（CS-BW-03）

```mml
!-- QoS 事件上报 URR（USAGERPTMODE=QOS，TR-BW-04）
ADD URR:URRID={id},USAGERPTMODE=QOS,...;

!-- QoS 属性（DP-BW-04 决定 QOSTYPE）
ADD QOSPROP:QOSPROPNAME="{qos_name}",QOSTYPE={QOS_FLOW_PARA|QOS_BEARER_PARA},
  FQI={fqi},                (5G: QOS_FLOW_PARA)
  QCIVALUE={qci},           (2/3/4G: QOS_BEARER_PARA)
  MBRUL={mbr_ul},MBRDL={mbr_dl},
  GBRUL={gbr_ul},GBRDL={gbr_dl},ARP={arp};

SET REFRESHSRV;   (最后)
```

---

## 3. UNC(UNC)侧输出模板

当 DP-BW-08 包含 UNC 时，按方案追加：

### 3.1 UNC 侧 BWM 策略规则（CS-BW-01 双产品协作）

```mml
!-- 系统级前置（已配置则跳过）
SET LICENSESWITCH:LICITEM="{unc_license}",SWITCH=ENABLE;
ADD PCRF:PCRFID={id},FQDN="{fqdn}",FEATURELIST=UMCH;        (首次)
ADD PCRFGROUP:PCRFGROUPNAME="{pg_name}",SELECTMODE={mode};
ADD PCRFBINDGRP:PCRFGROUPNAME="{pg_name}",PCRFID={id},PRIORITY={n};
SET DFTGLBPCRFGRP:PCRFGROUPNAME="{pg_name}";                 (可选)
SET PCCFUNC:MKPARSEFORMAT={ENABLE|DISABLE};                  (Gx 场景需 UMCH)

!-- 业务级 BWM 规则 + 标准绑定链
ADD RULE:RULENAME="{rule_name}",POLICYTYPE=BWM,PRIORITY={pri},...;  (RULENAME 必须与 UDG/PCRF 一致，CR-BW-05)
ADD USERPROFILE:UPNAME="{up_name}",UPTYPE=PCC;
ADD RULEBINDING:UPNAME="{up_name}",RULENAME="{rule_name}";
ADD USRPROFGROUP:UPGNAME="{upg_name}";
ADD UPBINDUPG:UPGNAME="{upg_name}",UPNAME="{up_name}";
ADD APNUSRPROFG:APNNAME="{apn}",UPGNAME="{upg_name}";
```

> **UNC 侧无 REFRESHSRV**（策略即时生效，见 `../业务感知域规则.md §1.1`）。

### 3.2 UNC 侧 FUP（CS-BW-02，仅 Gx 场景需额外配）

```mml
SET PCCFUNC:MKPARSEFORMAT=ENABLE;
MOD PCRF:PCRFID={id},FEATURELIST=UMCH;
MOD PCCPOLICYGRP:PCCPOLICYGRPNAME="{fup_pg}",FUPSESSIONEXC=ENABLE;
```

> N7(5G) 场景无需此步，阈值由 PCF 侧 umDecs 配置。

---

## 4. 排序规则

> **完整配置链依赖顺序见 `../业务感知域规则.md §1.2`。本节列出带宽场景的具体落点。**

### UDG(UDG)侧（严格顺序）

```
1.  SET LICENSESWITCH                    (License 门控，最先，BR-BW-06)
2.  LOD SIGNATUREDB / LOD PARSERDB       (SA 特征库，SA 前置)
3.  SET BANDWIDTHMNG                     (BWM 全局使能)
4.  CATEGORYPROP / FILTER / L7FILTER     (底层业务识别)
5.  FLOWFILTER → FLTBINDFLOWF → PROTBINDFLOWF  (流过滤器与绑定)
6.  BWMSERVICE → BWMCONTROLLER → BWMUSERGROUP → BWMRULE  (BWM 三级控制链，TR-BW-02)
6a. BCSRVLEVELPLY                         (智能 Shaping 各等级策略，依赖 BWMCONTROLLER)
7.  APNBINDBWMUSRG                        (APN 绑定 BWM 用户组)
8.  URR → URRGROUP → PCCPOLICYGRP        (FUP 三件套，TR-BW-03；或 QoS 上报 URR)
9.  QOSPROP                               (GBR 场景 QoS 属性)
10. ADCPARA                               (ADC 场景应用检测参数)
11. RULE                                  (PCC 规则汇聚)
12. USERPROFILE → RULEBINDING             (用户模板，仅新建时)
13. SET REFRESHSRV                        (刷新生效，必须最后，BR-BW-05/CR-BW-04)
```

### UNC(UNC)侧

```
1. SET LICENSESWITCH                      (License 门控，最先)
2. PCRF → PCRFGROUP → PCRFBINDGRP → SET DFTGLBPCRFGRP  (PCRF 组冗余体系)
3. SET PCCFUNC / SET APNPCCFUNC           (PCC 功能使能)
4. SET PCCFAILACTION / SET PCCTIMER       (故障与定时器)
5. SET POLICYMODE / SET N7RCVATTRCTRL     (接口模式，DP-BW-04)
6. RULE → USERPROFILE → RULEBINDING       (业务级规则)
7. USRPROFGROUP → UPBINDUPG → APNUSRPROFG (标准绑定链，TE-005)
8. 无 REFRESHSRV
```

> **详细 Task 内部命令顺序请加载 `03-task-layer.md` §9 TaskCommandOrderEdge 确认（TE-BWM-1~4 三级控制链、TE-204-1~2 FUP 三件套、TE-501-1~3 PCRF 组、TE-005-1~4 标准绑定链）。**

---

## 5. 配置决策指南

以下场景需要 Agent 从图谱/知识库获取业务规则后做出实现决策：

### CAR vs Shaping 选型（DP-BW-05）

| 控制类型 | 适用业务 | 超额处理 | 层级支持 |
|---------|---------|---------|---------|
| CAR (CTRLTYPE=CAR) | P2P 等低价值业务 | 直接丢弃/重标记 | 用户级/组级/全局级 |
| Shaping (CTRLTYPE=SHAPING) | 视频等抖动敏感业务 | 缓冲到 GTS 队列 | **仅用户级** |
| 智能Shaping (SHAPING+AUTO) | 组级多优先级业务 | 按丢包率公平分配 | 组级 |

> **CR-BW-03 约束**：同一 BWMSERVICE 不能同时绑 CAR 控制器和 Shaping 控制器。详细对比加载 `kb/04-令牌桶与三色标记.md`。

### BWMRULETYPE 三级选择（DP-BW-02）

| BWMRULETYPE | 适用场景 | 是否需 USERGROUPNAME |
|-------------|---------|---------------------|
| SUBSCRIBER_SPECIFIC | 单用户特定业务限速 | 是（指定用户组） |
| GROUP_SPECIFIC | 用户组级限速 | 是 |
| GLOBAL | 整机级业务带宽控制（BWMRULEGLOBAL） | 否 |

### FUP 降速优先级覆盖（BR-BW-02）

降速规则必须满足两条：
1. **PRIORITY 最高**（数值最小）—— 确保覆盖原保障规则
2. **FlowFilter 完全覆盖**原保障规则（端口号范围一致）—— 确保所有相关流量都降速

### 预定义规则三网元一致性（BR-BW-01 / CR-BW-05）

凡动态 PCC 场景（PCRF/PCF 下发预定义规则名）的特性，RULENAME 必须在 PCRF/PCF、UNC、UDG 三处**完全一致**；ADC 场景 FLOWFILTERNAME / appid 也需三网元一致。定向业务必须用预定义规则（PCF 无 L7 识别能力）。

### GBR 场景 QOSTYPE 分支（DP-BW-04 / TR-BW-07）

| 接口 | QOSTYPE | 关键参数 |
|------|---------|---------|
| N7 (5G) | QOS_FLOW_PARA | FQI (QoS Flow Identifier) |
| Gx (2/3/4G) | QOS_BEARER_PARA | QCIVALUE (QCI) |

### ADC 三策略组（TR-BW-05）

ADC 必须配置 Normal / Start / Stop **三个策略组**（EVENT-TRIGGER=APPLICATION_START/STOP），缺失则 ADC 事件上报不完整。

---

## 6. 注意事项

- 每个参数的枚举值必须从 `04-command-graph.md §5` CommandParameter 获取，不可自行推断
- BWM 三级控制链（BWMSERVICE → BWMCONTROLLER → BWMUSERGROUP → BWMRULE）每条业务独立，不可跨业务复用策略链（`../业务感知域规则.md §4`）
- CTRLTYPE 决定 BWMCONTROLLER 参数集（CR-BW-02），CAR 与 SHAPING 参数集互斥
- 排序错误会导致配置失败，REFRESHSRV 必须在最后（仅 UDG 侧）
- 两侧共用参数（RULENAME、PRIORITY、URRID）必须一致（CR-BW-05）
- POLICYTYPE 是带宽场景的关键分支标识（BWM/PCC/QOS/ADC），RULENAME 跨 POLICYTYPE 不能同名（CR-BW-01）
