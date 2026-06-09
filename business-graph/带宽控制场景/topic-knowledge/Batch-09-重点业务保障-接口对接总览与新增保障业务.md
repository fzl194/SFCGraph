# Batch-09 重点业务保障：接口对接总览与新增保障业务

---

## 1. 概述

本批文档来自"5G Core 重点业务保障解决方案"业务专题，涵盖两大主题：

**接口对接配置**：重点业务保障解决方案涉及 UDC（含 NWDAF 功能）、UDG（UPF）、UNC（SMF）、UPCF（智能 PCF）、CloudUDN 等多个网元之间的服务化接口（SBI）和非服务化接口的配置。核心是让 NWDAF（数据分析功能）能够与 SMF、PCF、UPF、UDN 等网元建立通信链路，实现网络数据的采集、分析和策略下发。

**新增保障业务**：当运营商在初始部署后需要新增保障业务时，UDC 侧通过 ADD APPGROUP 和 ADD APP 命令完成增量配置。保障类型分为 GBR（保证比特速率）和 Non-GBR（非保证比特速率）两种，对应不同的 QoS 参数集和带宽控制策略。

10 篇文档覆盖了：
- 接口配置总览（完整接口拓扑表）
- UDC 侧 NWDAF 本局数据配置（实例信息、Profile、TAI/服务）
- UDC 侧 SBI 接口配置（HTTP 端点、NRF 对接）
- UDC 侧本地 NRF 配置（静态发现 SMF/PCF/UDN）
- UDC 侧 NWDAF 配置调测验证
- UDG 侧 Nupf 接口数据配置（UPF 与 NWDAF 对接）
- UNC 侧配置（异厂商 PCF 场景 N7 接口）
- UPCF 侧 NWDAF 对接数据配置（N23/N5 接口）
- 新增保障业务 GBR 保障配置
- 新增保障业务 Non-GBR 保障配置

---

## 2. 核心知识点

### 2.1 接口配置总览：完整接口拓扑

重点业务保障解决方案的接口拓扑如下表所示，各网元之间的通信关系是理解整个方案的基础：

| 产品 | 通信NF | 参考点 | 接口类型 | 服务化接口 | 配置说明 |
|------|--------|--------|----------|-----------|---------|
| UPCF | PCF<->NWDAF | N23 | SBI | Nnwdaf | UPCF通过N23向NWDAF订阅用户体验分析数据 |
| UPCF | PCF<->NWDAF | N5 | SBI | Npcf | 非本方案新增，现网未配置时需配置 |
| UPCF | PCF<->SMF | N7 | SBI | Npcf | 异厂商PCF场景下需配置双N7接口 |
| UDC | NWDAF<->SMF | - | SBI | Nsmf | NWDAF为5GC新增网元，需配置本局数据和SBI接口 |
| UDC | NWDAF<->PCF | N23 | SBI | Nnwdaf | 需配置本局数据和SBI接口 |
| UDC | NWDAF<->PCF | N5 | SBI | Npcf | 需配置本局数据和SBI接口 |
| UDC | NWDAF<->UPF | - | SBI | Nupf | NWDAF侧无需配置，被动建链 |
| UDC | NWDAF(UDC)<->NWDAF(UDN) | - | SBI | Nudn | 通过本地NRF直连实现 |
| UNC | SMF<->UPF | N4 | 非服务化 | - | 基础组网接口，无新增配置 |
| UNC | SMF<->NWDAF | - | SBI | Nsmf | 基础组网接口，无新增配置 |
| UNC | SMF<->PCF | N7 | SBI | Npcf | 异厂商PCF场景需配置与智能PCF之间的第二个N7接口 |
| UDG | UPF<->NWDAF | - | SBI | Nnwdaf | HTTP接口直连NWDAF |
| CloudUDN | UDN<->UDN | - | 私有 | - | 主备容灾场景通信接口 |
| CloudUDN | NWDAF(UDN)<->NWDAF(UDC) | - | SBI | Nudn | 配置跨域NWDAF通信 |
| CloudUDN | UDN<->RAN-OAM | - | FTP/SFTP | - | 获取无线侧性能指标 |

