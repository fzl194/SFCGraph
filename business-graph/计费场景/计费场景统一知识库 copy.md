# 5G Core 计费场景统一知识库

> 融合日期: 2026-06-04
> 来源: 12份知识草稿 (draft-batch-01 ~ draft-batch-07)，原始来源555+篇UNC产品文档
> 编号范围: K001-K255
> 分类标签: [原理] [配置] [方案设计] [隐性规则] [协议] [运维] [故障案例]

## 章节索引

| 章 | 主题 | 编号段 | 条目数 |
|----|------|--------|--------|
| 一 | 计费系统架构 | K001-K011 | 11 |
| 二 | 计费方式与维度 | K012-K019 | 8 |
| 三 | 核心术语定义 | K020-K037 | 18 |
| 四 | Gy接口与DCC协议 | K038-K051 | 14 |
| 五 | Ga接口与CG | K052-K058 | 7 |
| 六 | 会话流程中的计费交互 | K059-K062 | 4 |
| 七 | Nchf融合计费服务(N40) | K101-K121 | 21 |
| 八 | PFCP/N4接口与URR | K122-K135 | 14 |
| 九 | Gx/PCC策略与计费 | K136-K146 | 11 |
| 十 | 规则匹配与业务识别 | K147-K161 | 15 |
| 十一 | Usage Monitoring与FUP | K162-K168 | 7 |
| 十二 | 融合计费配置全景 | K201-K213 | 13 |
| 十三 | 计费三件套配置 | K214-K223 | 10 |
| 十四 | PCF策略配置 | K224-K228 | 5 |
| 十五 | 方案设计知识 | K229-K234 | 6 |
| 十六 | 特殊场景 | K235-K241 | 7 |
| 十七 | 故障案例与运维 | K242-K255 | 14 |
| **合计** | | **K001-K255** | **185** |

---


## 第一章：计费系统架构

### K001: 5G计费系统演进路线 [原理]
> 来源: K01

4G及NSA网络中：
- 离线计费：收集用户计费信息生成话单，通过Ga接口访问CG
- 在线计费：收集计费信息及信用控制，通过Gy接口访问OCS

5G SA网络中：
- CHF（Charging Function）融合CG的CGF（计费网关功能）和OCS的ABMF（账户结余管理）+RF（批价功能）
- Nchf接口融合Ga口和Gy口
- **计费本质不变**：搜集流量、时长等信息上报，并对用户进行信用控制

融合计费的优势：
- 配合5GC的SBA架构，利于IT系统云化
- CHF既做配额管理又生成话单，数据归一
- 避免离线与在线计费分离时结果可能不一致的问题

### K002: 计费功能实体及其角色 [原理]
> 来源: K32, K42

| 功能实体 | 作用 |
|---------|------|
| CTF | 计费触发功能，检查流量/时长等业务使用情况，产生计费事件。在线计费余额不足时中断服务。内置于PGW-C/SMF。 |
| ABMF | 管理用户账户余额，完成扣费和充值 |
| RF | 批价功能，将费用转换成流量/时长等配额信息 |
| OCF | 在线计费功能，通过Gy接口与CTF交互，通过Rc/Re接口与ABMF/RF交互 |
| CDF | 计费数据功能，从CTF收集计费信息生成CDR，通过Ga接口传输给CGF |
| CGF | 计费网关功能，话单错误检查、预处理和持久存储，通过Bx接口发送至BD |
| BD | 运营商计费营帐系统 |

CHF融合了：ABMF + RF + CGF → 统一的服务化接口

### K003: 5GC计费架构中的网元角色 [原理]
> 来源: K03, K42

| 网元 | 融合计费中的角色 |
|------|----------------|
| SMF | Nchf服务使用者；选择CHF；处理计费参数；通过N4向UPF下发配额；通过N7与PCF交互；监控在线配额 |
| CHF | Nchf服务提供者；在线：批价/扣费/配额下发；离线：参数下发；处理用量上报生成CHF-CDR；提供重授权触发条件 |
| PCF | 通过N7接口进行计费策略控制；可下发CHF地址 |
| UPF | 接收PDR/URR规则或预定义规则；根据规则上报计费信息 |
| UDM | 通过CC计费特性传递签约数据到SMF |
| NRF | NF注册/发现；SMF通过NRF发现CHF |

### K004: 三种计费系统对比 [原理]
> 来源: K33

| 计费系统 | 接口 | 计费功能 | 部署方式 |
|---------|------|---------|---------|
| 离线计费系统 | Ga | 仅离线计费，指定时间更新余额 | 网络侧 |
| 在线计费系统 | Gy | 仅在线计费，实时监控余额 | 支撑系统侧 |
| 融合计费系统 | Nchf(N40) | 离线+在线 | 支撑系统侧 |

### K005: NCG引入背景和功能 [方案设计]
> 来源: K37

引入NCG解决的问题：
1. 避免对计费域大规模改造
2. 网络侧有离线话单网元，CHF异常时NCG可接替，防止计费损失

NCG功能：离线计费+在线计费+融合计费，支持将计费信息转换为话单文件本地存储，并提供实时话单。

NCG内部模块：
- AGF：接收PGW-C/SMF的计费信息，在线/融合转发给CHF，离线转发给CDF
- CDF：从AGF收集计费信息，生成CDR
- CGF：合并/过滤/优化CDR，传输给BD

### K006: 方案一 — 未部署NCG（SMF直连CHF）[方案设计]
> 来源: K36

组网：SMF+PGW-C → Nchf → CHF(OCS)

特点：
- 最简架构，SMF通过Nchf服务化接口与CHF直连
- 融合计费（离线+在线）
- 需要对计费域CHF(OCS)做改造
- 5G SA场景下无离线话单网元，CHF异常时可能导致计费损失

### K007: 方案二 — NCG + 传统Ga/Gy接口 [方案设计]
> 来源: K38

适用场景：5G SA前期，计费网络改造较慢，仍需依赖传统Ga/Gy接口

组网：SMF → Ga → NCG(离线)；SMF → Gy → OCS(在线)

特点：
- NCG仅承担离线计费（替代传统CG）
- OCS承担在线计费
- 不需要服务化接口改造

### K008: 方案三 — NCG + 服务化接口纯离线 [方案设计]
> 来源: K39

适用场景：5G SA前期，OCS未完成Nchf改造，作为过渡方案

组网：SMF → Nchf → NCG(离线)

特点：
- 基于Nchf服务化接口
- NCG承担离线计费
- 后期OCS改造完成后可升级为方案四（离线+在线）

### K009: 方案四 — NCG + 服务化接口离线+在线 [方案设计]
> 来源: K40

组网：SMF → Nchf → NCG → Nchf → CHF(OCS)(在线)；NCG本地处理(离线)

两阶段演进：
- **阶段一**：CHF(OCS)仅在线计费，NCG承担离线+转发在线+CHF故障时接替
- **阶段二**：CHF(OCS)同时支持在线和离线，NCG仅传递+异常时接替

可靠性：AGF发送在线话单给CHF后，也转发给CDF存储，保证计费可靠性

### K010: 方案五 — NCG + 融合接口（Ga/Gy + Nchf）[方案设计]
> 来源: K41

适用场景：CHF(OCS)完成Nchf改造后，同时支持传统接口和服务化接口

组网：
- 5G场景：SMF → Nchf → NCG → Nchf → CHF(OCS)
- 2/3/4G场景：SMF → Ga → NCG(离线)；SMF → Gy → CHF(OCS)(在线)

特点：
- 同时支持传统接口和服务化接口
- NCG承担5G离线计费 + 2/3/4G离线计费
- CHF(OCS)承担在线计费

### K011: 华为三种融合计费方案汇总 [方案设计]
> 来源: K43

| 方案 | 描述 | 可靠性特点 |
|------|------|-----------|
| 方案一 | CCS部署在计费域，无NCG | 网络侧无话单，可靠性低 |
| 方案二 | NCG(网络侧) + CCS(计费域) | NCG转发到CCS；NCG保存全量话单；CHF异常时NCG代应答 |
| 方案三 | NCG(网络侧) + OCS(计费域) | 离线由NCG完成，在线由OCS完成；OCS改造量减少40% |

### K012: 离线计费端到端架构 [原理]
> 来源: K70

离线计费端到端流程：GGSN-U/SGW-U/PGW-U收集用户业务使用情况 → 控制面按计费规则格式化为话单 → 通过Ga接口发送到CG → CG完成存储/标准化 → 定期上传BS → 运营商定期结算。

涉及网元：SGSN、GGSN-C/SGW-C/PGW-C、GGSN-U/SGW-U/PGW-U、CG、BS、OCS。

---

## 第二章：计费方式与维度

### K013: 计费粒度分类 [原理]
> 来源: K06

| 计费粒度 | 说明 | 别名 |
|---------|------|------|
| PDU会话计费 | 不区分业务，所有业务统一费率 | **普通计费** |
| 业务流计费 | 基于业务差别计费，不同业务不同费率(Rating Group) | **内容计费** |
| QoS flow计费 | 基于QoS流计费，不同QoS流不同费率 | **漫游计费** |

### K014: 计费方式的多维度分类 [原理]
> 来源: K34

| 维度 | 计费方式 | 说明 |
|------|---------|------|
| 实时监控 | 离线计费 | 基于离线计费架构 |
| 实时监控 | 在线计费 | 基于在线计费架构 |
| 实时监控 | 融合计费 | 从SMF是否申请配额维度分在线/离线 |
| 业务维度 | 普通计费 | 基于承载/PDU会话，不区分业务，统一费率 |
| 业务维度 | 内容计费 | 基于业务差别计费，不同业务不同费率 |
| 资源统计 | 流量计费 | 按访问业务的流量 |
| 资源统计 | 时长计费 | 按业务使用时间 |
| 资源统计 | 事件计费 | 按访问业务次数 |

### K015: 离线计费与在线计费的本质区别 [原理]
> 来源: K07

- **在线计费**：计费会话创建时，SMF**需到CHF申请业务的配额和相关计费参数**
- **离线计费**：计费会话创建时，SMF**只需到CHF申请相关计费参数，无需申请配额**

同一PDU会话中可同时存在在线和离线计费的数据流（融合计费场景）。

现阶段运营商基本按用户区分：部分用户只做在线，部分只做离线。
后续可能按业务区分：正常业务在线计费，免费业务离线计费（仅用于话单核对）。

### K016: 计费方式组合规则 [隐性规则]
> 来源: K35, K07

- 离线计费和在线计费**可以共存**（融合计费场景）
- 普通计费和内容计费**不可共存**
- 流量计费、时长计费和事件计费**可以共存**

融合计费中在线/离线的本质区分：
- **在线计费**：SMF向CHF请求配额，配额耗尽时申请新配额，配额不足时可停止业务
- **离线计费**：SMF不请求配额，仅在上报阈值、业务结束时上报使用情况

### K017: 5G NSA场景计费选择 [方案设计]
> 来源: K02

NSA场景下两种选择：
1. 对2/3/4/5G流量统一计费（**推荐**）
2. 对5G流量单独计费（由gNodeB统计，通过控制面上报CG）

单独5G计费的限制：
- 不支持在线计费
- 不支持基于内容的计费
- 推荐统一计费的原因：基于内容的差异化计费是主流

### K018: Nchf服务化接口操作 [协议]
> 来源: K04

| 服务操作 | 功能 | 发起方 | 对应融合计费消息 | 对应4G消息 |
|---------|------|--------|----------------|-----------|
| Nchf_ConvergedCharging_Create | 计费会话建立 | SMF | Charging Data Request/Response [Initial] | CCR-I/CCA-I |
| Nchf_ConvergedCharging_Update | 计费会话更新 | SMF | Charging Data Request/Response [Update] | CCR-U/CCA-U |
| Nchf_ConvergedCharging_Release | 计费会话结束 | SMF | Charging Data Request/Response [Termination] | CCR-T/CCA-T |
| Nchf_ConvergedCharging_Notify | 重授权/去活通知 | CHF | Charging Notify Request/Response | RAR/RAA |

### K019: 在线/离线计费方式选择的优先级机制 [配置]
> 来源: K71

在线计费来源优先级：PCRF下发 > AAA Server下发 > 本地配置（UserProfile > APN > CC）

离线计费来源优先级：PCRF下发 > 本地配置（UserProfile > APN > CC）

PCRF在CCA-I消息中通过Online AVP指示在线计费；RADIUS Server通过Access-Accept携带OCS-ID指示在线计费。

计费接口选择优先级：ADD APNCHGMODE（基于APN）> SET CHGMODE（全局）。

---

## 第三章：核心术语定义

### K020: CC (Charging Characteristics / 计费属性) [原理]
> 来源: K44, K107

CC是16位字符串，映射到行为索引表，定义：
- 默认计费方法（在线/离线/融合）
- CHF地址
- 每PDU会话的TimeLimit/VolLimit
- 变更条件限制
- 资费时间

**CC优先级（从高到低）：**
1. UserProfile（PCF下发）
2. DNN配置
3. 全局配置
4. 默认值

**CC来源：** 首先来自DNN订阅数据(UDM)。DNN无CC则回退到SMF本地配置。

**三种用户类型：** 本地用户(归属PLMN)、漫游用户、拜访用户

CC行为表中Behaviour index关联到：Default charging method、Charging service、Primary/Secondary CHF addresses、TimeLimit/VolLimit per PDU session、ChangeCondition、Tariff times等。

参考协议：3GPP TS 32.2 Chapter 5.1.2.2.7, 3GPP TS 32.255 Chapter A.1

### K021: RG (Rating Group / 计费费率组) [原理]
> 来源: K45, K109

- 共享相同计费类型/费率的一组服务
- SMF以RG粒度向CHF请求配额
- CHF以RG粒度授予配额和计费参数
- SMF维护RG→URR ID映射
- **所有RG都有URR ID，但并非所有URR ID都有RG**（非计费用途的URR无RG）

PCF可在PDU会话生命周期内更改：RG、SID、Sponsor ID、Application Service Provider ID、Policy and Reporting priority

在线计费使用统一费率时，必须为用户配置默认费率组（Default Rating Group）。

### K022: SID (Service Identifier / 业务识别标识) [原理]
> 来源: K46, K110

- 代表一个业务数据流，是RG的子集
- 必须与绑定的RG一起使用，不能单独使用
- 一个RG可包含多个SID
- 计费模型（流量/时长/事件）由RG+SID共同决定
- PCC规则中PCRF可随时下发并激活、更改或去激活SID

RG与SID关系示例：RG=7（某公司免流）下SID=11/12/13分别对应不同APP。

### K023: URR (Usage Reporting Rule / 使用量上报规则) [原理]
> 来源: K47, K111

SMF通过N4(PFCP)向UPF下发的规则，指示UPF测量和报告网络资源使用情况。
- 测量维度：流量(Volume)、时长(Duration)、事件(Event)
- 上报触发：阈值到达、周期性、应请求上报

**URR关键参数：**
- URR ID, Measurement Method, Reporting Triggers
- Volume Quota, Time Quota, Volume Threshold, Time Threshold
- Linked URR ID（关联上报）, Measurement Information（ISTM等）

**关键隐性规则**：
- PGW-C/SMF维护RG与URR ID之间的映射关系
- 所有RG都有对应的URR ID
- 但URR并不都是用作计费（存在非计费URR ID没有对应的RG）
- 即：RG → URR ID 是一对一映射，但 URR ID → RG 不是一一对应

参考协议：3GPP TS 29.244, Chapter 5.2.2

### K024: QCT (Quota Consumption Time / 配额空耗时间) [原理]
> 来源: K48

设置阈值（秒），确定数据包间空闲期是否算应计费时间。

**时长计费四种模式：**
1. **连续时长计费(CTP)**: QCT=0，从首包到尾包所有时间都计费
2. **QCT时长计费**: QCT>0，空闲≤QCT=应计费；空闲>QCT=仅QCT持续时间应计费
3. **CTP (Continuous-Time-Period)**
4. **DTP (Discrete-Time-Period)**

**QCT机制：** 空闲时启动QCT计时器。QCT到期前有数据包到达→重置；QCT到期→超出部分不计费。

在线计费连续模式：从SMF创建配额开始，无论有无流量，直到用户去活。
离线计费连续模式：从UPF接收第一个业务数据包开始。

### K025: QHT (Quota Holding Time / 配额空闲时间) [原理]
> 来源: K49

用户无数据包时UPF启动计时器（秒）。QHT到期→SMF向CHF报告计费信息。
- **在线计费**：QHT到期=SMF不请求配额，配额仅在下一次业务活动时请求
- **离线计费**：QHT到期=触发关闭当前业务容器
- QHT=0：禁用
- 适用于流量和时长计费

### K026: Container (容器 / Used Unit Container) [原理]
> 来源: K50

CDR中的容器，记录计费条件更改信息。一个CDR可包含多个容器。

**两种报告类别：**
- **即时上报**：立即关闭计数器，SMF立即发送Charging Data Request，打开新计数器
- **延迟上报**：关闭计数器存储数据，在下一条Charging Data Request中发送，打开新计数器

**PDU容器信息字段：** Time of First/Last Usage, QoS Information, User Location, UE Time Zone, RAT Type, Serving NF ID, Charging Rule Base Name, 3GPP PS Data Off Status 等

### K027: CAR双令牌桶机制 [原理]
> 来源: K263, K264

流量监管功能通过CAR（Committed Access Rate，承诺访问速率）限制报文流量。CAR使用双令牌桶模型：

**报文处理流程**:
1. 报文首先进入令牌桶P（峰值桶），速率PIR，溢出报文标记为**red**
2. 通过令牌桶P的报文进入令牌桶C（承诺桶），速率CIR，溢出报文标记为**yellow**
3. 通过令牌桶C的报文标记为**green**

**UDG染色处理**:
- red：直接丢弃
- yellow：拥塞时首先丢弃，不拥塞时高优先级可通过
- green：丢弃优先级最低

**四个核心参数：**

| 参数 | 全称 | 含义 |
|------|------|------|
| CIR | Committed Information Rate（承诺信息速率） | 向令牌桶C投放令牌的速率，即允许转发报文的平均速率 |
| CBS | Committed Burst Size（承诺突发尺寸） | 令牌桶C的容量，即允许通过的最大报文长度 |
| PIR | Peak Information Rate（峰值信息速率） | 向令牌桶P投放令牌的速率，即峰值允许转发报文的平均速率 |
| PBS | Peak Burst Size（峰值突发尺寸） | 令牌桶P的容量，即峰值允许通过的最大报文长度 |

关系：CIR < PIR，CBS和PBS分别对应两个令牌桶的容量。

---

## 第四章：Gy接口与DCC协议

### K028: Gy接口完整消息列表与方向 [协议]
> 来源: K315

Gy接口为GGSN/P-GW和OCS间的信令面接口，基于Diameter协议。完整消息列表如下：

