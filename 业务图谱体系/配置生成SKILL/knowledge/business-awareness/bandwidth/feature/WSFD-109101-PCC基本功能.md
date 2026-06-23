# WSFD-109101 PCC基本功能（SMF/PGW-C/AMF侧）知识文档

> **带宽控制场景视角**：本文档聚焦PCC如何作为带宽控制的核心决策通道，重点阐述PCC如何向用户面（UDG/UPF）下发QoS参数（QCI/5QI、MBR、GBR、ARP）、如何通过Event Triggers/PCR Triggers触发QoS变更，以及策略规则如何控制用户带宽分配。

## 1. 概述

### 1.1 定义

PCC（Policy and Charging Control）基本功能是UNC（SMF/PGW-C/AMF）侧的策略控制功能。在带宽控制场景中，PCC是QoS决策的接收者和管理者：UNC作为策略控制执行功能（PCEF-C），通过Gx接口（2G/3G/4G）或N7/N15/N28服务化接口（5G）接收PCRF/PCF下发的QoS策略规则，并将QoS参数（QCI/5QI、MBR上行/下行、GBR上行/下行、ARP优先级）下发到UDG（PCEF-U）执行实际的带宽管控。

本特性与UDG侧的GWFD-020351 PCC基本功能配合，构成完整的带宽控制策略执行链路：
- **UNC（控制面）**：接收QoS决策、管理规则生命周期、处理QoS变更事件
- **UDG（用户面）**：根据QoS参数执行实际的流量调度、限速（Rate Limiting）、整形（Shaping）、门控

### 1.2 适用NF

| 网元 | 角色 | 适用场景 | 最低版本 |
|------|------|----------|----------|
| SMF | 策略控制执行功能（PCEF-C） | 5G SM策略偶联、N7接口、PDU会话QoS控制 | UNC 20.0.0 |
| PGW-C | 策略控制执行功能（PCEF-C） | 2G/3G/4G Gx接口、IP-CAN会话QoS控制 | UNC 20.3.0 |
| AMF | 接入和移动性策略执行 | 5G AM策略偶联、UE策略偶联（RFSP/SAR） | UNC 20.0.0 |
| GGSN | 策略控制执行功能（PCEF-C） | 2G/3G Gx接口、PDP上下文QoS控制 | UNC 20.3.0 |
| UPF/PGW-U/GGSN-U | 用户面策略执行（PCEF-U） | 执行QoS限速/整形/门控 | UDG 20.0.0/20.3.0 |

### 1.3 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|----------|----------|----------|
| 01 | 20.0.0 | 5G PCC基本功能首次发布（AMF+SMF），支持N7/N15/N28接口。 |
| 01 | 20.3.0 | 2G/3G/4G PCC基本功能（Gx接口）首次发布（PGW-C/GGSN）。 |

### 1.4 License要求

| NF | License控制项 | 说明 |
|----|--------------|------|
| AMF | 82209964 LKV2PCCBF01 PCC基本功能 | AM策略（SAR、RFSP）、UE策略（ANDSP、URSP） |
| SMF/PGW-C/GGSN | 82207979 LKV3W9SPCC11 PCC基本功能 | SM策略（Session Rules + PCC Rules）、Gx策略 |

### 1.5 前置条件

- 完成UNC初始配置。
- 完成加载License。
- UDG侧已完成GWFD-020351 PCC基本功能配置（用户面QoS策略执行）。
- 2G/3G/4G场景：完成WSFD-104508 SCTP配置（Diameter传输层）。
- 5G场景：完成NRF发现配置（用于PCF发现）。

### 1.6 规格限制

| 参数 | 规格 |
|------|------|
| 每个PCRF组内PCRF数（2/3/4G） | 32 |
| 系统PCRF总数（2/3/4G） | 100 |
| PCRF组总数（2/3/4G） | 100 |
| UserProfile模板数 | 5000 |
| 每QoS Flow规则数（5G） | 50 |

### 1.7 遵循标准

| 标准编号 | 标准名称 | 适用范围 |
|----------|----------|----------|
| 3GPP 23.203 | Policy and Charging Control Architecture | 2G/3G/4G QoS架构 |
| 3GPP 29.212 | Policy and Charging Control over Gx Reference Point | 2G/3G/4G Gx接口（QoS AVP传递） |
| 3GPP 29.213 | Policy and Charging Control signalling flows and QoS parameter mapping | QoS参数映射 |
| 3GPP 29.229 | Cx and Dx Interfaces Based on the Diameter Protocol | Diameter协议 |
| 3GPP 23.214 | Architecture enhancements for control and user plane separation | CU分离 |
| 3GPP 29.244 | Interface between the Control Plane and the User Plane Nodes | N4接口（QoS下发到UPF） |
| 3GPP 23.501 | System Architecture for the 5G System; Stage 2 | 5G QoS体系 |
| 3GPP 23.502 | Procedures for the 5G System; Stage 2 | 5G流程 |
| 3GPP 23.503 | Policy and Charging Control Framework for the 5G System; Stage 2 | 5G PCC框架 |
| 3GPP 29.507 | Access and Mobility Policy Control Service; Stage 3 | 5G AM策略 |
| 3GPP 29.512 | Session Management Policy Control Service; Stage 3 | 5G SM策略（QoS下发） |
| 3GPP 29.513 | Policy and Charging Control signalling flows and QoS parameter mapping | 5G QoS映射 |

---

## 2. 核心概念

### 2.1 PCC在带宽控制中的角色

在带宽控制场景中，PCC承担QoS决策传递通道的角色。带宽控制的核心参数链路为：

```
PCRF/PCF（QoS决策）
  → UNC/PCEF-C（接收规则，管理QoS参数）
    → UDG/PCEF-U（执行限速/整形/门控）
```

**PCC规则携带的关键带宽控制参数：**

| QoS参数 | Gx AVP / N7 JSON字段 | 带宽控制作用 |
|---------|----------------------|------------|
| QCI / 5QI | QoS-Class-Identifier | 决定QoS转发处理类（GBR/Non-GBR、延迟、丢包率） |
| MBR-UL | Maximum-Requested-Bandwidth-UL | 上行最大比特率限制 |
| MBR-DL | Maximum-Requested-Bandwidth-DL | 下行最大比特率限制 |
| GBR-UL | Guaranteed-Bitrate-UL | 上行保证比特率 |
| GBR-DL | Guaranteed-Bitrate-DL | 下行保证比特率 |
| ARP | Allocation-Retention-Priority | 分配保留优先级（抢占、优先级、可被抢占） |
| Session-AMBR | sessAmbr（N7） | PDU会话聚合最大比特率 |
| Gate Status | Gate-Status (Open/Closed) | 门控（Open=允许流量，Closed=阻断流量） |
| Redirect URL | Redirect-Server | 重定向URL（阻断+重定向场景） |

### 2.2 CU分离架构下的PCC

PCC基本功能采用CU分离架构：
- **UNC（控制面 PCEF-C）**：SMF/PGW-C/GGSN负责与PCRF/PCF的信令交互，接收QoS策略规则，管理规则生命周期。
- **UDG（用户面 PCEF-U）**：UPF/PGW-U/GGSN-U负责执行实际的带宽管控（限速、整形、门控、重定向）。

