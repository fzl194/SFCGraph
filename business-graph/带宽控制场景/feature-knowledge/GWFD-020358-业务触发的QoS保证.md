# GWFD-020358 业务触发的QoS保证 - 特性知识文档

> **场景归属**: 业务感知 → 带宽控制子场景（辅助特性：专用承载/QoS Flow保证）
> **产品**: UDG (UPF网元)
> **场景定位**: 业务识别 → 触发专用承载/QoS Flow创建 → 业务流绑定 → GBR带宽保证
> **辅助特性说明**: 通过专用承载间接提供带宽保证（GBR下限保证）

---

## 1. 特性概述

### 1.1 基本信息

| 项目 | 值 |
|------|-----|
| 特性ID | GWFD-020358 |
| 特性名称 | 业务触发的QoS保证 |
| 适用NF | PGW-U、UPF（UDG产品） |
| 首次发布版本 | UDG 20.2.0 |
| License控制项 | `82200AFP LKV3G5STQE01 业务触发的QoS保证` |
| 遵循标准 | 3GPP TS 23.401 |

### 1.2 核心能力

当用户请求了需要特定QoS保障的业务时，UDG根据PGW-C/SMF下发的PCC预定义规则为用户建立专有承载/专有QoS Flow。业务触发后，PGW-U/UPF基于匹配的预定义规则向PGW-C/SMF上报QoS事件，PGW-C/SMF基于QoS策略发起专有承载激活/专有QoS Flow建立流程。

### 1.3 在带宽控制场景中的定位

本特性是**辅助特性**，不直接执行限速或整形操作，而是通过以下路径间接实现带宽保证：

```
SA/ADC识别业务 → PGW-U/UPF上报QoS事件 → PGW-C/SMF发起专有承载创建
→ 业务流绑定到专有承载 → 专有承载携带GBR参数 → 实现带宽保证（下限保证）
```

专有承载/专有QoS Flow通过QoS属性（QOSPROP）携带GBR（Guaranteed Bit Rate）和MBR（Maximum Bit Rate）参数，由底层网络（空口、传输网）执行实际的带宽保证调度。

### 1.4 与BWM（GWFD-110311）的差异

| 对比维度 | 业务触发的QoS保证 (GWFD-020358) | 带宽管理BWM (GWFD-110311) |
|----------|--------------------------------|---------------------------|
| 带宽控制方式 | GBR保证（保证下限带宽） | 限速（限制上限带宽） |
| 执行位置 | 由网络底层（空口+传输）执行调度 | PGW-U/UPF本地执行速率限制 |
| 触发机制 | 业务识别 → 创建专有承载 | 策略匹配 → 直接限速 |
| 适用场景 | 需要保证最低带宽的实时业务（VoIP、视频） | 需要限制总带宽的资源控制 |
| 网络制式 | 2/3/4G（专有承载）+ 5G（QoS Flow） | 独立于网络制式 |

### 1.5 网络制式支持

同时支持2/3/4G和5G两种网络制式：

- **2/3/4G**: 创建专有承载（Dedicated Bearer），通过EPS承载机制实现QoS控制
- **5G**: 创建专有QoS Flow，通过PDU会话内的QoS Flow机制实现QoS控制

### 1.6 特性规格

| 规格名称 | 规格指标 |
|----------|----------|
| 每个用户支持的最大专有承载个数 | 10 |
| 每个用户支持的最大专有QoS Flow个数 | 63 |

### 1.7 特性依赖关系

| 依赖特性 | 控制项 | 交互说明 |
|----------|--------|----------|
| GWFD-110101 SA-Basic | 82209749 SA-Basic | UDG需要根据用户请求的业务判断是否建立专有承载/专有QoS Flow，需开启SA-Basic功能进行业务识别 |
| GWFD-020351 PCC基本功能 | 82209825 PCC基本功能 | UDG可以使用PCRF/PCF下发的QoS参数建立专有承载/专有QoS Flow，需开启基本PCC功能以从PCRF/PCF获取规则 |

### 1.8 应用限制

- 为避免7层业务触发专有承载/专有QoS Flow导致的信令风暴，**只有并发链路流小于8个的协议或协议组**才适合配置为基于流触发专有承载/专有QoS Flow建立。
- 本特性**只支持HTTP1.x协议**，不支持HTTP2.0协议。
- 本特性**不支持加密场景**基于host的计费和控制。
- 对于并发链路流大于8条的业务，**不适合基于流触发**专有承载/专有QoS Flow建立，建议使用**基于下行链路触发**模式。

---

## 2. 核心概念

### 2.1 缺省承载（Default Bearer）

UE附着或请求PDN连接时，会建立一个EPS承载，这个承载在PDN连接过程中不会被释放，以保证UE和PDN间的永久性IP连接，被称为缺省承载。缺省承载提供默认的QoS等级，通常为Non-GBR类型。

### 2.2 专有承载（Dedicated Bearer，适用于2/3/4G）

当UE连接到分组数据网PDN时，除缺省承载外，所有其他为该PDN连接建立的EPS承载均为专有承载。专有承载提供不同于缺省承载的QoS，从而实现业务传输的多样性，为不同的业务提供不同的QoS保障。

专有承载与缺省承载通过LBI（Linked EPS Bearer Identity）关联。一个PDN连接中，缺省承载只有一个，专有承载可以有多个（每个用户最多10个）。

### 2.3 QoS Flow（适用于5G）

QoS Flow是5G QoS控制的最小粒度，类似于4G中的EPS Bearer概念。一个PDU会话可能包含多个QoS Flow。每一个QoS Flow由QFI（QoS Flow ID）唯一识别。

与4G专有承载的对应关系：