| 消息 | 方向 | 作用 |
|------|------|------|
| CCR (Credit-Control-Request) | P-GW -> OCS | 为用户请求计费控制信息 |
| CCA (Credit-Control-Answer) | OCS -> P-GW | 返回CCR消息的请求结果 |
| RAR (Re-Auth-Request) | OCS -> P-GW | 为用户请求重新认证/授权服务 |
| RAA (Re-Auth-Answer) | P-GW -> OCS | 返回RAR消息的请求结果 |
| ASR (Abort-Session-Request) | OCS -> P-GW | 发送会话终止信息 |
| ASA (Abort-Session-Answer) | P-GW -> OCS | 返回ASR消息的请求结果 |
| DPR (Disconnect-Peer-Request) | P-GW -> OCS | 通知对端将断开链路 |
| DPA (Disconnect-Peer-Answer) | OCS -> P-GW | 返回DPR消息的请求结果 |
| CER (Capabilities-Exchange-Request) | P-GW -> OCS | 链路维护消息 |
| CEA (Capabilities-Exchange-Answer) | OCS -> P-GW | 返回CER消息的请求结果 |
| DWR (Device-Watchdog-Request) | P-GW -> OCS | 心跳检测消息 |
| DWA (Device-Watchdog-Answer) | OCS -> P-GW | 返回DWR消息的请求结果 |

**计费相关**：CCR/CCA是核心计费交互对，对应CC-Request-Type的initial/update/terminate三种类型。RAR/RAA用于OCS发起重授权（对应Reporting-Reason=FORCED_REAUTHORISATION）。ASR/ASA用于OCS强制终止会话。DPR/DPA/CER/CEA/DWR/DWA为Diameter基础链路维护消息。

### K029: Gy接口Diameter Result-Code错误码分类体系 [协议]
> 来源: K316

Result-Code AVP编码268，Unsigned32类型，由千位数字标识错误分类：

| 分类 | 含义 | 关键错误码 |
|------|------|-----------|
| 1xxx | Informational（信息） | - |
| 2xxx | Success（成功） | 2001 DIAMETER_SUCCESS |
| 3xxx | Protocol Errors（协议错误） | 3001 COMMAND_UNSUPPORTED, 3002 UNABLE_TO_DELIVER, 3004 TOO_BUSY, 3007 APPLICATION_UNSUPPORTED |
| 4xxx | Transient Failures（临时失败） | 4001 AUTHENTICATION_REJECTED, 4010 END_USER_SERVICE_DENIED, 4011 CREDIT_CONTROL_NOT_APPLICABLE, **4012 CREDIT_LIMIT_REACHED** |
| 5xxx | Permanent Failure（永久失败） | 5001 AVP_UNSUPPORTED, 5002 UNKNOWN_SESSION_ID, 5003 AUTHORIZATION_REJECTED, 5004 INVALID_AVP_VALUE, 5005 MISSING_AVP, 5006 RESOURCES_EXCEEDED, 5030 USER_UNKNOWN, **5031 RATING_FAILED** |

**计费相关**：
- 4012 CREDIT_LIMIT_REACHED：用户信用额度已用完，是计费控制的核心错误码
- 4010 END_USER_SERVICE_DENIED：OCS拒绝用户业务访问
- 4011 CREDIT_CONTROL_NOT_APPLICABLE：用户不适用在线计费
- 5030 USER_UNKNOWN：OCS不识别该用户
- 5031 RATING_FAILED：OCS对用户进行批价失败
- 非成功Result-Code必须包含Error-Reporting-Host AVP
- 定义之外的结果编码必须处理为永久失败

### K030: DCC会话与信用控制实例的关系 [原理]
> 来源: K89, K108

DCC（Diameter Credit Control）是在Diameter协议基础上扩展的应用协议，PGW-C为DCC客户端，OCS为DCC服务器。

核心机制：
- DCC会话基于每个PDP上下文/EPS承载建立，承载去激活时终止
- 一个信用控制实例（RG或RG+SID）内可支持流量配额和时间配额两种类型
- 各信用控制实例的配额申请和上报独立进行，互不影响
- PGW-C在DCC消息的MSCC AVP中携带信用控制实例标识
- 所有属于该信用控制实例的业务可共享实例配额

消息序列：CCR/CCA-I（Initial）→ CCR/CCA-U（Update）→ CCR/CCA-T（Terminate）

与融合计费对比：DCC基于Diameter，5G N40基于HTTP/RESTful。但信用控制逻辑模型（Initial/Update/Terminate、多业务MSCC）概念上延续到融合计费的Charging Data Request/Response。

### K031: DCC会话创建的两种触发方式 [方案设计]
> 来源: K91

| 触发方式 | 时机 | 优势 | 配置命令 |
|---------|------|------|---------|
| 用户激活触发 | 用户激活时预申请配额 | 避免用户访问业务时才申请配额导致的延迟 | SET OCSINIT控制回激活响应时是否等待CCA-I |
| 业务触发 | PDP上下文长期在线但部分时段无流量 | 避免用户长期占用配额但业务流量较少 | PGW-U感知用户行为，向PGW-C发送配额申请消息 |

### K032: DCC会话更新触发事件分类 [原理]
> 来源: K92

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

### K033: 单RG单DCC会话功能（SESSIONMODE=MULTIPLE）[方案设计]
> 来源: K93

当OCS不支持在一个Gy会话中处理多个RG时，通过ADD DCCTEMPLATE的SESSIONMODE=MULTIPLE，使承载内每个RG使用独立DCC会话。

**隐性规则**：多RG场景下，去激活时必须等待所有RG对应的CCA-T响应或超时，才能完成整体去激活。

### K034: CC-Request-Type四种取值与P-GW实际支持 [协议]
> 来源: K317

CC-Request-Type AVP编码416，枚举类型，所有CCR消息必须携带：

| 取值 | 枚举值 | 含义 | 使用场景 |
|------|--------|------|---------|
| INITIAL_REQUEST | 1 | 发起CC会话 | 用户首次激活、PDP上下文建立、IP CAN会话建立 |
| UPDATE_REQUEST | 2 | 更新已存在的CC会话 | 配额/有效期到达需重授权、特定业务事件触发 |
| TERMINATION_REQUEST | 3 | 终止CC会话 | PDP上下文释放、IP CAN会话终止 |
| EVENT_REQUEST | 4 | 一次性事件请求 | 不保留CC会话状态时使用，必须同时携带Requested-Action AVP |

**P-GW当前仅支持三种**：initial、update、terminate（不支持EVENT_REQUEST）。

### K035: Multiple-Services-Credit-Control (MSCC) AVP完整结构 [协议]
> 来源: K318

MSCC AVP编码456，Grouped类型，是多重业务特性组合时非独立配额的控制标记。完整结构：

```
Multiple-Services-Credit-Control ::= < AVP Header: 456 >
  [ Granted-Service-Unit ]         -- OCS下发的授权配额
  [ Requested-Service-Unit ]       -- P-GW请求的配额
  *[ Used-Service-Unit ]           -- 已使用的配额上报
  [ Tariff-Change-Usage ]          -- 费率变化使用量标识
  *[ Service-Identifier ]          -- 业务标识
  [ Rating-Group ]                 -- 费率组
  *[ G-S-U-Pool-Reference ]       -- 信用池引用
  [ Result-Code ]                  -- 该MSCC的结果码
  [ Final-Unit-Indication ]        -- 最后单元指示
  [ Time-Quota-Threshold ]         -- 时间配额门限
  [ Volume-Quota-Threshold ]       -- 流量配额门限
  [ Unit-Quota-Threshold ]         -- 单元配额门限
  [ Quota-Holding-Time ]           -- 配额保持时间
  [ Quota-Consumption-Time ]       -- 配额消费时间
  *[ Reporting-Reason ]            -- 上报原因
  [ Trigger ]                      -- 重授权触发条件
  *[ Envelope ]                    -- 信封
  [ Envelope-Reporting ]           -- 信封上报
  [ Time-Quota-Mechanism ]         -- 时间配额机制
```

**关键规则**：
- Service-Identifier与Rating-Group同时下发时，优先采用Service-Identifier
- 仅下发Rating-Group时，MSCC关联的所有业务都采用该费率组
- G-S-U-Pool-Reference中必须携带实际业务标识（如Unit-Type为TIME则必须携带CC-Time）
- MSCC仅在多重业务采用非独立信用池时生效
- 参见: 3GPP TS 32.299 Va.4.0 7.1.9章节

### K036: Granted-Service-Unit (GSU) AVP子信元详解 [协议]
> 来源: K319

GSU AVP编码431，Grouped类型，指示业务释放或需发送新CCR前可用的资源总量。P-GW只有重新收到CCA消息时才能明确配额类型。

```
Granted-Service-Unit ::= < AVP Header: 431 >
  [ Tariff-Time-Change ]            -- 费率切换时间点
  [ CC-Time ]                       -- 授权时长（秒）
  [ CC-Total-Octets ]               -- 授权总字节数
  [ CC-Input-Octets ]               -- 授权上行字节数
  [ CC-Output-Octets ]              -- 授权下行字节数
  [ CC-Service-Specific-Units ]     -- 业务特定单元
```

**关键行为**：
- 如果CCA中未携带GSU（如OCS判定用户已终止业务访问），OCS在用户账户中预支配额
- 如果GSU不可接受，P-GW可通过Termination-Cause AVP携带DIAMETER_BAD_ANSWER终止业务承载
- CC-Input-Octets + CC-Output-Octets 与 CC-Total-Octets 可以组合使用
- 参见: RFC 4006 8.17章节

### K037: Final-Unit-Indication与三种Final-Unit-Action [协议]
> 来源: K320

Final-Unit-Indication AVP编码430，Grouped类型，表示GSU中包含的是最后一个单元。当这些单元截止，P-GW执行Final-Unit-Action指示的动作。

```
Final-Unit-Indication ::= < AVP Header: 430 >
  { Final-Unit-Action }              -- 必选：终止动作
  *[ Restriction-Filter-Rule ]       -- 限制过滤规则
  *[ Filter-Id ]                     -- 过滤器ID
  [ Redirect-Server ]                -- 重定向服务器
```

三种Final-Unit-Action及配套要求：

| 动作 | 含义 | 必须同时携带的AVP |
|------|------|-----------------|
| TERMINATE | 终止业务 | 无（不携带其他AVP） |
| REDIRECT | 重定向到指定服务器 | Redirect-Server（必须）+ Restriction-Filter-Rule/Filter-Id（可选，限制非重定向地址的访问） |
| RESTRICT_ACCESS | 限制访问 | Restriction-Filter-Rule 或 Filter-Id（至少一个） |

**Redirect-Server AVP**（编码434，Grouped）结构：
```
Redirect-Server ::= < AVP Header: 434 >
  { Redirect-Address-Type }          -- 地址类型
  { Redirect-Server-Address }        -- 服务器地址
```

**特殊行为**：
- 首次交互时Final-Unit-Action=REDIRECT或RESTRICT_ACCESS但CCA未携带GSU，P-GW需立即执行指定动作
- OCS需支持暂时中断功能才能执行终止业务的策略动作

### K038: Reporting-Reason九种上报原因详解 [协议]
> 来源: K321

Reporting-Reason AVP编码872，Enumerated类型，指出特定类别配额的使用量上报原因。仅在CCR消息上报使用量时携带。

| 取值 | 枚举值 | 携带位置 | 适用范围 | 含义 |
|------|--------|---------|---------|------|
| 0 | THRESHOLD | Used-Service-Units | 特定配额类型 | 配额门限达到 |
| 1 | QHT | MSCC | 所有配额类型 | 配额保持时长达到 |
| 2 | FINAL | MSCC | 所有配额类型 | 业务终止（PDP/IP CAN会话终止） |
| 3 | QUOTA_EXHAUSTED | Used-Service-Units | 特定配额类型 | 配额耗尽 |
| 4 | VALIDITY_TIME | MSCC | 所有配额类型 | Validity-Time到期 |
| 5 | OTHER_QUOTA_TYPE | Used-Service-Units | 特定配额类型 | 多重配额中一个达到触发条件 |
| 6 | RATING_CONDITION_CHANGE | MSCC | 所有配额类型 | Trigger预定义的费率条件变化 |
| 7 | FORCED_REAUTHORISATION | MSCC | 所有配额类型 | OCS发起重授权 |
| 8 | POOL_EXHAUSTED | Used-Service-Units / MSCC | 信用池级 | 信用池保障单元足够但费率组不够 |

**关键规则**：
- MSCC中可携带：QHT、FINAL、VALIDITY_TIME、FORCED_REAUTHORISATION、RATING_CONDITION_CHANGE（适用所有配额类型）
- Used-Service-Units中可携带：THRESHOLD、QUOTA_EXHAUSTED、OTHER_QUOTA_TYPE（仅指示特定配额类型）
- POOL_EXHAUSTED：在Used-Service-Units中指示该信用池所有类型配额；所有配额类型使用同一信用池时可在MSCC中携带
- Reporting-Reason=RATING_CONDITION_CHANGE时，必须同时在Trigger AVP中指出引发重授权的具体触发事件

参见: 3GPP TS 32.299 Va.4.0 7.2.175章节

### K039: Reporting-Reason与Trigger-Type的对应关系 [协议]
> 来源: K321, K331

Reporting-Reason与Trigger-Type的关联使用场景：

| 场景 | CCA中OCS下发 | CCR中P-GW上报 |
|------|-------------|--------------|
| 配额门限 | Time-Quota-Threshold / Volume-Quota-Threshold | Reporting-Reason=THRESHOLD |
| 配额保持时间 | Quota-Holding-Time | Reporting-Reason=QHT |
| 有效期到期 | Validity-Time | Reporting-Reason=VALIDITY_TIME |
| 配额耗尽 | Granted-Service-Unit中的配额量 | Reporting-Reason=QUOTA_EXHAUSTED |
| 费率条件变化 | Trigger AVP（含Trigger-Type列表） | Reporting-Reason=RATING_CONDITION_CHANGE + Trigger-Type |
| OCS强制重授权 | RAR消息 | Reporting-Reason=FORCED_REAUTHORISATION |
| 信用池耗尽 | G-S-U-Pool-Reference | Reporting-Reason=POOL_EXHAUSTED |
| 业务终止 | - | Reporting-Reason=FINAL |

**RATING_CONDITION_CHANGE的特殊规则**：CCA中下发Trigger AVP（包含多个Trigger-Type），当对应条件满足时，P-GW发送CCR(UPDATE)，同时携带Reporting-Reason=RATING_CONDITION_CHANGE和具体的Trigger-Type值。

### K040: Trigger-Type完整取值与重授权触发条件 [协议]
> 来源: K322

Trigger-Type AVP编码870，Enumerated类型。CCA中指示P-GW在何种事件下重新申请配额；CCR中指示触发重授权的是RATING_CONDITION_CHANGE事件。

| 取值 | 枚举值 | 触发条件 |
|------|--------|---------|
| 1 | CHANGE_IN_SGSN_IP_ADDRESS | SGSN IP地址变化 |
| 2 | CHANGE_IN_QOS | 用户协商QoS变化 |
| 3 | CHANGE_IN_LOCATION | 用户位置变化 |
| 4 | CHANGE_IN_RAT | 接入技术变化（Rate） |
| 5 | CHANGE_IN_UE_TIMEZONE | 终端时区变化 |
| 30 | CHANGEINLOCATION_MCC | 服务网络MCC改变 |
| 31 | CHANGEINLOCATION_MNC | 服务网络MNC改变 |
| 33 | CHANGEINLOCATION_LAC | 终端LAC改变 |
| 35 | CHANGEINLOCATION_TAC | 终端TAC改变 |
| 36 | CHANGEINLOCATION_ECGI | 终端ECGI改变 |
| 74 | CHANGE_IN_SERVING_PLMN_RATE_CONTROL | 服务PLMN速率控制改变 |
| 75 | CHANGE_IN_APN_RATE_CONTROL | APN速率改变 |

**计费关联**：只有由Trigger AVP给出的事件才能触发重新申请配额。OCS在CCA中下发Trigger-Type，P-GW监测对应条件变化，变化后发送CCR(UPDATE)并携带Reporting-Reason=RATING_CONDITION_CHANGE和Trigger-Type。

参见: 3GPP TS 32.299 Va.4.0 7.2.236章节

### K041: Validity-Time与配额有效期机制 [协议]
> 来源: K323, K334

Validity-Time AVP编码448，Unsigned32类型，OCS下发给P-GW，以秒为单位。

**核心行为**：
- 有效时间以P-GW收到CCA消息的时刻为起点计时
- 有效时间内业务资源耗尽 → P-GW发送CCR重新申请配额
- 有效时间到达 → 所有MSCC都需要上报配额（不管单个MSCC是否耗尽）
- 单一MSCC上报配额时计时不停止（只有全部MSCC都上报才重置）

**Validity-Time（Gy接口RFC 4006）与Quota-Holding-Time（N4接口）的区别：**

| 对比项 | Validity-Time (Gy) | Quota-Holding-Time (N4) |
|--------|--------------------|------------------------|
| 协议层 | Diameter/Gy接口 | PFCP/N4接口 |
| 下发方 | OCS | SMF |
| 接收方 | P-GW/SMF | UPF |
| 单位 | 秒 | 秒 |
| 起算点 | P-GW收到CCA消息的时刻 | UPF收到配额的时刻 |
| 触发动作 | 所有MSCC上报配额 | URR上报使用量 |
| Reporting-Reason | VALIDITY_TIME | QHT（配额保持时间） |

**融合计费中的映射**：SMF收到OCS/CHF下发的Validity-Time后，可能将其映射为N4接口的Quota-Holding-Time下发给UPF。

参见: RFC 4006 8.33章节

### K042: Tariff-Time-Change费率切换时间机制 [协议]
> 来源: K324

Tariff-Time-Change AVP编码451，Time类型。以January 1, 1900, 00:00 UTC为起点，以秒为单位。

**机制**：
- OCS在GSU中下发Tariff-Time-Change，指示费率切换的时间点
- 当MSCC和GSU同时绑定同一个业务标识或费率组时，Tariff-Time-Change和Tariff-Change-Usage会同时下发
- 两个配额值可能绑定同一个信用池，也可能是不同的两个信用池
- 应答消息中使用Used-Service-Unit AVP来表示时长费率的变化

**限制**：
- 费率改变机制是可选的，不能应用在基于时长的业务中
- 如果OCS不支持费率随时间改变的机制，该AVP值无效，OCS终止CC承载并在Termination-Cause中携带DIAMETER_BAD_ANSWER

参见: RFC 4006 8.20章节

### K043: OCS主备Group与负荷分担 [方案设计]
> 来源: K94

OCS组网架构：
- 主备OCS Group之间支持热备份：主用故障时DCC会话可动态迁移到备用Group
- 同一OCS Group内采用负荷分担，三种方式（互斥）：

| 方式 | 说明 |
|------|------|
| 平均负荷分担 | 所有OCS平均分担 |
| 基于用户号段组（MSISDN/IMSI） | 同一号段组可被多个OCS绑定但优先级必须不同 |
| 基于百分比例 | 按设置的比例分担 |

**隐性规则**：百分比例和用户号段组负荷分担**不能同时使用**。

### K044: OCS选择优先级机制 [方案设计]
> 来源: K95

