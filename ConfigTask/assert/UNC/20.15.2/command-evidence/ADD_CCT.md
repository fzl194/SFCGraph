# 命令证据包：ADD CCT
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/增加融合计费模板（ADD CCT）_09653176.md`
> 用该命令的特性数：4

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于新增融合计费模板（Converged Charging Template），用于配置融合计费相关参数。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 最多可输入101条记录。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CCTMPLTNAME | QHT | VQT | TQT | UQT | VT | MAXNUMOFCCC | PDUVOLUMELIMIT | PDUTIMELIMIT | RGVOLUMELIMIT | RGTIMELIMIT | QFVOLUMELIMIT |

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CCTMPLTNAME | 融合计费模板名称 | local_planned | required | 无 | 字符串类型，输入长度范围是1~63。不区分大小写。 |
| QHT | 配额空闲时间门限值(秒) | local_planned | optional | 0 | 整数类型，取值范围是0，5~3600。 |
| VQT | 流量阈值触发百分比(%) | local_planned | optional | 20 | 整数类型，取值范围是0~50。 |
| TQT | 时间阈值触发百分比(%) | local_planned | optional | 20 | 整数类型，取值范围是0~50。 |
| UQT | 事件阈值触发百分比(%) | local_planned | optional | 20 | 整数类型，取值范围是0~50。 |
| VT | 在线配额有效时长(分) | local_planned | optional | 30 | 整数类型，取值范围是0，5~1440。 |
| MAXNUMOFCCC | 计费条件改变阈值 | local_planned | optional | 3 | 整数类型，取值范围是1~10。 |
| PDUVOLUMELIMIT | PDU流量阈值(MB) | local_planned | optional | 500 | 整数类型，取值范围是0~2147483647，单位是兆字节。备注：1兆字节为1048576字节。 |
| PDUTIMELIMIT | PDU时长阈值(分钟) | local_planned | optional | 30 | 整数类型，取值范围是0~1440。 |
| RGVOLUMELIMIT | 业务级流量阈值(MB) | local_planned | optional | 500 | 整数类型，取值范围是0~2147483647，单位是兆字节。备注：1兆字节为1048576字节。 |
| RGTIMELIMIT | 业务级时长阈值(分钟) | local_planned | optional | 30 | 整数类型，取值范围是0~1440。 |
| QFVOLUMELIMIT | QF流量阈值(MB) | local_planned | optional | 500 | 整数类型，取值范围是0~2147483647，单位是兆字节。备注：1兆字节为1048576字节。 |
| QFTIMELIMIT | QF时长阈值(分钟) | local_planned | optional | 30 | 整数类型，取值范围是0~1440。 |
| UCITIMER | 业务停止时长(分钟) | 对端协商 | optional | 60 | 整数类型，取值范围是0~1440。 |
| FUATERMINATE | 最终配额动作指示终结方式 | local_planned | optional | TERM_SERVICE | <br>- “TERM_SERVICE（阻塞业务）”：阻塞业务 |
| TIMEFORMAT | 时间格式 | local_planned | optional | LocalTime | <br>- “LocalTime（本地时间）”：指定发给CHF的消息中的时间格式为localtime |
| MAXSVCCONTAINER | 最大携带的业务容器数量 | local_planned | optional | 100 | 整数类型，取值范围是0~100。 |
| SECRUTHRESHOLD | RAN-SecondaryRAT-Usage-Report上报CHF的阈值 | global_planned | optional | 100 | 整数类型，取值范围是0~100。 |
| MAXUSEDSRVNUM | 最大可使用的业务个数 | local_planned | optional | 60 | 整数类型，取值范围是0~100。 |
| QHTRPTTRIGGER | QHT超时触发的容器中Trigger的值 | local_planned | optional | QHT | <br>- “QHT（上报QHT）”：Nchf消息容器中Trigger的值填写QHT。 |
| ROAMFUATERMACT | 漫游用户最终配额动作指示终结方式 | local_planned | conditional | TERM_SERVICE | <br>- “TERM_SERVICE（阻塞业务）”：阻塞业务 |
| ROAMVOLUMELIMIT | 漫游用户的PDU流量阈值(MB) | local_planned | optional | 0 | 整数类型，取值范围是0~2147483647，单位是兆字节。 |
| BLKFREESRV | 会话层异常返回码动作为Block时阻塞免费业务 | local_planned | optional | PASS | <br>- “PASS（不阻塞）”：不阻塞免费业务。 |
| NOQUOTATRIGGER | 无配额更新开关 | local_planned | optional | ENABLE | <br>- “ENABLE（使能）”：允许在接入侧更新或PDU会话级阈值到触发上报时发起配额更新请求 |
| QHTEXPIREDRSU | QHT超时触发的N40消息的MUU中是否携带RSU | local_planned | optional | WITHOUT_RSU | <br>- “WITH_RSU（携带RSU）”：QHT超时触发的N40请求消息中携带RSU。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/WSFD-011206 支持融合计费参考信息_74013176.md`**
- 操作步骤上下文（±2 行原文）：
  L28:
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)
    > - [**ADD SELECTCCTBYCC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板绑定/增加基于CC配置融合计费模板处理（ADD SELECTCCTBYCC）_09654384.md)
    > - [**ADD PDUTRIGGER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/PDU级Trigger/增加PDU会话级的trigger参数（ADD PDUTRIGGER）_09653225.md)

