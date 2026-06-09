# Batch-08 重点业务保障：CloudUDN-NWDAF对接与跨区移动

---

## 1. 概述

本批次知识文档融合提炼自"5G Core 重点业务保障解决方案"业务专题下"业务部署与调测"章节中的10个产品文档，涵盖四大主题领域：

1. **智能码率识别功能调测** -- 验证NWDAF通过机器学习训练自动识别业务码率、动态调整保障带宽的能力。
2. **跨NWDAF服务区域移动调测** -- 分为"建设初期"和"建设完成"两个阶段，验证用户跨NWDAF服务区时的保障连续性机制差异。
3. **CloudUDN侧接口对接配置** -- 涵盖业务Portal登录IP、主备CloudUDN对接、配置入口说明、无线侧指标数据接入、服务化接口（SBI）五大配置方向。
4. **NWDAF UDC侧配置** -- 包含NWDAF典型配置实例（IP路由+SBI+NRF+UDN对接全流程MML脚本）和NWDAF配置流程总览。

**核心问题**：这批文档解决的是"重点业务保障解决方案"在CloudUDN（用户面数据网络）和UDC/NWDAF（控制面分析引擎）两侧的基础设施对接与功能调测问题。没有这些对接配置和验证流程，带宽保障策略无法从NWDAF的分析能力传递到UPF的执行层面，整个带宽控制闭环就无法运转。

**在整个带宽控制场景中的位置**：前序Batch覆盖了FUP（公平使用策略）、体验感知、信令流程等业务逻辑层；本Batch转向基础设施层，解决的是"分析引擎如何接入数据源、如何与策略执行网元互通、用户移动时保障如何延续"的工程问题。

---

## 2. 核心知识点

### 2.1 智能码率识别：训练驱动的动态带宽适配

智能码率识别是NWDAF的核心AI能力之一，通过采集UPF上报的业务体验数据，训练生成业务码率识别模型，实现保障带宽的动态自适应调整。

**训练流程**：
1. **样本积累**：用户访问直播业务时，系统按时间段（0:00-5:59、6:00-11:59、12:00-17:59、18:00-23:59四段）采集体验数据，至少持续一天。
2. **样本检查**：通过 `DSP TRAININGDATA` 命令查询指定应用的训练样本数，需满足 `SET CODETRAINRULE` 命令中设置的最低样本量要求。
3. **手动训练**：样本达标后执行 `STR TRAININGPROCESS` 启动训练任务。
4. **状态检查**：执行 `DSP TRAININGSTATUS` 查看训练状态，预期为"训练结束"。
5. **结果查询**：执行 `DSP TRAININGRESULT` 查询训练结果，训练结果即为智能识别出的业务码率。

**保障带宽的两条来源路径**：
- NWDAF智能码率识别结果（通过 `DSP TRAININGRESULT` 查询）
- UDC产品通过 `ADD BANDWIDBNDAPP` 命令配置的带宽档位（通过 `LST BANDWIDBNDAPP` 查询）

**保障调整机制**：当用户体验恢复正常（UPF上报质优事件，`infoIndicate=QOS_EXP`，携带 `avgBitrateUl`），NWDAF向PCF发送更新保障建议（`Npcf_PolicyAuthorizationServiceAPI_ModAppSessions Request`），将保证带宽和最大带宽调小，取值来自智能码率识别结果或配置的带宽档位。

### 2.2 跨NWDAF服务区域移动：建设初期 vs 建设完成

跨NWDAF服务区域移动是重点业务保障在用户漫游场景下的连续性保障机制，分为两个建设阶段，核心差异在于跨区后的保障处理方式。

**建设初期方案（省内跨NWDAF）**：

| 维度 | 建设初期 |
|------|----------|
| 适用场景 | 用户移出当前NWDAF服务区，仍在省内支持的TAI范围内 |
| 触发机制 | NWDAF向SMF订阅 `SAREA_CH`（服务区域变更）事件 |
| 保障处理 | NWDAF判定用户在支持的TA区域内，**保持重点业务保障订阅**，不取消保障 |
| 配额调整 | NWDAF更新本地对应小区GBR配额为**本地配置的拜访地GBR保障阈值** |
| 保障建议 | NWDAF**不向PCF发起更新保障建议**，保持已有保障建议 |
| 关键查询命令 | `LST NFTAI`（NWDAF服务区域）、`LST TAIRANGELIST`、`LST SRVTAI`、`LST SRVTAIRANGE`（支持的TA区域） |

