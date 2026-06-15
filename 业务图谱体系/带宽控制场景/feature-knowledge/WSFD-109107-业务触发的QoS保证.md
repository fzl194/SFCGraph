# WSFD-109107 业务触发的QoS保证 - 特性知识文档

> **场景归属**: 业务感知 → 带宽控制子场景（辅助特性：专用承载/QoS Flow保证，UNC侧）
> **产品**: UNC (SMF网元)
> **场景定位**: SMF接收业务触发 → 下发PCC规则 → 创建专用承载/QoS Flow → GBR保证
> **对应UDG特性**: GWFD-020358 业务触发的QoS保证

---

## 1. 特性概述

### 1.1 基本信息

| 属性 | 值 |
|------|-----|
| 特性ID | WSFD-109107 |
| 特性名称 | 业务触发的QoS保证 |
| 产品 | UNC |
| 适用网元 | GGSN-C / PGW-C / SMF（控制面），配合 PGW-U / UPF（用户面） |
| 首发版本 | UNC 20.5.0 |
| License控制项 | 82208819 / LKV3W9STQE11 / 业务触发的QoS保证 |

### 1.2 核心能力

业务触发的QoS保证是指：当用户请求了需要特定QoS保障的业务时，PGW-U/UPF根据UNC下发的PCC预定义规则，为用户建立专有承载（2/3/4G）或专有QoS Flow（5G）的功能。专有承载/专有QoS Flow创建成功后，用户即可在特定的QoS保证（如GBR保证带宽下限）下进行请求的数据业务。

### 1.3 在带宽控制场景中的定位

在业务感知-带宽控制子场景中，本特性属于**GBR保证路径**的UNC侧（控制面）实现：

- **UDG侧（GWFD-020358）**：UPF执行业务识别，匹配预定义规则后，向SMF上报QoS事件，并在用户面创建专有承载/QoS Flow的数据通道。
- **UNC侧（WSFD-109107）**：SMF接收UPF的QoS事件上报，基于本地或PCF下发的QoS策略，发起专有承载/QoS Flow的信令流程，通过N4/S11/S5接口下发规则和QoS参数。

### 1.4 与GWFD-020358（UDG侧）的对应关系

| 维度 | UNC侧 (WSFD-109107) | UDG侧 (GWFD-020358) |
|------|---------------------|---------------------|
| 网元 | SMF / PGW-C | UPF / PGW-U |
| 接口角色 | N4接口控制方 | N4接口执行方 |
| 核心动作 | 接收QoS事件上报 → 发起承载/QoS Flow建立信令 | 业务识别 → 上报QoS事件 → 执行QoS策略 |
| 配置重点 | URR/QoSProp/PCC策略组/规则绑定 | 业务过滤规则/预定义规则匹配 |
| 规则名称一致性 | SMF配置的预定义规则名称 | UPF配置的RULENAME必须与SMF一致 |

### 1.5 与BWM（WSFD-211005）的差异

| 维度 | 业务触发的QoS保证 (WSFD-109107) | 带宽管理BWM (WSFD-211005) |
|------|--------------------------------|--------------------------|
| 带宽控制方式 | GBR保证（带宽下限保证） | 限速/整形（带宽上限控制） |
| 触发机制 | 业务识别触发专用承载/QoS Flow创建 | 基于策略的速率限制 |
| 资源类型 | GBR资源（专用资源） | Non-GBR资源（共享资源池调度） |
| 载体 | 专有承载 / 专有QoS Flow | 缺省承载 / 缺省QoS Flow上的QER |
| 适用场景 | 需要带宽保证的高价值业务（如VoLTE） | 需要限制带宽的普通业务（如视频限速） |

---

## 2. 核心概念

### 2.1 专用承载（Dedicated Bearer，适用于2/3/4G）

专用承载是EPC网络中为特定业务流（SDF）提供特定QoS保障的EPS承载。与缺省承载不同，专用承载不分配新的IP地址，而是关联到已有的缺省承载（通过LBI - Linked EPS Bearer Identity）。专用承载通常为GBR类型，提供保证比特率。

### 2.2 QoS Flow（适用于5G）

QoS Flow是5G网络中进行QoS控制的最小粒度。每个QoS Flow由QFI（QoS Flow Identifier）唯一标识。5G网络中，专有QoS Flow为特定业务流提供专用的QoS保障，功能上对应2/3/4G的专用承载。专有QoS Flow通常为GBR类型。

### 2.3 缺省承载 / 缺省QoS Flow

用户建立PDU会话/PDN连接时自动建立的初始承载/QoS Flow，用于传输默认业务流。缺省承载/QoS Flow为Non-GBR类型。专用承载/专有QoS Flow通过LBI（2/3/4G）或PDU Session ID（5G）关联到缺省承载/缺省QoS Flow。

### 2.4 GBR / Non-GBR

- **GBR（Guaranteed Bit Rate）**：保证比特率。GBR类型的承载/QoS Flow在网络资源充足时，保证不低于GBR值的比特率传输。同时配置MBR（Maximum Bit Rate）限制最大速率。GBR参数通过ADD QOSPROP命令的GBRUPLKVALUE（保证的上行比特率）和GBRDNLKVALUE（保证的下行比特率）配置。
- **Non-GBR**：非保证比特率。不提供带宽保证，共享资源池调度，受AMBR（Aggregate Maximum Bit Rate）约束。

### 2.5 5QI / QCI

- **5QI（5G QoS Identifier）**：5G网络的QoS等级标识。通过ADD QOSPROP命令的FQI参数配置。5QI为2表示对话型（Conversational），典型用于语音业务。
- **QCI（QoS Class Identifier）**：2/3/4G网络的QoS等级标识。通过ADD QOSPROP命令的QCIVALUE参数配置。QCI=66对应特定的QoS等级。

### 2.6 ARP（Allocation and Retention Priority）

分配保留优先级，用于在资源受限时决定承载/QoS Flow的建立优先级和抢占行为。ARP值越小优先级越高。包含三个子属性：

- **EMPCAP（QoS抢占能力）**：ENABLE表示该业务可以抢占已分配给低优先级业务流的资源；DISABLE表示不可抢占。
- **EMPVUL（QoS被抢占设置）**：ENABLE表示本业务流的资源可被高优先级业务抢占；DISABLE表示不可被抢占。

