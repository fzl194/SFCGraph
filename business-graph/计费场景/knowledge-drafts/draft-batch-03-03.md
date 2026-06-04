# Batch 03-03: Ga/Gy接口离线/在线计费原理 知识草稿

## 来源文件清单

| # | 文件 | UNC路径 |
|---|------|---------|
| 1 | Ga_Gy接口离线_在线计费概述_87165687 | 计费原理/Ga_Gy接口离线_在线计费/ |
| 2 | CG组网可靠性（GGSN_SGW-C_PGW-C）_01_10016 | 同上/Ga接口离线计费原理/ |
| 3 | 离线计费业务流程（GGSN_SGW-C_PGW-C）_01_10015 | 同上 |
| 4 | 离线计费话单（GGSN_SGW-C_PGW-C）_01_10017 | 同上 |
| 5 | 离线计费话单（SGSN）_01_10018 | 同上 |
| 6 | Gy接口在线计费原理_89122043 | 同上/Gy接口在线计费原理/ |
| 7 | OCS组网和链路可靠性_01_10020 | 同上 |
| 8 | 在线计费DCC会话业务流程_01_10019 | 同上 |
| 9 | 在线计费的异常处理_01_10021 | 同上 |
| 10 | 在线计费可选功能介绍_01_10023 | 同上 |
| 11 | 在线计费自动回切业务流程_01_10022 | 同上 |
| 12 | CC_01_10011 | 同上/相关术语/ |
| 13 | DCC_01_10014 | 同上 |
| 14 | RG_01_10010 | 同上 |
| 15 | SID_01_10013 | 同上 |
| 16 | URR_01_10012 | 同上 |
| 17 | 话单_01_10009 | 同上 |

UNC根路径前缀: `网络部署/业务专题/5G Core 计费解决方案/计费解决方案概述/`

---

## 一、Ga/Gy概述与计费方式选择

### K70: 离线计费端到端架构
> 来源: Ga_Gy接口离线_在线计费概述_87165687

**原理知识**

离线计费端到端流程：GGSN-U/SGW-U/PGW-U收集用户业务使用情况 → 控制面按计费规则格式化为话单 → 通过Ga接口发送到CG → CG完成存储/标准化 → 定期上传BS → 运营商定期结算。

涉及网元：SGSN、GGSN-C/SGW-C/PGW-C、GGSN-U/SGW-U/PGW-U、CG、BS、OCS。

### K71: 在线/离线计费方式选择的优先级机制
> 来源: Ga_Gy接口离线_在线计费概述_87165687

**配置知识**

在线计费来源优先级：PCRF下发 > AAA Server下发 > 本地配置（UserProfile > APN > CC）
离线计费来源优先级：PCRF下发 > 本地配置（UserProfile > APN > CC）

PCRF在CCA-I消息中通过Online AVP指示在线计费；RADIUS Server通过Access-Accept携带OCS-ID指示在线计费。

计费接口选择优先级：ADD APNCHGMODE（基于APN）> SET CHGMODE（全局）。

### K72: 内容计费匹配流程与Rule优先级
> 来源: Ga_Gy接口离线_在线计费概述_87165687

**原理知识**

内容计费匹配流程：
1. 用户激活 → 通过APN确定UsrProfGroup → 根据用户信息匹配UserProfile
2. UserProfile绑定Rule组，Rule包含三四层/七层协议/七层信息
3. 数据报文到达UDG → SA技术解析 → 与Rule组匹配

**关键匹配规则**：
- 命中Rule的FlowFilter → 使用Rule携带的URR组计费
- 未命中Rule或Rule无URR组 → 继承UserProfile绑定的**缺省URR组**
- UserProfile无URR组 → 不计费（因此一般需配置缺省URR组）

Rule优先级：PCRF下发 > AAA Server下发 > UNC本地配置。

---

## 二、Ga接口离线计费原理

### K73: 离线计费核心业务流程（PFCP交互）
> 来源: 离线计费业务流程（GGSN_SGW-C_PGW-C）_01_10015

**协议知识**

离线计费核心流程（以EPC为例）：
1. 用户发起承载建立请求
2. SGW-C/PGW-C通过PFCP Session Establishment Request下发Create URR信元组
3. 用户承载建立成功
4. 用户访问业务，达到阈值时SGW-U/PGW-U发送PFCP Session Report Request（携带Usage Report）
5. SGW-C/PGW-C记录流量/时长信息 → 达到话单关闭条件后产生原始话单 → 通过Ga接口发送到CG

