# Batch-23: UNC侧 FUP会话级配置调测 + SM策略E2E实现原理

> **来源**: UNC 产品文档 - 业务专题/5G Core FUP解决方案（会话级） + 业务专题/5G PCC之SM策略解决方案
> **覆盖**: FUP会话级配置/调测/变更/特性映射 + SM策略E2E实现原理（概述/生成/下发执行） + SM策略关键QoS内容
> **文件数**: 15 md
> **侧重点**: UNC（SMF/PGW-C）侧FUP会话级配置与SM策略E2E机制，这是带宽控制策略下发执行的完整链路

---

## 1. 概述

本批次文档来自UNC产品文档的两个核心业务专题，共15个md文件，涵盖四大主题板块：

### 1.1 FUP会话级累计流量策略控制（5个文档）

| 文档 | 核心内容 |
|------|----------|
| 系统影响与约束_70687833.md | 系统性能影响和约束条件（UMCH仅支持总流量阈值等） |
| 调测会话级累计流量策略控制_24087906.md | FUP功能验证的完整调测流程（12步） |
| 配置会话级累计流量策略控制_23928082.md | 会话级FUP的License开关、可选参数配置 |
| 20.7.0 01_24087900.md | 版本变更记录（2021-08-30首次发布） |
| 特性映射_23928078.md | 会话级/业务级FUP特性ID与License映射 |

### 1.2 SM策略E2E实现原理（7个文档）

| 文档 | 核心内容 |
|------|----------|
| 原理概述_15464534.md | SM策略E2E实现总览：策略生成、下发、执行三阶段 |
| QoS Flow建立_修改_删除_86483638.md | QoS Flow生命周期管理（新建/修改/删除判断逻辑） |
| QoS参数映射机制_86483640.md | 无线QoS与承载网QoS映射（5QI→DSCP→PHB） |
| 业务识别与分流_86483639.md | PF/PFS业务识别 + 4G/5G业务分流差异 |
| 动态规则_86483635.md | 动态规则定义、触发器/条件组/动作组策略模型 |
| 规则相关概念_17152898.md | PCC策略来源、规则分类（动态/预定义/本地）对比 |
| 预定义规则_预定义规则组_本地规则_86483636.md | 静态规则配置逻辑、示例分析与规则安装应用流程 |

### 1.3 SM策略关键QoS内容（3个文档）

| 文档 | 核心内容 |
|------|----------|
| 5G业务对QoS的诉求_87689107.md | eMBB/uRLLC/mMTC三大场景的带宽/时延/质量诉求 |
| 4G_5G QoS架构差异总结_11970130.md | 控制粒度/映射机制/QoS参数/特征的全面差异对比 |
| 5G QoS关键参数及概念_11969173.md | 5QI/ARP/GBR/QoS Flow/反射QoS/AMBR等14项参数详解 |

---

## 2. 核心知识点

### 2.1 FUP会话级配置与调测

#### 2.1.1 FUP会话级配置目标

会话级累计流量策略控制（Session-level Usage Monitoring）保证用户公平使用流量。当用户累计使用流量达到PCRF/PCF设定的阈值后，系统按策略执行带宽降速或下发新计费规则，实现流量公平管控。

#### 2.1.2 系统影响与约束

**系统性能影响**：启用会话级FUP需要PGW-U/UPF、GGSN-C/PGW-C/SMF与PCRF/PCF持续交互并动态处理下发的策略，对系统性能影响较大，规划时需考虑启用该特性的用户比例。

**约束条件**：
- UMCH（Usage Monitoring Congestion Handling）仅支持总流量阈值，不支持分业务阈值
- 对于UE Category用户，要求PCRF/PCF下发的会话级流量阈值不低于1GB，否则影响流量累计准确性

#### 2.1.3 FUP特性映射

FUP解决方案包含会话级和业务级两个层次，每个层次在UNC和UDG上各有独立的特性ID和License项：

| 功能 | 特性ID | License项 | 产品 |
|------|--------|-----------|------|
| 会话级累计流量策略控制 | WSFD-109104 | 82207980 LKV3W9PCBT12 | UNC |
| 会话级累计流量策略控制 | GWFD-020353 | 82200AFM LKV3G5PCBT01 | UDG |
| 业务级累计流量策略控制 | WSFD-211009 | 82200BNU LKV2FUPSAT01 | UNC |
| 业务级累计流量策略控制 | GWFD-110312 | 82209776 LKV3G5FPBS01 | UDG |