**关键理解**：NWDAF 是本方案的中心节点。UDC 部署 NWDAF 功能，负责采集 SMF/PCF/UPF 的数据并分析；UPCF（智能PCF）通过 N23 接口订阅 NWDAF 分析结果，生成 QoS 策略；UPF 通过 Nupf 接口向 NWDAF 上报用户面数据。

### 2.2 NWDAF 本局数据配置要素

NWDAF 本局数据是 UDC 上 NWDAF 功能运行的基础，包含以下层级配置：

**第一层：运营商基础信息**
- `MOD NGMNO`：运营商信息（NOID/FULLNAME/SHORTNAME）
- `ADD NGHPLMN`：Home PLMN 信息（MCC/MNC）
- UDC 默认已配置 NOID=0 的记录，通常不需单独配置

**第二层：NWDAF 实例信息**
- `ADD NFUUID`：配置 NWDAF 的 NF 实例标识（NFTYPE=NfNWDAF）
- `ADD NFPROFILE`：NWDAF Profile 信息（NFTYPE/ NFSTATUS=Registered/FQDN）
- 关键：NF Instance ID 最后 12 位为 NodeID，可自定义

**第三层：TAI/TAC 区域与分析事件**
- `ADD NFTAI`：NWDAF 支持的 TAI 信息（MCC/MNC/TAC）
- `ADD TAIRANGELIST` + `ADD TACRANGE`：TAI 区域范围配置
- `ADD NWDAFINFO`：分析事件配置（QOS_ANALYSIS / QOS_EXP_ANALYSIS）
- `ADD NWDAFINFOEXT`：不同区域支持不同分析事件的场景

**第四层：服务实例**
- `ADD NFSERVICE`：NWDAF 提供的服务（如 NnwdafEvntSubs、NnwdafDataManagement）
- `ADD NFSERVICEVER`：服务版本信息（如 1.R15.0.0）

**两种 NwdafInfo 注册模式**：
- **统一模式**：`ADD NWDAFINFO` 配置所有区域都支持相同的分析事件
- **分区模式**：`ADD NWDAFINFOEXT` 为不同区域（通过 BINDNWDAFINFOID）配置不同的分析事件组合

### 2.3 SBI 接口配置与 NRF 对接

SBI（Service Based Interface）接口采用 HTTP/2 协议栈，传输层统一 HTTP/2，应用层携带不同服务消息。

**SBI 接口角色分配**（NWDAF 侧）：

| 接口 | 对接NF | 是否通过NRF查找 | NWDAF角色 |
|------|--------|----------------|-----------|
| Nsmf | SMF | 是 | 既作Client又作Server |
| Nupf | UPF | 否 | 仅作Server（被动建链） |
| Nnrf | NRF | 否 | 需配置与NRF对接数据 |
| N23 | PCF | 是 | 作Server |
| N5 | PCF | 是 | 既作Client又作Server |
| Nudn | UDN | 否 | 仅通过本地NRF |

**SBI 配置步骤**：
1. `ADD LOGICIP`：配置逻辑 IP（Server 和 Client 分别配置）
2. `ADD HTTPLEGRP`：HTTP 本端实体组
3. `ADD HTTPLE`：HTTP 本端实体（Server/Client 分别配置，端口 80）
4. `ADD SBIAPLE`：SBI 本端实体（NFTYPE=NFTypeNWDAF）
5. `ADD NRF` + `ADD NRFADDR` + `ADD NRFPARA`：NRF 对接数据
6. `ACT NFONLINE`：激活 NWDAF 向 NRF 的注册

**关键约束**：
- NWDAF 的 SBI 业务 IP 地址不能与其他接口业务 IP 共用
- 端口号无明确指定时使用 HTTP 知名端口 80
- 一个 NF 类型需配置一个 HTTP 本端端点组
- VPN 实例名称（VPN_SBI）需与 LLD 规划一致