OCS选择优先级从高到低：
1. PCRF下发的OCS（CCA-I消息AVP）
2. AAA Server下发的OCS（Access-Accept消息OCS-ID）
3. UserProfile配置的OCS Group（ADD UPBINDUPG匹配号段/接入类型/CC/漫游状态/位置区）
4. 本地APN配置的OCS Group
5. 本地整机配置的OCS Group
6. 基于CC属性选择OCS Group

### K045: Diameter链路可靠性 [方案设计]
> 来源: K96

PGW-C支持与一个OCS的多个IP/SCTP端点建立多条Diameter链路，构成链路组：
- 链路组内支持**主备**和**负荷分担**模式（ADD DIAMCONNGRP的SELECTMODE参数）
- 一条链路故障时自动选择组内其他可用链路
- TCP传输：与多个IP建立多条TCP链路
- SCTP传输：与多个SCTP端点建立多条SCTP偶联

### K046: CCFH异常处理机制 [原理]
> 来源: K97

CCFH（Credit Control Failure Handling）三种处理方式：

| CCFH值 | 备用OCS正常时 | 备用OCS故障时 |
|--------|--------------|--------------|
| TERMINATE | 终止DCC会话，去激活承载 | 终止DCC会话，去激活承载 |
| RETRY_AND_TERM | 重传给备用OCS，保持承载 | 终止DCC会话，去激活承载 |
| CONTINUE | 重传给备用OCS，保持承载 | 终止DCC会话（不发CCR-T）、保持承载、**转离线计费** |

**隐性规则**：CONTINUE模式下需开启离线计费功能才能保持承载。转离线后的话单中增加`failureHandlingContinueFlag`标志。

CCFH可由OCS下发或本地配置，OCS下发优先级更高。

### K047: 异常返回码两层处理 [协议]
> 来源: K98

CCA消息中有两层返回码：

| 层级 | 作用范围 | 配置命令 |
|------|---------|---------|
| Command层 | 针对整个承载 | ADD CMDRCACT |
| MSCC层 | 针对特定RG或RG+SID的业务 | ADD MSCCRCACT |

处理动作包括：阻塞业务、去激活承载、重定向、转离线计费等。**Command层配置的处理动作优先。**

### K048: 在线计费异常处理全景 [原理]
> 来源: K99

| 异常场景 | 配置命令 | 核心处理 |
|---------|---------|---------|
| OCS链路Down（激活时） | SET OCSDOWNACTION | PERMIT或FORBIDDEN |
| OCS链路Down（DCC会话中） | ADD DCCTEMPLATE(CCFH) | TERMINATE/RETRY_AND_TERM/CONTINUE |
| Tx定时器超时 | SET TXTIMER + CCFH | 同上 |
| 异常返回码（Command层） | ADD CMDRCACT | 阻塞/去激活/重定向/转离线 |
| 异常返回码（MSCC层） | ADD MSCCRCACT | 同上 |
| 紧急放通 | SET FHBYPASS | 仅OCS故障+Command层，需书面认可 |

**紧急放通（FHBYPASS）隐性规则**：SET FHBYPASS仅用于故障场景下的紧急处理，仅适用于OCS故障（非异常结果码场景）和Command层异常结果码，不支持MSCC层异常结果码的一键放通。由于影响用户计费方式，必须在获得客户书面认可后方可使用。

---

## 第五章：Ga接口与CG

### K049: CG链路状态三态判定机制 [方案设计]
> 来源: K75

链路状态三态判定（基于采样周期内通断比）：
- **高通态**（>80%）：允许话单发送，允许历史缓存话单发送
- **低通态**（50%~80%）：允许话单发送，禁止历史缓存话单发送
- **阻塞态**（<50%）：禁止话单发送

探测机制：配置CG后发Node Alive Request → 每固定1分钟发Echo Request → 3次无响应（可配置）则链路异常 → 触发ALM-81021告警。

此机制动态平滑调整传送速率，避免急停急起对CG的冲击。

### K050: CG选择优先级与号段匹配 [配置]
> 来源: K76

CG选择优先级：
1. PCRF下发（通过CCA-I的Primary/Secondary-Charging-Collection-Function-Name AVP）→ 必须在本地已配置才生效
2. 本地CG服务器池（号段匹配CG组 → 全局CG组 → 非CG组的CG）
3. PCRF下发的主备CG均不可用时，在本地CG服务器池中选择

号段匹配逻辑：号段匹配CG组 → 在组内按优先级和状态选择CG → 未匹配但配置了全局CG组 → 在全局CG组内选择 → 都未匹配 → 在非CG组CG中选最高优先级。

### K051: CG负荷分担两种算法 [方案设计]
> 来源: K77

| 算法 | 激活时选择 | 发送话单时 | 同一用户话单 | 负荷均衡性 |
|------|-----------|-----------|-------------|-----------|
| 基于负载 | 状态正常+最高优先级中选负载最少 | 重新选负载最少 | 可能发往不同CG | 处理快的CG接收更多 |
| 基于用户 | 状态正常+最高优先级中依次选择 | 激活时CG正常则继续使用 | 每次发往同一CG | 不同用户轮选，更均衡 |

通过SET CDRTRANSFER配置选择算法。

### K052: CG过载保护WAL机制 [配置]
> 来源: K78

UNC提供WAL（Windows Access Limit）过载保护：当CG当前待处理负荷超出配置的WAL值（ADD CG命令配置）时，将该CG置为不可用，后续负荷转移到其他CG。与Gy接口OCS的WAL机制原理相同。

### K053: 话单类型与版本对应关系 [原理]
> 来源: K79

| 话单类型 | 版本 | 说明 |
|---------|------|------|
| G-CDR | R98~R7 | GPRS/UMTS用户，不含内容计费 |
| eG-CDR | R6/R7 | GPRS/UMTS用户，增加内容计费字段，一张话单可记录多个业务 |
| SGW-CDR | R8~R10 | LTE用户（SGW-C形态），用户级计费，不支持内容计费 |
| PGW-CDR | R8~R10 | LTE/EPC融合用户（PGW-C形态），支持内容计费 |

**隐性规则**：EPC融合组网下必须采用PGW-CDR以保持GUL切换前后话单类型一致。

### K054: 话单容器机制 [原理]
> 来源: K80

引入容器概念的背景：为记录各种计费条件改变时的信息而不增加话单量。一张话单可包含多个容器。

| 容器类型 | 粒度 | 记录内容 | 新容器产生条件 |
|---------|------|---------|--------------|
| 流量容器 | 承载级 | 流量/时长，不区分业务 | QoS改变、费率时段改变、用户位置改变、产生话单 |
| 业务容器 | 业务级 | 某业务的流量/时长 | IP-CAN承载修改、费率时段改变、在线计费处理失败(CCFH=CONTINUE)、产生话单 |

容器触发通过SET CONTAINERTRIGGER配置。

### K055: 话单生成五个阶段 [原理]
> 来源: K81

1. **创建话单**：用户激活时或部分话单生成后触发创建
2. **生成部分话单**：满足特定条件时（时间/流量/条件变更阈值、强制产生）
3. **关闭话单**：用户去激活时生成最后话单
4. **话单编码**：ASN.1定义、BER编码，符合3GPP TS 32.298标准
5. **话单发送**：编码后封装到GTP'消息，通过Ga接口发送给CG

### K056: 话单触发条件分类 [配置]
> 来源: K82

部分话单触发条件：
- **按时间**：SET OFCTHRESHOLD设置的时间间隔
- **按流量**：SET OFCTHRESHOLD设置的流量阈值
- **按计费条件改变**：QoS/ULI/费率改变次数之和达到阈值；RAT/服务节点变更；MS Time Zone更新
- **强制产生**：FOC GENERATECDR命令

最后话单触发：MS/UE去激活。

### K057: 话单可靠性机制汇总 [方案设计]
> 来源: K83

| 机制 | 说明 |
|------|------|
| 预防重复话单 | 未收到主CG响应则发往备CG，GTP'消息携带"Send possible duplicated"标记 |
| 缓存话单信息 | 所有CG链路阻塞时按CG组/版本/IP分目录缓存，主目录charge1/备目录charge2 |
| 抑制零流量话单 | 用户未进行业务时不产生中间话单（去活话单和强制产生除外） |
| 话单池告警控制 | 池占用率达ALM-81005门限时，更新类trigger只记录不产生话单；控制用户接入数 |
| 备份计费信息 | 定时备份到CSDB_VNFC，计费POD故障时其他POD接替 |

---

## 第六章：会话流程中的计费交互

### K058: PDU会话建立流程中的计费交互点 [协议]
> 来源: K325, K332

PDU会话建立流程共29步，其中计费相关的关键交互点：

**步骤12-14: PCF策略交互（N7接口）**
- 步骤12: SMF选择PCF（如果部署动态PCC）
- 步骤13: SMF -> PCF: Npcf_SMPolicyControl_Create Request
  - 携带: supi, pduSessionId, notificationUri, pduSessionType, sliceInfo
- 步骤14: PCF -> SMF: Npcf_SMPolicyControl_Create Response
  - **计费关键信元**: chargingInfo（包含PDU会话的CHF地址）
  - 其他: sessRules(会话级QoS), authSessAmbr(授权Session-AMBR), authDefQos(默认QoS), pccRules(业务级PCC规则), flowInfos(流过滤信息), policyCtrlReqTriggers(策略触发器)

**步骤15-17: UPF选择与PFCP会话建立（N4接口）**
- 步骤16: SMF -> UPF: PFCP Session Establishment Request
  - **计费关键信元**: Create URR（定义统计类上报动作，如流量耗尽上报、离线计费上报等）
  - 其他: Create PDR, Create FAR, Create QER, Create BAR

**PFCP Session Establishment中的计费相关信元：**

| 信元 | 含义 | 计费作用 |
|------|------|---------|
| Create URR | Usage Reporting Rule | 定义统计类上报动作，如流量耗尽上报、离线计费上报 |
| Create PDR | Packet Detection Rule | 流检测规则，匹配数据包后关联URR计量 |
| Create FAR | Forwarding Action Rule | 转发规则 |
| Create QER | QoS Enforcement Rule | QoS流控规则，SMF通常下发3类QER：Session级、QoSFlow级、QFI级 |
| UE IP Address | SMF分配的UE IP | 计费话单中记录 |
| SDF Filter | 业务数据流过滤器 | 内容计费规则匹配 |

**URR与PDR的关联**：PDR匹配数据包后，同时触发关联的URR进行流量/时长计量。PDR区分上下行（Source interface: access=上行N3, core=下行N6）。

**步骤18-19: IP地址分配后PCF更新**
- 步骤18: SMF -> PCF: Npcf_SMPolicyControl_Update（携带UE IP地址）
  - 触发器: UE_IP_CH（IP地址变更）
- 步骤19: PCF -> SMF: 更新SM策略关联

**要点**：PDU会话建立时chargingInfo由PCF下发给SMF，SMF根据其中的CHF地址创建融合计费会话。Create URR在PFCP Session Establishment中同步下发。

### K059: PDU会话释放（SMF发起）流程中的计费交互 [协议]
> 来源: K326, K333

SMF发起的PDU会话释放共17步，触发条件为SMF识别本地配置策略刷新。

**步骤1-2: PFCP会话删除（N4接口）**
- 步骤1: SMF -> UPF: PFCP Session Deletion Request
- 步骤2: UPF -> SMF: PFCP Session Deletion Response
  - **计费关键信元**: Usage Report（如果UPF已开通URR且存在流量使用测量，必须返回使用量报告）

**Usage Report信元出现条件**：
- UPF已开通URR（Create URR时已下发）
- PFCP会话被删除
- URR的流量使用测量数据可用

**Usage Report在计费流程中的作用**：
1. UPF在PFCP Session Deletion Response中返回最终Usage Report
2. SMF收到Usage Report后，提取其中的流量/时长使用量
3. SMF构造Charging Data Request[Termination]，携带最终使用量发送给CHF
4. CHF生成最终话单，关闭计费会话

**步骤16-17: PCF策略删除（N7接口）**
- 步骤16: SMF -> PCF: Npcf_SMPolicyControl_Delete
  - 携带: userLocationInfo, nrLocation, pduSessRelCause
- 步骤17: PCF -> SMF: 204 No Content

**释放原因分类（SMF维度）**：
- #36 regular deactivation（常规去激活）
- #39 reactivation requested（重激活请求）
- #46 out of LADN service area（离开LADN服务区）
- #38 network failure（网络故障）
- #26 Insufficient resources（资源不足）
- PCF触发的释放

**计费流程要点**：释放时先删PFCP会话，UPF返回最终Usage Report；SMF收到后向CHF发送Charging Data Request[Termination]上报最终使用量；最后删除PCF策略关联。

### K060: PDU会话修改（PCF发起）流程中的计费交互 [协议]
> 来源: K327

PCF发起的PDU会话修改共19步，触发条件为PCF识别配置策略有修改。

**步骤1-2: PCF通知SMF策略更新**
- 步骤1: PCF -> SMF: Npcf_SMPolicyControl_UpdateNotify
  - 携带: smPolicyDecision, sessRules, pduSessionId, supi
- 步骤2: SMF -> PCF: 204 No Content 或 200 OK
  - 200 OK表示PCC规则和/或会话规则部分未安装/激活成功

**步骤11-12/16-17: PFCP会话修改（N4接口）- 两次**
- 步骤11: SMF -> UPF: PFCP Session Modification Request（QoS参数修改涉及UPF侧时触发）
- 步骤16: SMF -> UPF: PFCP Session Modification Request
  - 携带: Remove PDR/FAR/QER, Create PDR/FAR/QER, Update PDR, QoS Flow Identifier
  - **计费关联**：PCC规则变更可能导致URR的增删改

**步骤18-19: SMF向PCF上报事件**
- 步骤18: SMF -> PCF: Npcf_SMPolicyControl_Update
  - 携带: repPolicyCtrlReqTriggers（如SUCC_RES_ALLO表示资源分配成功）
- 步骤19: PCF -> SMF: 响应

**计费流程要点**：PCF发起策略修改 → SMF可能需要更新UPF的URR规则 → SMF向CHF发送Charging Data Update上报策略变更

### K061: 4G/5G会话管理关键差异（计费视角）[协议]
> 来源: K328

4G vs 5G会话管理对比（计费相关）：

| 对比项 | 4G | 5G |
|--------|-----|-----|
| 数据通道 | PDN连接 | PDU会话 |
| QoS控制粒度 | EPS承载 | QoS Flow |
| 计费承载 | 每个EPS承载独立URR | 每个QoS Flow独立URR |
| 默认承载 | 注册后强制建立默认承载 | 不强制建立，按需建立PDU会话 |
| 会话释放 | PDN去连接=释放所有承载 | PDU会话释放=释放所有QoS Flow |
| 控制面 | MME + S-GW/P-GW控制面 | SMF集中完成 |
| 业务连续性 | 仅IP连续性 | SSC Mode 1/2/3三种模式 |

**SSC Mode对计费的影响**：
- SSC Mode1: IP地址和UPF不变，计费会话连续
- SSC Mode2: 先断后连，旧PDU会话释放（上报最终Usage Report），新建PDU会话（新建计费会话）
- SSC Mode3: 先连后断，存在新旧两个PDU会话重叠期，两套计费会话并存

**5G新增流程（计费关联）**：
- 已有PDU会话用户面的选择性激活/去激活：去激活仅删除用户面连接、信令面保持不变，不影响计费会话状态

### K062: 5G QoS模型与计费QoS Flow的映射关系 [协议]
> 来源: K329, K335

5G QoS模型中与计费直接相关的概念：

**QoS Flow（数据通路）= 计费最小粒度**
- QFI（QoS Flow ID）在PDU Session中唯一
- QFI可动态分配，也可等于5QI
- 一个PDU会话共用一个NG-U隧道，通过QFI区分QoS Flow

**QoS参数与计费配置的关联**：

| QoS参数 | 计费关联 |
|---------|---------|
| ARP | QoS Flow建立/修改优先级，影响URR的创建时机 |
| 5QI | 业务质量索引，可用于区分不同费率组(Rating-Group) |
| Session-AMBR | PDU会话级聚合速率限制，影响流量计量 |
| GFBR/MFBR | GBR QoS Flow的保证/最大带宽 |

**QoS控制机制与计费触发**：
- 信令控制: SMF在PDU会话建立/修改时向UPF/RAN/UE发送QoS Flow信息（含URR）
- Reflective QoS: 仅用于Non-GBR，UE自行推演上行QoS Rule，SMF不发送信令
- Notification Control: RAN不满足GFBR时通知SMF，可能触发QoS变更进而触发计费更新

**两级映射机制**：
1. 数据包 -> QoS Flow（通过PDR/QoS Rule匹配）
2. QoS Flow -> Radio Bearer（RAN自主决定）

计费关注第一级映射：PDR匹配到QoS Flow后，关联对应的URR进行计量。

**5G QoS Flow与MSCC的映射模型**：

EPC场景（Gy接口直连OCS）：
- 每个EPS承载 = 一个MSCC实例
- 默认承载对应初始CCR(INITIAL)
- 专有承载对应CCR(UPDATE)中新增MSCC

5GC场景（融合计费Nchf）：
- 每个QoS Flow = 一个计费单元（通过Rating-Group区分）
- 默认QoS Flow对应Charging Data Request[Initial]
- 专有QoS Flow对应Charging Data Request[Update]中新增的multipleUnitUsage
- PCC规则中通过Rating-Group AVP将QoS Flow关联到费率组
- SMF通过PFCP的URR将QFI与Rating-Group关联，UPF按URR计量

**5G二级映射中的计费位置**：
- UPF执行PDR匹配 -> 关联URR计量（第一级：数据包到QoS Flow）
- 计费发生在UPF用户面，SMF控制面负责将使用量上报给CHF

---

## 知识统计

| 章节 | 数量 | 编号范围 |
|------|------|---------|
| 第一章：计费系统架构 | 12 | K001-K012 |
| 第二章：计费方式与维度 | 7 | K013-K019 |
| 第三章：核心术语定义 | 8 | K020-K027 |
| 第四章：Gy接口与DCC协议 | 21 | K028-K048 |
| 第五章：Ga接口与CG | 9 | K049-K057 |
| 第六章：会话流程中的计费交互 | 5 | K058-K062 |
| **合计** | **62** | K001-K062 |

| 分类标签 | 数量 |
|---------|------|
| [原理] | 24 |
| [协议] | 17 |
| [方案设计] | 14 |
| [配置] | 7 |
| [隐性规则] | 包含在各条知识中 |

---


## 第七章：Nchf融合计费服务（N40接口）

### K101: Nchf_ConvergedCharging四种服务操作 [协议]
> 来源: K04, K190

| 服务操作 | 功能 | 发起方 | 对应融合计费消息 | 对应4G消息 |
|----------|------|--------|------------------|------------|
| Nchf_ConvergedCharging_Create | 计费会话建立 | SMF | Charging Data Request/Response [Initial] | CCR-I / CCA-I |
| Nchf_ConvergedCharging_Update | 计费会话更新（配额申请/上报/VT等） | SMF | Charging Data Request/Response [Update] | CCR-U / CCA-U |
| Nchf_ConvergedCharging_Release | 计费会话结束 | SMF | Charging Data Request/Response [Termination] | CCR-T / CCA-T |
| Nchf_ConvergedCharging_Notify | 重授权/去活通知 | CHF | Charging Notify Request/Response | RAR / RAA |

