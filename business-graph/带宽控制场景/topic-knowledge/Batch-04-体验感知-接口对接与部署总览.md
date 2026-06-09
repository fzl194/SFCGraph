# Batch-04: 体验感知 - 接口对接与部署总览

> **来源**: UDG 5G Core 体验感知解决方案 - 接口对接(UDC/UDG/UNC/UPCF) + 部署总览 + License
> **文件数**: 10 md
> **带宽控制聚焦**: 体验感知全链路接口配置支撑带宽决策闭环

---

## 1. 文档概述（部署总览、接口配置总览）

### 1.1 体验感知解决方案定位

5G Core 体验感知解决方案是华为在5G核心网中实现用户业务体验数据采集、分析和策略反馈的端到端方案。该方案覆盖三类用户：

| 用户类型 | 核心采集对象 | 数据链路 | 带宽控制关联 |
|----------|-------------|----------|-------------|
| 保障用户 | 重点保障用户的QoS/体验数据 | UPF->NWDAF(UDC)->PCF->SMF->UPF策略闭环 | QoS加速/重点保障直接影响带宽分配 |
| 重点用户 | 重点用户的体验感知信息 | UPF->NWDAF(UDN)+UPF->NWDAF(UDC) | 体验分析可触发带宽调整策略 |
| 普通用户 | 普通用户的体验感知信息 | UPF->NWDAF(UDN) | 大规模体验数据支撑带宽策略优化 |

### 1.2 部署总览

体验感知解决方案涉及以下网元的部署或升级：

| 网元 | 部署要求 | 带宽控制角色 |
|------|----------|-------------|
| NWDAF(UDC) | 新建，逻辑分省 | 作为体验数据分析中心，向PCF下发QoS分析结果，间接驱动带宽策略调整 |
| NWDAF(UDN) | 新建，逻辑分省 | 作为体验数据汇聚和北向上报中心，支撑大数据分析 |
| UPF | 新建或智能改造（仅ARM平台），需具备智能板 | 执行带宽策略的网元，同时采集体验数据上报 |
| PCF | 升级到配套版本 | 接收NWDAF分析结果，生成策略下发给SMF/UPF |
| SMF | 升级到配套版本 | 在策略控制链路中转发策略到UPF |
| NRF | 升级到配套版本 | 提供服务发现功能，支撑SBI接口对接 |

**UPF关键约束**: 为支持同时签约双域智能分流和重点业务保障的用户同时享有两种服务，至少一对智能UPF必须支持双域智能分流业务。如果网络中无同时支持两种业务的UPF，会导致同时签约两种业务的用户在享用双域智能分流业务时无法同时享用重点业务保障。

### 1.3 接口配置总览

体验感知全链路涉及多个产品和多类接口，接口矩阵如下：

| 产品 | 通信NF | 接口名称 | 接口类型 | 保障用户 | 重点用户 | 普通用户 | 配置参考 |
|------|--------|----------|----------|----------|----------|----------|----------|
| UPCF | PCF<->NWDAF(UDC) | N23/Nnwdaf | SBI | Yes | Yes | No | UPCF侧配置 |
| UPCF | PCF<->NWDAF(UDC) | N5/Npcf | SBI | Yes | No | No | UPCF侧配置 |
| UPCF | PCF<->SMF | N7/Npcf | SBI | Yes | Yes | No | UPCF产品文档 |
| UDC | NWDAF(UDC)<->SMF | Nsmf | SBI | Yes | Yes | No | UDC侧配置 |
| UDC | NWDAF(UDC)<->PCF | N23/Nnwdaf | SBI | Yes | Yes | No | UDC侧配置 |
| UDC | NWDAF(UDC)<->PCF | N5/Npcf | SBI | Yes | No | No | UDC侧配置 |
| UDC | NWDAF(UDC)<->UPF | Nupf | SBI | No | No | No | NWDAF侧无需配置 |
| UDC | NWDAF(UDC)<->NWDAF(UDN) | Nudn | SBI | Yes | Yes | 可选 | 配置本地NRF |
| UNC | SMF<->UPF | N4 | 非SBI | NA | NA | NA | 无新增 |
| UNC | SMF<->NWDAF(UDC) | Nsmf | SBI | NA | NA | NA | 无新增 |
| UNC | SMF<->PCF | N7/Npcf | SBI | Yes | Yes | No | UNC侧配置(异厂商PCF) |
| UDG | UPF<->NWDAF(UDC) | Nupf | SBI | Yes | No | Yes | UDG侧配置 |
| UDG | UPF<->NWDAF(UDN) | Nupf | SBI | No | No | Yes | UDG侧配置 |
| UDG | UPF<->NWDAF(UDN) | NupfR | 私有接口 | No | Yes | Yes | 配置NupfR接口数据 |
| CloudUDN | NWDAF(UDN)<->NWDAF(UDC) | Nudn | SBI | Yes | 可选 | 可选 | CloudUDN侧配置 |

**关键解读（带宽控制视角）**:
- 保障用户的带宽策略闭环路径: UPF -> Nupf接口 -> NWDAF(UDC) -> N23接口 -> PCF(UPCF) -> N7接口 -> SMF(UNC) -> N4接口 -> UPF策略执行
- 重点用户体验数据路径: UPF -> NupfR私有接口 -> NWDAF(UDN)
- 普通用户体验数据路径: UPF -> Nupf SBI接口 -> NWDAF(UDN)

---

## 2. 核心知识点

### 2.1 UDC侧接口配置（NWDAF本局数据、SBI、NRF）

#### 2.1.1 配置NWDAF本局数据

UDC侧NWDAF本局数据配置是体验感知方案的基础，包括运营商信息、NWDAF实例信息和NWDAF服务信息三大部分。

**配置步骤**:

**步骤1: 配置运营商基础信息**

当前UDC中默认已配置NOID=0的默认记录，一般无需单独配置。如需修改，使用：

