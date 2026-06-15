# Batch-22: UNC侧 5G Core FUP解决方案 - 业务级与会话级累计流量策略控制

> **来源**: UNC 产品文档 - 业务专题/5G Core FUP解决方案
> **覆盖**: 业务级累计流量策略控制（原理+配置+调测）+ 会话级累计流量策略控制（原理）
> **文件数**: 10 md
> **侧重点**: UNC（PGW-C/SMF）在FUP中的角色、配置流程、信令交互和系统约束

---

## 1. 概述

本批次文档来自UNC（Unified Core，融合核心网控制面）产品文档中"5G Core FUP解决方案"业务专题，涵盖两个子专题共10个md文件：

- **业务级累计流量策略控制**（7个md）：针对特定业务（如视频、FTP等）的流量进行累计统计，达到配额后触发差异化策略。包括关键参数、Gx接口原理、N7接口原理、系统影响与约束、总览原理、配置流程和调测步骤。
- **会话级累计流量策略控制**（3个md）：针对用户整个会话的全部流量进行累计统计，达到配额后触发差异化策略。包括关键参数、Gx接口原理和N7接口原理。

**FUP（Fair Usage Policy，公平使用策略）的核心目标**：当用户或特定业务的使用量达到预设配额时，通过PCRF/PCF下发新的QoS和计费规则，实现"用量越多带宽越低"的阶梯式控制，保障网络资源的公平分配。典型动作包括限速（如从100Mbit/s降为32kbit/s）、计费费率变更（如从免费变为1元/M）、重定向到充值页面等。

**UNC在FUP中的角色**：UNC作为PGW-C/SMF，是FUP策略的中间转发和执行节点：
- 接收PCRF/PCF下发的累计流量阈值和PCC规则
- 将PCC规则转换为N4接口的URR（Usage Reporting Rule）规则
- 建立URR ID与Monitoring-Key/UMID之间的映射关系
- 将URR绑定到对应的PDR（Packet Detection Rule）上
- 转发PGW-U/UPF上报的流量使用量给PCRF/PCF
- 执行PCRF/PCF下发的新QoS和计费规则

---

## 2. 核心知识点

### 2.1 FUP的两种粒度：业务级 vs 会话级

FUP解决方案根据流量统计的粒度分为两个层级，两者可以独立部署也可以组合使用：

| 维度 | 业务级累计流量策略控制 | 会话级累计流量策略控制 |
|------|----------------------|----------------------|
| **统计对象** | 特定业务（如视频、FTP、P2P等）的流量 | 用户整个会话的全部流量 |
| **业务识别** | 需要识别具体业务流（三四层或七层） | 不区分业务，统计所有流量 |
| **URR绑定方式** | URR绑定到指定业务流对应的PDR上 | URR关联到所有PDR上（整个会话生效） |
| **规则类型** | 三四层业务可用预定义或动态规则；七层业务只能用预定义规则 | 可用预定义或动态规则；预定义规则需配置不区分业务的流条件 |
| **典型场景** | 视频包月套餐、FTP配额管控、特定应用限速 | 总流量套餐管控、包月总配额限速 |
| **Usage-Monitoring-Level（Gx）** | PCC_RULE_LEVEL(1) | SESSION_LEVEL(0) |
| **引用位置（N7）** | refUmData在PccRule中定义 | refUmData在sessRules（SessionRule）中定义 |

**组合使用场景**：用户同时签约了"总流量10G套餐"（会话级）和"视频专项2G套餐"（业务级）。会话级URR关联到所有PDR统计总流量，业务级URR绑定到视频业务PDR单独统计视频流量，两个FUP独立触发各自的带宽策略。

### 2.2 业务级累计流量策略控制

#### 2.2.1 基于Gx接口（4G/融合场景）

**适用场景**：使用4G定义的Gx接口对2/3/4G用户的特定业务进行累计流量策略控制。

**网元职责划分**（以预定义规则、七层业务为例）：

| 网元 | 职责 |
|------|------|
| PCRF | 开启基于业务的累计流量策略控制功能；配置配额；配置预定义规则名称 |
| PGW-C（UNC） | 开启基于业务的累计流量策略控制功能；配置累计流量的URR策略；配置预定义规则 |
| PGW-U（UDG） | 开启基于业务的累计流量策略控制功能；配置流条件；配置累计流量的URR策略和带宽控制策略；配置预定义规则 |

**三阶段业务流程**：

**阶段一：用户上线（会话建立）**

