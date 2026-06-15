# 带宽控制场景三层图谱 · 第5层：跨层映射关系总表

> **文件定位**：`three-layer-graph/05-cross-layer-mapping.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §12 跨层映射
> **作用**：汇总CS↔Feature/Task、Feature↔Task、Task↔Command/Object/DP的所有跨层边
> **合规要求**：严格避免 §13 禁止关系（CS→ConfigObject直接绑定、Feature→MMLCommand直接绑定等）

---

## 0. 跨层映射总览

| 跨层边类型 | 数量 | 方向 | 说明 |
|-----------|------|------|------|
| CS `uses_feature` | 25 | 业务层→特性层 | 7方案 × 平均3.6特性 |
| CS `uses_task`（方案闭包级） | 7 | 业务层→任务层 | 每方案一个主Task集 |
| Feature `decomposes_to` ConfigTask | 24 | 特性层→任务层 | 每核心Feature的Task展开 |
| ConfigTask `invokes` MMLCommand | ~50 | 任务层→命令层 | Task调用的MML命令 |
| ConfigTask `targets` SemanticObject/ConfigObject | ~30 | 任务层→业务/命令层 | Task操作的对象 |
| DP `selects` CS | 4 | 业务层内 | 决策点选择方案 |
| DP `sets_value_pattern` | 3 | 业务层→命令层 | 决策点设置参数模式 |

---

## §1. CS → Feature 映射（uses_feature，25条）

> 来源：`01-business-graph.md` §2.1~§2.7 + §9.2

| CS | uses_feature | Feature角色 |
|----|-------------|------------|
| CS-BW-01 SA-BWM带宽控制 | GWFD-110311（BWM UDG） | 核心：UDG侧三级BWM控制体系 |
| CS-BW-01 | GWFD-110101（SA-Basic） | 基础：SA业务识别前置 |
| CS-BW-01 | GWFD-020351（PCC UDG） | 基础：UDG侧PCC框架 |
| CS-BW-01 | WSFD-109101（PCC UNC） | 基础：UNC侧PCC规则管理 |
| CS-BW-01 | WSFD-211005（BWM UNC） | 核心：UNC侧BWM策略规则（POLICYTYPE=BWM） |
| CS-BW-01 | GWFD-020354（Shaping） | 可选：用户级Shaping整形 |
| CS-BW-01 | GWFD-110313（智能Shaping） | 可选：组级智能Shaping |
| CS-BW-02 FUP配额降速 | GWFD-020353（会话FUP UDG） | 核心：UDG侧会话级流量累计 |
| CS-BW-02 | WSFD-109104（会话FUP UNC） | 核心：UNC侧会话级FUP（Gx/N7） |
| CS-BW-02 | GWFD-110312（业务FUP UDG） | 可选：UDG侧业务级流量累计 |
| CS-BW-02 | WSFD-211009（业务FUP UNC） | 可选：UNC侧业务级FUP |
| CS-BW-03 GBR带宽保证 | GWFD-020358（QoS保证 UDG） | 核心：UDG侧GBR保证+QoS事件上报 |
| CS-BW-03 | WSFD-109107（QoS保证 UNC） | 核心：UNC侧专有承载/QoS Flow建立 |
| CS-BW-04 ADC应用感知 | GWFD-020357（ADC UDG） | 核心：UDG侧L7 DPI应用检测 |
| CS-BW-04 | WSFD-109102（ADC UNC） | 核心：UNC侧ADC三策略组+承载管理 |
| CS-BW-05 小区负荷动态 | GWFD-110332（小区负荷 UDG） | 核心：UDG侧负荷信息转发 |
| CS-BW-05 | WSFD-211101（小区负荷 UNC） | 核心：UNC侧Gx负荷上报 |
| CS-BW-06 位置区域差异化 | WSFD-109108（接入点策略 UNC） | 核心：UNC侧位置变化感知+预定义规则激活 |
| CS-BW-07 无线优化标记 | GWFD-020359（IM管控） | 核心：DSCP标记影响BSC/RNC调度 |
| CS-BW-07 | GWFD-110301（码率差异化） | 核心：终端OS差异化BWM策略 |
| CS-BW-07 | GWFD-110302（视频解耦） | 可选：上下行解耦专载 |
| CS-BW-07 | GWFD-110331（FPI标记） | 核心：FPI/DSCP标记影响基站队列调度 |

> **去重统计**：25条边，覆盖24个Feature中实际参与方案的21个（GWFD-111600 SA特征库管控、GWFD-020305 异常检测作为辅助能力通过FeatureRule和BusinessRule间接表达，不直接挂在方案闭包下）。

---

## §2. CS → ConfigTask 映射（uses_task，7条）

> 每方案一个主Task集，按方案闭包粒度聚合。
> **注**：uses_task列表为**声明式集合**（非执行顺序）。Task的执行先后关系由 `02-feature-graph.md` §6 FeatureTaskOrderEdge 和 `03-task-layer.md` TaskCommandOrderEdge 定义。

| CS | uses_task（主Task集） | 说明 |
|----|---------------------|------|
| CS-BW-01 SA-BWM带宽控制 | T-007, T-008, T-001, T-101, T-102, T-103, T-104, T-105, T-106, T-006, T-003, T-004, T-005, T-501, T-502, T-503 | UDG侧BWM三级控制体系(101~106) + UNC侧PCC规则链(003~005) + PCRF组(501) + 刷新(006) |
| CS-BW-02 FUP配额降速 | T-007, T-201, T-202, T-203, T-204, T-006, T-003, T-004, T-005, T-501, T-502, T-205 | FUP三件套(202~204) + UNC侧Gx功能(205) + 规则绑定(003~005) |
| CS-BW-03 GBR带宽保证 | T-007, T-008, T-001, T-202, T-301, T-003, T-004, T-005, T-501, T-502, T-302, T-303 | SA识别+URR(QOS)+QOSPROP(301)+UNC侧绑定链(005)+QoS Flow管理(302/303) |
| CS-BW-04 ADC应用感知 | T-007, T-008, T-001, T-401, T-402, T-003, T-004, T-005, T-501, T-502 | ADC参数(401)+三策略组(402)+规则绑定(003~005)+PCRF组(501) |
| CS-BW-05 小区负荷动态 | T-007, T-603, T-003, T-004, T-005, T-501, T-502 | 小区负荷上报(603)+PCC规则(003)+UNC绑定链(005) |
| CS-BW-06 位置区域差异化 | T-007, T-003(预定义规则), T-004, T-005, T-501, T-502 | 预定义规则+UNC绑定链（无SA依赖，无UDG侧配置） |
| CS-BW-07 无线优化标记 | T-007, T-008, T-001, T-601, T-602, T-603, T-003, T-006 | DSCP/FPI标记(601)+终端OS(602)+小区负荷(603可选)+刷新(006) |

---

## §3. Feature → ConfigTask 映射（decomposes_to，24条）

| Feature | decomposes_to | Task集 | 说明 |
|---------|---------------|--------|------|
| GWFD-110101 SA-Basic | T-007, T-008, T-001, T-006 | SA基础链：License+特征库+识别条件+刷新生效 |
| GWFD-111600 SA特征库管控 | T-007, T-008 | 特征库版本License+加载 |
| GWFD-020351 PCC(UDG) | T-007, T-001, T-002, T-003, T-004, T-006 | UDG PCC框架：分类+流过滤+规则+模板+刷新 |
| WSFD-109101 PCC(UNC) | T-007, T-501, T-502, T-503, T-504, T-003, T-004, T-005 | UNC PCC框架：PCRF组+功能开关+故障+规则+绑定链 |
| GWFD-110311 BWM(UDG) | T-007, T-008, T-101, T-102, T-103, T-104, T-105, T-106, T-006 | UDG BWM三级控制：规划→服务→控制器→用户组→规则→APN绑定+刷新 |
| WSFD-211005 BWM(UNC) | T-007, T-501, T-003(POLICYTYPE=BWM), T-004, T-005 | UNC BWM：PCRF组+POLICYTYPE=BWM规则+绑定链 |
| GWFD-020354 Shaping(UDG) | T-007, T-001, T-103(CTRLTYPE=SHAPING), T-105, T-006 | 用户级Shaping：复用BWM控制器+RATE/QUEDEPTH参数 |
| GWFD-110313 智能Shaping(UDG) | T-007, T-103, T-107, T-006 | 组级智能Shaping：BWMCONTROLLER(WORKMODE=AUTO)+BCSRVLEVELPLY |
| GWFD-020353 会话FUP(UDG) | T-007, T-201, T-202, T-203, T-204, T-006 | 会话级FUP三件套：URR→URRGROUP→PCCPOLICYGRP |
| WSFD-109104 会话FUP(UNC) | T-007, T-501, T-502, T-202, T-203, T-204, T-205 | UNC会话FUP：PCRF组+功能开关+FUP三件套+Gx FUP功能 |
| GWFD-110312 业务FUP(UDG) | T-007, T-008, T-201, T-202(MONITORINGKEY), T-203, T-204, T-006 | 业务级FUP：依赖SA+URR(PCC_RULE_LEVEL)+三件套 |
| WSFD-211009 业务FUP(UNC) | T-007, T-501, T-202, T-203, T-204 | UNC业务FUP：PCRF组+FUP三件套+Monitoring-Key |
| GWFD-020358 QoS保证(UDG) | T-007, T-008, T-202(USAGERPTMODE=QOS), T-301, T-003, T-006 | QoS事件上报：URR(QOS)+QOSPROP+规则+刷新 |
| WSFD-109107 QoS保证(UNC) | T-007, T-501, T-301, T-302, T-303, T-003, T-004, T-005 | UNC QoS：QOSPROP+空闲定时器+去活策略+绑定链 |
| GWFD-110302 视频解耦 | T-007, T-301(DECOUPLINGSW=ENABLE), T-006 | 视频上下行解耦：复用QOSPROP+DECOUPLINGSW |
| GWFD-020357 ADC(UDG) | T-007, T-008, T-401, T-006 | UDG ADC：ADC参数配置+刷新 |
| WSFD-109102 ADC(UNC) | T-007, T-401, T-402, T-003, T-004, T-005 | UNC ADC：ADC参数+三策略组+规则+绑定链 |
| GWFD-020305 异常检测 | T-007, T-003 | 异常检测：License+规则（辅助能力） |
| GWFD-020359 IM管控 | T-007, T-008, T-601, T-006 | IM管控：DSCP标记+刷新 |
| GWFD-110301 码率差异化 | T-007, T-602 | 终端OS差异化：SET APNOSLELBWMSW |
| GWFD-110331 FPI标记 | T-007, T-008, T-601, T-006 | FPI标记：业务流标识+无线调度优化 |
| GWFD-110332 小区负荷(UDG) | T-007, T-603 | UDG小区负荷：GTP-U扩展头接收+转发 |
| WSFD-211101 小区负荷(UNC) | T-007, T-603(UNC侧), T-501 | UNC小区负荷：SET APNREPORTATTR+PCRF组 |
| WSFD-109108 接入点策略 | T-007, T-501, T-003(预定义规则), T-004, T-005 | UNC位置策略：预定义规则+绑定链 |

---

## §4. ConfigTask → MMLCommand 映射（invokes，~50条核心映射）

| ConfigTask | invokes | MMLCommand | 说明 |
|-----------|---------|-----------|------|
| **通用Task** | | | |
| T-001 | invokes | ADD CATEGORYPROP, ADD FILTER, ADD L7FILTER | 业务分类与过滤条件定义 |
| T-002 | invokes | ADD FLOWFILTER, ADD FLTBINDFLOWF | 流过滤器组装 |
| T-003 | invokes | ADD RULE | PCC规则（POLICYTYPE由DP-BW-01决定） |
| T-004 | invokes | ADD USERPROFILE, ADD RULEBINDING | 用户模板+规则绑定 |
| T-005 | invokes | ADD USRPROFGROUP, ADD UPBINDUPG, ADD APNUSRPROFG | UNC标准绑定链 |
| T-006 | invokes | SET REFRESHSRV | 策略刷新生效（must_be_last） |
| T-007 | invokes | SET LICENSESWITCH | License前置门控 |
| T-008 | invokes | LOD SIGNATUREDB, LOD PARSERDB | SA特征库加载 |
| **BWM专属** | | | |
| T-101 | invokes | （规划task，无命令） | BWM策略规划 |
| T-102 | invokes | ADD BWMSERVICE | BWM服务实例 |
| T-103 | invokes | ADD BWMCONTROLLER | BWM控制器（CAR/Shaping参数集） |
| T-104 | invokes | ADD BWMUSERGROUP | BWM用户组 |
| T-105 | invokes | ADD BWMRULE, ADD BWMRULEGLOBAL | BWM规则（用户级/组级/全局级） |
| T-106 | invokes | ADD APNBINDBWMUSRG | BWM APN绑定 |
| T-107 | invokes | ADD BCSRVLEVELPLY | 智能Shaping服务等级策略 |
| **FUP专属** | | | |
| T-201 | invokes | （规划task，无命令） | FUP配额策略规划 |
| T-202 | invokes | ADD URR | URR规则（USAGERPTMODE由场景决定） |
| T-203 | invokes | ADD URRGROUP | URR组 |
| T-204 | invokes | ADD PCCPOLICYGRP | PCC策略组（FUP三件套完成） |
| T-205 | invokes | SET PCCFUNC, MOD PCRF, MOD PCCPOLICYGRP | UNC侧Gx FUP功能 |
| **QoS专属** | | | |
| T-301 | invokes | ADD QOSPROP | QoS属性（5QI/QCI/GBR/MBR/ARP） |
| T-302 | invokes | SET APNIDLETIME | 专有QoS Flow空闲定时器 |
| T-303 | invokes | ADD APNDEACTQFPLCY | 去活QoS Flow策略 |
| **ADC专属** | | | |
| T-401 | invokes | ADD ADCPARA | ADC应用检测参数 |
| T-402 | invokes | ADD RULE (×3) | ADC三策略组（Normal/Start/Stop） |
| **UNC控制面** | | | |
| T-501 | invokes | ADD PCRF, ADD PCRFGROUP, ADD PCRFBINDGRP, SET DFTGLBPCRFGRP | PCRF冗余体系 |
| T-502 | invokes | SET PCCFUNC, SET APNPCCFUNC | PCC功能开关 |
| T-503 | invokes | SET PCCFAILACTION, SET PCCTIMER | PCC故障与定时器 |
| T-504 | invokes | SET N7RCVATTRCTRL, SET N7SNDATTRCTRL | N7属性控制（仅5G） |
| **无线优化** | | | |
| T-601 | invokes | ADD RULE（DSCP/FPI标记规则） | DSCP/FPI标记 |
| T-602 | invokes | SET APNOSLELBWMSW | 终端OS BWM差异化开关 |
| T-603 | invokes | SET APNREPORTATTR | APN拥塞上报属性 |

---

## §5. ConfigTask → SemanticObject/ConfigObject 映射（targets）

| ConfigTask | targets SemanticObject | targets ConfigObject |
|-----------|------------------------|---------------------|
| T-001 | SO-BW-02（业务识别条件） | CATEGORYPROP, FILTER, L7FILTER |
| T-002 | SO-BW-02（业务识别条件） | FLOWFILTER, FLTBINDFLOWF |
| T-003 | SO-BW-01（带宽控制策略）, SO-BW-04（限速等级） | RULE |
| T-004 | — | USERPROFILE, RULEBINDING |
| T-005 | — | USRPROFGROUP, UPBINDUPG, APNUSRPROFG |
| T-006 | — | — (策略刷新，元操作) |
| T-007 | — | — (License全局) |
| T-008 | SO-BW-02（业务识别条件） | — (SA特征库数据) |
| T-101 | SO-BW-01（带宽控制策略） | — (规划输出) |
| T-102 | SO-BW-02（业务识别条件） | BWMSERVICE |
| T-103 | SO-BW-01（带宽控制策略）, SO-BW-04（限速等级） | BWMCONTROLLER |
| T-104 | — | BWMUSERGROUP |
| T-105 | SO-BW-04（限速等级） | BWMRULE, BWMRULEGLOBAL |
| T-106 | — | APNBINDBWMUSRG |
| T-107 | SO-BW-04（限速等级） | BCSRVLEVELPLY |
| T-201 | SO-BW-03（流量配额） | — (规划输出) |
| T-202 | SO-BW-03（流量配额） | URR |
| T-203 | SO-BW-03（流量配额） | URRGROUP |
| T-204 | SO-BW-03（流量配额） | PCCPOLICYGRP |
| T-205 | SO-BW-03（流量配额） | PCCPOLICYGRP（MOD FUPSESSIONEXC） |
| T-301 | SO-BW-05（QoS参数集） | QOSPROP |
| T-302 | SO-BW-05（QoS参数集） | — (APN级定时器) |
| T-303 | SO-BW-05（QoS参数集） | APNDEACTQFPLCY |
| T-401 | SO-BW-06（应用检测事件） | ADCPARA |
| T-402 | SO-BW-06（应用检测事件） | RULE（三策略组） |
| T-501 | — | PCRF, PCRFGROUP, PCRFBINDGRP |
| T-502 | — | — (PCC功能开关) |
| T-503 | — | — (PCC故障/定时器) |
| T-504 | SO-BW-05（QoS参数集） | — (N7属性映射) |
| T-601 | SO-BW-02（业务识别条件） | RULE（DSCP/FPI标记规则） |
| T-602 | — | — (APN级BWM OS开关) |
| T-603 | SO-BW-07（小区负荷等级） | — (APNREPORTATTR) |

---

## §6. DecisionPoint 跨层影响（selects / sets_value_pattern）

| DP | 关系 | 目标 | 说明 |
|----|------|------|------|
| DP-BW-01 带宽控制机制选择 | `selects` | CS-BW-01/CS-BW-02/CS-BW-03/CS-BW-05 | CAR限速→CS-BW-01；FUP降速→CS-BW-02；GBR保证→CS-BW-03；拥塞控制→CS-BW-05 |
| DP-BW-02 控制粒度选择 | `sets_value_pattern` | BWMRULE.BWMRULETYPE | 会话级→SUBSCRIBER_SPECIFIC；业务级→SUBSCRIBER_SPECIFIC+BWMSERVICE；用户组级→GROUP_SPECIFIC；全局级→GLOBAL |
| DP-BW-04 接口代际选择 | `selects` | T-504(是否需要N7属性) | 4G(Gx)→无需T-504；5G(N7)→需T-504+T-205可能不需要 |
| DP-BW-05 BWM控制类型选择 | `sets_value_pattern` | BWMCONTROLLER.CTRLTYPE | CAR→CIR/PIR/CBS/PBS参数集；SHAPING→RATE/QUEDEPTH参数集 |
| DP-BW-06 FUP累计粒度选择 | `sets_value_pattern` | URR.USAGERPTMODE + Monitoring-Level | 会话级FUP→ONLINE/SESSION_LEVEL(0)；业务级FUP→MONITORINGKEY/PCC_RULE_LEVEL(1) |
| DP-BW-07 应用识别需求 | `selects` | T-003(RULE类型) | L7识别→预定义规则；L3/L4→可用动态规则 |
| DP-BW-08 产品面配置分工 | `sets_value_pattern` | 配置入口路径 | UDG执行面→BWM命令体系；UNC控制面→ADD RULE体系；双产品→两端配置 |

---

## §7. 端到端链路验证（3条完整路径）

### 7.1 路径A：SA-BWM带宽控制端到端

```
[业务] BD-BW-01 业务感知
  → NS-BW-01 带宽控制场景
    → CS-BW-01 SA-BWM带宽控制方案
      → DP-BW-01 选择CAR限速
      → DP-BW-02 选择用户级控制（SUBSCRIBER_SPECIFIC）
      → DP-BW-05 选择CAR-CIR保障（CIR/PIR/CBS/PBS）
      → BR-BW-01 预定义规则三网元一致性
      → BR-BW-03 BWM与PCC独立匹配
      → BR-BW-05 REFRESHSRV必须最后执行
      → SO-BW-01 带宽控制策略（CIR/PIR参数集）
      → SO-BW-02 业务识别条件（SVC/APP）
      → SO-BW-04 限速等级（GREEN/YELLOW/RED）

