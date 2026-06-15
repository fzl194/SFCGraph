# Batch-31: UNC侧5G基础知识 - PCC策略E2E QoS管理与静态规则

> **来源类型**: UNC产品文档 / 5G基础知识 / "一望5G"概念解读系列
> **文档数量**: 10篇
> **视角侧重**: UNC（控制面/SMF/PCF）视角
> **知识定位**: 带宽控制场景的概念基础层，为理解SM策略QoS管控和PCC静态规则提供原理支撑

---

## 1. 概述

本批10篇文档来自UNC 20.15.2产品文档中"5G基础知识 > 一望5G"系列，涵盖两大主题系列：

**系列一：5G PCC策略之E2E QoS管理机制（7篇）**
- 从PCC策略总览出发，以SM策略为主线，端到端（E2E）讲解QoS策略的生成、下发、执行、更新全流程
- 覆盖PCF决策、SMF映射、UPF/RAN/UE执行的完整链路
- 区分Session级和业务级QoS策略，区分PCF发起和SMF发起的两种策略更新路径

**系列二：5G PCC策略之静态规则解读（3篇）**
- What/Why/How三段式解读PCC静态规则（预定义规则+本地规则）
- 侧重UPF侧七层业务识别能力对精细化带宽管理的支撑
- 提供完整的业务套餐配置示例（视频定向流量 + FUP限速场景）

**与UDG侧的差异**: 这些文档与UDG侧5G基础知识文档同属"一望5G"系列，内容相似。但作为UNC产品文档，本批文档的视角更侧重控制面（PCF/SMF侧的策略决策和下发机制），强调SMF在QoS Flow建立、映射、修改中的主导作用，以及PCF作为QoS参数最高决策者的角色定位。

---

## 2. 核心知识点

### 2.1 PCC策略三大类型及SM策略的核心地位

5G PCC策略按3GPP定义分为三大类，其中SM策略是带宽控制的核心载体：

| 策略类型 | 关键参数 | 内容描述 | 策略下发 | 策略执行 |
|----------|----------|----------|----------|----------|
| **SM策略** | QoS Flow级: 5QI、ARP、GFBR/MFBR、RQA、计费参数; 会话级: Session-AMBR | QoS带宽控制、计费控制、短信通知、重定向等，为终端用户提供差异化服务质量 | PCF | SMF |
| **AM策略**（5G新增） | SAR（服务区限制）、RFSP（无线频率选择优先级） | UE允许/不允许接入的TAI列表、无线资源管理 | PCF | AMF、UE、RAN |
| **UE策略**（5G新增） | ANDSP（UE选网策略）、URSP（UE路由选择策略） | 辅助UE选择Non-3GPP接入网、切片选择、DNN选择等路由决策 | PCF | UE |

**关键区别**: AM策略和UE策略是5G新引入的，侧重用户层面（移动性、入网选择）；SM策略侧重用户会话和业务层面的QoS管控，是带宽控制场景的核心策略类型。

**与4G的对比**: 5G在海量连接背景下，单用户接入类型从终端扩展到智能家居、车辆等"物"，5G引入VR/AR等需要超高速率、超低时延的场景。因此5G在SM策略之外新增AM/UE策略，实现更灵活的"按需定制"资源管控。

### 2.2 SM策略中Session级与业务级QoS策略的区别

- **Session级QoS策略**: 以PDU Session为度量单位，1个PDU Session中包含的全部QoS策略内容
- **业务级QoS策略**: 以用户访问的单一业务为度量单位，1个业务包含的QoS策略内容
- **关系**: 一个Session级QoS策略可能包含多个业务级QoS策略。一个PDU Session可以包含多个业务

**带宽控制视角**: Session级QoS策略对应Session-AMBR（会话级带宽上限），业务级QoS策略对应单个业务的5QI/MFBR等参数。带宽控制场景中，FUP限速是典型的业务级QoS管控，Session-AMBR限制是典型的Session级管控。

### 2.3 QoS策略的生成机制（PCF决策 + 静态/动态规则组装）

QoS策略的生成完全由PCF进行"决策"，不存在与UDM、SMF的协商过程。策略最终由多个"规则"组成，**"规则"是QoS策略下发的最小单位**。

规则分为两种：

**静态规则（预定义规则/预定义规则组）**:
- 在SMF/UPF侧提前配置QoS参数（QoS Flow信息 + 规则名等）
- PCF侧根据用户信息配置策略生成的"条件"，结合SMF/UPF提供的预定义规则名，组装生成完整QoS策略
- **适用场景**: 需要对特定业务类型（如FTP、视频业务）进行限速控制等，业务识别只能在UPF上进行
- UPF侧的业务识别配置过程即为静态规则的配置