```
MOD NGMNO: NOID=0, FULLNAME="Operator A", SHORTNAME="OA", DESC="Operator A";
ADD NGHPLMN: NOID=0, MCC="460", MNC="03";
```

**步骤2: 配置NWDAF实例信息**

NWDAF实例配置是UDC作为NWDAF网元的身份注册数据，包含四个子步骤：

(a) 配置NWDAF实例名称:
```
ADD NFUUID: NFTYPE=NfNWDAF, NFINSTANCENAME="NWDAF_Instance_0";
```

(b) 配置NWDAF实例Profile信息:
```
ADD NFPROFILE: NFINSTANCENAME="NWDAF_Instance_0", NFTYPE=NfNWDAF, NFSTATUS=Registered, FQDN="NWDAF.fqdn";
```

(c) 配置TAI/TAI区域信息及分析事件 -- 两种模式:

**模式A: 所有区域支持相同分析事件**
```
ADD NFTAI: NFINSTANCENAME="NWDAF_Instance_0", MCC="460", MNC="03", TAC="000201";
ADD TAIRANGELIST: NFINSTANCENAME="NWDAF_Instance_0", NFTYPE=NfNWDAF, MCC="460", MNC="03", TACRANGEINDEX=1;
ADD TACRANGE: INDEX=1, RANGESTART="000001", RANGEEND="000100";
ADD NWDAFINFO: INSTANCENAME="NWDAF_Instance_0", NWDAFEVENTS=QOS_ANALYSIS-1&QOS_EXP_ANALYSIS-1;
```

**模式B: 不同区域支持不同分析事件**（需使用NWDAFINFOEXT绑定）
```
ADD NWDAFINFOEXT: INSTANCENAME="NWDAF_Instance_0", ID="info1", NWDAFEVENTS=QOS_ANALYSIS-1&QOS_EXP_ANALYSIS-0;
ADD NWDAFINFOEXT: INSTANCENAME="NWDAF_Instance_0", ID="info2", NWDAFEVENTS=QOS_ANALYSIS-0&QOS_EXP_ANALYSIS-1;
ADD NFTAI: NFINSTANCENAME="NWDAF_Instance_0", MCC="460", MNC="03", TAC="111111", BINDNWDAFINFOID="info1";
ADD NFTAI: NFINSTANCENAME="NWDAF_Instance_0", MCC="460", MNC="03", TAC="222222", BINDNWDAFINFOID="info2";
ADD TAIRANGELIST: NFINSTANCENAME="NWDAF_Instance_0", NFTYPE=NfNWDAF, MCC="460", MNC="03", TACRANGEINDEX=2, BINDNWDAFINFOID="info1";
ADD TACRANGE: INDEX=2, RANGESTART="000101", RANGEEND="000200";
ADD TAIRANGELIST: NFINSTANCENAME="NWDAF_Instance_0", NFTYPE=NfNWDAF, MCC="460", MNC="03", TACRANGEINDEX=3, BINDNWDAFINFOID="info2";
ADD TACRANGE: INDEX=3, RANGESTART="000201", RANGEEND="000300";
```

**带宽控制关键参数**: `NWDAFEVENTS`中的`QOS_ANALYSIS`和`QOS_EXP_ANALYSIS`两个事件类型直接关联带宽决策。`QOS_ANALYSIS`支持QoS分析，`QOS_EXP_ANALYSIS`支持体验感知信息分析。

(d) 配置NWDAF服务实例及版本:
```
ADD NFSERVICE: NFINSTANCENAME="NWDAF_Instance_0", SRVINSTANCEID="Service_Instance_0", SERVICENAME=NnwdafEvntSubs;
ADD NFSERVICE: NFINSTANCENAME="NWDAF_Instance_0", SRVINSTANCEID="Service_Instance_1", SERVICENAME=NnwdafDataManagement;
ADD NFSERVICEVER: NFINSTANCENAME="NWDAF_Instance_0", SRVINSTANCEID="Service_Instance_0", APIFULLVERSION="1.R15.0.0";
ADD NFSERVICEVER: NFINSTANCENAME="NWDAF_Instance_0", SRVINSTANCEID="Service_Instance_1", APIFULLVERSION="1.R15.0.0";
```

NWDAF提供两个核心服务: `NnwdafEvntSubs`（事件订阅）和`NnwdafDataManagement`（数据管理），均为API版本1.R15.0.0。

**NWDAF本局数据配置命令清单**:

| 命令 | 作用 | 关键参数 |
|------|------|----------|
| MOD NGMNO | 修改运营商信息 | NOID, FULLNAME, SHORTNAME |
| ADD NGHPLMN | 增加Home PLMN | NOID, MCC, MNC |
| ADD NFUUID | 增加NF实例UUID | NFTYPE=NfNWDAF, NFINSTANCENAME |
| ADD NFPROFILE | 增加NF Profile | NFINSTANCENAME, NFTYPE, NFSTATUS, FQDN |
| ADD NFTAI | 增加TAI信息 | NFINSTANCENAME, MCC, MNC, TAC, BINDNWDAFINFOID |
| ADD TAIRANGELIST | 增加TAI区域 | NFINSTANCENAME, NFTYPE, MCC, MNC, TACRANGEINDEX, BINDNWDAFINFOID |
| ADD TACRANGE | 增加TAC区域 | INDEX, RANGESTART, RANGEEND |
| ADD NWDAFINFO | 增加NWDAF信息 | INSTANCENAME, NWDAFEVENTS |
| ADD NWDAFINFOEXT | 增加NWDAF扩展信息 | INSTANCENAME, ID, NWDAFEVENTS |
| ADD NFSERVICE | 增加NF服务 | NFINSTANCENAME, SRVINSTANCEID, SERVICENAME |
| ADD NFSERVICEVER | 增加服务版本 | NFINSTANCENAME, SRVINSTANCEID, APIFULLVERSION |