[特性] CS-BW-01 uses_feature
  → GWFD-110311 BWM（UDG三级控制体系）
  → GWFD-110101 SA-Basic（业务识别基础）
  → GWFD-020351 PCC(UDG)（策略框架）
  → WSFD-211005 BWM(UNC)（POLICYTYPE=BWM规则）
  → WSFD-109101 PCC(UNC)（UNC侧PCC框架）

[任务] GWFD-110311 decomposes_to（FTOE-BW-001~008）
  → T-007 License开启（LKV3G5TCSA01）
  → T-008 SA特征库加载
  → T-101 规划BWM控制策略
  → T-102 ADD BWMSERVICE ★ BWM服务实例
  → T-103 ADD BWMCONTROLLER（CTRLTYPE=CAR, CIR/PIR/CBS/PBS）★ 核心参数集
  → T-104 ADD BWMUSERGROUP
  → T-105 ADD BWMRULE（BWMRULETYPE=SUBSCRIBER_SPECIFIC）★ 规则绑定
  → T-106 ADD APNBINDBWMUSRG（APN绑定）
  → T-006 SET REFRESHSRV（must_be_last）

[命令] T-103 invokes → ADD BWMCONTROLLER
  → operates_on → ConfigObject: BWMCONTROLLER
    → 关键参数: BWMCNAME, CTRLTYPE=CAR, CIR, PIR, CBS, PBS, GREENACT, YELLOWACT, REDACT
  → constrained_by → CR-BW-02 CTRLTYPE决定参数集
  → constrained_by → CR-BW-03 CAR与Shaping不可同对象叠加
  → impacted_by → DP-BW-05 sets_value_pattern(CTRLTYPE=CAR)