### 2.4 本地 NRF 的作用与配置

**本地 NRF 的定位**：当网络中无 NRF，或网络有 NRF 但需基于运营商策略本地配置周边 NF 时，通过本地 NRF 手工配置 UDC 与周边 NF 的逻辑连接。

**与远程 NRF 的关系**：即使网络部署了 NRF，NWDAF(UDC) 与 NWDAF(UDN) 的对接也必须通过本地 NRF 直连实现。因此 `SET NFDISCPLCY` 的"服务发现策略"不能配置为 REMOTE_ONLY。

**本地 NRF 配置对象**：
- **到 SMF**：`ADD PNFPROFILE`(NFTYPE=NfSMF) + `ADD PNFSERVICE`(SERVICENAME=NsmfEventExp)
- **到 PCF**：`ADD PNFPROFILE`(NFTYPE=NfPCF) + `ADD PNFSERVICE`(SERVICENAME=NpcfPlcAuth)
- **到 UDN**：`ADD PNFPROFILE`(NFTYPE=NfUDN) + `ADD PNFSERVICE`(SERVICENAME=NudnDm)

**主备 UDN 场景**：通过 PRIORITY 参数区分主备 UDN 优先级（PRIORITY=1 高于 PRIORITY=5）。

**UUID 要求**：NWDAF 使用 LocalNRF 查找 SMF 和 PCF 时，NF 实例标识需配置为 UUID 格式，需在对端 NF 上执行 `LST NFUUID` 查询。

### 2.5 Nupf 接口数据配置（UDG 侧）

UPF（UDG）与 NWDAF 之间通过 Nupf 接口建立逻辑连接，实现用户面数据上报。

**配置前置条件**：需先安装 SSU 服务和 SBIM 服务。

**配置链路**：
1. `ADD LOGICIP`：Nupf 逻辑 IP（VPNINSTNAME=VRF_Nupf），Server 和 Client 分别配置
2. `ADD HTTPLEGRP`：HTTP 本端实体组
3. `ADD HTTPLE`：HTTP 本端实体（SERVER 端口 80，CLIENT 无端口）
4. `ADD SBIAPLE`：SBI 本端实体（NFTYPE=NFTypeUPF）
5. `SET HTTPCONF`：HTTP 属性（INITLINKINTVL=500, LINKAGINGTIME=120）

**关键约束**：逻辑接口的 VPN 必须与对应外联口的 VPN 相同（VRF_Nupf），否则报文查询路由失败。

**验证方法**：NGPING 检查逻辑接口 IP 互通 -> PING 检查外联口 IP 互通 -> 检查直连路由器路由。

### 2.6 UPCF 与 NWDAF 的对接数据

UPCF（智能 PCF）通过 N23 接口向 NWDAF 下发订阅用户体验分析数据请求。

**核心配置流程**：

**步骤一：基础设施配置**
- `ADD HLBDEVADDR`：增加 HLB 服务用于与 NWDAF 对接的本端 IP 地址
- `MOD INSP`：开启会话备份功能（VRM_SESSIONBACKUPSWITCH=3）

**步骤二：N23 接口功能开关**
- `MOD INSP: VRM_N23SWITCH=1`：开启 N23 接口功能
- `MOD INSP: VRM_N23SESSIONBACKUP=1`：开启 N23 会话备份
- `SET SBIDEVAUDIT: SBITYPE=N23, PERIODICDATIME=30`：N23 会话审计（时长应小于 NWDAF 的 N23 会话老化时长）
- `MOD INSP: VRM_SYNTIMER=1`：用户定时器持久化
- `SET EDRREPORT: SWITCH=N23SignalingEDR`：N23 信令 EDR

**步骤三：NWDAF 服务发现（两种模式）**