#### 2.1.2 配置SBI接口

SBI（Service Based Interface）接口是5GC核心网服务化架构的基础，NWDAF通过SBI接口与SMF、PCF、UPF、NRF等网元通信。

**NWDAF SBI接口矩阵**:

| NF实体类型 | 接口名称 | 对接NF | 是否通过NRF查找 | UDC角色 |
|-----------|----------|--------|----------------|---------|
| NWDAF | Nsmf(NWDAF<->SMF) | SMF | 是 | 既是客户端又是服务端 |
| NWDAF | Nupf(NWDAF<->UPF) | UPF | 否 | 仅作为HTTP服务端，被动建链 |
| NWDAF | Nnrf(NWDAF<->NRF) | NRF | 否 | 需配置与NRF对接数据 |
| NWDAF | N23(PCF<->NWDAF) | PCF | 是 | 作为HTTP服务的服务端 |
| NWDAF | N5(NWDAF<->PCF) | PCF | 是 | 既是客户端又是服务端 |
| NWDAF | Nudn(NWDAF<->UDN) | UDN | 否 | 只支持通过本地NRF通信 |

**协议栈**: 服务化接口统一采用HTTP/2协议（传输层），TLS（安全层，可选），应用层携带不同的服务消息。所有服务化接口在同一总线上传输。

**配置原则**:
- NWDAF服务化接口业务IP地址不能和其他接口业务IP地址共用
- 端口号没有明确时，使用HTTP知名端口号80
- 一个NF类型需配置一个HTTP本端实体组（HTTPLEGRP）和对应的HTTP本端实体（HTTPLE），然后配置对应的SBI端点（SBIAPLE）

**SBI接口配置数据（以IPv4为例）**:

| 配置项 | 命令 | 关键参数 | 取值样例 |
|--------|------|----------|----------|
| 逻辑IP地址 | ADD LOGICIP | LOGICIPV4, VPNINSTNAME | Server: 10.16.0.6 / Client: 10.16.0.7, VPN_SBI |
| HTTP本端实体组 | ADD HTTPLEGRP | INDEX | 1 |
| HTTP本端实体 | ADD HTTPLE | INDEX, HTTPLEGRPIDX, LETYPE, IPTYPE, IPV4, PORT, TLSFLG, VPNNAME | Server INDEX=3 / Client INDEX=4, LETYPE=SERVER/CLIENT, PORT=80, TLSFLG=NO |
| SBI本端实体 | ADD SBIAPLE | INDEX, HTTPLEGRPIDX, NFTYPE | INDEX=1, NFTYPE=NFTypeNWDAF |

**到NRF的配置数据**:

| 配置项 | 命令 | 关键参数 | 说明 |
|--------|------|----------|------|
| NRF实例 | ADD NRF | NRFINSTANCENAME, TLS, PRIORITY | 支持主备NRF，PRIORITY=0高于PRIORITY=1 |
| NRF地址 | ADD NRFADDR | NRFINSTANCENAME, IPADDRESSTYPE, IPV4ADDRESS, PORT | NRF服务端地址 |
| NRF参数 | ADD NRFPARA | NRFINSTANCENAME, WAITINTERVAL, MAXRETRYTIMES, LOADCARRYINHB, SUBSCRISWITCH, OAUTH2SWITCH | 等待5s, 重传3次 |
| 激活注册 | ACT NFONLINE | NFINSTANCENAME | 激活NWDAF向NRF的注册 |

#### 2.1.3 配置本地NRF

本地NRF用于在无全局NRF或需本地配置周边NF时，手工配置UDC与SMF、PCF、UDN等周边NF的逻辑连接。

**关键约束**: NWDAF(UDC)与NWDAF(UDN)的对接必须通过配置本地NRF直连实现，因此`SET NFDISCPLCY`命令的"服务发现策略"不能配置为`REMOTE_ONLY`。

**本地NRF配置步骤**:

**步骤1: 配置到SMF的数据**
```
ADD PNFPROFILE: NFINSTANCEID="a6a61c6f-0d3a-4221-b1da-424eda3ccf58", NFTYPE=NfSMF, NFSTATUS=Registered, IPADDRESSTYPE=IPTypeV4, IPV4ADDRESS1="10.255.255.180", PORT=80;
ADD PNFSERVICE: NFINSTANCEID="a6a61c6f-0d3a-4221-b1da-424eda3ccf58", SRVINSTANCEID="Service_Instance_0", SERVICENAME=NsmfEventExp, SCHEMA=http, NFSERVICESTATUS=REGISTERED;
```

**步骤2: 配置到PCF的数据**
```
ADD PNFPROFILE: NFINSTANCEID="b6a61c6f-0d3a-4221-b1da-424eda3ccf67", NFTYPE=NfPCF, NFSTATUS=Registered, IPADDRESSTYPE=IPTypeV4, IPV4ADDRESS1="10.255.255.181", PORT=80;
ADD PNFSERVICE: NFINSTANCEID="b6a61c6f-0d3a-4221-b1da-424eda3ccf67", SRVINSTANCEID="Service_Instance_0", SERVICENAME=NpcfPlcAuth, SCHEMA=http, NFSERVICESTATUS=REGISTERED;
```

