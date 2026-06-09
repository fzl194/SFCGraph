# Batch-18: UDG业务感知专题 -- 规则匹配流程与套餐配置

## 1. 概述

本批文档来源于"UDG业务感知专题"，涵盖业务感知功能的核心概念（规则、过滤条件）和端到端过程（业务解析与识别、规则匹配、策略执行、规则规划与获取），以及业务感知配置中的特征库加载和套餐配置实例。

具体内容覆盖以下主题：

- **规则（Rule）**：业务感知规则的结构定义、字段含义、策略类型体系。
- **过滤条件（Filter）**：三四层过滤器、七层过滤器、协议/协议组、流过滤器（组）的层级关系和组合逻辑。
- **业务感知过程总览**：从规则下发到报文识别、规则匹配、策略执行、数据转发的端到端流程。
- **业务解析与识别流程**：三四层解析、协议识别、七层解析的三级识别体系。
- **规则匹配流程**：单一规则匹配、多条同类型规则匹配（优先级机制）、多条不同类型规则匹配（叠加生效）的三层匹配模型。
- **策略执行流程**：匹配成功后将策略动作（计费、带宽控制、重定向、头增强等）实施到报文的过程。
- **规则规划与获取**：规则部署架构、自下而上的配置方法论、PCF/SMF/UPF三网元间的规则下发与一致性规划。
- **加载特征库**：业务感知前置条件，SA协议特征库的加载与验证。
- **套餐1计费场景配置实例**：4个业务、4条规则、优先级递减的完整MML配置脚本，是套餐2带宽控制场景的直接参照模板。

---

## 2. 核心知识点

### 2.1 规则（Rule）的概念与结构

规则是业务感知的核心载体，由**条件**和**动作**两部分组成，决定满足哪些条件的报文执行哪些动作。一条规则包含以下关键字段：

| 字段 | 说明 |
|------|------|
| **规则名称（Rule Name）** | 规则的唯一标识，用于策略绑定、User Profile绑定、查询/修改/删除 |
| **策略类型（Policytype）** | 决定规则的策略方向，UDG支持PCC、BWM、HEADEN、WEBPROXY、SMARTREDIRECT、ADC、WORKER七种 |
| **策略名称（Policy）** | 已配置策略的绑定引用，随策略类型变化（如PCC对应PCC策略组名，BWM对应分类属性名） |
| **优先级（Priority）** | 相同策略类型的规则中，取值越小优先级越高，高优先级规则命中后终止匹配 |
| **流过滤器（组）** | 绑定的过滤条件组合，决定报文匹配范围 |
| **其他参数** | 规则生效时间段、RADIUS消息触发标识、默认动作、重定向地址、Remark配置等 |

**策略类型体系**是理解规则的关键。对于带宽控制场景，最核心的策略类型是 **BWM**（带宽管理），其策略名称为 `ADD CATEGORYPROP` 配置的分类属性名称，分类结果用于带宽管理的策略匹配。其次是 **PCC**（计费与策略控制），用于计费场景。

**关键MML命令**：`ADD RULE` -- 配置规则，将流过滤器、策略、优先级绑定到一起。

### 2.2 过滤条件（Filter）的层级体系

过滤条件是规则匹配报文的判定依据，采用多层组合架构：

```
Rule
 |-- Flow Filter (Group)
      |-- Filter / Filter Group        (三四层)
      |-- Protocol / Protocol Group     (七层协议)
      |-- L7 Filter                     (七层关键字段)
      |-- IPv6 Filter                   (可选，IPv6报文)
```

**各层过滤器职责**：

- **Filter（三四层过滤器）**：配置源/目的IP地址、源/目的端口号、4层协议类型（TCP/UDP/ICMP等）。
- **Filter Group（过滤器组）**：多个Filter组合，支持与/或/非逻辑关系。
- **L7 Filter（七层过滤器）**：配置URL、User-Agent、method等七层关键字段，支持子七层过滤器区分配置。
- **Protocol（协议）**：应用层协议，如HTTP、FTP、RTSP等，内容取决于L7 Filter需求。
- **Protocol Group（协议组）**：由SA特征库预置的应用协议组合，定期更新特征库即可维护。
- **Flow Filter（流过滤器）**：Filter、L7 Filter、Protocol、Protocol Group的绑定组合，实现三四层+七层联合过滤。不需要过滤的内容配置为Any或不配置。
- **Flow Filter Group（流过滤器组）**：多个Flow Filter组合，组内支持与/或/非逻辑。

