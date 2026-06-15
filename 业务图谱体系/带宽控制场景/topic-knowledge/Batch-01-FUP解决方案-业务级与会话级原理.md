# Batch-01: 5G Core FUP解决方案 - 业务级与会话级原理

> **来源**: UDG 业务专题 - 5G Core FUP解决方案
> **覆盖**: 业务级+会话级累计流量策略控制（Gx/N7接口原理、关键参数、配置调测）
> **文件数**: 10 md
> **带宽控制聚焦**: FUP累计流量触发带宽调整（降速/限速）

## 1. 文档概述

本批次覆盖 UDG 产品文档中"5G Core FUP解决方案"的两个子专题：

- **业务级累计流量策略控制**（7个md）：针对特定业务（如视频、FTP）进行差异化流量累计控制，当指定业务流量达到配额时触发带宽策略变更。
- **会话级累计流量策略控制**（3个md）：针对用户整个会话的全部流量进行累计控制，当总流量达到配额时触发带宽策略变更。

在带宽控制场景中，FUP（Fair Usage Policy，公平使用策略）是核心的累计流量触发机制：通过PCRF/PCF配置流量配额和门限，由PGW-U/UPF执行流量检测和带宽策略（限速、重定向、计费变更），实现"用量越多带宽越低"的阶梯式带宽控制。

FUP支持两种接口路径：
- **Gx接口**（4G定义）：PCRF <-> PGW-C <-> PGW-U，覆盖2/3/4G用户
- **N7接口**（5G定义）：PCF <-> PGW-C/SMF <-> PGW-U/UPF，覆盖2/3/4/5G用户（N7可统一管控所有制式）

两种规则类型：
- **预定义规则**：在PGW-C/PGW-U上预先配置规则，PCRF/PCF仅下发规则名称和Monitoring-Key，适用于三四层和七层业务
- **动态规则**：PCRF/PCF直接下发完整业务流描述，适用于三四层业务

## 2. 核心知识点

### 2.1 业务级累计流量策略控制原理

#### 2.1.1 Gx接口实现

**适用场景**：使用4G定义的Gx接口对2/3/4G用户的特定业务（三四层或七层）进行累计流量策略控制。

**网元职责划分**（预定义规则方式，七层业务示例）：

| 网元 | 职责 |
|------|------|
| PCRF | 开启基于业务的累计流量策略控制功能；配置配额；配置预定义规则名称 |
| PGW-C | 开启基于业务的累计流量策略控制功能；配置累计流量的URR策略；配置预定义规则 |
| PGW-U | 开启基于业务的累计流量策略控制功能；配置流条件；配置累计流量的URR策略和带宽控制策略；配置预定义规则 |

**三阶段业务流程**：

1. **用户上线**
   - UE发起激活请求
   - PGW-C向PCRF发送CCR-I消息，请求建立IP-CAN会话
   - PCRF根据用户签约信息判断是否签约指定业务，签约则通过CCA-I下发累计流量阈值和策略
   - CCA-I关键信元：

     | 主信元 | 子信元 | 说明 |
     |--------|--------|------|
     | Usage-Monitoring-Information | Monitoring-Key | 标识一种业务，PGW-U据此执行累计流量动作。动态规则在Charging-Rule-Definition中扩展；预定义规则与PGW-C上ADD URR命令的MONITORINGKEY一致 |
     | Usage-Monitoring-Information | Granted-Service-Unit | 流量阈值下发 |
     | Usage-Monitoring-Information | Usage-Monitoring-Level | 取值PCC_RULE_LEVEL(1)，指示业务级 |
     | Usage-Monitoring-Information | Usage-Monitoring-Report | 指示PGW-C应上报的累积流量 |
     | Usage-Monitoring-Information | Usage-Monitoring-Support | 指示Monitoring Key的配额监控去使能 |
     | Event-Trigger | - | 携带USAGE_REPORT触发器 |

   - PGW-C根据PCRF授权安装计费和QoS规则，生成N4接口URR规则，将URR绑定在指定业务流对应的PDR上，建立URR ID与Monitoring-Key的映射
   - 通过PFCP Session Establishment Request（Create PDR）消息向PGW-U发送规则
   - PGW-U安装规则后返回PFCP Session Establishment Response，用户会话建立成功