**步骤3: 配置到UDN的数据（主备）**
```
//逻辑主UDN，优先级高于逻辑备
ADD PNFPROFILE: NFINSTANCEID="UDN_instance_0", NFTYPE=NfUDN, NFSTATUS=Registered, IPADDRESSTYPE=IPTypeV4, IPV4ADDRESS1="172.16.0.10", PORT=80, PRIORITY=1;
ADD PNFSERVICE: NFINSTANCEID="UDN_instance_0", SRVINSTANCEID="Service_Instance_0", SERVICENAME=NudnDm, SCHEMA=http, NFSERVICESTATUS=REGISTERED;
//逻辑备UDN
ADD PNFPROFILE: NFINSTANCEID="UDN_instance_1", NFTYPE=NfUDN, NFSTATUS=Registered, IPADDRESSTYPE=IPTypeV4, IPV4ADDRESS1="172.16.0.11", PORT=80, PRIORITY=5;
ADD PNFSERVICE: NFINSTANCEID="UDN_instance_1", SRVINSTANCEID="Service_Instance_0", SERVICENAME=NudnDm, SCHEMA=http, NFSERVICESTATUS=REGISTERED;
```

**主备UDN优先级**: PRIORITY=1的为逻辑主UDN，优先级高于PRIORITY=5的逻辑备UDN。当主UDN故障时，自动切换到备UDN。

### 2.2 UDG侧接口配置（NupfR、Nupf）

#### 2.2.1 配置NupfR接口数据（私有接口）

NupfR接口是UPF与CloudUDN之间的私有数据上报接口，用于体验分析场景的数据采集。

**适用场景**: UPF和CloudUDN对接的使能体验分析场景。重点业务保障场景不需要UDG和CloudUDN对接。

**前提条件**: 必须已完成SSU服务和SBIM服务的安装。

**配置内容: 配置Grp逻辑接口**

NupfR接口通过配置Grp逻辑接口实现，支持IPv4、IPv6和双栈三种模式：

```
//IPv4
ADD LOGICINF: NAME="grpif1/0/0", IPVERSION=IPV4, IPV4ADDRESS1="192.168.1.10", IPV4MASK1="255.255.255.255", VPNINSTANCE="VPN_report";

//IPv6
ADD LOGICINF: NAME="grpif1/0/0", IPVERSION=IPV6, IPV6ADDRESS1="FC00::10:1:20:10", IPV6PREFIXLEN1=128, VPNINSTANCE="VPN_report";

//IPv4和IPv6双栈
ADD LOGICINF: NAME="grpif1/0/0", IPVERSION=IPVER_ALL, IPV4ADDRESS1="192.168.1.10", IPV4MASK1="255.255.255.255", IPV6ADDRESS1="FC00:0:0:0:10:1:20:10", IPV6PREFIXLEN1=128, VPNINSTANCE="VRF_report";
```

**关键参数说明**:

| 参数 | 取值 | 说明 |
|------|------|------|
| NAME | "grpif1/0/0" | 固定取值，不可修改 |
| IPVERSION | IPV4 / IPV6 / IPVER_ALL | 根据网络规划选择 |
| IPV4ADDRESS1 / IPV6ADDRESS1 | 全网规划IP | 逻辑接口地址 |
| VPNINSTANCE | VRF_report | 逻辑接口的VPN必须与对应外联口的VPN相同 |

#### 2.2.2 配置Nupf接口数据（SBI接口）

Nupf接口是UPF与NWDAF之间的服务化接口，用于UPF和NWDAF对接场景。

**适用场景**: UPF和NWDAF对接的场景（包括NWDAF(UDC)和NWDAF(UDN)）。

**前提条件**: 必须已完成SSU服务和SBIM服务的安装。

**配置步骤（5步）**:

**步骤1: 增加Nupf接口IP地址**
```
ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.1.20.1", VPNINSTNAME="VRF_Nupf", DESC="UPF_server";
ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.1.20.2", VPNINSTNAME="VRF_Nupf", DESC="UPF_client";
```

**步骤2: 配置HTTP本端实体组**
```
ADD HTTPLEGRP: INDEX=1, DESC="UPF";
```

**步骤3: 配置HTTP本端实体（Server + Client）**
```
//UPF作为HTTP Server (IPv4)
ADD HTTPLE: INDEX=1, HTTPLEGRPIDX=1, LETYPE=SERVER, PORT=80, TLSFLG=NO, IPTYPE=IPv4, IPV4="10.1.20.1", VPNNAME="VRF_Nupf", DESC="UPF_server";

//UPF作为HTTP Client (IPv4)
ADD HTTPLE: INDEX=2, HTTPLEGRPIDX=1, LETYPE=CLIENT, IPTYPE=IPv4, IPV4="10.1.20.2", VPNNAME="VRF_Nupf", DESC="UPF_client";
```

**步骤4: 配置UPF使用的HTTP本端实体组**
```
ADD SBIAPLE: INDEX=1, HTTPLEGRPIDX=1, NFTYPE=NFTypeUPF, DESCRIPTION="UPF";
```

**步骤5: 设置HTTP属性**
```
SET HTTPCONF: INITLINKINTVL=500, LINKAGINGTIME=120;
```

**Nupf接口与NupfR接口对比**:

| 对比维度 | Nupf接口 | NupfR接口 |
|----------|----------|-----------|
| 接口类型 | SBI服务化接口 | 私有接口 |
| 对接网元 | NWDAF(UDC/UDN) | CloudUDN(UDN) |
| 协议 | HTTP/2 | 私有协议 |
| 配置方式 | LOGICIP + HTTPLEGRP + HTTPLE + SBIAPLE | LOGICINF |
| 保障用户 | Yes | No |
| 重点用户 | No | Yes |
| 普通用户 | Yes(到UDN) | Yes |
| 配置前提 | 安装SSU + SBIM | 安装SSU + SBIM |

### 2.3 UNC侧接口配置

**核心结论**: 典型场景中UNC侧（SMF）无新增接口配置。UNC的接口要求是满足基本组网的SBI、N4等接口。

**异厂商PCF场景的特殊配置**:

当PCF为异厂商时，SMF除了与大网异厂商PCF之间配置N7接口外，还需要配置与智能PCF之间的第二个N7接口。这是体验感知方案在异厂商PCF环境下的必要补充。

**UNC侧特殊软参配置**:

全省2C SMF需要开启软参，控制I-SMF给锚点SMF的HSMFUpdate消息中携带amfNfId:

