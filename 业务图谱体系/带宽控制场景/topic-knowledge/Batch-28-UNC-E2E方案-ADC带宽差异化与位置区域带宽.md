# Batch-28: UNC E2E方案 -- ADC带宽差异化控制与位置区域带宽差异化控制

> 来源：UNC 20.15.2 产品文档 -- 业务专题"5G PCC之SM策略解决方案" -- 典型业务场景E2E方案设计
> 共10个md文件，涵盖两个核心带宽控制方案的完整E2E实现

---

## 1. 概述

本批文档来自UNC产品文档中"5G PCC之SM策略解决方案"专题下的"典型业务场景E2E方案设计"章节，覆盖**两个带宽控制场景的完整E2E实现**：

### 方案一：基于业务类别的带宽差异化控制方案（ADC）

这是带宽控制场景中最核心的E2E方案之一。该方案以ADC（Application Detection and Control）功能为基础，实现**按业务类别差异化控制带宽**：当用户访问某特定视频应用时享受高带宽（100 Mbit/s），访问其他应用时为普通带宽（1 Mbit/s）。文档集包含完整的：需求描述、整体方案设计、PCF/SMF/UPF三侧业务配置、E2E快速调测方法。

### 方案二：基于位置区域的带宽差异化控制方案（预定义）

该方案实现**按用户位置区域差异化控制带宽**：用户从国内接入时享受100 Mbit/s带宽，从国外（漫游区）接入时带宽降至1 Mbit/s。采用预定义规则实现，文档集包含PCF/SMF侧业务配置、信令调测与快速调测方法。

两个方案共同构成了带宽控制场景的典型E2E实现范式，分别从"业务维度"和"位置维度"展示了带宽差异化控制的技术路径。

---

## 2. 核心知识点

### 2.1 ADC带宽差异化控制 -- 需求模型

ADC方案的核心需求可以归纳为一个简单的条件-动作矩阵：

| 业务场景 | 上下行带宽（Mbit/s） |
| --- | --- |
| 用户访问其他应用 | 1 |
| 用户开始访问某特定视频应用 | 100 |
| 用户停止访问某特定视频应用 | 1 |

该场景不涉及消息通知，核心是**动态感知应用类型并调整QoS保障**。

### 2.2 ADC方案 -- 业务拆解与策略架构

ADC方案采用动态规则实现，整体业务架构拆解为**1个业务（ADC_Service）+ 3个策略 + 4个规则**：

- **策略1（Policy_ADC_Normal）**：触发器为IPCAN_EST，用户上线时调用。包含两条规则：
  - Rule_ADC_Normal_PCC：保障用户访问其他应用时的普通带宽（maxbrUL/DL=1 Mbit/s）
  - Rule_ADC_AppId_PCC：下发appId=flow_ADC，通知UPF开启特定视频应用流检测

- **策略2（Policy_ADC_Start）**：触发器为APP_STA，用户开始访问特定视频应用时调用。包含一条规则：
  - Rule_ADC_Start_PCC：提供高带宽QoS保障（5qi=4，arp=1，maxbrUL/DL=100 Mbit/s，gbrUL/DL=100 Mbit/s）

- **策略3（Policy_ADC_Stop）**：触发器为APP_STO，用户停止访问特定视频应用时调用。包含一条规则：
  - Rule_ADC_Stop_PCC：Non-PCC类型规则，删除原有高带宽规则

**关键设计要点**：用户初始上线时必须下发appId（flow_ADC），通知UPF开启业务流检测开关，确保UPF能在用户开始访问特定视频应用时及时检测并通过APP_STA触发器上报PCF。

### 2.3 ADC方案 -- 三侧分工

| 网元 | 职责 | 规则类型 | 关键配置 |
| --- | --- | --- | --- |
| PCF（UPCF） | 定义动态规则、策略、业务，执行策略计算 | 动态规则 | 5G动作组（QoSData/FlowInformation/TrafficControlData/DynamicPccRule） |
| SMF（UNC） | 开启ADC基本功能，配置appId映射，开启流信息上报开关 | 无预定义规则 | License LKV2BADCF01、FLOWFILTER、ADCPARA |
| UPF（UDG） | 配置业务流识别条件（L3/L4或L7），检测应用流并上报事件 | 无预定义规则 | License LKV3G5ADCF01、FILTER/FLOWFILTER/L7FILTER |

