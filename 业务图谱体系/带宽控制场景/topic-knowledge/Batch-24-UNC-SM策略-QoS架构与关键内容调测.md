# Batch-24: UNC SM策略 - QoS架构与关键内容调测

## 1. 概述

本批次知识文档覆盖"5G PCC之SM策略解决方案"业务专题中SM策略的关键内容与调测方法，来源为UNC（控制面/SMF侧）产品文档。具体涵盖以下主题：

- **QoS基础理论**：QoS的含义、背景、度量标准（带宽/时延/抖动/丢包率）
- **5G QoS架构模型**：QoS Flow、PDU Session、DRB三层架构，默认QoS Flow与专有QoS Flow的区分
- **QoS如何控制**：PCF/SMF/UPF/RAN/UE在QoS控制中的角色分工，信令控制与Reflective QoS两种机制
- **SM策略关键参数**：计费参数（chgId/meteringMethod/offline/online/ratingGroup等）、短信/邮件通知、重定向
- **动态PCC策略调测**：信令调测法（网元间信令跟踪分析）与快速调测法（MML命令验证）两种方法的完整步骤

这些内容构成了带宽控制场景的理论基础和验证手段：QoS架构定义了带宽控制的执行框架，计费参数关联计费子场景，重定向关联访问限制子场景，调测方法则是验证带宽控制配置是否正确落地的工具链。

---

## 2. 核心知识点

### 2.1 QoS基础概念体系

#### 2.1.1 QoS的含义

QoS（Quality of Service，服务质量）有两层含义：
1. **服务质量指标**：表征QoS的具体参数（带宽、时延、抖动、丢包率等）
2. **服务质量保证机制**：如何保证这些指标得以实现的机制

类比交通运输系统：用户面（网络通道）是道路，业务数据是道路上运输的乘客或物资。不同运输需求对应不同道路类型（普通公路、公交专用道、BRT专用道等），根据业务需求分配道路的过程即数据通信中的信令过程。QoS的作用是保障货物运输质量——在必要的时间内将必要的信息运送到目的地。

#### 2.1.2 QoS的产生背景

随着网络普及和业务多样化，互联网流量激增导致：
- 网络拥塞
- 转发时延增加
- 严重时产生丢包
- 业务质量下降甚至不可用

解决网络拥塞最直接的办法是增加带宽，但从运营维护成本考虑不现实。QoS技术的核心思路是在有限带宽资源下，平衡地为各种业务分配带宽，针对不同业务需求提供端到端的服务质量保证。QoS本身不增加网络带宽，类似城市交通管理中设置"公交专用道"——通过有保证的策略进行拥塞管理。

#### 2.1.3 QoS度量标准（四大指标）

| 度量项 | 含义 | 关键说明 |
|--------|------|----------|
| **带宽** | 单位时间（1秒）内从网络一端传输到另一端的最大数据位数，单位bit/s。相关概念：吞吐量（实际成功传送的数据流大小） | 带宽越大通信能力越强。包含上行速率和下行速率。类比高速公路车道越多通行能力越强 |
| **时延** | 报文/分组从发送端到接收端的延迟时间，由传输延迟和处理延迟组成 | 时延<=100ms用户基本无感；100ms~300ms通话有轻微停顿感；>300ms明显影响通话体验 |
| **抖动** | 同一连接传输的分组延迟各不相同的程度，即最大延迟与最小延迟的时间差 | 对实时业务（语音/视频）极不容忍。可用缓存克服过量抖动，但会增加时延 |
| **丢包率** | 网络传输中丢失报文数量占传输报文总数的百分比 | 少量丢包影响不大（TCP可重发），大量丢包影响传输效率。QoS关注丢包的统计数据 |

### 2.2 5G QoS架构模型

5G QoS架构以**QoS Flow**为基础。一个PDU Session可包含1个或多个QoS Flow，至少要有一个默认QoS Flow承载。

#### 2.2.1 QoS Flow分类