| 4G概念 | 5G概念 | 说明 |
|--------|--------|------|
| 缺省承载 | 缺省QoS Flow | PDN连接/PDU会话建立时创建 |
| 专有承载 | 专有QoS Flow | 业务触发时动态创建 |
| EPS Bearer ID | QFI (QoS Flow ID) | 唯一标识 |
| TFT (Traffic Flow Template) | SDF Filter | 业务流过滤器 |
| PGW-C/PGW-U | SMF/UPF | 控制面/用户面网元 |

### 2.4 GBR与Non-GBR

- **GBR（Guaranteed Bit Rate，保证比特速率）**: 网络为该承载保证的最低比特速率。专有承载/QoS Flow通常是GBR类型，由QOSPROP中的GBRUPLKVALUE和GBRDNLKVALUE参数定义。
- **MBR（Maximum Bit Rate，最大比特速率）**: 承载允许的最高比特速率。由QOSPROP中的MBRUPLKVALUE和MBRDNLKVALUE参数定义。
- **Non-GBR**: 不保证最低比特速率的承载，缺省承载通常是Non-GBR类型。

### 2.5 5QI与QCI

- **QCI（QoS Class Identifier）**: 4G网络中标量值，用于标识QoS等级。每个QCI对应一组QoS参数（优先级、包延迟预算、丢包率等）。
- **5QI**: 5G网络中对应的QoS等级标识，功能类似QCI。

### 2.6 ARP（Allocation and Retention Priority）

分配与保持优先级，用于在资源受限时决定承载的建立、修改和保持优先级。包含以下子参数：
- 优先级级别（Priority Level）
- 抢占能力（Pre-emption Capability）
- 抢占脆弱性（Pre-emption Vulnerability）

### 2.7 TFT（Traffic Flow Template）

业务流模板，用于将业务数据流映射到对应的EPS承载。TFT包含上行和下行包过滤器，基于五元组（源IP、目的IP、源端口、目的端口、协议类型）过滤业务流。

### 2.8 PCC预定义规则

PCC模式预定义规则是本特性的核心机制：
- 预先在UDG上配置规则内容
- 规则名称由PGW-C/SMF下发给UDG
- UDG根据接收的规则名称，匹配本地配置的具体规则
- 根据匹配到的规则，对用户数据进行处理

规则来源：
- 部署PCRF/PCF时：预定义规则名称由PCRF/PCF和PGW-C/SMF一致定义并下发给UDG
- 未部署PCRF/PCF时：预定义规则名称由PGW-C/SMF定义并下发给UDG

### 2.9 业务触发机制

业务触发专用承载创建的完整机制链路：

1. **业务识别**：SA功能对业务报文进行内容解析。三四层解析获取五元组；七层解析获取URL等信息。
2. **规则匹配**：将解析得到的关键信息和PDR（Packet Detection Rule）进行比较，相符合即匹配成功。
3. **QoS上报**：当用户业务匹配到预定义规则且规则中绑定QoS-URR（Usage Reporting Rule）时，UDG触发QoS上报。
4. **承载创建**：PGW-C/SMF收到上报后，基于QoS策略发起专有承载/专有QoS Flow创建流程。

---

## 3. 实现原理与流程

### 3.1 总体查表流程

UDG支持基于匹配的预定义规则中配置的QoS类型URR进行上报，从而建立/更新/删除专有承载/专有QoS Flow。核心处理步骤：

1. **业务报文解析**：SA功能对业务报文进行特征分析
   - 三四层解析：获得五元组（源IP、目的IP、源端口、目的端口、协议类型）
   - 七层解析：获取URL等应用层信息
2. **规则匹配**：将解析结果与PDR比较，匹配所有PDR
3. **QoS上报触发**：当匹配到预定义规则且绑定QoS-URR时，触发QoS上报

### 3.2 七层触发的两种模式

七层业务触发专有承载/专有QoS Flow建立区分两种模式，每个协议或协议组可通过配置选择：

**模式一：基于流触发**
- 该7层业务的上行和下行链路都触发专有承载/专有QoS Flow建立
- 默认支持该模式的协议包括：GoogleTalk_Video、GoogleTalk_Audio、GoogleTalk_Stun、Skype_PctoPhone、Skype_PCtoPC、Skype_Sip、FTP、BBC_iPlayer_HTTP、BBC_iPlayer_Data、Quicktime_Streaming
- 适用于并发链路流小于8个的协议

**模式二：基于下行链路触发**
- 仅该7层业务的下行链路触发专有承载/专有QoS Flow建立
- 上行链路仍然保持在原有承载/QoS Flow运行
- 适用于并发链路流大于8条的业务

### 3.3 5G专有QoS Flow相关流程

#### 3.3.1 专有QoS Flow建立流程

专有QoS Flow建立由业务触发，当用户请求的业务数据流到达时，UPF将匹配到的QoS规则向SMF上报，SMF使用预定义规则中的QoS策略发起专有QoS Flow建立流程。

详细流程：

1. **（可选）预定义规则下发**：如果部署了动态PCC，PCF向SMF下发预定义规则；如果未部署动态PCC，则SMF在本地配置QoS策略规则。SMF通过PFCP Session Modification Request消息下发预定义规则名称，UPF匹配本地配置后返回PFCP Session Modification Response。
2. **业务匹配与QoS上报**：当有上行数据流到达时，UPF对报文进行规则匹配，当匹配到预定义规则且规则中绑定QoS-URR时，向SMF发送PFCP Session Report Request消息，携带Usage Report信元组（包含URR ID、Rule Information）。SMF处理上报事件后，向UPF下发PFCP Session Report Response（携带Update PDR、Update QER等信元组）。
3. **N4会话修改**：SMF向UPF发送PFCP Session Modification Request，携带QoS Flow Identifier、QER ID、Gate Status等信元，提供数据监测、报告规则和CN隧道信息。
4. **N1N2消息传递**：SMF向AMF发送Namf_Communication_N1N2MessageTransfer消息，携带N2 SM Information（包含QFI、QoS Profile、CN Tunnel Info）和N1 SM Container（包含PDU Session Establishment Accept、Allocated IPv4 Address）。
5. **(R)AN资源建立**：AMF向(R)AN发送PDU Session Resource Setup Request。(R)AN与UE进行信令交互，转发N1 SM Container，请求UE建立专有QoS Flow。
6. **(R)AN响应**：(R)AN向AMF发送PDU Session Resource Setup Response，建立AN隧道信息（AN Tunnel Info、List of Accepted/Rejected QFI）。
7. **N4会话更新**：AMF通过Nsmf_PDUSession_UpdateSMContext Request转发N2 SM Information给SMF。SMF向UPF发送PFCP Session Modification Request，将AN隧道信息和转发规则发送给UPF。
8. **完成**：SMF向AMF发送Nsmf_PDUSession_UpdateSMContext Response。