**建设完成方案（跨省漫游目标方案）**：

| 维度 | 建设完成 |
|------|----------|
| 适用场景 | 用户离开当前NWDAF服务区域，跨省漫游 |
| 触发机制 | NWDAF向SMF订阅 `SAREA_CH` **和** `SCNN_CH`（服务区域和核心网节点变更）事件 |
| SMF响应 | 携带最新的**TAI和AMFID**（建设初期仅携带TAI） |
| 分析转移 | 源NWDAF通过TAI寻址目标NWDAF，发起 `Nnwdaf_EventsSubscription_Subscribe Request`（携带 `nwdafId`） |
| 质差数据转发 | 源NWDAF向目标NWDAF转发质差数据（`Nnwdaf_DataManagement_Notify Request`，携带 `upfNotificationItems`） |
| 保障建议取消 | 源NWDAF向PCF发起保障建议取消（`Npcf_PolicyAuthorizationServiceAPI_DeleteAppSessions Request`） |
| 保障建议重建 | 目标NWDAF通过 `Nnwdaf_EventsSubscription_Notify Request` 向源NWDAF发送保障建议，源NWDAF再向PCF发起保障建议 |

**两阶段核心差异对比**：

| 差异点 | 建设初期 | 建设完成 |
|--------|----------|----------|
| 订阅事件 | 仅 `SAREA_CH` | `SAREA_CH` + `SCNN_CH` |
| SMF响应内容 | 最新TAI | 最新TAI + AMFID |
| 跨区后保障 | 保持原有保障，仅更新本地配额 | 取消原保障 -> 分析转移 -> 目标NWDAF重新发起保障 |
| NWDAF间交互 | 无 | 源->目标分析转移 + 目标->源质差数据订阅 |
| 复杂度 | 低（单NWDAF内部处理） | 高（源/目标NWDAF协同） |

### 2.3 CloudUDN的五大配置方向

CloudUDN（Cloud User Data Network）是用户面数据网络，作为重点业务保障的数据底座，承担数据采集、分析计算和策略下发的基础设施角色。

**（1）业务Portal登录IP配置**

- 目的：配置可登录CloudUDN业务Portal（特性报表查询入口）的IP地址
- 配置入口：`应用配置 > 业务配置 > 基础配置 > 系统配置 > 导航页配置`
- 配置内容：本端接口IP地址+掩码（来自PBU_C-A虚拟机vNIC2）、路由配置（对端IP地址+掩码+网关）
- 数据来源：《NFV LLD文档》"5G Core业务IP对接设计"页签
- 适用场景：首次使用特性前配置，或主备CloudUDN组网场景

**（2）主备CloudUDN对接配置**

采用双协商通道架构：

- **第一协商通道（Local-Center配置）**：配置对端IP地址、用户名（`actstdbyact`）、密码，打通主备CloudUDN间的基础通信。用户名需通过CSP管理页面在**对端**OM Portal创建，密码有效期设置为999天。
- **第二协商通道（主备配置页面）**：配置主备模式开关、倒换策略、故障判断阈值等。包含PGSQL业务数据库的IP地址配置和路由配置。

关键倒换参数：
- 逻辑主备关系：主侧配置为"逻辑主"，备侧配置为"逻辑备"
- 设备倒换：支持手动倒换（可勾选"强制倒换"）和自动倒换
- 自动倒回开关：逻辑主恢复后自动倒回
- 每日倒换次数上限：3次，倒换间隔：10分钟
- 故障判断阈值：接入节点/计算节点/存储节点故障均设为2个，NATLOG链路/UFDR链路故障阈值为2条
- SBI倒换判断条件：可用NWDAF（UDC）数，判定时长5分钟
- 主备信息同步间隔：5秒

限制：不支持静默部署的 V100R025C10SPC100 版本与低版本升级至该版本的CloudUDN进行主备对接。

验证告警检查：不应存在 ALM-86128（主备数据库数据同步失败）、ALM-86127（一级容灾控制通道连接失败）、ALM-86132（CloudUDN主备配置不一致）。

**（3）配置入口说明**