规则下发目标可选：
- **主锚点UPF**：默认下发到主锚点UPF。
- **辅锚点UPF**：通过DNAI绑定，下发到指定辅锚点UPF（SSC Mode 3或多锚点场景）。
- **两者同时**：同时下发到主锚点和辅锚点UPF。

### 2.3 5G策略分类与带宽控制

5G PCC包含三种策略类型，与带宽控制的关系：

| 策略类型 | NF | 内容项 | 带宽控制关联 |
|----------|-----|--------|------------|
| AM策略 | AMF | SAR（Service Area Restrictions） | 间接（限制用户接入区域，影响可用带宽） |
| AM策略 | AMF | RFSP Index | 间接（RAT/频段选择优先级） |
| UE策略 | AMF | ANDSP | 无直接关联 |
| UE策略 | AMF | URSP | 间接（路由选择策略，影响DNN/Slice选择） |
| **SM策略** | **SMF** | **Session Rules（Session-AMBR、缺省QoS）** | **直接：会话级带宽上限和缺省QoS** |
| **SM策略** | **SMF** | **PCC Rules（SDF级QoS）** | **直接：业务流级带宽控制（MBR/GBR/5QI/ARP）** |

### 2.4 规则类型

| 规则类型 | 定义来源 | 存储位置 | 下发方式 | 带宽控制适用场景 |
|----------|----------|----------|----------|----------------|
| 动态规则 | PCRF/PCF动态生成 | UNC仅临时存储 | PCRF/PCF主动下发或RAR推送 | 实时带宽调整（如FUP限速、QoS升级） |
| 预定义规则 | PCRF/PCF仅发送规则名 | UNC和UDG均有预配置 | PCRF/PCF通过名称引用 | 固定带宽套餐（如VIP用户100Mbps） |
| 预定义规则组（UserProfile） | PCRF/PCF发送UserProfile名 | UNC和UDG均有预配置 | PCRF/PCF通过名称引用 | 用户套餐打包下发（如多个带宽等级） |
| 本地规则 | UNC本地配置 | UNC和UDG均有预配置 | 无PCRF/PCF，本地安装 | 无PCRF/PCF场景的固定带宽分配 |

### 2.5 规则优先级与带宽控制

- 每条规则有全局优先级值（Priority），值越小优先级越高。
- 动态规则与预定义规则优先级相同时，动态规则优先。
- 高优先级规则可能抢占低优先级规则的带宽资源（通过ARP Preemption Capability/Vulnerability）。
- PCRF/PCF可为动态规则指定优先级；本地预定义规则的优先级通过ADD RULE命令配置。

### 2.6 IP-CAN会话（2G/3G/4G Gx）与QoS控制

IP-CAN会话是Gx接口上的策略控制基本单元，是带宽控制规则生效的载体：

| 阶段 | UNC→PCRF消息 | PCRF→UNC消息 | 带宽控制动作 |
|------|-------------|-------------|------------|
| 建立 | CCR-I | CCA-I（携带初始QoS规则） | 建立缺省承载+按需专有承载，下发QoS到UDG |
| 更新 | CCR-U或RAR | CCA-U或RAA（携带QoS变更规则） | 承载QoS修改/新建/删除（带宽变更） |
| 终止 | CCR-T | CCA-T | 删除所有承载和QoS规则 |

### 2.7 专有承载管理（QoS保障的核心机制）

专有承载是带宽控制中GBR保障的核心机制：

| 操作 | 触发条件 | 方向 | 带宽控制影响 |
|------|----------|------|------------|
| 专有承载激活 | PCRF下发新GBR QoS规则 | PCRF→UNC→UDG | 为特定业务流分配专用带宽（GBR） |
| 专有承载更新 | 规则QoS/ARP变化 | PCRF→UNC→UDG | 带宽变更（升速/降速/优先级调整） |
| 专有承载去激活 | 规则去激活/删除 | PCRF→UNC→UDG | 释放专用带宽资源 |

### 2.8 PCRF/PCF冗余与负荷分担

| 模式 | 说明 | 适用场景 |
|------|------|----------|
| 主备模式 | 主用PCRF故障时切换到备用 | 高可靠性场景 |
| 轮询模式 | 按轮询方式分配会话 | 简单负荷分担 |
| 百分比模式 | 按配置权重分配会话 | 精细化负荷分担 |

PCRF组（PCRFGROUP）用于管理冗余和负荷分担。5G N7接口支持GROUPID或PRIORITY两种负荷分担模式。

### 2.9 迟滞时间

规则激活/去激活时间切换的迟滞时间，默认10分钟。用于避免带宽控制规则在短时间内频繁切换激活状态（如用量阈值附近的抖动）。

### 2.10 PCF发现与选择（5G）

**AMF侧PCF发现：**
- 从旧AMF获取PCF信息（切换场景）
- 本地配置（AMFPCFSELPARAM）
- 通过NRF查询

**SMF侧PCF选择因素：**
- AMF提供的PCF信息（首选）
- 本地策略配置
- NRF查询
- 选择维度：SUPI号段、DNN、S-NSSAI、SUPI范围（PCF Serving Scope）

### 2.11 接口模式选择（5G N7 vs 2/3/4G Gx）

当同一UNC同时支持5G和4G用户时，接口模式选择优先级：
1. **PCF实例级**：通过ADD PCCCHGMODEBYPCFID配置，指定PCF实例使用N7。
2. **APN/DNN级**：通过ADD APNPOLICYMODE配置，指定APN使用Gx或N7。
3. **全局级**：通过SET POLICYMODE配置默认接口模式。

---

## 3. 原理与流程

### 3.1 带宽控制策略下发链路（核心原理）

PCC在带宽控制中的核心原理是将PCRF/PCF的QoS决策传递到用户面：

```
[2G/3G/4G]
PCRF ──CCA-I/CCA-U/RAR──> UNC(PGW-C/GGSN)
                              │
                              ├── N4/PFCP ──> UDG(UPF/PGW-U)：QoS Enforcement
                              │                 ├── MBR限速
                              │                 ├── GBR保障
                              │                 ├── Gate门控
                              │                 └── 重定向

[5G]
PCF ──N7 SM Policy Response/Update──> UNC(SMF)
                                        │
                                        ├── N4/PFCP ──> UDG(UPF)：QoS Enforcement
                                        │                 ├── Session-AMBR限速
                                        │                 ├── PCC Rule QoS（5QI/MBR/GBR）
                                        │                 ├── Gate门控
                                        │                 └── 重定向
```

### 3.2 QoS映射（2G/3G/4G Gx）

Gx接口支持GPRS/UMTS QoS与EPC QoS的映射，决定了用户面的实际带宽控制行为：

| GPRS/UMTS参数 | EPC Gx AVP | 带宽控制含义 |
|---------------|-----------|------------|
| Traffic Class | QoS-Class-Identifier (QCI) | QoS转发处理类 |
| Maximum Bit Rate (UL/DL) | Maximum-Requested-Bandwidth-UL/DL | APN级最大带宽 |
| Guaranteed Bit Rate (UL/DL) | Guaranteed-Bitrate-UL/DL | 业务流保证带宽 |
| Delivery Order | 不直接映射 | 通过QCI间接表达 |
| Maximum SDU Size | 不直接映射 | 通过QCI间接表达 |
| SDU Error Ratio | 不直接映射 | 通过QCI间接表达 |
| ARP | Allocation-Retention-Priority | 带宽分配优先级与抢占 |