**IPv4v6双栈特殊处理**：当配置AnytoAny的Filter规则创建专有承载时，UPF向SMF发送专有承载消息需要使用SET UPGLBPMPARA命令中FLOWDANYIPFMT配置具体的Flow-Description信息格式，以便SMF区分上报消息是IPv4还是IPv6。

#### 3.3.2 专有QoS Flow更新流程

当QoS参数变更时，UPF向SMF上报QoS更新事件，触发专有QoS Flow更新。

关键步骤：
1. UPF检测到业务匹配预定义规则且绑定QoS-URR，向SMF发送PFCP Session Report Request
2. SMF通过Namf_Communication_N1N2MessageTransfer通知AMF更新QoS信息
3. AMF向(R)AN发送PDU Session Resource Modify Request
4. (R)AN与UE交互，将PDU Session Modification Command转发给UE
5. UE确认后，(R)AN向AMF响应，SMF通过PFCP Session Modification更新N4会话
6. UE发送PDU Session Modification Complete确认接受

#### 3.3.3 专有QoS Flow释放流程

当业务暂停一段时间、业务流老化时，或业务暂停时间超过专有QoS创建时SMF下发给UPF的Deactivation Timer时，触发释放流程。

关键步骤：
1. UPF检测到业务老化，向SMF发送PFCP Session Report Request（携带URR ID、Rule Information）
2. SMF处理上报事件，通知UPF删除PDR、QER、URR等信息
3. SMF释放专有QoS Flow分配的用户面资源（PFCP Session Deletion）
4. SMF通过Namf_Communication_N1N2MessageTransfer通知AMF释放资源
5. (R)AN与UE交互释放AN资源
6. UE发送PDU Session Release Ack确认释放
7. 如果部署了动态PCC，SMF向PCF发起SM Policy Association Termination流程

**迟滞时间机制**：为减少专有QoS Flow的频繁创建和删除，可通过SET QOSURRRPTCTRL命令设置迟滞时间。业务流老化时，UPF延迟向SMF发送申请删除专有QoS Flow的消息。

### 3.4 2/3/4G专有承载相关流程

#### 3.4.1 专有承载激活流程

专有承载的激活由业务触发，当用户请求的业务数据流到达时，PGW-U将匹配到的QoS规则向PGW-C上报。

详细流程：

1. **（可选）预定义规则下发**：PCRF向PGW-C下发预定义规则（动态PCC）或PGW-C在本地配置QoS策略规则。PGW-C通过PFCP Session Modification Request消息下发预定义规则名称给PGW-U。
2. **业务匹配与QoS上报**：当有上行数据流到达时，PGW-U对报文进行规则匹配，匹配到预定义规则且绑定QoS-URR时，向PGW-C发送PFCP Session Report Request消息（携带URR ID、Rule Information）。PGW-C处理上报事件，触发专有承载创建。
3. **Create Bearer Request**：PGW-C向SGW-C发送Create Bearer Request消息，包含：IMSI、PTI、EPS Bearer QoS、TFT、S5/S8 TEID、Charging Id、**LBI（Linked EPS Bearer Identity）**。SGW-C根据LBI关联缺省承载和专有承载。
4. **SGW-C向MME转发**：SGW-C建立专有承载上下文后，向MME发送Create Bearer Request。
5. **MME向eNodeB发送Bearer Setup Request**：包含EPS Bearer Identity、EPS Bearer QoS、Session Management Request（含PTI、TFT、EPS Bearer QoS parameters excluding ARP、Protocol Configuration Options、EPS Bearer Identity、LBI）、S1-TEID。
6. **无线承载建立**：eNodeB将EPS Bearer QoS映射为Radio Bearer QoS，向UE发送RRC Connection Reconfiguration消息（含Radio Bearer QoS、Session Management Request、EPS RB Identity）。UE通过LBI关联专有承载和缺省承载。
7. **UE确认**：UE向eNodeB响应RRC Connection Reconfiguration Complete消息。
8. **eNodeB向MME响应**：eNodeB发送Bearer Setup Response（含EPS Bearer Identity、S1-TEID）。
9. **UE NAS层响应**：UE通过Direct Transfer消息发送Session Management Response（含EPS Bearer Identity）。
10. **MME确认**：MME收到Bearer Setup Response和Session Management Response后，向SGW-C响应Create Bearer Response（含EPS Bearer Identity、S1-TEID）。SGW-U建立和eNodeB间的S1-U专有承载。
11. **SGW-C向PGW-C响应**：SGW-C发送Create Bearer Response（含EPS Bearer Identity、S5/S8-TEID）。PGW-C保存S5/S8-TEID，建立专有承载。
12. **PGW-C将承载信息传递给PGW-U**。

#### 3.4.2 专有承载更新流程

当QoS参数变更时，PGW-U向PGW-C上报QoS更新事件。