1. UE发起激活请求
2. PGW-C向PCRF发送**CCR-I**消息，请求建立IP-CAN会话
3. PCRF根据签约信息判断是否签约指定业务，签约则通过**CCA-I**下发累计流量阈值和策略

   CCA-I关键信元（Gx接口）：

   | 主信元 | 子信元 | 说明 |
   |--------|--------|------|
   | Usage-Monitoring-Information | Monitoring-Key | 标识一种业务。动态规则在Charging-Rule-Definition中扩展；预定义规则与PGW-C上ADD URR命令的MONITORINGKEY参数一致 |
   | Usage-Monitoring-Information | Granted-Service-Unit | 流量阈值下发 |
   | Usage-Monitoring-Information | Usage-Monitoring-Level | 取值**PCC_RULE_LEVEL(1)**，指示业务级累计流量上报 |
   | Usage-Monitoring-Information | Usage-Monitoring-Report | 指示PGW-C应上报的累积流量 |
   | Usage-Monitoring-Information | Usage-Monitoring-Support | 指示Monitoring Key的配额监控去使能 |
   | Event-Trigger | - | 携带USAGE_REPORT触发器 |

4. PGW-C根据PCRF授权安装计费和QoS规则，生成N4接口URR规则，**将URR绑定在指定业务流对应的PDR上**，建立URR ID与Monitoring-Key映射
5. 通过PFCP Session Establishment Request（Create PDR）向PGW-U发送规则
6. PGW-U安装规则后返回Response，会话建立成功

**阶段二：配额消耗**

1. 用户访问指定业务，PGW-U检测到流量阈值耗尽，发送**PFCP Session Report Request**通知PGW-C（携带Usage Report信元组）
2. PGW-C返回PFCP Session Report Response
3. PGW-C根据URR ID与Monitoring-Key映射，通过**CCR-U**向PCRF上报指定业务流量（携带Used-Service-Unit）
4. PCRF扣减配额：
   - 配额未用尽：CCA-U下发**新流量阈值**继续累计 + 新QoS/计费规则
   - 配额耗尽：CCA-U指示**停止累计**，不再下发流量阈值，仅下发新策略（限速/计费变更/重定向）
5. PGW-C删除旧规则安装新规则，向无线侧发送更新的QoS信息，通过PFCP Session Modification Request向PGW-U下发新业务规则
6. PGW-U安装新规则，返回Response

**阶段三：用户下线**

1. 用户发起去激活或网络侧主动去激活
2. PGW-C发送PFCP Session Delete Request释放N4会话
3. PGW-U通过PFCP Session Delete Response上报指定业务使用量（Usage Report Trigger=**TERMR**）
4. PGW-C通过**CCR-T**上报指定业务使用量并通知PCRF删除会话
5. PCRF释放会话资源，回复CCA-T

#### 2.2.2 基于N7接口（5G/统一管控场景）

**适用场景**：使用5G定义的N7接口统一对2/3/4/5G用户的特定业务进行累计流量策略控制。N7接口可统一管控所有制式用户。

**网元职责划分**与Gx类似，但网元名称变为PCF、PGW-C/SMF、PGW-U/UPF。

**三阶段业务流程**：

**阶段一：会话建立**

1. UE发起**PDU Session Establishment**流程
2. PGW-C/SMF向PCF发送**Npcf_SMPolicyControl_Create Request (SmPolicyContextData)**请求会话策略，其中suppFeat字段指示是否支持Usage Monitoring Control功能（通过SET PCCFUNC命令配置）
3. PCF从UDR获取策略签约数据
4. PCF进行特性协商和策略决策，回复**Npcf_SMPolicyControl_Create Response (SmPolicyDecision)**

   SmPolicyDecision关键信元（N7接口，业务级）：

   | 主信元 | 子信元 | 说明 |
   |--------|--------|------|
   | PccRule | pccRuleId | PCC规则标识。预定义规则需与PGW-C/SMF和PGW-U/UPF上配置的规则名称一致 |
   | PccRule | flowInfos | 业务流描述信息。动态规则时PCF下发流描述；建议规划一个不区分业务流的默认动态规则 |
   | PccRule | refUmData | 引用umDecs中的umId值，**业务级时在PccRule中定义** |
   | umDecs | umId | 使用监控策略数据标识，与PGW-C/SMF上ADD URR命令的MONITORINGKEY一致 |
   | umDecs | volumeThreshold | 总流量阈值 |
   | policyCtrlReqTriggers | - | 达到流量阈值后上报的触发条件，如US_RE |
   | suppFeat | - | 特性协商结果，如UMC |

5. PGW-C/SMF根据pccRule和umDecs生成N4接口URR规则，将URR绑定在指定业务流对应的PDR上，建立URR ID与UMID映射
6. 通过PFCP Session Establishment Request向PGW-U/UPF发送规则

**阶段二：配额消耗**