2. **配额消耗**
   - 用户访问指定业务，PGW-U检测到流量阈值耗尽，发送PFCP Session Report Request通知PGW-C（携带Usage Report信元组）
   - PGW-C返回PFCP Session Report Response
   - PGW-C根据URR ID与Monitoring-Key映射关系，通过CCR-U消息向PCRF上报指定业务流量（携带Usage-Monitoring-Information和Used-Service-Unit）
   - PCRF扣减配额：若配额未用尽，CCA-U下发新流量阈值继续累计；若配额耗尽，指示停止累计，不下发新阈值
   - **配额耗尽后的带宽策略执行**：PCRF通过CCA-U下发新的QoS和计费规则（限速、计费变更、重定向等），PGW-C转发至PGW-U执行
   - PGW-U安装更新后的规则，返回PFCP Session Modification Response

3. **用户下线**
   - 用户发起去激活或网络侧主动去激活
   - PGW-C发送PFCP Session Delete Request释放N4会话
   - PGW-U通过PFCP Session Delete Response上报指定业务使用量（Usage Report Trigger=TERMR），删除会话
   - PGW-C通过CCR-T消息上报指定业务使用量并通知PCRF删除会话
   - PCRF释放会话资源，回复CCA-T

#### 2.1.2 N7接口实现

**适用场景**：使用5G定义的N7接口统一对2/3/4/5G用户的特定业务进行累计流量策略控制。

**网元职责划分**（预定义规则方式）：

| 网元 | 职责 |
|------|------|
| PCF | 开启基于业务的累计流量策略控制功能；配置配额；配置预定义规则名称 |
| PGW-C/SMF | 开启基于业务的累计流量策略控制功能；配置累计流量的URR策略；配置预定义规则 |
| PGW-U/UPF | 开启基于业务的累计流量策略控制功能；配置流条件；配置累计流量的URR策略和带宽控制策略；配置预定义规则 |

**三阶段业务流程**：

1. **会话建立**
   - UE发起PDU Session Establishment流程
   - PGW-C/SMF向PCF发送Npcf_SMPolicyControl_Create Request，suppFeat字段指示是否支持Usage Monitoring Control（通过SET PCCFUNC命令设置）
   - PCF从UDR获取策略签约数据
   - PCF进行特性协商和策略决策，回复Npcf_SMPolicyControl_Create Response（SmPolicyDecision），包含业务级PCC规则、UMID、流量阈值、触发条件

   SmPolicyDecision主要信元：

     | 主信元 | 子信元 | 说明 |
     |--------|--------|------|
     | PccRule | pccRuleId | PCC规则标识，预定义规则需与PGW-C/SMF和PGW-U/UPF配置一致 |
     | PccRule | flowInfos | 业务流描述信息，动态规则时PCF下发 |
     | PccRule | refUmData | 对使用监控数据决策的引用，业务级在PccRule中定义，引用umDecs的umId |
     | umDecs | umId | 标识使用监控策略数据，与PGW-C/SMF上ADD URR的MONITORINGKEY一致 |
     | umDecs | volumeThreshold | 总流量阈值 |
     | policyCtrlReqTriggers | - | 达到阈值后的上报触发条件，如US_RE |
     | suppFeat | - | 特性协商结果，如UMC |

   - PGW-C/SMF根据PccRule和umDecs生成N4接口URR规则，将URR绑定在指定业务流对应的PDR上，建立URR ID与UMID的映射
   - 通过PFCP Session Establishment Request（Create PDR）发送至PGW-U/UPF

2. **配额消耗**
   - PGW-U/UPF检测到业务流量阈值耗尽，发送PFCP Session Report Request（携带Usage Report）
   - PGW-C/SMF返回PFCP Session Report Response
   - PGW-C/SMF通过Npcf_SMPolicyControl_Update Request（accuUsageReports）上报流量阈值耗尽
   - PCF进行策略决策：下发新流量阈值并更新QoS规则，通过Npcf_SMPolicyControl_Update Response下发（authSessAmbr信元组更新QoS）
   - PGW-C/SMF检查是否下发新阈值：有则继续上报并更新规则；无则通过PFCP Session Modification Request通知PGW-U/UPF不再上报