CHF职责：配额管理、重授权触发条件下发、通知服务、接受用量报告、生成CHF-CDR话单。
SMF职责：请求并接收配额、发送用量报告、处理配额重授权或终止通知。

---

### K102: CHF选择优先级（6级） [配置]
> 来源: K08, K51, K191

SMF选择CHF的优先级从高到低：

| 优先级 | 选择方式 | 配置命令 | 说明 |
|--------|----------|----------|------|
| 1 | 基于IMSI拨测选择 | `ADD SELCHFGBYIMSI` | 拨测场景专用 |
| 2 | 基于IMSI号段选择 | - | 多CHF组负载均衡 |
| 3 | PCF下发的chargingInfo | - | 域名需查本地配置，IP直接使用 |
| 4 | UDM签约CC → 本地CHF | - | DNN/APN级CC优先于Session级CC |
| 5 | NRF发现CHF | - | 仅支持优先级/权重，不支持主备 |
| 6 | 本地配置CC选择CHF | `ADD SELECTCHFGBYCC` | 最低优先级兜底 |

---

### K103: Charging Data Request [Initial] 关键信元 [协议]
> 来源: K53, K192

Create Request关键信元：

| 信元 | 说明 |
|------|------|
| invocationSequenceNumber | 请求序号（首次为0） |
| nfConsumerIdentification | NF消费者标识（含nFIPv4/v6Address、nFName、nodeFunctionality=SMF） |
| invocationTimeStamp | 请求发送时间 |
| multipleUnitUsage | 配额管理请求/用量报告数组 |
| -- ratingGroup | 费率组标识 |
| -- requestedUnit | 配额申请（在线计费携带，离线计费不携带） |
| -- uPFID | UPF标识 |
| pDUSessionChargingInformation | PDU会话计费信息 |
| -- chargingId | PDU会话计费标识 |
| -- pduSessionInformation | 含chargingCharacteristics、startTime等 |
| -- unitCountInactivityTimer | 配额不活跃定时器 |
| notifyUri | 接收CHF Notify消息的SMF URI |

时间戳计算方式：`SET CNVRGDCHGPARA`的`TIMEROUNDMODE`参数控制——ROUNDOFF（四舍五入，默认）/ ROUNDDOWN（向下取整）。

---

### K104: Charging Data Response [Initial] 关键信元 [协议]
> 来源: K53, K193

Create Response关键信元：

| 信元 | 说明 |
|------|------|
| invocationSequenceNumber | 响应序号 |
| multipleUnitInformation | 数组 |
| -- resultCode | 结果码（SUCCESS等） |
| -- ratingGroup | 费率组标识 |
| -- grantedUnit | 授权配额（totalVolume字节 + time秒） |
| -- triggers | CHF下发的trigger全集（triggerType + triggerCategory） |
| -- timeQuotaThreshold | 时间配额门限（秒） |
| -- volumeQuotaThreshold | 流量配额门限（字节） |

Trigger类型示例：QUOTA_THRESHOLD（到达阈值）、QUOTA_EXHAUSTED（配额耗尽）。
TriggerCategory: IMMEDIATE_REPORT（立即上报）。

异常响应处理：`SET CNVRGDCHGPARA`的`BADRSPACT=CONTINUE`时，用户业务继续但不进行配额管理。

---

### K105: 在线计费与离线计费的信元差异 [隐性规则]
> 来源: K54, K194

| 维度 | 在线计费 | 离线计费 |
|------|----------|----------|
| Create Request | 含requestedUnit | **不含**requestedUnit |
| Create Response | 含grantedUnit、阈值、配额Trigger | **不含**grantedUnit/threshold/unitQuotaThreshold，不含QUOTA_THRESHOLD/QUOTA_EXHAUSTED |
| Update Request | quotaManagementIndicator=ONLINE_CHARGING，含requestedUnit | quotaManagementIndicator=OFFLINE_CHARGING，不含requestedUnit |
| PFCP Create URR | 含Volume Quota/Time Quota/Event Quota | **不含**配额信元 |

核心区别：在线计费申请配额（有配额管理），离线计费仅申请计费参数（无配额管理）。

---

### K106: 计费会话更新四种触发场景 [方案设计]
> 来源: K55, K197

| 触发场景 | 说明 | 关键流程 |
|----------|------|----------|
| UPF内部事件 | 配额耗尽/到达阈值、配额空闲时间门限、访问无配额新业务 | UPF Usage Report → SMF → CHF → 新配额 → UPF |
| SMF内部事件 | 在线配额有效时长超期（`ADD CCT`配置RG级有效时长） | SMF查询UPF用量 → CHF → 新配额 → UPF |
| 外部事件 | 接入条件更新（Serving Node变更、PRA变更、QoS改变、位置更新、时区改变、PLMN变更） | UE→SMF→UPF查询→CHF→新配额→UPF |
| CHF重授权 | 用户充值成功等场景CHF通知SMF重新申请配额 | CHF Notify → SMF查询UPF→CHF→新配额→UPF |

SMF上报方式：`SET CNVRGDCHGPARA`的`RPTBASEDONGU`参数——不使能时基于实际使用量上报；使能则基于GrantedUnit做配额管理，用量不超过下发配额。

UPF定时器保护：触发上报后启动定时器 = `T3RESPONSE * N3REQUEST + 4s`（`SET UPPFCPPATH`配置）；超时未收到配额更新则UPF阻塞业务。

---

### K107: Charging Data Update Request关键信元 [协议]
> 来源: K199

Update Request中的multipleUnitUsage包含：

| 信元 | 说明 |
|------|------|
| ratingGroup | 费率组 |
| requestedUnit | 配额申请（在线计费） |
| UsedUnitContainer | 已用配额容器 |

UsedUnitContainer子信元：

| 子信元 | 说明 |
|--------|------|
| totalVolume / downlinkVolume / uplinkVolume | 流量使用量 |
| time | 时长使用量 |
| quotaManagementIndicator | ONLINE_CHARGING / OFFLINE_CHARGING |
| serviceId | 服务标识 |
| triggers | 当前触发类型（仅一个，取优先级最高） |
| triggerTimestamp | 触发时间 |
| localSequenceNumber | 本地序号 |
| pDUContainerInformation | 含timeofFirstUsage/timeofLastUsage/rATType/userLocationInformation |

**隐性规则**：请求消息的triggerType只能携带一个，表示由哪个trigger触发；多个trigger同时满足时携带优先级最高的一个。

---

### K108: CHF下发的Trigger全集与优先级 [隐性规则]
> 来源: K56, K200

- CHF在Response中携带triggerType全集（如QUOTA_THRESHOLD + QUOTA_EXHAUSTED），与Request由哪个trigger触发无关
- SMF本地也可配置Trigger（`ADD PDUTRIGGER`/`ADD RGTRIGGER`），优先级低于CHF下发的
- 外部事件触发场景CHF可额外下发Session级Trigger：VOLUME_LIMIT、TIME_LIMIT、USER_LOCATION_CHANGE等
- CHF Response还可能携带：validityTime（配额有效时间）、sessionFailover（FAILOVER_SUPPORTED）、invocationResult.failureHandling（CONTINUE）

RG级VT事件合并：`SET CNVRGDCHGPARA`的`MERGERGVTSW=ENABLE`时，同时发生的RG级VT事件合并上报CHF。

---

### K109: 计费会话释放流程 [协议]
> 来源: K57, K201

UE发起释放流程：

1. UE发起PDU会话释放
2. SMF→UPF: PFCP Session Deletion Request
3. UPF→SMF: Deletion Response（携带计费统计信息）
4. SMF→CHF: ChargingDataRelease Request（含final用量）
5. CHF扣费处理，关闭CHF-CDR
6. CHF返回Release Response

Release Request特有信元：
- stopTime: PDU会话停止时间
- sessionStopIndicator: true（指示PDU会话终止）
- triggerType: FINAL（正常去活）

离线计费场景：quotaManagementIndicator=OFFLINE_CHARGING。

---

### K110: CHF Notify通知（重授权与去活） [协议]
> 来源: K59, K202

**CHF发起重授权（仅在线计费）：**

1. CHF→SMF: ChargingDataNotify Request（notificationType=REAUTHORIZATION, 含reauthorizationDetails: [{quotaManagementIndicator, ratingGroup}]）
2. SMF→CHF: Notify Response (204 No Content)
3. SMF→UPF: PFCP Session Modification（Query URR查询用量）
4. UPF→SMF: Modification Response（上报用量）
5. SMF→CHF: ChargingDataUpdate Request（请求重授权）
6. CHF→SMF: Update Response（新配额+新Trigger）

**CHF发起用户去活（所有计费类型）：**

1. CHF→SMF: Notify Request（notificationType=ABORT_CHARGING）
2. SMF→UPF: PFCP Session Deletion Request
3. UPF→SMF: Deletion Response（配额用量）
4. SMF→CHF: ChargingDataRelease Request（携带用量）
5. CHF扣费关闭CDR，返回Release Response
6. SMF发起PDU会话释放

---

### K111: 异常去活的triggerType填写规则 [隐性规则]
> 来源: K58

| 去活场景 | triggerType值 |
|----------|---------------|
| 正常去活 | FINAL |
| 异常去活（有`ADD N40DIAGTRIGGER`） | 按RELEASETRIGGER参数配置 |
| 异常去活（无N40DIAGTRIGGER，`SET CNVRGDCHGPARA` SPTABNTRIGGER=ENABLE） | AbnormalRelease |
| 异常去活（无N40DIAGTRIGGER，SPTABNTRIGGER=DISABLE） | FINAL |

优先级：`ADD N40DIAGTRIGGER` > `SET CNVRGDCHGPARA` SPTABNTRIGGER。

---

### K112: SMF维护RG与URR ID的映射关系 [原理]
> 来源: K195, K258

| 接口 | 方向 | RG/URR角色 |
|------|------|------------|
| Nchf（SMF→CHF） | SMF→CHF申请配额 | 按RG粒度申请配额，按RG或RG+SID粒度上报配额 |
| Nchf（CHF→SMF） | CHF→SMF下发配额 | 按RG粒度下发配额 |
| N4（SMF→UPF） | SMF→UPF下发URR | URR包含计费事件和计费参数，UPF按URR向SMF上报配额用量 |

关键映射规则：
- **所有RG都有对应的URR ID**
- 但URR并不都用于计费，**非计费的URR ID没有对应的RG**
- SMF负责维护RG与URR ID之间的映射关系

计费会话创建触发方式：默认在PDU会话建立时触发，可通过`SET CHFINIT`命令的`CHFINIT`参数配置为业务使用时触发。

---

### K113: UPF分配IP vs SMF分配IP的计费会话创建差异 [方案设计]
> 来源: K196

- **UPF分配IP**：先建立PFCP会话（SMF→UPF），UPF分配IP后返回，SMF再向CHF发Create Request，然后PFCP会话修改下发URR
- **SMF分配IP**：SMF直接携带用户IP向CHF发Create Request，CHF返回配额后，SMF向UPF发PFCP Session Establishment（含Create PDR/FAR/URR一步到位）

---

### K114: N40关键信元——multipleUnitUsage [协议]
> 来源: K203

- 定义：包含配额管理请求的相关参数以及/或者用量报告
- 数据类型：数组，每项包含ratingGroup、requestedUnit、usedUnitContainer、uPFID
- 应用场景：ChargingDataCreate/Update/Release Request、ChargingDataNotify Request
- 参考：3GPP TS 32.291

---

### K115: N40关键信元——quotaManagementIndicator [协议]
> 来源: K204

- 定义：表示重授权通知是否用于配额管理控制
- 枚举值：ONLINE_CHARGING（要求配额管理控制）/ OFFLINE_CHARGING（无配额管理控制）
- 应用场景：ChargingDataNotify Request（CHF→SMF通知消息）

---

### K116: N40关键信元——quotaHoldingTime [协议]
> 来源: K205

- 定义：限制配额保持时间（秒），同时限制时间配额和流量配额
- 含义：当观察不到与配额相关的流量时，SMF认为该配额已过期
- 特殊值：0表示不使用该机制
- 默认值：信元不存在时使用SMF本地配置的默认值
- 应用场景：ChargingDataCreate Response

---

### K117: N40关键信元——配额阈值三件套 [协议]
> 来源: K206

| 信元 | 含义 | 单位 | 数据类型 |
|------|------|------|----------|
| timeQuotaThreshold | 授权的时间配额阈值 | 秒 | 整型 |
| volumeQuotaThreshold | 授权的流量配额阈值 | 字节 | 无符号整型 [0, 2^64-1] |
| unitQuotaThreshold | 授权的事件计费配额阈值 | 次 | 整型 |

均出现在ChargingDataCreate Response中，由CHF下发给SMF。阈值到达时触发QUOTA_THRESHOLD事件，SMF向CHF更新计费会话。

---

### K118: N40关键信元——qosFlowsUsageReports [协议]
> 来源: K207

- 定义：每个QFI的容器清单，包含上报用量
- 子信元：qFI、startTimestamp、endTimestamp、downlinkVolume、uplinkVolume
- 应用场景：ChargingDataCreate Request

---

### K119: N40关键信元——rANSecondaryRATUsageReport [协议]
> 来源: K208

- 定义：指示无线侧上报的Secondary RAT usage值
- 子信元：rANSecondaryRATType（如NR）、qosFlowsUsageReports
- 应用场景：ChargingDataCreate Request

---

### K120: 多UPF配额管理 [方案设计]
> 来源: K64

华为融合计费只支持CHF管理方式：每个UPF独立配额。

- SMF在每个UPF基础上请求配额（`Multiple Unit Usage`携带`UPF ID`）
- 哪个UPF请求配额，配额就授予哪个UPF
- I-UPF和UL CL UPF不下发配额
- 只有主锚点(PSA1)和辅助锚点(PSA2)需要配额管理

---

### K121: MEC计费流程 [方案设计]
> 来源: K65

架构：UL CL + PSA1(主锚点) + PSA2(辅锚点)
- UL CL UPF没有计费规则，不进行计费
- PSA1和PSA2各自独立申请配额
- SMF按UPF独立请求CHF（携带UPF ID）
- 本地DN通过PSA2，互联网通过PSA1

---

## 第八章：PFCP/N4接口与URR

### K122: URR定义与关键参数 [原理]
> 来源: K47

URR（Usage Reporting Rule / 使用量上报规则）：SMF通过N4(PFCP)向UPF下发的规则，指示UPF测量和报告网络资源使用情况。

- 测量维度：流量(Volume)、时长(Duration)、事件(Event)
- 上报触发：阈值到达、周期性、应请求上报

URR关键参数：URR ID, Measurement Method, Reporting Triggers, Volume Quota, Time Quota, Volume Threshold, Time Threshold, Linked URR ID, Measurement Information。

---

### K123: URR生命周期——Create/Update/Remove [协议]
> 来源: K209, K210, K211

**Create URR**必选信元：URR ID、Measurement Method、Reporting Triggers。

条件必选信元（按需出现）：

| 信元 | 触发条件 |
|------|----------|
| Volume Threshold | 使用流量测量且需要流量阈值上报 |
| Volume Quota | 使用流量测量且需要提供流量配额 |
| Event Threshold | 使用事件测量且需要事件阈值上报 |
| Event Quota | 使用事件测量且需要事件配额 |
| Time Threshold | 使用时间测量且需要时间阈值上报 |
| Time Quota | 使用时间测量且需要时间配额 |
| Quota Holding Time | 时间/流量/事件测量中，不活动期间不传包时需要 |
| Inactivity Detection Time | 使用时间测量，不活动时需挂起时间测量 |
| Linked URR ID | 需要链接使用报告 |
| Measurement Information | Inactive/Reduced/ISTM标志位为1时 |
| Aggregated URRs | URR支持信用池 |
| FAR ID for Quota Action | 有配额且UPF支持配额动作特性 |

可选信元：Monitoring Time及其Subsequent系列（Subsequent Volume/Time/Event Threshold/Quota）。

**Update URR**与Create URR的差异：
- URR ID仍为必选（标识要修改的URR）
- 其余信元为条件必选（"如果需要修改xxx，该信元应出现"）
- 新增FAR ID for Quota Action：URR中新增配额且UPF支持配额动作时可能出现
- Aggregated URRs在Update时提供完整列表（替换而非增量）

**Remove URR**仅包含一个必选信元：URR ID。用于去激活或删除PFCP会话中的URR，触发PFCP Session Modification Response上报终止用量报告（TERMR触发）。

---

### K124: URR ID信元与编码规则 [协议]
> 来源: K212

- 功能：在PFCP会话配置的所有URR中唯一标识一个URR
- 第5字节bit8含义：
  - 0：Rule由控制面功能（SMF）动态分配
  - 1：Rule在用户面功能（UPF）中预定义

---

### K125: Usage Report Trigger完整编码（3字节位图） [协议]
> 来源: K213

**第5字节（bit1-8）：**

| bit | 名称 | 含义 |
|-----|------|------|
| 1 | PERIO | 定期上报 |
| 2 | VOLTH | 流量阈值到达 |
| 3 | TIMTH | 时间阈值到达 |
| 4 | QUHTI | 配额保持时间超时（无报文） |
| 5 | START | 流量开始 |
| 6 | STOPT | 流量结束 |
| 7 | DROTH | 下行丢弃流量达阈值 |
| 8 | IMMER | 立即上报 |

**第6字节（bit1-8）：**

| bit | 名称 | 含义 |
|-----|------|------|
| 1 | VOLQU | 流量配额耗尽 |
| 2 | TIMQU | 时间配额耗尽 |
| 3 | LIUSA | 关联使用报告（Linked URR触发） |
| 4 | TERMR | 终止报告（会话删除/URR删除） |
| 5 | MONIT | 监控时间到达 |
| 6 | ENVCL | 信封关闭 |
| 7 | MACAR | MAC地址上报 |
| 8 | EVETH | 事件阈值到达 |

**第7字节：** bit1: EVEQU（事件配额耗尽），bit2-8备用。

至少一个bit为1，可多个bit同时为1。

---

### K126: Measurement Method信元 [协议]
> 来源: K214

- 功能：指示测量网络资源使用情况的方法
- 第5字节编码：
  - bit1 DURAT：时长测量
  - bit2 VOLUM：流量测量
  - bit3 EVENT：事件测量
  - bit4-8：备用
- 至少一个bit为1，可多个bit同时为1（如DURATION_VOLUME对应DURAT+VOLUM）

---

### K127: Volume Measurement信元 [协议]
> 来源: K215

- 功能：指示测量的话务量
- 第5字节编码：
  - bit1 TOVOL：Total Volume字段存在
  - bit2 ULVOL：Uplink Volume字段存在
  - bit3 DLVOL：Downlink Volume字段存在
- Total/Uplink/Downlink Volume编码为Unsigned64，单位字节