**逻辑关系说明**：
- **与**：组内所有流过滤器都命中才算命中
- **或**：组内任一流过滤器命中即算命中
- **非**：组内所有流过滤器都不命中才算命中

**SA特征库预置的应用协议组合**覆盖：HTTP Pipeline/WAP Concatenation、Web Browsing、File Access、Mobile、Streaming、P2P、VoIP、Email、IM、Game、QUIC等十余大类。对于带宽控制场景，Streaming（大带宽）、P2P（带宽占用）、File Access（带宽限制）等协议组尤为关键。

### 2.3 业务感知过程总览（端到端）

业务感知从功能生效角度分为以下完整流程：

```
规则规划与获取 → 报文到达UPF → 解析与识别 → 规则匹配 → 策略执行 → 数据转发 → 使用量上报
```

**详细步骤**：

1. **规则下发**：用户接入时，PCF下发规则经SMF"翻译"后到UPF，存入规则库。规则往往多条、多类型。
2. **报文到达**：用户接入完成、开始会话后，数据报文经基站到达UPF。
3. **解析与识别**：UPF对报文进行三四层解析、协议识别、七层解析，获取报文特征。
4. **规则匹配**：UPF将报文特征与规则库中规则（绑定过滤条件、策略、优先级）进行匹配。
5. **策略执行**：成功匹配的报文执行对应策略（计费、阻塞/重定向、带宽控制、头增强等）。
6. **数据转发**：用户数据从UPF继续转发到网络/业务服务器。
7. **使用量上报**：UPF定期向SMF上报用户使用情况（计费套餐用量、使用时长、具体时间等）。

### 2.4 业务解析与识别流程（三级识别）

业务感知的解析与识别分为三大类，层层递进：

**第一级：三四层解析（浅度报文检测）**

- **三层（网络层）**：监控IP报文的源/目的IP地址。
- **四层（传输层）**：检测报文段的协议端口号。
- 获取信息：源IP地址、目的IP地址、IP协议类型（TCP/UDP/ICMP等）、源端口号范围、目的端口号范围。

**第二级：协议/协议组识别**

- 只有识别出用户报文的协议后，才能对报文做精确的业务感知。
- 识别方式依赖SA特征库中的协议签名。

**第三级：七层解析（精确业务感知）**

- 在三四层解析和协议识别后，对报文进行精确的业务感知。
- 获取七层协议类型、目的URL等有价值信息。
- 对每个请求和响应解析关键字段：URL、Method、响应码。

**前缀URL处理**：若报文包含代理服务器交互，SA解析得到的URL可能包含前缀URL（代理服务器域名）和真实URL。需检测并剥离前缀URL，采用真实URL进行策略匹配。

**性能参考**：典型话务模型下，所有报文都进行解析识别和规则匹配，约20-30%报文需要协议识别/解析，其中约15-20%需要协议解析。

### 2.5 规则匹配流程（三层匹配模型）-- 带宽控制核心环节

规则匹配是带宽控制场景的核心环节，决定了哪些报文最终受带宽策略控制。匹配流程分为三个层次：

**第一层：单一规则匹配**

```
报文到达 → 提取L3/4五元组 → 匹配/创建流表 → 判断是否需要SA处理
  → 不需要：保存策略到流表
  → 需要：SA处理 → 策略匹配 → 保存到流表
```

- 所有报文都需要通过五元组（源/目的IP、端口、协议类型）匹配或生成流表。
- 首包匹配流表失败后创建新流表，匹配策略判断是否需要SA处理。
- 后续报文匹配流表成功后，根据流表标识判断是否继续协议识别/解析。

**第二层：多条同类型规则匹配（优先级机制）**

- 存在多条相同策略类型的规则时，按优先级取值由低到高（取值越小优先级越高）逐条匹配。
- 报文命中优先级高的规则后，该规则生效，匹配终止。
- 未命中则继续匹配优先级低的规则，直到命中。
- **关键：同类型规则只有一条最终生效。**

**第三层：多条不同类型规则匹配（叠加生效）**

- 不同策略类型的规则之间独立匹配。
- 如果一条规则配置了多个策略类型，该规则分别参与每个策略类型的匹配。
- **关键：不同策略类型的规则叠加生效。**
- 最终结果：相同策略类型只有一条规则生效，不同策略类型的规则各自独立生效。