会话级首次正式发布于20.7.0 01版本（2021-08-30）。

#### 2.1.4 FUP会话级配置与调测详见

配置和调测流程的完整内容已在Batch-02中详细记录（License开关、Monitoring-Key解析方式、UMCH功能、FUP排除配置、重定向流量排除、12步调测流程）。此处不重复，重点说明本批次的关键补充：

**FUP排除场景**（MOD PCCPOLICYGRP的FUPSESSIONEXC参数）：当某类业务/应用的流量需要从用户级累计流量中排除时，将PCC策略组的`FUPSESSIONEXC`设置为`ENABLE`。典型用于免流业务的流量排除。

---

### 2.2 SM策略E2E实现原理概述

#### 2.2.1 SM策略E2E三阶段

SM策略（Session Management Policy）的E2E实现分为三个关键阶段：

| 阶段 | 执行网元 | 类比 | 核心动作 |
|------|----------|------|----------|
| **策略生成** | PCF（决策）、UDM（签约）、SMF（传递） | 制定运输方案 | PCF根据用户位置/等级/业务/时间等做出决策，生成QoS策略下发给SMF。无PCC功能时SMF可本地配置策略 |
| **策略下发** | SMF → UPF/RAN/UE（AMF透传） | 按方案修建道路 | SMF将QoS策略分别下发给UPF、RAN和UE |
| **策略执行** | UPF/RAN/UE | 车辆上路运输 | 将业务流基于QoS策略映射到QoS Flow/DRB，提供对应服务质量 |

**关键原则**：PCF拥有QoS参数的最高决策权，策略生成完全由PCF决策，不存在与UDM、SMF的协商过程。PCF可灵活根据用户位置、等级、时间段、配额状态、节假日等定制精细化策略。

#### 2.2.2 各网元在SM策略中的角色

| 网元 | 功能 |
|------|------|
| **PCF** | QoS参数最高决策权。根据用户上线信息（切片、位置等）生成QoS策略并下发SMF |
| **SMF** | 处理PCF下发的SM策略，确定QoS Flow信息（QFI/PFS/QoS参数），控制QoS Flow的建立/修改/删除 |
| **UDM** | 用户数据签约，分配默认QoS Flow的ARP/5QI，提供Session-AMBR和UE-AMBR |
| **AMF** | 对信令建立提供通道，信息透传 |
| **UPF** | QoS策略执行网元，处理PFS和QoS信息，执行下行QFI标记和控制，验证上行QFI |
| **RAN** | 处理信令面QoS策略，做用户面的QoS映射，实现业务服务质量控制 |

---

### 2.3 QoS Flow的建立/修改/删除

#### 2.3.1 QoS Flow的建立基础

QoS Flow通路的建立主要基于两个参数：

| 参数类型 | 参数名 | 作用 |
|----------|--------|------|
| **通路标识** | QFI（QoS Flow ID） | PDU Session中QoS差异化的最细粒度。一个PDU会话中QFI必须唯一。QFI可动态分配，也可等于5QI |
| **通路分类** | 默认QoS Flow | 5QI取值5~9、69、70、79、80，为用户业务建立固定QoS保证的数据通路 |
| | 专有QoS Flow | 5QI取值1~4、65~67、75，为特定业务（视频/语音等）建立特定QoS保证的数据通路 |

QoS Flow通路存在于RAN与UPF之间，SMF根据PCF下发的5QI建立对应QoS Flow并对每条添加QFI标识。

#### 2.3.2 QoS Flow的新建/修改/删除判断逻辑

**新建QoS Flow**：SMF比对PCF新下发的QoS profile中的5QI和ARP与已建好的流，只要5QI或ARP有一个不相等，则创建新的QoS Flow。

**删除已有QoS Flow**：以"规则"为粒度判断。PCF通过规则触发条件决策是否删除旧QoS Flow、新建新QoS Flow。关键依据是规则中定义的触发器和条件。

**修改流描述**：当5QI和ARP与已建好的流保持一致，但修改了部分流描述（如五元组等），SMF指示UE/UPF修改数据包到QoS Flow的映射规则。例如：原本走在QoS Flow2上的下载业务，调整到QoS Flow64。

---

### 2.4 QoS参数映射机制

#### 2.4.1 为什么需要QoS参数映射