3. **用户下线**
   - 用户发起PDU会话释放，AMF向PGW-C/SMF发送Nsmf_PDUSession_UpdateSMContext
   - PGW-C/SMF执行PDU会话释放，发送PFCP Session Delete Request
   - PGW-U/UPF通过PFCP Session Delete Response上报使用量（Usage Report Trigger=TERMR），删除会话
   - PGW-C/SMF通过Npcf_SMPolicyControl_Delete Request上报使用量并通知PCF删除会话
   - PCF释放资源，回复Npcf_SMPolicyControl_Delete Response

#### 2.1.3 业务级关键参数

| 产品 | 参数类型 | 参数名称 | 命令 | 必选/可选 | 说明 |
|------|----------|----------|------|-----------|------|
| UNC | Monitoring-Key解析方式 | MKPARSEFORMAT | SET PCCFUNC | 可选 | PCRF下发的Monitoring-Key值的解析方式选择，PCF不适用 |
| UNC | N7接口特性列表 | N7FEATURELIST=UMC | SET PCCFUNC | 必选 | 支持使用情况监视控制（Usage Monitoring Control） |
| UNC | Supported-Features动态协商 | FEATURELIST=UMCH | MOD PCRF | 可选 | Usage Monitoring拥塞处理功能，避免配额重置时Gx信令拥塞 |
| UNC | Session级FUP累计标识 | FUPSESSIONEXC | MOD PCCPOLICYGRP | 可选 | 某些业务/应用流量不计入用户级流量时设为ENABLE，默认DISABLE |
| UDG | 重定向报文FUP流量统计标识 | REDIRECTFUP | SET SRVCOMMONPARA | 可选 | 重定向流量是否统计到累计流量中。缺省不统计（重定向流量免费） |

#### 2.1.4 系统影响与约束

**系统影响**：
- 业务级累计流量策略控制需要PGW-U/UPF、PGW-C/SMF和PCRF/PCF之间持续交互，动态处理策略，对系统性能影响较大
- 影响程度取决于启用该特性的用户比例和话务模型，规划时需考虑用户比例

**约束**：
- 对于UE Category用户，PCRF/PCF下发的业务级流量阈值不低于1GB，否则影响流量累计准确性

---

### 2.2 会话级累计流量策略控制原理

#### 2.2.1 Gx接口实现

**适用场景**：使用4G定义的Gx接口对2/3/4G用户的全部业务进行累计流量策略控制。

**网元职责划分**：

动态规则方式：
| 网元 | 职责 |
|------|------|
| PCRF | 开启会话级累计流量策略控制功能；配置配额；配置动态规则 |
| PGW-C | 开启会话级累计流量策略控制功能 |
| PGW-U | 开启会话级累计流量策略控制功能 |

预定义规则方式：
| 网元 | 职责 |
|------|------|
| PCRF | 开启会话级累计流量策略控制功能；配置配额；配置预定义规则名称 |
| PGW-C | 开启会话级累计流量策略控制功能；配置累计流量的URR策略；配置预定义规则 |
| PGW-U | 开启会话级累计流量策略控制功能；配置不区分业务的流条件；配置累计流量的URR策略和带宽控制策略；配置预定义规则 |

**与业务级的关键差异在CCA-I信元**：

| 子信元 | 业务级取值 | 会话级取值 |
|--------|------------|------------|
| Usage-Monitoring-Level | PCC_RULE_LEVEL(1) | SESSION_LEVEL(0) |

**会话级URR绑定的关键差异**：
- 业务级：URR绑定在**指定业务流对应的PDR**上（按业务区分）
- 会话级：URR关联到**所有PDR**上（对整个会话生效，因为sessRule/sessionRule对整个会话有效）