### 2.4 ADC方案 -- 三大触发器机制

ADC方案依赖三个关键触发器实现E2E联动：

- **IPCAN_EST**：用户从N7接口上线触发PCF做策略计算，下发初始规则（含appId）
- **APP_STA**（Application Start）：UPF检测到用户**开始**访问特定应用流时，经SMF上报PCF，触发PCF下发高带宽规则
- **APP_STO**（Application Stop）：UPF检测到用户**停止**访问特定应用流时，经SMF上报PCF，触发PCF删除高带宽规则

### 2.5 ADC方案 -- QoS参数差异化设计

ADC方案中两条核心规则的QoS参数对比：

| 参数 | 普通应用规则 | 特定视频应用规则 |
| --- | --- | --- |
| 5QI | 取用户上线请求值（如9） | 4（专有QoS Flow） |
| ARP优先级 | 取用户上线请求值 | 2（更高优先级） |
| 抢占能力 | NOT_PREEMPT | MAY_PREEMPT |
| maxbrUL | 1 Mbps | 100 Mbps |
| maxbrDL | 1 Mbps | 100 Mbps |
| gbrUL | 无（非GBR） | 100 Mbps |
| gbrDL | 无（非GBR） | 100 Mbps |
| precedence | 30 | 1（高优先级匹配） |

**5qi=4的语义**：表示该动作组下发的是专有QoS Flow（Dedicated QoS Flow），gbrUL/gbrDL表示保障带宽。

### 2.6 位置区域带宽差异化 -- 需求与架构

位置区域方案实现"用户在不同地理区域享受不同带宽"，通过**预定义规则**实现：

- **Predefined1**：用户从国内接入时下发，5QI=5，ARP=2，MBR=100 Mbit/s
- **Predefined2**：用户从国外（漫游区）接入时下发，5QI=5，ARP=2，MBR=1 Mbit/s

架构特点：
- 业务名为Location_Service，类型为VALUE_ADDED_SERVICE
- 仅1个策略Policy_Location，触发器为IPCAN_EST + PLMN_CH
- 通过条件组判断RoamingRegion是否等于Region_Local来选择规则
- 需要在PCF侧配置PLMN和漫游区位置信息

### 2.7 位置区域方案 -- 触发器机制

- **IPCAN_EST**：用户上线时触发策略计算，根据当前位置下发对应预定义规则
- **PLMN_CH**（PLMN Change）：用户移动到不同区域时，UPF通过PFCP Session Report上报事件给SMF，SMF通过Npcf_SMPolicyControl_Update上报PCF，触发PCF更新策略（安装新规则、删除旧规则）

### 2.8 两方案的规则类型对比

| 维度 | ADC方案 | 位置区域方案 |
| --- | --- | --- |
| 规则类型 | 动态规则（DynamicPccRule） | 预定义规则（PredefinedPccRule） |
| 规则定义方 | PCF（UPCF） | SMF/UPF（本地预定义） |
| 带宽控制粒度 | 业务级（应用类型） | 会话级（位置区域） |
| 感知方式 | UPF ADC功能检测应用流 | PLMN信息判断区域 |
| 事件触发 | APP_STA/APP_STO | PLMN_CH |
| UPF侧配置 | 需配置FILTER/L7FILTER | 无需额外配置 |

---

## 3. 配置调测要点

### 3.1 ADC方案 -- PCF侧配置（UPCF Web UI）

配置顺序：5G动作组 > 规则 > 策略 > 业务 > 开户 > 签约

**（1）策略1 Policy_ADC_Normal的动作组配置**

需要配置7个5G动作组：