**对带宽控制的意义**：一条报文可以同时命中PCC规则和BWM规则。例如，PCC规则执行计费，BWM规则执行带宽限制，两者叠加生效互不冲突。这是套餐2带宽控制场景的理论基础。

### 2.6 策略执行流程

规则匹配成功后，UPF根据规则绑定的策略和用户QoS策略执行动作：

- 将数据包从GTP隧道映射到符合策略的QoS流
- 执行规则定义的动作：**计费、QoS控制、带宽控制、重定向、头增强**等

不同策略类型的规则执行动作方式不同，具体由各策略类型绑定的策略对象决定。策略执行完成后，业务感知功能实现完成。

**对带宽控制的意义**：BWM类型规则匹配成功后，对应的分类属性（CategoryProp）生效，分类结果输入到带宽管理策略匹配，触发具体的带宽限制动作（限速、整形等）。

### 2.7 规则规划与获取

#### 2.7.1 规则规划逻辑

业务感知部署架构包含三部分：

```
用户类型（User Profile/Group/APN）
  └── Rule
       ├── 流过滤器（组）（Flow Filter/Flow Filter Group）
       ├── 策略类型（Policytype）和策略名称（Policy）
       └── 全局优先级（Priority）
            ├── 过滤条件
            │    ├── 三/四层过滤器（组）
            │    ├── 协议/协议组
            │    └── 七层过滤器
```

**配置顺序要求自下而上**：

1. 先配置三四层过滤器（组）、七层流过滤器、协议或协议组，绑定到流过滤器（组）。
2. 将流过滤器（组）、策略、优先级和其他参数绑定到Rule。
3. 根据用户组、APN类型，将规则绑定到User Profile（Group）和APN。

**配置前置条件**：加载完成业务感知特征库，确保使用到的License已打开。

#### 2.7.2 规则类型与获取

从PCF视角，可下发的规则有三种：

| 类型 | 说明 | 特点 |
|------|------|------|
| **预定义规则** | 部署流程中规划的规则 | 部署完成后默认未启用，需PCF控制启用/停用 |
| **动态规则** | 与预定义规则互补 | 可在用户激活/会话过程中由PCF灵活下发 |
| **本地规则** | 在UPF/SMF上配置 | 当SMF无法从PCF获取规则或网络中无PCF时启用 |

#### 2.7.3 规则下发流程（5G核心网）

规则下发与QoS策略下发完全耦合，涉及4个流程：PDU会话建立、PDU会话修改、PCFP会话建立、PCFP会话修改。

**会话建立时**：

1. SMF从UDM获取签约QoS信息，向PCF发送Npcf_SMPolicyControl_Create Request（含已配置PCC规则）。
2. PCF根据用户信息生成条件，结合SMF提供的预定义规则生成完整QoS策略，通过Npcf_SMPolicyControl_Create Response下发。
3. SMF通过PFCP Session Establishment Request的Create PDR信元下发到UPF（动态规则可能同时下发Create URR、Create QER）。
4. UPF返回PFCP Session Establishment Response。
5. 开始建立PDU会话，UPF根据策略中Trigger定期上报使用量。

**会话过程中**：

1. 策略变更发起方（UE/SMF/PCF/基站）将变更需求传递到SMF。
2. SMF发送Npcf_SMPolicyControl_Update Request给PCF。
3. PCF通过Npcf_SMPolicyControl_Update Response下发新规则。
4. SMF向UPF发送PFCP Session Modification Request（含Remove/Create/Update PDR等信元）。
5. UPF更新PFCP会话上下文，返回PFCP Session Modification Response。

#### 2.7.4 用户面/控制面统一规划

5G网络中控制面和用户面解耦，UPF只能完成规则属性和过滤条件的部署。用户类型部署和部分策略参数部署需要在SMF、PCF上完成。

**需要三网元规划一致的参数**：APN/VPN、FlowFilter（5G映射为Gx接口appid）、ServiceProp、Rule、UserProfile、QosProp、BwmUserGroup、CbbID（URRID）。

**CP/UP配置不一致的处理**：
- UDG产生 ALM-81054 告警。
- 可用 `SET CUINCONSPOLICY` 命令控制不一致时的处理策略。

### 2.8 加载特征库

特征库加载是业务感知配置的前置条件。

**加载步骤**：

1. 执行 `LOD SIGNATUREDB` 加载指定版本协议特征库：
   ```
   LOD SIGNATUREDB:LOADMODE=SPECIFIC,VERSION="01.0002.1209.01"
   ```
