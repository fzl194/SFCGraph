# Batch-03: 体验感知 - 重点用户UPCF与接口对接

> **来源**: UDG 5G Core 体验感知解决方案 - 重点用户UPCF配置 + 接口对接(CloudUDN/UDC)
> **文件数**: 10 md
> **带宽控制聚焦**: QoE采集→NWDAF分析→PCF决策→带宽策略调整

---

## 1. 文档概述

本批次覆盖 5G Core 体验感知解决方案中三个核心层面的配置与调测：

| 层面 | 文档 | 职责 |
|------|------|------|
| UPCF侧配置 | 典型场景N23订阅策略、异厂商PCF场景N23订阅策略 | UPCF作为数据分析使用者，向NWDAF发起体验分析订阅，驱动策略计算和下发 |
| 重点用户体验感知调测 | 调测重点用户体验感知功能 | 端到端验证QoE数据采集链路（PCF→NWDAF→SMF→UPF→EMS-UFDR→BOSS/SFTP） |
| CloudUDN接口对接 | 主备CloudUDN对接、配置入口、NupfR接入、服务化接口 | CloudUDN作为数据底座，收集UPF上报的UFDR数据，提供主备容灾能力 |
| UDC侧NWDAF配置 | NWDAF典型配置实例、配置流程、调测 | NWDAF作为分析引擎，接收PCF订阅请求，向SMF转发订阅，汇聚体验数据 |

**体验感知与带宽控制的关联**: 体验感知是带宽策略动态调整的数据来源。UPCF通过N23接口向NWDAF订阅QoE体验分析（事件类型 `QOS_EXP_ANALYSIS`），NWDAF分析后返回结果，UPCF基于分析结果计算策略并下发至SMF，SMF再向UPF下发策略变更（含QoS参数、带宽限速规则等），实现"感知→分析→决策→执行"的闭环带宽控制。

---

## 2. 核心知识点

### 2.1 UPCF N23订阅策略

#### 2.1.1 典型场景（我司PCF）

**核心机制**: UPCF作为数据分析使用者，向NWDAF发起体验分析数据订阅请求。NWDAF返回体验分析数据订阅响应后，UPCF基于智能UPF选择成功的结果，通过N23接口向NWDAF下发体验分析数据订阅，并根据响应中的应用标识 `live` 进行策略计算，然后向SMF下发指定的策略。

**前提条件**:
- 已完成UPCF与NRF、NWDAF的对接数据配置
- 已完成加载License
- 已登录UPCF WebUI界面

**策略触发器**:
- `RAT_TY_CH`：接入网络类型变化（RAT Type Change）
- `IPCAN_EST`：IP-CAN会话建立（IPCAN Establishment）

**三条核心规则**:

| 规则 | 条件 | 5G动作 | 触发时机 |
|------|------|--------|----------|
| N23_EXP_Rule01 | 用户签约ID不为空（恒真条件） | UpfSelectRule（upfSelectId=select_ai_upf, reportInd=True） | 匹配smfID且接入网络类型变化时，触发智能UPF选择 |
| N23_EXP_Rule02 | 智能UPF选择成功 + 指定smfID + NR接入 + 指定TAC | CmdN23EventSubscription（event=QOS_EXP_ANALYSIS, appIds=live, status=NORMAL） | 5G网络接入时，发起N23事件订阅 |
| N23_EXP_Rule03 | 智能UPF选择成功 + 指定smfID + EUTRA/GERA接入 + 指定TAC | CmdN23EventSubscription（event=QOS_EXP_ANALYSIS, appIds=live, status=SUSPEND） | 4G/2G网络接入时，暂停N23事件订阅 |

**关键条件组详解**:

1. **条件组1（SubscriberStatus_CG01）**: `Subscriber.SubscriberIdentifier != System.Null`，判断用户签约ID不为空，是恒真条件，用于保障重点用户场景。