| 动作组 | 类型 | 关键参数 |
| --- | --- | --- |
| AG_FlowDesc | FlowDescription | action=PERMIT, direction=OUT, protocol=ANY |
| AG_FlowInfo | FlowInformation | flowDescription引用AG_FlowDesc, flowDirection=BIDIRECTIONAL |
| AG_TraCtrl | TrafficControlData | flowStatus=ENABLED |
| AG_Arp_Normal | Arp | 取值来自SmfSession.SubsDefQos*（用户上线请求值） |
| AG_Qos_Normal | QoSData | 5qi=用户请求值, maxbrUL/DL=1 Mbps |
| AG_ADC_Normal | DynamicPccRule | pccRuleId=AG_ADC_Normal, precedence=30, refQosData=AG_Qos_Normal |
| AG_ADC_AppId | DynamicPccRule | pccRuleId=AG_ADC_AppId, appId=flow_ADC, precedence=2 |

**（2）策略2 Policy_ADC_Start的动作组配置**

| 动作组 | 类型 | 关键参数 |
| --- | --- | --- |
| AG_Arp_Special | Arp | priorityLevel=2, preemptCap=MAY_PREEMPT, preemptVuln=NOT_PREEMPTABLE |
| AG_Qos_Special | QoSData | 5qi=4, maxbrUL/DL=100 Mbps, gbrUL/DL=100 Mbps |
| AG_ADC_Special | DynamicPccRule | appId=flow_ADC, precedence=1, refQosData=AG_Qos_Special |

**（3）策略3 Policy_ADC_Stop**

仅1个规则Rule_ADC_Stop_PCC，类型为Non-PCC，EDR=OFF。

**（4）业务配置与开户**

```
业务名：ADC_Service
类型：BASIC_SERVICE
QoS模式：替换
策略：Policy_ADC_Normal + Policy_ADC_Start + Policy_ADC_Stop
```

开户签约MML：
```
ADD PSUB:USRIDENTIFIER="46000120010****", USRMSISDN="861390010****", USRSTATE=Normal, ...;
ADD PSRV: USRIDENTIFIER="46000120010****", SRVNAME="ADC_Service", SRVUSAGESTATE=Normal;
```

### 3.2 ADC方案 -- SMF侧配置（UNC MML）

```
// 1. 开启PCC License和ADC License
SET LICENSESWITCH:LICITEM="LKV3W9SPCC11", SWITCH=ENABLE;
SET LICENSESWITCH:LICITEM="LKV2BADCF01",SWITCH=ENABLE;

// 2. 使能全局PCC开关
SET PCCFUNC:HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=ENABLE,VISITPCCSWITCH=ENABLE,N7FAILOVERSW=ENABLE;

// 3.（可选）使能APN级PCC开关
SET APNPCCFUNC: APN="cmnet", HOMEPCCSWITCH=ENABLE, ROAMPCCSWITCH=ENABLE, VISITPCCSWITCH=ENABLE;

// 4. 配置ADC流过滤器（appId映射）
ADD FLOWFILTER:FLOWFILTERNAME="flow_ADC";

// 5. 开启流信息上报开关
ADD ADCPARA: FLOWFILTERNAME="flow_ADC",FLOWINFORPT=ENABLE;
```

**关键约束**：SMF、UPF、PCF三个网元上的FlowFilterName必须一致。

### 3.3 ADC方案 -- UPF侧配置（UDG MML）

**方式一：L3/L4层过滤（基于服务器IP）**

```
// 1. 开启License
SET LICENSESWITCH:LICITEM="LKV3G5PCCB01",SWITCH=ENABLE;
SET LICENSESWITCH:LICITEM="LKV3G5ADCF01",SWITCH=ENABLE;

// 2. 配置三四层过滤条件
ADD FILTER: FILTERNAME="filter_test1", L34PROTTYPE=STRING, L34PROTOCOL=ANY, SVRIPMODE=IP, SVRIP="10.27.3.56", SVRIPMASKTYPE=LENGTHTYPE, SVRIPMASKLEN=32, MSSTARTPORT=0, MSENDPORT=65535, SVRSTARTPORT=0, SVRENDPORT=65535;

// 3. 配置流分类器
ADD FLOWFILTER:FLOWFILTERNAME="flow_ADC";

// 4. 绑定三四层过滤信息
ADD FLTBINDFLOWF:FLOWFILTERNAME="flow_ADC",FILTERNAME="filter_test1";

// 5. 刷新生效
SET REFRESHSRV:REFRESHTYPE=ALL;
```