[UNC侧] WSFD-211005 decomposes_to（FTOE-BW-014~017）
  → T-501 配置PCRF组
  → T-003 ADD RULE（POLICYTYPE=BWM）
  → T-004 ADD USERPROFILE + RULEBINDING
  → T-005 ADD USRPROFGROUP + UPBINDUPG + APNUSRPROFG

[证据] 全链路可追溯：
  CS-BW-01 → [EV-FK-04, EV-FK-01, EV-FK-03, EV-CA-01]
  GWFD-110311 → [EV-FK-04, EV-CA-01]
  ADD BWMCONTROLLER → [EV-FK-04, EV-CA-01]
```

### 7.2 路径B：FUP配额降速端到端

```
[业务] CS-BW-02 FUP配额降速方案
  → DP-BW-06 选择FUP累计粒度（会话级SESSION_LEVEL）
  → BR-BW-02 超额降速优先级覆盖 ★ 核心
  → BR-BW-01 预定义规则三网元一致性
  → SO-BW-03 流量配额（VolumeThreshold）
  → SO-BW-04 限速等级（高速→降速切换）

[特性] CS-BW-02 uses_feature
  → GWFD-020353 会话FUP（UDG侧流量累计）
  → WSFD-109104 会话FUP（UNC侧Gx/N7管理）

