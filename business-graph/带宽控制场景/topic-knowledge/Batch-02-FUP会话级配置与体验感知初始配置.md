# Batch-02: FUP会话级配置 + 体验感知初始配置

> **来源**: UDG 业务专题 - 5G Core FUP解决方案(会话级) + 5G Core 体验感知解决方案(初始配置)
> **覆盖**: 会话级FUP配置/调测/变更、体验感知(普通/重点/保障)场景配置
> **文件数**: 15 md
> **带宽控制聚焦**: FUP配置步骤 + QoE体验感知如何驱动带宽策略

---

## 1. 文档概述

本批次覆盖两大主题：

### 1.1 FUP会话级累计流量策略控制（5个文档）

| 文档 | 核心内容 |
|------|----------|
| 系统影响与约束_70687833.md | 会话级FUP的系统性能影响和约束条件 |
| 调测会话级累计流量策略控制_24087906.md | FUP功能验证的完整调测流程（12步） |
| 配置会话级累计流量策略控制_23928082.md | FUP配置命令、License和可选参数 |
| 20.7.0 01_24087900.md | 版本变更记录（2021-08-30首次发布） |
| 特性映射_23928078.md | FUP会话级和业务级特性的License与产品映射 |

### 1.2 体验感知解决方案初始配置（10个文档）

| 文档 | 核心内容 |
|------|----------|
| 保障用户体验感知场景_94432534.md | 保障用户场景的网元配置总览 |
| 调测保障用户体验感知功能_90690618.md | 保障用户体验感知调测验证流程 |
| 普通用户体验感知场景_36232121.md | 普通用户场景概述（仅UDG+UDN） |
| UDG侧配置（普通用户）_15642930.md | 普通用户UDG侧体验感知完整配置步骤 |
| 调测普通用户体验信息感知功能_21534654.md | 普通用户调测验证流程 |
| UDC侧配置（重点用户）_05937066.md | 重点用户UDC侧UDP地址配置 |
| UDG侧配置（重点用户）_15435520.md | 重点用户UDG侧体验感知配置 |
| UNC侧配置（典型场景）_18425829.md | 重点用户UNC侧SMF选择智能UPF配置 |
| 配置SMF选择智能PCF_31501709.md | 异厂商PCF场景SMF选择智能PCF配置 |
| 配置SMF选择智能UPF_95822676.md | 异厂商PCF场景SMF选择智能UPF配置 |

---

## 2. 核心知识点

### 2.1 会话级FUP配置与调测

#### 2.1.1 FUP会话级配置的目标

会话级累计流量策略控制（Session-level Usage Monitoring）的目标是保证用户公平使用流量。当用户累计使用流量达到PCRF/PCF设定的阈值后，系统按策略执行带宽降速或下发新的计费规则，从而实现流量公平管控。

#### 2.1.2 系统影响与约束

**系统性能影响**:
- 启用会话级FUP需要PGW-U/UPF、GGSN-C/PGW-C/SMF与PCRF/PCF持续交互，并动态处理PCRF/PCF下发的策略
- 对系统性能影响较大，规划时需考虑启用该特性的用户比例
- 详细性能影响需基于流量模型评估

**约束条件**:
- UMCH（Usage Monitoring Congestion Handling）仅支持总流量阈值，不支持分业务阈值
- 对于UE Category用户，要求PCRF/PCF下发的会话级流量阈值不低于1GB，否则影响流量累计的准确性

#### 2.1.3 必选配置命令

会话级FUP的最小配置只需要在UNC和UDG两侧打开License开关：

**UNC侧（控制面）**:
```
SET LICENSESWITCH:LICITEM="LKV3W9PCBT12",SWITCH=ENABLE;
```

**UDG侧（用户面）**:
```
SET LICENSESWITCH:LICITEM="LKV3G5PCBT01",SWITCH=ENABLE;
```

- UNC License项：`LKV3W9PCBT12`（特性ID: WSFD-109104）
- UDG License项：`LKV3G5PCBT01`（特性ID: GWFD-020353）
- 配额和动态规则在PCF上配置，UNC和UDG仅需开启功能

#### 2.1.4 可选配置命令

**Monitoring-Key解析方式设置（Gx接口）**:
```
SET PCCFUNC: MKPARSEFORMAT=UNSIGNED32, N7FEATURELIST=UMC;
```
- `MKPARSEFORMAT`：对PCRF下发的Monitoring-Key值的解析方式，需与PCRF一致，PCF不适用
- `N7FEATURELIST`：N7接口特性列表，支持使用情况监视控制（UMC），最终以PCF下发能力为准