核心网内部网元存储着5QI、ARP、MBR/GBR等QoS信息，但消息离开网元进入IP承载网络时，路由器/交换机看不到这些参数。为保证E2E QoS，需要在UPF转发报文时进行参数映射：

- **N6口（向DN侧）**：UPF修改数据包QoS标记，将核心网QoS转换为承载网QoS
- **N3口（向RAN侧）**：UPF在GTP包外层IP头中填入DSCP值，将承载网QoS转换为核心网QoS

#### 2.4.2 映射过程

**上行**：5QI参数 →（本地规则映射）→ DSCP/ToS值 → Service-Class+Color → DSCP/EXP/802.1p

**下行**：DSCP/EXP/802.1p → Service-Class+Color → DSCP → 填入外层IP报头（GTP-U封装）

#### 2.4.3 关键映射表

**5QI → DSCP默认映射**（部分）：

| 5QI | DSCP | 资源类型 | 典型业务 |
|-----|------|----------|----------|
| 1 | 46 (EF) | GBR | 会话语音 |
| 2/3/4 | 34 (AF4) | GBR | 会话视频/实时视频 |
| 5 | 46 (EF) | Non-GBR | IMS信令 |
| 6/7/8 | 18 (AF2) | Non-GBR | TCP类业务（视频缓冲/网页/FTP） |
| 9 | 0 (BE) | Non-GBR | 缺省QoS Flow |
| 69 | 46 (EF) | Non-GBR | 5G信号 |
| 70 | 18 (AF2) | Non-GBR | mission critical data |

**三种标准PHB（每跳转发行为）**：
- **EF（加速转发）**：低丢包率、低延迟、高带宽，适用于信令转发（DSCP=46）
- **AF（确保转发）**：订购带宽质量确保，超量按不同丢弃优先级处理，适用于多媒体业务（DSCP=10/12/14/18/20/22/26/28/30/34/36/38）
- **BE（尽力而为）**：缺省PHB，只关注可达性，适用于E-Mail等不敏感业务（DSCP=0）

映射规则可通过 `ADD EPSREMARK`（4G）和 `ADD 5GCREMARK`（5G）命令调整；DSCP/802.1p与内部服务等级映射可通过 `SET QOSBA` 命令调整。

---

### 2.5 业务识别与分流机制

#### 2.5.1 业务识别

TCP/IP网络用五元组（源IP、源端口、目的IP、目的端口、传输层协议）识别业务流。4G使用包过滤器PF（Packet Filter），5G使用包过滤器集PFS（Packet Filter Set）与业务数据包匹配。

PF包含五元组等信息，是识别业务的最小单位；PFS是一组包过滤器的集合。4G的PF有优先级，5G的PFS无优先级定义。

#### 2.5.2 4G vs 5G业务分流差异

| 对比项 | 4G | 5G |
|--------|----|----|
| **映射机制** | 一级映射：数据包 → EPS Bearer | 两级映射：数据包 → QoS Flow → Radio Bearer |
| **对称性** | 具备对称性（上下行处理一致） | 不具备对称性（上下行处理不一致） |
| **UL执行** | UE（使用UL TFT） | UE（使用QoS Rule，N:1对应QoS Flow） |
| **DL执行** | P-GW（使用DL TFT） | UPF（使用PDR）+ RAN（空口映射） |
| **关联工具** | TFT（与EPS Bearer一一对应） | QoS Rule / PDR（与QoS Flow为N:1关系） |

**5G的两级映射**：由于Radio Bearer与QoS Flow可以是一对多关系，5G需要发送端完成数据包 → QoS Flow的映射，空口侧再完成QoS Flow → Radio Bearer的映射。一个PDU会话共用一个NG-U隧道，通过数据包头上的QFI区分属于哪个QoS Flow。

---

### 2.6 SM策略生成：三种规则对比

#### 2.6.1 PCC策略来源

PCC策略有两种来源，优先级从高到低：

1. **PCF下发策略（动态PCC策略）**：策略由PCF定义、SMF执行。用户激活过程中SMF通过N7/Gx接口获取策略和计费控制授权信息。PCF可下发动态规则、预定义规则或预定义规则组。
2. **SMF本地策略（Local Policy）**：网络未部署PCF时使用。SMF/UPF使用本地配置的规则进行策略匹配和执行。PCF下发策略优先级高于本地策略。

#### 2.6.2 三种规则详细对比

