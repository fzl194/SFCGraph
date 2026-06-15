# 融合知识 Part A：计费架构、核心概念、接口协议（Gy/Ga/DCC）

> 融合来源：draft-batch-01, draft-batch-03-01, draft-batch-03-02, draft-batch-03-03, draft-batch-05-01, draft-batch-07
> 融合规则：同一知识点多批次覆盖时合并为一条，保留最完整描述；来源标注保留全部出处；新编号 K001-K100

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