### 2.7 TFT（Traffic Flow Template）

业务流模板，用于将特定业务数据流（SDF）映射到对应的专用承载。在2/3/4G中，TFT由PGW-C生成并随专有承载创建消息下发。TFT包含包过滤器（Packet Filter），用于匹配上行和下行业务流。

### 2.8 业务触发机制

业务触发的QoS保证的核心机制：

1. **预定义规则下发**：SMF通过N4接口向UPF下发预定义规则名称，UPF将本地配置的规则内容和规则名称匹配。
2. **业务识别与上报**：上行数据流到达UPF，UPF识别需要创建专用承载/QoS Flow的业务报文，向SMF发送PFCP Session Report Request消息，携带URR ID和Rule Information。
3. **QoS策略执行**：SMF收到上报事件后，基于QoS策略触发专用承载/QoS Flow的建立/更新流程。

---

## 3. 实现原理与流程

### 3.1 专有QoS Flow建立流程（5G）

当用户请求的业务数据流到达UPF时，UPF向SMF请求创建专有QoS Flow，SMF使用预定义规则中的QoS策略发起建立流程。

**详细流程（12步）**：

1. **预定义规则下发（可选）**：如果部署了动态PCC，PCF向SMF下发预定义规则；如果未部署动态PCC，SMF使用本地配置的QoS策略规则。SMF通过PFCP Session Modification Request向UPF下发预定义规则名称，UPF匹配本地规则后回复PFCP Session Modification Response。

2. **业务识别与事件上报**：上行数据流到达UPF，UPF识别需要创建专有QoS Flow传输该类业务报文时，向SMF发送PFCP Session Report Request消息。消息携带Usage Report信元组，包含：
   - URR ID
   - Rule Information（包含Rule Name、Precedence、Rule Filter Type、ToS Traffic Class等）

   SMF处理上报事件，基于QoS策略触发QoS Flow更新，向UPF下发PFCP Session Report Response（携带Update PDR、Update QER，含PDR ID、URR ID、SDF等）。

3. **N4会话修改**：SMF向UPF发送PFCP Session Modification Request，携带QoS Flow Identifier、QER ID、Gate Status等信元，提供数据监测、报告规则、CN隧道信息、QoS Flow级别的空闲上下文最大时长等。UPF回复PFCP Session Modification Response。
   - 专有QoS Flow空闲上下文最大时长通过SET APNIDLETIME（APN粒度）或SET DFTIDLETIME（全局粒度）命令的DEDQFIDLETIMER参数设置。

4. **N1N2消息传递**：SMF向AMF发送Namf_Communication_N1N2MessageTransfer消息，携带：
   - N2 SM Information（发送给RAN）：包含QFI、QoS Profile、CN Tunnel Info等
   - N1 SM Container（发送给UE）：PDU Session Modification Command，包含PDU Session ID、QoS rule(s)、QoS Flow级别的QoS参数

5. **AMF转发至RAN**：AMF向(R)AN发送PDU Session Resource Setup Request，包含N2 SM Information和N1 SM Container。

6. **RAN与UE交互**：(R)AN将N1 SM Container（PDU Session Modification Command）转发至UE，请求UE建立专有QoS Flow。

7. **RAN响应**：(R)AN向AMF发送PDU Session Resource Setup Response，建立AN隧道信息，包含AN Tunnel Info、List of Accepted/Rejected QFI等。

8. **AMF转发至SMF**：AMF向SMF发送Nsmf_PDUSession_UpdateSMContext Request，将N2 SM Information转发给SMF。

9. **N4隧道更新**：SMF向UPF发送PFCP Session Modification Request，将AN隧道信息和转发规则发送给UPF。UPF回复PFCP Session Modification Response。

10. **SMF响应AMF**：SMF向AMF发送Nsmf_PDUSession_UpdateSMContext Response。

### 3.2 专有QoS Flow更新流程（5G）

当UPF向SMF上报QoS更新事件（如QoS参数变更）时，发起专有QoS Flow更新流程。

**详细流程（12步）**：

1. 预定义规则下发（可选，同建立流程步骤1）。
2. UPF识别需要QoS更新时，向SMF发送PFCP Session Report Request（携带Usage Report，含URR ID、Rule Information）。SMF处理事件，向UPF下发PFCP Session Report Response（携带Update PDR、Update QER）。
3. SMF通过Namf_Communication_N1N2MessageTransfer响应AMF，携带N2 SM Information和N1 SM Container（PDU Session Modification Command），通知RAN和UE更新QoS信息。
4. AMF向(R)AN发送PDU Session Resource Modify Request，包含N2 SM Information和N1 SM Container。
5. (R)AN与UE交互，转发PDU Session Modification Command。
6. (R)AN向AMF发送PDU Session Resource Modify Response（包含N2 SM Information）。
7. AMF通过Nsmf_PDUSession_UpdateSMContext Request将N2 SM Information转发给SMF。SMF回复Response。
8. 当N4会话有修改时，SMF通过PFCP Session Modification Request更新N4会话，将更新的QoS信息通知UPF。UPF回复Response。
9. UE向(R)AN发送PDU Session Modification Complete（NAS消息），确认接受专有QoS Flow修改。
10. (R)AN将NAS消息转发至AMF。
11. AMF通过Nsmf_PDUSession_UpdateSMContext Request将PDU Session Modification Complete发送给SMF。SMF回复Response。
12. 当N4会话有修改时，SMF通过PFCP Session Modification Request更新N4会话。UPF回复Response。

### 3.3 专有QoS Flow释放流程（5G）

触发专有QoS Flow释放的主要场景：
- **业务流老化**：业务暂停一段时间，超过专有QoS Flow上下文空闲最大时长。
- **AN Release**：连接态UE进入无信号区域（如电梯、隧道），超过一定时间后RAN发起AN Release。此时SMF可根据ADD APNDEACTQFPLCY（APN粒度）/ ADD DEACTQFPLCY（全局粒度）配置决定是否延迟释放专有QoS Flow及延迟释放时间。

**业务流老化场景详细流程（12步）**：