### K74: Create URR关键信元
> 来源: 离线计费业务流程（GGSN_SGW-C_PGW-C）_01_10015

**协议知识**

Create URR主要子信元：
- **URR ID**：唯一标识一个Create URR
- **Measurement Method**：计费方式（流量/时长/事件）
- **Reporting Triggers**：上报触发条件（Periodic/Volume Threshold/Time Threshold/Linked Usage Reporting等）
- **Volume Threshold**：流量阈值（总/上行/下行）
- **Time Threshold**：时间阈值
- **Event Threshold**：事件阈值
- **Linked URR ID**：关联URR（A link B，当B上报时也上报A）

### K75: CG链路状态三态判定机制
> 来源: 离线计费业务流程（GGSN_SGW-C_PGW-C）_01_10015

**方案设计知识**

链路状态三态判定（基于采样周期内通断比）：
- **高通态**（>80%）：允许话单发送，允许历史缓存话单发送
- **低通态**（50%~80%）：允许话单发送，禁止历史缓存话单发送
- **阻塞态**（<50%）：禁止话单发送

探测机制：配置CG后发Node Alive Request → 每固定1分钟发Echo Request → 3次无响应（可配置）则链路异常 → 触发ALM-81021告警。

此机制动态平滑调整传送速率，避免急停急起对CG的冲击。

### K76: CG选择优先级与号段匹配
> 来源: CG组网可靠性（GGSN_SGW-C_PGW-C）_01_10016

**配置知识**

CG选择优先级：
1. PCRF下发（通过CCA-I的Primary/Secondary-Charging-Collection-Function-Name AVP）→ 必须在本地已配置才生效
2. 本地CG服务器池（号段匹配CG组 → 全局CG组 → 非CG组的CG）
3. PCRF下发的主备CG均不可用时，在本地CG服务器池中选择

号段匹配逻辑：号段匹配CG组 → 在组内按优先级和状态选择CG → 未匹配但配置了全局CG组 → 在全局CG组内选择 → 都未匹配 → 在非CG组CG中选最高优先级。

### K77: CG负荷分担两种算法
> 来源: CG组网可靠性（GGSN_SGW-C_PGW-C）_01_10016

**方案设计知识**

| 算法 | 激活时选择 | 发送话单时 | 同一用户话单 | 负荷均衡性 |
|------|-----------|-----------|-------------|-----------|
| 基于负载 | 状态正常+最高优先级中选负载最少 | 重新选负载最少 | 可能发往不同CG | 处理快的CG接收更多 |
| 基于用户 | 状态正常+最高优先级中依次选择 | 激活时CG正常则继续使用 | 每次发往同一CG | 不同用户轮选，更均衡 |

通过SET CDRTRANSFER配置选择算法。

### K78: CG过载保护WAL机制
> 来源: CG组网可靠性（GGSN_SGW-C_PGW-C）_01_10016

**配置知识**

UNC提供WAL（Windows Access Limit）过载保护：当CG当前待处理负荷超出配置的WAL值（ADD CG命令配置）时，将该CG置为不可用，后续负荷转移到其他CG。与Gy接口OCS的WAL机制原理相同。

---

## 三、离线计费话单

### K79: 话单类型与版本对应关系
> 来源: 离线计费话单（GGSN_SGW-C_PGW-C）_01_10017

**原理知识**

| 话单类型 | 版本 | 说明 |
|---------|------|------|
| G-CDR | R98~R7 | GPRS/UMTS用户，不含内容计费 |
| eG-CDR | R6/R7 | GPRS/UMTS用户，增加内容计费字段，一张话单可记录多个业务 |
| SGW-CDR | R8~R10 | LTE用户（SGW-C形态），用户级计费，不支持内容计费 |
| PGW-CDR | R8~R10 | LTE/EPC融合用户（PGW-C形态），支持内容计费 |

**隐性规则**：EPC融合组网下必须采用PGW-CDR以保持GUL切换前后话单类型一致。

### K80: 话单容器机制
> 来源: 离线计费话单（GGSN_SGW-C_PGW-C）_01_10017