**方式二：L7层过滤（基于URL）**

```
// 1. 配置七层过滤器
ADD L7FILTER:L7FILTERNAME="l7filter_test_01",SUBL7FLTNAME="sl7_test_1",URL="www.huawei.com";

// 2. 配置流分类器
ADD FLOWFILTER:FLOWFILTERNAME="flow_ADC";

// 3. 绑定七层过滤信息
ADD PROTBINDFLOWF:FLOWFILTERNAME="flow_ADC",PROTOCOLNAME="http",L7FILTERNAME="l7filter_test_01";

// 4. 刷新生效
SET REFRESHSRV:REFRESHTYPE=ALL;
```

> 两种方式根据实际业务流特征选择其一。修改完流信息后必须执行SET REFRESHSRV刷新才能立即生效。

### 3.4 ADC方案 -- 快速调测流程

调测分为三个阶段验证（上线/开始访问特定视频/停止访问特定视频），每阶段执行以下检查：

**步骤1 -- 检查签约**：`LST PSRV` 查询用户签约业务名为ADC_Service

**步骤2 -- 检查SMF规则安装**：
```
DSP PCCSESSINFO:USERIDTYPE=IMSI,IMSI="46000120010****";
```
- 用户上线（未访问特定视频）：应显示2条动态规则（AG_ADC_AppId, AG_ADC_Normal），1个QoS Flow（QFI=1, 5QI=9）
- 开始访问特定视频：应显示3条动态规则（增加AG_ADC_Special），2个QoS Flow（QFI=1保持普通, QFI=2为5QI=4专有流）
- 停止访问特定视频：回到2条规则状态

**步骤3 -- 检查SMF会话QoS**：
```
DSP SESSIONQOSINFO: QUERYTYPE=IMSI, IMSI="46000120010****", WLNETWKTYPE=NW5G, PDUSESSIONID=5;
```

**步骤4 -- 检查UPF用户上下文**：
```
DSP SESSIONINFO:QUERYTYPE=IMSI,IMSI="46000120010****";
```
UPF侧可看到带APP ID=flow_adc的PDR，以及APN Session级QER限速。

**步骤5 -- 业务体验验证**：使用测速软件验证实际网速（1 Mbit/s 或 100 Mbit/s）

### 3.5 位置区域方案 -- PCF侧配置

配置顺序：PLMN > 漫游区 > 条件组 > 5G动作组 > 规则 > 策略 > 业务 > 开户

**（1）位置管理配置**

```
PLMN_1: MCC=460, MNC=003, 类型=Local
PLMN_2: MCC=460, MNC=002, 类型=Local
漫游区 Region_Local: 关联 PLMN_1 + PLMN_2
```

**（2）条件组配置**

| 条件组 | 条件 | 操作符 | 右值 |
| --- | --- | --- | --- |
| CG_Local | SmfSession.RoamingRegion | Equal | Region_Local |
| CG_Roaming | SmfSession.RoamingRegion | Not Equal | Region_Local |

**（3）5G动作组配置**

| 动作组 | 类型 | pccRuleId |
| --- | --- | --- |
| AG_Local | PredefinedPccRule | Predefined1 |
| AG_Roaming | PredefinedPccRule | Predefined2 |

> 预定义规则名须与SMF/UPF侧规划一致。

**（4）规则配置**

| 规则 | 条件组 | 动作组 |
| --- | --- | --- |
| PrePCC_Rule1 | CG_Local | AG_Local（下发Predefined1） |
| PrePCC_Rule2 | CG_Roaming | AG_Roaming（下发Predefined2） |

**（5）策略与业务**

```
策略 Policy_Location:
  触发器：IPCAN_EST + PLMN_CH
  规则：PrePCC_Rule1 + PrePCC_Rule2

业务 Location_Service:
  类型：VALUE_ADDED_SERVICE
  策略：Policy_Location
```