| 维度 | 动态规则 | 预定义规则 | 预定义规则组 | 本地规则 |
|------|----------|------------|-------------|----------|
| **PCF** | 定义规则名称和完整内容并下发SMF | 定义的规则名称与SMF/UPF一致，仅下发规则名称 | 定义的规则组名称与SMF/UPF一致，仅下发组名 | 与PCF无关 |
| **SMF** | 将PCF规则内容传递给UPF/RAN/UE | 定义规则名称并传递给UPF | 定义UserProfile名称，绑定多条规则 | 定义UserProfile名称并传递给UPF |
| **UPF** | 根据接收的规则处理数据 | 定义规则名称（须与PCF/SMF一致）及规则具体内容，匹配本地配置后处理 | 定义规则内容，根据UserProfile匹配并按内部优先级处理 | 定义规则内容，根据UserProfile匹配并处理 |
| **规则内容来源** | PCF生成（流条件+动作） | UPF预配置（流条件+动作） | UPF预配置（多条规则的集合） | UPF预配置 |
| **业务识别能力** | 不需UPF业务识别 | 需UPF三四层/七层识别 | 需UPF三四层/七层识别 | 需UPF三四层/七层识别 |
| **实时更新** | PCF可随时增删规则 | PCF可随时增删规则 | PCF可随时增删规则组 | SMF不支持实时更新，新增规则需用户下次上线生效 |
| **使用场景** | 非定向业务流（通用流量包、达量限速、时间段/区域带宽控制） | 定向业务（需七层识别的精细化管理） | 定向业务（需七层识别，多规则批量管理） | 未部署PCF、PCF链路故障、PCF策略异常回滚 |

**规则优先级**：PCF下发的规则采用全局规划优先级。优先级相同时，动态规则优先级高于预定义规则。优先级值越小优先级越高。规则全局优先级在SMF侧定义，与UserProfile内部优先级无关。

**现网建议**：部署PCF时一般使用动态规则和预定义规则；SMF/UPF本地都配置本地规则用于异常情况下保证用户业务体验连续性。

#### 2.6.3 动态规则的策略模型（UPCF定义）

动态规则本质是"在XX**触发**下，**if 满足XX条件 then 执行XX动作**"的逻辑：

| 关键参数 | 解释 |
|----------|------|
| **策略** | 若干触发器和规则的组合。任一触发器事件发生时，UPCF下发策略下定义的规则 |
| **触发器** | 策略决策时机。如：会话建立(IPCAN_EST)、使用量状态上报(US_RE)、位置变更(SAREA_CH/PRA_CH/SCELL_CH/PLMN_CH)、应用类型变更(APP_STA/APP_STP) |
| **条件组** | 条件组合。如用户签约信息（类别/等级）、位置信息（小区/服务区/漫游状态）、上线时间、会话信息（配额状态/DNN） |
| **动作组** | 操作组合。如带宽控制（上下行带宽/专有QoS Flow）、计费控制、消息通知、重定向 |
| **配额** | 三种类型：流量配额、在线时长配额、时长配额（业务使用时长） |
| **漫游区** | 多个PLMN的集合，用于批量策略控制 |

#### 2.6.4 预定义规则的配置逻辑与安装应用

**配置要点**：
- 同一个预定义规则，PCF/SMF/UPF上标识规则名称的参数必须一致
- SMF和UPF上的URR ID必须一致

**预定义规则安装流程**（5步）：
1. 用户开机，发起PDU会话创建请求
2. SMF与PCF建立SM策略偶联，获取SM策略
3. PCF决策生成规则，向SMF下发预定义规则名称和Triggers
4. SMF向UPF发起会话建立请求（携带预定义规则名称、Triggers）
5. UPF安装预定义规则，返回响应。安装后UPF对接收数据报文进行业务识别和策略处理

**预定义规则应用流程**（以FUP场景为例）：
1. 用户访问业务报文到达UPF
2. UPF解析报文（如七层协议+URL）与预定义规则匹配
3. 匹配后按关联策略进行流量累计和带宽处理
4. 流量累计达到阈值时PCF更新规则（删除旧规则，要求安装新规则）
5. SMF/UPF删除旧规则、安装新规则
6. 后续报文按新规则带宽处理

**PCC vs BWM策略类型差异**：
- **PCC策略类型**：定义QoS Flow级整体QoS控制，如所有业务带宽合计不超过100Mbps
- **BWM策略类型**：定义QoS Flow中带宽管理分类策略，可在100Mbps总量下细分FTP 20Mbps + HTTPS 50Mbps + 其他30Mbps