1. 预定义规则下发（可选）。
2. 业务流老化时（超过专有QoS Flow上下文空闲最大时长），UPF向SMF发送PFCP Session Report Request（携带Usage Report，含URR ID、Usage Report trigger）。SMF回复PFCP Session Report Response。
3. SMF向AMF发送Namf_Communication_N1N2MessageTransfer，携带N2 SM Resource Modification Request、N1 SM Container。当专有QoS Flow的UP连接处于激活状态时，还包含N2 Resource Modification Command。
4. 空闲态UE：AMF指示网络侧发起Service Request流程；连接态UE：AMF向(R)AN发送N2 Session Request。
5. (R)AN与UE交互，释放专有QoS Flow相关的AN资源。
6. (R)AN向AMF发送N2 Session Response。
7. AMF发送Nsmf_PDUSession_UpdateSMContext Request给SMF。SMF回复Response。
8. UE向(R)AN发送PDU Session Modification Command Ack。
9. (R)AN向AMF发送N2 Uplink NAS Transfer。
10. AMF通过Nsmf_PDUSession_UpdateSMContext Request将PDU Session Modification Command Ack发送给SMF。SMF回复Response。
11. SMF释放专有QoS Flow的IP地址/前缀与用户面资源：向UPF发送PFCP Session Modification Request，删除PDR、QER、URR等信息。UPF丢弃相关数据包并释放隧道资源和上下文。UPF回复Response。
12. 如果部署了动态PCC，SMF向PCF发起SM Policy Association Modification流程，删除专有QoS Flow相应信息。

### 3.4 专有承载创建流程（2/3/4G）

当用户请求的业务数据流到达PGW-U时，PGW-U向PGW-C请求创建专有承载，PGW-C使用预定义规则关联的QoSProp配置发起专有承载激活流程。

**详细流程（13步）**：

1. 预定义规则下发（可选）：PCRF向PGW-C下发预定义规则，或PGW-C使用本地配置。PGW-C通过PFCP Session Modification Request向PGW-U下发预定义规则名称。

2. 业务识别与事件上报：上行数据流到达PGW-U，PGW-U识别需要创建专有承载时，向PGW-C发送PFCP Session Report Request（携带Usage Report，含URR ID、Rule Information）。PGW-C处理事件，向PGW-U下发PFCP Session Report Response（携带Create PDR、Create QER，含PDR ID、URR ID、SDF等）。
   - 业务触发专有承载创建时，如需同时申请配额，PGW-U在PFCP Session Report Request的Rule Information中包含Charging URR ID字段，指示专载绑定的计费URR ID。此后Gy接口的CCR-I消息中携带预申请配额的RG。

3. PGW-C向SGW-C发送Create Bearer Request，消息包含：IMSI、PTI、EPS Bearer QoS、TFT、S5/S8 TEID、Charging Id、LBI（Linked EPS Bearer Identity，即UE的缺省承载ID）。SGW-C收到后建立专有承载上下文，根据LBI关联缺省承载和专有承载，同时向SGW-U发送PFCP Session Modification Request。

4. SGW-C向MME发送Create Bearer Request。

5. MME向eNodeB发送Bearer Setup Request，消息包含：EPS Bearer Identity、EPS Bearer QoS、Session Management Request、S1-TEID。其中Session Management Request包含：PTI、TFT、EPS Bearer QoS parameters（不含ARP）、Protocol Configuration Options、EPS Bearer Identity、LBI。

6. eNodeB将EPS Bearer QoS映射为Radio Bearer QoS，向UE发送RRC Connection Reconfiguration消息（包含Radio Bearer QoS、Session Management Request、EPS RB Identity）。UE保存信息并通过LBI关联专有承载和缺省承载。

7. UE向eNodeB响应RRC Connection Reconfiguration Complete，确认无线承载激活。

8. eNodeB向MME发送Bearer Setup Response（EPS Bearer Identity、S1-TEID），确认空口承载已激活。

9. UE向eNodeB发送Direct Transfer消息（携带NAS层构建的Session Management Response，含EPS Bearer Identity）。

10. eNodeB向MME发送Session Management Response。

11. MME收到Bearer Setup Response和Session Management Response后，向SGW-C响应Create Bearer Response（EPS Bearer Identity、S1-TEID）。SGW-C保存S1-U TEID，传递给SGW-U，SGW-U建立和eNodeB间的S1-U专有承载。

12. SGW-C向PGW-C响应Create Bearer Response（EPS Bearer Identity、S5/S8-TEID）。PGW-C保存S5/S8-TEID，建立专有承载。

13. PGW-C将承载信息传递给PGW-U。

### 3.5 专有承载更新流程（2/3/4G）

当PGW-U向PGW-C上报QoS更新事件（QoS参数变更）时发起。

**详细流程（14步）**：

1. 预定义规则下发（可选）。
2. PGW-U向PGW-C发送PFCP Session Report Request（携带Usage Report，含URR ID、Rule Information）。PGW-C处理事件，向PGW-U下发PFCP Session Report Response（携带Update PDR、Update QER）。
3. PGW-C生成TFT并更新EPS Bearer QoS，向SGW-C发送Update Bearer Request（EPS Bearer Identity、EPS Bearer QoS、APN-AMBR、TFT）。
4. SGW-C向MME发送Update Bearer Request（EPS Bearer Identity、EPS Bearer QoS、APN-AMBR、TFT）。
5. MME向eNodeB发送Bearer Modify Request，包含NAS消息（Session Management Request）。
6. eNodeB将修改后的EPS Bearer QoS映射为Radio Bearer QoS，向UE发送RRC Connection Reconfiguration消息，同时转发Modify EPS Bearer Context Request。
7. UE向eNodeB发送RRC Connection Reconfiguration Complete确认无线承载更改。
8. eNodeB向MME发送Bearer Modify Response（EPS Bearer Identity），指示请求的EPS Bearer QoS是否可分配。
9. UE向eNodeB发送Direct Transfer消息（携带Session Management Response，含EPS Bearer Identity）。
10. eNodeB转发Session Management Response给MME。
11. MME收到Bearer Modify Response和Session Management Response后，向SGW-C发送Update Bearer Response（EPS Bearer Identity）。
12. SGW-C通过PFCP Session Modification Request将承载更新信息传递给SGW-U。
13. SGW-C向PGW-C发送Update Bearer Response（EPS Bearer Identity）。
14. PGW-C通过PFCP Session Modification Request将承载更新信息传递给PGW-U。