[任务] GWFD-020353 decomposes_to（FTOE-BW-009~013）
  → T-007 License开启（LKV3G5PCBT01）
  → T-201 规划FUP配额策略
  → T-202 ADD URR（USAGERPTMODE=ONLINE, VOLUMETHRESHOLD）★ 核心阈值
  → T-203 ADD URRGROUP（UPURRNAME1引用URR）
  → T-204 ADD PCCPOLICYGRP（URRGROUP→策略组）★ FUP三件套完成
  → T-006 SET REFRESHSRV

[命令] T-202 invokes → ADD URR
  → operates_on → ConfigObject: URR
    → 关键参数: URRID, USAGERPTMODE=ONLINE, MEASUREMENTMETHOD=VOLUME, VOLUMETHRESHOLD
  → constrained_by → TR-BW-04 URR模式校验（会话FUP=ONLINE，不可与QOS混用）
  → constrained_by → TR-BW-03 FUP三件套链（URR→URRGROUP→PCCPOLICYGRP）
  → impacted_by → DP-BW-06 sets_value_pattern(SESSION_LEVEL)

[UNC侧] WSFD-109104 decomposes_to
  → T-501 配置PCRF组
  → T-202/T-203/T-204 UNC侧FUP三件套
  → T-205 SET PCCFUNC + MOD PCRF(UMCH)（仅Gx场景）