```
SET SMFSOFTPARAOFBIT: DT=Dw, DWORDNUM=1038, VALUE=VALUE_1, POSITION=25;
```

此配置确保I-SMF场景下锚点SMF能获取AMF的NF ID信息，支撑体验感知策略的正确执行。

**UNC侧License依赖**:

| 特性 | License控制项 | 说明 |
|------|--------------|------|
| WSFD-107010 UPF选择 | LKV2USBL01 UPF选择 | 基于预定义规则选择支持重点业务保障的UPF |
| WSFD-109101 PCC基本功能 | LKV3W9SPCC11 PCC基本功能 | 进行规则判定及对UPF进行策略下发 |
| WSFD-211002 基于实时位置的策略控制 | LKV2PYCTRL1 基于实时位置信息的策略控制功能-USM | 触发重点业务保障签约用户实时位置上报 |

### 2.4 UPCF与NWDAF对接

#### 2.4.1 UPCF N23接口配置全流程

UPCF（智能PCF）与NWDAF的N23接口是体验感知策略闭环的关键链路。UPCF通过N23接口向NWDAF下发订阅用户体验分析数据请求，获取分析结果后生成策略。

**UPCF发现NWDAF服务的两种方式**:

| 方式 | 适用场景 | 关键命令 | 说明 |
|------|----------|----------|------|
| 动态发现（通过NRF） | 网络中部署了NRF | SET NFDISCCFG + ADD DISCCONDCFG | UPCF向NRF发送服务发现请求 |
| 静态发现（直接配置） | 无NRF或需指定NWDAF | ADD DISCNFPROFILE | 手工配置NWDAF实例信息 |

**N23接口配置核心步骤**:

**步骤1: 增加HLB设备地址（UPCF与NWDAF对接的本端IP）**
```
ADD HLBDEVADDR: DEVAID=5, VPNNAME="VPN_SBI", IPVER=IPV4, IP="10.100.100.156", HTTPSFUNC=OFF;
```
约束: DEVAID值需大于`LST HLBDEVADDR`中查询的所有值。

**步骤2: 开启会话备份功能**
```
MOD INSP: INSPN=VRM_SESSIONBACKUPSWITCH, INSPV=3;
```

**步骤3: 开启N23接口功能及会话备份**
```
MOD INSP: INSPN=VRM_N23SWITCH, INSPV=1;
MOD INSP: INSPN=VRM_N23SESSIONBACKUP, INSPV=1;
```

**步骤4: 开启设备间N23会话审计**
```
SET SBIDEVAUDIT: SBITYPE=N23, PERIODICDATIME=30;
```
约束: 审计时长(30分钟)应小于NWDAF的N23会话老化时长。

**步骤5: 开启用户定时器持久化和N23信令EDR**
```
MOD INSP: INSPN=VRM_SYNTIMER, INSPV=1;
SET EDRREPORT: ID=1, SWITCH=N23SignalingEDR-1;
```

**步骤6（可选）: 配置NWDAF服务发现**

方式A - 通过TAI和EVENT发现:
```
ADD DISCCONDCFG: NFTYPE=NWDAF, NWDAFPARASW=TAI-1&EVENT-1;
SET NFDISCCFG: SERVICETYPE=PES-NCS, NRFDISCSW=NWDAFDISC-1;
```

方式B - 通过NWDAF网元类型发现:
```
SET DISCNFTYPECFG: NFTYPE=NWDAF, SWITCH=ON;
SET NFDISCCFG: SERVICETYPE=PES-NCS, NRFDISCSW=NWDAFDISC-1;
```

方式C - 静态发现（配置DISCNFPROFILE后禁止向NRF发现）:
```
ADD DISCNFPROFILE: NFINSNAME="pcf_nwdaf", NFINSID="4947a69a-...", NFTYPE=NWDAF, NFPROFILE="{...}";
SET NFDISCCFG: SERVICETYPE=PES-NCS, NRFDISCSW=NWDAFDISC-0;
```

**步骤7（可选）: 开启N23头域填充subsPcfId**
```
MOD INSP: INSPN=VRM_N23HDPCFIDMODE, INSPV=1;
```

#### 2.4.2 UPCF N5接口配置（重点业务保障QoS加速）

体验感知场景下无需配置N5接口会话备份。仅当配置重点业务保障的QoS加速策略时才需要:
```
MOD INSP: INSPN=VRM_N5SESSIONBACKUP, INSPV=1;
```

UPCF向NRF注册N5接口服务名（重点业务保障QoS加速场景）:
```
ADD NFSERVICE: GRPNAME="SERVICE-PCF", SERVICEID="npcf-policyauthorization-1", SERVICEINSTID="6666a69a-...", SERVICENAME=npcf-policyauthorization, NFSRVVERGRP="SERVICE-PCF", SCHEME=http, STATUS=REGISTERED, NFCOMINFOID="COMINFO-1";
```

#### 2.4.3 UPCF NFPROFILE参数与NWDAF网元命令映射

当对接的NWDAF为华为提供时，UPCF的`ADD DISCNFPROFILE`命令中的NFPROFILE参数可通过以下映射关系从NWDAF侧查询获取:

| NFPROFILE参数 | NWDAF侧查询命令 | 查询参数 |
|---------------|-----------------|----------|
| nfInstanceId | LST NFUUID | NF实例标识 |
| nfType | LST NFUUID | NF类型（固定NWDAF） |
| ipv4Addresses / ipv6Addresses | LST HTTPLE | IPv4/IPv6地址（服务端） |
| serviceInstanceId | LST NFSERVICE | 服务实例标识 |
| serviceName | 固定值 | nnwdaf-eventssubscription |
| apiFullVersion | LST NFSERVICEVER | API版本信息 |
| port | LST HTTPLE | 端口号 |
| nwdafEvents | LST NWDAFINFO | NWDAF数据分析事件 |
| taiList (mcc/mnc/tac) | LST NFTAI | 移动国家码/网号/跟踪区域码 |
| tacRangeList | LST TACRANGE | TAC区域起点/结束值 |