### 3.6 专有承载去激活流程（2/3/4G）

当业务暂停一段时间、业务流老化时，PGW-U向PGW-C上报QoS事件发起承载去激活。

**详细流程（13步）**：

1. 预定义规则下发（可选）。
2. PGW-U向PGW-C发送PFCP Session Report Request（携带Usage Report）。PGW-C处理事件，向PGW-U下发PFCP Session Report Response，通知删除PDR、QER、URR等信息。
3. PGW-C向SGW-C发送Delete Bearer Request（EPS Bearer Identity）。
4. SGW-C向SGW-U发送PFCP Session Modification Request，请求释放承载上下文。
5. SGW-C向MME发送Delete Bearer Request（EPS Bearer Identity）。
6. MME向eNodeB发送E-Rab Release Command（EPS Bearer Identity），包含NAS消息Deactivate EPS Bearer Context Request。
7. eNodeB向UE发送Radio Bearer Release Request，同时转发Deactivate EPS Bearer Context Request。
8. UE向eNodeB回复Radio Bearer Release Response。eNodeB向MME发送E-Rab Release Response（EPS Bearer Identity）。
9. UE NAS层建立Deactivate EPS Bearer Context Accept（含EPS Bearer Identity），发送给eNodeB。eNodeB转发给MME。
10. MME删除专有承载上下文，向SGW-C发送Delete Bearer Response（EPS Bearer Identity）。
11. SGW-C收到MME响应后，向SGW-U发送PFCP Session Deletion Request，删除EPS专有承载相关上下文。
12. SGW-C向PGW-C发送Delete Bearer Response（EPS Bearer Identity）。
13. PGW-C通过PFCP Session Deletion Request释放承载信息。

### 3.7 端到端流程总结

```
[业务触发QoS保证 - 端到端信令路径]

用户面（UDG侧）                      控制面（UNC侧）
===========                          ===========

  用户业务流到达
       |
       v
  UPF/PGW-U 业务识别
  （匹配预定义规则）
       |
       +--- PFCP Session Report Request --->  SMF/PGW-C
       |     (URR ID, Rule Information)         |
       |                                        v
       |                                    处理QoS事件
       |                                    基于QoS策略
       |                                    发起承载/QoS Flow建立
       |                                        |
       <-- PFCP Session Report Response ---+    |
       |   (Update PDR, Update QER)        |    |
       |                                   |    |
       <-- PFCP Session Modification ---+  |    |
       |   (QFI/QoS参数)                |  |    |
       |                                |  |    |
       |                          +-> AMF/MME -> RAN -> UE
       |                          |    (N1N2/创建承载)
       |                          |    |
       |                          <-- 响应消息 --+
       |                                   |
       <-- PFCP Session Modification ---+  |
       |   (AN隧道信息)                  |  |
       |                                |  |
  UPF/PGW-U 建立专用通道                |  |
  业务流使用专用承载/QoS Flow传输 <-----+
```

### 3.8 5G QoS Flow 与 2/3/4G专用承载的差异

| 维度 | 5G专有QoS Flow | 2/3/4G专有承载 |
|------|----------------|----------------|
| QoS标识 | QFI（5QI映射） | EPS Bearer Identity（QCI映射） |
| 控制面消息 | Namf_Communication_N1N2MessageTransfer | Create Bearer Request/Update Bearer Request |
| 接入网节点 | (R)AN（gNB） | eNodeB/MME |
| 用户面接口 | N3/N9隧道 | S1-U/S5/S8隧道 |
| QoS参数配置 | QOSTYPE=QOS_FLOW_PARA, FQI | QOSTYPE=QOS_BEARER_PARA, QCIVALUE |
| 空闲定时器 | DEDQFIDLETIMER（专有QoS Flow空闲定时器） | 无独立参数（2/3/4G承载老化） |
| 延迟释放策略 | ADD APNDEACTQFPLCY（UE无线丢失场景） | 无延迟释放策略 |
| 规则下发接口 | N4（PFCP） | S5/S8（GTP-C）+ N4（PFCP） |
| TFT | 无TFT，使用QoS Rule | PGW-C生成TFT，下发至UE |

---

## 4. 配置规则

### 4.1 涉及的MML命令清单

本特性涉及的MML命令共13个（核心配置）+ 2个（License/查询辅助），分类如下：

**核心配置命令（13个）**：

| 序号 | 命令 | 用途 | 粒度 |
|------|------|------|------|
| 1 | ADD URR | 配置QoS使用量上报规则 | 全局 |
| 2 | ADD QOSPROP | 配置业务QoS属性（GBR/MBR/5QI/QCI/ARP） | 全局 |
| 3 | ADD PCCPOLICYGRP | 配置PCC策略组（绑定QoS属性） | 全局 |
| 4 | ADD RULE | 配置本地规则（绑定PCC策略组或QoS属性） | 全局 |
| 5 | ADD USERPROFILE | 配置用户模板 | 全局 |
| 6 | ADD RULEBINDING | 配置规则与用户模板的绑定关系 | 全局 |
| 7 | ADD USRPROFGROUP | 配置用户模板组 | 全局 |
| 8 | ADD UPBINDUPG | 配置用户模板与用户模板组的绑定关系 | 全局 |
| 9 | ADD APNUSRPROFG | 配置APN与用户模板组的绑定关系 | APN |
| 10 | SET APNIDLETIME | 设置专有QoS Flow空闲定时器 | APN |
| 11 | SET DFTIDLETIME | 设置默认空闲定时器（全局） | 全局 |
| 12 | ADD APNDEACTQFPLCY | 配置基于APN的去活专有QoS Flow策略 | APN |
| 13 | ADD DEACTQFPLCY | 配置去活专有QoS Flow策略（全局） | 全局 |

**License与查询命令（2个）**：

