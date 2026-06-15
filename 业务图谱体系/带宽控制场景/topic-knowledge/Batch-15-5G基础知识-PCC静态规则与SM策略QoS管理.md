# Batch-15: 5G基础知识 - PCC静态规则与SM策略QoS管理机制

---

## 1. 概述

本文件融合提炼自"5G基础知识/一望5G"目录下的两组概念文档，涵盖两大主题：

**主题一：PCC静态规则**（What / Why / How / 结语）
- 何为PCC静态规则：动态规则、预定义规则、本地规则的定义与区别
- 为何使用PCC静态规则：PCF不具备业务识别能力，需借助UPF的七层识别实现精细化管理
- PCC静态规则原理：业务套餐设计、参数规划、规则安装与应用流程
- 结语：带宽精细化管理对用户、内容提供商、运营商三方的意义

**主题二：SM策略之QoS管理机制**（总览 / 生成 / 下发执行 / 更新）
- QoS管理机制总览：Session级与业务级QoS策略的区别、信令面与数据面分工
- QoS策略的生成：PCF决策、静态规则与动态规则的组装逻辑
- QoS策略的下发与执行：两级映射（数据包 -> QoS Flow -> Radio Bearer）、GBR/Non-GBR场景差异、反射QoS
- QoS策略的更新：PCF发起 vs SMF发起的触发条件与信令流程
- 更新后的QoS下发与执行：新建QoS Flow、删除旧QoS Flow、修改流描述的判断逻辑

这两组文档共同构成了5G PCC策略框架中"策略如何定义、如何生成、如何下发、如何执行、如何更新"的完整知识链，是理解带宽控制场景底层机制的基础。

---

## 2. 核心知识点

### 知识点1：PCC规则的三种类型——动态规则、预定义规则、本地规则

PCC规则分为三类，其核心区别在于策略决策者、规则内容来源和激活方式：

| 维度 | 动态规则 | 预定义规则 | 本地规则 |
|------|----------|------------|----------|
| 策略决策者 | PCF | PCF | SMF |
| 规则内容来源 | PCF动态生成（含流匹配条件和动作） | UPF上预配置（含流匹配条件和动作） | UPF上预配置（含流匹配条件和动作） |
| 激活方式 | PCF直接下发完整规则 | PCF下发规则标识（名称），激活UPF/SMF上的预配置 | SMF下发规则组标识，激活UPF上的预配置 |
| 配置要求 | SMF/UPF无需特殊配置 | PCF/SMF/UPF上需定义相同的规则标识 | SMF/UPF上需定义相同的规则组标识 |
| 实时更新 | PCF可随时删除旧规则、安装新规则 | PCF可随时删除旧规则、安装新规则 | SMF不支持实时更新，新增绑定规则需用户下次上线生效 |
| 适用场景 | 不需要业务类型识别的场景 | 需要七层业务识别的精细化管理场景 | 未部署PCF、PCF链路故障或SMF未开启PCC功能开关时 |

预定义规则和本地规则统称为**静态规则**，因为规则内容（流匹配条件和动作）是提前在UPF上配置好的，而非由PCF动态生成。

现网部署了PCF时，一般使用动态规则和预定义规则。本地规则适用于无PCF部署、PCF链路故障或PCF策略异常且SMF配置了回滚为本地PCC用户的场景。

### 知识点2：PCC静态规则的本质——弥补PCF业务识别能力不足

PCF作为策略控制实体，不处理用户数据报文，因此不具备通过七层协议（如HTTP协议特征 + URL）识别业务的能力。而UPF作为业务感知及策略执行的实体，支持通过协议特征库/解析库识别业务。

**核心矛盾**：当业务套餐需要按特定业务类型（如A视频业务）进行差异化计费或带宽控制时，必须先识别出"哪些报文属于A视频业务"。PCF无法做到这一点，只能依靠UPF的七层识别能力。

**解决方案**：在UPF上预定义规则内容（包括七层流匹配条件和对应的计费/带宽管理动作），PCF通过下发规则标识来激活这些预定义规则。UPF识别出特定业务流后，按照静态规则中规划的精细化管理动作进行处理。

UPF支持的流匹配条件包括：
- 三四层特征：IP、Port、三四层协议等
- 七层特征：URL、HOST、七层协议等
- 组合模式：三四层any + 特定七层特征、特定三四层特征 + 特定七层特征、三四层any + 七层any等