**UMCH功能使能（配额重置拥塞处理）**:
```
MOD PCRF: HOSTNAME="pcrf_01", SUPFEANEGOSW=ENABLE, FEATURELIST=UMCH;
```
- 用途：配额重置时避免Gx接口Usage Monitoring信令拥塞
- 前提：PCRF需支持UMCH功能

**会话级FUP排除配置（特定业务流量不统计）**:
```
MOD PCCPOLICYGRP: PCCPOLICYGRPNM="pccpolicygrp_01", FUPSESSIONEXC=ENABLE;
```
- 用途：将某类业务/应用的流量不统计到用户级累计流量中
- 典型场景：特定免流业务的流量排除

**重定向流量FUP排除**:
```
SET SRVCOMMONPARA: REDIRECTFUP=ENABLE;
```
- 用途：缺省情况下重定向流量要求免费，不统计到累计流量中

#### 2.1.5 FUP调测完整流程（12步）

调测目标：验证用户达到流量阈值后，系统正确执行带宽降速或下发新计费规则。

| 步骤 | 操作 | 预期结果 |
|------|------|----------|
| 1 | UNC执行 `LST LICENSESWITCH`，检查License开关 | SWITCH为ENABLE |
| 2 | UDG执行 `LST LICENSESWITCH`，检查License开关 | SWITCH为ENABLE |
| 3 | UNC创建用户跟踪任务，消息类型选N4、Gx和N7 | 跟踪任务创建成功 |
| 4 | 测试终端使用目标APN接入网络 | 用户正常上线 |
| 5 | 查看CCA-I/Npcf_SMPolicyControl_Create Response | UsageMonitoringData与规划值一致 |
| 6 | 用户访问业务（在线视频或FTP下载） | 流量持续产生 |
| 7 | 达到流量阈值后查看PFCP Session Report Request | 消息携带用户使用流量 |
| 8 | 查看CCR-U/accuUsageReports | 上报流量与阈值接近相等 |
| 9 | 异常排查：执行 `LST APNPCCFUNC` | 确认指定DNN下PCC功能已开启 |
| 10 | 抓包工具统计实际流量 | 验证是否达到PCRF/PCF配额 |
| 11 | 查看CCA-U/Npcf_SMPolicyControl_Update Response | MBR/AMBR降为设定QoS带宽或下发新计费规则 |
| 12 | 联系华为技术支持（如以上步骤均无法解决） | 收集抓包和EXP MML数据 |

**调测关键验证点**:
- 步骤5：验证PCRF/PCF是否正确下发Session级流量监控信息
- 步骤7-8：验证UDG是否正确上报流量到UNC/SMF
- 步骤11：验证达到阈值后是否正确执行带宽控制策略（MBR降速或新规则下发）

### 2.2 FUP特性映射与版本变更

#### 2.2.1 FUP特性完整映射

FUP解决方案包含会话级和业务级两个层次，每个层次在UNC和UDG上各有独立的特性ID和License项：

| 功能名称 | 特性ID | 特性名称 | License项 | 产品 |
|----------|--------|----------|-----------|------|
| 会话级累计流量策略控制 | WSFD-109104 | 基于累计流量的策略控制 | 82207980 LKV3W9PCBT12 | UNC |
| 会话级累计流量策略控制 | GWFD-020353 | 基于累计流量的策略控制 | 82200AFM LKV3G5PCBT01 | UDG |
| 业务级累计流量策略控制 | WSFD-211009 | 基于业务累计流量的策略控制 | 82200BNU LKV2FUPSAT01 | UNC |
| 业务级累计流量策略控制 | GWFD-110312 | 基于业务累计流量的策略控制 | 82209776 LKV3G5FPBS01 | UDG |

**会话级 vs 业务级区别**:
- 会话级：监控整个会话（PDN连接）的累计流量，达到阈值后统一执行策略
- 业务级：按业务/应用分类监控累计流量，不同业务可有不同阈值和策略

#### 2.2.2 版本变更

会话级累计流量策略控制首次正式发布于20.7.0 01版本（2021-08-30）。

### 2.3 体验感知解决方案概述（普通/重点/保障用户场景）

#### 2.3.1 三种体验感知场景

体验感知解决方案根据用户类型和保障级别分为三种场景：