**动态规则**:
- PCF执行全部QoS参数的配置与QoS生成
- 基于用户位置区域、终端类型、用户等级、业务类型、时间段等输入源，灵活制定上网质量保证规则
- **适用场景**: 不需要区分业务类型的场景，完整QoS策略均由PCF配置下发

**UNC侧关键视角**: PCF虽然拥有QoS参数的最高决策权，但PCF不具备业务识别能力（无法识别七层协议特征）。因此需要UPF配合的精细化带宽控制场景（如基于URL的定向流量管控），必须通过静态规则实现。

### 2.4 QoS策略的生成流程（用户上线时）

1. 用户上线，从UDM获取签约数据（Session-AMBR、ARP、5QI等）
2. 经SMF，请求消息送达PCF
3. PCF根据用户上线携带的切片信息、位置信息等做出决策，生成QoS策略
4. PCF将QoS策略通过应答消息下发给SMF
5. SMF本地安装策略

**降级机制**: 如果网络中没有开启PCC功能或PCF异常导致N7会话不可达，SMF本地也能配置QoS策略，但无法实现PCF侧的精细化策略管控（根据位置、等级、时间段、配额状态、节假日等定制）。

### 2.5 QoS策略的下发与执行（两级映射机制）

PCF将QoS策略下发给SMF后，SMF需要完成两件事：

**任务一: 建立QoS Flow**
- QoS Flow类似4G的承载（Bearer），为数据流传输提供通道
- 不同的通路提供差异化的QoS保障
- 通过QFI（QoS Flow ID）标识

**任务二: 两级参数映射**

| 映射层级 | 映射关系 | 说明 |
|----------|----------|------|
| 数据包 -> QoS Flow | N:1 | UE/UPF将数据包经PFS（Packet Filter Set）识别分类后，映射到对应QoS Flow。类似公交车走公交车道、货车走货车道 |
| QoS Flow -> Radio Bearer | N:1 | RAN决策调度，将多个QoS Flow映射到有限的Radio Bearer上。RAN可动态调整映射关系 |

**两级映射的核心价值**: 4G中"城市道路->高速路->城市道路"是1:1:1的确定关系；5G解耦后可动态调整，高效利用资源有限的Radio Bearer（空口资源）。

**传输层DSCP机制**:
- 上行DSCP映射由基站（RAN）标记
- 下行DSCP值映射由核心网（UPF）标记
- 网络侧可针对不同接口（N3/N6/N9）配置5QI+ARP到DSCP映射规则

### 2.6 GBR与Non-GBR场景的下发差异

**GBR QoS场景**:
- SMF在PDU Session建立/修改/用户面激活时，向UPF/RAN/UE发送消息，携带PCF下发的QoS策略
- RAN和UE根据QoS Flow信息进行相应处理

**Non-GBR QoS场景（Reflective QoS机制）**:
- 5G新引入反射QoS（Reflective QoS）机制，减少PDU Session修改的信令消息
- PCF下发的策略中流信息可仅有下行流，UE自行推导上行QoS Rule
- 关键参数区分:
  - **RQA（Reflective QoS Attribute）**: 定义QoS流的反射"属性"，指定该流上的数据包"可能"进行反射QoS
  - **RQI（Reflective QoS Indication）**: 定义数据包的反射"指示"，UE对携带RQI的包执行反射QoS
- UPF/RAN在指定PFS的数据包头上增加RQI，UE收到后根据包头反推上行PFS

### 2.7 QoS策略更新机制（PCF发起 vs SMF发起）

PDU Session修改有两种触发路径，带宽控制场景的FUP限速、套餐变更等通过这两种路径实现：

#### PCF发起的策略更新

**必要条件**:
- PDU Session处于在线状态
- PCF侧触发的签约数据发生变更（如从客户营帐修改用户状态、等级等）

**原理**: PCF侧更新后的签约数据重新匹配新规则生成的"条件"，匹配成功后将新QoS策略通过Npcf_SMPolicyControl_UpdateNotify Request消息主动下发给SMF，通知SMF删除旧策略、安装新策略。

**典型场景**: 用户生日大礼包（用户属性变更触发新规则下发）、套餐变更等。

#### SMF发起的策略更新

**必要条件**:
- PDU Session处于在线状态
- PCF在PDU Session建立时已订阅需要SMF上报的变更事件
- 订阅事件触发: 用户位置变更、UDM发起的Session-AMBR/5QI/ARP变更、用户配额使用状态变更等