关键步骤：
1. PGW-U匹配预定义规则后向PGW-C上报PFCP Session Report Request
2. PGW-C生成TFT并更新EPS Bearer QoS，向SGW-C发送Update Bearer Request（EPS Bearer Identity、EPS Bearer QoS、APN-AMBR、TFT）
3. 经SGW-C→MME→eNodeB→UE的传递链路
4. eNodeB将修改的EPS Bearer QoS映射为Radio Bearer QoS
5. UE确认无线承载更改
6. 经eNodeB→MME→SGW-C→PGW-C的响应链路
7. PGW-C通过PFCP Session Modification Request将更新信息传递给PGW-U

#### 3.4.3 专有承载去激活流程

当业务暂停一段时间、业务流老化时，PGW-U向PGW-C上报QoS事件发起承载去激活。

关键步骤：
1. PGW-U检测业务流老化，向PGW-C发送PFCP Session Report Request
2. PGW-C决定发起承载去活，向SGW-C发送Delete Bearer Request（EPS Bearer Identity）
3. SGW-C向SGW-U发送PFCP Session Modification Request释放承载上下文
4. SGW-C向MME发送Delete Bearer Request
5. MME向eNodeB发送E-Rab Release Command（含NAS消息Deactivate EPS Bearer Context Request）
6. eNodeB向UE发送Radio Bearer Release Request
7. UE释放无线承载后确认
8. 经eNodeB→MME→SGW-C→PGW-C的Delete Bearer Response响应链路
9. PGW-C向PGW-U发送PFCP Session Deletion Request释放承载信息

### 3.5 三四层触发（L34）vs 七层触发（L7）

| 对比维度 | 三四层触发（L34） | 七层触发（L7） |
|----------|------------------|----------------|
| 报文解析 | 三四层信息（五元组） | 七层信息（URL等） |
| 匹配过滤器 | ADD FILTER（L34过滤器） | ADD L7FILTER（七层过滤器） + ADD FILTER（L34过滤器） |
| 流过滤器绑定 | ADD FLTBINDFLOWF（仅L34） | ADD FLTBINDFLOWF + ADD PROTBINDFLOWF（L34+L7） |
| 专有承载配置 | 无需ADD SADEDICBEARER | 需ADD SADEDICBEARER配置触发模式 |
| 信令开销 | 较低 | 较高（需7层深度解析） |
| 适用场景 | 基于IP/端口的业务区分 | 基于应用层协议的精确识别 |
| REFRESHSRV | 需要执行 | 需要执行 |

---

## 4. 配置规则

### 4.1 涉及的MML命令总览

本特性涉及的MML命令共16条，分为以下几类：

**License管理（1条）**：
| 命令 | 用途 |
|------|------|
| SET LICENSESWITCH | 打开本特性的License配置开关 |

**业务过滤器管理（6条）**：
| 命令 | 用途 |
|------|------|
| ADD FILTER | 配置三四层过滤条件 |
| ADD L7FILTER | 配置七层过滤条件 |
| ADD FLOWFILTER | 配置流过滤器 |
| ADD FLTBINDFLOWF | 配置流过滤器与三四层过滤器的绑定关系 |
| ADD PROTBINDFLOWF | 配置流过滤器与七层协议的绑定关系 |
| ADD WELLKNOWNPORT | 配置知名端口（协议识别） |

**业务刷新（1条）**：
| 命令 | 用途 |
|------|------|
| SET REFRESHSRV | 将新配置的Filter置为生效 |

**QoS控制与PCC策略（5条）**：
| 命令 | 用途 |
|------|------|
| ADD URR | 配置QoS类型URR（USAGERPTMODE=QOS） |
| ADD URRGROUP | 配置URR组 |
| ADD QOSPROP | 配置QoS属性（含GBR/MBR参数） |
| ADD PCCPOLICYGRP | 配置PCC策略组（绑定QoS属性和URR组） |
| ADD SADEDICBEARER | 使能协议或协议组支持基于业务感知能力触发专有承载创建 |

**业务规则管理（3条）**：
| 命令 | 用途 |
|------|------|
| ADD RULE | 配置业务规则（绑定流过滤器和PCC策略组） |
| ADD USERPROFILE | 创建用户模板 |
| ADD RULEBINDING | 将Rule绑定到UserProfile |

**全局参数配置（2条）**：
| 命令 | 用途 |
|------|------|
| SET UPGLBPMPARA | 配置UPF上报Flow-Description信息的格式（IPv4v6双栈） |
| SET QOSURRRPTCTRL | 设置QoS URR上报的迟滞时间参数（减少专有承载频繁创建删除） |

**软参（1条）**：
| 软参 | 用途 |
|------|------|
| BIT1104 | 控制L34业务触发QoS Flow创建时，PFCP Session Report Request消息中的Flow Information信元的获取方式 |

### 4.2 配置顺序

#### 4.2.1 三四层配置顺序

```
1. SET LICENSESWITCH          → 打开License开关
2. ADD FILTER                 → 配置三四层过滤条件
3. ADD FLOWFILTER             → 配置流过滤器
4. ADD FLTBINDFLOWF           → 绑定流过滤器与三四层过滤器
5. SET REFRESHSRV             → 刷新使Filter生效
6. ADD URR (USAGERPTMODE=QOS) → 配置QoS类型URR
7. ADD QOSPROP                → 配置QoS属性（GBR/MBR）
8. ADD PCCPOLICYGRP           → 配置PCC策略组
9. ADD RULE                   → 配置业务规则
10. ADD USERPROFILE           → 创建用户模板
11. ADD RULEBINDING           → 绑定Rule到UserProfile
12. SET UPGLBPMPARA           → 配置Flow-Description格式
13.（可选）BIT1104             → 配置软参
```

#### 4.2.2 七层配置顺序