**md：`WSFD-011206/计费会话更新流程_01_10002.md`**
- 操作步骤上下文（±2 行原文）：
  L184:
    > ![](计费会话更新流程_01_10002.assets/zh-cn_image_0278888691_2.png)
    > 
    > 1. SMF通过**ADD CCT**命令本地配置RG级配额的有效时长，SMF收到CHF下发的配额后会按照有效时长启动定时器，超时后SMF将向UPF查询配额用量并上报CHF。即SMF首先向UPF发送[PFCP Session Modification Request](../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Modification Request_32686661.md)消息，发起计费即时查询，查询配额用量。
    > 2. UPF向SMF返回[PFCP Session Modification Response](../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Modification Response_86008994.md)消息，根据指示上报计费信息。
    > 3. SMF向CHF发送[Nchf_ConvergedCharging_ChargingDataUpdate Request](../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Nchf/N40/Nchf_ConvergedCharging_Charging_f4a8bbee/Nchf_ConvergedCharging_ChargingDataUpdate Request_23690004.md)消息，更新计费会话，申请新的配额。当**SET CNVRGDCHGPARA**命令“MERGERGVTSW”参数配置为“ENABLE”时，支持对同时发生的RG级VT事件进行合并，一起上报给CHF。当“MERGERGVTSW”参数配置为“DISABLE”时，每个RG级VT事件单独上报CHF，不做消息合并。

**md：`WSFD-011206/配置融合计费模板_93400212.md`**
- 数据规划表（该命令的参数行）：
  | **ADD CCT** | 融合计费模板名称（CCTMPLTNAME） | cct_test | 本端规划 | 新增CCT模板。 |
  | **ADD CCT** | 配额空闲时间门限值(秒)（QHT） | 0 | 本端规划 | 设置配额空闲时间门限值，数据包停止传送后，QHT立即开始计时，当数据包停止传送时间达到此门限值，向CHF上报使用的配额。 |
  | **ADD CCT** | 流量阈值触发百分比(%)（VQT） | 20 | 本端规划 | 设置流量阈值。 |
  | **ADD CCT** | 时间阈值触发百分比(%)（TQT） | 20 | 本端规划 | 设置时间阈值。 |
  | **ADD CCT** | 事件阈值触发百分比(%)（UQT） | 0 | 本端规划 | 设置事件阈值。 |
  | **ADD CCT** | 在线配额有效时长(分)（VT） | 30 | 本端规划 | RG级配额的有效时长，即SMF收到CHF下发的配额后按有效时长启定时器，超时后SMF立即向CHF上报配额用量并申请新配额。 |
  | **ADD CCT** | 计费条件改变阈值（MAXNUMOFCCC） | 3 | 本端规划 | 指定计费条件改变几次后会触发Charging Data Request Update消息。 |
  | **ADD CCT** | PDU流量阈值(MB)（PDUVOLUMELIMIT） | 500 | 本端规划 | 指定PDU级触发Charging Data Request Update消息的流量阈值。 |
  | **ADD CCT** | PDU时长阈值(分钟)（PDUTIMELIMIT） | 30 | 本端规划 | 指定PDU级别触发Charging Data Request Update消息的时长阈值。 |
  | **ADD CCT** | 业务级流量阈值(MB)（RGVOLUMELIMIT） | 500 | 本端规划 | 指定RG级别触发Charging Data Request Update消息的流量阈值。 |
  | **ADD CCT** | 业务级时长阈值(分钟)（RGTIMELIMIT） | 30 | 本端规划 | 指定RG级别触发Charging Data Request Update消息的时长阈值。 |
  | **ADD CCT** | 最终配额动作指示终结方式（FUATERMINATE） | TERM_SERVICE | 本端规划 | 配置融合计费模板中最终配额动作指示终结方式为阻塞业务。 |
  | **ADD CCT** | 时间格式（TIMEFORMAT） | LocalTime | 本端规划 | 指定发给CHF的消息中的时间格式为localtime。 |
  | **ADD CCT** | 最大携带的业务容器数量（MAXSVCCONTAINER） | 100 | 本端规划 | 控制N40消息中最大可以携带的容器数，避免在延时上报场景，用量长期不上报CHF时容器个数过多和消息超大，并造成数据无法备份问题。<br>当消息中业务容器数量大于等于该值，会强制发送一个N40接口更新消息给CHF，并携带TriggerType为“MANAGEMENT_INTERVENTION”。取值0表示对消息中的业务容器数量不做限制。 |
  | **ADD CCT** | RAN-SecondaryRAT-Usage-Report上报CHF的阈值（SECRUTHRESHOLD） | 100 | 本端规划 | 当SMF检查当前的RAN-SecondaryRAT-Usage-Report数量已达到过阈值配置，发起用量下查并上报CHF，上报TriggerType为MANAGEMENT_INTERVENTION。<br>该参数在<br>****ADD N40MSGTEMP****<br>命令的<br>“SECRATUSAGE”<br>参数配置为ENABLE时才生效。 |