| 场景 | 涉及网元 | 核心功能 | 带宽控制关联 |
|------|----------|----------|------------|
| 普通用户体验感知 | UDG + UDN | 周期性采集用户体验KPI（带宽、时延、丢包），上报到BOSS/SFTP | 采集带宽KPI用于全局体验监控 |
| 重点用户体验感知 | UDC + UNC + UDG + UDN | 针对签约用户精准采集体验数据，支持智能UPF选择 | 为VIP用户提供智能带宽保障 |
| 保障用户体验感知 | 依赖重点业务保障配置 | 在重点保障基础上增加北向上报体验单据 | 保障VIP用户的带宽体验 |

#### 2.3.2 普通用户体验感知场景

**适用范围**: 仅涉及UDG和UDN两个网元，UDN侧需新增北向上报体验单据配置（资料受限）。

**UDG侧配置步骤（8步）**:

**步骤1**: 进入MML命令行-UDG窗口

**步骤2**: 加载协议特征库（低于01.0002.1661.01需加载）
```
SET SOFTPARA: DT=BYTE, BYTENUM=687, BYTEVALUE=1;
LOD SIGNATUREDB: LOADMODE=LATEST;
SET SOFTPARA: DT=BYTE, BYTENUM=687, BYTEVALUE=0;
```

**步骤3**: 开启必选License开关（7个License项）
```
// 普通用户体验感知
SET LICENSESWITCH:LICITEM="LKV3G5EXPR01",SWITCH=ENABLE;
// 智能板订阅和采集
SET LICENSESWITCH:LICITEM="LKV3G5IBIC01",SWITCH=ENABLE;
// TCP/UDP传输分析上报
SET LICENSESWITCH:LICITEM="LKV3G5TDIR01",SWITCH=ENABLE;
// 报表功能相关License
SET LICENSESWITCH:LICITEM="LKV3G5IARG01",SWITCH=ENABLE;
SET LICENSESWITCH:LICITEM="LKV3G5FSFR01",SWITCH=ENABLE;
SET LICENSESWITCH:LICITEM="LKV3G5SARS01",SWITCH=ENABLE;
SET LICENSESWITCH:LICITEM="LKV3G5RSLR01",SWITCH=ENABLE;
```

**步骤4**: 设置体验业务基本功能
```
SET EXPBASICFUNC: SWITCH=ENABLE, ANARPTPERIOD=300, SRVPORT=15000;
```
- `ANARPTPERIOD=300`：体验业务上报周期300秒（5分钟）
- `SRVPORT=15000`：体验业务上报服务器端口号

**步骤5**: 配置应用绑定关系
```
ADD SSUPROTCOLGROUP: DEFPRTGRPNAME="live_video", PROTOCOLNAME="taobao_live";
ADD APPPOLICYCTRL: APPIDNAME="appgroup1", SUBAPPIDNAME="app1", DEFPRTGRPNAME="live_video";
```
- `SSUPROTCOLGROUP`：定义协议组（自定义协议组名称+协议名称）
- `APPPOLICYCTRL`：将应用/子应用绑定到检测协议组

**步骤6**: 开启抽样率为100%
```
SET RPTGLBPARA: FLOWSAMPLERATE=1000;
```
- `FLOWSAMPLERATE=1000`：千分之1000即100%抽样

**步骤7**: 开启TCP/UDP分析
```
SET RPTGLBCFG: TCPINSIGHTSW=ENABLE, UDPINSIGHTSW=ENABLE;
```

**步骤8**: 配置报表服务器
```
ADD RPTSVR: RPTSVRNAME="UFDR_SERVER", RPTSVRTYPE=EXP;
```

**普通用户调测验证流程（7步）**:

| 步骤 | 操作 | 预期结果 |
|------|------|----------|
| 1 | 用户正常访问测试应用5分钟 | 业务正常使用 |
| 2 | UDN侧HTTP接口跟踪查看TCP链路保活消息 | 每分钟周期发送TCP保活消息 |
| 3 | 查看Nupf_EventExposureService_CreateSubscription Request | 消息存在 |
| 4 | 查看Nupf_EventExposureService_CreateSubscription Response | 响应为201 Created |
| 5 | UDG用户跟踪观察EMS-UFDR消息 | 消息中存在QosExpRptData信元 |
| 6 | UDN的Ufdr跟踪查看Ufdr_Collector_Request | 消息中存在QosExpRptData信元 |
| 7 | 联系BOSS/SFTP侧确认体验数据 | 数据正常接收，内容符合预期 |

#### 2.3.3 重点用户体验感知场景

重点用户场景涉及4个网元：UDC、UNC、UDG、UDN。