CloudUDN采用流水线式配置设计：
- 特性必选配置和仅该特性涉及的可选配置汇聚在**特性配置界面**
- 公共配置汇聚在**可选配置界面**
- 当前产品以**微服务粒度**进行配置呈现，但存在某微服务的部分功能不被当前特性支持的情况（需参考特性指南判断哪些配置项需要配置）
- 配置入口路径：`应用配置 > 业务配置`

**（4）接入无线侧指标数据**

CloudUDN作为FTP/SFTP客户端从MAE或第三方设备获取无线侧指标，为重点业务保障提供数据源。

配置要素：
- **IP配置**：服务实例名称（`upccreportftpserver-*`，自动生成）、接口IP地址（来自OM网络网段）
- **路由配置**：对端数据源设备的IP地址/网段+网关
- **FTP客户端模式配置**：FTP服务器名称、对端服务器IP、服务端口（22）、用户名/密码、协议类型（推荐SFTP）、下载路径、网管类型、时间偏移参数
- **SFTP客户端密钥配置**：密钥交换算法（推荐 `diffie-hellman-group-exchange-sha256`）、主机密钥算法（推荐 `ecdsa-sha2-nistp256`）、对称加密算法（推荐 `aes128-ctr`）、MAC算法（推荐 `hmac-sha2-256`）
- **文件存储配置**：分区数（建议 = CalcTForIntellect服务实例数 x 30，最大100）、文件老化时间（建议21600，可提高无线小区负载预测准确率）、下载时间范围/间隔（默认15分钟）

安全建议：推荐使用SFTP而非FTP，避免未加密传输风险。

验证方式：通过OM Portal的PING和TRACE操作验证网络连通性，检查 ALM-86115 告警。

**（5）服务化接口（SBI）配置**

CloudUDN支持两类服务化接口：
- **Nudn接口**：UDN与UDC之间，UDN做Server
- **Nupf接口**：UDN与UPF之间，UDN做Client

配置前提：已完成软件安装、加载特性Schema包（`CloudUDN_*V1XXR02XCXXSPCXXX*_Vvip_Schema.tar.gz`）、外联口及路由配置。

配置步骤（MML命令序列）：
1. 开启数据底座模式（OM Portal界面操作）
2. `ADD UDNNFUUID` -- 配置UDN的NF UUID
3. `ADD LOGICIP` -- 增加Server端和Client端的逻辑IP（IPv4/IPv6）
4. `ADD HTTPLEGRP` -- 配置HTTP本端实体组
5. `ADD HTTPLE` -- 配置HTTP本端实体（Server端口号80，Client端无端口）
6. `ADD SBIAPLE` -- 配置本端服务化接口接入点

验证：使用 `NGPING` 命令测试逻辑接口IP连通性，失败时回退到 `PING` 测试外联口连通性，再检查路由配置。

### 2.4 NWDAF UDC侧配置：典型实例与流程

**NWDAF配置流程（四步）**：

| 步骤 | 内容 | 参考文档 |
|------|------|----------|
| 本局数据配置 | NWDAF实例、Profile、TAI区域、事件、服务等 | 配置NWDAF本局数据 |
| 接口配置 | SBI接口逻辑IP、HTTP实体、接入点 | 配置SBI接口 |
| 本地NRF配置 | NRF实例、地址、协议参数 | 配置本地NRF |
| 业务配置 | 依据业务需求配置业务参数 | UDC侧配置 |

**NWDAF典型配置实例关键步骤**：

1. **关闭自动配置开关**：`LST AUTOCONFIG` 查询状态，`DSP OPSASSISTSTATE` 确认自动部署完成，`SET AUTOCONFIG: SWITCHFLAG=FALSE` 关闭
2. **全局激活BFD**：`SET BFD: BFDENABLE=TRUE`
3. **配置IP路由数据**：
   - 创建VPN实例：`ADD L3VPNINST: VRFNAME="VPN_SBI"` + `ADD VPNINSTAF`
   - 配置OSPF路由：`ADD OSPF`（进程+区域+BFD）+ `ADD OSPFIMPORTROUTE`
   - 配置外联口自动部署模板：`ADD AUTOSCALINGSERVICE`（VRF_SBI_100/200，含VLAN、IP范围、OSPF绑定）