2. **条件组2（N23_CG01）**: 包含两个AND条件：
   - `SmfSession.upfActive = select_ai_upf`：智能UPF选择成功
   - `SmfSession.SmfId = 5ec7a286-47e4-2032-fc0f-100909000008`：指定SMF实例

3. **条件组3（SmfSessionRatType_CG01）**: `SmfSession.RatType = NR`，5G NR接入。

4. **条件组4（SmfSessionRatType_CG02）**: `SmfSession.RatType = EUTRA OR GERA`，4G/2G接入（OR关系）。

5. **条件组5（SmfSessionTac_CG01）**: TAC匹配，支持4G TAC（`initEutraTac=4305`）或5G TAC（`initNRTac=63F84B`），OR关系。

**UpfSelectRule动作详解**:
- `upfSelectId=select_ai_upf`：触发智能UPF选择逻辑，选择AI型UPF
- `reportInd=True`：上报指示器，表示需要反馈选择结果

**CmdN23EventSubscription动作约束**:
- 只允许在5G Smf Pcc Rule和Non-PCC规则下关联
- 同一个规则下只能关联一个CmdN23EventSubscription动作
- 一个CmdN23EventSubscription动作仅支持配置一个event事件
- 系统所有CmdN23EventSubscription动作中QOS_ANALYSIS事件关联的appIds最大个数为40
- 系统所有CmdN23EventSubscription动作配置的appIds总共不能超过255个
- `status=NORMAL`：正常订阅；`status=SUSPEND`：暂停订阅

**业务发放**:
- `ADD PSUB`：增加用户，需指定USRIDENTIFIER（受软参 `VRM_SUBSRCIPTIONIDTYPE` 控制类型，默认IMSI）
- `ADD PSRV`：给用户签约业务，指定SRVNAME和SRVUSAGESTATE
- 业务类型为 `VALUE_ADDED_SERVICE`，激活方式为 `PCEF`，QoS模式为"替换"

#### 2.1.2 异厂商PCF场景

**适用场景**: 我司SMF同时对接异厂家PCF和智能PCF时，智能PCF（UPCF）侧进行数据分析订阅。

**与典型场景的核心差异**:

| 维度 | 典型场景 | 异厂商PCF场景 |
|------|----------|---------------|
| 条件判断 | SmfSession.upfActive + SmfSession.SmfId + RatType + TAC | `SmfSession.NeedN23Subs = QOS_ANALYSIS` |
| 事件类型 | QOS_EXP_ANALYSIS | QOS_ANALYSIS |
| 规则类型 | 5G Smf Pcc Rule | Non-PCC |
| 签约要求 | 否（SUBSCRIPTIONFORCED=No） | 是（SUBSCRIPTIONFORCED=Yes） |
| appIds | live | appgroup1 |
| 触发器 | RAT_TY_CH + IPCAN_EST | IPCAN_EST |

**异厂商场景简化逻辑**: 异厂商PCF场景下，条件判断简化为单个条件 `SmfSession.NeedN23Subs = QOS_ANALYSIS`，由SMF决定是否需要N23订阅。这降低了UPCF侧的条件配置复杂度，将决策权部分转移给SMF。

### 2.2 CloudUDN接口对接

#### 2.2.1 配置入口与模式

**CloudUDN采用流水线式配置**，特性必选配置和特性专属可选配置汇聚在特性配置界面，公共配置汇聚在可选配置界面。

- 登录OM Portal → "应用配置 > 业务配置" 进入配置界面
- 配置界面以业务特性或业务app名称命名
- 微服务粒度的配置呈现：同一微服务的多个配置项（对应不同业务功能）都会呈现，但只需配置特性支持的配置项
- **数据底座模式**: 需在"基础配置"中开启"是否开启数据底座模式"为"开启"

#### 2.2.2 主备CloudUDN对接

**主备容灾架构**: 两套CloudUDN互为主备，通过双协商通道实现配置同步和故障倒换。

**第一协商通道（Local-Center配置）**:
- 配置对端IP地址（IPv4/IPv6）
- 配置对端登录用户名和密码（账号需通过CSP管理页面新增，用户名建议 `actstdbyact`，密码有效期999天）
- 对端账号需分配角色权限：双机主备维护、信息采集项查询、服务监控、业务配置