---

### 2.7 5G业务对QoS的诉求

5G三大典型应用场景对网络提出了差异化QoS需求：

| 场景 | 全称 | 核心需求 | 典型业务 |
|------|------|----------|----------|
| **eMBB** | 增强移动宽带 | 大容量、高速、动态带宽分配 | 超高清视频、VR/AR、大文件传输 |
| **uRLLC** | 超可靠低时延通信 | 高可靠、高可用、超低时延 | 自动驾驶、远程手术、工业自动化 |
| **mMTC** | 海量机器类通信 | 大容量连接、低功耗 | 智慧城市IoT、百万设备/km² |

**5G vs 4G QoS挑战**：
- 带宽：5G可达10 Gbps（极限20 Gbps）
- 时延：端到端1~10ms，部分业务要求0.5ms
- 质量：误块率1ms内0.00001（4G为0.01），抖动10~100微秒

---

### 2.8 4G vs 5G QoS架构差异

| 对比项 | 4G | 5G |
|--------|----|----|
| **控制粒度** | EPS Bearer（EBI标识） | QoS Flow（QFI标识） |
| **控制机制** | 信令控制 | 信令控制 + Reflective QoS控制 |
| **数据通路分段** | UE↔P-GW端到端承载，各段一一对应 | UE↔UPF仅空口承载，N QoS Flow ↔ 1 Radio Bearer |
| **QoS映射** | 一级映射：数据包 → EPS Bearer | 二级映射：数据包 → QoS Flow → Radio Bearer |
| **QoS Flow/Bearer级参数** | QCI、ARP、GBR/MBR | 5QI、ARP、GFBR/MFBR、RQA、通知控制 |
| **会话级参数** | APN-AMBR | Session-AMBR |
| **UE级参数** | UE-AMBR | UE-AMBR |
| **默认承载/QoS Flow** | 默认承载只能Non-GBR | 默认QoS Flow可以是Non-GBR或GBR |
| **新增内容** | - | 资源类型Delay Critical GBR（82~85）；平均窗口；最大数据突发容量；新增标准5QI |

---

### 2.9 5G QoS关键参数及概念

#### 2.9.1 参数总览

| 参数 | 含义 | 取值/说明 | 与4G差异 |
|------|------|-----------|----------|
| **5QI** | 5G QoS Identifier，表征QoS Flow的质量特征 | 0~255 | 4G为QCI |
| **ARP** | 分配和保持优先级，含优先级/抢占能力/被抢占属性 | 优先级1~15 | 无差别 |
| **GFBR** | 保障流比特率（UL/DL） | bps | 对应4G的GBR |
| **MFBR** | 最大流比特率（UL/DL） | bps | 对应4G的MBR |
| **Session-AMBR** | 会话级聚合最大比特率 | bps | 对应4G的APN-AMBR |
| **UE-AMBR** | 用户级聚合最大比特率 | bps | 无差别 |
| **RQA** | 反射QoS属性，指示Non-GBR QoS Flow是否支持反射QoS | enabled/disabled | 5G新增 |
| **通知控制** | gNB无法满足GFBR时是否通知核心网 | enabled/disabled | 5G新增 |
| **QoS Profile** | 5G QoS配置文件，决定QoS Flow是否具备保障速率 | - | 无差别 |
| **QoS规则** | UE基于此对上行数据分类标记，关联QFI | - | 4G为TFT |

#### 2.9.2 5QI详解

5QI对应4G的QCI，是业务质量标识，代表资源类型、优先级、可靠性、丢包率等一组参数取值集合。定义标识后，核心网只需传递索引值即可传达一组完整QoS信息。

**5QI资源类型分类**：
- **GBR**（1/2/3/4/65/66/67/75）：保证带宽
- **Non-GBR**（5/6/7/8/9/69/70/79/80）：不保证带宽，受AMBR限制
- **Delay Critical GBR**（82/83/84/85）：5G新增，用于uRLLC高可靠低时延业务

**QFI与5QI的关系**：QFI在PDU会话中唯一标识QoS Flow。QFI可动态分配也可等于5QI。当5QI在QFI范围内（小于64）且为标准/预置值时，可直接作为QFI。其他场景应使用动态分配的QFI。