4. **打开自动配置开关**：`SET AUTOCONFIG: SWITCHFLAG=TRUE`（需等待自动部署生效，用 `DSP OPSASSISTSTATE` 确认Ready）
5. **配置运营商基础数据**：`MOD NGMNO` + `ADD NGHPLMN`
6. **配置NWDAF实例信息**：
   - 实例名称：`ADD NFUUID: NFTYPE=NfNWDAF`
   - Profile：`ADD NFPROFILE: NFSTATUS=Registered`
   - TAI及区域：`ADD NFTAI` + `ADD TAIRANGELIST` + `ADD TACRANGE`
   - 支持事件：`ADD NWDAFINFO: NWDAFEVENTS=QOS_ANALYSIS-1&QOS_EXP_ANALYSIS-1`
   - 服务实例：`ADD NFSERVICE`（NnwdafEvntSub + NnwdafDataManagement）+ `ADD NFSERVICEVER`
7. **配置SBI接口数据**：
   - 逻辑IP：`ADD LOGICIP`（Server: 10.16.0.6，Client: 10.16.0.7）
   - HTTP实体组：`ADD HTTPLEGRP`
   - HTTP实体：`ADD HTTPLE`（Server/Client，端口80，TLS=NO）
   - SBI接入点：`ADD SBIAPLE: NFTYPE=NFTypeNWDAF`
8. **配置到NRF的数据**：
   - NRF实例：`ADD NRF: TLS=FALSE`
   - NRF地址：`ADD NRFADDR`（IP+端口80）
   - NRF协议参数：`ADD NRFPARA`（等待间隔5秒，重试3次，订阅开关ON）
   - 激活注册：`ACT NFONLINE`（现网NRF未支持NWDAF注册前不需要）
9. **配置到UDN的数据**（现网无CloudUDN时跳过）：
   - 主UDN：`ADD PNFPROFILE: NFTYPE=NfUDN, PRIORITY=1` + `ADD PNFSERVICE: SERVICENAME=NudnDm`
   - 备UDN：`ADD PNFPROFILE: NFTYPE=NfUDN, PRIORITY=5` + `ADD PNFSERVICE`

**NWDAF支持的两种分析事件**：
- `QOS_ANALYSIS`：QoS分析（质差保障）
- `QOS_EXP_ANALYSIS`：QoS体验分析

### 2.5 UDC（统一数据中心）在保障架构中的角色

UDC（Unified Data Center）在重点业务保障解决方案中扮演NWDAF的承载平台角色：
- NWDAF作为UDC上的分析网元实例运行
- PCF（策略控制功能）向NWDAF发起QoS分析订阅
- SMF（会话管理功能）向NWDAF上报用户位置变更
- UPF（用户面功能）向NWDAF上报质差/质优事件
- NWDAF向PCF下发保障建议（带宽调整、专载建立/修改/删除）

**核心信令交互链路**：
```
UPF --质差/质优事件--> NWDAF --保障建议--> PCF --策略下发--> SMF --专载建立--> UPF
```

### 2.6 重点业务保障调测的信令观测体系

调测过程通过UDC用户跟踪观察以下关键信令：

| 信令消息 | 方向 | 用途 |
|----------|------|------|
| `Nnwdaf_EventsSubscription_Subscribe Request` | PCF -> NWDAF | PCF发起QoS分析订阅 |
| `Nsmf_EventExposure_SmEventExposureSubscribe Request` | NWDAF -> SMF | NWDAF订阅SMF事件（SAREA_CH/SCNN_CH/QOS_ANA） |
| `Nsmf_EventExposure_SmEventExposureSubscribe Response` | SMF -> NWDAF | SMF返回最新TAI（+AMFID） |
| `Nsmf_EventExposure_SmEventExposureUpdate Request` | NWDAF -> SMF | NWDAF更新订阅（增加QOS_ANA事件） |
| `Nsmf_EventExposure_SmEventExposureNotify Request` | SMF -> NWDAF | SMF通知用户位置变更 |
| `Nupf_EventExposureService_EventNotification Request` | UPF -> NWDAF | UPF上报质差/质优事件 |
| `Npcf_PolicyAuthorizationServiceAPI_PostAppSessionEventNotify Request` | PCF -> NWDAF | PCF通知保障成功（SUCCESSFUL_RESOURCES_ALLOCATION） |
| `Npcf_PolicyAuthorizationServiceAPI_ModAppSessions Request` | NWDAF -> PCF | NWDAF更新保障建议（调整带宽） |
| `Npcf_PolicyAuthorizationServiceAPI_DeleteAppSessions Request` | NWDAF -> PCF | NWDAF取消保障建议 |
| `Nnwdaf_EventsSubscription_Notify Request` | 目标NWDAF -> 源NWDAF | 跨区时目标NWDAF发送保障建议 |
| `Nnwdaf_DataManagement_Subscribe Request` | 目标NWDAF -> 源NWDAF | 跨区时目标NWDAF订阅质差数据 |
| `Nnwdaf_DataManagement_Notify Request` | 源NWDAF -> 目标NWDAF | 跨区时源NWDAF转发质差数据 |