UPF支持的流动作包括：计费、带宽管理（BWM）、头增强、QoS等。支持单个动作或多个动作组合（如计费 + FUP）。

### 知识点3：PCC静态规则的典型应用场景

**场景1：定向流量包（内容提供商合作）**
- 用户购买20G通用流量 + 30G A视频专项流量
- 访问A视频时优先计入30G专项流量，耗尽后计入通用流量
- 需要通过七层协议 + URL识别A视频业务 -> 必须使用预定义规则

**场景2：FUP公平使用（按业务限速）**
- 用户每天访问A视频流量在2000M以内时速率100Mbps，超过后降至25Mbps
- 需要按业务类型累计流量并动态切换速率 -> 必须使用预定义规则

**场景3：通用流量限速（FUP公平使用）**
- 用户本月通用流量20G以内时速率50Mbps，超过后降至1Mbps
- 不涉及区分业务类型，可使用动态规则或预定义规则

**核心判断依据**：是否需要七层业务识别。需要 -> 必须预定义规则；不需要 -> 动态规则或预定义规则均可。

### 知识点4：PCC静态规则的工作流程

**规则安装流程**（用户接入时）：
1. 用户开机，发起PDU会话创建请求
2. SMF选择PCF，与PCF建立SM策略偶联并获取SM策略
3. PCF决策并生成规则，向SMF下发预定义规则名称（如Prerule01）、动态规则、Triggers等信息
4. SMF选择UPF，向UPF发起会话建立请求（携带预定义规则名称、动态规则、Triggers等）
5. UPF安装预定义规则及动态规则，返回响应
6. UPF安装成功后，对数据报文进行业务识别，匹配预定义规则的过滤条件，按关联动作处理报文

**规则应用流程**（用户访问业务时）：
1. 用户业务报文到达UPF
2. UPF解析报文特征（如URL、七层协议），与预定义规则中的流匹配条件进行匹配
3. 匹配成功后，UPF根据关联的策略（计费、带宽管理等）处理报文
4. 当业务累计流量达到阈值时，PCF更新规则（删除旧规则、安装新规则）
5. SMF/UPF删除旧预定义规则，安装新预定义规则
6. 后续报文按新规则处理

**关键约束**：
- 同一预定义规则在PCF、SMF、UPF上的规则标识（名称）必须一致
- SMF和UPF上的URR ID必须一致
- 优先级参数决定规则匹配顺序（高优先级先匹配）

### 知识点5：SM策略QoS管理机制总览

SM策略侧重从用户Session和业务层面进行QoS管控，分为两个层级：

- **Session级QoS策略**：以PDU Session为度量单位，一个PDU Session中包含的全部QoS策略内容
- **业务级QoS策略**：以用户访问的业务为度量单位，一个业务包含的QoS策略内容

两者关系：一个Session级QoS策略可能包含多个业务级QoS策略内容（一个PDU Session可承载多个业务）。

**E2E QoS实现机制从两个维度分析**：
- **信令面**：将QoS Flow建立起来，侧重QoS策略的生成和下发
- **数据面**：基于已建好的QoS Flow做业务，侧重QoS策略的执行和保障

**各网元职责**：

| 网元 | 职责 |
|------|------|
| PCF | QoS参数最高决策者，根据用户签约、位置、等级等信息决策生成QoS策略 |
| SMF | 处理PCF下发的SM Policy，确定QoS Flow信息（QFI、PFS、QoS参数），控制QoS Flow的建立/修改/删除 |
| UDM | 用户数据签约，分配默认QoS Flow的ARP/5QI，提供Session-AMBR和UE-AMBR |
| AMF | 信令建立通道，信息透传 |
| UPF | QoS策略执行网元，处理PFS和QoS信息，下行QFI标记和控制，上行QFI验证 |
| RAN | 将信令面QoS参数映射到用户面，实现业务服务质量控制 |

**QoS策略全生命周期**：
1. 策略生成（步骤1）：用户上线 -> UDM获取签约数据 -> PCF决策生成QoS策略 -> 下发给SMF安装
2. 策略下发（步骤2）：SMF将策略分别下发给UPF、RAN（经AMF透传）和UE
3. 策略执行（步骤3）：UPF/RAN/UE执行策略，将业务流映射到对应QoS Flow/DRB

### 知识点6：SM策略QoS的生成机制

QoS策略由多个规则组成，**"规则"是QoS策略下发的最小单位**。规则分为静态规则和动态规则两种。