| 序号 | 命令 | 用途 |
|------|------|------|
| 14 | SET LICENSESWITCH | 打开License开关 |
| 15 | LST LICENSESWITCH | 查询License开关状态 |

**调测查询命令（补充）**：

| 序号 | 命令 | 用途 |
|------|------|------|
| 16 | LST APNIDLETIME | 查询APN空闲上下文定时器 |
| 17 | LST DFTIDLETIME | 查询默认空闲上下文定时器 |
| 18 | LST APNDEACTQFPLCY | 查询基于APN的去活QoS Flow策略 |
| 19 | LST DEACTQFPLCY | 查询去活QoS Flow策略 |
| 20 | LST APN | 查询APN配置 |
| 21 | EXP MML | 导出MML配置文件（故障排查用） |

### 4.2 ADD URR - 配置QoS使用量上报规则

配置用于QoS事件上报的URR规则。

| 参数 | 说明 | 取值样例 |
|------|------|----------|
| URRNAME | 使用量上报规则名称 | URR_qos_01 |
| URRID | URR标识（全局唯一，建议大于1000） | 1005 |
| USAGERPTMODE | 使用量上报模式 | QOS（固定取值） |

### 4.3 ADD QOSPROP - 配置QoS属性

配置专有承载/QoS Flow的QoS参数。这是本特性最核心的配置命令。

**5G用户参数（QOSTYPE=QOS_FLOW_PARA）**：

| 参数 | 说明 | 取值样例 |
|------|------|----------|
| QOSPROPNAME | QoS属性名称 | qosprop_501 |
| GBRUPLKVALUE | 保证的上行比特率(kbps) | 600 |
| GBRDNLKVALUE | 保证的下行比特率(kbps) | 6000 |
| MBRUPLKVALUE | 最大上行比特率(kbps) | 1000 |
| MBRDNLKVALUE | 最大下行比特率(kbps) | 10000 |
| QOSTYPE | QoS属性类型 | QOS_FLOW_PARA |
| ARPVALUE | 分配保留优先级（值越小优先级越高） | 5 |
| FQI | 5G QoS标识（5QI） | 2 |
| QOSURRNAME | QoS使用量上报规则名称 | URR_qos_01 |
| EMPCAP | QoS抢占能力 | DISABLE |
| EMPVUL | QoS被抢占设置 | ENABLE |

**2/3/4G用户参数（QOSTYPE=QOS_BEARER_PARA）**：

| 参数 | 说明 | 取值样例 |
|------|------|----------|
| QOSPROPNAME | QoS属性名称 | qosprop_401 |
| GBRUPLKVALUE | 保证的上行比特率(kbps) | 600 |
| GBRDNLKVALUE | 保证的下行比特率(kbps) | 6000 |
| MBRUPLKVALUE | 最大上行比特率(kbps) | 1000 |
| MBRDNLKVALUE | 最大下行比特率(kbps) | 10000 |
| QOSTYPE | QoS属性类型 | QOS_BEARER_PARA |
| QCIVALUE | QoS等级标识（QCI） | 66 |
| ARPVALUE | 分配保留优先级 | 5 |
| QOSURRNAME | QoS使用量上报规则名称 | URR_qos_01 |
| EMPCAP | QoS抢占能力 | DISABLE |
| EMPVUL | QoS被抢占设置 | ENABLE |

**关键差异**：5G使用FQI（5QI），2/3/4G使用QCIVALUE（QCI），QOSTYPE分别为QOS_FLOW_PARA和QOS_BEARER_PARA。

### 4.4 ADD PCCPOLICYGRP - 配置PCC策略组

将QoS属性绑定到PCC策略组，用于规则通过PCC策略组间接绑定QoS属性的场景。

| 参数 | 说明 | 取值样例 |
|------|------|----------|
| PCCPOLICYGRPNM | PCC策略组名称 | pccpolicy_group |
| QOSPROPNAME | QoS属性名称（引用ADD QOSPROP） | qosprop_501 |

### 4.5 ADD RULE - 配置规则

配置本地规则，通过PCC策略组或直接绑定QoS属性。有两种绑定方式：

**方式一：通过PCC策略组绑定（POLICYTYPE=PCC）**：

| 参数 | 说明 | 取值样例 |
|------|------|----------|
| RULENAME | 规则名称 | rule_test |
| POLICYTYPE | 策略类型 | PCC |
| POLICYNAME | 策略名称（引用PCCPOLICYGRPNM） | pccpolicy_group |

**方式二：直接绑定QoS属性（POLICYTYPE=QOS）**：

| 参数 | 说明 | 取值样例 |
|------|------|----------|
| RULENAME | 规则名称 | rule_test |
| POLICYTYPE | 策略类型 | QOS |
| POLICYNAME | 策略名称（引用QOSPROPNAME） | qosprop_501 |

**关键约束**：PCC类型的RULENAME值与QOS类型的RULENAME值不能相同。

### 4.6 用户模板配置链

用户模板配置链用于将规则绑定到具体的APN/DNN，实现策略的按APN生效。

**ADD USERPROFILE**：

| 参数 | 说明 | 取值样例 |
|------|------|----------|
| USERPROFILENAME | 用户模板名称 | up_test |
| UPTYPE | 用户模板类型 | PCC（固定取值） |

**ADD RULEBINDING**：

| 参数 | 说明 | 取值样例 |
|------|------|----------|
| USERPROFILENAME | 用户模板名称 | up_test |
| RULENAME | 规则名称 | rule_test |
| POLICYTYPE | 策略类型 | QOS |

**ADD USRPROFGROUP**：

| 参数 | 说明 | 取值样例 |
|------|------|----------|
| USERPROFGNAME | 用户模板组名称 | upg_test |

**ADD UPBINDUPG**：

| 参数 | 说明 | 取值样例 |
|------|------|----------|
| USERPROFGNAME | 用户模板组名称 | upg_test |
| UPBINDTYPE | 用户模板绑定类型 | DEFAULT |
| USERPROFILENAME | 用户模板名称 | up_test |

**ADD APNUSRPROFG**：

| 参数 | 说明 | 取值样例 |
|------|------|----------|
| APN | APN名称 | huawei.com |
| USERPROFGNAME | 用户模板组名称 | upg_test |