**原理知识**

引入容器概念的背景：为记录各种计费条件改变时的信息而不增加话单量。一张话单可包含多个容器。

| 容器类型 | 粒度 | 记录内容 | 新容器产生条件 |
|---------|------|---------|--------------|
| 流量容器 | 承载级 | 流量/时长，不区分业务 | QoS改变、费率时段改变、用户位置改变、产生话单 |
| 业务容器 | 业务级 | 某业务的流量/时长 | IP-CAN承载修改、费率时段改变、在线计费处理失败(CCFH=CONTINUE)、产生话单 |

容器触发通过SET CONTAINERTRIGGER配置。

### K81: 话单生成五个阶段
> 来源: 离线计费话单（GGSN_SGW-C_PGW-C）_01_10017

**原理知识**

1. **创建话单**：用户激活时或部分话单生成后触发创建
2. **生成部分话单**：满足特定条件时（时间/流量/条件变更阈值、强制产生）
3. **关闭话单**：用户去激活时生成最后话单
4. **话单编码**：ASN.1定义、BER编码，符合3GPP TS 32.298标准
5. **话单发送**：编码后封装到GTP'消息，通过Ga接口发送给CG

### K82: 话单触发条件分类
> 来源: 离线计费话单（GGSN_SGW-C_PGW-C）_01_10017

**配置知识**

部分话单触发条件：
- **按时间**：SET OFCTHRESHOLD设置的时间间隔
- **按流量**：SET OFCTHRESHOLD设置的流量阈值
- **按计费条件改变**：QoS/ULI/费率改变次数之和达到阈值；RAT/服务节点变更；MS Time Zone更新
- **强制产生**：FOC GENERATECDR命令

最后话单触发：MS/UE去激活。

### K83: 话单可靠性机制汇总
> 来源: 离线计费话单（GGSN_SGW-C_PGW-C）_01_10017

**方案设计知识**

| 机制 | 说明 |
|------|------|
| 预防重复话单 | 未收到主CG响应则发往备CG，GTP'消息携带"Send possible duplicated"标记 |
| 缓存话单信息 | 所有CG链路阻塞时按CG组/版本/IP分目录缓存，主目录charge1/备目录charge2 |
| 抑制零流量话单 | 用户未进行业务时不产生中间话单（去活话单和强制产生除外） |
| 话单池告警控制 | 池占用率达ALM-81005门限时，更新类trigger只记录不产生话单；控制用户接入数 |
| 备份计费信息 | 定时备份到CSDB_VNFC，计费POD故障时其他POD接替 |

---

## 四、SGSN话单机制

### K84: SGSN计费属性四类分类
> 来源: 离线计费话单（SGSN）_01_10018

**原理知识**

SGSN计费属性（Charging Characteristics）分为四类：
1. **普通计费属性**（Normal）：后付费用户
2. **预付费计费属性**（Prepaid）：预支付后获取服务
3. **包月制计费属性**（Flat rate）：月内固定收费，可配置不产生话单
4. **实时计费属性**（Hot billing）：短时间或流量达到某值时及时生成话单

### K85: SGSN计费属性五个来源与优先级
> 来源: 离线计费话单（SGSN）_01_10018

**配置知识**

SGSN计费属性来源优先级（从高到低）：
1. HLR签约的APN计费属性
2. HLR签约的用户计费属性
3. SGSN根据APN配置的计费属性（已激活PDP）
4. SGSN根据用户MCC/MNC配置的计费属性（漫游/拜访用户）
5. SGSN配置的本地/拜访/漫游用户缺省计费属性

### K86: SGSN话单创建点差异（Gb模式 vs Iu模式）
> 来源: 离线计费话单（SGSN）_01_10018

**隐性规则**

S-CDR话单创建点在Gb模式和Iu模式下存在关键差异：
- **MS发起PDP上下文激活**：Gb模式在发送Activate PDP Context Accept**之后**创建；Iu模式在发送**之前**创建
- **Inter RAU流程**：新SGSN发送RAU Accept后创建；旧SGSN关闭时机Gb模式为收到Cancel Location，Iu模式为收到Iu Release Complete

### K87: SGSN CG选择与PLMN隔离
> 来源: 离线计费话单（SGSN）_01_10018

**配置知识**