#### 2.9.3 ARP详解

ARP包含三个子参数，用于控制EPS Bearer/QoS Flow的创建或修改优先级：

- **优先级（Priority Level）**：1~15，值越小优先级越高。资源紧张时决定是否允许创建新承载/QoS Flow
- **抢占能力（Pre-Emption Capability）**：高优先级流是否可抢占低优先级流的资源
- **被抢占属性（Pre-Emption Vulnerability）**：该流是否可能被抢占资源

默认承载/QoS Flow的ARP优先级一般较高，保证缺省承载始终存在。一旦承载建立成功，ARP不再影响数据传输速率，速率仅由QCI/5QI、MBR/MFBR、GBR/GFBR决定。

#### 2.9.4 反射QoS机制

反射QoS是5G新特性：UE根据收到的下行数据分组自行推衍和创建QoS规则，无需SMF提前下发。

**触发方式**：
- **用户面触发**：UPF在能匹配反射规则的DL分组头部封装RQI标识，指示UE建立反射QoS规则
- **控制面触发**：SMF给UE发送标记为"反射型"的QoS规则，UE收到匹配DL分组时才使用

**优势**：无需UE侧提前建立多个QoS Flow和QoS规则，按需触发自动生成，节省资源。

**RQA vs RQI**：RQA是QoS Flow的属性（该流上的包"可能"进行反射QoS），RQI是数据包的指示（携带RQI的包UE才执行反射QoS）。

#### 2.9.5 通知控制

通知控制用于GBR QoS Flow：当RAN侧无法保证GFBR时，RAN向SMF发送通知，SMF可发起N2信令修改或移除QoS Flow。RAN同时保持QoS Flow并继续尝试执行GFBR。网络条件改善后，RAN再次通知SMF恢复GFBR执行。

#### 2.9.6 QoS Flow映射（两级映射）

**4G一级映射**：数据包 →（包过滤器集）→ EPS Bearer。各段承载一一对应，单UE最多15个EPS Bearer。

**5G两级映射**：
- 第一级：数据包 →（包过滤器集）→ QoS Flow（打QFI标记）
- 第二级：QoS Flow →（QFI）→ Radio Bearer

5G最大支持64条QoS Flow，控制精度更细，二级映射由RAN主导，控制方式更灵活。

#### 2.9.7 QoS Profile与QoS Flow的对应关系

| QoS Flow类型 | QoS Profile包含的关键参数 |
|-------------|-------------------------|
| 任意QoS Flow | 5QI + ARP |
| Non-GBR QoS Flow | + RQA（反射QoS仅对Non-GBR有效） |
| GBR QoS Flow | + GFBR + MFBR + 通知控制（通知控制仅对GBR有效） |

---

## 3. 配置调测要点

### 3.1 FUP会话级配置MML

**必选配置（最小集）**：

| 侧 | 命令 | 关键参数 |
|----|------|----------|
| UNC | `SET LICENSESWITCH` | LICITEM=LKV3W9PCBT12, SWITCH=ENABLE |
| UDG | `SET LICENSESWITCH` | LICITEM=LKV3G5PCBT01, SWITCH=ENABLE |

**可选配置**：

| 功能 | 命令 | 关键参数 |
|------|------|----------|
| Monitoring-Key解析方式（Gx） | `SET PCCFUNC` | MKPARSEFORMAT=UNSIGNED32（需与PCRF一致） |
| N7接口特性列表 | `SET PCCFUNC` | N7FEATURELIST=UMC |
| UMCH拥塞处理 | `MOD PCRF` | SUPFEANEGOSW=ENABLE, FEATURELIST=UMCH |
| 会话级FUP排除 | `MOD PCCPOLICYGRP` | FUPSESSIONEXC=ENABLE |
| 重定向流量排除 | `SET SRVCOMMONPARA` | REDIRECTFUP=ENABLE |

### 3.2 SM策略相关参数

**SM策略组成的层次结构**：业务 → 策略 → 触发器 + 规则（条件组 + 动作组）

**QoS参数与带宽控制的关系**：

| 参数 | 带宽控制作用 |
|------|-------------|
| Session-AMBR | 会话级带宽上限（所有Non-GBR QoS Flow聚合） |
| GFBR | 单条GBR QoS Flow的保证带宽 |
| MFBR | 单条GBR QoS Flow的最大带宽 |
| 5QI | 通过资源类型和优先级间接决定调度权重和准入 |
| UE-AMBR | 用户级带宽上限（所有PDU会话的Non-GBR聚合） |

