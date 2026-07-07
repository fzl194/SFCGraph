# 命令证据包：ADD URR
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md`
> 用该命令的特性数：9

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于增加使用量上报规则信息，通过该命令可以针对不同应用类型的数据采取不同的上报规则。URR即Usage Reporting Rule用量上报规则，一般对应用户报文的时长、流量等上报控制规则。URR可以通过ADD URRGROUP命令配置到使用量上报规则组。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为65000。
- 该命令支持配置在线计费URR、离线计费URR、监控属性以及Qos保证的URR。
- 该命令中的MONITORINGKEY字段要求在所有URR内唯一。
- 当同时配置UPSID、DOWNSID且不配置离线RG时，离线计费话单中RG取值使用配置的DOWNSID值。
- 该命令中的参数USAGERPTMODE取值ONLINE时，参数ON

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| URRNAME | 使用量上报规则名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| URRID | URR标识 | local_planned | required | 无 | 整数类型，取值范围为0～2147483646。 |
| USAGERPTMODE | 使用量上报模式 | local_planned | required | 无 | 枚举类型。 |
| OFFCOMPOUNDTYPE | 离线计费标识组成类型 | local_planned | conditional | 无 | 枚举类型。 |
| ONLCOMPOUNDTYPE | 在线计费标识组成类型 | local_planned | conditional | 无 | 枚举类型。 |
| RG | 离线计费组 | local_planned | conditional | 无 | 整数类型，取值范围为0～4294967294。 |
| SID | 离线业务标识 | local_planned | conditional | 无 | 整数类型，取值范围为0～4294967294。 |
| UPSID | 离线上行业务标识 | local_planned | conditional | 无 | 整数类型，取值范围为0～4294967294。 |
| DOWNSID | 离线下行业务标识 | local_planned | conditional | 无 | 整数类型，取值范围为0～4294967294。 |
| ONLINERG | 在线计费组 | local_planned | conditional | 无 | 整数类型，取值范围为0～4294967294。 |
| ONLINESID | 在线业务标识 | local_planned | conditional | 无 | 整数类型，取值范围为0～4294967294。 |
| OFFMETERINGTYPE | 离线计费统计类型 | local_planned | conditional | 无 | 枚举类型。 |
| ONLMETERINGTYPE | 在线计费统计类型 | local_planned | conditional | 无 | 枚举类型。 |
| TIMERSUVALUE | 时间配额值（秒） | 对端协商 | conditional | 无 | 整数类型，取值范围为0～3600000。 |
| VOLUMERSUVALUE | 流量配额值（字节） | 对端协商 | conditional | 无 | 整数类型，取值范围为0～4294967295。 |
| OFCSRVTMPLNAME | 离线业务模板名 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| REDIRENDTOKEN | Gy重定向结束Token | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| MONITORINGKEY | 监控属性值 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～31。4294967295是无效值，初始化时MonitoringKey |
| EVENTRSUVALUE | 事件配额值（次） | 对端协商 | conditional | 0 | 整数类型，取值范围为0～5000。 |
| N40AGESW | N40接口场景下是否允许老化 | global_planned | conditional | ENABLE | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109103

**md：`WSFD-109103/WSFD-109103 IPv6 SA参考信息_78881328.md`**
- 操作步骤上下文（±2 行原文）：
  L13:
    > 
    > - [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > - [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    > - [**MOD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_09897174.md)/[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)

### WSFD-109107

**md：`WSFD-109107/WSFD-109107 业务触发的QoS保证参考信息_85397060.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    > - [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)
    > - [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)

**md：`WSFD-109107/激活业务触发的QoS保证_85397058.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | URRNAME（使用量上报规则名称） | URR_qos_01 | 本端规划 | 存在多条记录时，不能重复。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | URRID（URR标识） | 1005 | 本端规划 | URRID在所有URR内唯一，建议分配大于1000的值。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | USAGERPTMODE（使用量上报模式） | QOS | 固定取值 | - |
- 任务示例脚本（该命令行）：
  `ADD URR: URRNAME="URR_qos_01", URRID=1005, USAGERPTMODE=QOS;`
- 操作步骤上下文（±2 行原文）：
  L72:
    >   [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 2. 配置QoS URR。
    >   [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    > 3. 配置QoS属性。
    >   [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)
  L121:
    > 
    > ```
    > ADD URR: URRNAME="URR_qos_01", URRID=1005, USAGERPTMODE=QOS;
    > ```
    > 

### WSFD-211009

**md：`WSFD-211009/WSFD-211009 基于业务累计流量的策略控制参考信息_27915158.md`**
- 操作步骤上下文（±2 行原文）：
  L13:
    > 
    > - [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > - [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    > - [**MOD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_09897174.md)/[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)

**md：`WSFD-211009/激活基于业务累计流量的策略控制_27915156.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 使用量上报规则名称（URRNAME） | urr_01 | 本端规划 | 存在多条记录时，该参数不能重复。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | URR标识（URRID） | 2000 | 与对端协商 | 该参数需要与PGW-U/UPF上的URR标识保持一致。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 使用量上报模式（USAGERPTMODE） | MONITORINGKEY | 固定取值 | - |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 监控属性值（MONITORINGKEY） | 2001 | 与对端协商 | 该参数需要与PCRF/PCF的监控属性值保持一致。 |
- 任务示例脚本（该命令行）：
  `ADD URR:URRNAME="urr_01", URRID=2000, USAGERPTMODE=MONITORINGKEY, MONITORINGKEY="2001";`