[证据] CS-BW-02 → [EV-FK-07, EV-FK-18, EV-CA-01, EV-CA-02]
  ADD URR → [EV-FK-07, EV-CA-01]
```

### 7.3 路径C：ADC应用感知端到端

```
[业务] CS-BW-04 ADC应用感知动态带宽方案
  → DP-BW-07 需L7识别→预定义规则
  → BR-BW-01 预定义规则三网元一致性（ADCPARA+RULENAME+FLOWFILTERNAME全网一致）
  → BR-BW-04 RULENAME跨策略类型不冲突
  → SO-BW-06 应用检测事件（APP_STA/APP_STO）
  → SO-BW-05 QoS参数集（三策略组QoS差异）

[特性] CS-BW-04 uses_feature
  → GWFD-020357 ADC（UDG侧L7 DPI检测）
  → WSFD-109102 ADC（UNC侧三策略组+承载管理）

[任务] GWFD-020357 decomposes_to
  → T-007 License开启（LKV3G5ADCF01）
  → T-008 SA特征库加载
  → T-401 ADD ADCPARA ★ ADC检测参数
  → T-006 SET REFRESHSRV

[任务] WSFD-109102 decomposes_to
  → T-501 配置PCRF组
  → T-401 ADD ADCPARA（UNC侧，三网元一致）
  → T-402 ADD RULE ×3（Normal/Start/Stop三策略组）★ 核心ADC策略
  → T-003/T-004/T-005 规则+模板+绑定链