*动态发现模式*（通过 NRF）：
- `ADD DISCCONDCFG: NFTYPE=NWDAF, NWDAFPARASW=TAI-1&EVENT-1`：指定条件发现
- `SET DISCNFTYPECFG: NFTYPE=NWDAF, SWITCH=ON`：按网元类型发现
- `SET NFDISCCFG: NRFDISCSW=NWDAFDISC-1`：允许向 NRF 发起 NWDAF 发现

*静态发现模式*（不通过 NRF）：
- `ADD DISCNFPROFILE`：配置 NWDAF 网元实例的完整 Profile JSON
- `SET NFDISCCFG: NRFDISCSW=NWDAFDISC-0`：禁止向 NRF 发起发现

**步骤四：N5 接口服务注册**（QoS 加速策略场景）
- `ADD NFSERVICE: SERVICENAME=npcf-policyauthorization`：向 NRF 注册 N5 接口服务名

**异厂商 PCF 场景特殊处理**：智能 PCF 与 NWDAF 之间的服务发现条件不携带 TAI，只勾选 EVENT(EVENT)。

### 2.7 新增保障业务：GBR vs Non-GBR

新增保障业务是重点业务保障解决方案的增量配置环节，分两种保障类型：

**GBR（保证比特速率）保障**：

| 参数 | 说明 | 取值样例 |
|------|------|---------|
| GUARANTEETYPE | 保障类型 | GBR（GBR文档中ADD APPGROUP未显式包含此参数，由APPGROUP类型隐式确定） |
| APPGROUPTYPE | 应用组类型 | MOBILE_GAME |
| FQI | QoS标识 | 4 |
| ARPVALUE | 分配保留优先级 | 1 |
| GBRULVALUE | 保证上行带宽(kbit/s) | 3000 |
| GBRDLVALUE | 保证下行带宽(kbit/s) | 3000 |
| MBRULVALUE | 最大上行带宽(kbit/s) | 1000000 |
| MBRDLVALUE | 最大下行带宽(kbit/s) | 1000000 |

**Non-GBR（非保证比特速率）保障**：

| 参数 | 说明 | 取值样例 |
|------|------|---------|
| GUARANTEETYPE | 保障类型 | Non-GBR |
| APPGROUPTYPE | 应用组类型 | MOBILE_GAME |
| FQI | QoS标识 | 7（与GBR不同） |
| ARPVALUE | 分配保留优先级 | 1 |
| MBRULVALUE | 最大上行带宽(kbit/s) | 6000 |
| MBRDLVALUE | 最大下行带宽(kbit/s) | 6000 |

**核心差异**：
- GBR 保障包含 GBRULVALUE/GBRDLVALUE（保证带宽参数），Non-GBR 不含
- GBR 的 FQI 值通常较低（如 4），Non-GBR 的 FQI 值通常较高（如 7）
- GBR 的 MBR 通常远大于 GBR（如 MBR=1000000 vs GBR=3000），表示最大可突破到很高带宽
- Non-GBR 只有 MBR 限制，不提供保证带宽

**两种新增场景**：
- **场景一**：已有应用组中增加应用 -> 仅执行 `ADD APP`
- **场景二**：新增应用组类型 -> 先 `ADD APPGROUP` 再 `ADD APP`

### 2.8 GBR 保障的智能码率功能

GBR 保障场景支持智能码率识别，通过以下命令配置：

- `STR TRAININGPROCESS`：启动应用的智能档位识别训练
- `ADD BANDWIDBNDAPP`：为应用配置多个带宽档位（BITRATESTART/BITRATEEND）
- `ADD APPBANDMATCHPLY`：设置带宽档位匹配规则优先级
  - CODETRAIN=FIRST_PRIORITY：智能算法训练优先
  - FROMCONFIG=SECOND_PRIORITY：配置带宽档位优先
  - DEFAULTMBR=THIRD_PRIORITY：默认最高档位保障

**智能码率配置前提**：`ADD APP` 命令中需设置 CODETRAINSW=ENABLE。

### 2.9 保障应用的计费配置