1. PGW-U/UPF检测到业务流量阈值耗尽，发送PFCP Session Report Request通知PGW-C/SMF
2. PGW-C/SMF返回Response
3. PGW-C/SMF根据URR ID与UMID映射，通过**Npcf_SMPolicyControl_Update Request**通知PCF流量阈值耗尽
4. PCF策略决策：配额未耗尽则下发新阈值+新QoS规则；配额耗尽则不下发新阈值，仅更新QoS规则
5. PGW-C/SMF通过Npcf_SMPolicyControl_Update Response接收新策略，通过PFCP Session Modification Request转发给PGW-U/UPF

**阶段三：用户下线**

1. 用户发起PDU会话释放
2. AMF向PGW-C/SMF发送Nsmf_PDUSession_UpdateSMContext
3. PGW-C/SMF发送PFCP Session Delete Request
4. PGW-U/UPF通过Response上报使用量（Usage Report Trigger=TERMR）
5. PGW-C/SMF通过**Npcf_SMPolicyControl_Delete Request**上报使用量并通知PCF删除会话
6. PCF释放资源，回复Delete Response

### 2.3 会话级累计流量策略控制

#### 2.3.1 基于Gx接口（4G/融合场景）

**适用场景**：使用4G定义的Gx接口对2/3/4G用户使用的所有业务进行累计流量策略控制。

**与业务级的关键差异**：

| 差异点 | 业务级（Gx） | 会话级（Gx） |
|--------|-------------|-------------|
| Usage-Monitoring-Level | PCC_RULE_LEVEL(1) | **SESSION_LEVEL(0)** |
| URR绑定范围 | 指定业务流的PDR | **所有PDR**（整个会话） |
| PCRF签约判断 | 判断是否签约指定业务 | 判断是否签约该业务套餐（总量套餐） |
| 动态规则PGW-C职责 | 仅需开启功能 | 仅需开启功能（无需配置URR策略） |
| 预定义规则PGW-U流条件 | 配置特定业务流条件 | 配置**不区分业务的流条件** |

**业务流程**与业务级基本一致（用户上线->配额消耗->用户下线），核心区别在于：
- CCA-I中Usage-Monitoring-Level取值为SESSION_LEVEL(0)
- PGW-C生成的URR规则需要**关联到所有PDR上**（因为对整个会话生效）
- PGW-U配置的流条件**不区分业务**（统计所有流量）

#### 2.3.2 基于N7接口（5G/统一管控场景）

**适用场景**：使用5G定义的N7接口统一对2/3/4/5G用户使用的所有业务进行累计流量策略控制。

**与业务级N7的关键差异**：

| 差异点 | 业务级（N7） | 会话级（N7） |
|--------|-------------|-------------|
| 引用位置 | refUmData在**PccRule**中定义 | refUmData在**sessRules（SessionRule）**中定义 |
| URR绑定范围 | 指定业务流的PDR | **所有Create PDRs**（整个会话） |
| 流条件 | 特定业务流条件 | **不区分业务的流条件** |

**SmPolicyDecision关键信元**（N7接口，会话级）：

| 主信元 | 子信元 | 说明 |
|--------|--------|------|
| sessRules | - | SessionRule，会话级规则名称，在PCF上定义 |
| sessRules | refUmData | 对使用监控数据决策的引用，**会话级时在SessionRule中定义** |
| umDecs | umId | 预定义规则时与PGW-C/SMF的MONITORINGKEY一致 |
| umDecs | volumeThreshold | 总流量阈值 |
| policyCtrlReqTrigger | - | 达到阈值后上报触发条件，如US_RE |
| suppFeat | - | 特性协商结果，如UMC |

**Create URR关键子信元**（N4接口）：

| 子信元 | 说明 |
|--------|------|
| URR ID | 唯一标识一个Create URR。预定义规则通过ADD URR配置映射；动态规则由PGW-C/SMF将UMID直接转换为URR ID |
| Measurement Method | 计费方式：流量/时长/事件 |
| Reporting Trigger | 触发条件：Periodic/Volume Quota/Time Quota/Linked Usage Reporting等 |
| Volume Threshold | 总流量阈值 |

**配额消耗阶段的Usage Report子信元**：

| 子信元 | 说明 |
|--------|------|
| URR ID | 标识上报的URR |
| Usage Report Trigger | **VOLTH**表示流量阈值耗尽 |
| Volume Measurement | 流量使用情况（总流量/上行/下行） |

**配额消耗上报信元（accuUsageReports）**：

| 子信元 | 说明 |
|--------|------|
| refUmId | UMID，根据URR ID与UMID映射关系获得 |
| volUsage | 用户使用的流量，从PGW-U/UPF上报获得 |

### 2.4 Gx vs N7接口对比