**第二协商通道（主备配置页面）**:

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| 主备模式开关 | 打开 | 开启主备容灾 |
| 设备倒换指令 | 手动倒换/强制倒换 | 强制倒换不考虑对端状态；非强制倒换根据告警数、链路数、配置一致性等判断 |
| 对端设备第二协商通道地址 | 两个PGSQL IP | 对端PGSQL业务数据库的两个IP地址 |
| 逻辑主备关系 | 逻辑主/逻辑备 | 主CloudUDN配"逻辑主"，备配"逻辑备" |
| 运行主备关系倒换开关 | 打开 | 允许运行主备关系倒换 |
| 自动倒回开关 | 打开 | 逻辑主恢复后自动倒回 |
| 每日倒换次数 | 3 | 每日最大倒换次数 |
| 倒换间隔时间（分钟） | 10 | 每次倒换最小间隔 |
| 接入节点故障判断阈值 | 2 | 接入节点故障数≥该值时触发倒换 |
| 计算节点故障判断阈值 | 2 | 计算节点故障数≥该值时触发倒换 |
| 存储节点故障判断阈值 | 2 | 存储节点故障数≥该值时触发倒换 |
| NATLOG链路故障阈值 | 2 | 主备NATLOG链路差值≥该值时触发倒换 |
| UFDR链路故障阈值 | 2 | 主备UFDR链路差值≥该值时触发倒换 |
| 主备信息同步间隔（秒） | 5 | 节点信息同步间隔 |
| 协商通道消息重传次数 | 3 | 超过该次数认为通道故障 |
| 基于SBI的倒换判断条件 | 可用NWDAF(UDC)数 | SBI接口状态检查项 |
| 可用NWDAF(UDC)数判定时长（分钟） | 5 | NWDAF与UDN SBI通信异常判定时长 |

**版本约束**: 不支持静默部署的 V100R025C10SPC100 版本与由低版本升级至该版本的CloudUDN进行主备对接。

**主备验证方法**:
1. PING验证：CspServgate服务 → 对端导航页IP
2. TRACE验证：CspServgate服务 → 对端IP（网络不通时）
3. PGSQL验证：PSIBusinessPGSQL服务 → 对端第二协商通道IP
4. 告警检查：确认无 ALM-86128（数据库同步失败）、ALM-86127（容灾通道连接失败）、ALM-86132（主备配置不一致）

#### 2.2.3 接入用户体验数据（NupfR）

**功能定位**: 配置CloudUDN接入UPF上报的体验感知数据（UFDR UDP数据流），是QoE数据采集链路的接入端。

**配置路径**: OM Portal → "应用配置 > 业务配置 > 用户流量信息数据开放 > UFDR数据北向"

**SingleIP开关**: 默认关闭。SingleIP功能影响UFDR数据接入的IP配置方式。

**IP配置**:
- 接口IP地址：从PBU_I-C/PBU_I-C_ARM虚拟机vNIC2获取，数量取决于 `ufdrudpcollector` POD个数
- 业务端口号：15000（需参考通信矩阵）
- 服务实例名称：CloudUDN自动生成（如 `ufdrudpcollector-a45aa132-5479546d97`）

**路由配置**:
- 对端IP地址：UPF侧协商提供，建议配置大段路由（不超过3个）
- 网关地址：从PBU_I-C/PBU_I-C_ARM虚拟机vNIC2获取

**数据验证**:
1. PING验证：UfdrUdpCollector服务 → 对端（UPF）服务器IP
2. TRACE验证：网络不通时执行
3. 性能指标检查：U2020/MAE网管查看"1915166030 接收的UFDR数据包数量"是否为0（不应为0）

#### 2.2.4 服务化接口配置

**CloudUDN支持的服务化接口**:

| 接口 | 方向 | 角色 |
|------|------|------|
| Nudn | UDN ↔ UDC | UDN做Server |
| Nupf | UDN ↔ UPF | UDN做Client |