### 3.3 2G/3G/4G Gx接口信令流程

#### 3.3.1 IP-CAN会话建立（初始QoS下发）

```
UE → GGSN/PGW-C(UNC) → PCRF
1. 用户发起PDP/PDN激活
2. UNC发送CCR-I到PCRF（携带IMSI、APN、UE-IP、RAT-Type、默认QoS等）
3. PCRF返回CCA-I（携带PCC规则、Event Triggers、QoS参数[QCI/MBR/GBR/ARP]）
4. UNC将QoS规则通过N4下发到UDG，建立缺省承载
5. UDG按QoS参数执行带宽控制（限速、整形）
```

#### 3.3.2 IP-CAN会话更新（带宽变更触发）

两种触发方式：

**UNC主动上报（CCR-U）**：
- Event Trigger条件满足（如USAGE_REPORT用量达到阈值），UNC发送CCR-U到PCRF
- PCRF根据用量/事件返回新的QoS规则（如降速、提速）
- UNC将新QoS下发UDG执行

**PCRF主动推送（RAR）**：
- PCRF发送Re-Auth-Request到UNC，携带新的QoS规则（如带宽提速/降速）
- UNC响应RAA，将新QoS下发UDG执行

#### 3.3.3 IP-CAN会话终止

```
1. 用户去激活
2. UNC发送CCR-T到PCRF
3. PCRF返回CCA-T
4. UNC通知UDG删除所有QoS规则和承载
```

#### 3.3.4 Supported Features动态协商

Gx接口支持能力协商：
1. CCR-I中携带Supported-Features AVP
2. CCA-I中PCRF返回支持的Feature列表
3. 双方取交集确定可用Feature
4. 通过ADD PCRF命令配置Supported-Features动态协商开关和Feature列表

### 3.4 5G策略偶联流程

#### 3.4.1 AM策略偶联

**建立流程：**
1. UE注册到AMF
2. AMF发送Npcf_AMPolicyControl_Create Request到PCF（携带SUPI、GPSI、接入类型、PEI等）
3. PCF返回Npcf_AMPolicyControl_Create Response（携带SAR策略、RFSP Index等）
4. AMF通知RAN/UE

**修改流程（三种触发场景）：**
- 触发条件满足（如位置变化、RFSP变化）— AMF发送UpdateNotify到PCF
- AMF变化（可复用原PCF）— 新AMF发送PolicyUpdate到PCF
- PCF策略变化 — PCF通过UpdateNotify通知AMF

**终止流程：**
- UE去注册、PCF变更、PCF主动终止

#### 3.4.2 UE策略偶联

**建立流程：**
1. AMF发送Npcf_UEPolicyControl_Create Request到PCF
2. PCF返回Response（携带ANDSP、URSP策略）
3. AMF通过MANAGE UE POLICY COMMAND下发到UE

**修改流程：**与AM策略类似，三种触发场景。

**终止流程：**Npcf_UEPolicyControl_Delete Request/Response。

#### 3.4.3 SM策略偶联（带宽控制核心流程）

**建立流程：**
1. UE发起PDU会话建立
2. SMF发送Npcf_SMPolicyControl_Create Request到PCF（携带SUPI、DNN、S-NSSAI、UE-IP等）
3. PCF返回Response（携带Session Rules + PCC Rules）
4. SMF将QoS规则通过N4下发到UPF执行

**SM策略内容（带宽控制关键参数）：**
- **Session Rules**：Session-AMBR（PDU会话聚合最大比特率）、缺省QoS（5QI/ARP）
- **PCC Rules**：SDF模板（业务流过滤）、QoS参数（5QI/ARP/GBR/MBR）、门控状态（Open/Closed）、计费参数

### 3.5 Event Triggers / PCR Triggers（带宽变更事件驱动）

Event Triggers和PCR Triggers是触发PCRF/PCF重新下发QoS决策的机制，是动态带宽控制的关键驱动。

#### 3.5.1 Gx接口Event Triggers（2/3/4G）与带宽控制

| Event Trigger ID | 描述 | 带宽控制关联 |
|-----------------|------|------------|
| QOS_CHANGE | QoS变化 | 直接触发带宽调整 |
| USAGE_REPORT | 使用量报告 | FUP用量阈值触发降速/提速 |
| SGSN_CHANGE | SGSN变化 | 可能触发QoS重新协商 |
| RAI_CHANGE | 路由区变化 | 位置相关QoS策略 |
| TAI_CHANGE | 跟踪区变化 | 位置相关QoS策略 |
| ECGI_CHANGE | ECGI变化 | 位置相关QoS策略 |
| RAT_CHANGE | RAT类型变化 | 不同接入类型QoS差异化 |
| USER_LOCATION_CHANGE | 用户位置变化 | 位置相关QoS策略 |
| UE_IP_CHANGE | UE IP变化 | 重新下发QoS规则 |
| DEFAULT_EPS_BEARER_QOS_CHANGE | 缺省承载QoS变化 | 缺省带宽变更 |
| AN_GW_CHANGE | 接入网关变化 | 可能影响QoS保障能力 |
| RESOURCE_MODIFICATION_REQUEST | 资源修改请求 | UE请求专用带宽 |
| PLMN_CHANGE | PLMN变化 | 漫游QoS策略 |
| MAX_MBR_CHANGED | 最大MBR变化 | APN-AMBR带宽上限变更 |
| REMOVE_MBR_ENFORCEMENT | 移除MBR执行 | 取消带宽限制 |
| REVALIDATION_TIMEOUT | 重验证超时 | 触发策略重评估 |

#### 3.5.2 N7接口PCR Triggers（5G SMF）与带宽控制

5G SM策略支持25+种PCR Triggers，关键带宽控制触发器：

| PCR Trigger | 描述 | 带宽控制关联 |
|-------------|------|------------|
| USAGE_REPORT | 使用量报告 | FUP用量阈值触发QoS变更 |
| QOS_NOTIF | QoS通知 | QoS Flow级QoS变更 |
| QOS_CHANGE | QoS变化 | 直接触发带宽调整 |
| SUCCESS_HANDOVER | 切换成功 | 可能触发QoS重新评估 |
| FAIL_REPORT | 失败报告 | QoS Flow建立失败 |
| RATE_LIMITS_CHANGE | 速率限制变化 | SM调度限速变化 |
| PLMN_CH | PLMN变化 | 漫游QoS策略 |
| CON_STATE_CH | 连接状态变化 | 空闲/连接态QoS差异 |
| ACC_STATE_CH | 接入状态变化 | 接入类型QoS差异 |
| LOC_CH | 位置变化 | 位置相关QoS策略 |
| PRA_CH | PRA变化 | Presence Reporting Area |
| SERV_AREA_CH | 服务区变化 | 服务区域QoS策略 |
| RFSP_CH | RFSP变化 | RAT/频段选择优先级 |
| ALLOWED_NSSAI_CH | 允许NSSAI变化 | 网络切片QoS |

#### 3.5.3 N15接口PCR Triggers（5G AMF）

AMF侧PCR Triggers：LOC_CH、PRA_CH、SERV_AREA_CH、RFSP_CH、ALLOWED_NSSAI_CH。

### 3.6 Gx Failover功能

#### 3.6.1 基本Failover