**UDG侧配置**（与普通用户UDG配置步骤一致）:
- 协议特征库加载、License开关（7项）、体验业务基本功能、应用绑定、抽样率、TCP/UDP分析
- 配置步骤和命令与普通用户UDG侧完全相同
- 区别：重点用户场景依赖UNC侧智能UPF选择和UDC侧UDP地址配置

**UDC侧配置**（配置UDN接收体验数据的IP地址）:
```
// IPv4场景
ADD UDPADDR: NFINSTANCEID="6d25a684-9558-11e9-aa94-efccd7a0659a", IPADDRESSTYPE=IPTypeV4, IPV4ADDRESS="10.10.25.10", INDEX=0;
ADD UDPADDR: NFINSTANCEID="6d25a684-9558-11e9-aa94-efccd7a0659b", IPADDRESSTYPE=IPTypeV4, IPV4ADDRESS="10.10.25.12", INDEX=2;
```
- `NFINSTANCEID`：NF实例标识（NWDAF实例）
- `IPV4ADDRESS`：UDN接收体验数据的IP地址
- NWDAF将该IP通过SMF传递给UPF，UPF后续向该地址上报重点用户体验数据
- UDN主备部署时需分别配置主备UDN上的IP地址
- IP地址来源：从LLD文档的"虚拟机资源需求"页签查看ufdrudpcollector个数，在"5G Core业务IP对接设计"页签查看PBU_I-C虚拟机vNIC2网口的IP

**UNC侧配置（典型场景）**:
```
// SMF支持体验感知信息采集订阅
SET SMCOMMFUNC: QOSEXPSW=Support;
// SMF支持事件订阅和上报
SET SMFFUNC: EVENTEXPOSURE=Support;
// 智能规则和UPF绑定关系
ADD UPFBINDSELRULE: INDEX=1, NFINSTANCENAME="upf_instance_1", RULENAME="select_ai_upf";
ADD UPFBINDSELRULE: INDEX=2, NFINSTANCENAME="upf_instance_2", RULENAME="select_ai_upf";
// UPF选择规则
ADD SELECTRULEINFO: RULENAME="select_ai_upf", RULEFUNC=QOSEXP;
// PFCP私有信元携带
SET PFCPPVTEXT: FEATURE=Qos_Experience, SWITCH=ENABLE;
// UPF权重调整
MOD PNFPROFILE: NFINSTANCEID="upf_instance_1", CAPACITY=60;
MOD PNFPROFILE: NFINSTANCEID="upf_instance_2", CAPACITY=60;
```

关键参数说明:
- `QOSEXPSW=Support`：SMF支持体验感知信息采集订阅
- `RULEFUNC=QOSEXP`：UPF选择规则功能为QoS体验感知
- `PFCPPVTEXT`：控制PFCP Session Modification Request消息SRR IE中是否携带私有信元QoS Experience Information
- `CAPACITY`：UPF权重，智能板UPF承载普通用户和智能业务双流量，权重需规划

**UNC侧配置（异厂商PCF场景 - 智能PCF选择）**:
```
// 开启智能双N7会话功能
SET IPEN7SESSFUNC: IPEN7SESSFUNC=ENABLE;
// 配置智能PCF组
ADD TNFGRP: TNFGRPINDEX=0, TNFTYPE=PCF, TNFGRPNAME="IPE_PCF_GROUP_0";
// 配置智能PCF实例
ADD TNFINS: TNFINSINDEX=1, TNFTYPE=PCF, TNFINSNAME="a6a61c6f-0d3a-4221-b1da-424eda3ccf67", SCHEMA=http, FQDN="pcf1.cluster1.net2.pcf.5gc.mnc012.mcc345.3gppnetwork.org", NFDESCNAME="IPE_PCF";
// 配置智能PCF实例IP
ADD TNFINSIP: TNFINSINDEX=1, IPTYPE=IPV4, IPV4ADDR="10.10.12.3", PORT=1234;
// 绑定关系
ADD TNFBINDGRP: TNFGRPINDEX=0, TNFINSINDEX=1, PRIORITY=1, WEIGHT=50;
// 主智能PCF组
SET DFTIPEPCFGRP: PRIMIPEPCFGRP="IPE_PCF_GROUP_0";
// 业务策略规则（SMF匹配用户套餐后与智能PCF建立第二个N7会话）
ADD RULE: RULENAME="testrulepcf", POLICYTYPE=PCC, POLICYNAME="pccprop_test", NWDAFEVENTS=QOS_ANALYSIS;
// 智能业务后缀匹配
ADD IPEN7SUFFIX: INTELLISUFFIX="rulepcf", INTELLINAME="LIVE_VIDEO";
```