| Flow类型 | 5QI范围 | 速率保证 | 类比 | 创建时机 |
|----------|---------|----------|------|----------|
| **默认QoS Flow** | GBR或Non-GBR均可 | 取决于5QI | 汽车出行（公路不保证速度），兜底方案 | 必须创建 |
| **专有QoS Flow（GBR）** | 1~4, 65~67, 75 | 保证bit率，无线侧资源支持时一定保障 | 飞机出行（保证速度） | 按需创建 |
| **专有QoS Flow（Non-GBR）** | 5~9, 69~70, 79~80 | 不保证bit率 | 轮船出行（不保证速度） | 按需创建 |

关键规则：
- UE接入5G网络时首先创建默认QoS Flow
- 当默认QoS Flow不能满足业务QoS要求时，根据业务需求创建专有QoS Flow
- 专有QoS Flow主要用于对网络质量有较高要求的应用场景
- GBR QoS Flow的速率在无线侧资源支持时一定受保障，PCF下发参数必然携带保证带宽参数

#### 2.2.2 QoS配置文件关键参数

| 参数 | 全称 | 说明 |
|------|------|------|
| **5QI** | 5G QoS Identifier | QoS通路的综合评估结果，5G网络QoS控制的主线，在5G网元间传递 |
| **ARP** | Allocation and Retention Priority | 标识业务获取通路（主要是空口）的能力，控制QoS Flow建立、修改的优先级 |
| **GFBR** | Guaranteed Flow Bit Rate | 保证流速率（类比高铁承诺速度120km/h） |
| **MFBR** | Maximum Flow Bit Rate | 最大流速率（类比高铁最高速度300km/h） |
| **Session-AMBR** | Session Aggregate Maximum Bit Rate | 同一PDU Session所有Non-GBR QoS Flow总速率上限，由UE和UPF控制 |
| **UE-AMBR** | UE Aggregate Maximum Bit Rate | 同一UE所有PDU Session的Non-GBR QoS Flow总速率上限，由gNB控制 |

带宽层级关系：**UE-AMBR >= Session-AMBR >= QoS Flow级带宽**

- Session-AMBR由UE和UPF统一控制（一个PDU会话汇聚在一个UE和同一个UPF上处理）
- UE-AMBR由gNB控制（gNB识别UE信息，一个UE的全部承载在同一gNB上）

### 2.3 QoS如何控制

#### 2.3.1 QoS控制角色分工

| 网元 | 角色 | 职责 |
|------|------|------|
| **PCF** | "老板" | 拥有QoS参数的最高决策权 |
| **SMF** | "经理" | 根据PCF指示进行QoS Flow控制，保存最终决策的QoS参数 |
| **UPF/RAN/UE** | "员工" | 按照SMF指示执行用户面动作 |

#### 2.3.2 QoS参数决策机制

| QoS Flow类型 | QoS参数 | 决策方式 |
|--------------|---------|----------|
| 默认QoS Flow | 5QI/ARP/Session-AMBR | SMF从UDM获取QoS后结合本地配置协商，上报PCF。PCF下发新QoS则以PCF为准 |
| 默认QoS Flow | UE-AMBR | AMF从UDM获取，发送给RAN |
| 网络侧发起的专有QoS Flow | 5QI/ARP/GFBR/MFBR/Notification control/Max Packet Loss Rate | PCF直接下发 |
| UE发起的专有QoS Flow | 同上 | UE可在请求消息中携带期望参数，最终以PCF下发为准 |

#### 2.3.3 QoS Flow控制两种机制

| 机制 | 适用对象 | 原理 |
|------|----------|------|
| **信令控制** | 所有QoS Flow | SMF在PDU会话建立/修改/用户面激活时向UPF/RAN/UE发送消息，携带QoS Flow信息。RAN和UE据此处理 |
| **Reflective QoS** | 仅Non-GBR QoS Flow | UE根据收到的下行数据包包头信息自行推演上行QoS rule。SMF发送RQI给UPF，UPF在隧道包头打RQI标记，AN将RQI和QFI通过空口传给UE。UE启动RQ定时器，超时后删除推导出的QoS rule |