**前提条件：**
- PCRF配置为主备或负荷分担模式
- UNC本地支持Failover
- PCRF间使用相同的LOCALHOSTNAME（同一Diameter链路组）
- PCRF支持CC-Session-Failover AVP
- PCRF支持热备（Hot Standby）

**触发机制：**
1. UNC发送Diameter消息后启动Tx定时器
2. Tx定时器超时未收到响应
3. UNC切换到备用PCRF重新发送

**配置命令：**
- ADD PCRF（配置PCRF信息）
- ADD PCRFGROUP（FAILOVERSW=ENABLE）
- SET PCCTIMER（APPRETRYTIMEOUT参数）
- SET PCCMSGATTR（消息属性配置）

#### 3.6.2 增强Failover（BIT1202）

当PCRF不支持热备时，启用增强Failover：
- 备用PCRF从CCR-U消息重建会话
- 软参配置：SET SMFSOFTPARA（BIT1202=1）
- 适用于非热备PCRF的场景

### 3.7 QoS能力开放功能

UNC通过私有Restif接口提供QoS能力开放：
- **功能**：SBC通过HTTP接口向UNC查询用户的PCRF ID
- **接口**：Restif接口（HTTP/BSF方式）
- **协议**：HTTP/1.1
- **交互**：queryPCRFRequest / queryPCRFResponse消息

### 3.8 N7 Failover（5G）

5G N7接口Failover机制：
- PCF主备配置
- 支持GROUPID或PRIORITY两种负荷分担模式
- Failover仅尝试一次
- 失败后按SET PCCFAILACTION配置处理

### 3.9 异常处理

#### 3.9.1 PENDING_TRANSACTION处理（5G N7）

- PCF返回PENDING_TRANSACTION（400错误码）
- SMF根据SET PCCTIMER的PENDRETRYTIMES和PENDRETRYTIMER参数重试
- 重试次数耗尽后按SET PCCFAILACTION处理

#### 3.9.2 回退到本地PCC（5G）

- SMF发送DEA SMCTX消息到UPF，携带FAIL_HANDLE_TYPE=PCC_ROLLBACK
- UPF收到后按本地PCC规则处理
- 回退后按SET PCCFAILACTION的在线保持时间配置决定是否允许新用户上线

#### 3.9.3 Gx接口异常处理（2/3/4G）

7种异常场景通过SET PCCFAILACTION和ADD RESULTCODECTRL配置处理策略：

| 异常场景 | 典型处理策略 | 带宽控制影响 |
|----------|------------|------------|
| PCRF无响应 | 回退到本地PCC或拒绝 | 回退后按本地QoS规则执行或拒绝用户 |
| PCRF返回失败 | 根据Result-Code配置处理 | 可能降级或维持当前QoS |
| 链路中断 | Failover到备用PCRF | QoS策略可能短暂中断 |
| 规则安装失败 | 拒绝用户或降级处理 | 用户可能无法获得请求的带宽 |
| CCR-U发送失败 | 保持当前策略或回退 | 当前QoS保持不变或回退 |
| 规则更新失败 | 保持或回退 | 当前QoS保持不变或回退 |
| 资源不足 | 拒绝或降级 | 无法分配请求的带宽资源 |

**SET FHBYPASS（紧急旁路）**：
- 最高优先级的故障旁路处理
- 必须获得客户书面授权后才能启用
- 启用后所有PCC用户按非PCC方式处理（无QoS控制）

---

## 4. 配置规则

### 4.1 PCC使能层级（2/3/4G Gx）

PCC功能使能分三个层级，上层开关控制下层是否生效：

| 层级 | 命令 | 说明 | 带宽控制影响 |
|------|------|------|------------|
| 全局 | SET PCCFUNC | 控制Home/Roam/Visit用户的PCC开关 | 全局启用/禁用QoS策略控制 |
| APN | SET APNPCCFUNC | 控制特定APN的PCC开关 | 按APN粒度启用QoS控制 |
| 号段 | ADD GLBPCRFGROUP | 控制特定号段使用的PCRF组 | 按号段分配PCRF进行QoS决策 |

### 4.2 PCRF组选择优先级（2/3/4G Gx）

| 优先级 | 来源 | 命令 | 说明 |
|--------|------|------|------|
| 1（最高） | APN绑定 | ADD PCRFGRPBNDAPN | 指定APN使用的PCRF组 |
| 2 | 号段绑定 | ADD GLBPCRFGROUP | 指定号段使用的PCRF组 |
| 3（最低） | 全局缺省 | SET DFTGLBPCRFGRP | 全局缺省PCRF组 |

### 4.3 动态PCC配置流程（2/3/4G Gx）

```
步骤1：License配置
  LST LICENSESWITCH → SET LICENSESWITCH（LKV3W9SPCC11）

步骤2：基础数据配置
  ADD IMSIMSISDNSEG（IMSI/MSISDN号段）

步骤3：PCRF对接配置
  ADD PCRF → ADD PCRFGROUP → ADD PCRFBINDGRP → SET DFTGLBPCRFGRP

步骤4：PCC功能使能
  SET PCCFUNC（使能Home/Roam/Visit）

步骤5：APN级配置
  ADD PCRFGRPBNDAPN → SET APNPCCFUNC

步骤6：预定义规则配置（可选）
  ADD RULE → ADD RULEBINDDNAI（规则绑定DNAI）

步骤7：预定义规则组配置（可选）
  ADD USERPROFILE → ADD RULEBINDING → ADD USRPROBINDDNAI（UserProfile绑定DNAI）
```

### 4.4 本地PCC配置流程（2/3/4G Gx）

当无PCRF部署时，使用本地静态规则实现固定带宽控制：

```
步骤1：License配置
步骤2：关闭动态PCC
  SET PCCFUNC（DISABLE所有开关）
步骤3：PCC模板配置
  ADD PCCTEMPLATE（INITIALFAILACT=FORBIDDEN）
步骤4：APN级配置
  SET APNPCCFUNC
步骤5：QoS映射
  ADD QOSPROP
步骤6：策略组配置
  ADD PCCPOLICYGRP
步骤7：规则配置（定义带宽控制参数）
  ADD RULE（包含QCI/MBR/GBR/ARP/Gate等QoS参数）
步骤8：UserProfile配置
  ADD USERPROFILE → ADD RULEBINDING
步骤9：用户模板组配置
  ADD USRPROFGROUP → ADD UPBINDUPG → ADD APNUSRPROFG
步骤10（可选）：多UserProfile安装
  ADD PCCPBINDUPG
```

### 4.5 与PCRF对接数据配置（2/3/4G Gx）

#### 4.5.1 标准场景（不同PGW-U用户IP）

```
VPN配置 → SET CONCENPOINT → ADD LOGICINF → ADD DIAMLOCINFO
→ ADD PCRF → ADD DIAMPEERADDR → ADD DIAMCONNGRP → ADD DIAMCONNECTION
```

#### 4.5.2 用户IP重叠场景

当多个PGW-U的用户IP存在重叠时，需要额外配置：
- ADD LOCALHOSTGRP（本端主机组）
- ADD LOCALHOSTBIND（本端主机绑定）
- ADD GXUPFGROUP（Gx UPf组）
- ADD UPFBINDGXUPFGRP（UPF绑定Gx UPf组）
- ADD UPFGLOCGBNDGRP（UPF组绑定本端主机组）
- ADD UPFGBINDLOCG（UPF组绑定本端主机组）