### 4.7 SET APNIDLETIME - 专有QoS Flow空闲定时器

| 参数 | 说明 | 取值样例 |
|------|------|----------|
| APN | APN名称 | huawei.com |
| INHERIT | 继承默认开关 | NO |
| HSMFTIMERLEVEL | H-SMF空闲上下文核查级别 | QOSFLOW（固定取值） |
| DEDQFIDLETIMER | 专有QoS Flow空闲定时器时长(min) | 600 |

**优先级**：APN粒度 > 全局粒度（SET DFTIDLETIME）。修改DEDQFIDLETIMER后对新激活的用户生效，仅对专有QoS Flow生效。设置过大会长时间占用上下文资源；设置过小会强制拆话，删除后需重新创建。

### 4.8 ADD APNDEACTQFPLCY - 去活专有QoS Flow策略

用于UE无线连接丢失（NGAPCAUSEVALUE=21）场景，配置是否延迟释放专有GBR类型QoS Flow。

| 参数 | 说明 | 取值样例 |
|------|------|----------|
| APN | APN名称 | imsapn.com |
| NGAPCAUSEGROUP | NgApCause组 | RADIO_NETWORK |
| NGAPCAUSEVALUE | NgApCause值 | 21 |
| QFPLCY | 专有GBR类型QoS Flow处理策略 | DELAY_RELEASE |
| DELAYTIMER | 延迟释放时长(秒) | 60 |

**优先级**：APN粒度（ADD APNDEACTQFPLCY） > 全局粒度（ADD DEACTQFPLCY）。

### 4.9 配置架构总结

```
配置层次关系：

License开关
  SET LICENSESWITCH (LKV3W9STQE11)
      |
      v
QoS上报规则
  ADD URR (USAGERPTMODE=QOS)
      |
      v
QoS属性 (GBR/MBR/5QI/QCI/ARP)
  ADD QOSPROP ---引用---> ADD URR
      |
      +---> 方式一: ADD PCCPOLICYGRP ---引用---> ADD QOSPROP
      |         |
      |         v
      |    ADD RULE (POLICYTYPE=PCC) ---引用---> ADD PCCPOLICYGRP
      |
      +---> 方式二: ADD RULE (POLICYTYPE=QOS) ---引用---> ADD QOSPROP
                  |
                  v
             ADD USERPROFILE (UPTYPE=PCC)
                  |
             ADD RULEBINDING (绑定RULE到USERPROFILE)
                  |
             ADD USRPROFGROUP
                  |
             ADD UPBINDUPG (绑定USERPROFILE到GROUP)
                  |
             ADD APNUSRPROFG (绑定GROUP到APN/DNN)

可选配置:
  SET APNIDLETIME (专有QoS Flow空闲定时器)
  ADD APNDEACTQFPLCY (去活策略/延迟释放)
```

---

## 5. 配置案例

### 5.1 案例一：5G用户业务触发专有QoS Flow（L7业务触发）

**场景描述**：5G用户访问视频业务，UPF通过L7 URL识别业务流，触发创建专有QoS Flow，提供GBR=6000kbps下行保证带宽。

**网络条件**：无可用PCF，使用本地PCC静态规则。

**完整命令序列**：

```mml
// 步骤1: 打开License开关
SET LICENSESWITCH:LICITEM="LKV3W9STQE11",SWITCH=ENABLE;

// 步骤2: 配置QoS使用量上报规则
ADD URR: URRNAME="URR_qos_01", URRID=1005, USAGERPTMODE=QOS;

// 步骤3: 配置5G业务QoS属性（GBR保证）
ADD QOSPROP: QOSPROPNAME="qosprop_501", GBRUPLKVALUE=600, GBRDNLKVALUE=6000, MBRUPLKVALUE=1000, MBRDNLKVALUE=10000, QOSTYPE=QOS_FLOW_PARA, ARPVALUE=5, FQI=2, QOSURRNAME="URR_qos_01";

// 步骤4: 配置PCC策略组（绑定QoS属性）
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicy_group",QOSPROPNAME="qosprop_501";

// 步骤5: 配置规则（通过PCC策略组绑定）
ADD RULE:RULENAME="rule_test",POLICYTYPE=PCC,POLICYNAME="pccpolicy_group";

// 步骤6: 配置用户模板
ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC;

// 步骤7: 绑定规则到用户模板
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test",POLICYTYPE=QOS;

// 步骤8: 配置用户模板组
ADD USRPROFGROUP:USERPROFGNAME="upg_test";

// 步骤9: 绑定用户模板到用户模板组
ADD UPBINDUPG:USERPROFGNAME="upg_test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up_test";

// 步骤10: 绑定用户模板组到APN/DNN
ADD APNUSRPROFG:APN="huawei.com",USERPROFGNAME="upg_test";

// 步骤11（可选）: 配置专有QoS Flow空闲定时器
SET APNIDLETIME: APN="huawei.com", INHERIT=NO, HSMFTIMERLEVEL=QOSFLOW, DEDQFIDLETIMER=600;

// 步骤12（可选）: 配置去活策略（UE无线丢失时延迟释放）
ADD APNDEACTQFPLCY: APN="huawei.com", NGAPCAUSEGROUP=RADIO_NETWORK, NGAPCAUSEVALUE=21, QFPLCY=DELAY_RELEASE, DELAYTIMER=60;
```

**预期效果**：
- UPF上配置对应的L7 URL过滤规则（RULENAME="rule_test"），名称与SMF一致
- 用户访问匹配URL的业务流时，UPF向SMF上报PFCP Session Report Request
- SMF基于QoS策略发起专有QoS Flow建立，QFI由FQI=2映射
- 专有QoS Flow提供GBR=600kbps上行 / 6000kbps下行保证
- 用户停止访问10分钟后（调测场景），专有QoS Flow释放

### 5.2 案例二：2/3/4G用户业务触发专有承载（L34业务触发）

**场景描述**：4G用户访问特定业务，PGW-U通过L34五元组识别业务流，触发创建专有承载，提供GBR保证。规则直接绑定QoS属性（不经过PCC策略组）。

**网络条件**：无可用PCRF，使用本地PCC静态规则。

**完整命令序列**：