计费标识（CHARGINGID）的配置取决于计费方案选择：

| 计费方案 | CHARGINGID 配置 | 说明 |
|---------|----------------|------|
| 保障流量归一化计费 | 无需配置 | 与普通流量统一计费 |
| 保障流量独立计费 | 必须配置 | 配置保障应用的计费 RG |
| 异厂商 PCF 场景 | 不支持 | 不配置该参数 |

---

## 3. 配置调测要点

### 3.1 NWDAF 配置调测验证（UDC 侧）

**路由连通性检查**：
```
NGPING: IPTYPE=IPv4, VPNNAME="VRF_SBI", SRCIPV4ADDR="本端SBI地址", DSTIPV4ADDR="对端NF地址";
```
预期结果：看到响应报文，有成功收发包个数。

**服务化链路状态检查**：
- NWDAF 作为服务端：`DSP SBILINKSTATUS: ENTITYTYPE=Server;` -> 链路状态为 Normal
- NWDAF 作为客户端：`DSP SBILINKSTATUS: ENTITYTYPE=Client, PEERNFINSTID="nf_instance_0";` -> 链路状态为 Normal

**NRF 注册验证**：
- 查询已注册 NF 实例：`DSP REGNFINSTANCE:;` -> 可查看到 NWDAF 注册信息
- 查询 NF Profile：`DSP REGNFINFO: NFINSTANCEID="实例ID";` -> Profile 与配置一致
- 验证 NF 状态为 REGISTERED

### 3.2 Nupf 接口调测验证（UDG 侧）

**逻辑接口 IP 互通**：
```
NGPING: IPTYPE=IPv4, VPNNAME="VRF_Nupf", SRCIPV4ADDR="10.1.20.1", DSTIPV4ADDR="NWDAF的Nupf接口IP";
```

**外联口 IP 互通**：
```
PING: IPVERSION=IPv4, VPNNAME="VRF_Nupf", SOURCEIPV4ADDRESS="UPF Nupf外联口IP", DESTIPV4ADDRESS="NWDAF Nupf逻辑接口对应外联口IP";
```

**故障排查路径**：NGPING 失败 -> PING 检查外联口 -> 检查直连路由器路由 -> 检查 VNF 侧 IP 路由数据 -> 收集信息寻求技术支持。

### 3.3 UPCF N23/N5 接口调测验证

**N23 接口调测**：
```
NGPING: IPTYPE=IPv4, VPNNAME="VPN_SBI", SRCIPV4ADDR="UPCF的N23接口IP", DSTIPV4ADDR="NWDAF的Nnwdaf接口IP";
```

**N5 接口调测**：
```
NGPING: IPTYPE=IPv4, VPNNAME="VPN_SBI", SRCIPV4ADDR="UPCF的N5接口IP", DSTIPV4ADDR="NWDAF的Npcf接口IP";
```

**UPCF 公共信息验证**：
- `LST NFCOMINFO:;` -> "允许的网元类型"应为 NULL
- 若不为 NULL：`MOD NFCOMINFO: NFCOMINFOID="COMINFO-1", CHECKIPADDR=YES, ALLOWEDNFTYPES=" ";`

### 3.4 UPCF 关键内参开关汇总

| 参数名 | 取值 | 作用 |
|--------|------|------|
| VRM_SESSIONBACKUPSWITCH | 3 | 开启会话备份功能 |
| VRM_N5SESSIONBACKUP | 1 | 开启N5会话备份（QoS加速场景） |
| VRM_N23SWITCH | 1 | 开启N23接口功能 |
| VRM_N23SESSIONBACKUP | 1 | 开启N23会话备份 |
| VRM_N23HDPCFIDMODE | 1 | N23头域填充subsPcfId |
| VRM_SYNTIMER | 1 | 用户定时器持久化 |

### 3.5 UNC 侧配置要点

典型场景下 UNC-SMF 侧无新增接口。异厂商 PCF 场景需配置 SMF 与智能 PCF 之间的第二个 N7 接口。