### 4.6 5G AMF配置流程

```
步骤1：License配置
  LST LICENSESWITCH → SET LICENSESWITCH（LKV2PCCBF01）

步骤2：PCF选择策略
  ADD PCFSELPLCY

步骤3：AM/UE策略控制
  ADD AMUEPLCYCTRL →（可选）MOD AMUEPLCYCTRL

步骤4：AMF策略功能
  SET AMFPLCYFUNC

步骤5：NGMM用户数据
  ADD NGMMSUBDATA

步骤6：AMF对等选择功能
  SET AMFPEERSELFUNC
```

### 4.7 5G SMF配置流程

```
步骤1：License配置
  LST LICENSESWITCH → SET LICENSESWITCH（LKV3W9SPCC11）

步骤2：PCC功能使能
  SET PCCFUNC

步骤3：N7消息属性控制
  SET N7RCVATTRCTRL → SET N7SNDATTRCTRL

步骤4：PCC模板
  ADD PCCTEMPLATE

步骤5：APN级配置
  SET APNPCCFUNC

步骤6（可选）：预定义规则和策略组
  ADD PCCPOLICYGRP → ADD RULE → ADD USERPROFILE

步骤7：用户模板组
  ADD USRPROFGROUP → ADD APNUSRPROFG

步骤8（可选）：接口模式选择
  SET POLICYMODE → ADD APNPOLICYMODE → ADD PCCCHGMODEBYPCFID

步骤9（可选）：PCF Serving Scope
  ADD PCFSSCOPE → ADD USRTAIRANGE → ADD PCFSSCOPEBIND
```

### 4.8 异常场景配置（2/3/4G Gx）

```
步骤1：配置异常处理策略
  SET PCCFAILACTION（全局异常处理策略）

步骤2：配置返回码控制
  ADD RESULTCODECTRL（按Result-Code配置处理方式）

步骤3（可选）：配置紧急旁路
  SET FHBYPASS（需客户书面授权）
```

### 4.9 QoS能力开放配置

```
步骤1：VPN和IP配置
  ADD VPNINST → ADD LOGICIP

步骤2：HTTP链路配置
  ADD HTTPLEGRP → ADD HTTPLE（CLIENT+SERVER）

步骤3：SBI应用配置
  ADD SBIAPLE（NFType=BSF）

步骤4：HTTP协议配置
  SET HTTPCONF（HTTP1.1）

步骤5：功能开关
  SET SMCOMMFUNC（PCRFQRYSW=ENABLE）
```

### 4.10 Gx Failover配置

```
步骤1：PCRF配置
  ADD PCRF（配置主备PCRF）

步骤2：PCRF组配置
  ADD PCRFGROUP（FAILOVERSW=ENABLE）

步骤3：定时器配置
  SET PCCTIMER（APPRETRYTIMEOUT）

步骤4（可选）：增强Failover
  SET SMFSOFTPARA（BIT1202=1）

步骤5：消息属性配置
  SET PCCMSGATTR
```

---

## 5. 配置案例

### 案例1：2G/3G/4G动态PCC带宽控制基本配置

**场景**：PGW-C通过Gx接口连接2个PCRF（主备模式），为Home用户启用PCC带宽控制。PCRF下发的QoS规则包含MBR/GBR/QCI参数，由UDG执行限速。

```
// 1. License使能
SET LICENSESWITCH:LICITEM="LKV3W9SPCC11",SWITCH=ENABLE;

// 2. 集中点模式
SET CONCENPOINT:MODE=CONCENTRATION;

// 3. 逻辑接口
ADD LOGICINF:NAME="gxif1/0/0",IPV4ADDR1="10.8.10.1",IPV4MASK1="255.255.255.255",VPNNAME="vpn_gxif";

// 4. Diameter本端信息
ADD DIAMLOCINFO:LOCALHOST="pgw_1",LOCALREALM="huawei.com";

// 5. PCRF配置
ADD PCRF:HOSTNAME="pcrf_1",REALM="example.com";
ADD PCRF:HOSTNAME="pcrf_2",REALM="example.com";

// 6. PCRF对端地址
ADD DIAMPEERADDR:PEERHOSTNAME="pcrf_1",PEERADDR="10.11.21.59";
ADD DIAMPEERADDR:PEERHOSTNAME="pcrf_2",PEERADDR="10.11.21.60";

// 7. Diameter链路组和链路
ADD DIAMCONNGRP:GROUPNAME="gx_grp";
ADD DIAMCONNECTION:CONNNAME="gx_conn_1",GROUPNAME="gx_grp",LOCALHOST="pgw_1",PEERHOSTNAME="pcrf_1";
ADD DIAMCONNECTION:CONNNAME="gx_conn_2",GROUPNAME="gx_grp",LOCALHOST="pgw_1",PEERHOSTNAME="pcrf_2";

// 8. PCRF组（主备模式，开启Failover保障QoS决策链路可靠性）
ADD PCRFGROUP:PCRFGRPNAME="pcrf_group_1",SHAREMODE=MASTER_SLAVE,FAILOVERSW=ENABLE;
ADD PCRFBINDGRP:PCRFGRPNAME="pcrf_group_1",HOSTNAME="pcrf_1",PERCENTAGE=100;
ADD PCRFBINDGRP:PCRFGRPNAME="pcrf_group_1",HOSTNAME="pcrf_2",PERCENTAGE=0;
SET MASTERPCRF:PCRFGRPNAME="pcrf_group_1",HOSTNAME="pcrf_1";

// 9. 全局缺省PCRF组
SET DFTGLBPCRFGRP:PCRFGRPNAME="pcrf_group_1";

// 10. PCC功能使能（启用Home用户PCC，激活PCRF QoS决策通道）
SET PCCFUNC:HOMESWITCH=ENABLE;

// 11. PCC模板（初始失败禁止，保障QoS策略必须成功下发）
ADD PCCTEMPLATE:TEMPLATENAME="pcc_tpl_1",INITIALFAILACT=FORBIDDEN;
SET APNPCCFUNC:APN="pccnet",PCCSWITCH=ENABLE,TEMPLATENAME="pcc_tpl_1";
```

### 案例2：5G SMF动态PCC带宽控制配置

**场景**：SMF通过N7接口连接PCF，为DNN启用5G PCC。PCF通过SM策略下发Session-AMBR和PCC Rules（含5QI/MBR/GBR），控制PDU会话和业务流级带宽。

```
// 1. License使能
SET LICENSESWITCH:LICITEM="LKV3W9SPCC11",SWITCH=ENABLE;

// 2. PCC功能使能
SET PCCFUNC:HOMESWITCH=ENABLE;

// 3. N7消息属性控制
SET N7RCVATTRCTRL:...;
SET N7SNDATTRCTRL:...;

// 4. PCC模板
ADD PCCTEMPLATE:TEMPLATENAME="sm_pcc_tpl",INITIALFAILACT=FORBIDDEN;

// 5. DNN级配置
SET APNPCCFUNC:APN="internet",PCCSWITCH=ENABLE,TEMPLATENAME="sm_pcc_tpl";

// 6. 全局接口模式（5G使用N7）
SET POLICYMODE:POLICYMODE=N7;

// 7. 预定义规则（可选，定义固定带宽套餐的QoS参数）
ADD RULE:RULENAME="rule_video_100m",PRIORITY=10;
ADD PCCPOLICYGRP:POLICYGRPNAME="policy_grp_1";
```