**静态规则（预定义规则）生成逻辑**：
- SMF/UPF侧预配置QoS参数（含QoS Flow信息和规则名）
- PCF侧配置策略生成的"条件"
- PCF结合SMF/UPF提供的预定义规则名，组装生成完整QoS策略
- 适用场景：需要UPF进行七层业务识别的场景（如对FTP业务限速）

**动态规则生成逻辑**：
- PCF独立完成QoS参数配置与策略生成
- 策略计算输入源：用户位置区域、终端类型、用户等级、业务类型、时间段等
- 适用场景：不需要区分业务类型的场景（如不区分视频/下载/其他业务的统一QoS管控）

**关键原则**：PCF是QoS策略的唯一决策者，策略生成过程不存在与UDM、SMF的协商。若网络中未开启PCC功能或PCF异常导致N7会话不可达，SMF可使用本地配置的QoS策略，但SMF本地策略灵活性较差（无法根据位置、等级、时间段、配额状态等精细化定制）。

### 知识点7：SM策略QoS的下发与执行——两级映射机制

PCF下发的QoS策略到达SMF后，SMF需要完成两件事：
1. 建立QoS Flow（为数据流传输提供通道，不同通道提供差异化QoS保障）
2. 进行参数映射（将QoS参数映射为RAN/UPF/UE可识别的参数）

**两级映射机制**：

| 映射层级 | 映射关系 | 说明 |
|----------|----------|------|
| 数据包 -> QoS Flow | N:1 | UE/UPF通过PFS（Packet Filter Set）对数据包进行业务识别分类，映射到对应QoS Flow |
| QoS Flow -> Radio Bearer | N:1 | 由RAN决策调度，将QoS Flow映射到Radio Bearer（空口资源有限，需动态调度） |

**两级映射的设计意义**：数据包和Radio Bearer与QoS Flow都是N:1的映射关系，两级映射解耦，二级映射全权由RAN主导，使RAN的QoS控制更加灵活。相比4G的1:1:1确定映射关系，5G能根据"高速道路拥堵"情况动态调整，高效利用有限的空口资源。

**传输层DSCP标记**：
- 上行DSCP映射由基站标记
- 下行DSCP值映射由核心网标记
- 网络侧可针对不同接口（N3/N6/N9）配置5QI + ARP到DSCP映射规则

### 知识点8：GBR QoS与Non-GBR QoS的下发差异

**GBR QoS场景**：
- SMF在PDU Session建立/修改/用户面激活时向UPF/RAN/UE发送消息
- 携带PCF下发的QoS策略（含QoS Flow信息）
- RAN和UE根据收到的QoS Flow信息进行相应的QoS Flow处理

**Non-GBR QoS场景**：
- 5G引入了Reflective QoS（反射QoS）机制
- PCF下发的策略中流信息可以仅含下行流
- UPF/RAN在指定PFS数据包头添加RQI（Reflective QoS Indication）
- UE收到含RQI的下行数据包后，自行推导上行QoS Rule
- 目的：减少新应用部署时PDU Session修改的信令开销

**反射QoS的两个关键概念**：
- **RQA**（Reflective QoS Attribution）：定义一个QoS流的反射"属性"，该QoS流上的数据包"可能"进行反射QoS
- **RQI**（Reflective QoS Indication）：定义某些数据包的反射"指示"，UE对携带RQI的数据包进行反射QoS
- 一个具备RQA属性的QoS流上的数据包不一定全部应用反射QoS，只有携带RQI的才应用

### 知识点9：QoS策略的更新——PCF发起 vs SMF发起

QoS策略更新有两种触发方式，对应实际中的不同场景：

**PCF发起的策略更新**：

触发条件：
- PDU Session处于在线状态
- PCF侧触发的签约数据发生变更（如用户状态、等级变更，可从营帐侧修改触发）

更新原理：
- PCF侧更新后的签约数据重新匹配新规则生成的"条件"
- 若匹配成功，PCF通过Npcf_SMPolicyControl_UpdateNotify Request消息主动下发新QoS策略给SMF
- 通知SMF删除旧策略，安装新策略

典型场景：用户生日赠送流量、老客户权益升级等基于用户属性变更的策略调整。

**SMF发起的策略更新**：

触发条件：
- PDU Session处于在线状态
- PCF在PDU Session建立时订阅的需要SMF上报的变更事件发生（SMF不能主动发起，必须基于PCF订阅的事件）