| 对比维度 | Gx接口 | N7接口 |
|----------|--------|--------|
| **定义来源** | 4G定义 | 5G定义 |
| **适用用户** | 2/3/4G用户 | 统一对2/3/4/5G用户（N7可覆盖所有制式） |
| **策略控制节点** | PCRF | PCF |
| **转发节点** | PGW-C | PGW-C/SMF |
| **执行节点** | PGW-U | PGW-U/UPF |
| **会话建立消息** | CCR-I / CCA-I（Diameter） | Npcf_SMPolicyControl_Create Request/Response（HTTP/JSON） |
| **配额消耗上报** | CCR-U / CCA-U | Npcf_SMPolicyControl_Update Request/Response |
| **会话释放上报** | CCR-T / CCA-T | Npcf_SMPolicyControl_Delete Request/Response |
| **业务标识** | Monitoring-Key（AVP） | umId / UMID（JSON字段） |
| **流量阈值下发** | Granted-Service-Unit | volumeThreshold |
| **流量使用上报** | Used-Service-Unit | accuUsageReports -> volUsage |
| **业务级标识** | Usage-Monitoring-Level=PCC_RULE_LEVEL(1) | refUmData在PccRule中 |
| **会话级标识** | Usage-Monitoring-Level=SESSION_LEVEL(0) | refUmData在sessRules中 |
| **特性协商** | Event-Trigger=USAGE_REPORT | suppFeat=UMC |
| **规则下发方式** | PCC规则（动态/预定义）通过CCA消息下发 | PccRule通过SmPolicyDecision下发 |
| **N4接口消息** | PFCP Session Establishment/Modification/Delete | 相同（PFCP协议） |

### 2.5 规则类型：预定义规则 vs 动态规则

| 对比维度 | 预定义规则 | 动态规则 |
|----------|-----------|---------|
| **定义位置** | 在PGW-C和PGW-U上预先配置完整规则 | PCRF/PCF直接下发完整业务流描述 |
| **PCRF/PCF下发内容** | 仅下发规则名称和Monitoring-Key/UMID | 下发完整PCC规则+flowInfos（业务流描述） |
| **业务流匹配** | 在PGW-U上通过预配置的流条件匹配 | PGW-U根据PCRF下发的flowInfos匹配 |
| **适用业务层** | 三四层和七层均可 | 仅三四层 |
| **URR ID来源** | PGW-C/PGW-U上ADD URR命令配置 | PGW-C/SMF将PCRF下发的UMID/Monitoring-Key转换为URR ID |
| **配置复杂度** | 较高（需在多个网元上预配置） | 较低（PCRF/PCF集中管理） |
| **灵活性** | 低（规则固定，修改需重新配置） | 高（PCRF/PCF可动态调整） |

### 2.6 FUP触发后的动作

当流量达到配额或阈值时，PCRF/PCF通过新策略下发以下动作（可组合）：

| 动作类型 | 说明 | 实现方式 |
|----------|------|---------|
| **限速/降速** | 降低用户或业务的MBR/GMBR带宽 | 通过QoS-Information(QoSData)下发新MBR；或下发新预定义规则（配额耗尽后的规则） |
| **计费费率变更** | 从免费变为收费，或调整费率组 | 下发新计费规则，URR关联不同的Rating Group（如RG=10变RG=20） |
| **重定向** | 将用户流量重定向到充值/提醒页面 | 通过重定向规则实现 |
| **停止累计** | 配额耗尽后不再下发新流量阈值 | CCA-U/Update Response中不携带Granted-Service-Unit/volumeThreshold |
| **QoS降级** | 降低QCI/5QI优先级或ARP | 通过更新的QoS规则实现 |

### 2.7 系统影响与约束

**系统性能影响**：
- 业务级累计流量策略控制需要PGW-U/UPF、PGW-C/SMF和PCRF/PCF之间不断交互，同时需要动态处理PCRF/PCF下发的策略，对系统性能影响较大
- 影响程度取决于启用该特性的用户比例和话务模型
- 规划时需要考虑启用比例，建议联系华为技术支持获取性能评估服务

**约束条件**：
- 对于UE Category用户，要求PCRF/PCF下发的业务级流量阈值**不低于1GB**，否则影响该用户业务流量累计的准确性
- 规则名称需要在PCRF/PCF、UNC、UDG三个网元上配置一致
- URR标识需要在UNC和UDG两端配置一致
- 费率组（Rating Group）需要在UNC和CHF/OCS上保持一致

---

## 3. 配置调测要点

### 3.1 关键参数清单

#### 3.1.1 UNC侧关键参数