2. 等待5分钟后，执行 `DSP SIGNATUREDB` 查询加载状态：
   ```
   DSP SIGNATUREDB:;
   ```
3. 确认返回结果中"特征库加载状态 = 加载完成"。

**特征库更新**：特征库经常更新，需要定期重新加载刷新内容。详细操作参考配套版本的《协议特征库加载指导书》。

### 2.9 套餐1计费场景配置实例 -- 套餐2带宽控制的直接参照

#### 2.9.1 场景描述

运营商需要部署离线计费业务套餐，包含4个业务：

| 业务编号 | 过滤条件 | 策略 | 优先级 |
|----------|----------|------|--------|
| 业务1 | 七层：https://www.huawei.com | PCC，1元/GB | 最高 |
| 业务2 | 协议：HTTP | PCC，0.5元/GB | 高 |
| 业务3 | 三四层：10.123.234.10~13 或 协议：RTSP | PCC，免费 | 中 |
| 业务4 | 任意（兜底） | PCC，0.1元/GB | 低 |

#### 2.9.2 配置分析

| 配置项 | 业务1 | 业务2 | 业务3 | 业务4 |
|--------|-------|-------|-------|-------|
| 三四层过滤器 | filterA | filterA | filterC / filterA | filterA |
| 七层过滤器 | l7filterA | 无（仅协议） | 无（仅协议） | 无 |
| 流过滤器 | flowfilterA | flowfilterB | flowfiltergroupC | flowfilterD |
| URR ID | urrA=1000 | urrB=2000 | urrC=4000(免费) | urrD=3000 |
| PCC策略组 | pccgA | pccgB | pccgC | pccgD |
| 优先级 | 100 | 200 | 300 | 400 |

#### 2.9.3 完整配置脚本（8步）

**步骤1：配置IP地址列表**
```
ADD IPLIST:IPLISTNAME="iplistB",IPVERSION=IPV4,IPV4ADDR="10.123.234.10",MASKVALUE=32;
ADD IPLIST:IPLISTNAME="iplistB",IPVERSION=IPV4,IPV4ADDR="10.123.234.11",MASKVALUE=32;
ADD IPLIST:IPLISTNAME="iplistB",IPVERSION=IPV4,IPV4ADDR="10.123.234.12",MASKVALUE=32;
ADD IPLIST:IPLISTNAME="iplistB",IPVERSION=IPV4,IPV4ADDR="10.123.234.13",MASKVALUE=32;
```

**步骤2：配置三四层过滤条件**
```
ADD FILTER:FILTERNAME="filterA",L34PROTTYPE=STRING,L34PROTOCOL=ANY;
ADD FILTER:FILTERNAME="filterC",L34PROTTYPE=STRING,L34PROTOCOL=TCP,SVRIPMODE=IPLIST,SVRIPLISTNAME="iplistB";
```

**步骤3：配置七层过滤条件**
```
ADD L7FILTER:L7FILTERNAME="l7filterA",SUBL7FLTNAME="sl7A",URLTYPE=URL,URL="www.huawei.com/*";
```

**步骤4：配置流过滤器（组），绑定三四层与七层**
```
// 业务1
ADD FLOWFILTER:FLOWFILTERNAME="flowfilterA";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilterA",FILTERNAME="filterA";
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilterA",PROTOCOLNAME="HTTPS",L7FILTERNAME="l7filterA";

// 业务2
ADD FLOWFILTER:FLOWFILTERNAME="flowfilterB";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilterB",FILTERNAME="filterA";
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilterB",PROTOCOLNAME="HTTP";

// 业务3（流过滤器组，与逻辑）
ADD FLOWFILTER:FLOWFILTERNAME="flowfilterC1";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilterC1",FILTERNAME="filterC";
ADD FLOWFILTER:FLOWFILTERNAME="flowfilterC2";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilterC2",FILTERNAME="filterA";
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilterC2",PROTOCOLNAME="RTSP";
ADD FLOWFILTERGRP:FLWFLTRGRPNAME="flowfiltergroupC",FLOWFILTERNAME="flowfilterC1";
ADD FLOWFILTERGRP:FLWFLTRGRPNAME="flowfiltergroupC",FLOWFILTERNAME="flowfilterC2";

// 业务4（兜底）
ADD FLOWFILTER:FLOWFILTERNAME="flowfilterD";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilterD",FILTERNAME="filterA";
```