### 3.6 位置区域方案 -- SMF侧配置（UNC MML）

```
// 1. 开启License
SET LICENSESWITCH:LICITEM="LKV2FUPSAT01",SWITCH=ENABLE;

// 2. 打开PCC功能开关
SET PCCFUNC: HOMEPCCSWITCH=ENABLE;

// 3. 配置QoS URR
ADD URR:URRNAME="urr_QoS2", URRID=2, USAGERPTMODE=QOS;
ADD URR:URRNAME="urr_QoS3", URRID=3, USAGERPTMODE=QOS;

// 4. 配置QoS参数（国内100M）
ADD QOSPROP: QOSPROPNAME="qosprop_5qi5_arp2_100", MBRUPLKVALUE=100000, MBRDNLKVALUE=100000, QOSTYPE=QOS_FLOW_PARA, ARPVALUE=2, FQI=5, QOSURRNAME="urr_QoS2";

// 5. 配置QoS参数（漫游1M）
ADD QOSPROP: QOSPROPNAME="qosprop_5qi5_arp2_1", MBRUPLKVALUE=1000, MBRDNLKVALUE=1000, QOSTYPE=QOS_FLOW_PARA, ARPVALUE=2, FQI=5, QOSURRNAME="urr_QoS3";

// 6. 配置PCC策略组
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccfuppolicy_100M", QOSPROPNAME="qosprop_5qi5_arp2_100";
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccfuppolicy_1M", QOSPROPNAME="qosprop_5qi5_arp2_1";

// 7. 配置预定义规则
ADD RULE:RULENAME="Predefined1",POLICYTYPE=PCC,PRIORITY=10,POLICYNAME="pccfuppolicy_100M";
ADD RULE:RULENAME="Predefined2",POLICYTYPE=PCC,PRIORITY=10,POLICYNAME="pccfuppolicy_1M";
```

> MBR单位为kbps：100000 kbps = 100 Mbit/s，1000 kbps = 1 Mbit/s。

### 3.7 位置区域方案 -- 调测方法

**信令调测法**：
1. 在PCF/SMF/UPF建立消息跟踪任务
2. 用户从国内上线，观察PCF侧Npcf_SMPolicyControl_Create Response下发Predefined1
3. SMF通过PFCP Session Establishment Request将Predefined1下发给UPF（含activate-predefined-rules信元）
4. 用户移动到国外，UPF上报PLMN_CH事件 -> SMF转发给PCF -> PCF安装Predefined2、删除Predefined1

**快速调测法**：
1. `LST PSRV` 查询签约Location_Service
2. 用户从国内上线，`DSP PCCSESSINFO` 查询SMF安装Predefined1
3. `DSP SESSIONQOSINFO` 查询会话AMBR=2000000 Kbps
4. `DSP SESSIONINFO` 查询UPF侧QER限速=2000000kbps
5. 测速验证约100 Mbit/s
6. 用户从国外区域上线，验证下发Predefined2，测速约1 Mbit/s

---

## 4. 与带宽控制的关系

### 4.1 在带宽控制场景中的定位

这两个E2E方案是带宽控制场景（套餐2）中**最核心的典型实现案例**：

| 方案 | 带宽控制维度 | 技术路径 | 对应特性 |
| --- | --- | --- | --- |
| ADC带宽差异化 | 业务类别（应用类型） | 动态规则 + ADC检测 | GWFD-020357 ADC基本功能（UPF）、WSFD-109102 ADC基本功能（SMF） |
| 位置区域带宽差异化 | 位置区域（国内/漫游） | 预定义规则 + PLMN判断 | WSFD-109101 PCC基本功能（SMF） |

### 4.2 与带宽控制特性的关联

ADC方案直接依赖带宽控制场景的核心特性链：
- **ADC基本功能**（GWFD-020357/WSFD-109102）：提供应用流检测能力
- **PCC基本功能**（WSFD-109101）：提供PCC策略框架
- **PCC规则下发**：动态规则方式实现精细带宽控制
- **QoS Flow管理**：通过5QI=4建立专有QoS Flow提供GBR保障