```
1. SET LICENSESWITCH          → 打开License开关
2. ADD FILTER                 → 配置三四层过滤条件
3. ADD L7FILTER               → 配置七层过滤条件
4. ADD FLOWFILTER             → 配置流过滤器
5. ADD FLTBINDFLOWF           → 绑定流过滤器与三四层过滤器
6. ADD PROTBINDFLOWF          → 绑定流过滤器与七层协议
7. SET REFRESHSRV             → 刷新使Filter生效
8. ADD URR (USAGERPTMODE=QOS) → 配置QoS类型URR
9. ADD QOSPROP                → 配置QoS属性（GBR/MBR）
10. ADD PCCPOLICYGRP          → 配置PCC策略组
11. ADD WELLKNOWNPORT         → 配置协议知名端口
12. ADD SADEDICBEARER         → 使能协议触发专有承载创建
13. ADD RULE                  → 配置业务规则
14. ADD USERPROFILE           → 创建用户模板
15. ADD RULEBINDING           → 绑定Rule到UserProfile
16. SET UPGLBPMPARA           → 配置Flow-Description格式
```

### 4.3 关键参数说明

#### 4.3.1 ADD URR（QoS类型URR）

| 参数名 | 说明 | 本特性取值 |
|--------|------|------------|
| URRNAME | 使用量上报规则名称 | 自定义（如urr_1） |
| URRID | URR标识 | 自定义数字（如1001） |
| USAGERPTMODE | 使用量上报模式 | **QOS**（固定取值，标识为QoS事件上报） |

#### 4.3.2 ADD QOSPROP（QoS属性 - 带宽保证核心参数）

| 参数名 | 说明 | 示例值 | 带宽控制含义 |
|--------|------|--------|--------------|
| QOSPROPNAME | QoS属性名称 | qos-property1 | - |
| QOSURRNAME | QoS使用量上报规则名称 | urr_1 | 关联QoS类型URR |
| GBRUPLKVALUE | 保证的上行比特率 | 110 | GBR上行保证（kbps） |
| GBRDNLKVALUE | 保证的下行比特率 | 110 | GBR下行保证（kbps） |
| MBRUPLKVALUE | 最大上行比特率 | 220 | MBR上行限制（kbps） |
| MBRDNLKVALUE | 最大下行比特率 | 220 | MBR下行限制（kbps） |

#### 4.3.3 ADD SADEDICBEARER（业务感知专有承载配置）

| 参数名 | 说明 | 取值 |
|--------|------|------|
| PROTOCOLLEVEL | 协议等级 | PROTOCOL（协议级）/ PROTOCOLGROUP（协议组级） |
| PROTOCOLNAME | 协议名称 | 如http |
| TRIGGERMODE | 触发专有承载模式 | DOWNLINK_ONLY（基于下行链路触发）/ FLOW_BASED（基于流触发） |

### 4.4 配置约束

1. **REFRESHSRV必须在过滤器配置完成后执行**，否则新配置的Filter不生效。
2. **USAGERPTMODE必须为QOS**，表示该URR用于QoS事件上报。
3. **ADD RULE的POLICYTYPE必须为PCC**，FILTERINGMODE通常为FLOWFILTER（也支持FLOWFILTERGRP）。
4. **七层触发必须配置ADD SADEDICBEARER**，三四层触发无需此命令。
5. **并发链路流大于8条的协议应使用DOWNLINK_ONLY模式**，避免信令风暴。
6. **SET UPGLBPMPARA的FLOWDANYFMT参数**用于IPv4v6双栈场景，配置Flow-Description信息格式。
7. **SET QOSURRRPTCTRL设置的迟滞时间**用于减少专有承载/QoS Flow的频繁创建和删除。

---

## 5. 配置案例

### 5.1 案例一：三四层业务触发专有承载创建

**场景**：基于三四层信息（五元组）识别业务，触发专有承载创建，为业务提供GBR=110kbps、MBR=220kbps的QoS保证。

```mml
// 步骤1：打开License开关
SET LICENSESWITCH:LICITEM="LKV3G5STQE01",SWITCH=ENABLE;

// 步骤2：配置三四层过滤条件
ADD FILTER:FILTERNAME="filter_test",L34PROTTYPE=STRING,L34PROTOCOL=ANY;

// 步骤3：配置流过滤器
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_test1",TETHERDETFLAG=DETECT_ONLY;

// 步骤4：绑定流过滤器与三四层过滤器
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test1",FILTERNAME="filter_test";

// 步骤5：刷新使Filter生效
SET REFRESHSRV:REFRESHTYPE=USERPROFILE;

// 步骤6：配置QoS类型URR
ADD URR:URRNAME="urr_1",URRID=1001,USAGERPTMODE=QOS;

// 步骤7：配置QoS属性（GBR=110, MBR=220）
ADD QOSPROP:QOSPROPNAME="qos-property1",QOSURRNAME="urr_1",
  GBRUPLKVALUE=110,GBRDNLKVALUE=110,
  MBRUPLKVALUE=220,MBRDNLKVALUE=220;

// 步骤8：配置PCC策略组
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="ppg1",
  URRGROUPNAME="urrgroup1",QOSPROPNAME="qos-property1";

// 步骤9：配置业务规则
ADD RULE:RULENAME="rule_test",POLICYTYPE=PCC,
  FILTERINGMODE=FLOWFILTER,
  FLOWFILTERNAME="flowfilter_test1",
  POLICYNAME="ppg1",PRIORITY=10;

// 步骤10：配置用户模板
ADD USERPROFILE:USERPROFILENAME="up_test";

// 步骤11：绑定Rule到UserProfile
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";

// 步骤12：配置Flow-Description信息格式（IPv4v6双栈）
SET UPGLBPMPARA:FLOWDANYFMT=AnyFMT;
```

**注意**：ADD FLOWFILTER中使用了TETHERDETFLAG=DETECT_ONLY参数（Tethering检测标识），用于指定Tethering检测行为。