**配置步骤**:

1. **开启数据底座模式**: OM Portal → "应用配置 > 业务配置 > 基础配置 > CloudUDN模式配置"

2. **配置NFUUID**:
   ```
   ADD UDNNFUUID: NFTYPE=NfUDN, NFINSTANCENAME="UDN_Instance_0", NFINSTANCEID="654C307D-4CD6-2035-941E-03030000006F";
   ```

3. **配置逻辑IP**: 需配置Server端和Client端各一组IP（IPv4/IPv6），VPN实例需与外联口VPN一致（如 `VPN_SBI`）

4. **配置HTTP本端实体组**:
   ```
   ADD HTTPLEGRP: INDEX=1, DESC="UDN";
   ```

5. **配置HTTP本端实体**:
   - Server实体：LETYPE=SERVER，PORT=80
   - Client实体：LETYPE=CLIENT
   - TLS：建议启用TLS确保数据传输安全（需全网统一规划）

6. **配置服务化接口接入点**:
   ```
   ADD SBIAPLE: INDEX=1, HTTPLEGRPIDX=1, NFTYPE=NFTypeUDN, DESCRIPTION="UDN";
   ```

**验证方法**:
1. `NGPING`：UDN与UDC之间逻辑接口IP互通检查
2. `PING`：外联口IP互通检查
3. 路由检查：确认直连路由器存在到UDN的路由

### 2.3 NWDAF配置（UDC侧）

#### 2.3.1 NWDAF配置流程

NWDAF配置分为四个阶段：

| 步骤 | 内容 | 参考文档 |
|------|------|----------|
| 本局数据配置 | 运营商信息、NWDAF实例、TAI区域 | 配置NWDAF本局数据 |
| 接口配置 | SBI接口、HTTP实体、NF Profile | 配置SBI接口 |
| 本地NRF配置 | NRF实例、地址、协议参数 | 配置本地NRF |
| 业务配置 | NWDAF到UDN对接数据 | 业务部署与调测 |

#### 2.3.2 NWDAF典型配置实例

**组网场景**:
- 网络形态：5G网络
- 路由协议：OSPF动态路由 + BFD快速检测
- 组网IP格式：IPv4
- 对接NF：PCF、SMF、UDN

**配置步骤详解**:

**步骤1: 关闭自动配置开关**
```
LST AUTOCONFIG:;
DSP OPSASSISTSTATE:;
SET AUTOCONFIG: SWITCHFLAG=FALSE;
```
- 关闭前需确认自动部署维护助手 `autoscaling_autoconfig.py` 状态为"Ready"

**步骤2: 全局激活BFD**
```
SET BFD: BFDENABLE=TRUE;
```
- BFD用于OSPF路由快速收敛，保障服务化接口的高可用

**步骤3: 配置IP路由数据**
- 配置VPN实例 `VPN_SBI`
- 配置OSPF进程（PROCID=6），绑定BFD（BFDALLINTFFLG=TRUE）
- 配置OSPF区域（AREAID=10.0.0.5）
- 配置引入路由（wlr协议引入）
- 配置外联口自动部署模板（VRF_SBI_100/VRF_SBI_200），指定VNIC、VLAN、IP范围、OSPF绑定

**步骤4: 打开IP路由自动配置开关**
```
SET AUTOCONFIG: SWITCHFLAG=TRUE;
```
- 打开后需查询 `DSP OPSASSISTSTATE` 确认自动部署状态为"Ready"

**步骤5: 配置运营商基础数据**
```
MOD NGMNO: NOID=0, FULLNAME="Operator A", SHORTNAME="OA";
ADD NGHPLMN: NOID=0, MCC="460", MNC="03";
```
- UDC默认配置NOID=0的默认记录

**步骤6: 配置NWDAF实例信息**