可触发的变更事件包括：
- 用户位置变更
- UDM发起的Session-AMBR/5QI/ARP变更
- 用户配额使用状态变更（如流量耗尽）

更新原理：
- 变更事件经AMF透传给SMF后，SMF通过Npcf_SMPolicyControl_Update Request消息发送变更点给PCF
- PCF结合UDM签约的QoS策略全局数据，匹配条件，生成新QoS策略
- PCF通过Npcf_SMPolicyControl_Update Response消息通知SMF删除旧策略，安装新策略

典型场景：用户月度流量配额耗尽后限速（FUP核心机制）。

**两者关键区别**：PCF发起是PCF侧签约数据变更直接驱动；SMF发起是SMF检测到PCF订阅的事件后上报PCF，由PCF决策后驱动。

### 知识点10：更新后的QoS策略下发与执行——三种QoS Flow变更场景

SMF收到PCF更新后的QoS策略后，根据最新QoS profile（主要是5QI和ARP）判断需要进行哪种操作：

**场景1：新建QoS Flow**
- 判断依据：PCF新下发的5QI和ARP与已有QoS Flow流的5QI和ARP只要有一个不相等
- 结果：创建新的QoS Flow流
- 说明：不同的5QI或ARP代表不同的QoS保障等级，需要独立的QoS Flow承载

**场景2：删除已有QoS Flow**
- 判断依据：PCF以"规则"粒度下发策略，触发"规则"下发的条件（如流量阈值达到、时间段切换）是决策关键
- 结果：删除旧的QoS Flow，新建新的QoS Flow
- 说明：旧规则被删除意味着旧QoS Flow不再被任何规则引用

**场景3：修改已有流描述**
- 判断依据：5QI和ARP与已建好的流保持一致（QoS等级不变），但部分流描述（如五元组PFS）有变更
- 结果：修改业务数据包到QoS Flow的映射规则
- 说明：类似于让原本走在QoS Flow1上的某业务调整到QoS Flow2，业务流识别的关键参数变更

**PFS（Packet Filter Set）**：5G使用包过滤器集与业务数据包进行匹配，实现业务识别。PF包含五元组、方向和其他IP头属性等信息，是识别业务的最小单位。PFS是一组包过滤器的集合。

---

## 3. 配置调测要点

### 3.1 PCC静态规则配置要点

**参数一致性约束**（关键调测检查项）：
- 同一预定义规则在PCF、SMF、UPF上的规则标识（名称）必须完全一致
- SMF和UPF上的URR ID必须一致
- 不一致会导致规则安装失败或流量统计错误

**PCF侧配置**：
- 配置规则标识（如Prerule01）和对应的下发/删除逻辑
- 配置策略类型（PCC计费、BWM带宽管理等）
- 配置优先级（多规则场景下的匹配顺序）
- 配置触发条件（如流量阈值、时间段）

**SMF侧配置**：
- 配置与PCF/UPF一致的规则标识
- 将UmData转换为MK URR，传递给UPF
- 配置策略类型转换逻辑

**UPF侧配置**：
- 配置流匹配条件（三四层特征和/或七层特征）
- 配置关联动作（计费、BWM、QoS等）
- 配置URR ID与SMF一致
- 配置带宽参数（如100Mbps、25Mbps、50Mbps、1Mbps等不同档位）

### 3.2 SM策略QoS配置关键参数

| 参数 | 含义 | 作用 |
|------|------|------|
| 5QI | 5G QoS Identifier | 标识QoS特征（优先级、时延、丢包率等），由标准化和非标准化两类 |
| ARP | Allocation and Retention Priority | 分配与保持优先级，含优先级、抢占能力、抢占脆弱性 |
| GFBR | Guaranteed Flow Bit Rate | 保证流比特率（仅GBR QoS Flow），QoS Flow必须保证的速率 |
| MFBR | Maximum Flow Bit Rate | 最大流比特率，QoS Flow允许的最大速率 |
| Session-AMBR | Session Aggregate Maximum Bit Rate | PDU Session聚合最大比特率 |
| UE-AMBR | UE Aggregate Maximum Bit Rate | UE聚合最大比特率 |
| GBR | Guaranteed Bit Rate | 保证比特率（GBR QoS Flow专有） |
| MBR | Maximum Bit Rate | 最大比特率 |
| QFI | QoS Flow Identifier | QoS Flow标识符，唯一标识一个QoS Flow |
| PFS | Packet Filter Set | 包过滤器集，业务识别的最小单位集合 |