### 5.2 案例二：七层业务触发专有承载创建

**场景**：基于七层信息识别HTTP协议业务（URL: www.example.com），触发专有承载创建，触发模式为DOWNLINK_ONLY（基于下行链路触发），为业务提供GBR=110kbps、MBR=220kbps的QoS保证。

```mml
// 步骤1：打开License开关
SET LICENSESWITCH:LICITEM="LKV3G5STQE01",SWITCH=ENABLE;

// 步骤2：配置三四层过滤条件
ADD FILTER:FILTERNAME="filter_test",L34PROTTYPE=STRING,L34PROTOCOL=ANY;

// 步骤3：配置七层过滤条件
ADD L7FILTER:L7FILTERNAME="l7_test",
  SUBL7FLTNAME="subl7_test",
  URL="www.example.com*/*";

// 步骤4：配置流过滤器
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_test1";

// 步骤5：绑定流过滤器与三四层过滤器
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test1",FILTERNAME="filter_test";

// 步骤6：绑定流过滤器与七层协议
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilter_test1",
  PROTOCOLNAME="http",L7FILTERNAME="l7_test";

// 步骤7：刷新使Filter生效
SET REFRESHSRV:REFRESHTYPE=USERPROFILE;

// 步骤8：配置QoS类型URR
ADD URR:URRNAME="urr_1",URRID=1001,USAGERPTMODE=QOS;

// 步骤9：配置QoS属性（GBR=110, MBR=220）
ADD QOSPROP:QOSPROPNAME="qos-property1",QOSURRNAME="urr_1",
  GBRUPLKVALUE=110,GBRDNLKVALUE=110,
  MBRUPLKVALUE=220,MBRDNLKVALUE=220;

// 步骤10：配置PCC策略组
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="ppg1",
  URRGROUPNAME="urrgroup1",QOSPROPNAME="qos-property1";

// 步骤11：配置协议知名端口（HTTP默认端口80）
ADD WELLKNOWNPORT:IDENPROTNAME="http",
  PROTOCOLNAME="http",
  PORTOP=EQUAL,STARTPORT=80,PRIORITY=5;

// 步骤12：使能HTTP协议支持基于业务感知能力触发专有承载创建
ADD SADEDICBEARER:PROTOCOLLEVEL=PROTOCOL,
  PROTOCOLNAME="http",
  TRIGGERMODE=DOWNLINK_ONLY;

// 步骤13：配置业务规则
ADD RULE:RULENAME="rule_test",POLICYTYPE=PCC,
  FILTERINGMODE=FLOWFILTER,
  FLOWFILTERNAME="flowfilter_test1",
  POLICYNAME="ppg1",PRIORITY=10;

// 步骤14：配置用户模板
ADD USERPROFILE:USERPROFILENAME="up_test";

// 步骤15：绑定Rule到UserProfile
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";

// 步骤16：配置Flow-Description信息格式
SET UPGLBPMPARA:FLOWDANYFMT=AnyFMT;
```

### 5.3 案例三：基于协议或协议组的专有承载创建

**场景**：在案例二基础上，重点验证基于协议的专有承载创建功能。使能HTTP协议支持基于业务感知能力触发专有承载创建，配置为DOWNLINK_ONLY模式。用户进行HTTP业务时，UDG创建"rule-filter-type"字段为"l7-downlink"的模板，将所有用户下行HTTP报文汇聚到特定专有承载。

**配置核心命令**（前置配置同案例二）：

```mml
// 使能HTTP协议支持基于业务感知能力触发专有承载创建
// 触发模式为DOWNLINK_ONLY（基于下行链路触发）
ADD SADEDICBEARER:PROTOCOLLEVEL=PROTOCOL,
  PROTOCOLNAME="http",
  TRIGGERMODE=DOWNLINK_ONLY;
```

**验证效果**：
- 当用户进行HTTP业务时，PGW-U/UPF立即向PGW-C/SMF发送PFCP Session Report Request消息
- 消息中Usage Report信元组包含QoS类型的URR ID
- Usage Report Trigger为start
- rule-filter-type字段为l7-downlink（下行链路模式标识）
- 基于该协议的所有用户下行报文汇聚到特定专有承载
- 上行报文仍使用原专有承载

**对比：如果不配置ADD SADEDICBEARER**：
- 用户进行HTTP业务时，不会触发创建专有承载流程
- 即基于协议或协议组的专有承载创建功能不使能时，即使匹配到了业务规则，也不会通过协议级触发创建专有承载

---

## 6. 验证与调测

### 6.1 验证License状态

```mml
LST LICENSESWITCH:LICITEM="LKV3G5STQE01";
```

预期结果：SWITCH字段为ENABLE。如果为DISABLE，执行：
```mml
SET LICENSESWITCH:LICITEM="LKV3G5STQE01",SWITCH=ENABLE;
```

### 6.2 专用承载/QoS Flow状态查询

通过用户IMSI查询建立专有承载/专有QoS Flow和使用的APN：

```mml
DSP SESSIONINFO:QUERYTYPE=IMSI,IMSI="460000123456789";
```

### 6.3 配置数据验证

#### 6.3.1 验证UserProfile和Rule绑定

```mml
LST RULEBINDING:USERPROFILENAME="up_test";
```

预期输出：
```
用户模板名称  =  up_test
    规则名称  =  rule_test
      优先级  =  10
    策略类型  =  PCC
```

#### 6.3.2 验证Rule配置

```mml
LST RULE:RULENAME="rule_test";
```

关键验证项：流过滤器名称（flowfilter_test1）、PCC策略组名称（ppg1）、策略类型（PCC）。

#### 6.3.3 验证PCC策略组和QoS属性

```mml
LST PCCPOLICYGRP:PCCPOLICYGRPNM="ppg1";
LST URR:URRNAME="urr_1";
LST QOSPROP:QOSPROPNAME="qos-property1";
```