| 配置项 | 命令 | 说明 |
|--------|------|------|
| 实例名称 | ADD NFUUID | NFTYPE=NfNWDAF |
| Profile | ADD NFPROFILE | NFSTATUS=Registered, FQDN |
| TAI | ADD NFTAI | 配置支持的TAI（MCC/MNC/TAC） |
| TAI区域列表 | ADD TAIRANGELIST + ADD TACRANGE | 支持TAC范围配置 |
| 支持事件 | ADD NWDAFINFO | **NWDAFEVENTS=QOS_ANALYSIS-1&QOS_EXP_ANALYSIS-1** |
| 服务实例 | ADD NFSERVICE | NnwdafEvntSubs + NnwdafDataManagement |
| 服务版本 | ADD NFSERVICEVER | APIFULLVERSION |

**NWDAF支持的事件类型（与带宽控制直接相关）**:
- `QOS_ANALYSIS`：QoS分析事件
- `QOS_EXP_ANALYSIS`：QoS体验分析事件
- 事件后缀 `-1` 表示事件订阅级别

**步骤7: 配置NWDAF服务化接口数据**
- Server IP: `10.16.0.6`（FOR Server SBI）
- Client IP: `10.16.0.7`（FOR Client SBI）
- HTTP端口：80
- NF类型：NFTypeNWDAF

**步骤8: 配置NWDAF到NRF的数据**
```
ADD NRF: NRFINSTANCENAME="NRF_Instance_0", TLS=FALSE, PRIORITY=0;
ADD NRFADDR: NRFINSTANCENAME="NRF_Instance_0", IPV4ADDRESS="172.16.0.7", PORT=80;
ADD NRFPARA: NRFINSTANCENAME="NRF_Instance_0", WAITINTERVAL=5, MAXRETRYTIMES=3, SUBSCRISWITCH=ON, OAUTH2SWITCH=OFF;
```
- WAITINTERVAL=5：NRF等待间隔5秒
- MAXRETRYTIMES=3：最大重试3次
- SUBSCRISWITCH=ON：开启订阅功能

**步骤9: 激活NWDAF向NRF注册**
```
ACT NFONLINE: NFINSTANCENAME="NWDAF_Instance_0";
```
- 注意：现网NRF未支持NWDAF注册前，不需要执行此步骤

**步骤10: 配置NWDAF到UDN的数据**

主备UDN对接配置（PRIORITY控制优先级）:
```
// 逻辑主UDN - PRIORITY=1（高优先级）
ADD PNFPROFILE: NFINSTANCEID="UDN_instance_0", NFTYPE=NfUDN, IPV4ADDRESS1="172.16.0.10", PORT=80, PRIORITY=1;
ADD PNFSERVICE: NFINSTANCEID="UDN_instance_0", SERVICENAME=NudnDm, SCHEMA=http;

// 逻辑备UDN - PRIORITY=5（低优先级）
ADD PNFPROFILE: NFINSTANCEID="UDN_instance_1", NFTYPE=NfUDN, IPV4ADDRESS1="172.16.0.11", PORT=80, PRIORITY=5;
ADD PNFSERVICE: NFINSTANCEID="UDN_instance_1", SERVICENAME=NudnDm, SCHEMA=http;
```
- 现网未部署CloudUDN时无需此步骤
- PRIORITY值越小优先级越高，逻辑主UDN优先处理

#### 2.3.3 NWDAF调测

**调测验证项**:

| 验证项 | 命令 | 预期结果 |
|--------|------|----------|
| 路由互通 | NGPING | 收到响应且有成功收发包数 |
| Server链路状态 | DSP SBILINKSTATUS: ENTITYTYPE=Server | 链路状态为Normal（需有业务流程） |
| Client链路状态 | DSP SBILINKSTATUS: ENTITYTYPE=Client, PEERNFINSTID=xxx | 链路状态为Normal |
| NRF注册查询 | DSP REGNFINSTANCE | 可查看到NWDAF注册信息 |
| NRF Profile查询 | DSP REGNFINFO: NFINSTANCEID=xxx | Profile信息与实际配置一致 |

### 2.4 重点用户体验感知端到端调测