- 任务示例脚本（该命令行）：
  `ADD CCT: CCTMPLTNAME="cct_test", QHT=0, VQT=20, TQT=20, UQT=0, VT=30, MAXNUMOFCCC=3, PDUVOLUMELIMIT=500, PDUTIMELIMIT=30, RGVOLUMELIMIT=500, RGTIMELIMIT=30, FUATERMINATE=TERM_SERVICE, TIMEFORMAT=LocalTime, MAXSVCCONTAINER=100, SECRUTHRESHOLD=100;`
- 操作步骤上下文（±2 行原文）：
  L74:
    > - 配置CC粒度的CCT。
    >     1. 配置CCT模板。
    >       **ADD CCT**
    >     2. 配置计费属性。
    >       请参见 [配置计费属性CC](配置计费属性CC_90776700.md) 。
  L81:
    > - 配置DNN粒度的CCT。
    >     1. 配置CCT模板。
    >       **ADD CCT**
    >     2. 配置DNN。
    >       **ADD APN**
  L88:
    > - 配置UserProfile粒度的CCT。
    >     1. 配置CCT模板。
    >       **ADD CCT**
    >     2. 配置UserProfile，将CCT绑定到UserProfile上。
    >           a. 配置UserProfile。

### WSFD-109003

**md：`WSFD-109003/WSFD-109003 基于业务时长的计费参考信息_74013180.md`**
- 操作步骤上下文（±2 行原文）：
  L20:
    > - [**LST OFCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/显示离线计费模板（LST OFCTEMPLATE）_09896914.md)
    > - [**RMV OFCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/删除离线计费模板或者属性（RMV OFCTEMPLATE）_09896913.md)
    > - [**ADD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)
    > - [**MOD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/修改融合计费模板（MOD CCT）_09652641.md)
    > - [**RMV CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/删除融合计费模板（RMV CCT）_09653730.md)

### WSFD-109004

**md：`WSFD-109004/WSFD-109004 基于业务流量的计费参考信息_74013203.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - [**RMV DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/删除DCC模板（RMV DCCTEMPLATE）_09896925.md)
    > - [**LST DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/查询DCC模板（LST DCCTEMPLATE）_09896933.md)
    > - [**ADD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)
    > - [**MOD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/修改融合计费模板（MOD CCT）_09652641.md)
    > - [**RMV CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/删除融合计费模板（RMV CCT）_09653730.md)

### WSFD-109007

**md：`WSFD-109007/WSFD-109007 支持事件计费参考信息_74112323.md`**
- 操作步骤上下文（±2 行原文）：
  L18:
    > - [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)
    > - [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
    > - [**ADD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)

**md：`WSFD-109007/配置事件计费功能_74112321.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/增加融合计费模板（ADD CCT）_09653176.md) | CCTMPLTNAME（融合计费模板名称） | cct-test | 本端规划 | 配置融合计费的CCT模板。 |
- 任务示例脚本（该命令行）：
  `ADD CCT: CCTMPLTNAME="cct-test";`
- 操作步骤上下文（±2 行原文）：
  L87:
    > 6. 配置融合计费模板或在线计费模板。
    >     - 配置融合计费模板。
    >       [**ADD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)
    >       [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
    >     - 配置在线计费模板。
  L144:
    > 
    > ```
    > ADD CCT: CCTMPLTNAME="cct-test";
    > SET USRPROFCHARGE: USRPROFNAME="up-test", CCTEMPLATE="cct-test";
    > ```

## ④ 自动比对
- 命令真相参数（25）：['BLKFREESRV', 'CCTMPLTNAME', 'FUATERMINATE', 'MAXNUMOFCCC', 'MAXSVCCONTAINER', 'MAXUSEDSRVNUM', 'NOQUOTATRIGGER', 'PDUTIMELIMIT', 'PDUVOLUMELIMIT', 'QFTIMELIMIT', 'QFVOLUMELIMIT', 'QHT', 'QHTEXPIREDRSU', 'QHTRPTTRIGGER', 'RGTIMELIMIT', 'RGVOLUMELIMIT', 'ROAMFUATERMACT', 'ROAMVOLUMELIMIT', 'SECRUTHRESHOLD', 'TIMEFORMAT', 'TQT', 'UCITIMER', 'UQT', 'VQT', 'VT']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 16}（多值→atom 应考虑 decision_driven）