- 操作步骤上下文（±2 行原文）：
  L53:
    >   [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > 4. 配置URR标识与监控属性值的绑定关系。
    >   [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    > 5. 在PCC策略组中配置用于累计流量的URR标识。
    >   [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
  L81:
    > 
    > ```
    > ADD URR:URRNAME="urr_01", URRID=2000, USAGERPTMODE=MONITORINGKEY, MONITORINGKEY="2001";
    > ```
    > 

### WSFD-011201

**md：`WSFD-011201/配置离线_在线计费方式（GGSN_PGW-C）_95923455.md`**
- 操作步骤上下文（±2 行原文）：
  L94:
    > 5. 配置免费业务的计费方式。
    >     a. 配置免费业务的计费模式。
    >       **ADD URR**
    >       > **说明**
    >       > 离线计费：参数 “USAGERPTMODE” 设置为 “OFFIINE” ， “OFFMETERINGTYPE” 设置为 “FREE” 。

**md：`WSFD-011201/配置离线计费的费率标识（GGSN_SGW-C_PGW-C）_98555879.md`**
- 数据规划表（该命令的参数行）：
  | **ADD URR** | 使用量上报规则名称（URRNAME） | offlineURR | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。<br>说明：参数<br>“USAGERPTMODE”<br>取值<br>“OFFLINE”<br>时，参数<br>“OFFCOMPOUNDTYPE”<br>、<br>“RG”<br>、<br>“SID”<br>组合配置要求唯一。 |
  | **ADD URR** | URR标识（URRID） | 1000 | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。<br>说明：参数<br>“USAGERPTMODE”<br>取值<br>“OFFLINE”<br>时，参数<br>“OFFCOMPOUNDTYPE”<br>、<br>“RG”<br>、<br>“SID”<br>组合配置要求唯一。 |
  | **ADD URR** | 使用量上报模式（USAGERPTMODE） | OFFLINE | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。<br>说明：参数<br>“USAGERPTMODE”<br>取值<br>“OFFLINE”<br>时，参数<br>“OFFCOMPOUNDTYPE”<br>、<br>“RG”<br>、<br>“SID”<br>组合配置要求唯一。 |
  | **ADD URR** | 离线计费标识组成类型（OFFCOMPOUNDTYPE） | RGSID | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。<br>说明：参数<br>“USAGERPTMODE”<br>取值<br>“OFFLINE”<br>时，参数<br>“OFFCOMPOUNDTYPE”<br>、<br>“RG”<br>、<br>“SID”<br>组合配置要求唯一。 |
  | **ADD URR** | 离线计费组（RG） | 10 | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。<br>说明：参数<br>“USAGERPTMODE”<br>取值<br>“OFFLINE”<br>时，参数<br>“OFFCOMPOUNDTYPE”<br>、<br>“RG”<br>、<br>“SID”<br>组合配置要求唯一。 |
  | **ADD URR** | 离线业务标识（SID） | 20 | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。<br>说明：参数<br>“USAGERPTMODE”<br>取值<br>“OFFLINE”<br>时，参数<br>“OFFCOMPOUNDTYPE”<br>、<br>“RG”<br>、<br>“SID”<br>组合配置要求唯一。 |
  | **ADD URR** | 离线计费统计类型（OFFMETERINGTYPE） | EVENT_VOLUME_TIME | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。<br>说明：参数<br>“USAGERPTMODE”<br>取值<br>“OFFLINE”<br>时，参数<br>“OFFCOMPOUNDTYPE”<br>、<br>“RG”<br>、<br>“SID”<br>组合配置要求唯一。 |
- 任务示例脚本（该命令行）：
  `ADD URR: URRNAME="offlineURR", URRID=1000, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=RGSID, RG=10, SID=20, OFFMETERINGTYPE=VOLUME;`
  `ADD URR: URRNAME="offlineURR", URRID=1000, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=RGSID, RG=10, SID=20, OFFMETERINGTYPE=VOLUME;`
  `ADD URR: URRNAME="offlineURR", URRID=1000, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=RGSID, RG=10, SID=20, OFFMETERINGTYPE=EVENT_VOLUME_TIME;`
- 操作步骤上下文（±2 行原文）：
  L62:
    > - 配置全局粒度的Session级计费费率标识。
    >     1. 配置全局URR，从而配置相应的计费费率标识，包括必须配置的RG和可选配置的SID。
    >       **ADD URR**
    >     2. 将全局URR绑定到全局URR组上，上下行可以使用不同的URR。
    >       **SET GLBURRGROUP**
  L68:
    >     1. 配置UserProfile下绑定的缺省URR组及相应URR，从而配置相应的计费费率标识。
    >           a. 配置URR，从而配置相应的计费费率标识，包括必须配置的RG和可选配置的SID。
    >             **ADD URR**
    >           b. 配置URR组，将上下行URR绑定到URR组上。上下行可以使用不同的URR。
    >             **ADD URRGROUP**
  L92:
    >     2. 配置内容计费使用的URR组及相应URR，从而配置相应的计费费率标识。
    >           a. 配置URR，从而配置相应的计费费率标识，包括必须配置的RG和可选配置的SID。
    >             **ADD URR**
    >           b. 配置URR组，将上下行URR绑定到URR组上。上下行可以使用不同的URR。
    >             **ADD URRGROUP**

### WSFD-011206

**md：`WSFD-011206/WSFD-011206 支持融合计费参考信息_74013176.md`**
- 操作步骤上下文（±2 行原文）：
  L22:
    > - [**ADD TNFBINDGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例绑定组管理/增加目标NF实例绑定组（ADD TNFBINDGRP）_09651533.md)
    > - [**ADD SELECTCHFGBYCC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/CHF选择/增加基于CC选择CHF处理（ADD SELECTCHFGBYCC）_09652118.md)
    > - **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)**
    > - [**SET GLBURRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/全局使用量上报规则组/设置全局使用量上报规则组（SET GLBURRGROUP）_09897187.md)
    > - [**ADD URRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)

**md：`WSFD-011206/使用全局CCT模板进行融合计费实例_93029782.md`**
- 数据规划表（该命令的参数行）：
  | **ADD URR** | URRNAME（使用量上报规则名称） | urr1 | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。 |
  | **ADD URR** | URRID（URR标识） | 1 | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。 |
  | **ADD URR** | USAGERPTMODE（使用量上报模式） | ONLINE | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。 |
  | **ADD URR** | ONLCOMPOUNDTYPE（在线计费标识组成类型） | RGSID | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。 |
  | **ADD URR** | ONLINERG（在线计费组） | 10 | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。 |
  | **ADD URR** | ONLINESID（在线业务标识） | 20 | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。 |
  | **ADD URR** | ONLMETERINGTYPE（在线计费统计类型） | VOLUME | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。 |
- 任务示例脚本（该命令行）：
  `ADD URR: URRNAME="urr1", URRID=1, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=RGSID, ONLINERG=10, ONLINESID=20, ONLMETERINGTYPE=VOLUME;`
- 操作步骤上下文（±2 行原文）：
  L70:
    > 
    > ```
    > ADD URR: URRNAME="urr1", URRID=1, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=RGSID, ONLINERG=10, ONLINESID=20, ONLMETERINGTYPE=VOLUME; 
    > SET GLBURRGROUP:UPONLURRNAME = "urr1", DNONLURRNAME = "urr1";
    > ```

**md：`WSFD-011206/配置SMF与CHF交互的条件和内容_93420840.md`**
- 数据规划表（该命令的参数行）：
  | **ADD URR** | 使用量上报规则名称（URRNAME） | urr_test | 本端规划 | - |
  | **ADD URR** | URR标识（URRID） | 1111 | 全网规划 | SMF和UPF上的URR标识需要一致。 |
  | **ADD URR** | 使用量上报模式（USAGERPTMODE） | ONLINE | 全网规划 | - |
  | **ADD URR** | 在线计费标识组成类型（ONLCOMPOUNDTYPE） | ONLYRG | 全网规划 | 根据业务套餐情况，确定使用RG还是（RG，SID）作为费率标识。<br>此处以使用RG作为费率标识为例。 |
  | **ADD URR** | 在线计费组（ONLINERG） | 111 | 本端规划 | - |
  | **ADD URR** | 在线计费统计类型（ONLMETERINGTYPE） | VOLUME | 全网规划 | 根据业务套餐情况，确定使用免费、按时长计费、按流量计费，还是按照流量+时长计费。<br>此处以按流量计费为例。 |
- 任务示例脚本（该命令行）：
  `ADD URR: URRNAME="urr_test", URRID=1111, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=111, ONLMETERINGTYPE=VOLUME;`
- 操作步骤上下文（±2 行原文）：
  L75:
    > 2. **可选：** 配置SMF在建立计费会话的ChargingDataRequest中携带的为哪些RG申请预配额。
    >     a. 配置URR组合URR，指定需预申请配额的RG。
    >       **ADD URR**
    >       **ADD URRGROUP**
    >     b. 配置UserProfile。
  L114:
    > 
    > ```
    > ADD URR: URRNAME="urr_test", URRID=1111, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=111, ONLMETERINGTYPE=VOLUME;
    > ADD URRGROUP: URRGROUPNAME="urrgroup_test", UPURRNAME1="urr_test", DOWNURRNAME1="urr_test";
    > ADD USERPROFILE: USERPROFILENAME="up_test", UPTYPE=PCC;

**md：`WSFD-011206/配置融合计费费率标识_93360308.md`**
- 数据规划表（该命令的参数行）：
  | **ADD URR** | 使用量上报规则名称（URRNAME） | urr_online_URL<br>urr_online_IMS<br>urr_online_any<br>URR_abnormal_online | 本端规划 | 配置业务在线计费URR。<br>URRID、USAGERPTMODE、ONLMETERINGTYPE在SMF和UPF上的配置需要保持一致。 |
  | **ADD URR** | URR标识（URRID） | 2300<br>3300<br>1300<br>4300 | 全网规划 | 配置业务在线计费URR。<br>URRID、USAGERPTMODE、ONLMETERINGTYPE在SMF和UPF上的配置需要保持一致。 |
  | **ADD URR** | 使用量上报模式（USAGERPTMODE） | ONLINE | 全网规划 | 配置业务在线计费URR。<br>URRID、USAGERPTMODE、ONLMETERINGTYPE在SMF和UPF上的配置需要保持一致。 |
  | **ADD URR** | 在线计费标识组成类型（ONLCOMPOUNDTYPE） | ONLYRG | 全网规划 | 根据业务套餐情况，确定使用RG还是（RG，SID）作为费率标识。<br>此处以使用RG作为费率标识为例。 |
  | **ADD URR** | 在线计费组（ONLINERG） | 100<br>200<br>300<br>400 | 本端规划 | - |
  | **ADD URR** | 在线计费统计类型（ONLMETERINGTYPE） | VOLUME<br>VOLUME<br>VOLUME<br>FREE | 全网规划 | 根据业务套餐情况，确定使用免费、按时长计费、按流量计费，还是按照流量+时长计费。<br>此处以按流量计费为例。 |
  | **ADD URR** | 使用量上报规则名称（URRNAME） | urr_offline_URL<br>urr_offline_IMS<br>urr_offline_any<br>URR_abnormal_offline | 本端规划 | 配置业务离线计费URR。<br>URRID、USAGERPTMODE、OFFMETERINGTYPE在SMF和UPF上的配置需要保持一致。 |
  | **ADD URR** | URR标识（URRID） | 12500<br>13500<br>11500<br>14500 | 全网规划 | 配置业务离线计费URR。<br>URRID、USAGERPTMODE、OFFMETERINGTYPE在SMF和UPF上的配置需要保持一致。 |
  | **ADD URR** | 使用量上报模式（USAGERPTMODE） | OFFLINE | 全网规划 | 配置业务离线计费URR。<br>URRID、USAGERPTMODE、OFFMETERINGTYPE在SMF和UPF上的配置需要保持一致。 |
  | **ADD URR** | 离线计费标识组成类型（OFFCOMPOUNDTYPE） | ONLYRG | 全网规划 | 根据业务套餐情况，确定使用RG还是（RG，SID）作为费率标识。<br>此处以使用RG作为费率标识为例。 |
  | **ADD URR** | 离线计费组（RG） | 1100<br>1200<br>1300<br>1400 | 本端规划 | - |
  | **ADD URR** | 离线计费统计类型（OFFMETERINGTYPE） | VOLUME<br>VOLUME<br>VOLUME<br>FREE | 全网规划 | 根据业务套餐情况，确定使用免费、按时长计费、按流量计费，还是按照流量+时长计费。<br>此处以按流量计费为例。 |
- 任务示例脚本（该命令行）：
  `ADD URR: URRNAME="urr_online_URL", URRID=2300, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=100, ONLMETERINGTYPE=VOLUME;`
  `ADD URR: URRNAME="urr_offline_URL", URRID=12500, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=ONLYRG, RG=1100, OFFMETERINGTYPE=VOLUME;`
  `ADD URR: URRNAME="urr_online_IMS", URRID=3300, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=200, ONLMETERINGTYPE=VOLUME;`
  `ADD URR: URRNAME="urr_offline_IMS", URRID=13500, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=ONLYRG, RG=1200, OFFMETERINGTYPE=VOLUME;`
  `ADD URR: URRNAME="urr_online_any", URRID=1300, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=300, ONLMETERINGTYPE=VOLUME;`
  `ADD URR: URRNAME="urr_offline_any", URRID=11500, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=ONLYRG, RG=1300, OFFMETERINGTYPE=VOLUME;`
  `ADD URR: URRNAME="URR_abnormal_online", URRID=4300, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=400, ONLMETERINGTYPE=FREE;`
  `ADD URR: URRNAME="URR_abnormal_offline", URRID=14500, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=ONLYRG, RG=1400, OFFMETERINGTYPE=FREE;`
- 操作步骤上下文（±2 行原文）：
  L89:
    >     1. 配置内容计费使用的URR组及相应URR。
    >           a. 配置URR。
    >             **ADD URR**
    >           b. 配置URR组，将URR绑定到URR组上。
    >             **ADD URRGROUP**
  L145:
    > 
    > ```
    > ADD URR: URRNAME="urr_online_URL", URRID=2300, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=100, ONLMETERINGTYPE=VOLUME;
    > ADD URR: URRNAME="urr_offline_URL", URRID=12500, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=ONLYRG, RG=1100, OFFMETERINGTYPE=VOLUME;
    > ADD URR: URRNAME="urr_online_IMS", URRID=3300, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=200, ONLMETERINGTYPE=VOLUME;
  L146:
    > ```
    > ADD URR: URRNAME="urr_online_URL", URRID=2300, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=100, ONLMETERINGTYPE=VOLUME;
    > ADD URR: URRNAME="urr_offline_URL", URRID=12500, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=ONLYRG, RG=1100, OFFMETERINGTYPE=VOLUME;
    > ADD URR: URRNAME="urr_online_IMS", URRID=3300, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=200, ONLMETERINGTYPE=VOLUME;
    > ADD URR: URRNAME="urr_offline_IMS", URRID=13500, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=ONLYRG, RG=1200, OFFMETERINGTYPE=VOLUME;

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L15:
    > - [**SET CHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/设置计费控制配置（SET CHARGECTRL）_09896792.md)
    > - [**SET APNCHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md)
    > - **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)**
    > - [**ADD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
    > - [**SET OCSINIT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/设置DCC模板OCS初始化（SET OCSINIT）_09896932.md)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L15:
    > - [**SET CHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/设置计费控制配置（SET CHARGECTRL）_09896792.md)
    > - [**SET APNCHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md)
    > - **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)**
    > - [**ADD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
    > - [**SET OCSINIT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/设置DCC模板OCS初始化（SET OCSINIT）_09896932.md)

**md：`WSFD-109001/配置在线计费的费率标识_95923388.md`**
- 数据规划表（该命令的参数行）：
  | **ADD URR** | 使用量上报规则名称（URRNAME） | onlineURR | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。<br>说明：参数<br>“USAGERPTMODE”<br>取值<br>“ONLINE”<br>时，参数<br>“ONLCOMPOUNDTYPE”<br>、<br>“ONLINERG”<br>、<br>“ONLINESID”<br>组合配置要求唯一。 |
  | **ADD URR** | URR标识（URRID） | 1100 | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。<br>说明：参数<br>“USAGERPTMODE”<br>取值<br>“ONLINE”<br>时，参数<br>“ONLCOMPOUNDTYPE”<br>、<br>“ONLINERG”<br>、<br>“ONLINESID”<br>组合配置要求唯一。 |
  | **ADD URR** | 使用量上报模式（USAGERPTMODE） | ONLINE | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。<br>说明：参数<br>“USAGERPTMODE”<br>取值<br>“ONLINE”<br>时，参数<br>“ONLCOMPOUNDTYPE”<br>、<br>“ONLINERG”<br>、<br>“ONLINESID”<br>组合配置要求唯一。 |
  | **ADD URR** | 在线计费标识组成类型（ONLCOMPOUNDTYPE） | RGSID | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。<br>说明：参数<br>“USAGERPTMODE”<br>取值<br>“ONLINE”<br>时，参数<br>“ONLCOMPOUNDTYPE”<br>、<br>“ONLINERG”<br>、<br>“ONLINESID”<br>组合配置要求唯一。 |
  | **ADD URR** | 在线计费组（ONLINERG） | 10 | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。<br>说明：参数<br>“USAGERPTMODE”<br>取值<br>“ONLINE”<br>时，参数<br>“ONLCOMPOUNDTYPE”<br>、<br>“ONLINERG”<br>、<br>“ONLINESID”<br>组合配置要求唯一。 |
  | **ADD URR** | 在线业务标识（ONLINESID） | 20 | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。<br>说明：参数<br>“USAGERPTMODE”<br>取值<br>“ONLINE”<br>时，参数<br>“ONLCOMPOUNDTYPE”<br>、<br>“ONLINERG”<br>、<br>“ONLINESID”<br>组合配置要求唯一。 |
  | **ADD URR** | 在线计费统计类型（ONLMETERINGTYPE） | EVENT_VOLUME_TIME | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。<br>说明：参数<br>“USAGERPTMODE”<br>取值<br>“ONLINE”<br>时，参数<br>“ONLCOMPOUNDTYPE”<br>、<br>“ONLINERG”<br>、<br>“ONLINESID”<br>组合配置要求唯一。 |
- 任务示例脚本（该命令行）：
  `ADD URR: URRNAME="onlineURR", URRID=1100, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=RGSID, ONLINERG=10, ONLINESID=20, ONLMETERINGTYPE=EVENT_VOLUME_TIME;`
  `ADD URR: URRNAME="onlineURR", URRID=1100, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=RGSID, ONLINERG=10, ONLINESID=20, ONLMETERINGTYPE=EVENT_VOLUME_TIME;`
  `ADD URR: URRNAME="onlineURR", URRID=1100, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=RGSID, ONLINERG=10, ONLINESID=20, ONLMETERINGTYPE=EVENT_VOLUME_TIME;`
- 操作步骤上下文（±2 行原文）：
  L63:
    > - 配置全局粒度的Session级计费费率标识。
    >     1. 配置全局URR，从而配置相应的计费费率标识，包括必须配置的RG和可选配置的SID。
    >       **ADD URR**
    >       > **说明**
    >       > - 各费率组RG的配额一般由OCS下发，当OCS不支持配置配额下发的具体数值时，也可以在GGSN/PGW-C本地配置要申请的配额数。本地通过**ADD URR**命令参数“ONLMETERINGTYPE”的值“VOLUME”（按流量计费），或“TIME”（按时间计费）配置相应的配额数即可。
  L65:
    >       **ADD URR**
    >       > **说明**
    >       > - 各费率组RG的配额一般由OCS下发，当OCS不支持配置配额下发的具体数值时，也可以在GGSN/PGW-C本地配置要申请的配额数。本地通过**ADD URR**命令参数“ONLMETERINGTYPE”的值“VOLUME”（按流量计费），或“TIME”（按时间计费）配置相应的配额数即可。
    >       > - 当OCS和GGSN/PGW-C都配置有费率下发/申请的配额数时，OCS上的配置优先级高。
    >     2. 将全局URR绑定到全局URR组上，上下行可以使用不同的URR。
  L72:
    >     1. 配置UserProfile下绑定的缺省URR组及相应URR，从而配置相应的计费费率标识。
    >           a. 配置URR，从而配置相应的计费费率标识，包括必须配置的RG和可选配置的SID。
    >             **ADD URR**
    >           b. 配置URR组，将上下行URR绑定到URR组上。上下行可以使用不同的URR。
    >             **ADD URRGROUP**

**md：`WSFD-109001/配置普通在线计费实例_95923459.md`**
- 数据规划表（该命令的参数行）：
  | **ADD URR** | 使用量上报规则名称（URRNAME） | onlineURR | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。 |
  | **ADD URR** | URR标识（URRID） | 1100 | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。 |
  | **ADD URR** | 使用量上报模式（USAGERPTMODE） | ONLINE | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。 |
  | **ADD URR** | 在线计费标识组成类型（ONLCOMPOUNDTYPE） | RGSID | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。 |
  | **ADD URR** | 在线计费组（ONLINERG） | 10 | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。 |
  | **ADD URR** | 在线业务标识（ONLINESID） | 20 | 本端规划 | 配置使用量上报规则，从而配置使用的费率标识。 |
- 任务示例脚本（该命令行）：
  `ADD URR: URRNAME="onlineURR", URRID=1100, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=RGSID, ONLINERG=10, ONLINESID=20;`
- 操作步骤上下文（±2 行原文）：
  L89:
    > 3. 配置在线计费的费率标识。
    >     a. 配置URR，从而配置相应的计费费率标识，包括必须配置的RG和可选配置的SID。
    >       **ADD URR**
    >     b. 配置URR组，将上下行URR绑定到URR组上。上下行可以使用不同的URR。
    >       **ADD URRGROUP**
  L150:
    > 3. 配置在线计费的费率标识。
    >   ```
    >   ADD URR: URRNAME="onlineURR", URRID=1100, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=RGSID, ONLINERG=10, ONLINESID=20;
    >   ```
    >   ```

**md：`WSFD-109001/配置离线_在线计费方式（GGSN_PGW-C）_15408914.md`**
- 操作步骤上下文（±2 行原文）：
  L94:
    > 5. 配置免费业务的计费方式。
    >     a. 配置免费业务的计费模式。
    >       **ADD URR**
    >       > **说明**
    >       > 离线计费：参数 “USAGERPTMODE” 设置为 “OFFIINE” ， “OFFMETERINGTYPE” 设置为 “FREE” 。

**md：`WSFD-109001/配置CCR消息中携带的参数_95923469.md`**
- 操作步骤上下文（±2 行原文）：
  L62:
    >   > 各费率组RG的配额一般由OCS下发，当OCS不支持配置配额下发的具体数值时，也可以在GGSN/PGW-C本地配置要申请的配额数。当OCS和GGSN/PGW-C都配置有费率下发/申请的配额数时，OCS上的配置优先级高。
    >     1. 配置时长/流量计费时CCR消息中默认请求的时长/流量配额数。
    >       **ADD URR**
    >       > **说明**
    >       > 参数 “ONLMETERINGTYPE” 的值 “VOLUME” （按流量计费），或 “TIME” （按时间计费）配置相应的配额数即可。

**md：`WSFD-109001/配置CCR触发场景_95923545.md`**
- 任务示例脚本（该命令行）：
  `ADD URR: URRNAME="onlineURR", URRID=1100, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=100, ONLMETERINGTYPE=TIME;`
- 操作步骤上下文（±2 行原文）：
  L92:
    >     2. 配置用户激活时CCR-I消息要携带的费率标识（RG），具体步骤请参见 [配置在线计费的费率标识](../配置在线计费的费率标识_95923388.md) 。
    >           a. 配置URR。
    >             **ADD URR**
    >           b. 配置上行和下行发起的业务对应的URR。
    >             **ADD URRGROUP**
  L122:
    > 
    > ```
    > ADD URR: URRNAME="onlineURR", URRID=1100, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=100, ONLMETERINGTYPE=TIME;
    > ```
    > 

### WSFD-109007

**md：`WSFD-109007/WSFD-109007 支持事件计费参考信息_74112323.md`**
- 操作步骤上下文（±2 行原文）：
  L13:
    > 
    > - [**SET CHFINIT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/设置融合计费模板中用户激活相关参数（SET CHFINIT）_09653178.md)
    > - **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)**
    > - [**ADD URRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)

**md：`WSFD-109007/实现原理（适用于Ga接口的离线计费用户）_74112320.md`**
- 操作步骤上下文（±2 行原文）：
  L3:
    > # 实现原理（适用于Ga接口的离线计费用户）
    > 
    > 离线计费通过话单将用户计费信息上报给计费系统BS，当GGSN-C/PGW-C上通过配置 **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)** 设置业务计费是事件类型后，即在话单中增加事件计费信息。
    > 
    > 事件计费采用的话单类型必须是R7以上的eG-CDR或PGW-CDR。事件次数和对应的时间戳信息在话单业务容器（List of Service Data）的“Event Based Charging Information”字段中记录。如下所示话单的业务容器中“eventBasedChargingInformation”字段记录业务RatingGroup 1007发生了5次事件及其时间戳信息。