**三阶段流程**与业务级Gx流程结构一致（用户上线 -> 配额消耗 -> 用户下线），消息交互序列相同（CCR-I/CCA-I -> CCR-U/CCA-U -> CCR-T/CCA-T）。

配额消耗阶段的带宽策略执行：
- PCRF扣减配额，通过CCA-U下发新QoS和计费规则
- 配额未用尽：同时下发新流量阈值继续累计
- 配额耗尽：停止累计，不下发新阈值，下发新的带宽限制QoS规则（如限速32kbit/s）

#### 2.2.2 N7接口实现

**适用场景**：使用5G定义的N7接口统一对2/3/4/5G用户的全部业务进行累计流量策略控制。

**SmPolicyDecision信元关键差异**（相比业务级）：

| 主信元 | 子信元 | 业务级 | 会话级 |
|--------|--------|--------|--------|
| 信元位置 | refUmData | 在PccRule中定义 | 在sessRules（SessionRule）中定义 |
| 规则容器 | sessRules | 无 | 有，会话级规则名称，在PCF上定义 |

**会话级N4 URR绑定关键差异**：
- 业务级：URR绑定在指定业务流对应的PDR上
- 会话级：由于sessRule对整个会话有效，**URR需要关联到所有Create PDRs上**

**N7会话级Create URR信元**：

| 子信元 | 信元解释 | 说明 |
|--------|----------|------|
| URR ID | 唯一标识一个Create URR | 预定义规则通过ADD URR配置映射；动态规则由PGW-C/SMF将UMID转换为URR ID |
| Measurement Method | 计费方式 | 流量/时长/事件计费 |
| Reporting Trigger | 上报触发条件 | Periodic Reporting / Volume Quota / Time Quota / Linked Usage Reporting |
| Volume Threshold | 总流量阈值 | - |

**配额消耗阶段Update URR信元**：

| 子信元 | 信元解释 | 说明 |
|--------|----------|------|
| URR ID | 标识URR | 预定义规则映射/动态规则转换 |
| Measurement Method | 计费方式 | 值为VOLUM |
| Reporting Trigger | 触发条件 | 值为VOLTH（流量阈值） |
| Volume Threshold | 新流量阈值 | PCF下发的新阈值 |

**Usage Report上报信元（PFCP Session Report）**：

| 子信元 | 信元解释 |
|--------|----------|
| URR ID | 标识上报的URR |
| Usage Report Trigger | VOLTH表示流量阈值耗尽 |
| Volume Measurement | 总流量/上行流量/下行流量 |

**配额耗尽后的处理**：
- 用户配额未耗尽：PCF下发新流量阈值，Update URR下发新Volume Threshold
- 用户配额耗尽：sessRules下的refUmData为NULL，不再下发流量阈值，PGW-U/UPF不再上报流量，同时PCF更新QoS规则（限速等带宽策略生效）

#### 2.2.3 会话级关键参数

| 产品 | 参数类型 | 参数名称 | 命令 | 必选/可选 | 说明 |
|------|----------|----------|------|-----------|------|
| UNC | Monitoring-Key解析方式 | MKPARSEFORMAT | SET PCCFUNC | 可选 | PCRF下发的Monitoring-Key值的解析方式选择 |
| UNC | N7接口特性列表 | N7FEATURELIST=UMC | SET PCCFUNC | 必选 | 支持使用情况监视控制 |
| UNC | 使用量上报模式 | USAGERPTMODE=MONITORINGKEY | ADD URR | 必选 | 标识累计流量业务的Monitoring-Key参数 |
| UNC | 监控属性值 | MONITORINGKEY | ADD URR | 必选 | 标识累计流量业务的Monitoring-Key参数 |
| UDG | 使用量上报模式 | USAGERPTMODE=MONITORINGKEY | ADD URR | 必选 | 设置业务使用量上报模式 |

---

### 2.3 业务级 vs 会话级差异对比