**全省 2C SMF 软参**：
```
SET SMFSOFTPARAOFBIT: DT=Dw, DWORDNUM=1038, VALUE=VALUE_1, POSITION=25;
```
作用：控制 I-SMF 给锚点 SMF 的 HSMFUpdate 消息中携带 amfNfId。

### 3.6 新增保障业务关键 MML 命令汇总

**应用组配置**：
- `ADD APPGROUP`：新增应用组（含 QoS 参数、带宽参数）
- 应用组名称需与 PCF、UPF 配置一致

**应用配置**：
- `ADD APP`：新增应用并绑定到应用组
- 应用名称需与 UPF 配置一致

**智能码率配置（仅 GBR）**：
- `STR TRAININGPROCESS`：启动训练
- `ADD BANDWIDBNDAPP`：配置带宽档位
- `ADD APPBANDMATCHPLY`：配置档位匹配优先级

---

## 4. 与带宽控制的关系

这批接口对接和业务配置文档在带宽控制全链路中的位置如下：

### 4.1 数据采集层

**UPF -> NWDAF（Nupf 接口）**：UDG 侧配置 Nupf 接口数据，使 UPF 能够向 NWDAF 上报用户面流量统计数据（如应用识别结果、流量统计、体验指标）。这是带宽控制的数据来源。

**SMF -> NWDAF（Nsmf 接口）**：SMF 向 NWDAF 上报会话管理事件（如 PDU 会话建立/释放），帮助 NWDAF 了解会话上下文。

**CloudUDN -> RAN-OAM（FTP/SFTP）**：获取无线侧性能指标，作为无线侧带宽分析的补充数据。

### 4.2 数据分析层

**NWDAF 分析引擎**：基于采集的 UPF 用户面数据、SMF 会话事件、无线侧指标，NWDAF 执行 QOS_ANALYSIS（QoS 分析）和 QOS_EXP_ANALYSIS（体验感知分析），生成用户体验分析结果。

**NWDAF(UDC) <-> NWDAF(UDN)**：通过本地 NRF 直连，实现跨域数据分析协同。

### 4.3 策略决策层

**UPCF <- NWDAF（N23 接口）**：UPCF（智能 PCF）通过 N23 接口订阅并获取 NWDAF 的用户体验分析数据，据此生成 QoS 加速策略和带宽保障决策。

**UPCF -> SMF（N7 接口）**：UPCF 将策略下发给 SMF（UNC），异厂商 PCF 场景需配置双 N7 接口（大网 PCF + 智能 PCF）。

### 4.4 保障执行层

**UDC 侧应用组配置**：`ADD APPGROUP` 和 `ADD APP` 定义了保障业务的 QoS 参数（FQI、ARP、GBR/MBR），这些参数通过 NWDAF 分析触发，由 UPCF 决策后下发到 SMF/UPF 执行。

**GBR 保障 -> 带宽控制**：GBRULVALUE/GBRDLVALUE 直接设定保证带宽，MBRULVALUE/MBRDLVALUE 设定最大带宽上限，实现精确的带宽控制。

**Non-GBR 保障 -> 带宽控制**：仅通过 MBR 限制最大带宽，适用于非实时但对带宽有上限要求的业务。

**智能码率识别 -> 动态带宽调整**：GBR 保障场景的智能码率功能（ADD BANDWIDBNDAPP + ADD APPBANDMATCHPLY）实现了基于应用码率特征的动态带宽档位调整，是带宽控制的高级形态。

### 4.5 带宽控制全链路映射

```
数据采集 (Nupf/Nsmf) -> NWDAF分析 (QOS_ANALYSIS) -> UPCF策略决策 (N23订阅)
    -> 策略下发 (N7到SMF) -> UPF执行 (QoS规则+带宽限速)
    -> 增量配置 (ADD APPGROUP/ADD APP定义QoS参数)
```

---

## 5. 关键术语