| 参数名称 | 涉及命令 | 必选/可选 | 说明 |
|----------|---------|-----------|------|
| MKPARSEFORMAT | SET PCCFUNC | 可选 | Monitoring-Key的解析方式，需与PCRF/PCF一致。PCF不适用此参数 |
| N7FEATURELIST=UMC | SET PCCFUNC | 必选 | N7接口特性列表，支持使用情况监视控制（Usage Monitoring Control） |
| FEATURELIST=UMCH | MOD PCRF | 可选 | Usage Monitoring拥塞处理功能，配额重置时避免Gx接口信令拥塞 |
| FUPSESSIONEXC | MOD PCCPOLICYGRP | 可选 | Session级FUP累计标识。ENABLE表示该PCC策略组对应的业务**不计入**Session级流量；默认DISABLE（计入） |
| USAGERPTMODE=MONITORINGKEY | ADD URR | 必选 | 使用量上报模式，标识累计流量业务 |
| MONITORINGKEY | ADD URR | 必选 | 监控属性值，标识累计流量业务，需与PCRF/PCF一致 |
| URRID | ADD URR | 必选 | URR标识，需与PGW-U/UPF一致 |
| ONLCOMPOUNDTYPE / ONLINERG | ADD URR | 必选 | 在线计费标识组成类型和费率组 |
| ONLMETERINGTYPE=VOLUME | ADD URR | 必选 | 在线计费统计类型（流量计费） |

#### 3.1.2 UDG侧关键参数

| 参数名称 | 涉及命令 | 必选/可选 | 说明 |
|----------|---------|-----------|------|
| REDIRECTFUP | SET SRVCOMMONPARA | 可选 | 重定向报文FUP流量统计标识。缺省不统计重定向流量到累计流量中（重定向流量免费） |
| USAGERPTMODE=MONITORINGKEY | ADD URR | 必选 | 使用量上报模式 |
| FILTER / FLOWFILTER / FLTBINDFLOWF | ADD系列 | 必选 | 三四层过滤条件、流过滤器及其绑定 |

#### 3.1.3 License要求

| 产品 | License项 | 命令 | 说明 |
|------|----------|------|------|
| UNC | LKV2FUPSAT01 | SET LICENSESWITCH | 业务级累计流量策略控制的License项 |
| UDG | LKV3G5FPBS01 | SET LICENSESWITCH | 业务级累计流量策略控制的License项 |

### 3.2 业务级FUP配置流程（UNC侧）

**配置顺序**（UNC侧）：

1. **开启License**
   ```
   SET LICENSESWITCH:LICITEM="LKV2FUPSAT01",SWITCH=ENABLE;
   ```

2. **配置PCC功能**
   ```
   SET PCCFUNC:MKPARSEFORMAT=UNSIGNED32,N7FEATURELIST=UMC;
   ```

3. **配置累计流量上报URR**（Monitoring-Key绑定）
   ```
   ADD URR:URRNAME="urr_mk", URRID=1000, USAGERPTMODE=MONITORINGKEY, MONITORINGKEY="2001";
   ```

4. **配置配额耗尽前计费URR**
   ```
   ADD URR:URRNAME="urr_basic", URRID=2000, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=10, ONLMETERINGTYPE=VOLUME;
   ```

5. **配置URR组**（配额耗尽前）
   ```
   ADD URRGROUP:URRGROUPNAME="urrg_basic", UPURRNAME1="urr_mk", UPURRNAME2="urr_basic", DOWNURRNAME1="urr_mk", DOWNURRNAME2="urr_basic";
   ```

6. **配置PCC策略组**（配额耗尽前）
   ```
   ADD PCCPOLICYGRP:PCCPOLICYGRPNM="cg_basic", URRGROUPNAME="urrg_basic", FUPSESSIONEXC=ENABLE;
   ```

7. **配置配额耗尽后计费URR**
   ```
   ADD URR:URRNAME="urr_exhaust", URRID=3000, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=20, ONLMETERINGTYPE=VOLUME;
   ```

8. **配置URR组**（配额耗尽后）
   ```
   ADD URRGROUP:URRGROUPNAME="urrg_exhaust", UPURRNAME1="urr_mk", UPURRNAME2="urr_exhaust", DOWNURRNAME1="urr_mk", DOWNURRNAME2="urr_exhaust";
   ```

9. **配置PCC策略组**（配额耗尽后）
   ```
   ADD PCCPOLICYGRP:PCCPOLICYGRPNM="cg_exhaust", URRGROUPNAME="urrg_exhaust", FUPSESSIONEXC=ENABLE;
   ```