### 3.3 QoS Flow变更判断规则

SMF在收到更新后的QoS策略时，按以下逻辑判断QoS Flow操作：
1. 比对5QI和ARP：任一不同 -> 新建QoS Flow
2. 5QI和ARP相同但流描述（PFS/五元组）变更 -> 修改已有QoS Flow的映射规则
3. 旧规则被删除且旧QoS Flow无规则引用 -> 删除旧QoS Flow

### 3.4 信令流程要点

**策略生成阶段**：
- 用户上线 -> UDM获取签约数据 -> PCF决策生成QoS策略 -> SMF安装策略

**策略下发阶段**：
- SMF -> UPF（N4接口，直接下发）
- SMF -> AMF -> RAN（经AMF透传）
- SMF -> AMF -> UE（经AMF透传）

**策略更新信令**：
- PCF发起：Npcf_SMPolicyControl_UpdateNotify Request（PCF -> SMF）
- SMF发起：Npcf_SMPolicyControl_Update Request（SMF -> PCF）+ Npcf_SMPolicyControl_Update Response（PCF -> SMF）

### 3.5 反射QoS配置要点

- RQA（Reflective QoS Attribution）：在QoS Flow级别配置反射属性
- RQI（Reflective QoS Indication）：在数据包级别标记反射指示
- UPF/RAN在满足条件的下行数据包上添加RQI
- UE检测到RQI后自动推导上行QoS Rule，无需额外信令

---

## 4. 与带宽控制的关系

PCC静态规则和SM策略QoS管理机制是带宽控制场景的两大底层支撑：

**PCC静态规则 -> 带宽控制策略的载体**：
- 预定义规则中关联的BWM（带宽管理）动作，是UPF执行带宽限速的直接依据
- 通过切换不同的预定义规则（如Prerule02的100Mbps vs Prerule03的25Mbps），实现FUP限速切换
- PCF通过监控业务累计流量，在阈值达到时删除旧规则、安装新规则，完成带宽策略的动态切换
- 七层业务识别能力使得按业务类型差异化限速成为可能（如视频业务单独限速）

**SM策略QoS管理 -> 带宽控制执行的核心机制**：
- QoS Flow是带宽保障的管道：GBR QoS Flow提供保证带宽（GFBR），Non-GBR QoS Flow提供尽力而为的带宽
- 5QI参数决定了QoS Flow的传输特性（优先级、时延、丢包率），间接决定带宽保障级别
- AMBR参数（Session-AMBR、UE-AMBR）直接限制PDU Session或UE的总带宽
- ARP参数决定带宽资源紧张时的抢占优先级

**两者协同关系**：
- PCC静态规则负责"识别业务并关联带宽管理动作"
- SM策略QoS管理负责"建立带宽保障通道并下发执行"
- 预定义规则中的BWM动作最终通过QoS参数（如5QI映射的MFBR、AMBR）在QoS Flow上执行
- FUP场景中，配额耗尽触发SMF上报 -> PCF重新决策 -> 更新QoS策略 -> SMF修改QoS Flow参数 -> 实现限速

**典型带宽控制场景的实现路径**：
1. UPF上配置预定义规则（七层识别 + BWM限速动作）
2. 用户上线，PCF下发预定义规则标识激活规则
3. UPF识别业务流并按BWM动作限速
4. 流量累计达到阈值，SMF上报配额状态变更
5. PCF生成新QoS策略（含新的限速参数）
6. SMF更新QoS Flow或新建QoS Flow
7. UPF/RAN/UE执行新的带宽控制策略

---

## 5. 关键术语