Reflective QoS的设计目的是减少部署新应用时PDU会话修改的信令消息数量。

### 2.4 SM策略中的计费参数

PCF下发的参数中除QoS参数外，还包含一组计费控制参数。这些参数通过ChargingData类型的5G动作组配置，下发给SMF执行。

| 参数 | 含义 | 取值/说明 |
|------|------|-----------|
| **chgId** | 统一标识PDU会话内的计费控制策略数据 | string类型，必选，出现1次 |
| **meteringMethod** | 离线计费计量方式 | DURATION（计时长）/ VOLUME（计流量）/ DURATION_VOLUME（时长+流量）/ EVENT（计事件） |
| **offline** | 是否开启离线计费 | true/false，优先使用PCF配置值 |
| **online** | 是否开启在线计费 | true/false，优先使用PCF配置值 |
| **ratingGroup** | PCC规则的费率组标识 | Uint32，相同费率类型的业务属于同一费率组 |
| **reportingLevel** | SMF上报使用情况的级别 | SER_ID_LEVEL / RAT_GR_LEVEL / SPON_CON_LEVEL |
| **serviceId** | 服务标识，业务数据流所属的服务或服务组件标识 | Uint32，需与ratingGroup保持一致 |
| **sponsorId** | 赞助商标识 | 支持N5相关的Sponsored业务场景 |
| **appSvcProvId** | 应用服务提供商标识 | 支持N5相关的Sponsored业务场景 |
| **afChargingIdentifier** | AF提供的计费标识 | 将PCC规则计费键值与应用级别报告关联 |
| **sdfHandl** | 等待信用请求响应时是否允许业务数据流通过 | true/false，默认false（阻止），仅支持配置下发不支持业务处理 |

计费关键约束：
- offline和online**不能同时为true**，但可同时为false（不计费场景）
- ratingGroup与serviceId取值需保持一致
- ratingGroup和reportingLevel组合可唯一标识所请求的费率组
- 离线/在线计费方式选择优先使用PCF配置值，未配置则使用SMF本地配置

### 2.5 SM策略中的短信/邮件通知

UPCF通过SMSC（短信中心）、Email服务器和SOAP服务器向终端用户发送通知，提醒用户当前的业务状态。

特性：
- 支持短信通知与邮件通知**独立发送**，发送速度互不影响
- 支持配置消息通知的**发送时间段**，避免在用户休息时间打扰
- 支持控制消息通知的**发送速度**，避免对端无法处理
- 支持按照用户的**IMSI号段**配置不同的通知内容

典型应用场景：FUP（Fair Usage Policy）触发时，通过短信/邮件通知用户当前流量使用状态（如配额耗尽、降速提醒等）。

### 2.6 SM策略中的重定向

重定向是SM策略中的关键参数类型，4G/5G网络均支持。当用户触发重定向规则时，将其当前访问状态重定向到指定服务页URL地址。

触发重定向的典型场景：
1. **基于配额/资费消耗**：流量配额或资费耗尽时，将用户访问重定向到运营商充值首页
2. **基于位置区域**：用户进入特定区域（出国、热点接入区域）时，重定向到套餐订购页面或免费接入验证页面

### 2.7 动态PCC策略调测：信令调测法 vs 快速调测法

#### 2.7.1 两种方法对比

| 维度 | 信令调测法 | 快速调测法 |
|------|-----------|-----------|
| **方法本质** | 基于网元间信令交互的详细分析 | 基于MML命令查询的直接验证 |
| **分析深度** | 最深——消息流程+消息内容+码流级分析 | 中等——查询网元本地状态和参数 |
| **工具依赖** | OM Portal消息跟踪 | MML命令（DSP系列）+ 测速软件 |
| **网元覆盖** | PCF + SMF + UPF 三网元全链路跟踪 | UPCF Web LMT + UNC OM + UDG OM 逐网元查询 |
| **适用场景** | 深度排查协议合规性、策略逻辑问题、网元间交互异常 | 快速验证配置是否生效、QoS参数是否一致、业务体验是否符合预期 |
| **操作复杂度** | 高（需建立跟踪任务、解读码流） | 低（执行MML命令、对比输出结果） |
| **验证完备性** | 全面——策略内容、消息流程、消息内容三维验证 | 直观——规则安装、QoS参数、用户上下文、终端体验四层验证 |