10. **配置预定义规则**（配额耗尽前/后）
    ```
    ADD RULE:RULENAME="rule_test1", POLICYTYPE=PCC, PRIORITY=30, POLICYNAME="cg_basic";
    ADD RULE:RULENAME="rule_test2", POLICYTYPE=PCC, PRIORITY=40, POLICYNAME="cg_exhaust";
    ```

11. **配置用户模板和规则绑定**（可选）
    ```
    ADD USERPROFILE:USERPROFILENAME="up_test", UPTYPE=PCC;
    ADD RULEBINDING:USERPROFILENAME="up_test", RULENAME="rule_test1";
    ADD RULEBINDING:USERPROFILENAME="up_test", RULENAME="rule_test2";
    ```

### 3.3 业务级FUP配置流程（UDG侧）

**配置顺序**（UDG侧）：

1. **开启License**
   ```
   SET LICENSESWITCH:LICITEM="LKV3G5FPBS01",SWITCH=ENABLE;
   ```

2. **配置三四层过滤条件**
   ```
   ADD FILTER:FILTERNAME="filter_red", L34PROTTYPE=STRING, L34PROTOCOL=ANY, SVRIPMODE=IP, SVRIP="10.7.19.38", SVRIPMASKTYPE=LENGTHTYPE, SVRIPMASKLEN=32;
   ADD FLOWFILTER:FLOWFILTERNAME="fg_red";
   ADD FLTBINDFLOWF:FLOWFILTERNAME="fg_red", FILTERNAME="filter_red";
   SET REFRESHSRV:REFRESHTYPE=USERPROFILE;
   ```

3. **配置URR**（累计流量上报+配额耗尽前+配额耗尽后，URR ID需与UNC一致）
   ```
   ADD URR:URRNAME="urr_mk", URRID=1000, USAGERPTMODE=MONITORINGKEY;
   ADD URR:URRNAME="urr_basic", URRID=2000, USAGERPTMODE=ONLINE, ONLMETERINGTYPE=VOLUME;
   ADD URR:URRNAME="urr_exhaust", URRID=3000, USAGERPTMODE=ONLINE, ONLMETERINGTYPE=VOLUME;
   ```

4. **配置URR组和PCC策略组**（配额耗尽前/后，结构同UNC侧）

5. **配置规则**（需绑定FlowFilter）
   ```
   ADD RULE:RULENAME="rule_test1", POLICYTYPE=PCC, FILTERINGMODE=FLOWFILTER, FLOWFILTERNAME="fg_red", POLICYNAME="cg_basic", PRIORITY=100;
   ADD RULE:RULENAME="rule_test2", POLICYTYPE=PCC, FILTERINGMODE=FLOWFILTER, FLOWFILTERNAME="fg_red", POLICYNAME="cg_exhaust", PRIORITY=200;
   ```

6. **配置用户模板和规则绑定**

### 3.4 FUP配置的三件套结构

业务级FUP的配置遵循"URR -> URRGROUP -> PCCPOLICYGRP"三件套模式：

```
配额耗尽前：
  URR(urr_mk, ID=1000, MONITORINGKEY)  ← 累计流量上报
  URR(urr_basic, ID=2000, ONLINE, RG=10) ← 配额耗尽前计费
  URRGROUP(urrg_basic) = {UP1=urr_mk, UP2=urr_basic, DOWN1=urr_mk, DOWN2=urr_basic}
  PCCPOLICYGRP(cg_basic) ← URRGROUP=urrg_basic, FUPSESSIONEXC=ENABLE

配额耗尽后：
  URR(urr_exhaust, ID=3000, ONLINE, RG=20) ← 配额耗尽后计费
  URRGROUP(urrg_exhaust) = {UP1=urr_mk, UP2=urr_exhaust, DOWN1=urr_mk, DOWN2=urr_exhaust}
  PCCPOLICYGRP(cg_exhaust) ← URRGROUP=urrg_exhaust, FUPSESSIONEXC=ENABLE

规则绑定：
  RULE(rule_test1, PRIORITY=30/100) → cg_basic（配额耗尽前生效）
  RULE(rule_test2, PRIORITY=40/200) → cg_exhaust（配额耗尽后生效）
```

**关键设计**：
- URRGROUP的UPURRNAME1/DOWNURRNAME1始终绑定`urr_mk`（累计流量上报URR），确保无论配额耗尽前后都持续统计累计流量
- UPURRNAME2/DOWNURRNAME2在配额耗尽前绑定`urr_basic`（RG=10），耗尽后绑定`urr_exhaust`（RG=20），实现费率切换
- FUPSESSIONEXC=ENABLE表示该业务流量不计入Session级FUP累计（避免重复统计）

### 3.5 调测步骤

**前提条件**：完成FUP配置、完成PCC基本功能配置、S1-U/N3/N6镜像接口已安装抓包工具。