**原理**: PCF订阅的事件发生时，SMF通过Npcf_SMPolicyControl_Update Request消息将变更点发送给PCF；PCF获取变更点后结合签约数据匹配条件，生成新策略，通过Npcf_SMPolicyControl_Update Response消息通知SMF删除旧策略、安装新策略。

**典型场景**: FUP限速（配额耗尽后限速，如20GB后限速至1Mbps）、用户位置变更触发新QoS规则等。

**UNC侧关键视角**: PCF不具备业务类型识别、用户位置变更等能力，因此PCF需要通过"订阅事件"机制让SMF上报这些变更。这是SMF作为控制面执行者的核心职责之一。

### 2.8 更新后的QoS Flow处理逻辑

SMF收到PCF新下发的QoS参数后，判断三种处理场景：

| 场景 | 判断条件 | 处理动作 |
|------|----------|----------|
| 新建QoS Flow | 新下发的5QI和ARP与已有QoS Flow的5QI或ARP至少有一个不相等 | 创建新的QoS Flow |
| 删除QoS Flow | 规则匹配条件不再满足（如套餐耗尽） | 删除旧QoS Flow，释放资源 |
| 修改流描述 | 5QI和ARP不变，但流描述变更（如五元组变化） | 修改UE/UPF的数据包到QoS Flow的映射规则 |

**PFS（Packet Filter Set）的作用**: PFS包含五元组、方向和其他IP头属性等信息，是识别业务的最小单位。PFS匹配结果是决定业务流识别的关键参数。

### 2.9 PCC静态规则体系（What）

PCC规则完整分类:

| 规则类型 | 策略决策者 | 配置位置 | 激活方式 | 适用场景 |
|----------|-----------|----------|----------|----------|
| **动态规则** | PCF | PCF全量配置业务流特征及动作 | PCF实时下发/删除 | 现网部署PCF时的主要规则类型 |
| **预定义规则** | PCF | UPF配置流特征及动作，PCF/SMF/UPF定义相同规则标识 | PCF下发规则标识激活 | 需要七层业务识别的场景 |
| **本地规则** | SMF | UPF配置流特征及动作，SMF/UPF定义相同规则组标识 | SMF下发规则组标识激活 | 未部署PCF或PCC链路故障时降级使用 |

**静态规则（预定义规则 + 本地规则）的核心特点**: 规则内容（流匹配条件和动作）提前在UPF上配置完成，不是由PCF动态生成。用户注册过程中通过下发规则名称/规则组名称激活。

**本地规则的特殊限制**: SMF不支持实时更新规则，在用户已激活且已有生效的本地规则组中新增绑定规则，新增规则不会实时生效，需等用户下次上线才生效。

**UPF支持的流条件和动作**:
- 流条件: 三四层特征（IP、Port、三四层协议）+ 七层特征（URL、HOST、七层协议）
- 支持组合: 三四层any+特定七层、特定三四层+特定七层、特定三四层、三四层any+七层any
- 流动作: 计费、带宽管理、头增强、QoS（支持单动作和组合动作）

### 2.10 PCC静态规则的业务应用（Why + How）

**为什么需要静态规则（Why）**:
- PCF作为策略控制实体，不处理用户数据报文，无法通过七层协议（如HTTP协议特征+URL）识别业务
- UPF作为业务感知及策略执行实体，支持通过协议特征库/解析库识别业务
- 定向流量包、FUP限速等场景需要基于七层特征识别特定业务（如A视频业务），必须通过UPF上的静态规则实现

**工作原理示例（How）**: 以"A视频定向流量 + FUP限速"套餐为例:

| 网元 | 配置要点 | 作用 |
|------|----------|------|
| PCF | 配置规则标识(Prerule01-06)、触发条件、策略类型(PCC/BWM) | 决策何时安装/删除规则，控制流量监控和带宽策略 |
| SMF | 配置相同规则标识，将UmData转换为MK URR传递给UPF | 中继策略信息，流量上报阈值管理 |
| UPF | 配置相同规则标识、流匹配条件(URL+七层协议)、具体动作(带宽值) | 执行业务识别、流量统计、带宽限速 |

**一致性要求**: 同一预定义规则在PCF、SMF、UPF上的规则名称参数取值必须一致；SMF和UPF上的URR ID必须一致。

**规则安装流程**: 用户接入 -> PDU会话创建 -> PCF下发预定义规则名称 -> SMF向UPF发起会话建立携带规则名称 -> UPF安装规则 -> UPF对数据报文进行业务识别和策略执行。

**规则动态更新**: PCF根据流量使用状态（如A视频流量达2000M），删除旧规则(Prerule02: 100Mbps)并安装新规则(Prerule03: 25Mbps)，实现FUP限速。