**md：`WSFD-109007/实现原理（适用于Gy接口的在线计费用户）_74112319.md`**
- 操作步骤上下文（±2 行原文）：
  L53:
    > 1~2. 标准ECUR不支持预申请配额，PDP/承载激活时不为事件计费业务预申请配额，不创建ECUR会话。当PGW-U检测到事件计费发生时，PGW-U上报事件计费新业务，请求申请配额。
    > 
    > 3. PGW-C向OCS发送CCR-I消息，建立ECUR事件计费会话并申请配额，其中 **RSU** （Requested-Service-Unit）中携带的事件配额为 **ADD URR** 命令配置的EVENTRSUVALUE预申请事件配额值加上PGW-U本次请求的事件数总和。
    > 
    > 4. OCS向PGW-C下发事件配额。标准ECUR不支持 **UQT** ，当OCS下发UQT时，PGW-C忽略。标准ECUR模式下事件计费业务支持同时上报时长/流量用量的上报，但不支持时长/流量配额的信用控制，如果OCS下发的配额中包括时长/流量配额，PGW-C忽略。
  L109:
    > 
    > - 彩信的每个被叫号码添加到一个MSCC中，每个MSCC中RSU{CC-Service-Specific-Units = 1}。
    > - 忽略**ADD URR**命令配置的EVENTRSUVALUE预申请事件配额值，只按PGW-U请求的事件次数申请配额，不多申请。
    > - Service-Information下新增MMS-Information信元组，携带彩信信息。
    > - Service-Context-Id固定填充mms_ggsn@huawei.com