---

### K128: Duration Measurement信元 [协议]
> 来源: K216

- 功能：指示已用时间
- 单位：秒

---

### K129: Volume Quota与Time Quota信元 [协议]
> 来源: K217, K218

**Volume Quota：**
- 功能：指示UPF需要监控的流量配额
- 编码同Volume Measurement（TOVOL/ULVOL/DLVOL标志位+对应值）
- Unsigned64类型，单位字节

**Time Quota：**
- 功能：指示UPF需要监控的时间配额
- 单位：秒

---

### K130: Reporting Triggers信元（N4接口） [协议]
> 来源: K219

N4接口的Reporting Triggers编码与Usage Report Trigger基本一致但略有差异：

- 第5字节：PERIO/VOLTH/TIMTH/QUHTI/START/STOPT/DROTH/LIUSA
- 第6字节：VOLQU/TIMQU/ENVCL/MACAR/EVETH/EVEQU

与Usage Report Trigger的差异：第5字节bit8是LIUSA（非IMMER），第6字节bit3是ENVCL（非TERMR），bit4是MACAR（非MONIT），无第7字节。

---

### K131: Quota Holding Time信元（N4接口） [协议]
> 来源: K49, K205, K220

- 功能：指示配额保持时间
- 单位：秒
- 含义：在给定不活动期间没有收到数据包时，不再允许数据包传输，触发QUHTI上报
- 特殊值：QHT=0禁用该机制
- 适用于流量和时长计费

**在线计费**：QHT到期=SMF不请求配额，配额仅在下一次业务活动时请求。
**离线计费**：QHT到期=触发关闭当前业务容器。
**N40接口**：CHF在Create Response中下发quotaHoldingTime，SMF映射到N4的Quota Holding Time下发给UPF。

---

### K132: Aggregated URRs信元（信用池机制） [协议]
> 来源: K221

- 功能：支持URR信用池（多个URR共享同一配额）
- 子信元：
  - Aggregated URR ID：共享信用池的聚合URR ID（必选）
  - Multiplier：乘法器，应用于测量抽象业务单元从信用池中消耗的流量（必选）
- 使用场景：多个业务共享一个总配额池，按不同权重消耗

---

### K133: Linked URR ID信元 [协议]
> 来源: K222

- 功能：指示Linked URR的ID
- 机制：上报某个URR时，也会上报其关联的URR。例如A link B，当B上报时也会上报A
- 可存在多个相同类型的信元表示与该URR相关的多个链接URR

---

### K134: Subsequent Volume Quota信元 [协议]
> 来源: K223

- 功能：指示UPF在监控时间（Monitoring Time）之后仍需要监控的流量配额
- 编码同Volume Quota（TOVOL/ULVOL/DLVOL标志位+对应值）
- 前提：存在Monitoring Time信元且使用基于流量的测量

---

### K135: Usage Report信元（PFCP Session Report） [协议]
> 来源: K198

UPF上报的Usage Report包含：

| 信元 | 说明 |
|------|------|
| URR ID | 标识上报的URR |
| UR-SEQN | 唯一标识该URR的Usage Report |
| Start Time / End Time | 起止时间 |
| Volume Measurement | 总流量/上行/下行 |
| Duration Measurement | 时长使用情况 |
| Time of First Packet / Last Packet | 首尾包时间 |

Duration Measurement的ISTM标志位说明：
- ISTM=0或不携带：从UPF首次收到业务数据包开始，到业务终止结束
- ISTM=1：从UPF首次收到授权配额成功开始，到用户去激活或配额管理实例终止

配额更新超时保护：定时器 = T3RESPONSE * N3REQUEST + 4秒（`SET UPPFCPPATH`配置），超时未收到配额更新则UPF阻塞业务。

---

## 第九章：Gx/PCC策略与计费

### K136: PCC规则类别与一致性要求 [配置]
> 来源: K63, K159

| 规则类别 | PCF | SMF | UPF |
|---------|-----|-----|-----|
| 动态规则 | 定义名称+内容，下发 | 传递 | 执行 |
| 预定义规则 | 定义名称（与SMF匹配） | 匹配名称，传递 | 匹配本地配置，执行 |
| 预定义规则组 | 名称与SMF UserProfile匹配 | 定义UserProfile包含多条规则 | 匹配UserProfile，按优先级执行 |
| 本地规则 | 无关联 | 定义UserProfile | 匹配并执行 |

优先级：PCF全局优先级。相同优先级时动态>预定义。

一致性要求（SMF与UPF必须匹配）：UserProfile name、Rule name、URR ID。

---

### K137: Charging-Rule-Definition AVP结构 [协议]
> 来源: K224

Charging-Rule-Definition（AVP 1003, Grouped类型）定义PCRF发送给PCEF的PCC规则：

| 子信元 | 类型 | 计费相关 |
|--------|------|----------|
| Charging-Rule-Name | 必选 | 规则唯一标识 |
| Service-Identifier | 可选 | 服务标识(SID) |
| Rating-Group | 可选 | 费率组(RG) |
| Flow-Information | 可选 | 业务流信息 |
| Reporting-Level | 可选 | 上报级别 |
| Online | 可选 | 在线计费使能 |
| Offline | 可选 | 离线计费使能 |
| Metering-Method | 可选 | 计量方式 |
| Monitoring-Key | 可选 | 配额监控键 |
| Precedence | 可选 | 优先级 |

规则：如果可选AVP被删除但之前已提供，之前的信息保留有效。Flow-Information/Flows AVP如果重新提供则替换所有之前的值。

---

### K138: Charging-Rule-Install与Charging-Rule-Remove [协议]
> 来源: K225

**Charging-Rule-Install**（AVP 1001, Grouped）：
- 功能：激活、安装或修改PCC规则（PCRF→PCEF）
- 安装新规则或修改已安装规则：使用Charging-Rule-Definition
- 激活预定义规则：使用Charging-Rule-Name或Charging-Rule-Base-Name
- GPRS场景：包含Bearer-Identifier
- 可含Rule-Activation-Time/Rule-Deactivation-Time控制生效时间

**Charging-Rule-Remove**（AVP 1002, Grouped）：
- 功能：去激活或删除PCC规则（PCRF→PCEF）
- 使用Charging-Rule-Name删除特定PCC规则
- 使用Charging-Rule-Base-Name去激活预定义规则组

---

### K139: Online AVP与Offline AVP [协议]
> 来源: K158, K226

**Online AVP**（AVP 1009, 枚举型）：
- DISABLE_ONLINE (0)：PCC规则在线计费接口禁用
- ENABLE_ONLINE (1)：PCC规则在线计费接口使能
- 在initial CCR中：指示PCEF预配置的在线计费方式是否可用
- 在initial CCA中：指示默认在线计费方式，PCRF下发的优先级高于PCEF预配置

**Offline AVP**（AVP 1008, 枚举型）：
- DISABLE_OFFLINE (0)：PCC规则离线计费接口禁用
- ENABLE_OFFLINE (1)：PCC规则离线计费接口使能
- 规则同Online AVP

**互斥规则**：offline和online不能同时为true，但可同时为false（不计费）。两者都不存在或都为false时，使用PDU会话的默认计费方法。PCF下发的优先级高于SMF本地配置。

---

### K140: Metering-Method AVP [协议]
> 来源: K227

Metering-Method AVP（AVP 1007, 枚举型）定义离线计费的计量参数：

| 取值 | 含义 |
|------|------|
| DURATION (0) | 测量持续时间 |
| VOLUME (1) | 测量流量 |
| DURATION_VOLUME (2) | 同时测量持续时间和流量 |

- PCEF在decentralized unit determination中将该AVP用于在线计费
- 删除后之前提供的信息保持有效；之前未提供则使用PCEF预配置的默认计量方法

---

### K141: Reporting-Level AVP [协议]
> 来源: K228

Reporting-Level AVP（AVP 1011, 枚举型）定义PCEF上报配额的等级：

| 取值 | 含义 | 条件 |
|------|------|------|
| SERVICE_IDENTIFIER_LEVEL (0) | 基于SID+RG联合等级 | CRD中提供Service-Identifier和Rating-Group |
| RATING_GROUP_LEVEL (1) | 基于费率组等级 | CRD中提供Rating-Group |

未携带但之前已提供，则之前的值保持有效。未携带且之前未提供，使用PCEF预配置的默认上报等级。

---

### K142: Rating-Group AVP [协议]
> 来源: K229

Rating-Group AVP（AVP 432, Unsigned32类型）：
- 包含费率组的标识
- 同一费率类型的所有业务属于同一费率组
- 请求相关的特定费率组被联合的Service-Context-Id和Rating-Group AVPs唯一标识
- 参考：RFC 4006 8.29章节

---

### K143: Event-Trigger AVP关键计费触发器 [协议]
> 来源: K233

Event-Trigger AVP（AVP 1006, 枚举型）与计费相关的关键触发器：

| 取值 | 名称 | 计费关联 |
|------|------|----------|
| 0 | SGSN_CHANGE | SGSN变更触发PCC规则更新 |
| 2 | RAT_CHANGE | RAT变更触发PCC规则更新 |
| 4 | PLMN_CHANGE | PLMN变更触发PCC规则更新 |
| 13 | USER_LOCATION_CHANGE | 用户位置变更（CGI/SAI/RAI/TAI/ECGI） |
| 14 | NO_EVENT_TRIGGERS | PCRF不需要事件触发通知 |
| 17 | REVALIDATION_TIMEOUT | 重新验证超时触发 |
| 25 | UE_TIME_ZONE_CHANGE | UE时区变更 |
| 26/27 | TAI_CHANGE | TAI变更 |
| 27/28 | ECGI_CHANGE | ECGI变更 |
| 28/29 | CHARGING_CORRELATION_EXCHANGE | 上报接入网计费标识 |
| 26/33 | USAGE_REPORT | 配额监控上报 |
| 39 | APPLICATION_START | 应用流量检测开始 |
| 40 | APPLICATION_STOP | 应用流量检测结束 |
| 45 | ACCESS_NETWORK_INFO_REPORT | 接入网络信息上报 |
| 101 | TETHERING_REPORT | Tethering检测上报 |
| 1003 | CELL_CONGESTION_CHANGE | 小区状态变更（华为私有） |

USAGE_REPORT触发器与Usage Monitoring（FUP）直接关联：PCRF下发Monitoring-Key+Granted-Service-Unit，PCEF上报Used-Service-Unit。

---

### K144: PCF下发的计费参数全集（ChargingData） [原理]
> 来源: K157

PCF通过ChargingData动作组下发计费参数：

| 参数 | 含义 | 必选 |
|------|------|------|
| chgId | 计费控制策略数据标识 | 必选(1次) |
| meteringMethod | 离线计量方式：DURATION/VOLUME/DURATION_VOLUME/EVENT | 可选 |
| offline | 是否离线计费 | 可选 |
| online | 是否在线计费 | 可选 |
| ratingGroup | 费率组(RG) | 可选 |
| reportingLevel | 上报级别：SER_ID_LEVEL/RAT_GR_LEVEL/SPON_CON_LEVEL | 可选 |
| serviceId | 服务标识(SID) | 可选 |
| sponsorId | 赞助商标识 | 可选 |
| sdfHandl | 在线等待信用响应时是否允许通过 | 可选(仅在线) |

---

### K145: 5G动态规则必配动作组 [配置]
> 来源: K160

5G DynamicPccRule完整配置需7种动作类型：

1. FlowDescription（流描述）
2. FlowInformation（流信息）
3. TrafficControlData（flowStatus=enabled，配流描述时必须配）
4. Arp（优先级参数）
5. QoSData（带宽参数：5qi, maxbrUl, maxbrDl）
6. UsageMornitoringData（配额监控键值，业务关联配额时必须通过5G动作组下发）
7. DynamicPccRule（汇总动作）

4G/5G差异：条件组Object选择4G选"IPSession"，5G选"SmfSession"；策略类型4G为"Gx Policy"，5G为"N7 Policy"。

---

### K146: 三种规则类型对比（动态/预定义/本地） [原理]
> 来源: K16, K159

| 维度 | 动态规则 | 预定义规则 | 本地规则 |
|------|----------|------------|----------|
| 规划位置 | PCF | UPF+SMF+PCF | UPF+SMF |
| 策略决策者 | PCF | PCF | SMF |
| 流条件 | PCF配置 | UPF配置 | UPF配置 |
| 流动作 | PCF配置 | UPF配置 | UPF配置 |
| 规则名一致性 | 不需要 | PCF/SMF/UPF三侧一致 | SMF/UPF两侧一致 |
| 业务识别 | 不识别（非定向流） | UPF识别（三四层+七层） | UPF识别 |
| 计费控制 | PCF通过ChargingData下发 | UPF本地配置计费动作 | UPF本地配置 |
| 七层支持 | **不支持** | **支持** | **支持** |
| 适用场景 | 非定向流、达量限速 | 定向流（需识别特定业务） | PCF故障降级方案 |

使用场景：
- 有PCF → 动态规则+预定义规则
- 无PCF或PCF故障 → 本地规则
- 需要七层匹配 → 必须用预定义规则或本地规则

---

## 第十章：规则匹配与业务识别

### K147: 过滤条件体系 [原理]
> 来源: K14

| 过滤条件类型 | 说明 |
|------------|------|
| 三四层过滤 | 网络层/传输层协议、端口号、IP地址 |
| 七层过滤 | URL、User-Agent、method等应用层关键字段 |
| 协议/协议组 | HTTP、RTSP等应用层协议或协议组合 |
| 流过滤器 | 以上三种的组合，实现过滤逻辑 |

关键规则：
- 每条规则只能绑定一个流过滤器
- 流过滤器是其他过滤条件的集合
- 报文必须符合规则下**所有**过滤条件才算匹配成功

---

### K148: 策略类型分类 [原理]
> 来源: K15

| 策略类型 | 含义 | 典型用途 |
|---------|------|---------|
| PCC | 计费与策略控制 | 计费、禁止访问、重定向 |
| BWM | 带宽管理 | 带宽分类、限速 |
| HEADEN | 头增强 | HTTP/RTSP报文头插入字段 |
| WEBPROXY | Web代理 | 服务器地址池设置 |
| SMARTREDIRECT | 智能重定向 | CaptivePortal、DNS重写 |

关键规则：一条规则只能绑定一条策略；可按绑定的策略类型分类规则（PCC规则、BWM规则等）。

---

### K149: 规则匹配原则 [原理]
> 来源: K17, K254

1. 所有报文按规则优先级逐条匹配
2. 报文必须符合一条规则**所有**过滤条件才算成功匹配
3. **不同类型**的规则会同时匹配，每种类型至多匹配一条
4. 多个PDR时取优先级最高的PDR
5. 动态PDR与预定义PDR优先级相同时，**动态PDR优先级高于预定义PDR**

匹配维度：
- 不同类型规则间独立匹配（PCC/BWM/HEADEN各自匹配）
- 同类型规则间按优先级先后匹配，直到有一条匹配成功或全部失败

---

### K150: UPF支持的流动作组合 [原理]
> 来源: K18

UPF支持的"流"动作：计费、带宽管理、头增强、QoS等。
- 支持单个动作（仅计费）
- 支持多个动作组合（计费+FUP等）

---

### K151: 静态规则的关键一致性约束 [配置]
> 来源: K19

对于同一个预定义规则：
1. PCF、SMF和UPF上**规则标识名称**必须一致
2. SMF和UPF上的**URR ID**必须一致

这是配置正确性的前提条件。

**隐性规则**：SMF配预定义规则级则UPF配规则级；SMF配规则组级则UPF须配规则组级。

---

### K152: 预定义规则安装流程 [协议]
> 来源: K20

1. 用户开机 → PDU会话创建请求
2. SMF选择PCF → 建立SM策略偶联 → 获取SM策略
3. PCF决策 → 向SMF下发**预定义规则名称**（如Prerule01、Prerule02等）+ 动态规则 + Triggers
4. SMF选择UPF → 会话建立请求（携带预定义规则名称）
5. UPF安装预定义规则及动态规则 → 返回响应

UPF成功安装后：对接收到的报文进行业务识别 → 判断是否满足规则中的过滤条件 → 满足后按照规则关联的动作处理。

---

### K153: Usage Monitoring机制 [方案设计]
> 来源: K21

在PCF侧：向SMF下发UmData（Usage Monitoring Data），用于监控业务使用量；根据累计流量决定下发/删除规则。

在SMF侧：将UmData转换成MK（Monitoring Key）URR传递给UPF；达到上报阈值时将UPF上报的业务流量转发给PCF。

在UPF侧：对匹配的业务流量统计到对应的流量统计容器（URR）中；达到上报阈值时向SMF上报。

方案设计示例（A视频专项流量包）：
- 套餐1（视频专项）：优先计入30G A视频流量，URL+七层匹配，PCC策略
- 套餐2（视频FUP）：每天2000M以内100Mbps，超过后25Mbps，需规则动态替换
- 套餐3（通用流量）：三四层any+七层any，PCC策略
- 套餐4（通用FUP）：20G以内50Mbps，超过后1Mbps，需规则动态替换

---

### K154: 流量触发的规则动态替换 [方案设计]
> 来源: K22

当用户流量累计达到阈值时，PCF会动态更新规则：

1. PCF更新规则（删除旧规则，安装新规则）
2. SMF/UPF删除旧规则并安装新规则
3. 新规则生效后，后续报文按新策略处理

示例：
- A视频流量累计达2000M → 删除Prerule02(100Mbps) → 安装Prerule03(25Mbps)
- 通用流量累计达20G → 删除Prerule05(50Mbps) → 安装Prerule06(1Mbps)

---

### K155: 动态规则不支持七层的根本原因 [原理]
> 来源: K23

PCF作为策略控制实体，不处理用户数据报文，因此不具备七层识别能力。
UPF作为业务感知及策略执行的实体，支持通过协议特征库/解析库识别业务。

对于需要七层识别（如A视频业务的HTTP+URL特征）的场景，**必须使用预定义规则或本地规则**。

---

### K156: PDR核心定义与信息构成 [原理]
> 来源: K250

PDR（Packet Detection Rule，流检测规则）是SMF在PFCP会话建立过程中下发给UPF的，用于指示UPF识别流及流处理动作的属性集合。

| 参数 | 说明 |
|------|------|
| PDI（Packet Detection Information） | 流匹配信息，包含报文方向（source interface: 0=上行, 1=下行）和filter（SDF Filter / Application ID）。入口数据流量的对应字段与PDI中所有匹配条件全部匹配则命中 |
| FAR ID | 指示转发动作FAR ID（转发动作包含转发、缓存、重传、丢弃等） |
| QER ID | 指示流控类动作的QER ID（流控类动作如CAR） |
| URR ID | 指示统计上报类动作的URR ID |
| Precedence | PDR优先级 |
| Activate Predefined Rules | 预定义规则名称 |

PDI/FAR/QER/URR通过PDR聚合：PDI负责匹配，FAR/QER/URR分别负责转发/流控/计费动作。

---

### K157: PDR两大类型——动态PDR与预定义PDR [原理]
> 来源: K251