**事件类型转换**: NWDAF侧查询的中文值需转换为NFPROFILE中的英文值:
- "QOS分析" -> "QOS_ANALYSIS"
- "体验感知信息分析" -> "QOS_EXP_ANALYSIS"

### 2.5 License申请

体验感知解决方案涉及的License控制项跨多个产品和网元，共21项，全部为必选项:

#### 2.5.1 UPCF侧License

| 特性 | License控制项 | 说明 |
|------|--------------|------|
| WHFD-611123 N23接口（使用HTTP协议）策略控制 | LRM0PCFN23107 N23接口（使用HTTP协议）策略控制 | 必须加载，依赖该特性的功能 |

#### 2.5.2 UDC(NWDAF)侧License

| 特性 | License控制项 | 说明 |
|------|--------------|------|
| DCFD-010301 QoS分析事件订阅管理 | LKV8SPDUSN01 重点业务订阅会话数 | 重点业务保障体验感知场景依赖 |
| DCFD-010401 体验分析事件订阅管理 | LKV8EAESUDC01 体验分析订阅会话数 | 控制体验分析订阅会话数 |
| DCFD-010302 重点业务保障管理 | LKV8GPDUSN01 5G保障会话数 | 重点业务保障体验感知场景依赖 |
| DCFD-010171 支持端到端跟踪 | LKV8ESTUDC01 端到端用户跟踪 | 端到端跟踪功能依赖 |
| DCFD-010202 磁盘故障隔离 | LKV6DIFAUDC01 磁盘故障隔离 | 磁盘故障隔离功能依赖 |
| DCFD-010303 体验信息能力开放 | LKV8EIEEUDC01 体验信息能力开放 | 向UDN上报体验数据依赖 |

#### 2.5.3 UNC(SMF)侧License

| 特性 | License控制项 | 说明 |
|------|--------------|------|
| WSFD-107010 UPF选择 | LKV2USBL01 UPF选择 | 基于预定义规则选择支持重点业务保障的UPF |
| WSFD-109101 PCC基本功能 | LKV3W9SPCC11 PCC基本功能 | 进行规则判定及对UPF策略下发 |
| WSFD-211002 基于实时位置的策略控制 | LKV2PYCTRL1 基于实时位置信息的策略控制功能-USM | 触发重点业务保障签约用户实时位置上报 |

#### 2.5.4 UDG(UPF)侧License

| 特性 | License控制项 | 说明 |
|------|--------------|------|
| GWFD-111286 重点用户质差监测和保障 | LKV3G5ANAR01 重点用户质差监测和保障 | 质差判断及上报功能 |
| GWFD-111284 体验信息采集 | LKV3G5EXPR01 体验信息采集 | 体验信息采集功能 |
| GWFD-111283 智能板订阅和采集 | LKV3G5IBIC01 智能板订阅和采集 | 智能板基础功能 |
| GWFD-111304 TCP/UDP传输分析上报 | LKV3G5TDIR01 TCP/UDP传输分析上报 | TCP/UDP传输分析功能 |
| GWFD-111301 智能分析记录生成 | LKV3G5IARG01 智能分析记录生成 | 智能分析记录功能 |
| GWFD-111302 业务全样分析上报 | LKV3G5FSFR01 业务全样分析上报 | 业务全样分析功能 |
| GWFD-111311 业务分析上报订阅 | LKV3G5SARS01 业务分析上报订阅 | 业务分析上报订阅功能 |
| GWFD-111305 用户实时位置分析上报 | LKV3G5RSLR01 用户实时位置分析上报 | 用户实时位置分析上报功能 |

#### 2.5.5 CloudUDN侧License

| 控制项名称 | 说明 |
|-----------|------|
| LKVVIPNBI01 VVIP用户体验数据开放增值包 | 保障用户体验数据开放时需打开 |
| LKVEXPNBI02 用户体验数据开放增值包 | 重点用户和普通用户体验数据开放时需打开 |

---

## 3. 配置与调测要点

### 3.1 接口对接配置顺序

体验感知方案接口配置应按以下顺序执行:

1. **申请License** -> 所有网元的License必须先加载完成
2. **UPCF侧配置** -> PCF通过N23接口订阅NWDAF分析数据
3. **UDC侧配置** -> NWDAF本局数据 + SBI接口 + 本地NRF
4. **UDG侧配置** -> UPF侧Nupf SBI接口 + NupfR私有接口（前提: SSU + SBIM已安装）
5. **UNC侧配置** -> 典型场景无新增；异厂商PCF场景配置第二个N7接口
6. **CloudUDN侧配置** -> UDN与UDC/UPF对接接口

### 3.2 UDG侧Nupf接口验证方法

**验证步骤1**: 执行NGPING检查逻辑接口IP互通
```
NGPING: IPTYPE=IPv4, VPNNAME="VRF_Nupf", SRCIPV4ADDR="10.1.20.1", DSTIPV4ADDR="NWDAF的Nupf接口IP";
```

**验证步骤2**: 执行PING检查外联口IP互通
```
PING: IPVERSION=IPv4, VPNNAME="VRF_Nupf", SOURCEIPV4ADDRESS="UPF Nupf对应的外联口IP", DESTIPV4ADDRESS="NWDAF Nupf逻辑接口对应的外联口IP";
```

**验证步骤3**: 检查直连路由器路由是否存在
- 如果NGPING不通但PING通，检查直连路由器是否存在到UPF(Nupf接口IP)的路由，下一跳是外联口IP
- 如果路由不存在，联系路由器工程师增加路由

### 3.3 UPCF侧N23接口验证方法