#### 2.7.2 信令调测法的核心验证维度

1. **策略内容验证完备性**：PCF签约业务中定义的动作组下发时须满足的"条件"场景需全量覆盖测试
2. **消息流程是否正确**：网元处理策略下发、策略执行、策略更新、事件上报等消息流程符合3GPP协议
3. **消息内容是否正确**：策略下发消息携带内容是否与策略逻辑定义保持一致

#### 2.7.3 快速调测法的验证层级

1. **用户签约验证**：LST PSRV（UPCF Web LMT）确认签约业务正确
2. **SMF规则安装验证**：DSP PCCSESSINFO 确认PCF下发的动态规则已在SMF成功安装
3. **SMF QoS参数验证**：DSP SESSIONQOSINFO 确认协商QoS与PCF配置下发一致
4. **UPF用户上下文验证**：DSP SESSIONINFO 确认UPF侧会话信息和规则匹配
5. **终端业务体验验证**：使用Speedtest/AndFTP等测速软件验证实际带宽体验

---

## 3. 配置调测要点

### 3.1 QoS参数配置逻辑链

```
业务需求 → PCF策略配置（PCC规则+QoS决策+计费决策）
  → PCF下发（Npcf_SMPolicyControl_Create/Update Response）
    → SMF接收并安装规则
      → SMF通过N4接口下发UPF（PFCP Session Establishment/Modification Request）
        → UPF/RAN/UE执行QoS控制
```

### 3.2 信令调测法完整步骤

**前提条件**：已完成动态规则配置；终端用户已在UDM完成开户签约；已通过UPCF PGW Web LMT签约UPCF配置的业务。

**步骤1：建立三网元消息跟踪**
- PCF侧：登录UPCF CSP OM Portal > 监控分析 > 消息跟踪 > 任务管理 > 创建用户消息跟踪（选中N7接口）
- SMF侧：登录UNC CSP OM Portal > 监控分析 > 消息跟踪 > UNC > 用户跟踪 > 添加跟踪任务
- UPF侧：登录UDG CSP OM Portal > 监控分析 > 消息跟踪 > 用户跟踪 > 创建跟踪任务

**步骤2：用户上线并观察PCF侧信令**

三个关键信令流程：
1. **初始下发策略**：用户上线后，SMF向PCF发送 `Npcf_SMPolicyControl_Create Request`，PCF返回 `Response` 携带完整策略（pccRules/qosDecs/sessRules/umDecs/traffContDecs等）
2. **PCF发起的策略更新**：PCF修改签约信息后，主动发送 `Npcf_SMPolicyControl_UpdateNotify Request`，包含新规则（值为对象）和待删除规则（值为null）
3. **SMF发起的会话更新**：触发事件（如配额分片耗尽）时，SMF发送 `Npcf_SMPolicyControl_Update Request` 上报事件（如accuUsageReports中的volUsage），PCF在Response中决策是否更新策略

**步骤3：观察SMF/UPF侧信令**

三个关键信令流程：
1. **初始下发消息**：SMF收到PCF策略后，通过 `PFCP Session Establishment Request` 下发UPF，携带PDR/FAR/QER等规则
2. **PCF发起的会话更新**：PCF修改后，SMF通过 `PFCP Session Modification Request` 向UPF更新策略内容
3. **UPF发起的会话更新**：事件触发时，UPF通过 `PFCP Session Report Request` 向SMF上报，SMF再向PCF上报请求决策

### 3.3 快速调测法完整步骤

**步骤1：检查用户签约**
```
LST PSRV（UPCF Web LMT）  → 确认签约业务名称与目标一致
```