| 类型 | 组成 | 特点 |
|------|------|------|
| 动态PDR | PDI + FAR + QER + URR + Precedence | 所有匹配条件和动作由SMF动态下发 |
| 预定义PDR | PDI + FAR + QER + URR + Precedence + Activate Predefined Rules | 携带预定义规则名，UPF匹配本地配置 |

预定义PDR的关键特性：
- 一条预定义PDR可携带多个Activate Predefined Rules
- Activate Predefined Rules可以是UPF/PGW-U本地配置的userprofile名称，或者是本地配置的rule名称

---

### K158: PDR匹配机制——数据流转发过程中的匹配位置 [方案设计]
> 来源: K253

1. **PDR下发**：SMF向UPF下发一组PDR（通过PFCP Session Establishment Request消息），至少包含一个access类型PDR（上行）和一个core类型PDR（下行）
2. **报文到达**：用户数据报文发送至UPF
3. **会话匹配**：UPF对用户报文进行PDR匹配，查找用户所属PDU Session
4. **PDR命中**：UPF根据PDR优先级、报文关键信息（域名、IP等）进行PDR匹配
5. **动作执行**：UPF根据PDR中的相关信息或本地配置的相关规则信息，执行数据流的相关动作并转发

---

### K159: 动态PDR的两种匹配方式——动态rule vs ADC rule [原理]
> 来源: K255

| 方式 | SDF filter | Application ID | 匹配逻辑 | 动作执行 |
|------|-----------|----------------|----------|----------|
| 动态rule | 携带转发匹配条件 | 不携带 | 按SDF filter匹配报文 | 按PDR中对应动作执行流转发 |
| ADC rule | "Permit out ip from any to assigned" | 携带 | 根据Application ID匹配本地配置的Flowfilter/Flowfilter Group | 按本地的Flowfilter/Flowfilter Group配置执行流动作 |

关键区别：动态rule直接用SDF filter匹配报文字段；ADC rule通过Application ID间接匹配本地配置的Flowfilter/Flowfilter Group。

---

### K160: 预定义PDR匹配方式 [原理]
> 来源: K256

- UPF根据Activate Predefined Rules值匹配本地配置的**userprofile**或本地配置的**rule**
- 命中该PDR后，UPF按照userprofile或rule进行带宽、计费等策略控制

---

### K161: PDR与本地规则的映射关系（分流场景） [原理]
> 来源: K257

在分流特性中，PDR通过Application ID与本地配置的分流规则建立映射关系：

- 映射方式：PDR中的Application-ID值对应本地分流规则的flowfilter或flowfiltergroup名称
- 执行顺序：数据报文先匹配flowfilter/flowfiltergroup，根据Application-ID检索到分流PDR，然后按照PDR中的FAR（转发规则）、QER（QoS规则）执行策略动作
- 即：**报文 → flowfilter/flowfiltergroup匹配 → App ID → 检索PDR → 执行FAR/QER/URR动作**

---

## 第十一章：Usage Monitoring与FUP

### K162: Usage-Monitoring-Information AVP结构 [协议]
> 来源: K230

Usage-Monitoring-Information AVP（AVP 1067, Grouped类型）包含配额监控信息：

| 子信元 | 功能 |
|--------|------|
| Monitoring-Key | 监控键值，标识一个配额监控实例 |
| Granted-Service-Unit | CHF/PCRF授权的服务单元（配额） |
| Used-Service-Unit | PCEF/SMF已使用的服务单元 |
| Usage-Monitoring-Level | 监控级别（Session级/PCC规则级） |
| Usage-Monitoring-Report | 上报指示 |
| Usage-Monitoring-Support | 监控支持指示 |

---

### K163: Usage-Monitoring-Level AVP [协议]
> 来源: K231

Usage-Monitoring-Level AVP（AVP 1068, 枚举型）：

| 取值 | 含义 |
|------|------|
| SESSION_LEVEL (0) | 配额监控实例应用于整个IP-CAN会话（会话级FUP） |
| PCC_RULE_LEVEL (1) | 配额监控实例应用于一个或多个PCC规则（业务级FUP） |

默认值：未提供时指示PCC_RULE_LEVEL (1)。

---

### K164: Usage-Monitoring-Report AVP [协议]
> 来源: K232

Usage-Monitoring-Report AVP（AVP 1069, 枚举型）：
- USAGE_MONITORING_REPORT_REQUIRED (0)：PCRF指示PCEF应该上报累积流量
- 用于PCRF在RAR/CCA中请求PCEF上报特定监控键值的累积流量（无论门限是否到达）

---

### K165: 会话级FUP vs 业务级FUP对比 [原理]
> 来源: K169

| 维度 | 会话级FUP | 业务级FUP |
|------|-----------|-----------|
| 监控范围 | 用户所有业务 | 特定业务(三四层/七层) |
| N7信元位置 | sessRules.refUmData | PccRule.refUmData |
| URR绑定 | 关联到**所有PDR** | 绑定到**指定业务流PDR** |
| MONITORINGKEY | 动态规则时由PCF下发 | ADD URR中必选配置 |
| UNC/UDG配置量 | 仅需License开关 | 需完整三件套+两套策略 |
| License(UNC) | LKV3W9PCBT12 | LKV2FUPSAT01 |
| License(UDG) | LKV3G5PCBT01 | LKV3G5FPBS01 |

---

### K166: FUP配额驱动策略切换机制 [方案设计]
> 来源: K170

FUP核心机制：配额状态驱动策略切换：

1. **初始**：PCF下发流量阈值 + 规则（高优先级，低费率/免费）
2. **阈值耗尽**：UPF检测VOLTH触发，上报Usage Report → SMF转发PCF
3. **PCF决策**：
   - 配额未耗尽 → 下发新阈值，维持当前规则
   - 配额耗尽 → **不下发新阈值**(refUmData=NULL)，更新QoS(限速/重定向)，切换到低优先级规则(高费率)

**隐性规则**：FUPSESSIONEXC=ENABLE的业务流量**不参与会话级FUP累计**，避免双重计量。

---

### K167: 业务级FUP三件套扩展模型 [配置]
> 来源: K171

业务级FUP是标准三件套的**扩展版本**，需配配额耗尽前/后**两套策略**：

**三组URR：**
1. urr_mk：URRID=1000, USAGERPTMODE=MONITORINGKEY, MONITORINGKEY="2001"（累计流量监控）
2. urr_basic：URRID=2000, USAGERPTMODE=ONLINE, RG=10（配额耗尽前，免费）
3. urr_exhaust：URRID=3000, USAGERPTMODE=ONLINE, RG=20（配额耗尽后，1元/M）

**两套PCCPOLICYGRP：**
- cg_basic：绑定urrg_basic(urr_mk + urr_basic)，FUPSESSIONEXC=ENABLE
- cg_exhaust：绑定urrg_exhaust(urr_mk + urr_exhaust)，FUPSESSIONEXC=ENABLE

**两条RULE：** rule_test1(绑定cg_basic, PRIORITY=30) + rule_test2(绑定cg_exhaust, PRIORITY=40)

---

### K168: FUP URR ID与UMID映射机制 [原理]
> 来源: K172

SMF建立URR ID与UMID之间的映射：
- 预定义规则：通过ADD URR命令配置URR ID和MONITORINGKEY
- 动态规则：SMF直接将PCF下发的UMID转换为URR ID

映射流转路径：UPF检测VOLTH触发 → Usage Report(含URR ID, Volume Measurement) → SMF通过URR ID→UMID映射 → Npcf_SMPolicyControl_Update(accuUsageReports含refUmId, volUsage) → PCF决策

---

## 附录：跨协议映射关系摘要

### Gx → Nchf → N4 参数映射链

| Gx AVP | Nchf N40信元 | N4 PFCP信元 |
|--------|-------------|-------------|
| Online=ENABLE_ONLINE | quotaManagementIndicator=ONLINE_CHARGING | Create URR含Volume/Time/Event Quota |
| Online=DISABLE_ONLINE | quotaManagementIndicator=OFFLINE_CHARGING | Create URR不含配额信元 |
| Metering-Method=DURATION | grantedUnit.time | Time Quota |
| Metering-Method=VOLUME | grantedUnit.totalVolume | Volume Quota |
| Metering-Method=DURATION_VOLUME | grantedUnit.time+totalVolume | Time Quota+Volume Quota |
| Rating-Group | multipleUnitUsage.ratingGroup | (SMF映射到URR ID) |
| Reporting-Level=SERVICE_IDENTIFIER_LEVEL | UsedUnitContainer.serviceId+ratingGroup | (N4无对应，SMF层处理) |
| Reporting-Level=RATING_GROUP_LEVEL | UsedUnitContainer.ratingGroup | (N4无对应，SMF层处理) |
| Monitoring-Key | (5G: UsageMonitoringData动作组) | (5G: 独立UM URR) |
| Usage-Monitoring-Level=SESSION_LEVEL | (5G: 会话级UM) | (5G: 会话级UM URR) |
| Usage-Monitoring-Level=PCC_RULE_LEVEL | (5G: 业务级UM) | (5G: 业务级UM URR) |

### Trigger映射链

| Gx Event-Trigger | Nchf Trigger Type | N4 Reporting Trigger |
|-------------------|-------------------|---------------------|
| USAGE_REPORT | (Usage Monitoring机制) | (配额阈值/耗尽触发) |
| USER_LOCATION_CHANGE | USER_LOCATION_CHANGE | (SMF层Query URR) |
| REVALIDATION_TIMEOUT | VALIDITY_TIME | (SMF本地定时器) |
| (配额相关) | QUOTA_THRESHOLD | VOLTH / TIMTH |
| (配额相关) | QUOTA_EXHAUSTED | VOLQU / TIMQU |
| (配额保持) | - | QUHTI |

---

## 知识统计

| 章节 | 知识条目 | 数量 |
|------|----------|------|
| 第七章：Nchf融合计费服务 | K101-K121 | 21 |
| 第八章：PFCP/N4接口与URR | K122-K135 | 14 |
| 第九章：Gx/PCC策略与计费 | K136-K146 | 11 |
| 第十章：规则匹配与业务识别 | K147-K161 | 15 |
| 第十一章：Usage Monitoring与FUP | K162-K168 | 7 |
| **合计** | K101-K168 | **68** |

### 按类型统计

| 类型 | 数量 | 编号 |
|------|------|------|
| [协议] | 30 | K101, K103, K104, K107, K109, K110, K114-K119, K123-K125, K127-K130, K132-K135, K137, K138, K140-K143, K152, K162-K164 |
| [原理] | 17 | K112, K122, K144, K146-K150, K155-K157, K159-K161, K165, K168 |
| [隐性规则] | 4 | K105, K108, K111, K151 |
| [方案设计] | 10 | K106, K113, K120-K121, K153, K154, K158, K166 |
| [配置] | 7 | K102, K123, K136, K145, K151, K167 |

### 融合去重记录

| 新编号 | 融合来源 | 说明 |
|--------|----------|------|
| K101 | K04 + K190 | 四种服务操作合并 |
| K102 | K08 + K51 + K191 | CHF选择优先级保留6级版本 |
| K103 | K53 + K192 | Create Request信元合并 |
| K104 | K53 + K193 | Create Response信元合并 |
| K105 | K54 + K194 | 在线/离线信元差异合并 |
| K106 | K55 + K197 | Update触发场景合并 |
| K108 | K56 + K200 | Trigger全集与优先级合并 |
| K109 | K57 + K201 | Release流程合并 |
| K110 | K59 + K202 | Notify通知合并 |
| K112 | K195 + K258 | RG与URR ID映射合并 |
| K123 | K209 + K210 + K211 | URR生命周期三阶段合并 |
| K131 | K49 + K205 + K220 | QHT三来源合并 |
| K136 | K63 + K159 | PCC规则类别合并 |
| K139 | K158 + K226 | Online/Offline AVP合并 |
| K146 | K16 + K159 | 三种规则类型对比合并 |
| K149 | K17 + K254 | 规则匹配原则合并 |

---


## 第十二章：融合计费配置全景

### K201: 融合计费配置五层嵌套模型 `[隐性规则]`
> 来源: K114 (归纳自故障案例1-3)

融合计费配置是五层嵌套结构，任何一层配置错误都导致下游功能异常：

| 层级 | 配置项 | 命令 | 说明 |
|------|--------|------|------|
| L1 计费模式 | CHGMODE | SET CHGMODE | 设为NchfMode才走N40接口 |
| L2 融合计费使能 | CHARGECTRL | SET CHARGECTRL / SET USRPROFCHARGE / SET APNCHARGECTRL | 按用户/APN粒度使能 |
| L3 CHF交互使能 | CHFINIT | SET CHFINIT | 设为SENDREQ才在激活时发Initial |
| L4 RG配置 | URR/URRGROUP | ADD/MOD URR / ADD/MOD URRGROUP | 定义RG和计费方式 |
| L5 Rule绑定 | RULE/PCCPOLICYGRP | ADD/MOD RULE / ADD/MOD PCCPOLICYGRP | 将RG绑定到业务匹配规则 |

---

### K202: 方案一组网与12步配置依赖链 `[方案设计]`
> 来源: K132

未部署NCG方案：网络侧仅SMF，运营商侧部署CHF(OCS)。仅支持融合计费，SGW-C不支持。

**SMF侧配置依赖链（12步顺序）**：
1. SET LICENSESWITCH（License）
2. SET CHARGECTRL（融合计费开关）
3. SET CHGMODE（接口模式=NchfMode）
4. ADD CHARGECHAR / SET GLBCHARGECHAR（计费属性CC）
5. ADD CCT / MOD CCT（融合计费模板）
6. ADD PDUTRIGGER / ADD RGTRIGGER（Trigger交互条件）
7. SET N40APIVER（N40 API版本）
8. SET FAILHANDLING / ADD PDUSCACT / ADD RGRCACT（异常处理）
9. ADD URR / ADD URRGROUP / ADD PCCPOLICYGRP（费率标识三件套）
10. ADD TARIFFGROUP（费率切换，可选）
11. ADD TNFINS / ADD TNFGRP / SET CHFSELECTMODE（CHF选择）
12. SET N40MSGSTG（消息缓存，可选）

**网元协同**：UPF(规则/URR/策略) + PCF(配额/规则/策略) + SMF三方配置必须一致。

---

### K203: 计费License项 `[配置]`
> 来源: K133

| 特性 | License控制项 |
|------|-------------|
| 融合计费 | WSFD-011206 |
| 内容计费 | LKV3W9BCC12 |
| 时长计费 | LKV3W9TBCS12 |
| 流量计费 | LKV3WPVBCS11 |
| 事件计费 | LKV3W9EBCS12 |

命令：SET LICENSESWITCH，必须最先配置。

---

### K204: 融合计费开关配置 `[配置]`
> 来源: K134

优先级：PCF下发 > User Profile(SET USRPROFCHARGE) > DNN(SET APNCHARGECTRL) > 计费属性(ADD CHARGEMETHOD) > 全局(SET CHARGECTRL)

**SET CHARGECTRL关键参数**：
- HOMECONVERGED/VISITCONVERGED/ROAMCONVERGED=ENABLE（对应的ONLINE/OFFLINE必须DISABLE）
- RGAPPLIED：业务申请上报模式（ONLINERGONLY / OFFLINERGONLY / DEFAULT）

**RGAPPLIED约束（隐性规则）**：
- RGAPPLIED=DEFAULT时：URRGROUP中**不能**同时配RG相同的离线和在线URR
- RGAPPLIED=ONLINERGONLY或OFFLINERGONLY时：建议同时配离线和在线URR

---

### K205: 计费接口模式全景 `[配置]`
> 来源: K135, K272, K273, K274, K275, K276, K277

#### 接口选择优先级

计费接口选择有三级优先级（从高到低）：
1. **基于用户漫游属性** (ADD ROAMCHGMODE) — 最高优先级
2. **基于APN/DNN** (ADD APNCHGMODE) — 中等优先级
3. **全局配置** (SET CHGMODE) — 最低优先级（兜底）

策略接口选择有两级优先级：基于APN/DNN > 全局配置。

#### SET CHGMODE按终端和接入类型选择

SET CHGMODE命令通过TMACCTYPE（终端和接入类型）参数区分不同场景：
- **UE5G_RAT5G**：5G终端接入5G网络（SMF场景，典型用NchfMode）
- **UE5G_RAT4G**：5G终端接入4G网络（PGW-C场景，可选NchfMode或GaGyMode）
- **UENON5G_RAT4G**：非5G终端接入4G网络（PGW-C场景，典型用GaGyMode）
- **RAT2G/RAT3G**：2G/3G接入（GGSN场景，典型用GaGyMode）
- **RATNBIOT**：NB-IoT终端接入
- **RATLTEM**：LTE-M终端接入
- **NON_3GPP**：非3GPP网络接入

FORCED参数指定计费接口：NchfMode（融合计费）或GaGyMode（传统离线+在线）。

#### 5GS互操作指示(BY5GSIWKI)

BY5GSIWKI参数控制是否根据对端携带的"5GS Interworking Indication"参数选择计费接口：
- BY5GSIWKI=True时：对端携带"5GS Interworking Indication"为1则选Nchf，为0或未携带则选GaGy
- BY5GSIWKI=False时：不根据互操作指示判断，直接使用FORCED指定的计费接口
- 典型用法：ADD APNCHGMODE中按APN级别配置，5G终端4G接入时根据互操作指示灵活选择

#### V-SMF和I-SMF的计费模式

SET CHGMODE中与SMF角色相关的参数：
- **FORVSMFONLY**：UNC作为V-SMF时的计费模式，典型配置NchfMode
- **ISMFCHGSW**：I-SMF是否支持计费，典型配置DISABLE（I-SMF不进行计费）

#### 基于PCF实例标识决策接口(ADD PCCCHGMODEBYPCFID)

当需要基于PCF实例标识调整用户最终使用的计费/策略接口时使用：
- 以SET CHGMODE或ADD APNCHGMODE为初选结果
- 在此基础上决策：是否由N40回落GaGy，或由GaGy升级为N40
- 策略接口类型：N7（5G PCF）或Gx（4G PCRF）
- 计费接口类型：INHERIT（继承初选结果）或指定N40/GaGy

#### SET POLICYMODE策略接口选择

- FORCED=Npcf：使用5G PCF（N7服务化接口）
- FORCED=Gx：使用4G PCRF（Diameter接口）
- PCFRESELBYPCFID：是否基于PCF实例标识决策策略接口类型
- 典型配置：5G终端4G接入和非5G终端4G接入用Npcf，2G/3G/NB-IoT/LTE-M/非3GPP用Gx

#### 2/3/4/5G共存网络典型配置

| 接入场景 | UNC角色 | 计费接口 | 策略接口 |
|----------|---------|---------|---------|
| 5G终端+5G接入 | SMF | NchfMode | Npcf |
| 5G终端+4G接入 | PGW-C | 按互操作指示选Nchf/GaGy | Npcf |
| 非5G终端+4G接入 | PGW-C | GaGyMode | Npcf或Gx |
| 2G/3G接入 | GGSN | GaGyMode | Gx |
| NB-IoT/LTE-M | GGSN/PGW-C | GaGyMode或NchfMode | Gx或Npcf |