---

## 3. 配置调测要点

### 3.1 智能码率识别调测命令清单

| 命令 | 网元 | 用途 |
|------|------|------|
| `SET CODETRAINRULE` | UDC | 设置训练规则（含最低样本数要求） |
| `DSP TRAININGDATA` | UDC | 查询训练样本数 |
| `STR TRAININGPROCESS` | UDC | 手动启动训练任务 |
| `DSP TRAININGSTATUS` | UDC | 查询训练状态（预期"训练结束"） |
| `DSP TRAININGRESULT` | UDC | 查询训练结果（智能码率识别值） |
| `ADD POLICYCONDITION` | UDG | 设置质差检测条件（触发质差） |
| `ADD APP` | UDG | 配置应用保障带宽 |
| `LST APP` | UDG | 查询应用保障带宽配置 |
| `ADD BANDWIDBNDAPP` | UDC | 配置带宽档位 |
| `LST BANDWIDBNDAPP` | UDC | 查询带宽档位配置 |

**调测触发质差的技巧**：
- 速率类基线（如上行平均速率基线）：设置较高的值，更容易触发质差检测
- 时延类基线（如E2E RTT基线值）：设置较低的值，更容易触发质差检测
- 重新设置质差检测条件后，需要重新激活用户再观察

### 3.2 跨NWDAF服务区域移动调测要点

**通用前提条件**：
- 测试用户已签约重点业务保障套餐
- 已完成应用GBR保障功能调测
- 已完成对应的跨NWDAF配置（建设初期/建设完成）
- 已在网管下发端到端用户跟踪

**建设初期调测观测关键点**：
1. PCF向NWDAF发起QoS分析订阅（Nnwdaf_EventsSubscription_Subscribe）
2. NWDAF向SMF订阅携带 `SAREA_CH` 事件
3. 用户移出服务区但在支持TA内时：NWDAF保持订阅、保持保障建议、仅更新本地GBR配额
4. 查询NWDAF服务区域：`LST NFTAI`、`LST TAIRANGELIST`
5. 查询NWDAF支持TA区域：`LST SRVTAI`、`LST SRVTAIRANGE`

**建设完成调测观测关键点**：
1. NWDAF向SMF订阅携带 `SAREA_CH` + `SCNN_CH` 事件
2. SMF响应携带最新TAI + AMFID
3. 用户离开服务区后，SMF向NWDAF通知最新位置
4. 源NWDAF向目标NWDAF发起分析转移（携带nwdafId）
5. 目标NWDAF向源NWDAF订阅质差数据（anaSub）
6. 源NWDAF向PCF取消已有保障建议
7. 源NWDAF向目标NWDAF转发质差数据
8. 目标NWDAF向源NWDAF发送新保障建议
9. 源NWDAF向PCF发起保障建议

### 3.3 CloudUDN侧配置检查清单

| 配置项 | 检查内容 | 验证方法 |
|--------|----------|----------|
| 业务Portal登录IP | 接口IP+路由配置 | 访问业务Portal |
| 主备对接-第一协商通道 | 对端IP+用户名密码 | CspServgate服务PING对端导航页IP |
| 主备对接-第二协商通道 | PGSQL IP+路由+主备参数 | PSIBusinessPGSQL服务PING对端协商通道IP |
| 主备告警 | 无同步失败/通道断/配置不一致 | 检查ALM-86128/86127/86132 |
| 无线侧指标接入 | FTP/SFTP服务器连通 | UPCCReportFtpServer服务PING对端 |
| 无线侧文件下载 | 成功下载数据文件 | 检查ALM-86115告警 |
| SBI接口 | UDN-UDC逻辑IP互通 | NGPING -> PING -> 路由检查 |