**步骤2：用户上线，检查SMF规则安装**
```
DSP PCCSESSINFO:USERIDTYPE=IMSI,IMSI="46000000000****";
```
验证要点：
- RuleName与PCF配置的pccRuleId一致
- RuleSource显示"PCF created"
- QFI对应的5QI和ARP与PCF配置吻合

**步骤3：检查SMF QoS参数一致性**
```
DSP SESSIONQOSINFO:QUERYTYPE=IMSI,IMSI="46000000000****",WLNETWKTYPE=NW5G,PDUSESSIONID=5;
```
验证要点：
- "协商的QCI/5QI"与PCF配置下发值一致
- "协商的QoS ARP"与PCF配置吻合
- 协商类上下行比特率取值为UDM签约值与PCF下发值中的**较小值**
- 排除UDM签约默认值干扰：可将UDM签约默认值改大，再判断协商QoS是否为PCF下发值

**步骤4：检查UPF用户QoS上下文**
```
DSP SESSIONINFO:QUERYTYPE=IMSI,IMSI="46000000000****";
```
验证要点：
- PDR/FAR/QER规则已正确安装
- URR（使用量上报规则）的Measurement Method和Reporting Triggers正确
- 上下行Gate状态（UpLink Gate/DownLink Gate = Open）
- 注意：UPF查询到的规则仅含预定义规则/预定义规则组/本地规则，**不含动态规则**

**步骤5：终端业务体验验证**
- 安装测速软件（Speedtest、AndFTP）
- 确保仅使用移动蜂窝网络
- 不同时段验证限速策略（如19:00-21:00限速1Mbit/s，其他时段10Mbit/s）

### 3.4 策略更新码流关键字段解读

PCF初始下发策略消息中的关键信元：
- `pccRules`：动态PCC规则（含规则名、流信息、QoS引用、计费引用、优先级）
- `qosDecs`：QoS决策数据（含5QI、maxbrUl/maxbrDl、ARP等）
- `sessRules`：会话级规则（含authSessAmbr会话级AMBR、authDefQos默认QoS）
- `umDecs`：使用量监控数据（含volumeThreshold配额分片阈值）
- `traffContDecs`：业务流状态控制（flowStatus: ENABLED/DISABLED）
- `policyCtrlReqTriggers`：策略控制请求触发器（如US_RE使用量上报）

---

## 4. 与带宽控制的关系

本批次知识文档与带宽控制场景的关联关系：

### 4.1 QoS架构是带宽控制的执行框架

带宽控制的核心操作——限速（Rate Limiting）、保证带宽（GBR）、最大带宽限制（MFBR/AMBR）——全部依托5G QoS架构实现：
- **5QI**定义了不同业务的带宽保障等级
- **GBR/MFBR**直接控制QoS Flow的保证速率和最大速率
- **Session-AMBR/UE-AMBR**实现会话级和用户级的聚合带宽控制
- **QoS Flow建立/修改/删除**是带宽控制策略执行的载体

### 4.2 计费参数关联计费子场景

SM策略中的计费参数（ratingGroup/serviceId/meteringMethod等）与计费场景知识库直接对应：
- 在线/离线计费方式选择
- 费率组与业务标识的组合标识计费维度
- meteringMethod的DURATION/VOLUME/DURATION_VOLUME对应计费计量方式
- sdfHandl控制等待信用授权时是否放通流量

### 4.3 重定向关联访问限制子场景

重定向是访问限制场景的重要手段：
- 配额/资费耗尽时重定向到充值页面
- 特定位置区域重定向到套餐订购/认证页面
- 与URL过滤、阻塞等构成完整的访问限制工具集

### 4.4 调测方法是验证带宽控制配置的工具

- **信令调测法**用于深度排查带宽控制策略下发与执行的协议合规性
- **快速调测法**用于快速验证限速配置是否生效、QoS参数是否一致
- DSP系列MML命令是日常运维中验证带宽控制效果的核心工具

### 4.5 短信/邮件通知是FUP用户感知的配套手段

FUP（Fair Usage Policy）触发降速/限速时，通过短信/邮件通知用户当前状态，是带宽控制场景中用户体验管理的重要配套。

---