---

### K206: CC属性配置全景 `[配置]`
> 来源: K136, K259, K260, K261

#### CC标准取值

| 取值 | 含义 |
|------|------|
| 0x0100 | 热计费(Hot Billing) |
| 0x0200 | 统一费率(Flat Rate) |
| 0x0400 | 预付费(Prepaid) |
| 0x0800 | 普通计费(Normal Billing) |

#### CC四级优先级

| 优先级 | 来源 | 说明 |
|--------|------|------|
| 1（最高） | UserProfile下的配置 | 用户级配置 |
| 2 | APN/DNN下的配置 | 接入点级配置 |
| 3 | 全局配置 | 全局默认 |
| 4（最低） | normal（普通计费） | 兜底默认 |

如果高级别参数没有配置，则依次向下使用低一级别的参数取值。

CC来源优先级补充：RADIUS Server下发 > User Profile > DNN > 全局 > normal(默认)

命令：SET GLBCHARGECHAR(全局) / ADD CHARGECHAR(CC实例) / SET USRPROFCHARGE(绑定UP) / SET APNCHARGECTRL(绑定DNN)

#### 本地CC与签约CC的选择控制

本地CC与签约CC的选择受两类命令控制，核心参数为HOMESGSN、ROAMSGSN、VISITSGSN（分别控制本地、漫游、拜访用户）：

| 场景 | 控制命令 | ENABLE含义 | DISABLE含义 |
|------|----------|-----------|------------|
| 基于UserProfile/APN/DNN配置CC | ADD CHARGECHAR | 使用签约下发的CC | 使用本地配置的CC |
| 基于全局配置CC | SET GLBCHARGECHAR | 使用签约下发的CC | 使用本地基于全局配置的CC |

决策逻辑：先按四级优先级确定本地CC，再根据HOMESGSN/ROAMSGSN/VISITSGSN的ENABLE/DISABLE决定是否用签约CC覆盖本地CC。

#### 各网络制式下签约CC的来源网元

| 网络制式 | UNC角色 | 签约CC来源 |
|----------|---------|-----------|
| 5G | SMF | UDM下发 |
| 4G（SP合设） | SGW-C + PGW-C | 左侧MME携带（MME从HSS获取） |
| 4G（SP分离，UNC=SGW-C） | SGW-C | 左侧MME携带 |
| 4G（SP分离，UNC=PGW-C） | PGW-C | 左侧SGW-C携带 |
| 2/3G | GGSN | 左侧SGSN携带 |

规律：4G网络中签约CC统一由左侧MME/SGW-C携带；5G由UDM下发；2/3G由SGSN携带。

---

### K207: 融合计费模板(CCT)配置 `[配置]`
> 来源: K137

CCT模板粒度优先级：User Profile > DNN > 计费属性(CC) > global(整机)

**ADD CCT关键参数**：
- QHT：配额空闲时间门限(秒)
- VQT/TQT/UQT：流量/时间/事件阈值触发百分比
- VT：在线配额有效时长(分)
- PDUVOLUMELIMIT/PDUTIMELIMIT：PDU级阈值
- RGVOLUMELIMIT/RGTIMELIMIT：RG(业务)级阈值
- MAXSVCCONTAINER：最大业务容器数
- FUATERMINATE：最终配额动作终结方式

绑定：ADD SELECTCCTBYCC(CC粒度) / SET APNCHARGECTRL(DNN粒度) / SET USRPROFCHARGE(UP粒度)

---

### K208: Trigger配置 `[配置]`
> 来源: K138

**SET CHFINIT**：PDU会话建立时是否与CHF交互
- CHFINIT=SENDREQ：激活时发送Initial
- CCRINITRGNUM：初始RG个数
- RGSOURCE：RG来源（DEFAULT / CTXSTARTRATING）

**Trigger三级取值**：IMMEDIATE(立即上报) / DEFERRED(延迟上报) / NONREPORT(不上报)

**Session级Trigger (ADD PDUTRIGGER)**：QOSCHG, ULCHG, SRVNDCHG, PLMNCHG, RATCHG, TAICHG, TIMELIMIT, VOLUMELIMIT, EVENTLIMIT, SESSAMBRCHG, ADDUPF

**RG级Trigger (ADD RGTRIGGER)**：额外包含QUOTATHRESHOLD(配额阈值), VT(配额有效时长), QHT(配额保持时长)

**隐性规则**：
- Session级和RG级同一Trigger冲突时，Session级优先。Session级"不上报"时才按RG级生效
- Trigger来源：CHF下发（Response的triggers信元）+ SMF本地配置
- 建议每用户上报间隔>30秒，避免SMF和CHF频繁交互

---

### K209: N40 API版本配置 `[配置]`
> 来源: K139

SET N40APIVER：
- APIVER：版本号（如F30），需与CHF一致
- FEATURE：增强功能集，支持&叠加（NODEFUNC-1, NBIOTCHG-1, LTEMCHG-1, UTRANCHG3GPP-1等）

---

### K210: 异常返回码处理配置 `[配置]`
> 来源: K140

异常处理三粒度：整个用户 > PDU会话 > RG

**SET FAILHANDLING**：
- FHACTION=CONTINUE（放通）/ 其他
- FAILOVERSUP=ENABLE（支持failover）
- TXTIMER：Tx定时器时长(秒)
- HOLDINGTIME：用户保持时长(分)
- CNVCHGRECOVER：融合计费自动恢复开关

**ADD PDUSCACT**：PDU级异常返回码动作（如502→FAILOVER）
**ADD RGRCACT**：RG级异常码动作（如QUOTAMNOTAPPL→BLCK_IMMED_RPT）
**SET CNVRGDCHGPARA**：BADRSPACT=CONTINUE/Terminate，忽略CHF响应信元列表

---

### K211: 费率切换配置 `[配置]`
> 来源: K147

粒度优先级：User Profile > APN > CC > 整机

命令：ADD FESTIVAL(节假日) → ADD WEEKDAY(星期表) → ADD TARIFFGROUP(时间段) → SET N40QUOTACTRL(TCMODE: DEFAULT/DAILY/MONTHLY) → 绑定(SET APNCHARGECTRL或SET USRPROFCHARGE)

约束：CCVALUE不能为0x0200(统一费率)，每DNN/UP只能绑一个费率切换组。

---

### K212: 计费消息缓存配置 `[配置]`
> 来源: K148

场景：主备CHF均故障时SMF缓存计费消息。

前提：SET FAILHANDLING的FHACTION=CONTINUE。此功能为定制能力，要求对端为华为NCG。

命令：SET N40MSGSTG(缓存开关+回放间隔/速率) → SET STGTRIGGER(缓存期间trigger) → SET CNVRGDCHGPARA(CHGDATAREFGEN=SMF) → SET CDRSTORAGECTRL(超期天数) → SET N4CHGMSGCTRL(缓存池扩展)

---

### K213: CHF选择配置全景 `[配置]`
> 来源: K145, K155, K156

#### CHF选择优先级（高到低）

1. ADD SELCHFGBYIMSI（基于IMSI，测试用）
2. ADD SELCHFGBIMSISEG（基于IMSI号段）
3. 基于PCF下发FQDN
4. 基于UDM签约CC
5. 基于标准化NRF服务发现
6. ADD SELECTCHFGBYCC（基于SMF本地CC）

配置命令链：ADD TNFINS(CHF实例) → ADD TNFINSIP(IP) → ADD TNFGRP(CHF组) → ADD TNFBINDGRP(绑定) → SET CHFSELECTMODE → SET GLBDFTCHFGROUP → ADD SELECTCHFGBYCC

#### 基于IMSI选择CHF的三层配置

1. ADD TNFINS(CHF实例) + ADD TNFINSIP(IP) — SRVNAME固定取**NchfConvCharg**
2. ADD TNFGRP(CHF组) + ADD TNFBINDGRP(实例绑定组)
3. ADD SELCHFGBYIMSI(IMSI绑定主备CHF组)

#### IMSI-CHF绑定的实时生效限制 `[隐性规则]`

MOD SELCHFGBYIMSI修改后，已激活用户**不会立即**切换CHF。必须去激活后重新激活才能生效。不支持在线切换CHF。

**建议**：配置缺省CHF组避免选不到CHF。FQDN需与PCF下发一致。

---

## 第十三章：计费三件套配置

### K214: 融合计费三件套配置命令 `[配置]`
> 来源: K141

**ADD URR**(SMF侧)：
- URRNAME, URRID（**SMF和UPF必须一致**）
- USAGERPTMODE：ONLINE / OFFLINE
- ONLCOMPOUNDTYPE/OFFCOMPOUNDTYPE：ONLYRG
- ONLINERG/RG：费率组编号
- ONLMETERINGTYPE/OFFMETERINGTYPE：VOLUME / DURATION / FREE

**ADD URRGROUP**：
- URRGROUPNAME
- UPURRNAME1/DOWNURRNAME1：第1组上下行URR
- UPURRNAME2/DOWNURRNAME2：第2组上下行URR（1/2仅为编号，无优先级语义）

**ADD PCCPOLICYGRP**：
- PCCPOLICYGRPNM, URRGROUPNAME

**ADD RULE**：RULENAME, POLICYTYPE=PCC, PRIORITY, POLICYNAME

**ADD QUOTAEXHAUSTACT**：在线RG配额耗尽后动作（BLOCK / REDIRECT / FORWARD）

---

### K215: UPF侧配置流程 `[配置]`
> 来源: K142

UPF配置5步：
1. ADD URR + ADD URRGROUP（URR组）
2. ADD PCCPOLICYGRP（PCC策略组）
3. ADD FILTER / ADD L7FILTER / ADD FLOWFILTER / ADD FLTBINDFLOWF / ADD PROTBINDFLOWF（过滤规则）
4. ADD RULE + ADD USERPROFILE + ADD RULEBINDING
5. SET URRGRPBINDING + SET SPECTRAFURRGRP（默认URR组）

**隐性规则**：
- FLOWFILTER必须绑定过滤条件，否则匹配失败
- 只绑定L34的Rule优先级应**低于**绑定L7的Rule
- any Rule优先级设最低(如65000)
- **SET REFRESHSRV必须最后执行**，否则Filter变更不生效

---

### K216: SET SPECTRAFURRGRP — 特殊流量计费兜底 `[配置]`
> 来源: K143

SET SPECTRAFURRGRP配置全局缺省URR组，用于：
1. 七层未匹配已转发流量（特殊流量）
2. 无URR配置的业务

当BIT1232软参值=1时特殊流量通过该规则组计费。

---

### K217: 跨网元名称一致性要求汇总 `[隐性规则]`
> 来源: K144

| 配置项 | 一致性要求 | 涉及网元 |
|--------|-----------|----------|
| USERPROFILENAME | 必须一致 | PCF, SMF, UPF |
| RULENAME | 必须一致 | SMF, UPF |
| RULE.POLICYTYPE+POLICYNAME | 必须一致 | SMF, UPF |
| URRID | 必须一致 | SMF, UPF |
| USAGERPTMODE | 必须一致 | SMF, UPF |
| ONLMETERINGTYPE/OFFMETERINGTYPE | 必须一致 | SMF, UPF |
| 配额名称(Quota) | PCF配额名须与CHF侧一致 | PCF, CHF |
| FQDN | SMF的TNFINS.FQDN须与PCF下发一致 | SMF, PCF |

---

### K218: 内容计费验证链 `[方案设计]`
> 来源: K149

内容计费逐级验证链：
1. LST RULEBINDING → UserProfile绑定的RULE
2. LST RULE → RULE绑定的FlowFilter和PCCPOLICYGRP
3. LST PCCPOLICYGRP → PCC策略组绑定的URRGROUP
4. LST URRGROUP → URR组中的上下行URR
5. LST URR → 最终URR的ID和计费模式

七层内容计费还需验证：LST PROTBINDFLOWF → LST FLOWFILTER → LST L7FILTER

---

### K219: 内容计费双License要求 `[配置]`
> 来源: K150

内容计费需**两个**License同时开启：
- UNC侧：LKV3W9BCC12
- UDG侧：LKV3G5BCBC01

两处必须均为ENABLE才能正常使用。

---

### K220: URR ID在PFCP信令中的编码规则 `[原理]`
> 来源: K151

Usage Report中URR ID编码：高位80代表URR是预定义类型（UPF本地配置），低位代表UPF本地URR ID。
示例：0x80000001(2147483649) → 预定义标志 + URR ID=01

调测时需做进制转换对照。

---

### K221: 带配额管理的融合计费E2E调测流程 `[方案设计]`
> 来源: K152

端到端调测关键步骤：
1. 双License检查
2. 用户激活 → 验证Initial消息
3. 验证Initial携带的RG
4. 用户访问新业务 → UPF上报新URR ID → SMF下发Create URR
5. Trigger条件满足 → 验证Update消息
6. 用户去激活 → 验证Termination消息中流量一致性

---

### K222: URRFAILACTION — 新业务无URR时的容灾 `[配置]`
> 来源: K153

UNC未配置新业务URR时，新业务被阻塞。通过`SET URRFAILACTION: RETRYFAILACT=CONTINUE`可放通。
这是一个重要容灾配置，允许计费规则未完全配置时仍保障业务可用性。

---

### K223: 计费三件套修改命令链 `[配置]`
> 来源: K154

新业务配额下发失败时，需执行完整修改链：
```
MOD URR → MOD URRGROUP → MOD PCCPOLICYGRP → MOD RULE
```
体现URR→URRGROUP→PCCPOLICYGRP层级修改顺序，最终通过RULE下发给用户。

---

## 第十四章：PCF策略配置

### K224: PCF下发的计费参数全集(ChargingData) `[原理]`
> 来源: K157

PCF通过ChargingData动作组下发计费参数：

| 参数 | 含义 | 必选 |
|------|------|------|
| chgId | 计费控制策略数据标识 | 必选(1次) |
| meteringMethod | 离线计量方式：DURATION/VOLUME/DURATION_VOLUME/EVENT | 可选 |
| offline | 是否离线计费 | 可选 |
| online | 是否在线计费 | 可选 |
| ratingGroup | 费率组(RG) | 可选 |
| reportingLevel | 上报级别：SER_ID_LEVEL/RAT_GR_LEVEL/SPON_CON_LEVEL | 可选 |
| serviceId | 服务标识(SID) | 可选 |
| sponsorId | 赞助商标识 | 可选 |
| sdfHandl | 在线等待信用响应时是否允许通过 | 可选(仅在线) |

---

### K225: offline/online互斥规则 `[隐性规则]`
> 来源: K158

- offline和online**不能同时为true**，但可同时为false（不计费）
- 优先级：PCF下发 > SMF本地配置
- 两者都不存在或都为false时，使用PDU会话的**默认计费方法**
- sdfHandl仅用于在线计费场景
- meteringMethod为离线专用参数

---

### K226: 三种规则类型与计费信息携带方式 `[原理]`
> 来源: K159

| 维度 | 动态规则 | 预定义规则 | 本地规则 |
|------|----------|------------|----------|
| 流条件 | PCF配置 | UPF配置 | UPF配置 |
| 流动作 | PCF配置 | UPF配置 | UPF配置 |
| 规则名一致性 | 不需要 | PCF/SMF/UPF三侧一致 | SMF/UPF两侧一致 |
| 业务识别 | 不识别（非定向流） | UPF识别（三四层+七层） | UPF识别 |
| 计费控制 | PCF通过ChargingData下发 | UPF本地配置计费动作 | UPF本地配置 |
| 适用场景 | 非定向流、达量限速 | 定向流（需识别特定业务） | PCF故障降级方案 |

---

### K227: 5G动态规则必配动作组 `[配置]`
> 来源: K160

5G DynamicPccRule完整配置需7种动作类型：
1. FlowDescription（流描述）
2. FlowInformation（流信息）
3. TrafficControlData（flowStatus=enabled，配流描述时必须配）
4. Arp（优先级参数）
5. QoSData（带宽参数：5qi, maxbrUl, maxbrDl）
6. UsageMornitoringData（配额监控键值，业务关联配额时必须通过5G动作组下发）
7. DynamicPccRule（汇总动作）

4G/5G差异：条件组Object选择4G选"IPSession"，5G选"SmfSession"；策略类型4G为"Gx Policy"，5G为"N7 Policy"。

---

### K228: PCF侧配置流程 `[配置]`
> 来源: K146

PCF融合计费配置流程：
1. 配置配额(Quota) — 名称须与CHF侧一致
2. 配额状态映射 — Sy协议状态(0/1/2/5) → UPCF状态(Normal/Level1/Level2/Exhaust)
3. 配置条件组 — 基于QuotaStatus匹配
4. 配置5G动作组 — PredefinedPccRule类型，pccRuleId指定预定义规则名
5. 配置规则 — 类型"5G Smf Pcc Rule"
6. 配置策略 — 策略类型N7 Policy
7. ADD PSUB(用户) + ADD PSRV(签约业务)

前提：N28接口开关已启用(VRM_SYSWITCH设为1/2/3)。

---

## 第十五章：方案设计知识

### K229: 配额类型与触发器 `[原理]`
> 来源: K161

配额类型（PCF用于策略计算）：
- **流量配额**：UPCF统计的用户业务流量
- **在线时长配额**：UPCF统计的在线会话时长
- **时长配额**：SMF上报的时长

**关键触发器**：
- IPCAN_EST：PDU会话建立（必须配置）
- US_RE：使用量状态上报（配额变化触发策略更新）
- SAREA_CH/PRA_CH/SCELL_CH/PLMN_CH：位置变更
- APP_STA/APP_STP：应用类型变更
- TimeRangeChange：时间范围变更

---

### K230: 多业务拆解6步法 `[方案设计]`
> 来源: K162

多业务拆解方法：**抽取 → 合并 → 排查 → 规则类型判断 → 触发器选择 → 业务关系判断**

关键步骤：
- 合并：条件相同的动作合并或动作相同的条件合并
- 排查：确认条件完备（如"配额未耗尽"+"配额耗尽"=全部状态）
- 触发器选择：IPCAN_EST + US_RE（配额变化）+ 可选TimeRangeChange
- 业务互斥：通过互斥组定义多业务间关系（订购互斥/激活互斥）

---

### K231: 基于用户等级的资费差异化控制 `[方案设计]`
> 来源: K163

用户等级→费率/带宽映射：

| 用户等级 | RatingGroup | 上下行带宽 |
|----------|-------------|------------|
| Gold | RG=1 | 100 Mbps |
| Silver | RG=2 | 50 Mbps |
| Normal | RG=3 | 10 Mbps |

PCF配置：3个规则(Rule_Gold/Silver/Normal)，每个规则动作组包含ChargingData(设置ratingGroup) + QoSData(设置带宽)。用户等级变更由业务发放系统通过订阅通知推送。

---

### K232: 多业务场景配额+时间约束组合 `[方案设计]`
> 来源: K164

场景1（基础流量包）：配额未耗尽→10Mbps；配额耗尽→1Mbps+通知。触发器：IPCAN_EST + US_RE