**预定义规则关键约束**：
- PCF/SMF/UPF三方规则名称必须一致
- SMF与UPF的URR ID必须一致
- 规则全局优先级在SMF侧定义，值越小优先级越高

### 3.3 QoS参数映射调整命令

| 命令 | 用途 |
|------|------|
| `ADD EPSREMARK` | 调整4G QoS到DSCP映射规则 |
| `ADD 5GCREMARK` | 调整5G QoS到DSCP映射规则 |
| `SET QOSBA` | 调整DSCP/802.1p与内部服务等级映射 |

### 3.4 FUP调测关键验证消息

| 步骤 | 接口 | 消息 | 验证内容 |
|------|------|------|----------|
| 规则下发验证 | Gx | CCA-I | UsageMonitoringData与规划值一致 |
| 规则下发验证 | N7 | Npcf_SMPolicyControl_Create Response(201) | UsageMonitoringData与规划值一致 |
| 流量上报验证 | N4 | PFCP Session Report Request | 消息携带用户使用流量 |
| 流量转发验证 | Gx | CCR-U（携带Usage-Monitoring-Information AVP） | 上报流量与阈值接近相等 |
| 流量转发验证 | N7 | Npcf_SMPolicyControl_Update Request（携带accuUsageReports） | 上报流量与阈值接近相等 |
| 策略执行验证 | Gx | CCA-U（QoS-Information AVP/Default-EPS-Bearer-QoS AVP） | MBR/AMBR降为设定值 |
| 策略执行验证 | N7 | Npcf_SMPolicyControl_Update Response（QoSData） | MBR/AMBR降为设定值 |

---

## 4. 与带宽控制的关系

### 4.1 FUP会话级是带宽控制的触发器

FUP会话级累计流量策略控制是**会话级带宽控制的触发机制**：
- PCRF/PCF设定流量阈值和对应的QoS策略
- 用户累计流量达到阈值时，PCRF/PCF下发新的QoS参数（降低MBR/AMBR或下发新规则）
- 新QoS参数通过SM策略链路下发到UPF执行，实现带宽降速

### 4.2 SM策略E2E是带宽控制策略下发执行的完整链路

SM策略E2E实现原理描述了带宽控制策略从决策到执行的**完整端到端流程**：

```
PCF决策（生成QoS策略）
    ↓ N7/Gx接口
SMF处理（确定QFI/PFS/QoS参数）
    ↓ N4接口          ↓ N1/N2接口（AMF透传）
UPF执行（QoS标记/限速）   RAN/UE执行（DRB映射/分类标记）
```

- **策略生成阶段**：PCF根据用户信息和业务需求计算带宽控制策略（如限速100Mbps）
- **策略下发阶段**：SMF将策略转化为QoS Flow级别的参数（QFI + GFBR/MFBR/AMBR）
- **策略执行阶段**：UPF/RAN/UE执行QoS控制（限速、调度、队列管理）

### 4.3 QoS参数决定带宽保障/限制的具体值

| QoS参数 | 带宽控制维度 |
|---------|-------------|
| **Session-AMBR** | 会话级总带宽上限——最常用的会话级限速参数 |
| **GFBR** | GBR业务的保证带宽——带宽保障的下限 |
| **MFBR** | GBR业务的最大带宽——带宽限制的上限 |
| **UE-AMBR** | 用户级总带宽上限——跨PDU会话的聚合限制 |
| **5QI** | 通过资源类型和优先级间接决定调度权重——影响带宽优先级 |

### 4.4 三种规则对带宽控制策略的影响

- **动态规则**：适合通用流量包限速（不区分业务），PCF直接下发QoS参数
- **预定义规则**：适合定向业务限速（如视频限速），UPF识别业务后按预设动作执行BWM
- **本地规则**：PCF异常时的带宽保障兜底

### 4.5 5QI→DSCP映射实现承载网带宽差异化

QoS参数映射机制将核心网的QoS决策传递到承载网：高优先级业务（如语音5QI=1→DSCP=46/EF）在承载网中获得低延迟高优先转发，低优先级业务（如缺省流量5QI=9→DSCP=0/BE）获得尽力而为转发。这保证了带宽控制策略在整个E2E链路中的一致执行。

---

## 5. 关键术语