### 3.4 NWDAF UDC侧配置关键MML命令

| 命令 | 用途 | 关键参数 |
|------|------|----------|
| `SET AUTOCONFIG` | 自动配置开关 | SWITCHFLAG=TRUE/FALSE |
| `DSP OPSASSISTSTATE` | 查询自动部署状态 | 确认Ready后再操作 |
| `SET BFD` | 全局BFD | BFDENABLE=TRUE |
| `ADD L3VPNINST` | VPN实例 | VRFNAME="VPN_SBI" |
| `ADD OSPF` | OSPF进程 | PROCID+BFDALLINTFFLG=TRUE |
| `ADD AUTOSCALINGSERVICE` | 自动部署模板 | VLAN+IP范围+OSPF绑定 |
| `ADD NFUUID` | NF实例UUID | NFTYPE=NfNWDAF |
| `ADD NFPROFILE` | NF Profile | NFSTATUS=Registered |
| `ADD NFTAI` | NF支持的TAI | MCC+MNC+TAC |
| `ADD NWDAFINFO` | NWDAF事件 | NWDAFEVENTS=QOS_ANALYSIS-1&QOS_EXP_ANALYSIS-1 |
| `ADD NRF` | NRF实例 | TLS=FALSE |
| `ADD NRFADDR` | NRF地址 | IP+PORT |
| `ADD NRFPARA` | NRF协议参数 | WAITINTERVAL=5, MAXRETRYTIMES=3, SUBSCRISWITCH=ON |
| `ACT NFONLINE` | 激活NF注册 | 现网NRF不支持NWDAF注册前不需要 |
| `ADD PNFPROFILE` | 对端NF Profile | UDN主备（PRIORITY区分） |

---

## 4. 与带宽控制的关系

本批次文档虽然是基础设施对接和调测类内容，但与带宽控制场景存在深层关联：

### 4.1 智能码率识别是带宽控制的前置感知

带宽控制的核心是"根据业务实际需求动态调整保障带宽"。智能码率识别通过AI训练自动学习业务的真实码率特征，为带宽控制提供精确的带宽基线数据：
- 训练结果直接影响 `ADD APP` 和 `ADD BANDWIDBNDAPP` 中保障带宽值的合理性
- 质差触发 -> NWDAF保障建议（初始带宽）-> 体验恢复 -> NWDAF调整建议（降低带宽），形成带宽控制的动态闭环
- 没有智能码率识别，保障带宽只能依赖静态配置，无法适配不同业务类型和变化的网络条件

### 4.2 跨区移动涉及QoS连续性

用户跨NWDAF服务区移动时的保障连续性，本质上是带宽控制策略的跨域延续：
- **建设初期**：带宽保障在NWDAF内部维持，仅切换GBR配额来源（本地配置阈值），保障策略本身不中断
- **建设完成**：保障策略经历"取消 -> 分析转移 -> 重建"过程，存在短暂保障中断窗口，但目标NWDAF接管后恢复完整带宽控制
- 跨区移动中的GBR配额调整、专载建立/取消，都是带宽控制在移动场景下的具体实现

### 4.3 NWDAF提供负荷数据用于策略调整

NWDAF作为分析引擎，其数据分析能力是带宽控制策略决策的大脑：
- QoS分析（`QOS_ANALYSIS`）：检测业务质差，触发保障
- QoS体验分析（`QOS_EXP_ANALYSIS`）：监测业务体验恢复，触发保障调整
- 无线侧指标数据接入：提供小区负荷、无线质量等数据，用于更精确的带宽策略决策
- 这些分析能力为PCC策略、FUP策略、带宽管理等带宽控制特性提供数据输入

### 4.4 CloudUDN作为数据底座支撑带宽决策

CloudUDN开启"数据底座模式"后，作为用户面数据的采集和分析平台：
- 从MAE/第三方设备采集无线侧指标（小区负荷、PRB利用率等）
- 通过FTP/SFTP获取性能数据文件
- 数据经CalcTForIntellect服务处理，为NWDAF提供决策依据
- 主备CloudUDN容灾保障数据采集的高可用性，确保带宽控制数据源不中断

### 4.5 SBI接口是策略传递的管道