**调测前提**:
- 测试用户已签约重点用户业务套餐（如全球通套餐）
- 已完成各网元体验感知场景的业务配置
- 已在网管上下发端到端用户跟踪或各网元用户跟踪

**端到端验证流程（8步验证法）**:

| 步骤 | 观察点 | 接口/消息 | 预期结果 |
|------|--------|-----------|----------|
| 1 | UDC用户跟踪 | Nnwdaf_EventsSubscription_Subscribe Request | PCF向NWDAF发起订阅请求，event=QOS_EXP_ANALYSIS, status=NORMAL |
| 2 | UDC用户跟踪 | Nnwdaf_EventsSubscription_Subscribe Response | NWDAF回复"201 Created"，携带event=QOS_EXP_ANALYSIS |
| 3 | UDC用户跟踪 | Nsmf_EventExposure_SmEventExposureSubscribe Request | NWDAF向SMF发送订阅请求，携带appIds、event、nwdafInfo，event固定为QOS_EXP |
| 4 | UDG用户跟踪 | PFCP_Session_Modification Request | SMF向UPF发送订阅请求，SRR信元携带订阅的app-id，UPF回复响应 |
| 5 | UDC用户跟踪 | SMF回复订阅成功 | SMF回复"201 Created"，携带subId和appIds |
| 6 | UDG用户跟踪 | EMS-UFDR消息 | 业务持续5分钟或结束后，出现EMS-UFDR消息，含QosExpRptData信元 |
| 7 | UDN Ufdr跟踪 | Ufdr_Collector_Request | 收到UPF发送的Ufdr_Collector_Request消息，含QosExpRptData信元 |
| 8 | BOSS/SFTP | 体验数据接收 | BOSS/SFTP服务器正常收到体验数据 |

---

## 3. 配置与调测要点

### 3.1 UPCF配置链路（条件组→动作组→规则→策略→业务→发放）

配置必须按以下顺序执行：
1. **条件组**（ADD CONDITIONGROUP + ADD CONDITION）→ 策略管理 > 策略 > 条件组
2. **5G动作组**（ADD NGACTION + ADD NGACTIONATTR）→ 策略管理 > 策略 > 5G动作组
3. **规则**（ADD RULE + ADD RULECONDITIONGROUP + ADD RULENGACTION）→ 策略管理 > 策略 > 规则
4. **策略**（ADD POLICY + ADD POLICYRULE + ADD POLICYTRIGGER）→ 策略管理 > 策略 > 策略
5. **业务**（ADD SERVICE + ADD SERVICEPOLICY）→ 业务管理 > 业务 > 业务
6. **用户发放**（ADD PSUB + ADD PSRV）→ UPCF业务管理窗口

### 3.2 CloudUDN配置链路

1. 开启数据底座模式
2. 配置NFUUID
3. 配置逻辑IP（Server + Client）
4. 配置HTTP实体组和实体
5. 配置服务化接口接入点
6. 配置UFDR UDP接入（IP + 路由）
7. 配置主备容灾（第一协商通道 + 第二协商通道）

### 3.3 NWDAF配置链路

1. 关闭自动配置开关
2. 全局激活BFD
3. 配置IP路由数据（VPN + OSPF + 自动部署模板）
4. 打开IP路由自动配置开关
5. 配置运营商基础数据
6. 配置NWDAF实例（名称、Profile、TAI、事件、服务）
7. 配置NWDAF服务化接口（IP + HTTP + SBI接入点）
8. 配置NWDAF到NRF数据
9. 激活NWDAF向NRF注册
10. 配置NWDAF到UDN数据（主备）

### 3.4 关键约束与注意事项