SGSN CG选择五个来源：PLMNCG > 计费行为CG > 计费属性CG > GGSN推荐CG > 缺省CG。

PLMN隔离机制：
- **禁止非PLMNCG**：PLMN用户话单只能发到PLMNCG
- **允许非PLMNCG**：PLMNCG全部故障时允许选择缺省CG

### K88: SGSN硬盘话单管理机制
> 来源: 离线计费话单（SGSN）_01_10018

**方案设计知识**

硬盘空间三态流转：正常 → 不足（超告警门限50%~90%）→ 满（超99%）→ 恢复（降至95%以下）→ 不足 → 正常（降至告警门限以下10%）。

硬盘话单覆盖功能（SET CHGGA: CDROVERWRITE=YES）：当使用空间达告警门限时自动删除最早生成的话单文件。按文件名编号从小到大删除，正在读写的文件跳过。

---

## 五、Gy接口在线计费原理

### K89: DCC会话与信用控制实例的关系
> 来源: 在线计费DCC会话业务流程_01_10019

**原理知识**

- DCC会话基于每个PDP上下文/EPS承载建立，承载去激活时终止
- 一个信用控制实例（RG或RG+SID）内可支持流量配额和时间配额两种类型
- 各信用控制实例的配额申请和上报独立进行，互不影响
- PGW-C在DCC消息的MSCC AVP中携带信用控制实例标识
- 所有属于该信用控制实例的业务可共享实例配额

### K90: 配额申请与上报的三种模式
> 来源: 在线计费DCC会话业务流程_01_10019

**配置知识**

PGW-C支持三种配额粒度模式（SET OLNCHGPARA配置）：

| 模式 | 申请粒度 | 上报粒度 | OCS下发粒度 | 约束 |
|------|----------|----------|-------------|------|
| 模式1 | RG | RG | RG | 无 |
| 模式2 | RG+SID | RG+SID | RG+SID | 无 |
| 模式3 | RG | RG+SID | RG | 不支持时长计费 |

**隐性规则**：模式3下以RG粒度申请、RG+SID粒度上报，OCS仍基于RG下发配额。

### K91: DCC会话创建的两种触发方式
> 来源: 在线计费DCC会话业务流程_01_10019

**方案设计知识**

| 触发方式 | 时机 | 优势 | 配置命令 |
|---------|------|------|---------|
| 用户激活触发 | 用户激活时预申请配额 | 避免用户访问业务时才申请配额导致的延迟 | SET OCSINIT控制回激活响应时是否等待CCA-I |
| 业务触发 | PDP上下文长期在线但部分时段无流量 | 避免用户长期占用配额但业务流量较少 | PGW-U感知用户行为，向PGW-C发送配额申请消息 |

### K92: DCC会话更新触发事件分类
> 来源: 在线计费DCC会话业务流程_01_10019

**原理知识**

DCC会话更新触发事件：

| 事件类型 | 触发条件 | 配置命令 |
|---------|---------|---------|
| 内部-配额 | 配额耗尽/达到阈值（TQT/VQT） | ADD DCCTEMPLATE |
| 内部-空闲 | 配额空耗定时器（QHT）超期 | ADD DCCTEMPLATE |
| 内部-新业务 | 新业务触发信用控制实例更新 | ADD DCCTEMPLATE |
| 内部-有效期 | 配额有效期（VALIDTIME）超期 | ADD DCCTEMPLATE |
| 外部-接入侧 | SGSN/S-GW地址改变、RAT改变、QoS改变、ULI改变、终端时区改变 | ADD DCCTEMPLATE |
| OCS重授权 | OCS主动发送RAR重授权请求 | — |

**关键规则**：OCS下发的触发条件优先级高于PGW-C本地配置。

### K93: 单RG单DCC会话功能（SESSIONMODE=MULTIPLE）
> 来源: 在线计费DCC会话业务流程_01_10019

**方案设计知识**

当OCS不支持在一个Gy会话中处理多个RG时，通过ADD DCCTEMPLATE的SESSIONMODE=MULTIPLE，使承载内每个RG使用独立DCC会话。

**隐性规则**：多RG场景下，去激活时必须等待所有RG对应的CCA-T响应或超时，才能完成整体去激活。

---

## 六、OCS组网与链路可靠性