| 术语 | 简释 |
|------|------|
| **FUP** | Fair Usage Policy，公平使用策略。用户用量达到阈值后触发带宽降速或计费变更 |
| **SM策略** | Session Management Policy，会话管理策略。包含QoS、计费、通知等控制策略 |
| **QoS Flow** | 5G数据通路，端到端QoS控制最小粒度，由QFI标识 |
| **QFI** | QoS Flow Identifier，PDU会话中唯一标识QoS Flow |
| **5QI** | 5G QoS Identifier，业务质量标识，映射一组QoS特征 |
| **ARP** | Allocation and Retention Priority，分配和保持优先级，含优先级/抢占/被抢占 |
| **GFBR/MFBR** | 保障/最大流比特率，GBR QoS Flow的带宽参数 |
| **Session-AMBR** | 会话级聚合最大比特率，限制PDU会话所有Non-GBR QoS Flow总速率 |
| **UE-AMBR** | 用户级聚合最大比特率，限制UE所有Non-GBR QoS Flow总速率 |
| **PFS** | Packet Filter Set，包过滤器集，5G业务识别的最小单位集合 |
| **PDR** | Packet Detection Rule，UPF上的包检测规则，N:1对应QoS Flow |
| **QoS Rule** | UE上的QoS规则，用于上行数据分类标记和QoS Flow关联 |
| **UMCH** | Usage Monitoring Congestion Handling，流量监控拥塞处理，配额重置时避免信令拥塞 |
| **PHB** | Per-Hop Behaviour，每跳转发行为，IETF定义EF/AF/BE三种标准 |
| **DSCP** | Differentiated Services Code Point，区分服务编码点，承载网QoS标记 |
| **反射QoS** | 5G新特性，UE根据下行数据自行推衍创建QoS规则 |
| **RQA** | Reflective QoS Attribute，反射QoS属性，指示QoS Flow是否支持反射 |
| **ADC** | Application Detection and Control，应用检测和控制，基于Gx/N7的应用流检测 |
| **动态规则** | PCF配置并生成的完整SM策略规则，含QoS参数等 |
| **预定义规则** | UPF预配置的规则（流条件+动作），PCF下发名称激活 |
| **本地规则** | SMF/UPF本地配置的规则，不依赖PCF |
| **UserProfile** | 预定义规则组/本地规则在SMF/UPF侧的绑定容器 |

---

## 6. 知识来源

| 序号 | 文件名 | 来源专题 |
|------|--------|----------|
| 1 | 系统影响与约束_70687833.md | 5G Core FUP解决方案/会话级累计流量策略控制/原理描述 |
| 2 | 调测会话级累计流量策略控制_24087906.md | 5G Core FUP解决方案/会话级累计流量策略控制 |
| 3 | 配置会话级累计流量策略控制_23928082.md | 5G Core FUP解决方案/会话级累计流量策略控制 |
| 4 | 20.7.0 01（2021-08-30）_24087900.md | 5G Core FUP解决方案/变更描述 |
| 5 | 特性映射_23928078.md | 5G Core FUP解决方案 |
| 6 | QoS Flow建立_修改_删除_86483638.md | 5G PCC之SM策略解决方案/SM策略下发与执行原理 |
| 7 | QoS参数映射机制_86483640.md | 5G PCC之SM策略解决方案/SM策略下发与执行原理 |
| 8 | 业务识别与分流_86483639.md | 5G PCC之SM策略解决方案/SM策略下发与执行原理 |
| 9 | 动态规则_86483635.md | 5G PCC之SM策略解决方案/SM策略生成原理 |
| 10 | 规则相关概念_17152898.md | 5G PCC之SM策略解决方案/SM策略生成原理 |
| 11 | 预定义规则_预定义规则组_本地规则_86483636.md | 5G PCC之SM策略解决方案/SM策略生成原理 |
| 12 | 原理概述_15464534.md | 5G PCC之SM策略解决方案/SM策略E2E实现原理 |
| 13 | 5G业务对QoS的诉求_87689107.md | 5G PCC之SM策略解决方案/SM策略关键内容/QoS |
| 14 | 4G_5G QoS架构差异总结_11970130.md | 5G PCC之SM策略解决方案/SM策略关键内容/QoS/QoS架构 |
| 15 | 5G QoS关键参数及概念_11969173.md | 5G PCC之SM策略解决方案/SM策略关键内容/QoS/QoS架构 |