关键参数说明:
- `IPEN7SESSFUNC=ENABLE`：使能智能双N7会话功能，SMF可与两个PCF分别建立N7会话
- `NWDAFEVENTS=QOS_ANALYSIS`：NWDAF数据分析事件类型
- `IPERULEDELYSW=DISABLE`：当UPF上无预定义规则时关闭智能规则传递开关
- `IPEN7SUFFIX`：智能业务后缀与PCF下发的rulename后缀匹配，匹配成功建立第二个N7会话

**UNC侧配置（异厂商PCF场景 - 智能UPF选择）**:
```
// SMF支持QoS质差分析
SET SMCOMMFUNC: QOSANASW=Support;
// 事件订阅和上报
SET SMFFUNC: EVENTEXPOSURE=Support;
// 用户模板
ADD USERPROFILE: USERPROFILENAME="testruleupf", UPTYPE=UPSELECT;
// UPF选择规则
ADD SELECTRULEINFO: RULENAME="testruleupf", RULEFUNC=QOSANA-1&QOSEXP-1, PRIORITY=0, DELIVERSW=DISABLE;
// UPF和规则绑定
ADD UPFBINDSELRULE: INDEX=0, NFINSTANCENAME="a6a61c6f-0d3a-4221-b1da-123eda3ccf76", RULENAME="testruleupf";
// PFCP私有信元
SET PFCPPVTEXT: FEATURE=Qos_Analysis, SWITCH=ENABLE;
SET PFCPPVTEXT: FEATURE=Qos_Experience, SWITCH=ENABLE;
```

关键参数说明:
- `QOSANASW=Support`：SMF支持QoS质差分析
- `UPTYPE=UPSELECT`：用户模板类型为UPF选择
- `RULEFUNC=QOSANA-1&QOSEXP-1`：规则同时包含质差分析和体验感知功能
- `DELIVERSW=DISABLE`：异厂商UPF不下发规则到UPF

#### 2.3.4 保障用户体验感知场景

保障用户体验感知场景依赖重点业务保障功能的配置，所有网元无新增配置：

| 网元 | 新增配置 |
|------|----------|
| UPCF | 无新增配置 |
| UDC | 无新增配置 |
| UNC | 无新增配置 |
| UDG | 无新增配置 |
| UDN | 新增北向上报体验单据的相关配置（资料受限公开） |

**保障用户调测验证流程（4步）**:

| 步骤 | 操作 | 预期结果 |
|------|------|----------|
| 1 | 用户正常访问测试应用5分钟 | 业务正常使用 |
| 2 | UDC跟踪查看UPF是否向NWDAF上报体验数据 | Nupf_EventExposureService_EventNotification Request，携带infoIndicate为QOS_EXP，subAppQosMonReport含带宽、时延、丢包数等KPI |
| 3 | UDC跟踪查看UDC是否向UDN发送体验数据 | Nudn_DataManagement_CreateUDNDataStoreRecord Request，携带带宽、时延、丢包数等KPI |
| 4 | 联系BOSS/SFTP侧确认体验数据 | 数据正常接收，内容符合预期 |

### 2.4 体验感知与带宽决策的关系

#### 2.4.1 体验感知采集的带宽KPI

体验感知解决方案采集的核心KPI中直接包含带宽信息：

- **带宽（Bandwidth）**：用户实际使用的上下行带宽
- **时延（Latency）**：业务传输时延
- **丢包数（Packet Loss）**：业务传输丢包数

这些KPI通过以下路径流转：
```
UDG(UPF) → UDC(NWDAF) → UDN(BOSS/SFTP)
         → NWDAF → 智能PCF（通过NWDAFEVENTS=QOS_ANALYSIS触发）
```

#### 2.4.2 QoE驱动带宽决策的机制

**闭环决策链路**:

1. **数据采集层**: UDG/UPF采集用户体验KPI（带宽、时延、丢包），通过EMS-UFDR消息上报
2. **数据分析层**: NWDAF接收体验数据，执行QoS质差分析（QOS_ANALYSIS）
3. **策略决策层**: 智能PCF基于NWDAF分析结果和用户套餐，生成QoS保障策略
4. **策略执行层**: SMF/UPF执行PCF下发的带宽策略（MBR/QoS调整）

**关键触发机制**:

- `NWDAFEVENTS=QOS_ANALYSIS`：SMF匹配规则后与智能PCF建立第二个N7会话，触发NWDAF向PCF提供QoS分析数据
- `RULEFUNC=QOSANA-1&QOSEXP-1`：规则同时包含质差分析和体验感知，确保数据采集和策略调整闭环
- `PFCPPVTEXT: FEATURE=Qos_Experience/Qos_Analysis`：控制PFCP消息中携带私有信元，传递体验数据