**验证步骤1**: N23接口调测
```
NGPING: IPTYPE=IPv4, VPNNAME="VPN_SBI", SRCIPV4ADDR="UPCF的N23接口IP", DSTIPV4ADDR="NWDAF的Nnwdaf接口IP";
```

**验证步骤2**: N5接口调测（如需）
```
NGPING: IPTYPE=IPv4, VPNNAME="VPN_SBI", SRCIPV4ADDR="UPCF的N5接口IP", DSTIPV4ADDR="NWDAF的Npcf接口IP";
```

### 3.4 配置约束汇总

| 约束项 | 约束内容 | 影响范围 |
|--------|----------|----------|
| SSU + SBIM服务 | UDG侧配置前必须已完成安装 | Nupf接口、NupfR接口 |
| 业务IP地址隔离 | NWDAF SBI接口业务IP不能与其他接口共用 | UDC侧SBI接口 |
| VPN一致性 | 逻辑接口VPN必须与对应外联口VPN相同 | 所有逻辑接口配置 |
| 端口号 | 无明确指定时使用HTTP知名端口80 | SBI接口 |
| 服务发现策略 | NWDAF(UDC)与NWDAF(UDN)对接时不能设为REMOTE_ONLY | UDC本地NRF |
| 审计时长 | UPCF N23审计时长应小于NWDAF的N23会话老化时长 | UPCF侧N23 |
| DEVAID | UPCF HLB设备地址标识需大于LST HLBDEVADDR中已有值 | UPCF侧 |
| 智能UPF双域 | 同时签约双域分流和重点业务保障时需至少一对支持双域的UPF | 部署总览 |

---

## 4. 与带宽控制的关系

### 4.1 体验感知在带宽控制闭环中的角色

体验感知方案是带宽控制策略的"感知层"，为带宽决策提供实时数据输入:

```
UPF(采集体验数据) -> NWDAF(分析体验数据) -> PCF(生成带宽策略) -> SMF(转发策略) -> UPF(执行带宽策略)
```

**具体链路分析**:

| 链路段 | 接口 | 产品 | 带宽控制贡献 |
|--------|------|------|-------------|
| 数据采集 | Nupf SBI / NupfR私有 | UDG -> UDC/UDN | UPF采集用户业务体验数据（QoS指标、传输分析、业务全样分析等） |
| 数据分析 | 内部 | UDC(NWDAF) | NWDAF分析QoS和体验感知数据，生成分析结果 |
| 策略下发 | N23 SBI | UDC -> UPCF | NWDAF向PCF推送QoS分析结果，PCF据此调整策略 |
| 策略执行 | N7 SBI + N4 | UPCF -> SMF -> UPF | PCF生成的新策略通过SMF下发给UPF执行 |
| 效果验证 | Nupf SBI | UDG -> UDC | UPF采集调整后的体验数据，形成闭环 |

### 4.2 关键License与带宽控制的映射

| License | 带宽控制关联 |
|---------|-------------|
| GWFD-111284 体验信息采集 | 采集带宽使用情况的基础数据 |
| GWFD-111304 TCP/UDP传输分析上报 | 分析传输层带宽利用率 |
| GWFD-111302 业务全样分析上报 | 全量业务带宽使用画像 |
| GWFD-111305 用户实时位置分析上报 | 结合位置信息触发区域带宽策略 |
| GWFD-111286 重点用户质差监测和保障 | 质差检测触发带宽保障策略 |
| DCFD-010301 QoS分析事件订阅管理 | QoS分析直接驱动带宽QoS调整 |
| DCFD-010302 重点业务保障管理 | 5G保障会话数控制带宽保障覆盖范围 |

### 4.3 体验感知事件类型与带宽决策

NWDAF支持的两个核心分析事件直接关联带宽控制:

| 事件类型 | 英文标识 | 分析内容 | 带宽决策影响 |
|----------|----------|----------|-------------|
| QoS分析 | QOS_ANALYSIS | 用户会话QoS参数偏离度分析 | 触发GBR/MBR参数调整、QCI/5QI重映射 |
| 体验感知信息分析 | QOS_EXP_ANALYSIS | 用户体验质量综合分析 | 触发端到端带宽保障、业务优先级调整 |

### 4.4 NupfR与带宽控制数据上报

NupfR私有接口是重点用户和普通用户体验数据的主要上报通道。通过Grp逻辑接口上报的数据包括:
- TCP/UDP传输分析数据（反映带宽利用率）
- 业务全样分析数据（反映各业务带宽消耗）
- 智能分析记录（综合体验评估）
- 用户实时位置数据（支撑位置化带宽策略）

这些数据上报到CloudUDN后，经过汇聚分析，可反馈给NWDAF(UDC)进一步驱动PCF策略调整，形成完整的带宽控制闭环。

---

## 5. 关键概念术语