[命令] T-401 invokes → ADD ADCPARA
  → operates_on → ConfigObject: ADCPARA
    → 关键参数: ADCPARANAME, APPNAME, MATCHMODE
  → constrained_by → CR-BW-05 预定义规则名全网唯一（ADCPARA+RULENAME三网元一致）

[命令] T-402 invokes → ADD RULE ×3
  → constrained_by → TR-BW-06 预定义规则全网一致性
  → constrained_by → TR-BW-05 ADC三策略组完整性

[证据] CS-BW-04 → [EV-FK-09, EV-FK-21, EV-CA-02]
  ADD ADCPARA → [EV-FK-09, EV-CA-01]
```

---

## §8. 跨层 refined_by 关系（6条）

> **Schema参考**：Schema §12.1~§12.4 定义了 `refined_by` 跨层精化关系：上层规则被下层规则具体化。
> **含义**：BusinessRule 的高层约束在 FeatureRule 和 TaskRule 中被精化为可执行的配置规则，TaskRule 进一步在 CommandRule 中体现为具体命令约束。

| 序号 | 上层规则 | 关系 | 下层规则 | 精化语义 |
|------|---------|------|---------|---------|
| 1 | `BR-BW-01`（预定义规则三网元一致性） | `refined_by` | `TR-BW-06`（预定义规则全网一致性前置） | BR"三网元参数一致"→TR"T-003配置PCC规则时RULENAME在PCF/SMF/UPF三侧必须同名同参" |
| 2 | `BR-BW-01`（预定义规则三网元一致性） | `refined_by` | `CR-BW-05`（预定义规则名全网唯一） | BR"三网元一致"→CR"ADD RULE.RULENAME必须在PCRF/PCF+UNC+UDG三处保持一致" |
| 3 | `BR-BW-04`（RULENAME跨策略类型不冲突） | `refined_by` | `CR-BW-01`（RULENAME跨POLICYTYPE不冲突） | BR"不冲突"→CR"PCC类型RULENAME≠QOS类型RULENAME" |
| 4 | `BR-BW-05`（REFRESHSRV必须最后执行） | `refined_by` | `TR-BW-01`（REFRESHSRV时序约束） | BR"最后执行"→TR"T-006必须在所有配置后执行，约60秒生效" |
| 5 | `BR-BW-05`（REFRESHSRV必须最后执行） | `refined_by` | `CR-BW-04`（REFRESHSRV后60秒生效） | BR"最后执行"→CR"PROTBINDFLOWF定时器约60秒后才完全下发" |
| 6 | `BR-BW-06`（License前置门控） | `refined_by` | `FR-BW-02`（智能Shaping依赖链） | BR"License使能"→FR"智能Shaping需BWM+Shaping双License同时开启" |

> **覆盖范围**：以上6条覆盖了 BR→TR（3条）、BR→CR（3条）、BR→FR（1条）三层refined_by关系。其余BR（如BR-BW-02超额降速优先级覆盖、BR-BW-03 BWM与PCC独立匹配）暂无直接下层规则精化，作为独立高层约束存在。

---

## §9. 禁止关系检查（§13 合规）

| 禁止关系 | 是否存在 | 说明 |
|---------|---------|------|
| CS → ConfigObject 直接绑定 | 无 | CS通过uses_feature→Feature→decomposes_to→Task→invokes→Command→operates_on间接到达ConfigObject |
| Feature → MMLCommand 直接绑定 | 无 | Feature通过decomposes_to→ConfigTask→invokes→MMLCommand间接到达 |
| CS → CommandParameter 直接绑定 | 无 | CS通过DP.sets_value_pattern间接设置参数 |
| Feature → ConfigObject 直接绑定 | 无 | Feature通过Task间接操作ConfigObject |
| BusinessRule → CommandRule 直接绑定 | 无 | BR和CR独立定义，通过共同约束的对象关联 |
| SemanticObject → ConfigObject 直接绑定（非realized_by） | 无 | SO通过realized_by关系表达，非直接操作 |

> **合规结论**：本图谱严格遵循Schema §13禁止关系约束，所有跨层连接通过标准关系边（uses_feature/decomposes_to/invokes/operates_on）完成。

---

## §10. 跨层边统计

| 跨层边 | 数量 |
|-------|------|
| CS `uses_feature` | 25 |
| CS `uses_task`（闭包级） | 7 |
| Feature `decomposes_to` ConfigTask | 24 |
| ConfigTask `invokes` MMLCommand | ~50（32 Task × 平均1.5命令，含10个无命令规划task） |
| ConfigTask `targets` SO/ConfigObject | ~30 |
| DP `selects` CS | 4 |
| DP `sets_value_pattern` | 3 |
| BR/TR `refined_by` FR/TR/CR | 6 |
| **跨层边总计** | **~149** |

---

## §11. 与计费场景跨层映射的对比

| 维度 | 计费场景 | 带宽控制场景 |
|------|---------|------------|
| CS uses_feature 边数 | 20 | 25 |
| CS uses_task 边数 | 7 | 7 |
| Feature decomposes_to 边数 | 14 | 24 |
| ConfigTask invokes 边数 | ~50 | ~50 |
| ConfigTask targets 边数 | ~28 | ~30 |
| DP selects 边数 | 3 | 4 |
| DP sets_value_pattern 边数 | 3 | 3 |
| refined_by 边数 | 5 | 6 |
| 跨层边总计 | ~130 | ~149 |
| 核心路径数 | 6 | 3 |
| 共享机制 | URR三件套（计费→差异化费率） | URR三件套（FUP→流量阈值监控） |
| 独有跨层链 | 在线DCC链(T-201~T-204), 融合18步链(T-301~T-310) | BWM三级控制(101~106), ADC三策略组(401~402), QoS专载(301~303) |
| POLICYTYPE | 固定CHARGING | 动态BWM/PCC/QOS/ADC（由DP-BW-01决策） |
| 端到端差异 | 路径覆盖离线/在线/融合/内容计费/配额降速/兜底 | 路径覆盖BWM限速/FUP降速/ADC应用感知 |

> 两场景共享部分通用Task链（T-001~T-007、T-003 PCC规则、T-005 绑定链），但POLICYTYPE分支不同。URR跨场景复用但参数语义完全不同：计费场景用RG/USAGERPTMODE区分费率，带宽控制场景用USAGERPTMODE区分FUP/QoS/MONITORING用途。

---

## §12. 跨层一致性检查清单

- [x] 所有CS的uses_feature指向真实存在的Feature（24个）
- [x] 所有Feature的decomposes_to指向真实存在的ConfigTask（32个）
- [x] 所有ConfigTask的invokes指向真实存在的MMLCommand（55个）
- [x] 所有MMLCommand的operates_on指向真实存在的ConfigObject（29个）
- [x] 所有ConfigTask的targets指向真实存在的SemanticObject（8个）或ConfigObject
- [x] 所有DP的selects指向真实存在的CS（7个）
- [x] 路径A~C端到端完整：BD→NS→CS→Feature→Task→Command→Object
- [x] 无 §13 禁止关系

---

> 本文件为带宽控制场景三层图谱第5层。第6层证据索引见同目录其他文件。