| 维度 | 业务级累计流量 | 会话级累计流量 |
|------|----------------|----------------|
| **控制范围** | 特定业务（如视频、FTP、P2P）的流量 | 用户会话的全部流量（所有业务汇总） |
| **Monitoring-Level** | PCC_RULE_LEVEL(1) | SESSION_LEVEL(0) |
| **N7信元位置** | refUmData在PccRule中定义 | refUmData在sessRules(SessionRule)中定义 |
| **URR绑定方式** | 绑定在指定业务流对应的PDR上 | 关联到所有PDR上（整个会话生效） |
| **业务区分** | 可区分三四层（动态/预定义规则）和七层业务（仅预定义规则） | 不区分业务，所有流量统一累计 |
| **配额触发** | 指定业务流量达到配额阈值 | 用户总流量达到配额阈值 |
| **带宽策略触发** | 特定业务超量后对该业务限速 | 总量超限后对用户整体限速 |
| **典型场景** | 视频包月套餐超量限速、FTP配额耗尽后计费变更 | 流量包月套餐超量降速（不限业务类型） |

**关键技术差异总结**：
1. 会话级URR必须关联到所有PDR，因为sessRule对整个会话有效；业务级URR只需绑定到特定业务流的PDR
2. Gx接口通过Usage-Monitoring-Level区分（0=会话级，1=业务级）
3. N7接口通过信元位置区分（sessRules vs PccRule中的refUmData）
4. 业务级可针对不同业务分别设置配额和带宽策略；会话级是统一的总量控制

## 3. 配置与调测要点

### 3.1 配置流程（业务级，预定义规则方式）

**License开关**：
```
// UNC侧
SET LICENSESWITCH:LICITEM="LKV2FUPSAT01",SWITCH=ENABLE;
// UDG侧
SET LICENSESWITCH:LICITEM="LKV3G5FPBS01",SWITCH=ENABLE;
```

**UNC侧配置步骤**：

1. 配置PCC功能（SET PCCFUNC）
2. 配置累计流量上报URR（ADD URR，USAGERPTMODE=MONITORINGKEY）
3. 配置配额耗尽前计费URR（ADD URR，USAGERPTMODE=ONLINE，ONLINERG=费率组）
4. 配置配额耗尽后计费URR（ADD URR，USAGERPTMODE=ONLINE，ONLINERG=新费率组）
5. 配置URR组（ADD URRGROUP，关联累计流量URR和计费URR）
6. 配置PCC策略组（ADD PCCPOLICYGRP，绑定URR组，设FUPSESSIONEXC）
7. 配置规则（ADD RULE，关联PCC策略组）
8. 配置用户模板和规则绑定（ADD USERPROFILE / ADD RULEBINDING）

**UDG侧配置步骤**：

1. 配置三四层过滤条件（ADD FILTER）
2. 配置流过滤器（ADD FLOWFILTER）
3. 绑定过滤器到流过滤器（ADD FLTBINDFLOWF）
4. 刷新使配置生效（SET REFRESHSRV，REFRESHTYPE=USERPROFILE）
5. 配置累计流量上报URR（ADD URR，USAGERPTMODE=MONITORINGKEY）
6. 配置配额耗尽前/后计费URR（ADD URR，USAGERPTMODE=ONLINE）
7. 配置URR组（ADD URRGROUP）
8. 配置PCC策略组（ADD PCCPOLICYGRP）
9. 配置规则（ADD RULE，FILTERINGMODE=FLOWFILTER，关联流过滤器和PCC策略组）
10. 配置用户模板和规则绑定（ADD USERPROFILE / ADD RULEBINDING）

**URR ID规划要点**：
- 累计流量URR ID（如1000）：UNC和UDG必须一致
- 配额耗尽前URR ID（如2000）：UNC和UDG必须一致
- 配额耗尽后URR ID（如3000）：UNC和UDG必须一致
- 费率组（RG）：UNC与CHF/OCS需保持一致

### 3.2 配置任务示例

**业务套餐**：FTP业务配额2G，配额耗尽前免费，配额耗尽后1元/M