**步骤5：配置流动作（URR + URRGroup + PCCPolicyGroup）**
```
// 业务1
ADD URR:URRNAME="urrA",URRID=1000,USAGERPTMODE=OFFLINE;
ADD URRGROUP:URRGROUPNAME="urrgA",UPURRNAME1="urrA",DOWNURRNAME1="urrA";
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccgA",URRGROUPNAME="urrgA";

// 业务2
ADD URR:URRNAME="urrB",URRID=2000,USAGERPTMODE=OFFLINE;
ADD URRGROUP:URRGROUPNAME="urrgB",UPURRNAME1="urrB",DOWNURRNAME1="urrB";
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccgB",URRGROUPNAME="urrgB";

// 业务3（免费计费）
ADD URR:URRNAME="urrC",URRID=4000,USAGERPTMODE=OFFLINE,OFFMETERINGTYPE=FREE;
ADD URRGROUP:URRGROUPNAME="urrgC",UPURRNAME1="urrC",DOWNURRNAME1="urrC";
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccgC",URRGROUPNAME="urrgC";

// 业务4
ADD URR:URRNAME="urrD",URRID=3000,USAGERPTMODE=OFFLINE;
ADD URRGROUP:URRGROUPNAME="urrgD",UPURRNAME1="urrD",DOWNURRNAME1="urrD";
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccgD",URRGROUPNAME="urrgD";
```

**步骤6：将过滤条件与流动作绑定成Rule**
```
ADD RULE:RULENAME="ruleA",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilterA",POLICYNAME="pccgA",PRIORITY=100;
ADD RULE:RULENAME="ruleB",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilterB",POLICYNAME="pccgB",PRIORITY=200;
ADD RULE:RULENAME="ruleC",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTERGRP,FLWFLTRGRPNAME="flowfiltergroupC",POLICYNAME="pccgC",PRIORITY=300;
ADD RULE:RULENAME="ruleD",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilterD",POLICYNAME="pccgD",PRIORITY=400;
```

**步骤7：配置User Profile，绑定默认策略**
```
ADD USERPROFILE:USERPROFILENAME="up_charging";
SET URRGRPBINDING:USERPROFILENAME="up_charging",DFTURRGRPNAME="urrgD",DFTSIGURRGNAME="urrgD";
```

**步骤8：将Rule绑定到User Profile，刷新生效**
```
ADD RULEBINDING:USERPROFILENAME="up_charging",RULENAME="ruleA",POLICYTYPE=PCC;
ADD RULEBINDING:USERPROFILENAME="up_charging",RULENAME="ruleB",POLICYTYPE=PCC;
ADD RULEBINDING:USERPROFILENAME="up_charging",RULENAME="ruleC",POLICYTYPE=PCC;
ADD RULEBINDING:USERPROFILENAME="up_charging",RULENAME="ruleD",POLICYTYPE=PCC;
SET REFRESHSRV:REFRESHTYPE=USERPROFILE;
```

#### 2.9.4 套餐1对套餐2（带宽控制）的参照价值

套餐1的配置模式可直接迁移到套餐2带宽控制场景，核心差异在于**策略类型从PCC变为BWM**：

| 维度 | 套餐1（计费） | 套餐2（带宽控制） |
|------|---------------|-------------------|
| 策略类型 | PCC | BWM |
| 策略对象 | URR + URRGroup + PCCPolicyGroup | CategoryProp（分类属性） |
| 动作 | 计费（费率/免费） | 带宽限制（限速/整形/保证速率） |
| 过滤条件 | 完全相同（Filter/FlowFilter/Protocol/L7Filter） | 完全相同 |
| Rule配置 | POLICYTYPE=PCC | POLICYTYPE=BWM |
| 优先级机制 | 完全相同（取值越小优先级越高） | 完全相同 |
| User Profile绑定 | 完全相同 | 完全相同 |

**可复用的配置步骤（步骤1-4、7-8完全一致）**：
- 步骤1-2：IP列表 + 三四层过滤器 -- 完全复用
- 步骤3：七层过滤器 -- 完全复用
- 步骤4：流过滤器（组） -- 完全复用
- 步骤6：ADD RULE -- 结构一致，仅POLICYTYPE和POLICYNAME不同
- 步骤7-8：User Profile + RuleBinding -- 完全复用

**需要替换的配置步骤**：
- 步骤5：从"URR + URRGroup + PCCPolicyGroup"替换为"CategoryProp（分类属性）"