### 案例3：本地PCC带宽控制配置（无PCRF）

**场景**：未部署PCRF，PGW-C使用本地静态规则实现固定带宽分配。规则中包含QCI、MBR、GBR等QoS参数，直接由UDG执行限速。

```
// 1. License使能
SET LICENSESWITCH:LICITEM="LKV3W9SPCC11",SWITCH=ENABLE;

// 2. 关闭动态PCC（不连接PCRF）
SET PCCFUNC:HOMESWITCH=DISABLE,ROAMSWITCH=DISABLE,VISITSWITCH=DISABLE;

// 3. PCC模板
ADD PCCTEMPLATE:TEMPLATENAME="local_tpl",INITIALFAILACT=FORBIDDEN;

// 4. APN配置
SET APNPCCFUNC:APN="internet",PCCSWITCH=DISABLE,TEMPLATENAME="local_tpl";

// 5. QoS映射（定义QCI到实际QoS参数的映射）
ADD QOSPROP:...;

// 6. 策略组
ADD PCCPOLICYGRP:POLICYGRPNAME="local_policy_grp";

// 7. 规则（定义带宽控制QoS参数：QCI、MBR-UL/DL、GBR-UL/DL、ARP、Gate）
ADD RULE:RULENAME="local_rule_1",PRIORITY=10;

// 8. UserProfile（将规则打包到用户模板）
ADD USERPROFILE:PROFILENAME="profile_1";
ADD RULEBINDING:PROFILENAME="profile_1",RULENAME="local_rule_1";

// 9. 用户模板组
ADD USRPROFGROUP:GROUPNAME="user_grp_1";
ADD UPBINDUPG:GROUPNAME="user_grp_1",PROFILENAME="profile_1";
ADD APNUSRPROFG:APN="internet",GROUPNAME="user_grp_1";
```

### 案例4：PCRF负荷分担配置（高并发带宽控制）

**场景**：2个PCRF按40:60比例负荷分担，支持大规模用户的QoS策略决策。

```
ADD PCRFGROUP:PCRFGRPNAME="pcrf_group_1",SHAREMODE=PERCENTAGE;
ADD PCRFBINDGRP:PCRFGRPNAME="pcrf_group_1",HOSTNAME="pcrf_1",PERCENTAGE=40;
ADD PCRFBINDGRP:PCRFGRPNAME="pcrf_group_1",HOSTNAME="pcrf_2",PERCENTAGE=60;
SET DFTGLBPCRFGRP:PCRFGRPNAME="pcrf_group_1";
```

### 案例5：异常处理配置（带宽控制容灾）

**场景**：当PCRF故障时，回退到本地PCC规则，保障基本带宽控制不中断。

```
// 1. 异常处理策略（PCRF故障时回退本地PCC，保持在线用户3600秒）
SET PCCFAILACTION:FAILACTION=ROLLBACK_LOCAL,ONLINEHOLDTIME=3600;

// 2. Failover ALL（指定时间后全部Failover到备用PCRF）
SET PCCFAILACTION:FAILACTION=FAILOVER_ALL,DURATIONTIMER=300;

// 3. 返回码控制（指定Result-Code对应的处理策略）
ADD RESULTCODECTRL:RESULTCODE=5012,ACTION=ROLLBACK_LOCAL;

// 4. 紧急旁路（需书面授权，仅在极端故障时使用，跳过所有QoS控制）
SET FHBYPASS:SWITCH=ENABLE;
```

---

## 6. 验证与调测

### 6.1 验证PCRF链路状态（2/3/4G）

```
// 查询PCRF状态
DSP PCRFSTATUS:PCRFNAME="pcrf_1";

// 期望输出：
// PCRF主机名  =  pcrf_1
// POD名称     =  uncpod-0
// 本端地址    =  10.8.10.1:16400
// 对端地址    =  10.11.21.59:3868
// Gx 状态    =  Normal
// 本端主机名  =  pgw_1
```

### 6.2 验证PCRF配置

```
// 查询PCRF信息
LST PCRF:HOSTNAME="pcrf_1";

// 查询PCRF组
LST PCRFGROUP:PCRFGRPNAME="pcrf_group_1";

// 查询PCRF绑定
LST PCRFBINDGRP:PCRFGRPNAME="pcrf_group_1";
```

### 6.3 验证Gx接口配置

```
// 查询逻辑接口
LST LOGICINF:;

// 查询Diameter本端信息
LST DIAMLOCINFO:;
```

### 6.4 验证PCC业务（2/3/4G）与QoS下发

```
// 1. 查询License
LST LICENSESWITCH:LICITEM="LKV3W9SPCC11";

// 2. OM Portal建立用户跟踪
// 3. 激活用户，跟踪消息
// 4. 检查CCR-I/CCA-I消息内容，特别关注QoS参数（QCI、MBR、GBR、ARP）

// 5. 查询PCC会话信息
DSP PCCSESSINFO:IMSI="460000123456789";

// 6. 查询PCRF组状态
DSP PCRFGRPSTATUS:PCRFGRPNAME="pcrf_group_1";

// 7. 查询APN PCC配置
LST APNPCCFUNC:APN="pccnet";

// 8. 查询APN绑定的PCRF组
LST PCRFGRPBNDAPN:APN="pccnet";
```

### 6.5 验证PCRF负荷分担

```
// 1. 激活大量PCC用户
// 2. 使用U2020/MAE客户端查看"PCC发送CCR-I消息数(PCRF)"指标
// 3. 验证各PCRF的CCR-I消息比例与配置一致

// 异常排查：
DSP PCRFSTATUS:PCRFNAME="pcrf_1";
DSP PCRFSTATUS:PCRFNAME="pcrf_2";
LST PCRFGROUP:PCRFGRPNAME="pcrf_group_1";
LST PCRFBINDGRP:PCRFGRPNAME="pcrf_group_1";
```

### 6.6 验证5G PCC与QoS下发

```
// 1. 添加测试PCF绑定
ADD TSTPCFBINDING:...;

// 2. 删除SM上下文触发重新建立
DEA SMCTX:...;

// 3. 用户激活后查询PDU会话和QoS Flow信息
DSP PDUSESSION:IMSI="460000123456789";
DSP PCCSESSINFO:IMSI="460000123456789";

// 4. 检查N7 SM Policy Response中的QoS参数（5QI、Session-AMBR、PCC Rule QoS）

// 5. 清理测试绑定
RMV TSTPCFBINDING:...;
```

### 6.7 验证QoS能力开放

```
// 1. OM Portal建立用户跟踪
// 2. 激活用户
// 3. 检查queryPCRFRequest/queryPCRFResponse消息
// 4. 验证local_addr和peer_addr与规划一致

// 异常排查：
LST SMCOMMFUNC:;  // 检查PCRFQRYSW是否开启
```

### 6.8 规则失败码（带宽控制故障诊断）