**UNC侧关键脚本**：
```
SET LICENSESWITCH:LICITEM="LKV2FUPSAT01",SWITCH=ENABLE;
SET PCCFUNC:MKPARSEFORMAT=UNSIGNED32,N7FEATURELIST=UMC;
// 累计流量URR
ADD URR:URRNAME="urr_01",URRID=1000,USAGERPTMODE=MONITORINGKEY,MONITORINGKEY="2001";
// 配额耗尽前计费URR（RG=10）
ADD URR:URRNAME="urrA",URRID=2000,USAGERPTMODE=ONLINE,ONLCOMPOUNDTYPE=ONLYRG,ONLINERG=10,ONLMETERINGTYPE=VOLUME;
ADD URRGROUP:URRGROUPNAME="urrgA",UPURRNAME1="urr_01",UPURRNAME2="urrA",DOWNURRNAME1="urr_01",DOWNURRNAME2="urrA";
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccgA",URRGROUPNAME="urrgA",FUPSESSIONEXC=ENABLE;
// 配额耗尽后计费URR（RG=20）
ADD URR:URRNAME="urrB",URRID=3000,USAGERPTMODE=ONLINE,ONLCOMPOUNDTYPE=ONLYRG,ONLINERG=20,ONLMETERINGTYPE=VOLUME;
ADD URRGROUP:URRGROUPNAME="urrgB",UPURRNAME1="urr_01",UPURRNAME2="urrB",DOWNURRNAME1="urr_01",DOWNURRNAME2="urrB";
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccgB",URRGROUPNAME="urrgB",FUPSESSIONEXC=ENABLE;
// 规则（配额耗尽前优先级高）
ADD RULE:RULENAME="rule_test1",POLICYTYPE=PCC,PRIORITY=30,POLICYNAME="pccgA";
ADD RULE:RULENAME="rule_test2",POLICYTYPE=PCC,PRIORITY=40,POLICYNAME="pccgB";
ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC;
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test1";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test2";
```

**UDG侧关键脚本**：
```
SET LICENSESWITCH:LICITEM="LKV3G5FPBS01",SWITCH=ENABLE;
// 流条件（匹配FTP服务器IP）
ADD FILTER:FILTERNAME="filter_red",L34PROTTYPE=STRING,L34PROTOCOL=ANY,SVRIPMODE=IP,SVRIP="10.7.19.38",SVRIPMASKTYPE=LENGTHTYPE,SVRIPMASKLEN=32;
ADD FLOWFILTER:FLOWFILTERNAME="fg_red";
ADD FLTBINDFLOWF:FLOWFILTERNAME="fg_red",FILTERNAME="filter_red";
SET REFRESHSRV:REFRESHTYPE=USERPROFILE;
// 累计流量URR
ADD URR:URRNAME="urr_mk",URRID=1000,USAGERPTMODE=MONITORINGKEY;
// 配额耗尽前计费URR
ADD URR:URRNAME="urr_basic",URRID=2000,USAGERPTMODE=ONLINE,ONLMETERINGTYPE=VOLUME;
ADD URRGROUP:URRGROUPNAME="urrg_basic",UPURRNAME1="urr_mk",UPURRNAME2="urr_basic",DOWNURRNAME1="urr_mk",DOWNURRNAME2="urr_basic";
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="cg_basic",URRGROUPNAME="urrg_basic";
// 配额耗尽后计费URR
ADD URR:URRNAME="urr_exhaust",URRID=3000,USAGERPTMODE=ONLINE,ONLMETERINGTYPE=VOLUME;
ADD URRGROUP:URRGROUPNAME="urrg_exhaust",UPURRNAME1="urr_mk",UPURRNAME2="urr_exhaust",DOWNURRNAME1="urr_mk",DOWNURRNAME2="urr_exhaust";
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="cg_exhaust",URRGROUPNAME="urrg_exhaust";
// 规则（关联流过滤器和PCC策略组）
ADD RULE:RULENAME="rule_test1",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="fg_red",POLICYNAME="cg_basic",PRIORITY=100;
ADD RULE:RULENAME="rule_test2",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="fg_red",POLICYNAME="cg_exhaust",PRIORITY=200;
ADD USERPROFILE:USERPROFILENAME="up_test";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test1";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test2";
```

### 3.3 调测要点