**md：`WSFD-109007/实现原理（适用于Nchf_N40接口的融合计费用户）_74112318.md`**
- 操作步骤上下文（±2 行原文）：
  L44:
    > 1：用户发起PDU会话建立请求。
    > 
    > 2：GGSN-C/PGW-C/SMF向CHF发送Charging Data Request[Initial]消息，请求建立计费会话。该消息可携带预申请的事件计费配额（通过 [**SET CTXSTARTRATING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/设置给OCS_CHF发送的消息初始携带的计费属性（SET CTXSTARTRATING）_09897210.md) 命令配置），预申请的事件计费配额数 **由 [ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)** 命令中的 “EVENTRSUVALUE” 参数决定，并通过serviceSpecificUnits字段携带给CHF。
    > 
    > 3：CHF向GGSN-C/PGW-C/SMF返回Charging Data Response[Initial]消息。如果GGSN-C/PGW-C/SMF预申请了事件计费配额，事件计费配额和阈值会通过serviceSpecificUnits字段和unitQuotaThreshold字段携带给GGSN-C/PGW-C/SMF。
  L78:
    > - GGSN-C/PGW-C/SMF本地配置不支持事件计费功能时，GGSN-U/PGW-U/UPF本地配置支持事件计费功能。GGSN-C/PGW-C/SMF上报[ALM-81026 接口信元不一致](../../../../../网络运维/故障处理/UNC告警处理/业务告警/SMF&GW-C&GGSN/ALM-81026 接口信元不一致_34629541.md)告警。
    > 
    > 8：GGSN-C/PGW-C/SMF收到GGSN-U/PGW-U/UPF发送的事件计费配额申请，根据本地配置的事件计费配额（通过 **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)** 中的 “EVENTRSUVALUE” 参数值决定）和GGSN-U/PGW-U/UPF申请的事件计费配额之和作为事件计费配额，通过serviceSpecificUnits字段发给CHF。
    > 
    > 9：GGSN-C/PGW-C/SMF发送PFCP Session Report Response给GGSN-U/PGW-U/UPF。