---

## 3. 配置调测要点

### 3.1 规则配置要素

配置业务感知规则时，必须遵循以下要素：

1. **前置条件**：先加载SA特征库（`LOD SIGNATUREDB`），确保License已打开。
2. **自下而上**：先配过滤器，再配流过滤器，再配规则，最后绑User Profile。
3. **策略类型选择**：带宽控制场景使用BWM类型，计费场景使用PCC类型，可共存叠加。
4. **优先级规划**：相同策略类型内，取值越小优先级越高，高优先级命中后终止匹配。
5. **兜底策略**：配置最低优先级的兜底规则，三四层过滤为ANY，确保未命中其他规则的报文有默认处理。

### 3.2 过滤条件配置

| 过滤类型 | MML命令 | 关键参数 |
|----------|---------|----------|
| IP地址列表 | `ADD IPLIST` | IPLISTNAME, IPV4ADDR, MASKVALUE |
| 三四层过滤器 | `ADD FILTER` | FILTERNAME, L34PROTTYPE, L34PROTOCOL, SVRIPMODE, SVRIPLISTNAME |
| 七层过滤器 | `ADD L7FILTER` | L7FILTERNAME, SUBL7FLTNAME, URLTYPE, URL |
| 流过滤器 | `ADD FLOWFILTER` | FLOWFILTERNAME |
| 过滤器绑定流过滤器 | `ADD FLTBINDFLOWF` | FLOWFILTERNAME, FILTERNAME |
| 协议绑定流过滤器 | `ADD PROTBINDFLOWF` | FLOWFILTERNAME, PROTOCOLNAME, L7FILTERNAME |
| 流过滤器组 | `ADD FLOWFILTERGRP` | FLWFLTRGRPNAME, FLOWFILTERNAME |

### 3.3 特征库加载命令

| 命令 | 用途 | 示例 |
|------|------|------|
| `LOD SIGNATUREDB` | 加载协议特征库 | `LOD SIGNATUREDB:LOADMODE=SPECIFIC,VERSION="01.0002.1209.01"` |
| `DSP SIGNATUREDB` | 查询特征库加载状态 | `DSP SIGNATUREDB:;` |

### 3.4 规则与绑定命令

| 命令 | 用途 |
|------|------|
| `ADD RULE` | 配置规则，绑定流过滤器、策略类型、策略名称、优先级 |
| `ADD USERPROFILE` | 创建用户配置文件 |
| `ADD RULEBINDING` | 将规则绑定到User Profile |
| `SET URRGRPBINDING` | 配置User Profile的默认URR组（兜底计费） |
| `SET REFRESHSRV` | 刷新配置使策略生效（必须最后执行） |

### 3.5 CP/UP配置一致性

| 命令 | 用途 |
|------|------|
| `SET CUINCONSPOLICY` | 设置CP和UP关键配置不一致时的处理策略 |

当CP/UP配置不一致时，UDG产生ALM-81054告警。

---

## 4. 与带宽控制的关系

### 4.1 规则匹配是带宽控制的核心环节

带宽控制的完整链路为：**识别业务 -> 匹配规则 -> 执行带宽动作**。

- **识别业务**：通过三四层解析、协议识别、七层解析，获取报文特征。
- **匹配规则**：将报文特征与规则库中BWM类型规则的过滤条件进行匹配，按优先级确定生效规则。
- **执行带宽动作**：匹配成功的报文，根据BWM策略绑定的分类属性，触发带宽限制动作（限速、整形、保证速率等）。

规则匹配流程中的**三层匹配模型**确保带宽控制可以与其他策略（计费、重定向等）叠加生效。例如，一条视频流报文可以同时命中PCC规则（计费）和BWM规则（限速），两者独立匹配、叠加执行。

### 4.2 套餐1计费场景是套餐2带宽控制的直接参照

套餐1的完整配置模式（8步流程）可直接迁移到套餐2带宽控制场景。两者的过滤条件体系、规则匹配机制、User Profile绑定方式完全一致。核心差异仅在于：

- 套餐1的策略对象三件套：URR -> URRGroup -> PCCPolicyGroup
- 套餐2的策略对象：CategoryProp（分类属性） -> 带宽管理策略

这意味着在规划套餐2时，可以参照套餐1的业务分级逻辑（专项业务、协议级业务、兜底业务），将计费动作替换为带宽控制动作即可。