| 失败码 | 描述 | 可能原因 | 带宽控制影响 |
|--------|------|----------|------------|
| UNKNOWN_RULE_NAME | 未知规则名 | 规则未配置或名称不匹配 | QoS规则无法下发 |
| RATING_GROUP_ERROR | Rating Group错误 | 计费组配置错误 | 计费和QoS规则安装失败 |
| SERVICE_IDENTIFIER_ERROR | Service ID错误 | 业务标识配置错误 | 业务流QoS控制失败 |
| GW/PCEF_MALFUNCTION | 网关/PCEF故障 | 设备异常 | 所有QoS控制可能中断 |
| RESOURCES_LIMITATION | 资源不足 | 承载资源不足 | 无法分配请求的GBR带宽 |
| MAX_NR_BEARERS_REACHED | 最大承载数达到 | 承载数超限 | 无法建立新的QoS Flow |
| UNKNOWN_RULE_BASE_NAME | 未知规则组名 | UserProfile未配置 | 用户级带宽套餐无法生效 |
| RAT_GRANULARITY_MISMATCH | RAT粒度不匹配 | RAT配置错误 | QoS规则安装失败 |
| UNSUPPORTED_RULE_DATA | 不支持的规则数据 | 规则格式不兼容 | QoS规则安装失败 |
| RULE_EVENT_TRIGGER_ERROR | 事件触发错误 | Event Trigger配置错误 | 带宽变更事件无法触发 |
| RULE_CONDITIONS_ERROR | 规则条件错误 | 流过滤器配置错误 | 业务流匹配失败 |
| REQUESTED_RULE_NOT_APPLIED | 请求规则未应用 | 规则安装失败 | 请求的QoS未生效 |
| RULE_NOT_ADDED | 规则未添加 | 资源或配置不足 | QoS规则未安装 |
| TRIGGER_TYPE_ERROR | 触发类型错误 | 触发类型不支持 | 事件驱动QoS变更失败 |

### 6.9 告警处理

| 告警ID | 告警名称 | 处理建议 | 带宽控制影响 |
|--------|----------|----------|------------|
| ALM-81024 | PCRF无响应 | 检查PCRF状态、链路连通性、路由配置 | QoS策略决策链路中断 |
| ALM-100065 | 资源过载 | 检查系统资源使用情况 | QoS规则下发可能延迟或失败 |
| ALM-100066 | 资源拥塞 | 检查系统资源使用情况，考虑扩容 | QoS规则下发可能失败 |

---

## 7. 参考信息

### 7.1 核心MML命令清单（2/3/4G Gx）

| 命令 | 功能 | 配置对象 | 带宽控制用途 |
|------|------|----------|------------|
| SET CONCENPOINT | 设置集中点部署模式 | 基础参数 | Gx接口基础配置 |
| ADD LOGICINF | 增加逻辑接口 | Gx接口 | QoS信令传输接口 |
| ADD DIAMLOCINFO | 增加Diameter本端信息 | Diameter连接 | Gx传输层 |
| ADD DIAMPEERADDR | 增加Diameter对端地址 | Diameter连接 | Gx传输层 |
| ADD DIAMCONNGRP | 增加Diameter链路组 | Diameter连接 | Gx链路管理 |
| ADD DIAMCONNECTION | 增加Diameter链路 | Diameter连接 | Gx链路管理 |
| ADD PCRF | 增加PCRF | PCRF Diameter连接 | QoS决策来源配置 |
| ADD PCRFGROUP | 增加PCRF组 | PCRF Diameter连接 | QoS决策冗余/负荷分担 |
| ADD PCRFBINDGRP | 增加PCRF与PCRF组的关联 | PCRF Diameter连接 | PCRF组内权重 |
| SET MASTERPCRF | 设置主用PCRF | PCRF Diameter连接 | 主备模式主用PCRF |
| ADD GLBPCRFGROUP | 增加全局PCRF组绑定 | PCRF Diameter连接 | 号段级PCRF选择 |
| SET DFTGLBPCRFGRP | 设置全局缺省PCRF组 | PCRF Diameter连接 | 缺省QoS决策来源 |
| ADD PCRFGRPBNDAPN | 增加APN和PCRF组关联 | PCRF Diameter连接 | APN级PCRF选择 |
| SET PCCFUNC | 设置PCC功能 | PCC公共参数 | 全局QoS策略控制开关 |
| SET PCCFAILACTION | 设置PCC故障处理 | PCC公共参数 | QoS决策链路故障容灾 |
| SET PCCTIMER | 设置PCC定时器 | 信令控制 | QoS信令重试/超时控制 |
| ADD RESULTCODECTRL | 增加返回码控制 | 信令控制 | 按返回码处理QoS策略失败 |
| ADD PCCTEMPLATE | 增加PCC模板 | PCC模板 | QoS策略模板 |
| SET APNPCCFUNC | 设置APN PCC功能 | APN控制 | APN级QoS策略开关 |
| ADD RULE | 增加规则 | 规则 | **定义带宽控制QoS参数** |
| ADD RULEBINDDNAI | 增加预定义规则DNAI绑定 | DNAI绑定 | 规则下发目标 |
| ADD USERPROFILE | 增加用户模板 | 用户模板 | 用户级带宽套餐 |
| ADD RULEBINDING | 增加用户模板和规则绑定 | 规则绑定 | 绑定QoS规则到用户 |
| ADD USRPROFGROUP | 增加用户模板组 | 用户模板组 | 用户组级带宽控制 |
| ADD UPBINDUPG | 增加用户模板组和用户模板绑定 | 用户模板绑定 | 模板组与模板关联 |
| ADD APNUSRPROFG | 增加APN用户模板组绑定 | APN用户模板组绑定 | APN级带宽控制绑定 |
| ADD USRPROBINDDNAI | 增加用户模板DNAI绑定 | DNAI绑定 | 模板下发目标 |
| ADD IMSIMSISDNSEG | 增加IMSI和MSISDN号段 | 业务公共 | 号段配置 |
| ADD PCCPOLICYGRP | 增加PCC策略组 | 业务策略 | QoS策略组管理 |
| SET FHBYPASS | 设置失败旁路处理 | 失败旁路处理 | 紧急旁路（跳过QoS控制） |

### 7.2 核心MML命令清单（5G AMF）

| 命令 | 功能 | 带宽控制用途 |
|------|------|------------|
| ADD GUAMI | 增加GUAMI | AMF标识 |
| ADD PCFSELPLCY | 增加PCF选择策略 | AM策略PCF发现 |
| ADD AMUEPLCYCTRL | 增加AM/UE策略控制 | AM/UE策略控制开关 |
| MOD AMUEPLCYCTRL | 修改AM/UE策略控制 | 修改策略控制参数 |
| SET AMFPLCYFUNC | 设置AMF策略功能 | AMF策略功能开关 |
| ADD NGMMSUBDATA | 增加NGMM用户数据 | 用户数据配置 |
| SET AMFPEERSELFUNC | 设置AMF对等选择功能 | AMF对等选择 |

### 7.3 核心MML命令清单（5G SMF）

| 命令 | 功能 | 带宽控制用途 |
|------|------|------------|
| SET PCCFUNC | 设置PCC功能 | 全局QoS策略控制开关 |
| ADD PCCTEMPLATE | 增加PCC模板 | QoS策略模板 |
| SET APNPCCFUNC | 设置APN PCC功能 | DNN级QoS策略开关 |
| SET N7RCVATTRCTRL | 设置N7接收消息属性控制 | N7消息接收属性 |
| SET N7SNDATTRCTRL | 设置N7发送消息属性控制 | N7消息发送属性 |
| SET POLICYMODE | 设置接口模式 | N7/Gx接口模式选择 |
| ADD APNPOLICYMODE | 增加APN接口模式 | APN级接口模式 |
| ADD PCCCHGMODEBYPCFID | 增加PCF实例级接口模式 | PCF实例级接口模式 |
| ADD PCFSSCOPE | 增加PCF Serving Scope | PCF服务范围 |
| ADD USRTAIRANGE | 增加用户TAI范围 | TAI范围配置 |
| ADD PCFSSCOPEBIND | 增加PCF Serving Scope绑定 | Scope绑定 |