#### 2.4.3 体验感知与FUP的协同关系

| 维度 | FUP会话级 | 体验感知 |
|------|-----------|----------|
| 触发条件 | 累计流量达到阈值 | KPI指标变化（实时） |
| 决策来源 | PCRF/PCF预设策略 | NWDAF分析+PCF动态策略 |
| 执行方式 | MBR降速/新计费规则 | QoS调整/智能UPF选择 |
| 时间粒度 | 长周期（月/天） | 短周期（分钟级，上报周期300秒） |
| 带宽影响 | 达到阈值后限制带宽 | 基于体验反馈动态调整带宽 |

两者可协同工作：FUP负责基于流量总量的宏观管控，体验感知负责基于实时体验的微观优化。

---

## 3. 配置与调测要点（MML命令、步骤）

### 3.1 FUP会话级配置命令速查

| 命令 | 用途 | 关键参数 | 必选/可选 |
|------|------|----------|-----------|
| `SET LICENSESWITCH` | 打开License开关 | LICITEM, SWITCH | 必选 |
| `SET PCCFUNC` | 设置Monitoring-Key解析方式 | MKPARSEFORMAT, N7FEATURELIST | 可选 |
| `MOD PCRF` | 使能UMCH拥塞处理 | HOSTNAME, SUPFEANEGOSW, FEATURELIST | 可选 |
| `MOD PCCPOLICYGRP` | 配置业务流量排除 | PCCPOLICYGRPNM, FUPSESSIONEXC | 可选 |
| `SET SRVCOMMONPARA` | 重定向流量FUP排除 | REDIRECTFUP | 可选 |
| `LST LICENSESWITCH` | 查询License开关状态 | LICITEM | 调测用 |
| `LST APNPCCFUNC` | 查询指定DNN下PCC功能 | - | 排障用 |

### 3.2 体验感知配置命令速查

| 命令 | 用途 | 关键参数 | 适用场景 |
|------|------|----------|----------|
| `SET EXPBASICFUNC` | 开启体验业务功能 | SWITCH, ANARPTPERIOD, SRVPORT | 普通+重点 |
| `ADD SSUPROTCOLGROUP` | 定义协议组 | DEFPRTGRPNAME, PROTOCOLNAME | 普通+重点 |
| `ADDTO` `APPPOLICYCTRL` | 应用绑定协议组 | APPIDNAME, SUBAPPIDNAME, DEFPRTGRPNAME | 普通+重点 |
| `SET RPTGLBPARA` | 设置抽样率 | FLOWSAMPLERATE | 普通+重点 |
| `SET RPTGLBCFG` | TCP/UDP分析开关 | TCPINSIGHTSW, UDPINSIGHTSW | 普通+重点 |
| `ADD RPTSVR` | 配置报表服务器 | RPTSVRNAME, RPTSVRTYPE | 普通用户 |
| `ADD UDPADDR` | UDN接收体验数据IP | NFINSTANCEID, IPV4ADDRESS, INDEX | 重点用户 |
| `SET SMCOMMFUNC` | SMF体验感知/质差分析 | QOSEXPSW, QOSANASW | 重点用户 |
| `SET SMFFUNC` | SMF事件订阅上报 | EVENTEXPOSURE | 重点用户 |
| `ADD UPFBINDSELRULE` | 智能规则和UPF绑定 | INDEX, NFINSTANCENAME, RULENAME | 重点用户 |
| `ADD SELECTRULEINFO` | UPF选择规则 | RULENAME, RULEFUNC, PRIORITY | 重点用户 |
| `SET PFCPPVTEXT` | PFCP私有信元携带 | FEATURE, SWITCH | 重点用户 |
| `MOD PNFPROFILE` | UPF权重调整 | NFINSTANCEID, CAPACITY | 重点用户 |
| `SET IPEN7SESSFUNC` | 智能双N7会话 | IPEN7SESSFUNC | 异厂商PCF |
| `ADD TNFGRP/TNFINS` | 智能PCF组/实例 | TNFGRPINDEX, TNFINSNAME, FQDN | 异厂商PCF |
| `ADD TNFINSIP` | 智能PCF实例IP | TNFINSINDEX, IPV4ADDR, PORT | 异厂商PCF |
| `ADD TNFBINDGRP` | 实例绑定NF组 | TNFGRPINDEX, TNFINSINDEX, PRIORITY | 异厂商PCF |
| `SET DFTIPEPCFGRP` | 主智能PCF组 | PRIMIPEPCFGRP | 异厂商PCF |
| `ADD RULE` | 业务策略规则 | RULENAME, POLICYTYPE, NWDAFEVENTS | 异厂商PCF |
| `ADD IPEN7SUFFIX` | 智能业务后缀匹配 | INTELLISUFFIX, INTELLINAME | 异厂商PCF |
| `ADD USERPROFILE` | 用户模板 | USERPROFILENAME, UPTYPE | 异厂商PCF |
| `LOD SIGNATUREDB` | 加载协议特征库 | LOADMODE | 普通+重点 |
| `DSP SIGNATUREDB` | 查询协议特征库版本 | - | 普通+重点 |