### K94: OCS主备Group与负荷分担
> 来源: OCS组网和链路可靠性_01_10020

**方案设计知识**

OCS组网架构：
- 主备OCS Group之间支持热备份：主用故障时DCC会话可动态迁移到备用Group
- 同一OCS Group内采用负荷分担，三种方式（互斥）：

| 方式 | 说明 |
|------|------|
| 平均负荷分担 | 所有OCS平均分担 |
| 基于用户号段组（MSISDN/IMSI） | 同一号段组可被多个OCS绑定但优先级必须不同 |
| 基于百分比例 | 按设置的比例分担 |

**隐性规则**：百分比例和用户号段组负荷分担**不能同时使用**。

### K95: OCS选择优先级机制
> 来源: OCS组网和链路可靠性_01_10020

**方案设计知识**

OCS选择优先级从高到低：
1. PCRF下发的OCS（CCA-I消息AVP）
2. AAA Server下发的OCS（Access-Accept消息OCS-ID）
3. UserProfile配置的OCS Group（ADD UPBINDUPG匹配号段/接入类型/CC/漫游状态/位置区）
4. 本地APN配置的OCS Group
5. 本地整机配置的OCS Group
6. 基于CC属性选择OCS Group

### K96: Diameter链路可靠性
> 来源: OCS组网和链路可靠性_01_10020

**方案设计知识**

PGW-C支持与一个OCS的多个IP/SCTP端点建立多条Diameter链路，构成链路组：
- 链路组内支持**主备**和**负荷分担**模式（ADD DIAMCONNGRP的SELECTMODE参数）
- 一条链路故障时自动选择组内其他可用链路
- TCP传输：与多个IP建立多条TCP链路
- SCTP传输：与多个SCTP端点建立多条SCTP偶联

---

## 七、在线计费异常处理

### K97: CCFH异常处理机制
> 来源: 在线计费的异常处理_01_10021

**原理知识**

CCFH（Credit Control Failure Handling）三种处理方式：

| CCFH值 | 备用OCS正常时 | 备用OCS故障时 |
|--------|--------------|--------------|
| TERMINATE | 终止DCC会话，去激活承载 | 终止DCC会话，去激活承载 |
| RETRY_AND_TERM | 重传给备用OCS，保持承载 | 终止DCC会话，去激活承载 |
| CONTINUE | 重传给备用OCS，保持承载 | 终止DCC会话（不发CCR-T）、保持承载、**转离线计费** |

**隐性规则**：CONTINUE模式下需开启离线计费功能才能保持承载。转离线后的话单中增加`failureHandlingContinueFlag`标志。

CCFH可由OCS下发或本地配置，OCS下发优先级更高。

### K98: 异常返回码两层处理
> 来源: 在线计费的异常处理_01_10021

**协议知识**

CCA消息中有两层返回码：

| 层级 | 作用范围 | 配置命令 |
|------|---------|---------|
| Command层 | 针对整个承载 | ADD CMDRCACT |
| MSCC层 | 针对特定RG或RG+SID的业务 | ADD MSCCRCACT |

处理动作包括：阻塞业务、去激活承载、重定向、转离线计费等。**Command层配置的处理动作优先。**

### K99: 紧急放通（FHBYPASS）
> 来源: 在线计费的异常处理_01_10021

**隐性规则**

SET FHBYPASS仅用于故障场景下的紧急处理：
- 仅适用于OCS故障（非异常结果码场景）和Command层异常结果码
- **不支持MSCC层异常结果码的一键放通**
- 由于影响用户计费方式，**必须在获得客户书面认可后方可使用**

### K100: 在线计费异常处理全景
> 来源: 在线计费的异常处理_01_10021

**原理知识**

| 异常场景 | 配置命令 | 核心处理 |
|---------|---------|---------|
| OCS链路Down（激活时） | SET OCSDOWNACTION | PERMIT或FORBIDDEN |
| OCS链路Down（DCC会话中） | ADD DCCTEMPLATE(CCFH) | TERMINATE/RETRY_AND_TERM/CONTINUE |
| Tx定时器超时 | SET TXTIMER + CCFH | 同上 |
| 异常返回码（Command层） | ADD CMDRCACT | 阻塞/去激活/重定向/转离线 |
| 异常返回码（MSCC层） | ADD MSCCRCACT | 同上 |
| 紧急放通 | SET FHBYPASS | 仅OCS故障+Command层，需书面认可 |