### 4.3 规则规划中的带宽控制关键参数

在规则规划中，UPF/SMF需要统一规划的参数包含 **BwmUserGroup**，专门用于带宽管理。这表明带宽控制在规则规划阶段就需要纳入CP/UP一致性规划，确保SMF与UPF上的带宽管理参数一致。

### 4.4 过滤条件对带宽控制的支撑

过滤条件体系支持按协议类型识别带宽敏感业务：

- **Streaming**（RTSP/MMS等）：需要大带宽保障视频体验
- **P2P**：需要限制带宽避免拥塞
- **File Access**（FTP/TFTP）：需要限制或保障文件传输带宽

这些协议组由SA特征库预置，无需手工逐个配置协议，大幅简化了带宽控制场景的过滤条件配置。

---

## 5. 关键术语

| 术语 | 说明 |
|------|------|
| **Rule（规则）** | 业务感知的核心载体，由条件和动作组成，决定满足哪些条件的报文执行哪些动作 |
| **Policytype（策略类型）** | 规则的策略方向，UDG支持PCC、BWM、HEADEN、WEBPROXY、SMARTREDIRECT、ADC、WORKER七种 |
| **BWM（带宽管理）** | 带宽管理策略类型，分类结果用于带宽管理策略匹配 |
| **PCC（计费与策略控制）** | 计费策略类型，用于实现计费和策略控制功能 |
| **Flow Filter（流过滤器）** | Filter、L7Filter、Protocol、Protocol Group的绑定组合，实现三四层+七层联合过滤 |
| **Flow Filter Group（流过滤器组）** | 多个Flow Filter的组合，支持与/或/非逻辑 |
| **Filter（三四层过滤器）** | 配置源/目的IP、端口、协议类型的三四层过滤条件 |
| **L7 Filter（七层过滤器）** | 配置URL、User-Agent、method等七层关键字段的过滤条件 |
| **Protocol Group（协议组）** | 由SA特征库预置的应用协议组合 |
| **Priority（优先级）** | 相同策略类型规则中的匹配顺序，取值越小优先级越高 |
| **SA（Service Awareness，业务感知）** | 对用户报文进行业务解析和识别的技术 |
| **UPF（用户面功能）** | 5G核心网用户面网元，执行报文解析、规则匹配和策略执行 |
| **PCF（策略控制功能）** | 5G核心网控制面网元，负责下发规则和策略 |
| **SMF（会话管理功能）** | 5G核心网控制面网元，负责"翻译"PCF规则并下发到UPF |
| **PFCP** | Packet Forwarding Control Protocol，SMF与UPF之间的接口协议 |
| **预定义规则** | 部署流程中规划的规则，默认未启用，由PCF控制启用 |
| **动态规则** | PCF在会话过程中灵活下发的规则，与预定义规则互补 |
| **本地规则** | UPF/SMF上配置的规则，无PCF或PCF不可用时启用 |
| **CategoryProp（分类属性）** | BWM策略类型绑定的策略对象，用于带宽管理的分类 |
| **特征库（SignatureDB）** | SA协议特征库，预置各类应用的协议签名和协议组合 |
| **前缀URL** | 代理服务器域名信息，SA解析时需剥离前缀URL使用真实URL匹配 |

---

## 6. 知识来源

| 序号 | 文件名 | 主题 |
|------|--------|------|
| 1 | 规则_92407887.md | 规则的概念、字段定义、策略类型体系 |
| 2 | 过滤条件_92407888.md | 过滤条件层级体系、各层过滤器、协议组 |
| 3 | 业务解析与识别流程_92407893.md | 三级识别体系（三四层/协议/七层）、前缀URL处理 |
| 4 | 策略执行流程_92407895.md | 匹配后策略执行（计费/QoS/带宽/重定向/头增强） |
| 5 | 规则匹配流程_92407894.md | 三层匹配模型（单一/同类型/不同类型）、优先级机制 |
| 6 | 规则获取_92407892.md | 规则类型（预定义/动态/本地）、5G规则下发流程 |
| 7 | 规则规划_92407891.md | 部署架构、自下而上配置、CP/UP统一规划 |
| 8 | 业务感知过程_92407889.md | 端到端业务感知流程总览（7步） |
| 9 | 加载特征库_92882614.md | SA特征库加载命令与验证 |
| 10 | 套餐1：计费场景_93112148.md | 4业务计费套餐完整MML配置脚本（8步） |