PCC策略组预期：Qos属性名称=qos-property1，URR组名称=urrgroup1。
QoS属性预期：保证的上行/下行比特率=110，最大上行/下行比特率=220，QoS使用量上报规则名称=urr_1。
URR预期：使用量上报模式=QOS。

#### 6.3.4 验证过滤器配置（三四层）

```mml
LST FLOWFILTER:FLOWFILTERNAME="flowfilter_test1";
LST FILTER:FILTERNAME="filter_test";
```

#### 6.3.5 验证过滤器配置（七层）

```mml
LST FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test1";
LST PROTBINDFLOWF:FLOWFILTERNAME="flowfilter_test1";
LST L7FILTER:L7FILTERNAME="l7_test";
```

#### 6.3.6 验证专有承载配置

```mml
LST SADEDICBEARER:;
```

预期输出：
```
协议等级  =  Protocol
协议名称  =  http
触发专有承载模式 =  DOWNLINK_ONLY
```

### 6.4 业务触发验证

**验证方法**：在OM Portal上创建UDG N4接口跟踪任务。

**验证步骤**：
1. 测试终端使用规划的APN接入网络
2. 测试终端正常访问网页（如www.huawei.com），确认基本业务连通
3. 使用测试终端访问能触发专有承载/专有QoS Flow创建或更新的业务
4. 查看PGW-U/UPF是否立即向PGW-C/SMF发送**PFCP Session Report Request**消息

**关键验证点**：
- Usage Report信元组中包含**QoS类型的URR ID**
- Usage Report Trigger为**start**
- 查看PGW-C/SMF返回的**PFCP Session Report Response**消息中，Create PDR信元组携带的URR ID与Request中的URR ID**一致**

**下行链路模式验证**：
- 查看PFCP Session Report Request消息中**rule-filter-type**字段是否为**l7-downlink**
- 如果为l7-downlink，说明基于协议或协议组的专有承载创建的模式是下行链路模式，调测通过

### 6.5 常见问题排查

#### 问题1：专有承载/QoS Flow创建失败

**排查路径**：
1. 检查License开关是否打开（LST LICENSESWITCH）
2. 检查UserProfile绑定的Rule是否正确（LST RULEBINDING）
3. 检查Rule配置是否正确（LST RULE）
4. 检查PCC策略组、URR、QoS属性是否正确（LST PCCPOLICYGRP / LST URR / LST QOSPROP）
5. 检查过滤器配置是否正确（LST FILTER / LST FLTBINDFLOWF / LST PROTBINDFLOWF / LST L7FILTER）
6. 确认是否执行了SET REFRESHSRV刷新

#### 问题2：业务流未绑定到专有承载

**排查路径**：
1. 检查DSP SESSIONINFO确认用户的APN是否正确
2. 检查ADD SADEDICBEARER中TRIGGERMODE是否配置正确
3. 确认rule-filter-type字段值是否符合预期

#### 问题3：七层触发未生效

**排查路径**：
1. 检查ADD SADEDICBEARER是否配置（七层触发必须有此配置）
2. 检查ADD SADEDICBEARER中PROTOCOLNAME是否与ADD PROTBINDFLOWF中的PROTOCOLNAME一致
3. 检查并发链路流是否大于8条（大于8条应使用DOWNLINK_ONLY模式）
4. 确认是否为HTTP2.0协议（本特性不支持HTTP2.0）
5. 确认是否为加密场景（不支持加密场景基于host的计费和控制）

#### 问题4：专有承载频繁创建和删除

**排查路径**：
1. 检查是否配置了SET QOSURRRPTCTRL设置迟滞时间
2. 业务流老化时间是否设置过短
3. 检查Deactivation Timer配置

### 6.6 故障信息收集

如需寻求技术支持，收集以下信息：
1. OM Portal上的用户跟踪任务报文
2. 导出当前MML配置：`EXP MML`
3. 所有LST查询结果
4. DSP SESSIONINFO查询结果

---

## 7. 参考信息

### 7.1 3GPP标准

| 标准类别 | 标准编号 | 标准名称 |
|----------|----------|----------|
| 3GPP | TS 23.401 | General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access |

### 7.2 涉及网元与接口

| 网元 | 角色 | 接口 |
|------|------|------|
| PCRF/PCF | 策略决策，提供基于业务的QoS策略、计费规则 | Gx（4G）/ N7（5G） |
| PGW-C/SMF | 承载绑定控制、策略规则授权、通过Sx/N4接口下发URR信元 | Sx（4G）/ N4（5G） |
| PGW-U/UPF | 业务数据流检测、QoS执行、上报QoS事件 | Sx/N4 |
| SGW-C/SGW-U (4G) | 服务网关，转发承载建立/更新/删除信令 | S5/S8, S11 |
| MME (4G) | 移动性管理，处理承载相关NAS信令 | S11, S1-MME |
| AMF (5G) | 接入和移动性管理，转发N1/N2消息 | N11 (与SMF) |
| (R)AN (5G) | 无线接入网，建立无线承载 | N2, Uu |
| eNodeB (4G) | 演进型NodeB，建立无线承载 | S1, Uu |

### 7.3 关键信元说明

**PFCP接口信元**：

| 信元名称 | 所在消息 | 说明 |
|----------|----------|------|
| Usage Report | PFCP Session Report Request/Response | 使用量报告，包含URR ID和Rule Information |
| URR ID | Usage Report内 | 标识上报的QoS类型URR |
| Rule Information | Usage Report内 | 匹配到的规则信息 |
| Create PDR | PFCP Session Report Response | 创建报文检测规则 |
| Update PDR | PFCP Session Report Response | 更新报文检测规则 |
| Create QER | PFCP Session Report Response | 创建QoS执行规则 |
| Update QER | PFCP Session Report Response | 更新QoS执行规则 |
| QoS Flow Identifier | PFCP Session Modification Request | 5G QoS Flow标识 |
| QER ID | PFCP Session Modification Request | QoS执行规则标识 |
| Gate Status | PFCP Session Modification Request | 门控状态 |
| Session Endpoint Identifier | PFCP Session | 会话端点标识 |