**调测前提**：
- 完成配置业务级累计流量策略控制
- 完成PCC基本功能配置
- S1-U/N3/N6镜像接口已安装第三方抓包工具

**调测步骤**：

1. 在UNC和UDG上分别执行**LST LICENSESWITCH**，确认License开关ENABLE
2. 在UNC创建用户跟踪任务，消息类型选择N4、Gx和N7
3. 测试终端使用APN接入网络，访问目标业务（如P2P）
4. 检查CCA-I/Npcf_SMPolicyControl_Create Response中的UsageMonitoringData是否与规划值一致
5. 用户使用一定时间业务后，检查用户跟踪中是否有PFCP Session Report Request携带流量
6. 检查CCR-U/Npcf_SMPolicyControl_Update Request中的流量是否与下发阈值的100%接近相等
7. 检查APN下PCC功能是否开启（**LST APNPCCFUNC**）
8. 检查CCA-U/Npcf_SMPolicyControl_Update Response是否下发预期QoS规则：
   - 动态规则：检查QoS-Information AVP(Gx) / QoSData(N7)中的MBR是否降为目标带宽
   - 预定义规则：检查是否下发正确的PCC规则名称

**关键调测检查点**：
- License开关是否打开（UNC: LKV2FUPSAT01, UDG: LKV3G5FPBS01）
- PCRF/PCF是否正确下发Monitoring-Key和流量阈值
- URR ID在UNC和UDG两侧是否一致
- 配额耗尽后是否正确切换PCC规则（限速生效）
- 动态规则的MBR降速值或预定义规则名称是否与规划一致

## 4. 与带宽控制的关系

### 4.1 FUP触发带宽调整的完整链路

```
用户激活 -> PCRF/PCF下发流量阈值和初始QoS -> PGW-U/UPF执行正常带宽
    -> 用户使用业务，流量累计达到阈值 -> PGW-U/UPF通过PGW-C/SMF上报流量
    -> PCRF/PCF累计流量，判断配额状态 -> 配额耗尽
    -> PCRF/PCF下发新QoS规则（降速/限速）和计费规则
    -> PGW-U/UPF执行新带宽策略
```

### 4.2 带宽调整的触发条件

| 触发场景 | 条件 | 执行动作 |
|----------|------|----------|
| 业务流量达到阈值 | 指定业务累计流量 >= PCRF/PCF下发阈值 | PGW-U/UPF上报流量，PCRF/PCF决策 |
| 配额未耗尽 | 阈值到达但总配额仍有余量 | PCRF/PCF下发新阈值，继续累计，QoS不变 |
| 配额耗尽 | 累计流量 >= 用户配额 | PCRF/PCF停止累计，下发新QoS规则（限速/降速），变更计费规则 |
| 配额耗尽-带宽降速 | 配额耗尽触发CCA-U/Update Response | 动态规则：MBR降为目标速率；预定义规则：切换到限速PCC策略组 |

### 4.3 典型带宽控制场景

**场景1：视频包月套餐限速**
- 签约：视频业务配额1G/月
- 配额内：正常带宽访问视频
- 超量后：视频业务限速32kbit/s（业务级FUP，七层业务，预定义规则）

**场景2：总流量套餐降速**
- 签约：每月总流量配额1G
- 配额内：正常带宽访问所有业务
- 超量后：用户整体限速32kbit/s（会话级FUP）

**场景3：FTP业务配额计费变更**
- 签约：FTP业务配额2G，配额内免费
- 超量后：按1元/M计费，可叠加限速策略（业务级FUP，三四层业务）

### 4.4 带宽策略执行机制

**动态规则方式**（三四层业务）：
- PCRF/PCF在配额耗尽后直接下发QoS-Information AVP(Gx) / QoSData(N7)
- QoS中MBR/GBR参数直接控制带宽
- 无需在PGW-U/UPF上预配置带宽策略

**预定义规则方式**（三四层/七层业务）：
- PCRF/PCF配额耗尽后下发新的PCC规则名称
- PGW-U/UPF根据预定义规则中关联的PCC策略组执行带宽控制
- 需在PGW-U/UPF上预先配置好"配额耗尽前"和"配额耗尽后"两套PCC策略组