**调测流程**（11步）：

1. **验证License**：UNC上执行`LST LICENSESWITCH`，确认SWITCH=ENABLE
2. **验证License**：UDG上执行`LST LICENSESWITCH`，确认SWITCH=ENABLE
3. **创建用户跟踪任务**：消息类型选择N4、Gx和N7
4. **用户接入**：测试终端使用目标APN接入网络，访问目标业务（如P2P）
5. **验证规则下发**：查看CCA-I/Npcf_SMPolicyControl_Create Response中的Usage-Monitoring-Information/UsageMonitoringData是否与规划值一致
6. **流量产生**：继续使用业务，通过镜像接口抓包确认流量正常
7. **验证流量上报**：流量达到阈值后，查看PFCP Session Report Request是否携带流量使用量
8. **验证UNC上报**：检查UNC发起的CCR-U（Gx）是否携带Usage-Monitoring-Information，或Npcf_SMPolicyControl_Update Request（N7）是否携带accuUsageReports，且上报流量接近阈值的100%
9. **排查PCC功能**：如果步骤8异常，执行`LST APNPCCFUNC`检查DNN下是否开启PCC功能
10. **验证配额耗尽**：继续使用业务直至超过PCRF/PCF配额
11. **验证策略变更**：查看CCA-U/Npcf_SMPolicyControl_Update Response是否下发预期的QoS规则或计费规则。动态规则查看MBR是否降为设置值；预定义规则查看PCC规则名称是否正确切换

---

## 4. 与带宽控制的关系

### 4.1 FUP是带宽控制场景的核心触发机制

在带宽控制场景中，FUP（公平使用策略）扮演"累计流量触发器"的角色：

```
用户签约套餐 → PCRF/PCF配置流量配额和门限
  → PGW-U/UPF检测流量累计
    → 达到阈值：上报流量给PCRF/PCF
      → PCRF/PCF下发新QoS规则（降低MBR/变更费率组）
        → PGW-U/UPF执行新的带宽控制策略（限速）
```

FUP与带宽控制的关系链：
- **输入**：流量配额（volumeThreshold / Granted-Service-Unit）
- **检测**：PGW-U/UPF通过URR统计流量，达到阈值触发上报
- **决策**：PCRF/PCF根据累计流量决定策略变更
- **输出**：新的QoS规则（MBR降速）或新预定义规则（配额耗尽后规则，可能关联不同的带宽控制策略）

### 4.2 FUP与带宽控制特性的对应关系

| FUP层级 | UNC侧特性 | UDG侧特性 | 带宽控制动作 |
|---------|----------|----------|-------------|
| 业务级FUP基础 | GWFD-020353（FUP） | WSFD-109104（FUP） | 业务流量达阈值后限速 |
| 业务级FUP增强 | GWFD-110312（业务级FUP） | WSFD-211009（业务级FUP） | 支持SA识别+业务级累计+差异化限速 |
| 会话级FUP | GWFD-020353（FUP基础） | WSFD-109104（FUP基础） | 总流量达阈值后限速 |

### 4.3 FUP与带宽控制其他场景的协作

FUP作为累计流量维度的带宽控制，与以下带宽控制场景互补：
- **实时带宽监控（BWM）**：基于实时速率的带宽控制，与FUP的累计流量控制维度不同
- **ADC带宽控制**：基于应用识别的带宽控制，FUP的业务级控制可复用ADC的SA识别能力
- **QoS承载控制**：FUP触发后的QoS降级通过QoS承载控制特性执行
- **Shaping整形**：FUP触发限速后，具体的流量整形由Shaping特性执行

### 4.4 业务级与会话级FUP的协同

当用户同时签约业务级和会话级FUP时，两个FUP独立运行：
- 业务级URR绑定到特定业务PDR，单独统计该业务流量
- 会话级URR关联到所有PDR，统计全部流量
- 业务级FUP的流量可以通过FUPSESSIONEXC=ENABLE排除在会话级统计之外（避免重复统计）
- 两个FUP各自独立触发各自的带宽策略，先达阈值的先触发

---

## 5. 关键术语