---

## 八、在线计费可选功能

### K101: WAL过载保护
> 来源: 在线计费可选功能介绍_01_10023

**方案设计知识**

PGW-C提供WAL（Windows Access Limit）过载保护：当检测出OCS当前待处理负荷超出WAL值（ADD OCS命令配置）时，将该OCS置为不可用，将后续负荷转移到其他OCS。

### K102: 费率切换（Tariff Switching）
> 来源: 在线计费可选功能介绍_01_10023

**原理知识**

PGW-C支持接受OCS下发的费率切换时间点，对切换前后进行独立的信用控制和消费统计：
- **单配额方式**：OCS在CCA中仅下发费率切换前的配额
- **双配额方式**：OCS在CCA中可下发费率切换前后的配额

目的：避免到费率切换点集中向OCS申请配额引发网络信令风暴。

### K103: 重定向三种触发方式
> 来源: 在线计费可选功能介绍_01_10023

**方案设计知识**

| 方式 | 触发条件 | 机制 |
|------|---------|------|
| FUI触发 | 用户配额耗尽后 | OCS在CCA中携带FUI/FUA AVP，PGW-C执行重定向 |
| 返回码触发 | OCS返回异常返回码 | 根据异常返回码配置的动作执行重定向 |
| 一次重定向 | OCS主动触发 | OCS在MSCC层携带成功结果码+足量配额+Redirect-Server AVP |

### K104: 多字典与Default Quota
> 来源: 在线计费可选功能介绍_01_10023

**配置知识**

**多字典**：Gy接口支持加载两套数据字典，可基于DCC模板设置使用的数据字典。同一局点多套字典的session-id填充格式必须相同。

**Default Quota**：为用户提供默认配额，在配额申请期间（新业务触发或配额耗尽）用户可先使用默认配额保证业务不中断。OCS下发配额成功后，从新配额中扣除使用量。

---

## 九、在线计费自动回切

### K105: 链路故障恢复场景（立即回切）
> 来源: 在线计费自动回切业务流程_01_10022

**方案设计知识**

OCS链路故障导致用户转离线后，链路恢复时**立即回切**：
1. 链路恢复后，立即向OCS发送CCR-I创建新DCC会话
2. 离线计费立即产生话单
3. 恢复正常在线计费

**隐性规则**：链路恢复场景是立即回切（无定时器等待），与Tx超时等场景的定时回切不同。

### K106: 定时尝试回切场景
> 来源: 在线计费自动回切业务流程_01_10022

**方案设计知识**

非链路故障导致的转离线（Tx超时、OCS过载/异常返回码、激活选不到OCS等），采用定时尝试回切：
1. 转离线后，在holding-time内启动Recover-Timer
2. Recover-Timer超时 → 发送CCR-I尝试创建新DCC会话
3. 若Tx超时未收到CCA-I → 回切不成功 → 重启Recover-Timer
4. 收到CCA-I → 回切成功 → 离线计费产生话单 → 恢复在线计费

---

## 十、相关术语

### K107: CC（计费属性）
> 来源: CC_01_10011

**原理知识**

CC（Charging Characteristics）是对用户采用的计费类型属性，由16位字符串构成。CC决定会话的具体计费方式。

**CC来源优先级**：User Profile > APN下配置 > 全局配置 > 缺省(普通计费)

CC支持三类用户：本地用户、漫游用户、拜访用户，每类可独立配置计费行为。

CC行为表中Behaviour index关联到：Default charging method、Charging service、Primary/Secondary CHF addresses、TimeLimit/VolLimit per PDU session、ChangeCondition、Tariff times等。

参考协议：3GPP TS 32.2 Chapter 5.1.2.2.7, 3GPP TS 32.255 Chapter A.1

### K108: DCC（Diameter信用控制协议）
> 来源: DCC_01_10014

**协议知识**

DCC（Diameter Credit Control）是在Diameter协议基础上扩展的应用协议，PGW-C为DCC客户端，OCS为DCC服务器。

核心机制：
- DCC会话基于每个PDP上下文/EPS承载建立
- 消息序列：CCR/CCA-I（Initial）→ CCR/CCA-U（Update）→ CCR/CCA-T（Terminate）
- 同一DCC会话支持多业务信用控制，每个Credit Instance通过MSCC AVP组承载
- 信用控制实例粒度：RG 或 RG+SID