### 3.3 配置依赖关系

**FUP配置依赖**:
```
PCC基本功能配置 → License加载 → SET LICENSESWITCH(UNC+UDG) → [可选] SET PCCFUNC → [可选] MOD PCRF → [可选] MOD PCCPOLICYGRP → [可选] SET SRVCOMMONPARA
```

**体验感知配置依赖（普通用户）**:
```
接口配置 → License加载 → 加载协议特征库 → SET LICENSESWITCH(7项) → SET EXPBASICFUNC → ADD SSUPROTCOLGROUP + ADD APPPOLICYCTRL → SET RPTGLBPARA → SET RPTGLBCFG → ADD RPTSVR
```

**体验感知配置依赖（重点用户）**:
```
重点业务保障配置(前置) → UDC: ADD UDPADDR → UDG: 同普通用户UDG配置 → UNC: SET SMCOMMFUNC + SET SMFFUNC + ADD UPFBINDSELRULE + ADD SELECTRULEINFO + SET PFCPPVTEXT + MOD PNFPROFILE
```

**体验感知配置依赖（异厂商PCF场景）**:
```
在重点用户典型场景基础上，增量配置: SET IPEN7SESSFUNC → ADD TNFGRP + ADD TNFINS + ADD TNFINSIP + ADD TNFBINDGRP → SET DFTIPEPCFGRP → ADD RULE + ADD IPEN7SUFFIX (智能PCF) 或 ADD USERPROFILE + ADD SELECTRULEINFO + ADD UPFBINDSELRULE (智能UPF)
```

---

## 4. 与带宽控制的关系

### 4.1 FUP会话级对带宽控制的直接作用

FUP会话级累计流量策略控制是带宽控制的核心手段之一：

1. **阈值触发带宽降速**: 当用户累计流量达到PCRF/PCF设定的阈值后，系统将MBR/AMBR降为设定的QoS带宽
2. **阈值触发新计费规则**: 达到阈值后PCRF/PCF可下发新的计费规则（如从高速档切换到低速档）
3. **公平使用保障**: 通过会话级累计监控，确保所有用户公平使用带宽资源

### 4.2 体验感知对带宽决策的间接作用

体验感知不直接控制带宽，但通过采集KPI反馈驱动带宽策略优化：

1. **KPI采集驱动分析**: UDG采集带宽、时延、丢包KPI，周期上报（300秒）
2. **NWDAF分析驱动策略**: NWDAF基于体验KPI执行QoS质差分析，为PCF提供决策依据
3. **智能PCF/UPF选择**: 异厂商场景下，SMF根据用户套餐匹配规则，选择智能PCF/UPF提供差异化带宽保障
4. **闭环优化**: 体验数据 → NWDAF分析 → PCF策略调整 → 带宽QoS变更 → 体验改善 → 新一轮采集

### 4.3 带宽控制场景中的定位

| 带宽控制能力 | 实现方式 | 本批次覆盖 |
|-------------|----------|-----------|
| 基于流量阈值的带宽限制 | FUP会话级累计流量策略控制 | 是（核心） |
| 基于实时体验的带宽优化 | 体验感知+NWDAF分析+智能PCF | 是（支撑） |
| 基于业务的带宽管控 | PCCPOLICYGRP排除/包含配置 | 部分（FUPSESSIONEXC） |
| 基于用户类型的带宽保障 | 智能UPF选择+UPF权重调整 | 是（重点用户） |

---

## 5. 关键概念术语