- **CmdN23EventSubscription约束**: appIds全局上限255个，QOS_ANALYSIS事件关联的appIds上限40个
- **规则类型约束**: CmdN23EventSubscription只允许在5G Smf Pcc Rule和Non-PCC规则下关联
- **VPN一致性**: 逻辑接口的VPN必须与对应外联口的VPN相同，否则报文查询路由失败
- **自动部署时延**: 打开自动配置开关后，需等待自动部署生效（查询DSP OPSASSISTSTATE状态为Ready）
- **主备版本兼容**: 静默部署的V100R025C10SPC100版本与升级版不可主备对接
- **TLS安全**: 建议启用TLS确保SBI接口数据安全（需全网统一规划）
- **NWDAF注册条件**: 现网NRF未支持NWDAF注册前，不需要执行ACT NFONLINE

---

## 4. 与带宽控制的关系（QoE→带宽决策链路）

### 4.1 完整决策链路

```
重点用户签约业务套餐
    ↓
UE注册 + PDU激活 + 发起业务
    ↓
[UPCF] 触发器RAT_TY_CH/IPCAN_EST → 匹配条件组
    ↓
[UPCF] UpfSelectRule → 智能UPF选择成功（select_ai_upf）
    ↓
[UPCF] CmdN23EventSubscription → 通过N23接口向NWDAF订阅QOS_EXP_ANALYSIS
    ↓ (event=QOS_EXP_ANALYSIS, appIds=live, status=NORMAL)
[NWDAF] 接收订阅 → 向SMF转发订阅（Nsmf_EventExposure, event=QOS_EXP）
    ↓
[SMF] 向UPF发送订阅请求（PFCP Session Modification, SRR携带app-id）
    ↓
[UPF] 采集业务体验数据 → 上报EMS-UFDR消息（含QosExpRptData信元）
    ↓
[CloudUDN] UfdrUdpCollector接收Ufdr_Collector_Request → 汇聚体验数据
    ↓
[CloudUDN] 数据通过Nudn接口传递给UDC/NWDAF
    ↓
[NWDAF] 分析体验数据 → 返回分析结果给UPCF
    ↓
[UPCF] 基于分析结果计算策略 → 向SMF下发新策略
    ↓
[SMF/UPF] 执行QoS/带宽策略调整（限速、整形、保障等）
```

### 4.2 带宽控制关键接口

| 接口 | 消息 | 带宽控制作用 |
|------|------|-------------|
| N23（PCF↔NWDAF） | Nnwdaf_EventsSubscription | PCF发起QoE体验分析订阅，驱动带宽策略决策 |
| Nsmf（NWDAF↔SMF） | Nsmf_EventExposure | NWDAF向SMF转发订阅，触发UPF数据采集 |
| N4/PFCP（SMF↔UPF） | PFCP_Session_Modification | SMF向UPF下发订阅和策略变更（含带宽参数） |
| UFDR UDP（UPF→CloudUDN） | Ufdr_Collector_Request | UPF上报体验数据（含QosExpRptData）给数据底座 |
| Nudn（UDN↔UDC） | 服务化接口 | CloudUDN将汇聚数据传递给UDC/NWDAF分析 |

### 4.3 体验数据与带宽策略的映射

- **appIds=live**: 典型场景中的应用标识，NWDAF基于此标识分析对应应用的体验质量
- **QOS_EXP_ANALYSIS vs QOS_ANALYSIS**: 典型场景使用QOS_EXP_ANALYSIS（体验分析），异厂商场景使用QOS_ANALYSIS（QoS分析）
- **status=NORMAL/SUSPEND**: 控制N23订阅的启停，当用户切换到4G/2G网络时暂停订阅（SUSPEND），回到5G时恢复（NORMAL），避免无效的带宽策略调整
- **智能UPF选择（select_ai_upf）**: 只有选择了AI型UPF后才触发体验订阅，确保带宽调整决策有可靠的数据来源

### 4.4 与带宽控制特性的协同点

| 带宽控制特性 | 体验感知协同点 |
|-------------|---------------|
| SA带宽控制（GWFD-110311） | 体验感知分析结果可驱动SA场景下的带宽策略动态调整 |
| 流量整形Shaping（GWFD-020354） | QoE数据反映实际用户体验，可触发整形参数优化 |
| FUP公平使用（GWFD-020353） | 体验数据辅助FUP决策，避免过度限速影响重点用户体验 |
| PCC策略控制 | UPCF的N23订阅策略本身就是PCC体系的一部分 |