---

## 3. 配置调测要点

### 3.1 QoS参数体系

| 参数层级 | 参数名称 | 含义 |
|----------|----------|------|
| QoS Flow级 | 5QI | QoS通路的综合评估标识，决定通道的传输质量等级 |
| QoS Flow级 | ARP | 分配和保持优先级，标识业务获取空口资源的能力 |
| QoS Flow级 | GFBR/MFBR | 保证流比特率/最大流比特率，GFBR是承诺速率，MFBR是最高速率 |
| QoS Flow级 | RQA | 反射QoS属性，标记QoS Flow是否具备反射QoS能力 |
| 会话级 | Session-AMBR | 会话聚合最大比特率，一个PDU Session的带宽上限 |
| 用户级 | UE-AMBR | 终端聚合最大比特率，一个UE所有Session的总带宽上限 |

### 3.2 静态规则配置要素

- **规则标识一致性**: PCF/SMF/UPF三侧的预定义规则名称必须完全一致
- **URR ID一致性**: SMF和UPF之间的URR ID必须对齐，确保流量统计信息正确传递
- **流匹配条件**: 根据业务场景选择三四层特征、七层特征或组合
- **动作关联**: 每条规则关联具体动作（计费、带宽管理、QoS等），支持单动作和组合
- **优先级规划**: 多条规则同时匹配时按优先级处理（高/较高/低等）

### 3.3 PCC功能开关与降级

- 正常场景: PCC功能开启，PCF生成精细化策略（含动态规则和预定义规则）
- 降级场景1: PCF异常/N7不可达 -> SMF本地配置QoS策略（粗粒度）
- 降级场景2: SMF和PCF链路故障 -> SMF使用本地规则（需配置回滚为本地PCC用户）
- 降级场景3: 未部署PCF -> 直接使用本地规则

### 3.4 Npcf_SMPolicyControl接口关键消息

| 消息 | 方向 | 用途 |
|------|------|------|
| Npcf_SMPolicyControl_Create Request/Response | SMF<->PCF | PDU Session建立时获取初始QoS策略 |
| Npcf_SMPolicyControl_UpdateNotify Request | PCF->SMF | PCF主动发起策略更新通知 |
| Npcf_SMPolicyControl_Update Request/Response | SMF<->PCF | SMF上报变更事件，PCF返回新策略 |

---

## 4. 与带宽控制的关系

### 4.1 E2E QoS管理是带宽控制的全链路视角

本批文档描述的SM策略QoS管理机制，完整覆盖了带宽控制从决策到执行的端到端链路:

```
PCF(策略决策) -> SMF(策略映射/QoS Flow建立) -> UPF(下行QFI标记/策略执行)
                                          -> RAN(Radio Bearer调度/空口资源管理)
                                          -> UE(上行PFS匹配/QoS Rule推导)
```

带宽控制场景中的Session-AMBR限制、业务级5QI/MFBR参数、FUP限速等，全部通过这条链路落地执行。

### 4.2 PCC静态规则是精细化带宽控制的载体

带宽控制场景的核心需求:
- **定向流量管控**: 需要七层业务识别（URL+协议），PCF无法独立完成
- **FUP限速**: 需要流量累计监控，通过预定义规则+URR机制实现
- **多业务差异化带宽**: 不同业务不同速率，通过预定义规则的优先级和动作组合实现

这些需求都依赖PCC静态规则体系: PCF提供决策框架，UPF提供业务识别和执行能力。

### 4.3 SM策略QoS更新是动态带宽调整的核心机制

带宽控制场景中的动态带宽调整（如FUP触发限速、套餐变更调整速率）通过两种路径实现:

- **PCF主动更新**: 用户属性变更（等级提升、套餐变更）触发新规则下发
- **SMF事件上报**: 流量配额耗尽、位置变更等PCF订阅事件触发，SMF上报后PCF重新计算策略

两种路径最终都通过"删除旧规则 -> 安装新规则"的方式实现QoS Flow级别的带宽调整。

### 4.4 UNC侧特有的控制面视角

与UDG侧文档相比，本批文档作为UNC产品文档，更强调:
- **PCF的决策者角色**: PCF拥有QoS参数最高决策权，SM策略生成完全由PCF决策
- **SMF的中枢角色**: SMF负责QoS Flow的建立/修改/删除，以及参数到RAN/UPF/UE的映射
- **Npcf接口的交互细节**: PCF与SMF之间的策略下发、更新通知、事件订阅机制
- **PCC功能降级机制**: 无PCF时SMF本地配置策略的降级方案