| 术语 | 全称/含义 | 说明 |
|------|----------|------|
| **FUP** | Fair Usage Policy，公平使用策略 | 当用户/业务使用量达到配额时触发差异化策略（限速/计费变更/重定向） |
| **Gx接口** | 4G定义的PCRF与PGW-C之间策略接口 | 基于Diameter协议，覆盖2/3/4G用户 |
| **N7接口** | 5G定义的PCF与SMF之间策略接口 | 基于HTTP/JSON（SBI接口），可统一覆盖2/3/4/5G用户 |
| **累计流量** | 在一定周期内对特定业务或会话的流量进行累加统计 | 达到预设阈值后触发策略变更 |
| **业务级** | 针对特定业务（如视频、FTP）的流量进行FUP控制 | Usage-Monitoring-Level=PCC_RULE_LEVEL(1)；refUmData在PccRule中 |
| **会话级** | 针对用户整个会话的全部流量进行FUP控制 | Usage-Monitoring-Level=SESSION_LEVEL(0)；refUmData在sessRules中 |
| **Monitoring-Key** | Gx接口中标识一种业务的监控键值 | 用于关联URR与特定业务；动态规则在Charging-Rule-Definition中扩展，预定义规则在ADD URR命令中配置 |
| **UMID / umId** | N7接口中使用监控策略数据标识 | 功能等同于Gx的Monitoring-Key，在umDecs中定义 |
| **URR** | Usage Reporting Rule，使用量上报规则 | PGW-C/SMF生成，下发到PGW-U/UPF执行流量统计和上报 |
| **PDR** | Packet Detection Rule，报文检测规则 | URR绑定到PDR上实现特定业务流的流量统计 |
| **PCC规则** | Policy and Charging Control Rule | 包含计费规则和QoS规则，分为动态规则和预定义规则 |
| **预定义规则** | 在PGW-C/PGW-U上预先配置的PCC规则 | PCRF/PCF仅下发规则名称，支持三四层和七层业务 |
| **动态规则** | PCRF/PCF直接下发完整业务流描述的PCC规则 | 仅支持三四层业务，灵活性更高 |
| **UMC** | Usage Monitoring Control，使用情况监视控制 | N7接口的特性协商标识，通过suppFeat=UMC协商 |
| **UMCH** | Usage Monitoring Congestion Handling | 拥塞处理功能，避免配额重置时Gx接口信令拥塞 |
| **配额** | PCRF/PCF上配置的流量总额度 | 如每月10G、视频专项2G等 |
| **阈值** | PCRF/PCF下发的流量上报门限 | PGW-U/UPF统计到该门限时触发上报，如1G上报一次 |
| **Rating Group (RG)** | 费率组 | 标识计费费率，FUP配额耗尽前后可切换到不同RG实现费率变更 |
| **FUPSESSIONEXC** | Session级FUP累计排除标识 | ENABLE表示该PCC策略组的业务流量不计入Session级FUP统计 |
| **TERMR** | Termination Reporting | 会话释放时的流量上报触发器，指示终止PFCP Session时的流量上报 |
| **VOLTH** | Volume Threshold | 流量阈值耗尽触发器，指示URR检测到流量达到阈值 |

---

## 6. 知识来源

| 序号 | 文件名 | 内容概要 |
|------|--------|---------|
| 1 | 关键参数_23928086.md | 业务级FUP关键参数（UNC+UDG侧）：MKPARSEFORMAT、N7FEATURELIST、USAGERPTMODE、MONITORINGKEY等 |
| 2 | 基于Gx接口策略控制_70687837.md | 业务级FUP基于Gx接口的完整原理：业务场景、网元规划、三阶段信令流程（用户上线/配额消耗/用户下线） |
| 3 | 基于N7接口策略控制_70607727.md | 业务级FUP基于N7接口的完整原理：业务场景、网元规划、三阶段信令流程（会话建立/配额消耗/用户下线） |
| 4 | 系统影响与约束_24087910.md | 业务级FUP的系统性能影响（PGW-U/UPF/PGW-C/PCRF交互开销）和约束条件（UE Category阈值不低于1GB） |
| 5 | 原理描述_24087908.md | 业务级FUP总览：Gx/N7接口区分、三四层/七层业务区分、预定义/动态规则区分 |
| 6 | 调测业务级累计流量策略控制_70687839.md | 业务级FUP调测步骤（11步）：License验证→规则下发验证→流量上报验证→策略变更验证 |
| 7 | 配置业务级累计流量策略控制_70607729.md | 业务级FUP完整配置流程（UNC+UDG侧）：License→PCC功能→URR→URRGROUP→PCCPOLICYGRP→RULE→USERPROFILE |
| 8 | 关键参数_70607723.md | 会话级FUP关键参数：MKPARSEFORMAT、N7FEATURELIST、UMCH、FUPSESSIONEXC、REDIRECTFUP |
| 9 | 基于Gx接口策略控制_24087904.md | 会话级FUP基于Gx接口的完整原理：三阶段信令流程，Usage-Monitoring-Level=SESSION_LEVEL(0)，URR关联所有PDR |
| 10 | 基于N7接口策略控制_23928080.md | 会话级FUP基于N7接口的完整原理：三阶段信令流程，refUmData在sessRules中，Create URR信元详解 |