---

## 5. 关键概念术语

| 术语 | 说明 |
|------|------|
| UPCF | 智能PCF（User Plane aware PCF），支持通过N23接口向NWDAF订阅体验分析 |
| NWDAF | Network Data Analytics Function，网络数据分析功能，负责体验数据分析和返回 |
| N23接口 | PCF与NWDAF之间的体验分析数据订阅接口 |
| QOS_EXP_ANALYSIS | QoS体验分析事件，典型场景下PCF订阅的事件类型 |
| QOS_ANALYSIS | QoS分析事件，异厂商PCF场景下使用的事件类型 |
| QOS_EXP | SMF侧事件类型，NWDAF向SMF转发订阅时使用 |
| CmdN23EventSubscription | UPCF的5G动作类型，用于发起/暂停N23事件订阅 |
| UpfSelectRule | 智能UPF选择规则，选择AI型UPF |
| select_ai_upf | AI型UPF选择标识 |
| appIds | 应用标识列表，NWDAF基于此分析对应应用的体验质量 |
| CloudUDN | Cloud User Data Network，云化用户数据网络，作为体验感知的数据底座 |
| UFDR | User Flow Data Report，用户流数据报告 |
| QosExpRptData | QoS体验报告数据信元，包含体验感知采集结果 |
| UfdrUdpCollector | UFDR UDP采集器，CloudUDN中接收UPF上报体验数据的微服务 |
| NupfR | UPF与CloudUDN之间的体验数据上报接口 |
| Nudn | UDN与UDC之间的服务化接口 |
| SBI | Service Based Interface，服务化接口 |
| NRF | Network Repository Function，网络存储库功能 |
| RAT_TY_CH | RAT Type Change触发器，接入网络类型变化 |
| IPCAN_EST | IP-CAN Establishment触发器，IP-CAN会话建立 |
| 数据底座模式 | CloudUDN的工作模式，启用后可汇聚和处理体验感知数据 |
| 主备容灾 | 两套CloudUDN互为主备，通过双协商通道实现高可用 |
| 第一协商通道 | Local-Center配置，用于主备之间的基础通信 |
| 第二协商通道 | 主备配置页面，用于业务级容灾控制和倒换管理 |

---

## 6. 知识来源

| 序号 | 源文档 | 原始路径 |
|------|--------|----------|
| 1 | 配置智能PCF N23订阅策略（典型场景） | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/重点用户体验感知场景/UPCF侧配置/配置智能PCF N23订阅策略（典型场景）_39409773.md` |
| 2 | 配置智能PCF N23订阅策略（异厂商PCF场景） | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/重点用户体验感知场景/UPCF侧配置/配置智能PCF N23订阅策略（异厂商PCF场景）_31342057.md` |
| 3 | 调测重点用户体验感知功能 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/重点用户体验感知场景/调测重点用户体验感知功能_11788606.md` |
| 4 | 配置主备CloudUDN对接 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/接口对接配置/CloudUDN侧配置/配置主备CloudUDN对接_01_10010.md` |
| 5 | 配置入口说明 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/接口对接配置/CloudUDN侧配置/配置入口说明_34250365.md` |
| 6 | 配置接入用户体验数据（NupfR） | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/接口对接配置/CloudUDN侧配置/配置接入用户体验数据（NupfR）_58126773.md` |
| 7 | 配置服务化接口 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/接口对接配置/CloudUDN侧配置/配置服务化接口_19148098.md` |
| 8 | NWDAF典型配置实例 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/接口对接配置/UDC侧配置/NWDAF典型配置实例_90530646.md` |
| 9 | NWDAF配置流程 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/接口对接配置/UDC侧配置/NWDAF配置流程_34250353.md` |
| 10 | 调测NWDAF配置 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/接口对接配置/UDC侧配置/调测NWDAF配置_90690582.md` |