### 7.4 关键软参（2/3/4G Gx）

| 软参 | 功能 | 说明 | 带宽控制影响 |
|------|------|------|------------|
| BYTE68 | 控制号段匹配位数 | UserProfile选择时的号段匹配精度 | 影响用户带宽套餐匹配 |
| BYTE589 | 控制Diameter协议故障倒换处理 | Diameter故障倒换增强 | 保障QoS信令链路可靠性 |
| BYTE654 | 控制PCC定制功能 | PCC定制功能开关 | 定制QoS行为 |
| BIT1790 | 控制MSISDN前缀剥离 | Gx/N7发送MSISDN时是否剥离965/00965前缀 | 影响用户标识 |
| BIT1854 | Private Extension传递ANSI | 通过Private Extension传递Access Network Switch Indication | 接入网信息传递 |
| STRING20 | 特殊Charging-Rule-Name | 传递ANSI的特殊规则名 | 特殊规则标识 |
| BIT1202 | Gx Failover增强 | 非热备PCRF的Failover增强 | 保障QoS决策链路高可用 |
| BIT1596 | X-HW-Session-Restoration AVP严格检查 | 控制是否严格检查该AVP | 会话恢复检查 |

### 7.5 关键软参（5G AMF）

| 软参 | 功能 |
|------|------|
| DWORD60 | AMF策略控制相关 |
| DWORD68/71/72 | AM/UE策略控制参数 |
| DWORD74/80 | AMF策略功能参数 |

### 7.6 测量指标

| 测量类别 | 说明 | 带宽控制关联 |
|----------|------|------------|
| Gx接口测量 | Gx接口消息统计（CCR/CCA/RAR/RAA等） | QoS策略信令量监控 |
| SMF策略控制测量 | 5G SM策略控制统计 | 5G QoS策略信令监控 |
| N7接口测量 | N7接口消息统计 | 5G QoS策略信令监控 |
| N15接口测量 | N15接口消息统计 | AM策略信令监控 |
| RESTful接口会话绑定测量 | QoS能力开放接口统计 | QoS能力开放监控 |
| PCC发送CCR-I消息数(PCRF) | 按PCRF统计CCR-I数量 | 负荷分担验证 |

### 7.7 与其他特性的关系

| 关联特性 | 关系类型 | 说明 |
|----------|----------|------|
| GWFD-020351 PCC基本功能（UDG） | 依赖 | UDG侧PCC用户面执行，本特性的QoS参数由UDG实际执行 |
| GWFD-110311 基于业务感知的带宽控制 | 协同 | 本特性提供PCRF动态QoS，SA提供本地业务感知QoS |
| GWFD-110312 基于业务累计流量的策略控制 | 协同 | FUP场景下，本特性上报USAGE_REPORT触发QoS变更 |
| GWFD-110313 基于智能Shaping的组级带宽控制 | 协同 | 本特性提供用户级QoS，Shaping提供组级整形 |
| GWFD-020353 基于累计流量的策略控制（UDG） | 协同 | UDG侧FUP，本特性上报用量后由PCRF下发新QoS |
| WSFD-104508 SCTP配置 | 依赖 | Diameter传输层依赖SCTP |

---

## 8. 知识来源

| 序号 | 文档标题 | 范围 | 来源路径 |
|------|----------|------|----------|
| 1 | 特性概述（2G/3G/4G） | 适用NF、License、规格、标准 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/特性概述_29056157.md |
| 2 | 实现原理（2G/3G/4G） | 规则类型、IP-CAN会话、专有承载、PCRF冗余、Event Triggers、QoS映射 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/实现原理_29056158.md |
| 3 | PCC基本功能（2G/3G/4G）参考信息 | MML命令、告警、软参、测量指标 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md |
| 4 | 配置动态PCC功能 | PCC使能层级、PCRF组选择、预定义规则 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/配置动态PCC功能_30805098.md |
| 5 | 配置本地PCC功能 | 无PCRF场景、本地规则配置流程 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/配置本地PCC功能_30805097.md |
| 6 | Gx Failover功能 | Failover原理、增强Failover、配置 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/Gx Failover功能_31422950.md |
| 7 | 配置QoS能力开放功能 | Restif接口、HTTP/BSF配置 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/配置QoS能力开放功能_48518810.md |
| 8 | 配置与PCRF对接数据 | VPN、Diameter链路、IP重叠场景 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/配置与PCRF对接数据_30805096.md |
| 9 | 配置异常场景数据 | 7种异常场景、SET PCCFAILACTION、SET FHBYPASS | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/配置异常场景数据_31422947.md |
| 10 | 调测PCC业务 | 验证流程、规则失败码 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/调测PCC基本功能/调测PCC业务_31422956.md |
| 11 | 调测PCRF负荷分担功能 | 负荷分担验证、指标查看 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/调测PCC基本功能/调测PCRF负荷分担功能_31422955.md |
| 12 | 调测QoS能力开放功能 | queryPCRF消息验证 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/调测PCC基本功能/调测QoS能力开放功能_84718093.md |
| 13 | 调测到PCRF的数据 | PCRF链路验证、配置检查 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/调测PCC基本功能/调测到PCRF的数据_31422954.md |
| 14 | PCC基本功能特性概述（5G） | AMF/SMF适用范围、5G策略类型、PCF发现 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/WSFD-109101 PCC基本功能特性概述（适用于5G）_71770359.md |
| 15 | 相关概念（5G） | AM/UE/SM策略详解、PCR Triggers | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/相关概念_71770360.md |
| 16 | AM策略偶联建立流程 | AMF→PCF Create流程 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/AM策略偶联建立流程_50510738.md |
| 17 | AM策略偶联修改流程 | 三种修改场景 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/AM策略偶联修改流程_50510739.md |
| 18 | AM策略偶联终止流程 | AM策略终止 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/AM策略偶联终止流程_50510740.md |
| 19 | UE策略偶联建立流程 | AMF→PCF Create→UE Config Update | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/UE策略偶联建立流程_50510744.md |
| 20 | UE策略偶联修改流程 | 三种修改场景 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/UE策略偶联修改流程_50510745.md |
| 21 | UE策略偶联终止流程 | UE策略终止 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/UE策略偶联终止流程_50510746.md |
| 22 | 异常处理流程（5G） | PENDING_TRANSACTION、回退本地PCC | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/异常处理流程_53323998.md |
| 23 | PCC基本功能（5G）参考信息 | AMF/SMF MML命令、告警、软参、测量 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/WSFD-109101 PCC基本功能（5G）参考信息_72466541.md |
| 24 | 激活PCC基本功能（5G） | AMF/SMF配置流程、接口模式选择、PCF Serving Scope | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/激活PCC基本功能_72467890.md |
| 25 | 调测PCC基本功能（5G） | 5G验证流程、TSTPCFBINDING | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/调测PCC基本功能_45059543.md |