位置区域方案展示了另一种带宽控制路径：
- **预定义规则方式**：规则内容在SMF/UPF本地预配置，PCF仅下发规则名
- **位置感知**：通过PLMN/漫游区配置实现位置触发的策略切换

### 4.3 与其他E2E方案的协同

这两个方案展示了带宽控制的两种典型实现范式（动态规则 vs 预定义规则），与带宽控制场景中的其他方案（如FUP用量阈值带宽切换、BWM带宽管理、Shaping流量整形等）形成互补。实际部署中，ADC方案可与FUP方案组合（如：检测到特定应用且未达FUP阈值时提供高带宽），也可与位置区域方案组合（如：漫游时降低所有应用带宽）。

---

## 5. 关键术语

| 术语 | 简释 |
| --- | --- |
| ADC（Application Detection and Control） | 应用检测与控制，UPF通过L3/L4或L7协议识别应用数据流，实现基于应用的QoS控制 |
| PCC（Policy and Charging Control） | 策略与计费控制，3GPP定义的策略框架，包含PCC规则、QoS控制、计费控制等 |
| UPCF（Unified Policy Control Function） | 华为统一策略控制功能，即5G PCF的华为产品名称 |
| DynamicPccRule | 动态PCC规则，规则内容由PCF定义并通过N7/N4接口下发 |
| PredefinedPccRule | 预定义PCC规则，规则内容在SMF/UPF本地预配置，PCF仅下发规则标识 |
| IPCAN_EST | IP-CAN Session Establishment触发器，用户PDU会话建立时触发PCF策略计算 |
| APP_STA | Application Start触发器，UPF检测到用户开始访问特定应用流时上报 |
| APP_STO | Application Stop触发器，UPF检测到用户停止访问特定应用流时上报 |
| PLMN_CH | PLMN Change触发器，用户位置区域（PLMN）发生变化时触发策略更新 |
| 5QI | 5G QoS Identifier，5QI=9为非GBR默认QoS，5QI=4为非GBR但可建立专有QoS Flow |
| MBR（Maximum Bit Rate） | 最大比特率，包括上下行最大速率限制 |
| GBR（Guaranteed Bit Rate） | 保证比特率，5QI=4场景下的上下行保障带宽 |
| FlowFilter | 流过滤器，SMF/UPF上配置的应用流标识，三侧名称需一致 |
| appId | 应用标识，PCF动态规则中携带的应用流标识，映射到UPF本地FlowFilter |
| QER（QoS Enforcement Rule） | QoS执行规则，UPF上实际执行限速的规则实体 |
| PDR（Packet Detection Rule） | 报文检测规则，UPF上检测和分类用户面报文的规则 |
| FAR（Forwarding Action Rule） | 转发动作规则，UPF上定义报文转发行为的规则 |
| RoamingRegion | 漫游区，UPCF位置管理中定义的区域分组，用于位置条件判断 |
| Non-PCC规则 | 非PCC类型规则，用于删除已有规则（如Rule_ADC_Stop_PCC） |

---

## 6. 知识来源

| 序号 | 文件名 | 所属方案 |
| --- | --- | --- |
| 1 | 需求描述_08571740.md | ADC带宽差异化控制 |
| 2 | 整体方案设计_08571770.md | ADC带宽差异化控制 |
| 3 | PCF侧业务配置_08571772.md | ADC带宽差异化控制 |
| 4 | SMF侧业务配置_13928808.md | ADC带宽差异化控制 |
| 5 | UPF侧业务配置_13928809.md | ADC带宽差异化控制 |
| 6 | 快速调测方法_08571775.md | ADC带宽差异化控制 |
| 7 | PCF侧业务配置_08571779.md | 位置区域带宽差异化控制 |
| 8 | SMF侧业务配置_08571780.md | 位置区域带宽差异化控制 |
| 9 | 信令调测方法_08571765.md | 位置区域带宽差异化控制 |
| 10 | 快速调测方法_08571782.md | 位置区域带宽差异化控制 |

> 原始路径前缀：`output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/`