```mml
// 步骤1: 打开License开关
SET LICENSESWITCH:LICITEM="LKV3W9STQE11",SWITCH=ENABLE;

// 步骤2: 配置QoS使用量上报规则
ADD URR: URRNAME="URR_qos_02", URRID=1006, USAGERPTMODE=QOS;

// 步骤3: 配置2/3/4G业务QoS属性（GBR保证）
ADD QOSPROP: QOSPROPNAME="qosprop_401", GBRUPLKVALUE=600, GBRDNLKVALUE=6000, MBRUPLKVALUE=1000, MBRDNLKVALUE=10000, QOSTYPE=QOS_BEARER_PARA, QCIVALUE=66, ARPVALUE=5, QOSURRNAME="URR_qos_02";

// 步骤4: 配置规则（直接绑定QoS属性，不经过PCC策略组）
ADD RULE:RULENAME="rule_l34_test",POLICYTYPE=QOS,POLICYNAME="qosprop_401";

// 步骤5: 配置用户模板
ADD USERPROFILE:USERPROFILENAME="up_l34_test",UPTYPE=PCC;

// 步骤6: 绑定规则到用户模板
ADD RULEBINDING:USERPROFILENAME="up_l34_test",RULENAME="rule_l34_test",POLICYTYPE=QOS;

// 步骤7: 配置用户模板组
ADD USRPROFGROUP:USERPROFGNAME="upg_l34_test";

// 步骤8: 绑定用户模板到用户模板组
ADD UPBINDUPG:USERPROFGNAME="upg_l34_test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up_l34_test";

// 步骤9: 绑定用户模板组到APN
ADD APNUSRPROFG:APN="internet.apn",USERPROFGNAME="upg_l34_test";
```

**预期效果**：
- PGW-U上配置对应的L34五元组过滤规则（RULENAME="rule_l34_test"），名称与PGW-C一致
- 用户访问匹配五元组的业务流时，PGW-U向PGW-C上报PFCP Session Report Request
- PGW-C基于QoS策略发起专有承载激活流程，QCI=66
- 专有承载提供GBR=600kbps上行 / 6000kbps下行保证
- 业务流老化后PGW-U上报事件，PGW-C发起承载去激活

### 5.3 案例一与案例二的关键差异

| 维度 | 案例一（5G） | 案例二（2/3/4G） |
|------|-------------|------------------|
| QOSTYPE | QOS_FLOW_PARA | QOS_BEARER_PARA |
| QoS标识 | FQI=2（5QI） | QCIVALUE=66（QCI） |
| 规则绑定方式 | 方式一：PCC策略组 | 方式二：直接绑定QoS属性 |
| 建立结果 | 专有QoS Flow | 专有承载 |
| 空闲定时器 | DEDQFIDLETIMER可配 | 无独立参数 |
| 延迟释放 | ADD APNDEACTQFPLCY可配 | 无延迟释放策略 |

---

## 6. 验证与调测

### 6.1 调测前提条件

- 已完成激活业务触发的QoS保证的全部配置步骤。
- 已加载License（LKV3W9STQE11）。
- 测试终端可用，OM Portal可用。

### 6.2 调测数据准备

| 数据项 | 取值样例 | 说明 |
|--------|----------|------|
| 用户IMSI号 | 460000123456789 | 测试终端自带 |
| APN名称 | apn1 | 已通过ADD APN命令配置 |
| 业务触发地址 | www.example.com/ | 取自UPF上配置的七层过滤规则中的URL |
| GBRUPLKVALUE | 600 | 取自ADD QOSPROP配置 |
| GBRDNLKVALUE | 6000 | 取自ADD QOSPROP配置 |
| DEDQFIDLETIMER | 10 | 取自SET APNIDLETIME/SET DFTIDLETIME配置 |
| DELAYTIMER | 60 | 取自ADD APNDEACTQFPLCY/ADD DEACTQFPLCY配置 |

### 6.3 调测步骤详解

**步骤1：验证License开关**

```
LST LICENSESWITCH:LICITEM="LKV3W9STQE11";
```

- SWITCH为ENABLE：继续下一步。
- SWITCH为DISABLE：执行 `SET LICENSESWITCH:LICITEM="LKV3W9STQE11",SWITCH=ENABLE;`

**步骤2：创建用户跟踪任务**

在OM Portal上创建用户跟踪任务，关联测试终端IMSI。

**步骤3：测试终端接入网络**

测试终端使用配置的APN（如apn1）接入网络。
- 接入成功：继续下一步。
- 接入失败：调测接入功能。

**步骤4：验证预定义规则名称一致性**

根据用户跟踪任务，检查PCF、SMF下发的预定义规则名称是否与UPF上的RULENAME一致。
- 一致：继续下一步。
- 不一致：将SMF、PCF和UPF上的预定义规则名称修改为相同后重新接入。
  - **关键约束**：网络中存在PCRF/PCF时，UPF、SMF、PCRF/PCF上配置的预定义规则名称必须一致，否则不能达到预期效果。

**步骤5：触发业务访问**

测试终端访问 www.example.com 网页。

**步骤6：验证UPF事件上报**

根据用户跟踪任务，检查UPF是否向SMF发送PFCP Session Report Request，且消息中携带URRID、Rule Information等。
- 是：继续下一步。
- 否：检查并确保UPF上的业务触发的QoS保证功能配置正确后重新测试。

**步骤7：验证SMF发起建立流程**

根据用户跟踪任务，检查SMF是否向AMF发送Namf_Communication_N1N2MessageTransfer消息，且消息中携带QoS-rule等。
- 是：继续下一步。
- 否：检查并确保SMF上的QoS URR和QoSProp配置正确后重新测试。

**步骤8：验证信令流程完整性**

根据用户跟踪任务，结合实现原理中的消息流程，判断后续消息是否正常。
- 是：继续验证业务效果。
- 否：联系华为技术支持。

**步骤9：验证业务流使用专有QoS Flow**

测试终端访问 www.example.com 上的指定业务（例如视频），在UPF上观测业务流使用的QoS Flow是否正确（QFI值是否与FQI配置一致）。

**步骤10：验证空闲定时器（可选）**