**md：`WSFD-109007/配置事件计费功能_74112321.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)** | URRNAME（使用量上报规则名称） | urr1 | 本端规划 | 配置SMF在建立PDU会话时，在ChargingDataRqueset中携带的预申请配额RG的参数。 |
  | **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)** | URRID（URR标识） | 1000 | 本端规划 | 配置SMF在建立PDU会话时，在ChargingDataRqueset中携带的预申请配额RG的参数。 |
  | **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)** | USAGERPTMODE（使用量上报模式） | ONLINE | 本端规划 | 配置SMF在建立PDU会话时，在ChargingDataRqueset中携带的预申请配额RG的参数。 |
  | **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)** | ONLCOMPOUNDTYPE（在线计费标识组成类型） | ONLYRG | 本端规划 | 配置SMF在建立PDU会话时，在ChargingDataRqueset中携带的预申请配额RG的参数。 |
  | **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)** | ONLINERG（在线计费组） | 100 | 本端规划 | 配置SMF在建立PDU会话时，在ChargingDataRqueset中携带的预申请配额RG的参数。 |
  | **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)** | ONLMETERINGTYPE（在线计费统计类型） | EVENT | 本端规划 | 配置SMF在建立PDU会话时，在ChargingDataRqueset中携带的预申请配额RG的参数。 |
  | **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)** | URRNAME（使用量上报规则名称） | urr2 | 本端规划 | 配置离线计费用户的事件计费属性。 |
  | **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)** | URRID（URR标识） | 1002 | 本端规划 | 配置离线计费用户的事件计费属性。 |
  | **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)** | USAGERPTMODE（使用量上报模式） | OFFLINE | 本端规划 | 配置离线计费用户的事件计费属性。 |
  | **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)** | OFFCOMPOUNDTYPE<br>（离线计费标识组成类型） | ONLYRG | 本端规划 | 配置离线计费用户的事件计费属性。 |
  | **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)** | RG<br>（离线计费组） | 102 | 本端规划 | 配置离线计费用户的事件计费属性。 |
  | **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)** | OFFMETERINGTYPE<br>（离线计费统计类型） | EVENT | 本端规划 | 配置离线计费用户的事件计费属性。 |
- 任务示例脚本（该命令行）：
  `ADD URR: URRNAME="urr1", URRID=1000, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=100, ONLMETERINGTYPE=EVENT;`
  `ADD URR: URRNAME="urr2", URRID=1002, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=ONLYRG, RG=102, OFFMETERINGTYPE=EVENT;`
- 操作步骤上下文（±2 行原文）：
  L76:
    > 4. **可选：**配置事件计费使用的计费属性。
    >     a. 配置事件计费的RG使用的URR组及相应URR。
    >       **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)**
    >       [**ADD URRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)
    >     b. 配置UserProfile。
  L129:
    > 
    > ```
    > ADD URR: URRNAME="urr1", URRID=1000, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=100, ONLMETERINGTYPE=EVENT;
    > ADD URRGROUP: URRGROUPNAME="urrgroup1", UPURRNAME1="urr1", DOWNURRNAME1="urr1";
    > ADD USERPROFILE:USERPROFILENAME="up-test", UPTYPE=PCC;
  L168:
    > 
    > ```
    > ADD URR: URRNAME="urr2", URRID=1002, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=ONLYRG, RG=102, OFFMETERINGTYPE=EVENT;
    > ```