这些控制面机制是理解带宽控制策略如何在网络中落地执行的基础。

---

## 5. 关键术语

| 术语 | 全称 | 简释 |
|------|------|------|
| PCC | Policy and Charging Control | 策略与计费控制，5G核心网中用于QoS管控和计费控制的框架 |
| PCF | Policy Control Function | 策略控制功能网元，PCC策略的决策中心 |
| SMF | Session Management Function | 会话管理功能网元，负责PDU Session管理和QoS Flow控制 |
| QoS Flow | - | 5G中数据传输的QoS通道，类似4G的Bearer（承载），通过QFI标识 |
| QFI | QoS Flow ID | QoS Flow的标识符 |
| PFS | Packet Filter Set | 包过滤器集合，包含五元组等信息，用于业务流识别 |
| 5QI | 5G QoS Identifier | 5G QoS标识符，标示QoS Flow的传输质量等级 |
| ARP | Allocation and Retention Priority | 分配和保持优先级，控制QoS Flow建立/修改的优先级 |
| GFBR | Guaranteed Flow Bit Rate | 保证流比特率，GBR QoS Flow的承诺速率 |
| MFBR | Maximum Flow Bit Rate | 最大流比特率，QoS Flow允许的最高速率 |
| Session-AMBR | Session Aggregate Maximum Bit Rate | 会话聚合最大比特率，一个PDU Session的带宽上限 |
| RQA | Reflective QoS Attribute | 反射QoS属性，标记QoS Flow是否具备反射QoS能力 |
| RQI | Reflective QoS Indication | 反射QoS指示，标记具体数据包是否执行反射QoS |
| DSCP | Differentiated Services Codepoint | 差异化服务代码点，传输层QoS标记 |
| URR | Usage Reporting Rule | 使用量上报规则，用于流量统计和上报 |
| UmData | Usage Monitoring Data | 使用量监控数据，PCF下发的流量监控配置 |
| AMBR | Aggregate Maximum Bit Rate | 聚合最大比特率 |
| RAN | Radio Access Network | 无线接入网 |
| UPF | User Plane Function | 用户面功能网元，策略执行实体 |
| AMF | Access and Mobility Management Function | 接入和移动性管理功能网元 |
| UDM | Unified Data Management | 统一数据管理网元，存储用户签约数据 |
| DNN | Data Network Name | 数据网络名称，类似4G的APN |
| PDU Session | - | 协议数据单元会话，UE到DN的数据连接 |
| Radio Bearer | - | 无线承载，空口资源通道 |
| SAR | Service Area Restrictions | 服务区限制，AM策略关键参数 |
| RFSP | RAT Frequency Selection Priority | 无线频率选择优先级索引 |
| ANDSP | Access Network Discovery & Selection Policy | UE选网策略 |
| URSP | UE Route Selection Policy | UE路由选择策略 |
| FUP | Fair Usage Policy | 公平使用策略，流量达到阈值后限速 |
| BWM | Bandwidth Management | 带宽管理 |

---

## 6. 知识来源

| 序号 | 文件名 | 所属系列 |
|------|--------|----------|
| 1 | SM策略之QoS的下发与执行_33030755.md | E2E QoS管理机制 |
| 2 | PCF发起的策略更新_86168492.md | E2E QoS管理机制 |
| 3 | SMF发起的策略更新_85720414.md | E2E QoS管理机制 |
| 4 | 更新后的QoS策略下发与执行_86008546.md | E2E QoS管理机制 |
| 5 | SM策略之QoS的生成_85848900.md | E2E QoS管理机制 |
| 6 | SM策略之QoS的管理机制_32686211.md | E2E QoS管理机制 |
| 7 | 5G PCC策略—E2E QoS管理机制_32945129.md | E2E QoS管理机制 |
| 8 | PCC静态规则原理——How？_86009740.md | PCC静态规则解读 |
| 9 | 何为PCC静态规则——What？_86169704.md | PCC静态规则解读 |
| 10 | 使用PCC静态规则——Why？_32946325.md | PCC静态规则解读 |

**原始路径前缀**: `output/UNC 20.15.2 产品文档(裸机容器) 05/5G基础知识/一望5G/5G Core业务解决方案解读/`

**关联知识**:
- E2E QoS管理机制系列: 5G PCC策略总览 -> SM策略QoS管理机制 -> QoS生成 -> QoS下发与执行 -> QoS更新(PCF/SMF发起) -> 更新后下发与执行
- PCC静态规则解读系列: What(规则定义) -> Why(业务需求) -> How(配置实现)
- 本批知识为带宽控制场景提供原理基础，后续特性文档和业务专题在此基础上展开具体配置实现