测试终端停止访问该业务，达到QoS Flow级别的上下文空闲最大时长（如10分钟）时，观察SMF是否释放该专有QoS Flow。
- 是：验证通过。
- 否：联系华为技术支持。

**步骤11-12：验证延迟释放（可选）**

- 步骤11：测试终端发起语音呼叫，进入无信号区域，停留时间小于延迟释放时间（如60秒），查看呼叫是否中断。
  - 否（未中断）：步骤12。
  - 是（中断）：联系华为技术支持。
- 步骤12：停留时间大于延迟释放时间（如60秒），查看呼叫是否中断。
  - 是（中断）：验证通过。
  - 否（未中断）：联系华为技术支持。

### 6.4 常见问题排查

| 问题现象 | 可能原因 | 排查方法 |
|----------|----------|----------|
| UPF不上报QoS事件 | UPF上业务过滤规则未配置或名称不一致 | 检查UPF上的RULENAME是否与SMF一致 |
| SMF收到事件但不建立QoS Flow | SMF上QoS URR或QoSProp配置错误 | 检查ADD URR的USAGERPTMODE是否为QOS，ADD QOSPROP参数是否正确 |
| QoS Flow建立后无GBR保证效果 | QoSProp中GBR值配置为0或错误 | 检查GBRUPLKVALUE和GBRDNLKVALUE取值 |
| 专有QoS Flow频繁释放 | DEDQFIDLETIMER设置过小 | 调大SET APNIDLETIME的DEDQFIDLETIMER值 |
| 语音呼叫在弱信号区域中断 | 未配置延迟释放策略 | 配置ADD APNDEACTQFPLCY（QFPLCY=DELAY_RELEASE） |
| License未生效 | License开关未打开 | 执行LST LICENSESWITCH确认，必要时SET LICENSESWITCH |
| 接入失败 | APN配置问题或接入功能异常 | 使用LST APN确认APN配置，调测接入功能 |

### 6.5 故障信息收集

调测失败时，执行以下操作收集信息供华为技术支持分析：

1. 重新执行上述调测步骤并保存报文。
2. 执行 `EXP MML` 命令将当前配置数据导出为MML脚本文件并保存。
3. 收集并保存所有查询命令的输出信息。
4. 收集用户跟踪日志。

---

## 7. 参考信息

### 7.1 遵循标准

| 标准类别 | 标准编号 | 标准名称 |
|----------|----------|----------|
| 3GPP | TS 23.401 | General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access |
| 3GPP | TS 23.501 | System Architecture for the 5G System |

### 7.2 特性交互

| 交互类型 | 相关特性 | 控制项 | 交互说明 |
|----------|----------|--------|----------|
| 依赖 | WSFD-109101 PCC基本功能 | 82207979 PCC基本功能 | UNC从PCRF/PCF获取预定义规则时，需要开启PCC基本功能 |
| 影响 | WSFD-205105 上下文回收管理 | 82200BNN 上下文回收管理 | 上下文回收管理中设置的"专有QoS Flow空闲定时器时长"参数影响本特性创建的专有QoS Flow生命周期。空闲超时后SMF会强制释放该QoS Flow |

### 7.3 License要求

| License控制项 | License编号 | 说明 |
|---------------|-------------|------|
| 业务触发的QoS保证 | 82208819 / LKV3W9STQE11 | 必须获得License许可并使用SET LICENSESWITCH打开开关 |

### 7.4 版本支持

| NF | 支持版本 | 功能说明 |
|----|----------|----------|
| GGSN-C/PGW-C/SMF (UNC) | UNC 20.5.0及后续 | PCRF/PCF状态维护、规则选择、Gx/N7消息处理、承载/QoS Flow绑定控制、N4接口URR下发、本地PCC策略 |
| PGW-U/UPF (UDG) | UDG 20.2.0及后续 | 业务信息收集检测、PCC策略执行、QoS策略执行 |
| PCRF/PCF | 无特殊要求 | 策略决策、QoS策略/计费规则下发、AF会话绑定 |

### 7.5 对系统的影响

UNC支持业务触发专有承载/专有QoS Flow建立，会增加信令消息的处理开销；由于开销增加，将导致CPU占用率相应上升。

### 7.6 应用限制

园区ULCL分流和专用DNN+ULCL分流/超级漫游（正向分流）场景下，仅支持公网业务触发的专有承载创建，不支持园区业务触发的专有承载创建。

### 7.7 发布历史

| 特性版本 | 发布版本 | 发布说明 |
|----------|----------|----------|
| 01 | 20.5.0 | 首次发布，支持业务触发的QoS保证特性 |

---

## 8. 知识来源

### 8.1 源文档登记表

| 序号 | 文档名称 | 原始路径 | 内容贡献 |
|------|----------|----------|----------|
| 1 | WSFD-109107 业务触发的QoS保证参考信息 | `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109107 业务触发的QoS保证/WSFD-109107 业务触发的QoS保证参考信息_85397060.md` | MML命令清单（13个命令）、告警/软参/测量指标信息 |
| 2 | 专有QoS Flow相关流程（适用于5G） | `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109107 业务触发的QoS保证/实现原理/专有QoS Flow相关流程（适用于5G）_85678418.md` | 5G专有QoS Flow建立（10步）、更新（12步）、释放（12步）完整流程 |
| 3 | 专有承载相关流程（适用于2/3/4G） | `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109107 业务触发的QoS保证/实现原理/专有承载相关流程（适用于2_3_4G）_85678417.md` | 2/3/4G专有承载创建（13步）、更新（14步）、去激活（13步）完整流程 |
| 4 | 激活业务触发的QoS保证 | `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109107 业务触发的QoS保证/激活业务触发的QoS保证_85397058.md` | 配置步骤（9步）、参数数据规划表、完整命令脚本示例 |
| 5 | 特性概述 | `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109107 业务触发的QoS保证/特性概述_85397056.md` | 特性定义、客户价值、应用场景、可获得性、特性交互、遵循标准 |
| 6 | 调测业务触发的QoS保证 | `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109107 业务触发的QoS保证/调测业务触发的QoS保证_85397059.md` | 调测步骤（13步）、调测数据准备、故障信息收集方法 |