### WSFD-201207

**md：`WSFD-201207/WSFD-201207 语音PCF_PCRF故障Bypass参考信息_85304300.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    > 
    > **[RMV URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/删除URR（RMV URR）_09897160.md)**

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（Gx接口）_60552093.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 使用量上报规则名称（URRNAME） | urr_signaling_offline<br>urr_signaling_online | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | URR标识（URRID） | 2005<br>2015 | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 使用量上报模式（USAGERPTMODE） | OFFLINE<br>ONLINE | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 离线计费标识组成类型（OFFCOMPOUNDTYPE） | ONLYRG | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 离线计费组（RG） | 20 | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 离线计费统计类型（OFFMETERINGTYPE） | VOLUME | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 在线计费标识组成类型（ONLCOMPOUNDTYPE） | ONLYRG | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 在线计费组（ONLINERG） | 25 | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 在线计费统计类型（ONLMETERINGTYPE） | VOLUME | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 使用量上报规则名称（URRNAME） | urr_voice_offline<br>urr_voice_online<br>urr_qos_01 | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | URR标识（URRID） | 1005<br>1015<br>1006 | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 使用量上报模式（USAGERPTMODE） | OFFLINE<br>ONLINE<br>QOS | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 离线计费标识组成类型（OFFCOMPOUNDTYPE） | ONLYRG | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 离线计费组（RG） | 10 | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 离线计费统计类型（OFFMETERINGTYPE） | VOLUME | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 在线计费标识组成类型（ONLCOMPOUNDTYPE） | ONLYRG | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 在线计费组（ONLINERG） | 15 | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 在线计费统计类型（ONLMETERINGTYPE） | VOLUME | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
- 任务示例脚本（该命令行）：
  `ADD URR:URRNAME="urr_signaling_offline", URRID=2005, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=ONLYRG, RG=20, OFFMETERINGTYPE=VOLUME;`
  `ADD URR:URRNAME="urr_signaling_online", URRID=2015, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=25, ONLMETERINGTYPE=VOLUME;`
  `ADD URR:URRNAME="urr_qos_01", URRID=1006, USAGERPTMODE=QOS;`
  `ADD URR:URRNAME="urr_voice_offline", URRID=1005, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=ONLYRG, RG=10, OFFMETERINGTYPE=VOLUME;`
  `ADD URR:URRNAME="urr_voice_online", URRID=1015, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=15, ONLMETERINGTYPE=VOLUME;`
  `ADD URR:URRNAME="urr_qos_01", URRID=1006, USAGERPTMODE=QOS;`
  `ADD URR:URRNAME="urr_voice_offline", URRID=1005, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=ONLYRG, RG=10, OFFMETERINGTYPE=VOLUME;`
  `ADD URR:URRNAME="urr_voice_online", URRID=1015, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=15, ONLMETERINGTYPE=VOLUME;`
- 操作步骤上下文（±2 行原文）：
  L194:
    > 
    >   a. 增加使用量上报规则信息。
    >       [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    >     b. 增加使用量上报规则组。
    >       **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)**
  L223:
    > 
    >   a. 增加使用量上报规则信息。
    >       [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    >     b. 增加使用量上报规则组。
    >       **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)**
  L305:
    > 
    >       ```
    >       ADD URR:URRNAME="urr_signaling_offline", URRID=2005, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=ONLYRG, RG=20, OFFMETERINGTYPE=VOLUME;
    >       ADD URR:URRNAME="urr_signaling_online", URRID=2015, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=25, ONLMETERINGTYPE=VOLUME;
    >       ```

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（N7接口）_32852169.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 使用量上报规则名称（URRNAME） | urr_signaling_offline<br>urr_signaling_online | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | URR标识（URRID） | 2005<br>2015 | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 使用量上报模式（USAGERPTMODE） | OFFLINE<br>ONLINE | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 离线计费标识组成类型（OFFCOMPOUNDTYPE） | ONLYRG | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 离线计费组（RG） | 20 | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 离线计费统计类型（OFFMETERINGTYPE） | VOLUME | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 在线计费标识组成类型（ONLCOMPOUNDTYPE） | ONLYRG | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 在线计费组（ONLINERG） | 25 | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 在线计费统计类型（ONLMETERINGTYPE） | VOLUME | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 使用量上报规则名称（URRNAME） | urr_voice_offline<br>urr_voice_online<br>urr_qos_01 | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | URR标识（URRID） | 1005<br>1015<br>1006 | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 使用量上报模式（USAGERPTMODE） | OFFLINE<br>ONLINE<br>QOS | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 离线计费标识组成类型（OFFCOMPOUNDTYPE） | ONLYRG | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 离线计费组（RG） | 10 | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 离线计费统计类型（OFFMETERINGTYPE） | VOLUME | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 在线计费标识组成类型（ONLCOMPOUNDTYPE） | ONLYRG | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 在线计费组（ONLINERG） | 15 | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
  | [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 在线计费统计类型（ONLMETERINGTYPE） | VOLUME | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
- 任务示例脚本（该命令行）：
  `ADD URR:URRNAME="urr_signaling_offline", URRID=2005, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=ONLYRG, RG=20, OFFMETERINGTYPE=VOLUME;`
  `ADD URR:URRNAME="urr_signaling_online", URRID=2015, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=25, ONLMETERINGTYPE=VOLUME;`
  `ADD URR:URRNAME="urr_qos_01", URRID=1006, USAGERPTMODE=QOS;`
  `ADD URR:URRNAME="urr_voice_offline", URRID=1005, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=ONLYRG, RG=10, OFFMETERINGTYPE=VOLUME;`
  `ADD URR:URRNAME="urr_voice_online", URRID=1015, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=15, ONLMETERINGTYPE=VOLUME;`
  `ADD URR:URRNAME="urr_qos_01", URRID=1006, USAGERPTMODE=QOS;`
  `ADD URR:URRNAME="urr_voice_offline", URRID=1005, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=ONLYRG, RG=10, OFFMETERINGTYPE=VOLUME;`
  `ADD URR:URRNAME="urr_voice_online", URRID=1015, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=15, ONLMETERINGTYPE=VOLUME;`
- 操作步骤上下文（±2 行原文）：
  L213:
    > 
    >   a. 增加使用量上报规则信息。
    >       [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    >     b. 增加使用量上报规则组。
    >       **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)**
  L242:
    > 
    >   a. 增加使用量上报规则信息。
    >       [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    >     b. 增加使用量上报规则组。
    >       **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)**
  L333:
    > 
    >       ```
    >       ADD URR:URRNAME="urr_signaling_offline", URRID=2005, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=ONLYRG, RG=20, OFFMETERINGTYPE=VOLUME;
    >       ADD URR:URRNAME="urr_signaling_online", URRID=2015, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=25, ONLMETERINGTYPE=VOLUME;
    >       ```

## ④ 自动比对
- 命令真相参数（20）：['DOWNSID', 'EVENTRSUVALUE', 'MONITORINGKEY', 'N40AGESW', 'OFCSRVTMPLNAME', 'OFFCOMPOUNDTYPE', 'OFFMETERINGTYPE', 'ONLCOMPOUNDTYPE', 'ONLINERG', 'ONLINESID', 'ONLMETERINGTYPE', 'REDIRENDTOKEN', 'RG', 'SID', 'TIMERSUVALUE', 'UPSID', 'URRID', 'URRNAME', 'USAGERPTMODE', 'VOLUMERSUVALUE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 84, '固定取值': 2, '与对端协商': 2, '全网规划': 12}（多值→atom 应考虑 decision_driven）