与融合计费对比：DCC基于Diameter，5G N40基于HTTP/RESTful。但信用控制逻辑模型（Initial/Update/Terminate、多业务MSCC）概念上延续到融合计费的Charging Data Request/Response。

### K109: RG（费率组）
> 来源: RG_01_10010

**原理知识**

RG（Rating Group）是使用相同计费类型的服务集合。费率是每个业务的费用指数，根据用户或业务套餐签约情况决定。

关键规则：
- Gy接口上PGW-C按RG粒度向OCS申请配额，OCS按RG粒度下发配额
- 在线计费使用统一费率时，必须为用户配置默认费率组（Default Rating Group）
- PGW-C可按RG或RG+SID粒度上报配额

### K110: SID（业务识别标识）
> 来源: SID_01_10013

**原理知识**

SID（Service Identifier）代表一条业务数据流，是RG的子集。

核心规则：
- SID必须和绑定的RG一起使用，不能单独使用
- PCC规则中PCRF可随时下发并激活、更改或去激活SID
- RG+SID共同决定数据流的具体计费模型（基于流量、时间、事件次数）

RG与SID关系：RG可包含多个SID。例如RG=7（某公司免流）下SID=11/12/13分别对应不同APP。

### K111: URR（使用量上报规则）
> 来源: URR_01_10012

**原理知识**

URR（Usage Reporting Rule）是控制面指示用户面上报流量/时长/事件等网络资源使用情况的规则。

核心机制：
- URR在PFCP会话建立/修改请求中下发
- 测量维度：流量、时长、事件
- 上报触发：测量达到阈值、周期性上报、Reporting Triggers IE定义的触发器、控制面请求立即报告

**关键隐性规则**：
- PGW-C维护RG与URR ID之间的映射关系
- 所有RG都有对应的URR ID
- 但URR并不都是用作计费（存在非计费URR ID没有对应的RG）
- 即：RG → URR ID 是一对一映射，但 URR ID → RG 不是一一对应

参考协议：3GPP TS 29.244, Chapter 5.2.2

### K112: 话单/CDR（计费数据记录）
> 来源: 话单_01_10009

**原理知识**

话单（CDR）是离线计费记录用户业务使用情况的最小单元。

关键规则：
- 话单基于每个PDP上下文/EPS承载生成
- 一个承载生命周期内可产生多张话单（Partial CDR）
- Partial CDR通过record-sequence-number关联

与融合计费对比：4G Ga接口话单基于PDP上下文/EPS承载粒度，5G N40对应Charging Data Request，粒度变为PDU Session/SMF。

---

## 十一、跨术语关键隐性规则汇总

### K113: Ga/Gy术语间关联规则
> 来源: 综合6篇术语文档

**隐性规则**

1. **RG是配额申请粒度，URR是用量计量粒度**：Gy按RG向OCS申请/下发配额，N4按URR向PGW-U下发计量规则，PGW-C负责RG↔URR ID映射。

2. **SID不能独立使用**：SID必须与RG绑定，DCC信用控制实例粒度可以是RG或RG+SID。

3. **CC决定一切计费行为**：CC通过优先级链确定后，决定在线/离线、CHF地址、配额阈值等全部计费参数。

4. **DCC会话 = 承载生命周期**：一个PDP上下文/EPS承载对应一个DCC会话。

5. **部分话单机制**：一个承载生命周期内可产生多张Partial CDR，这是离线计费处理长时间会话和配额分段上报的基本方式。

---

## 知识统计

| 类别 | 数量 |
|------|------|
| 原理知识 | 22 (K70, K72, K73, K79, K80, K81, K84, K89, K92, K97, K100, K102, K107, K109, K110, K111, K112) |
| 方案设计知识 | 10 (K75, K77, K86, K88, K91, K93, K94, K96, K101, K105, K106) |
| 配置知识 | 10 (K71, K76, K78, K82, K85, K87, K90, K98, K104) |
| 协议知识 | 5 (K74, K108, K98, K79) |
| 隐性规则 | 6 (K79, K90, K97, K99, K105, K113) |
| **合计** | **44条 (K70-K113)** |