| 术语 | 全称/含义 | 说明 |
|------|-----------|------|
| NWDAF | Network Data Analytics Function | 网络数据分析功能，5GC中负责数据采集和分析的网元 |
| UDC | Unified Data Center（华为产品） | 华为实现NWDAF(UDC)的产品，承担网络数据分析中心角色 |
| UDN | Unified Data Node（华为产品） | 华为实现NWDAF(UDN)的产品，承担体验数据汇聚和北向上报角色 |
| UPCF | Unified PCF（华为智能PCF产品） | 华为实现的策略控制功能，支持N23接口与NWDAF交互 |
| SBI | Service Based Interface | 服务化接口，5GC架构中基于HTTP/2的服务间通信接口 |
| NRF | Network Repository Function | 网络存储库功能，提供服务注册和发现 |
| Nupf | Nupf接口 | UPF与NWDAF之间的服务化接口 |
| NupfR | NupfR接口 | UPF与CloudUDN之间的私有数据上报接口 |
| N23 | N23接口 | PCF与NWDAF之间的服务化接口，用于策略分析数据交互 |
| N5 | N5接口 | PCF与AF/NWDAF之间的策略授权接口 |
| N4 | N4接口 | SMF与UPF之间的接口，用于会话管理和策略下发 |
| N7 | N7接口 | SMF与PCF之间的策略控制接口 |
| SSU | （UDG可选服务） | UDG侧服务化接口的前置依赖服务 |
| SBIM | （UDG可选服务） | UDG侧SBI管理的服务 |
| QOS_ANALYSIS | QoS分析事件 | NWDAF支持的QoS质量分析事件类型 |
| QOS_EXP_ANALYSIS | 体验感知信息分析事件 | NWDAF支持的体验感知信息分析事件类型 |
| TAI | Tracking Area Identity | 跟踪区域标识，由MCC+MNC+TAC组成 |
| LocalNRF | 本地NRF | 不依赖全局NRF，手工配置周边NF的逻辑连接方式 |
| HLB | （华为内部通信组件） | UPCF侧用于与NWDAF对接的高性能负载均衡组件 |
| EDR | Event Data Record | 事件数据记录，用于信令跟踪和故障定位 |
| FQDN | Fully Qualified Domain Name | 完全限定域名 |

---

## 6. 知识来源

| 序号 | 文件名 | 原始路径 | 核心内容 |
|------|--------|----------|----------|
| 1 | 部署总览_90530630.md | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/ | 网元部署要求、建设方案、配置任务总表 |
| 2 | 接口配置总览_90530634.md | .../接口对接配置/ | 全链路接口矩阵、三类用户(保障/重点/普通)的接口需求 |
| 3 | 配置NWDAF本局数据_90690578.md | .../接口对接配置/UDC侧配置/ | NWDAF实例信息、TAI/TAI区域、分析事件、服务实例配置 |
| 4 | 配置SBI接口_90530642.md | .../接口对接配置/UDC侧配置/ | SBI接口矩阵、协议栈、NRF对接数据、HTTP实体配置 |
| 5 | 配置本地NRF_34250357.md | .../接口对接配置/UDC侧配置/ | 本地NRF配置、SMF/PCF/UDN对接、主备UDN优先级 |
| 6 | 配置NupfR接口数据_15641438.md | .../接口对接配置/UDG侧配置/ | UPF与CloudUDN私有接口、Grp逻辑接口配置 |
| 7 | 配置Nupf接口数据_90690586.md | .../接口对接配置/UDG侧配置/ | UPF与NWDAF SBI接口、HTTP实体组、验证方法 |
| 8 | UNC侧配置_21814228.md | .../接口对接配置/ | SMF侧无新增（典型场景）、异厂商PCF的第二个N7、I-SMF软参 |
| 9 | 配置UPCF与NWDAF的对接数据_88928805.md | .../接口对接配置/UPCF侧配置/ | N23接口全流程、动态/静态发现、NFPROFILE映射、验证方法 |
| 10 | 申请License_34250345.md | .../业务部署与调测/ | 21项License控制项（UPCF/UDC/UNC/UDG/CloudUDN全覆盖） |

---

## 附录: 配置命令速查表

### UDC侧命令

| 命令 | 用途 |
|------|------|
| MOD NGMNO | 修改运营商信息 |
| ADD NGHPLMN | 增加Home PLMN |
| ADD NFUUID | 增加NF实例UUID |
| ADD NFPROFILE | 增加NF Profile |
| ADD NFTAI | 增加TAI信息 |
| ADD TAIRANGELIST | 增加TAI区域 |
| ADD TACRANGE | 增加TAC区域 |
| ADD NWDAFINFO | 增加NWDAF信息 |
| ADD NWDAFINFOEXT | 增加NWDAF扩展信息 |
| ADD NFSERVICE | 增加NF服务 |
| ADD NFSERVICEVER | 增加服务版本 |
| ADD LOGICIP | 增加逻辑IP |
| ADD HTTPLEGRP | 增加HTTP本端实体组 |
| ADD HTTPLE | 增加HTTP本端实体 |
| ADD SBIAPLE | 增加SBI本端实体 |
| ADD NRF | 增加NRF实例 |
| ADD NRFADDR | 增加NRF地址 |
| ADD NRFPARA | 增加NRF参数 |
| ACT NFONLINE | 激活NF上线 |
| ADD PNFPROFILE | 增加对端NF Profile |
| ADD PNFSERVICE | 增加对端NF服务 |

### UDG侧命令

| 命令 | 用途 |
|------|------|
| ADD LOGICINF | 增加逻辑接口（NupfR用） |
| ADD LOGICIP | 增加逻辑IP（Nupf用） |
| ADD HTTPLEGRP | 增加HTTP本端实体组 |
| ADD HTTPLE | 增加HTTP本端实体 |
| ADD SBIAPLE | 增加SBI本端实体 |
| SET HTTPCONF | 设置HTTP属性 |
| NGPING | 网络连通性检测 |
| PING | IP连通性检测 |

### UPCF侧命令

| 命令 | 用途 |
|------|------|
| ADD HLBDEVADDR | 增加HLB设备地址 |
| MOD INSP | 修改内部软参 |
| SET SBIDEVAUDIT | 设置SBI会话审计 |
| SET EDRREPORT | 设置EDR上报 |
| ADD DISCCONDCFG | 增加发现条件配置 |
| SET DISCNFTYPECFG | 设置发现NF类型配置 |
| SET NFDISCCFG | 设置NF发现配置 |
| ADD DISCNFPROFILE | 增加发现NF Profile |
| ADD NFSERVICE | 增加NF服务 |
| MOD NFCOMINFO | 修改NF公共信息 |
| LST NFCOMINFO | 查询NF公共信息 |

### UNC侧命令

| 命令 | 用途 |
|------|------|
| SET SMFSOFTPARAOFBIT | 设置SMF软参位 |