场景2（周末流量包）：配额未耗尽→100Mbps（仅周末）；配额耗尽→终止业务+通知。触发器：IPCAN_EST + US_RE + **TimeRangeChange**

业务互斥：场景2优先级高于场景1，使用"激活+替换"互斥模式。

---

### K233: 配额耗尽重定向完整控制链 `[方案设计]`
> 来源: K165

配额耗尽后完整控制：**限速(1Kbit/s) + 发送提醒通知 + 重定向到充值页面**

**动态规则方案（仅PCF配置）**：
- Rule_Normal：条件=配额未耗尽，动作=QoSData(100Mbit/s)
- Rule_Exhaust：条件=配额耗尽，动作=QoSData(1Kbit/s) + RedirectInformation

**预定义规则方案（PCF+SMF+UPF三方配置）**：
- PCF侧：下发规则名Rule_Normal和up_Exhaust
- SMF侧：识别预定义规则名，配置URR/URRGROUP/PCCPOLICYGRP/RULE
- UPF侧：配置流过滤器+QoS+重定向URL(ADD REDIRECT)+PCCPOLICYGRP+RULE

**隐性规则**：SMF配预定义规则级则UPF配规则级；SMF配规则组级则UPF须配规则组级。配额耗尽场景需用**预定义规则组**。

---

### K234: FUP达量限速配置实例 `[方案设计]`
> 来源: K166

需求：2000MB配额，<100%时10Mbit/s，>=100%时512Kbit/s。

5G配置方案：
- AG_Basic：SessionRuleAction（缺省QoS Flow）
- AG_Basic_Dyn：DynamicPccRule（rule01, maxbr=10000Kbit/s, umId=2001）
- predefinedPccRule01：pccRuleId=Pre_Quota_exhaust（配额耗尽时激活预定义规则）
- 策略：Policy_usage，trigger=US_RE OR IPCAN_EST
- 配额：quota01, MonitorKey=2001, Value=2048000, Slice=100%

---

## 第十六章：特殊场景

### K235: ULCL多锚点计费全景 `[方案设计]`
> 来源: K167, K168, K262

#### 计费架构

- 主锚点PSA0(Internet) + 辅锚点PSA1(本地DN) + UL CL UPF(分流器，通常与PSA1合设)
- SMF将计费规则通过N4接口分别下发到PSA0和PSA1
- CHF对每个锚点UPF**独立进行配额管理**，每个UPF**独享配额**
- SMF按UPF向CHF申请配额，消息中Multiple Unit Usage携带UPF ID
- **UL CL UPF不计费**：UL CL UPF没有计费规则，仅负责分流

核心原则：UL CL只分流、不计费；计费在锚点UPF按各自的URR独立执行。

#### 系统约束 `[隐性规则]`

- UL CL仅针对5G用户，2/3/4G不支持
- 国漫V-SMF场景下不支持UL CL
- 当前版本仅支持UL CL UPF和辅锚点UPF**合一部署**
- **UL CL方案只支持融合计费**

---

### K236: 3GPP PS Data Off功能 `[原理]`
> 来源: K125

PS Data Off解决UE关闭移动数据开关后网络仍转发下行数据并产生计费的问题。生效需**同时满足三条件**：
1. UE携带3GPP PS Data Off UE Status为activated
2. SMF/PGW-C/GGSN-C配置PSDATAOFFSWITCH=ENABLE
3. 当前业务为**非豁免业务**

核心机制：网络侧通过下发Gate Status=closed的Create QER绑定到PDR上，阻止UPF向UE转发下行数据。

---

### K237: PS Data Off豁免业务与各制式差异 `[方案设计]`
> 来源: K126

**豁免业务**：IMS默认豁免（SET APNIMSATTR/SET GLOBALIMS配置），其他通过ADD EXEMPTSERVICE配置。

**各制式差异**：

| 维度 | 2/3G | 4G | 5G |
|------|------|----|-----|
| UE携带方式 | PCO | PCO | **ePCO** |
| 能力协商 | 需协商 | 需协商 | **不需协商（5G必须支持）** |
| Non-3GPP互操作 | 不涉及 | 切到Non-3GPP时清除status并删QER | 不涉及 |

---

### K238: PS Data Off ULCL场景处理 `[方案设计]`
> 来源: K127

- **I-UPF**：仅通知锚点UPF，不通知I-UPF
- **ULCL**：需同时通知主锚点+辅锚点UPF停止下行转发
- 新辅锚点插入时若data off已activated → 在PFCP Session Establishment Request中直接包含Gate Status=closed的Create QER

---

### K239: 计费暂停功能 `[原理]`
> 来源: K128

计费暂停用于移出网络覆盖区的用户，提高计费准确性。**仅4G支持，5G不支持**。

三个触发场景：
1. **S1 Release（ARRL）**：Release Access Bearers Request中ARRL=1，无线链路异常释放
2. **DDN寻呼失败**：DDN Acknowledge携带失败原因值（排除"Context not found"和"Unable to page UE due to Suspension"）
3. **下行丢包阈值**：SGW-U检测下行丢包达设定阈值后上报

---

### K240: 计费暂停能力协商与配置 `[方案设计]`
> 来源: K129

**协商流程**：SGW-C检查SET SGWCHGPAUSE → Create Session Request中PDN Pause Support Indication=1 → PGW-C检查ADD APNPGWCHGPAUSE(APN级优先)或SET GLBPGWCHGPAUSE(全局) → Response中PDN Pause Enable Indication=1

**PFCP机制**：触发计费暂停时PGW-C向PGW-U下发优先级最高的Create PDR（**不携带URR ID**，表示不计费），停止时下发Remove PDR。

**隐含规则**：计费暂停**只在空闲态生效**，Handover只在连接态，因此不可能同时存在。

---

### K241: 计费暂停互操作场景 `[方案设计]`
> 来源: K130

| 场景 | 处理 |
|------|------|
| PGW-C→GGSN-C | GGSN不支持，需停止计费暂停(Remove PDR) |
| GGSN-C→PGW-C | 重新协商；满足条件时下发丢包检测URR |
| PGW-C→SMF | 5G不支持，需停止计费暂停 |
| SMF→PGW-C | 重新协商；满足条件时下发丢包检测URR |

---

## 第十七章：故障案例与运维

### K242: 故障1 — N40未发送Initial消息 `[故障案例]`
> 来源: K115

- **现象**：SMF未通过N40接口发送Charging Data Request [Initial]消息
- **根因**：(1) 计费模式未配为N40 (2) 融合计费未使能 (3) CHFINIT未设为SENDREQ (4) 无可用CHF (5) N40链路故障
- **排查**：LST CHGMODE → LST CHARGECTRL → LST CCT → LST GLBDFTCHFGROUP → ALM-100072
- **隐含知识**：三层配置必须全部正确：CHGMODE=NchfMode + CHARGECTRL使能 + CHFINIT=SENDREQ

---

### K243: 故障2 — 预申请配额未携带预期RG `[故障案例]`
> 来源: K116

- **现象**：Initial消息中RG缺失或不符合预期
- **根因**：(1) CCRINITRGNUM设置不合理 (2) RGSOURCE设置不合理 (3) RG配置或绑定错误
- **排查**：LST CCT(CCRINITRGNUM/RGSOURCE) → LST URRGROUP → LST URR → LST CTXSTARTRATING
- **隐含知识**：RG来源两种模式：CTXSTARTRATING（显式配置RG）和DEFAULT（按优先级自动获取）。RG绑定链路：URR → URRGROUP → CTXSTARTRATING。

---

### K244: 故障3 — RG计费方式不符合预期 `[故障案例]`
> 来源: K117

- **现象**：N40接口RG的在线/离线计费方式与规划不一致
- **根因**：(1) 用户计费方式(RGAPPLIED)设置错误 (2) URR的USAGERPTMODE与用户计费方式不一致
- **排查**：LST CHARGECTRL → LST USRPROFCHARGE → LST URR(USAGERPTMODE)
- **隐含知识**：
  - RGAPPLIED三个取值：ONLINERGONLY、OFFLINERGONLY、DEFAULT（同一N40会话可同时支持在线和离线RG）
  - **URR的USAGERPTMODE必须与用户级别的RGAPPLIED一致，否则不生效**
  - 计费方式可基于User Profile或DNN或CC三种粒度配置

---

### K245: 故障4 — Trigger未上报 `[故障案例]`
> 来源: K118

- **现象**：SMF未向CHF发送Charging Data Request [update]上报Trigger
- **根因**：(1) CHF未下发对应Trigger (2) SMF本地未配置 (3) Session级与RG级冲突
- **排查**：用户跟踪查看CHF Response的triggers → LST PDUTRIGGER → LST RGTRIGGER
- **隐含知识**：
  - Trigger分两级：Session级(PDUTRIGGER)和RG级(RGTRIGGER)
  - **优先级规则**：Session级和RG级同一Trigger冲突时，Session级优先。Session级"不上报"时才按RG级生效
  - Trigger来源：CHF下发（Response的triggers信元）+ SMF本地配置

---

### K246: 故障5 — 主备CHF未生效 `[故障案例]`
> 来源: K119

- **现象**：主CHF故障时SMF未切换到备用CHF
- **根因**：(1) 未配置备用CHF (2) CHF下发FAILOVER_NOT_SUPPORTED (3) SMF本地FAILOVERSUP未使能 (4) 备用CHF链路故障
- **排查**：LST SELECTCHFGBYCC → LST TNFBINDGRP → LST TNFGRP → LST FAILHANDLING
- **隐含知识**：
  - **Failover三要素**：备用CHF已配置 + CHF未指示FAILOVER_NOT_SUPPORTED + SMF本地FAILOVERSUP=ENABLE
  - CHF侧sessionFailover信元具有决定权
  - CHF选择基于CC绑定：SELECTCHFGBYCC → TNFBINDGRP → TNFGRP → TNFINSIP

---

### K247: 故障6 — 业务被放通未上报CHF `[故障案例]`
> 来源: K120

- **现象**：用户数据业务被放通但计费信息被缓存或丢弃
- **根因**：(1) CHF无响应 (2) CHF链路故障 (3) CHF返回异常结果码
- **排查**：用户跟踪消息 → ALM-100072告警
- **隐含知识**："放通"是容错机制，保证业务连续性但牺牲计费准确性。计费消息可能被缓存（等CHF恢复后回放）或丢弃。

---

### K248: 故障7 — 缓存消息未正常回放 `[故障案例]`
> 来源: K121

- **现象**：CHF恢复后SMF缓存消息未回放
- **根因**：(1) 无缓存文件 (2) N40链路不正常 (3) 缓存文件超期 (4) 未达到回放间隔
- **排查**：DSP CDRSTRGINFO → ALM-100072 → ALM-81059(超期告警) → LST N40MSGSTG(回放间隔)
- **隐含知识**：**回放四条件**全部满足才回放：有缓存文件 + 链路正常 + 文件未超期(CDRSTORAGECTRL) + 达到回放间隔(N40MSGSTG)。

---

### K249: 故障8 — CP和UP URR配置不一致 `[故障案例]`
> 来源: K122

- **现象**：ALM-81026(接口信元不一致) + ALM-81054(CP/UP关键配置不一致)
- **根因**：SMF和UPF的URR配置不一致
- **隐含知识**：SMF产生ALM-81026，UPF产生ALM-81054，是配对告警。URR变更必须同步CP和UP。

---

### K250: 故障9 — 计费流量与实际访问流量不一致 `[故障案例]`
> 来源: K123

- **现象**：N40上报的计费流量与用户实际访问流量不一致
- **根因**：(1) 存在免费业务(METERINGTYPE=FREE) (2) PCF动态Rule未指定RG (3) 预定义Rule不绑定RG (4) 欠费场景信令流量丢弃
- **排查**：LST URR(METERINGTYPE) → LST USERPROFILE(FREESER) → LST RULE → LST PCCPOLICYGRP → LST SPECTRAFURRGRP
- **隐含知识**：
  - 免费业务和欠费丢弃是"正常现象"，Rule未绑定RG是"配置错误"
  - Rule→PCCPOLICYGRP→URRGROUP→URR绑定链路任何一环断裂都导致流量不一致
  - 欠费场景信令流量由SPECTRAFURRGRP控制

---

### K251: 故障10 — 用户异常去活诊断体系 `[故障案例]`
> 来源: K124

- **现象**：用户异常去活，Termination消息携带ABNORMAL_RELEASE
- **根因**：周边网元故障，通过diagnostics原因值定位
- **排查**：用户跟踪查看diagnostics字段 → LST N40DIAGTRIGGER

**关键运维知识 — 去活原因值映射表**：

| 原因值 | 指向网元 | 场景 |
|--------|---------|------|
| 12 | GTPC链路 | GTPC链路中断 |
| 21 | UPF | UPF收到Error indication |
| 22 | 对端网元 | 对端重启(recovery IE不匹配) |
| 258 | **CHF** | CHF返回信元不合法 |
| 262 | **CHF** | CHF响应超时 |
| 263 | **CHF** | 主备CHF重发均超时 |
| 302 | **PCF** | PCF无响应 |
| 351 | **UPF** | UPF请求去活 |
| 352 | **UPF** | UPF无响应 |

**原因值258子场景**：请求体类型与返回码不匹配、UPF独享配额模式下CHF未携带uPFID、CHF未携带ResultCode、SMF申请配额但CHF未授权也未指示重定向。

**关键参数**：SET CNVRGDCHGPARA的BADRSPACT=CONTINUE时允许CHF异常时业务继续而非去活。

---

### K252: 计费告警速查表 `[运维]`
> 来源: K289, K290, K291, K292, K293, K294

| 告警ID | 名称 | 级别 | 适用NF | 核心含义 | 关键处理 |
|--------|------|------|--------|----------|----------|
| 82000 | 计费中心长时间未取话单 | 紧急 | NCG | PULL模式下计费中心未取话单 | 配置分发/备份任务；磁盘剩余400MB停止接收 |
| 100417 | UPF中转RADIUS无响应 | 重要 | SMF/GW-C/GGSN | SMF通过UPF中转RADIUS链路断 | MOD RDSSVRGRP调重发参数 |
| 100530 | 融合计费用户放通不计费 | 次要 | SMF/GW-C/GGSN | CHF故障+缓存关闭导致放通 | 开启SET N40MSGSTG缓存；分析话统维度 |
| 100630 | 在线计费定时器过载流控 | 重要 | SMF/GW-C/GGSN | 在线计费定时器拥塞(VT/NPT/Tx) | 等10分钟自动恢复，否则联系支持 |
| 81020 | RADIUS计费服务器无响应 | 重要 | SMF/GW-C/GGSN | UNC直连RADIUS链路断 | SET APNRDSACCTCTRL可设CONTINUE |
| 100682 | 计费网元设备故障 | 重要 | SMSF | NCG设备故障 | 查NCG对应告警 |
| 100683 | 计费网元业务状态异常 | 重要 | SMSF | NCG业务异常 | 查NCG对应告警 |

**ALM-100530处理要点**：
- 核心关联命令：SET CNVRGDCHGPARA(CONTINUEALARM=ENABLE) + SET N40MSGSTG(STGSWITCH=ENABLE)
- 话统分析维度：无可用CHF / CHF无响应 / 结果码错误 / 信元错误 导致的放通次数
- 建议：现网应开启话单缓存功能以避免CHF故障时放通不计费

---

### K253: 信令跟踪 — 5G计费问题定位 `[运维]`
> 来源: K295

5G计费问题定位流程：
1. 建立用户跟踪，查看是否上报**EMS_CtfErrorRpt**消息
2. 打开EMS_CtfErrorRpt消息，解析关键字段：
   - **ChargingID**：计费编号
   - **AnonymizeSupi**：匿名化用户永久标识
   - **PduSessionId**：PDU会话编号
   - **RptErrorInfo**：错误原因描述
   - **Details**：定位详细信息
   - **Suggestion**：错误处理建议
3. 根据原因和建议处理，重新拨测验证

---

### K254: 信令跟踪 — 5G策略问题定位 `[运维]`
> 来源: K296

5G策略问题定位流程：
1. 建立用户跟踪，查看是否上报**EMS_SmpolicyErr**消息
2. 打开EMS_SmpolicyErr消息，解析关键字段：
   - **AnonymizedSupi**：匿名化用户永久标识
   - **PdusessionId**：PDU会话编号
   - **Rattype**：无线接入类型
   - **PcfInstanceId**：PCF实例标识
   - **EmsErrInfo**：错误原因描述
   - **Suggestion**：错误处理建议
3. 根据原因和建议处理，重新拨测验证

---

### K255: N40接口链路状态检查 `[运维]`
> 来源: K131

SMF和CHF之间N40接口链路状态检查步骤：
1. 执行`DSP SBILINKSTATUS`命令，选择对端NF类型为NFTypeCHF，检查链路状态是否为"正常"
2. 查看是否存在ALM-100072（目的NF服务不可达，对端网元类型为CHF）告警
3. 不符合预期时收集告警、日志、配置信息联系技术支持

---

## 知识统计

| 章 | 标题 | 编号范围 | 数量 |
|----|------|----------|------|
| 第十二章 | 融合计费配置全景 | K201-K213 | 13 |
| 第十三章 | 计费三件套配置 | K214-K223 | 10 |
| 第十四章 | PCF策略配置 | K224-K228 | 5 |
| 第十五章 | 方案设计知识 | K229-K234 | 6 |
| 第十六章 | 特殊场景 | K235-K241 | 7 |
| 第十七章 | 故障案例与运维 | K242-K255 | 14 |
| **合计** | | K201-K255 | **55** |

### 融合去重记录

| 新编号 | 合并来源 | 融合说明 |
|--------|----------|----------|
| K205 | K135 + K272 + K273 + K274 + K275 + K276 + K277 | 计费接口模式：K135基础定义 + K272优先级 + K273终端类型 + K274互操作指示 + K275 V/I-SMF + K276 PCF实例 + K277策略模式 |
| K206 | K136 + K259 + K260 + K261 | CC属性：K136标准取值 + K259四级优先级 + K260本地/签约选择 + K261制式来源 |
| K213 | K145 + K155 + K156 | CHF选择：K145选择优先级 + K155 IMSI三层配置 + K156实时生效限制 |
| K235 | K167 + K168 + K262 | ULCL计费：K167独立配额 + K168系统约束 + K262架构原理 |
| K252 | K289 + K290 + K291 + K292 + K293 + K294 | 7个告警条目合入速查表，K291(ALM-100530)补充处理要点 |

### 按类型统计

| 类型 | 数量 | 编号 |
|------|------|------|
| [配置] | 22 | K203, K204, K205, K207, K208, K209, K210, K211, K212, K213, K214, K215, K216, K219, K222, K223, K227, K228 |
| [原理] | 8 | K220, K224, K226, K229, K236, K239 |
| [方案设计] | 12 | K202, K218, K221, K230, K231, K232, K233, K234, K235, K237, K238, K240, K241 |
| [隐性规则] | 4 | K201, K217, K225 |
| [故障案例] | 10 | K242-K251 |
| [运维] | 3 | K252, K253, K254, K255 |