| 术语 | 全称/含义 | 说明 |
|------|-----------|------|
| FUP | Fair Usage Policy / 公平使用策略 | 基于累计流量的策略控制机制 |
| UMCH | Usage Monitoring Congestion Handling | 流量监控拥塞处理，防止配额重置时信令风暴 |
| UsageMonitoringData | 使用情况监控数据 | PCRF/PCF下发的会话级流量监控信息 |
| Monitoring-Key | 监控键值 | PCRF下发的流量监控标识，用于区分不同监控实例 |
| QoE | Quality of Experience | 用户体验质量，包含带宽、时延、丢包等KPI |
| QOS_EXP | QoS Experience | 体验感知功能标识，用于UPF选择规则和私有信元 |
| QOS_ANALYSIS | QoS质差分析 | NWDAF数据分析事件类型 |
| NWDAF | Network Data Analytics Function | 网络数据分析功能，体验感知分析中枢 |
| EMS-UFDR | - | UDG侧体验数据上报消息，携带QosExpRptData信元 |
| QosExpRptData | QoS Experience Report Data | 体验感知报告数据信元，含带宽/时延/丢包KPI |
| 智能PCF | Intelligent PCF | 支持体验感知能力的PCF，通过双N7会话机制实现 |
| 智能UPF | Intelligent UPF | 支持体验感知数据采集的UPF，通过UPF选择规则优选 |
| 双N7会话 | Dual N7 Session | SMF与普通PCF和智能PCF分别建立的N7接口会话 |
| UFDR | User Flow Data Report | 用户流量数据报告，体验数据北向上报通道 |
| Protocol Signature DB | 协议特征库 | UDG用于业务识别的特征数据库，需定期加载更新 |
| UE Category | 用户分类 | PCRF/PCF侧的用户类型分类，影响FUP阈值设置 |
| DELIVERSW | 是否下发给UPF | 规则下发开关，异厂商UPF场景设为DISABLE |
| IPEN7SUFFIX | 智能业务后缀 | 与PCF下发rulename后缀匹配，触发双N7会话建立 |

---

## 6. 知识来源

### 6.1 FUP会话级来源

| 序号 | 文档路径 | 核心内容 |
|------|----------|----------|
| 1 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/会话级累计流量策略控制/原理描述/系统影响与约束_70687833.md` | 系统性能影响、UMCH约束、UE Category阈值约束 |
| 2 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/会话级累计流量策略控制/调测会话级累计流量策略控制_24087906.md` | 12步完整调测流程、License验证、消息跟踪验证 |
| 3 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/会话级累计流量策略控制/配置会话级累计流量策略控制_23928082.md` | 配置命令全集（必选+可选）、UNC/UDG配置脚本 |
| 4 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/变更描述/20.7.0 01（2021-08-30）_24087900.md` | 版本变更记录 |
| 5 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/特性映射_23928078.md` | 会话级+业务级特性License映射（4个特性） |

### 6.2 体验感知来源

| 序号 | 文档路径 | 核心内容 |
|------|----------|----------|
| 6 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/保障用户体验感知场景/调测保障用户体验感知功能_90690618.md` | 保障用户调测4步流程、NWDAF/UDC上报验证 |
| 7 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/保障用户体验感知场景_94432534.md` | 保障用户场景网元配置总览（5网元） |
| 8 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/普通用户体验感知场景/UDG侧配置_15642930.md` | 普通用户UDG配置8步、7个License项、协议特征库加载 |
| 9 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/普通用户体验感知场景/调测普通用户体验信息感知功能_21534654.md` | 普通用户调测7步流程、Nupf_EventExposure验证 |
| 10 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/普通用户体验感知场景_36232121.md` | 普通用户场景概述（UDG+UDN） |
| 11 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/重点用户体验感知场景/UDC侧配置_05937066.md` | UDC侧ADD UDPADDR配置、IP地址获取方法 |
| 12 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/重点用户体验感知场景/UDG侧配置_15435520.md` | 重点用户UDG配置（与普通用户一致） |
| 13 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/重点用户体验感知场景/UNC侧配置/UNC侧配置（典型场景）_18425829.md` | UNC典型场景配置（SMCOMMFUNC、UPFBINDSELRULE、PFCPPVTEXT等） |
| 14 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/重点用户体验感知场景/UNC侧配置/配置SMF选择智能PCF及下发订阅策略（异厂商PCF场景）_31501709.md` | 异厂商PCF场景智能PCF选择配置（双N7会话、TNFGRP、IPEN7SUFFIX） |
| 15 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/重点用户体验感知场景/UNC侧配置/配置SMF选择智能UPF及下发订阅策略（异厂商PCF场景）_95822676.md` | 异厂商PCF场景智能UPF选择配置（QOSANASW、USERPROFILE、SELECTRULEINFO） |