服务化接口（SBI）是NWDAF保障建议从分析引擎传递到策略执行网元的通信管道：
- Nudn接口（UDN-UDC）：CloudUDN与UDC/NWDAF之间的数据交互通道
- Nupf接口（UDN-UPF）：CloudUDN与UPF之间的用户面数据通道
- 没有SBI接口配置，NWDAF的分析结果无法到达PCF，带宽控制策略无法下发执行

---

## 5. 关键术语

| 术语 | 全称/含义 |
|------|-----------|
| **CloudUDN** | Cloud User Data Network，云端用户数据网络，重点业务保障的数据底座 |
| **NWDAF** | Network Data Analytics Function，网络数据分析功能，5G核心网分析网元 |
| **UDC** | Unified Data Center，统一数据中心，承载NWDAF等网元的平台 |
| **SBI** | Service Based Interface，服务化接口，5GC控制面网元间基于HTTP的通信接口 |
| **NRF** | Network Repository Function，网络存储库功能，提供NF发现和注册服务 |
| **PCF** | Policy Control Function，策略控制功能，接收NWDAF保障建议并下发策略 |
| **SMF** | Session Management Function，会话管理功能，管理PDU会话和用户位置 |
| **UPF** | User Plane Function，用户面功能，执行QoS策略和业务数据转发 |
| **MAE** | Mobile Autonomous Engine，移动自动驾驶引擎，华为无线网管系统 |
| **OM Portal** | Operation Maintenance Portal，操作维护门户 |
| **BFD** | Bidirectional Forwarding Detection，双向转发检测，用于快速检测链路故障 |
| **OSPF** | Open Shortest Path First，开放式最短路径优先，动态路由协议 |
| **SAREA_CH** | Service Area Change，服务区域变更事件 |
| **SCNN_CH** | Serving Core Network Node Change，服务核心网节点变更事件 |
| **QOS_ANA** | QoS Analysis，QoS分析事件 |
| **QOS_EXP** | QoS Experience，QoS体验事件 |
| **GBR** | Guaranteed Bit Rate，保证比特速率 |
| **PGSQL** | PostgreSQL，CloudUDN中使用的业务数据库 |
| **Schema包** | 特性配置模板包，格式为 `CloudUDN_*V1XXR02XCXXSPCXXX*_Vvip_Schema.tar.gz` |
| **CSP** | Cloud Service Platform，云服务平台，CloudUDN底层管理平台 |
| **CalcTForIntellect** | CloudUDN中的计算服务实例，用于无线侧指标数据处理 |
| **NFUUID** | Network Function Universally Unique Identifier，网络功能唯一标识 |
| **Nudn接口** | UDN与UDC之间的服务化接口 |
| **Nupf接口** | UDN与UPF之间的服务化接口 |
| **数据底座模式** | CloudUDN的工作模式，开启后支持VVIP业务体验保障特性 |

---

## 6. 知识来源

| 序号 | 文件名 | 内容主题 |
|------|--------|----------|
| 1 | 调测智能码率识别功能_78412864.md | 智能码率识别训练流程与调测验证 |
| 2 | 调测跨NWDAF服务区域移动（建设初期）_26365357.md | 建设初期跨区移动调测（省内TA内保持保障） |
| 3 | 调测跨NWDAF服务区域移动（建设完成）_06163700.md | 建设完成跨区移动调测（跨省分析转移） |
| 4 | 配置业务Portal登录IP_77403933.md | CloudUDN业务Portal登录IP与路由配置 |
| 5 | 配置主备CloudUDN对接_10321188.md | 主备CloudUDN双协商通道与倒换参数 |
| 6 | 配置入口说明_02548688.md | CloudUDN流水线式配置入口与微服务粒度说明 |
| 7 | 配置接入无线侧指标数据_17790682.md | FTP/SFTP接入无线侧指标数据全流程 |
| 8 | 配置服务化接口_17947706.md | CloudUDN SBI接口（Nudn/Nupf）MML配置 |
| 9 | NWDAF典型配置实例_57714293.md | NWDAF完整MML脚本（路由+SBI+NRF+UDN） |
| 10 | NWDAF配置流程_57682729.md | NWDAF四步配置流程总览 |

**原始路径前缀**：`output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/`

**文件1-3子路径**：`初始业务配置/调测初始业务配置/`

**文件4-8子路径**：`接口对接配置/CloudUDN侧配置/`

**文件9-10子路径**：`接口对接配置/UDC侧配置/`