| 术语 | 全称/含义 |
|------|----------|
| NWDAF | Network Data Analytics Function，网络数据分析功能，5GC 核心网元，负责数据采集与分析 |
| NRF | Network Repository Function，网络存储库功能，提供 NF 服务注册与发现 |
| SBI | Service Based Interface，服务化接口，基于 HTTP/2 的服务间通信架构 |
| Nupf | UPF 与 NWDAF 之间的服务化接口，用于用户面数据上报 |
| N23 | PCF 与 NWDAF 之间的参考点，UPCF 通过此接口订阅分析数据 |
| N5 | PCF 与 AF/PCF 之间的参考点，用于策略授权 |
| N7 | SMF 与 PCF 之间的参考点，用于策略下发 |
| N4 | SMF 与 UPF 之间的接口（非服务化），用于会话管理规则下发 |
| Nudn | NWDAF(UDC) 与 NWDAF(UDN) 之间的服务化接口 |
| UDC | Huawei UDG Data Center，华为用户数据中心（控制面，含 NWDAF 功能） |
| UDG | Huawei User Data Gateway，华为用户面网关（含 UPF 功能） |
| UNC | Huawei Unified Network Controller，华为统一网络控制器（含 SMF 功能） |
| UPCF | Huawei Unified PCF，华为统一策略控制功能（智能 PCF） |
| CloudUDN | Cloud User Data Network，云端用户数据网络 |
| FQI | Flow QoS Identifier，流级 QoS 标识 |
| ARP | Allocation and Retention Priority，分配保留优先级 |
| GBR | Guaranteed Bit Rate，保证比特速率 |
| MBR | Maximum Bit Rate，最大比特速率 |
| TAI | Tracking Area Identity，跟踪区域标识 |
| NF Profile | Network Function Profile，网元功能描述信息 |
| Local NRF | 本地 NRF，手工配置周边 NF 的逻辑连接，不依赖远程 NRF |
| HLB | Huawei Load Balance，华为负载均衡服务 |
| EDR | Event Data Record，事件数据记录 |
| SSU | Shared Service Unit，共享服务单元 |
| SBIM | SBI Management，服务化接口管理服务 |

---

## 6. 知识来源

| 序号 | 文件名 | 内容主题 |
|------|--------|---------|
| 1 | 调测NWDAF配置_57682741.md | UDC 侧 NWDAF 配置调测验证步骤 |
| 2 | 配置NWDAF本局数据_57602561.md | UDC 侧 NWDAF 实例信息、Profile、TAI、服务配置 |
| 3 | 配置SBI接口_09763604.md | UDC 侧 SBI 接口配置（HTTP端点、NRF对接、接口角色） |
| 4 | 配置本地NRF_09923084.md | UDC 侧本地 NRF 配置（静态发现 SMF/PCF/UDN） |
| 5 | 配置Nupf接口数据_18470868.md | UDG 侧 Nupf 接口数据配置（UPF 与 NWDAF 对接） |
| 6 | UNC侧配置_35434301.md | UNC 侧配置（异厂商 PCF 场景 N7 接口和软参） |
| 7 | 配置UPCF与NWDAF的对接数据_88915249.md | UPCF 侧 N23/N5 接口配置（开关、服务发现、Profile） |
| 8 | 接口配置总览_24938213.md | 完整接口拓扑表（各网元接口对应关系） |
| 9 | 配置新增保障应用GBR保障_12266562.md | UDC 侧新增 GBR 保障业务配置（含智能码率） |
| 10 | 配置新增保障应用Non-GBR保障_82035082.md | UDC 侧新增 Non-GBR 保障业务配置 |

**原始路径前缀**：`output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/`

- 文件 1-4: `接口对接配置/UDC侧配置/`
- 文件 5: `接口对接配置/UDG侧配置/`
- 文件 6: `接口对接配置/`
- 文件 7: `接口对接配置/UPCF侧配置/`
- 文件 8: `接口对接配置/`
- 文件 9-10: `新增保障业务/UDC侧配置/`