**4G承载相关信元**：

| 信元名称 | 说明 |
|----------|------|
| EPS Bearer Identity | EPS承载标识 |
| LBI (Linked EPS Bearer Identity) | 关联缺省承载标识 |
| EPS Bearer QoS | EPS承载QoS参数（含QCI、GBR、MBR、ARP） |
| TFT | 业务流模板（上下行包过滤器） |
| PTI (Procedure Transaction Identity) | 过程事务标识 |
| S1-TEID | S1接口隧道端点标识 |
| S5/S8-TEID | S5/S8接口隧道端点标识 |

**5G QoS Flow相关信元**：

| 信元名称 | 说明 |
|----------|------|
| QFI (QoS Flow Identifier) | QoS Flow唯一标识 |
| QoS Profile | QoS配置文件 |
| CN Tunnel Info | 核心网隧道信息 |
| AN Tunnel Info | 接入网隧道信息 |
| N1 SM Container | N1会话管理容器 |
| N2 SM Information | N2会话管理信息 |
| PDU Session ID | PDU会话标识 |

### 7.4 特性交互

| 交互类型 | 相关特性 | 交互说明 |
|----------|----------|----------|
| 依赖 | GWFD-110101 SA-Basic | 需开启SA-Basic功能进行业务识别（三四层五元组解析、七层URL解析） |
| 依赖 | GWFD-020351 PCC基本功能 | 需开启基本PCC功能以从PCRF/PCF获取QoS规则 |

### 7.5 对系统的影响

- 需要打开业务感知功能，对用户报文进行匹配比较，**对系统转发性能有影响**。
- UDG需要主动触发专有承载/专有QoS Flow建立，**会增加信令消息的处理开销**。
- 由于开销增加，**将导致CPU占用率相应上升**。

### 7.6 软参说明

| 软参名称 | 说明 |
|----------|------|
| BIT1104 | 控制L34业务触发QoS Flow创建时，PFCP Session Report Request消息中的Flow Information信元的获取方式 |

### 7.7 计费与话单

本特性不涉及计费与话单。

---

## 8. 知识来源

### 8.1 源文档清单

| 序号 | 文档名称 | 原始路径（相对output/） |
|------|----------|------------------------|
| 1 | GWFD-020358 业务触发的QoS保证特性概述_80966039.md | UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/ |
| 2 | 参考信息_92206303.md | 同上目录 |
| 3 | 专有QoS Flow相关流程（适用于5G）_10779227.md | 同上目录/实现原理/ |
| 4 | 专有承载相关流程（适用于2_3_4G）_81656835.md | 同上目录/实现原理/ |
| 5 | 实现原理_81656834.md | 同上目录 |
| 6 | 配置七层业务触发的QOS保证（PGW-U、UPF）_80361858.md | 同上目录/激活业务触发的QoS保证/ |
| 7 | 配置三四层业务触发的QoS保证（PGW-U、UPF）_80318438.md | 同上目录/激活业务触发的QoS保证/ |
| 8 | QoS Flow_11153135.md | 同上目录/相关术语/ |
| 9 | 专有承载_84864577.md | 同上目录/相关术语/ |
| 10 | 缺省承载_84864576.md | 同上目录/相关术语/ |
| 11 | 调测七层业务触发的QoS保证_10883660.md | 同上目录/调测业务触发的QoS保证/ |
| 12 | 调测三四层业务触发的QoS保证_10507253.md | 同上目录/调测业务触发的QoS保证/ |
| 13 | 调测基于协议或协议组的专有承载创建功能_10883659.md | 同上目录/调测业务触发的QoS保证/ |

### 8.2 关键MML命令覆盖情况

本特性涉及的16条核心MML命令及2条辅助命令：

| 分类 | 命令 | 用途 | 覆盖状态 |
|------|------|------|----------|
| License | SET LICENSESWITCH | License开关 | 已覆盖 |
| 过滤器 | ADD FILTER | L34过滤器 | 已覆盖 |
| 过滤器 | ADD L7FILTER | L7过滤器 | 已覆盖 |
| 过滤器 | ADD FLOWFILTER | 流过滤器 | 已覆盖 |
| 过滤器 | ADD FLTBINDFLOWF | 流过滤器绑定L34 | 已覆盖 |
| 过滤器 | ADD PROTBINDFLOWF | 流过滤器绑定L7协议 | 已覆盖 |
| 过滤器 | ADD WELLKNOWNPORT | 知名端口 | 已覆盖 |
| 刷新 | SET REFRESHSRV | 刷新使生效 | 已覆盖 |
| QoS | ADD URR | QoS类型URR | 已覆盖 |
| QoS | ADD URRGROUP | URR组 | 已覆盖 |
| QoS | ADD QOSPROP | QoS属性（GBR/MBR） | 已覆盖 |
| PCC | ADD PCCPOLICYGRP | PCC策略组 | 已覆盖 |
| 专有承载 | ADD SADEDICBEARER | 业务感知专有承载 | 已覆盖 |
| 规则 | ADD RULE | 业务规则 | 已覆盖 |
| 规则 | ADD USERPROFILE | 用户模板 | 已覆盖 |
| 规则 | ADD RULEBINDING | 规则绑定 | 已覆盖 |
| 全局参数 | SET UPGLBPMPARA | Flow-Description格式 | 已覆盖 |
| 全局参数 | SET QOSURRRPTCTRL | 迟滞时间控制 | 已覆盖 |