**重定向场景**：
- 配额耗尽后可执行重定向到充值页面
- UDG通过SET SRVCOMMONPARA的REDIRECTFUP参数控制重定向流量是否计入累计流量
- 缺省不统计（重定向流量免费）

## 5. 关键概念术语

| 术语 | 定义 |
|------|------|
| FUP (Fair Usage Policy) | 公平使用策略，通过累计流量控制实现网络资源的公平分配，超量用户被降速或变更计费 |
| 业务级累计流量 | 针对特定业务（如视频、FTP）单独累计流量，Usage-Monitoring-Level=PCC_RULE_LEVEL(1) |
| 会话级累计流量 | 针对用户整个会话的全部流量累计，Usage-Monitoring-Level=SESSION_LEVEL(0) |
| Usage Monitoring Control (UMC) | 使用情况监视控制，5G N7接口的特性名称，通过SET PCCFUNC的N7FEATURELIST启用 |
| Monitoring-Key | 标识一种业务的监控键值，PGW-U据此执行累计流量动作 |
| UMID (Usage Monitoring ID) | N7接口中标识使用监控策略数据的ID，与Gx的Monitoring-Key概念对应 |
| URR (Usage Reporting Rule) | 使用量上报规则，PGW-C/SMF生成的N4接口规则，控制流量检测和上报 |
| URR ID | URR的唯一标识，需在PGW-C/SMF和PGW-U/UPF之间保持一致 |
| Granted-Service-Unit | Gx接口中PCRF授权下发的服务单元（流量阈值） |
| volumeThreshold | N7接口中PCF下发的总流量阈值 |
| PCC规则 | 策略和计费控制规则，分为动态规则（PCRF/PCF下发完整流描述）和预定义规则（网元预配置） |
| PDR (Packet Detection Rule) | 报文检测规则，N4接口上PGW-U/UPF用于检测业务流 |
| PCC策略组 (PCCPOLICYGRP) | 关联URR组的策略组，一个策略组对应一种带宽/计费策略组合 |
| 配额耗尽 | 用户累计流量达到PCRF/PCF配置的总配额，触发带宽策略变更 |
| UMCH (Usage Monitoring Congestion Handling) | Usage Monitoring拥塞处理功能，避免配额重置时Gx信令拥塞 |
| FUPSESSIONEXC | Session级FUP累计排除标识，设为ENABLE表示该业务流量不计入会话级流量统计 |
| REDIRECTFUP | 重定向报文FUP流量统计标识，控制重定向流量是否计入累计流量 |

## 6. 知识来源

| 序号 | 文件名 | 路径 |
|------|--------|------|
| 1 | 关键参数_23928086.md | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/业务级累计流量策略控制/原理描述/关键参数_23928086.md |
| 2 | 基于Gx接口策略控制_70687837.md | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/业务级累计流量策略控制/原理描述/基于Gx接口策略控制_70687837.md |
| 3 | 基于N7接口策略控制_70607727.md | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/业务级累计流量策略控制/原理描述/基于N7接口策略控制_70607727.md |
| 4 | 系统影响与约束_24087910.md | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/业务级累计流量策略控制/原理描述/系统影响与约束_24087910.md |
| 5 | 原理描述_24087908.md | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/业务级累计流量策略控制/原理描述_24087908.md |
| 6 | 调测业务级累计流量策略控制_70687839.md | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/业务级累计流量策略控制/调测业务级累计流量策略控制_70687839.md |
| 7 | 配置业务级累计流量策略控制_70607729.md | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/业务级累计流量策略控制/配置业务级累计流量策略控制_70607729.md |
| 8 | 关键参数_70607723.md | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/会话级累计流量策略控制/原理描述/关键参数_70607723.md |
| 9 | 基于Gx接口策略控制_24087904.md | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/会话级累计流量策略控制/原理描述/基于Gx接口策略控制_24087904.md |
| 10 | 基于N7接口策略控制_23928080.md | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/会话级累计流量策略控制/原理描述/基于N7接口策略控制_23928080.md |