## 5. 关键术语

| 术语 | 全称/释义 |
|------|-----------|
| **QoS** | Quality of Service，服务质量 |
| **QoS Flow** | 5G中最小的QoS区分粒度，一个PDU Session可含多个QoS Flow |
| **5QI** | 5G QoS Identifier，5G QoS标识符，标量值，映射到一组QoS特性 |
| **GBR** | Guaranteed Bit Rate，保证比特率 |
| **Non-GBR** | Non-Guaranteed Bit Rate，非保证比特率 |
| **GFBR** | Guaranteed Flow Bit Rate，保证流速率 |
| **MFBR** | Maximum Flow Bit Rate，最大流速率 |
| **Session-AMBR** | Session Aggregate Maximum Bit Rate，会话级聚合最大比特率 |
| **UE-AMBR** | UE Aggregate Maximum Bit Rate，用户级聚合最大比特率 |
| **ARP** | Allocation and Retention Priority，分配和保持优先级 |
| **PDU Session** | 协议数据单元会话，UE与DN之间的连接 |
| **PCF** | Policy Control Function，策略控制功能 |
| **SMF** | Session Management Function，会话管理功能 |
| **UPF** | User Plane Function，用户面功能 |
| **RAN** | Radio Access Network，无线接入网 |
| **gNB** | 5G基站 |
| **Reflective QoS** | 反射QoS，UE根据下行数据包自行推演上行QoS rule的机制 |
| **RQI** | Reflective QoS Indication，反射QoS指示 |
| **RQA** | Reflective QoS Attribute，反射QoS属性 |
| **PCC** | Policy and Charging Control，策略与计费控制 |
| **PDR** | Packet Detection Rule，包检测规则 |
| **FAR** | Forwarding Action Rule，转发动作规则 |
| **QER** | QoS Enforcement Rule，QoS执行规则 |
| **URR** | Usage Reporting Rule，使用量上报规则 |
| **PFCP** | Packet Forwarding Control Protocol，包转发控制协议（N4接口） |
| **FUP** | Fair Usage Policy，公平使用策略 |
| **SMSC** | Short Message Service Center，短信服务中心 |
| **DNN** | Data Network Name，数据网络名称（类似4G的APN） |
| **ratingGroup** | 费率组标识，相同费率类型的业务属于同一费率组 |
| **meteringMethod** | 计量方式，定义离线计费计量哪些参数 |

---

## 6. 知识来源

| 序号 | 文件名 | 主题 |
|------|--------|------|
| 1 | 5G QoS架构模型_11970128.md | 5G QoS架构模型（QoS Flow分类、配置文件参数、AMBR层级） |
| 2 | QoS如何控制_99586315.md | QoS控制机制（PCF/SMF角色分工、参数决策、信令控制与Reflective QoS） |
| 3 | 含义_12276278.md | QoS的含义（服务质量指标+保证机制） |
| 4 | 度量标准_12276279.md | QoS度量标准（带宽/时延/抖动/丢包率四大指标） |
| 5 | 背景_12276277.md | QoS产生背景（网络拥塞问题与QoS解决方案） |
| 6 | 短信_邮件通知_86483632.md | SM策略短信/邮件通知（UPCF通知特性与配置） |
| 7 | 计费参数_86483630.md | SM策略计费参数（chgId/meteringMethod/offline/online/ratingGroup等11个参数详解） |
| 8 | 重定向_86483631.md | SM策略重定向（触发场景与实现方式） |
| 9 | 信令调测法_20602326.md | 动态PCC策略信令调测法（三网元消息跟踪+信令流程分析） |
| 10 | 快速调测法_20442424.md | 动态PCC策略快速调测法（MML命令验证+终端测速验证） |

---

> **文档信息**
> - 场景：带宽控制场景
> - 来源：UNC 20.15.2 产品文档 - 业务专题 - 5G PCC之SM策略解决方案
> - 批次：Batch-24
> - 网元：UNC（SMF/PCF侧）
> - 文档类型：业务专题知识融合
> - 创建时间：2026-06-09