| 术语 | 全称/含义 |
|------|-----------|
| PCC | Policy and Charging Control，策略与计费控制，5G核心网中用于制定和执行业务策略的框架 |
| PCC规则 | 分为动态规则、预定义规则和本地规则三类，是PCC策略控制的基本单元 |
| 预定义规则 | UPF/SMF/PCF上预配置相同标识的PCC规则，PCF通过下发标识激活，UPF上配置流匹配条件和动作 |
| 本地规则 | 仅在SMF/UPF上配置的PCC规则，SMF通过规则组标识激活，决策者为SMF |
| 动态规则 | 由PCF动态生成并直接下发的PCC规则，包含完整的流匹配条件和动作 |
| SM策略 | Session Management Policy，会话管理策略，5G三大PCC策略之一，侧重Session和业务层面的QoS管控 |
| Session级QoS | 以PDU Session为度量单位的QoS策略 |
| 业务级QoS | 以用户访问的特定业务为度量单位的QoS策略 |
| 5QI | 5G QoS Identifier，5G QoS标识符，标准化或非标准化的QoS特征标识 |
| ARP | Allocation and Retention Priority，分配与保持优先级，含优先级、抢占能力、抢占脆弱性三个子参数 |
| QoS Flow | 5G中QoS控制的最小粒度，类似4G的承载（Bearer），通过QFI标识 |
| QFI | QoS Flow Identifier，QoS Flow标识符 |
| GBR | Guaranteed Bit Rate，保证比特率，GBR QoS Flow必须保证的最低速率 |
| Non-GBR | 非保证比特率QoS Flow，无速率保证，尽力而为 |
| GFBR | Guaranteed Flow Bit Rate，保证流比特率 |
| MFBR | Maximum Flow Bit Rate，最大流比特率 |
| Session-AMBR | PDU Session聚合最大比特率 |
| UE-AMBR | UE聚合最大比特率 |
| PFS | Packet Filter Set，包过滤器集，业务识别的最小单位集合，含五元组、方向等 |
| Radio Bearer | 无线承载，空口资源通道，QoS Flow到Radio Bearer的映射由RAN主导 |
| DSCP | Differentiated Services Codepoint，差分服务代码点，传输层QoS标记 |
| Reflective QoS | 反射QoS，UE根据下行数据包推导上行QoS Rule的机制 |
| RQA | Reflective QoS Attribution，QoS Flow级别的反射属性标记 |
| RQI | Reflective QoS Indication，数据包级别的反射指示标记 |
| BWM | Bandwidth Management，带宽管理，PCC规则中的一种动作类型 |
| UmData | Usage Monitoring Data，用量监控数据，PCF下发的流量监控配置 |
| MK URR | Measurement Key Usage Reporting Rule，测量键使用量上报规则 |
| FUP | Fair Usage Policy，公平使用策略，对超过配额的用户进行限速等控制 |
| URR | Usage Reporting Rule，使用量上报规则，UPF用于流量统计和上报 |
| SA | Service Awareness，业务感知，UPF通过协议特征库/解析库识别业务的能力 |

---

## 6. 知识来源

本文件融合提炼自以下10个产品文档md：

| 序号 | 文件名 | 主题归属 |
|------|--------|----------|
| 1 | 何为PCC静态规则——What？_86169704.md | PCC静态规则定义与类型 |
| 2 | 使用PCC静态规则——Why？_32946325.md | PCC静态规则使用动机与场景 |
| 3 | PCC静态规则原理——How？_86009740.md | PCC静态规则配置与应用流程 |
| 4 | 结语_33031965.md | 带宽精细化管理展望 |
| 5 | SM策略之QoS的管理机制_32686211.md | QoS管理机制总览（Session级/业务级、网元职责、全生命周期） |
| 6 | SM策略之QoS的生成_85848900.md | QoS策略生成机制（静态规则与动态规则组装逻辑） |
| 7 | SM策略之QoS的下发与执行_33030755.md | QoS策略下发与执行（两级映射、GBR/Non-GBR、反射QoS） |
| 8 | PCF发起的策略更新_86168492.md | PCF发起的QoS策略更新原理与信令流程 |
| 9 | SMF发起的策略更新_85720414.md | SMF发起的QoS策略更新原理与信令流程 |
| 10 | 更新后的QoS策略下发与执行_86008546.md | QoS Flow新建/删除/修改的判断逻辑 |

**原始路径前缀**：
- 文件1-4：`output/UDG_Product_Documentation_CH_20.15.2/5G基础知识/一望5G/5G Core业务解决方案解读 -5G PCC策略之静态规则解读/`
- 文件5-10：`output/UDG_Product_Documentation_CH_20.15.2/5G基础知识/一望5G/5G Core业务解决方案解读：5G PCC策略之E2E QoS管理机制/5G PCC策略—E2E QoS管理机制/`

**文档类型**：5G基础知识概念文档（非特性指南、非MML命令、非业务专题），属于"其他文档"类型，以单md为原子单元。

**知识定位**：本文档为带宽控制场景提供底层原理支撑。PCC静态规则解释了"带宽控制策略如何定义和识别业务"，SM策略QoS管理机制解释了"带宽控制如何通过QoS Flow执行和动态更新"。两者共同构成带宽控制场景从策略定义到执行更新的完整知识链。
