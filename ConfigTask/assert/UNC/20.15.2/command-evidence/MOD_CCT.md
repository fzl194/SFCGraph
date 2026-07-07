# 命令证据包：MOD CCT
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/修改融合计费模板（MOD CCT）_09652641.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于修改融合计费模板（Converged Charging Template），用于配置融合计费相关参数。
**notes（规格/上限→应投影 atom rule）**：
- 该命令执行后立即生效。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CCTMPLTNAME | 融合计费模板名称 | local_planned | required | 无 | 字符串类型，输入长度范围是1~63。不区分大小写。 |
| QHT | 配额空闲时间门限值(秒) | local_planned | optional | 无 | 整数类型，取值范围是0，5~3600。 |
| VQT | 流量阈值触发百分比(%) | local_planned | optional | 无 | 整数类型，取值范围是0~50。 |
| TQT | 时间阈值触发百分比(%) | local_planned | optional | 无 | 整数类型，取值范围是0~50。 |
| UQT | 事件阈值触发百分比(%) | local_planned | optional | 无 | 整数类型，取值范围是0~50。 |
| VT | 在线配额有效时长(分) | local_planned | optional | 无 | 整数类型，取值范围是0，5~1440。 |
| MAXNUMOFCCC | 计费条件改变阈值 | local_planned | optional | 无 | 整数类型，取值范围是1~10。 |
| PDUVOLUMELIMIT | PDU流量阈值(MB) | local_planned | optional | 无 | 整数类型，取值范围是0~2147483647，单位是兆字节。备注：1兆字节为1048576字节。 |
| PDUTIMELIMIT | PDU时长阈值(分钟) | local_planned | optional | 无 | 整数类型，取值范围是0~1440。 |
| RGVOLUMELIMIT | 业务级流量阈值(MB) | local_planned | optional | 无 | 整数类型，取值范围是0~2147483647，单位是兆字节。备注：1兆字节为1048576字节。 |
| RGTIMELIMIT | 业务级时长阈值(分钟) | local_planned | optional | 无 | 整数类型，取值范围是0~1440。 |
| QFVOLUMELIMIT | QF流量阈值(MB) | local_planned | optional | 无 | 整数类型，取值范围是0~2147483647，单位是兆字节。备注：1兆字节为1048576字节。 |
| QFTIMELIMIT | QF时长阈值(分钟) | local_planned | optional | 无 | 整数类型，取值范围是0~1440。 |
| UCITIMER | 业务停止时长(分钟) | 对端协商 | optional | 无 | 整数类型，取值范围是0~1440。 |
| FUATERMINATE | 最终配额动作指示终结方式 | local_planned | optional | 无 | <br>- “TERM_SERVICE（阻塞业务）”：阻塞业务 |
| TIMEFORMAT | 时间格式 | local_planned | optional | 无 | <br>- “LocalTime（本地时间）”：指定发给CHF的消息中的时间格式为localtime |
| MAXSVCCONTAINER | 最大携带的业务容器数量 | local_planned | optional | 无 | 整数类型，取值范围是0~100。 |
| SECRUTHRESHOLD | RAN-SecondaryRAT-Usage-Report上报CHF的阈值 | global_planned | optional | 无 | 整数类型，取值范围是0~100。 |
| MAXUSEDSRVNUM | 最大可使用的业务个数 | local_planned | optional | 无 | 整数类型，取值范围是0~100。 |
| QHTRPTTRIGGER | QHT超时触发的容器中Trigger的值 | local_planned | optional | 无 | <br>- “QHT（上报QHT）”：Nchf消息容器中Trigger的值填写QHT。 |
| ROAMFUATERMACT | 漫游用户最终配额动作指示终结方式 | local_planned | conditional | 无 | <br>- “TERM_SERVICE（阻塞业务）”：阻塞业务 |
| ROAMVOLUMELIMIT | 漫游用户的PDU流量阈值(MB) | local_planned | optional | 无 | 整数类型，取值范围是0~2147483647，单位是兆字节。 |
| BLKFREESRV | 会话层异常返回码动作为Block时阻塞免费业务 | local_planned | optional | 无 | <br>- “PASS（不阻塞）”：不阻塞免费业务。 |
| NOQUOTATRIGGER | 无配额更新开关 | local_planned | optional | 无 | <br>- “ENABLE（使能）”：允许在接入侧更新或PDU会话级阈值到触发上报时发起配额更新请求 |
| QHTEXPIREDRSU | QHT超时触发的N40消息的MUU中是否携带RSU | local_planned | optional | 无 | <br>- “WITH_RSU（携带RSU）”：QHT超时触发的N40请求消息中携带RSU。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/使用全局CCT模板进行融合计费实例_93029782.md`**
- 数据规划表（该命令的参数行）：
  | **MOD CCT** | CCTMPLTNAME（融合计费模板名称） | global | 本端规划 | 配置全局通用参数CCT模板。 |
  | **MOD CCT** | QHT（配额空闲时间门限值(秒)） | 5 | 本端规划 | 配置全局通用参数CCT模板。 |
- 任务示例脚本（该命令行）：
  `MOD CCT:CCTMPLTNAME="global",QHT=5;`
- 操作步骤上下文（±2 行原文）：
  L77:
    > 
    > ```
    > MOD CCT:CCTMPLTNAME="global",QHT=5;
    > ```
    > 

**md：`WSFD-011206/配置融合计费模板_93400212.md`**
- 数据规划表（该命令的参数行）：
  | **MOD CCT** | 融合计费模板名称（CCTMPLTNAME） | global | 本端规划 | 修改全局通用参数CCT模板。 |
  | **MOD CCT** | 配额空闲时间门限值(秒)（QHT） | 5 | 本端规划 | 修改全局通用参数CCT模板。 |
- 任务示例脚本（该命令行）：
  `MOD CCT: CCTMPLTNAME="global", QHT=5;`
- 操作步骤上下文（±2 行原文）：
  L71:
    > - 配置全局通用CCT模板。
    >     1. 修改系统默认配置的全局通用参数CCT模板，该模板名称为 “global” 。
    >       **MOD CCT**
    > - 配置CC粒度的CCT。
    >     1. 配置CCT模板。
  L120:
    > 
    > ```
    > MOD CCT: CCTMPLTNAME="global", QHT=5;
    > ```
    > 

### WSFD-109003

**md：`WSFD-109003/WSFD-109003 基于业务时长的计费参考信息_74013180.md`**
- 操作步骤上下文（±2 行原文）：
  L21:
    > - [**RMV OFCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/删除离线计费模板或者属性（RMV OFCTEMPLATE）_09896913.md)
    > - [**ADD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)
    > - [**MOD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/修改融合计费模板（MOD CCT）_09652641.md)
    > - [**RMV CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/删除融合计费模板（RMV CCT）_09653730.md)
    > - [**LST CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/查询融合计费模板（LST CCT）_09653820.md)

**md：`WSFD-109003/激活基于业务时长的计费_74013179.md`**
- 数据规划表（该命令的参数行）：
  | [**MOD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/修改融合计费模板（MOD CCT）_09652641.md) | 融合计费模板名称（CCTMPLTNAME） | cct-test | 本端规划 | 配置CCT模板中的时长计费参数。 |
  | [**MOD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/修改融合计费模板（MOD CCT）_09652641.md) | 配额空闲时间门限值（秒）（QHT） | 5 | 本端规划 | 配置CCT模板中的时长计费参数。 |
  | [**MOD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/修改融合计费模板（MOD CCT）_09652641.md) | 时间阈值触发百分比（%）（TQT） | 30 | 本端规划 | 配置CCT模板中的时长计费参数。 |
  | [**MOD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/修改融合计费模板（MOD CCT）_09652641.md) | 在线配额有效时长（分）（VT） | 40 | 本端规划 | 配置CCT模板中的时长计费参数。 |
- 任务示例脚本（该命令行）：
  `MOD CCT: CCTMPLTNAME="cct-test", QHT=40, TQT=30, VT=40;`
- 操作步骤上下文（±2 行原文）：
  L60:
    >   [**MOD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/修改DCC模板（MOD DCCTEMPLATE）_09896924.md)
    >   [**MOD OFCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/修改离线计费模板（MOD OFCTEMPLATE）_09896909.md)
    >   [**MOD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/修改融合计费模板（MOD CCT）_09652641.md)
    >   > **说明**
    >   > DCC在线计费模板、离线计费模板和融合计费模板均已配置可参见 [激活离线计费](../WSFD-011201 支持离线计费/激活离线计费_25768943.md) 、 [激活Gy/Diameter在线计费](../WSFD-109001 Gy_Diameter在线计费/激活Gy_Diameter在线计费_27639894.md) 或 [激活支持融合计费](../WSFD-011206 支持融合计费/激活支持融合计费_73659885.md) ，此处通过MOD命令配置时长相关参数。
  L95:
    > 
    > ```
    > MOD CCT: CCTMPLTNAME="cct-test", QHT=40, TQT=30, VT=40;
    > ```

### WSFD-109004

**md：`WSFD-109004/WSFD-109004 基于业务流量的计费参考信息_74013203.md`**
- 操作步骤上下文（±2 行原文）：
  L17:
    > - [**LST DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/查询DCC模板（LST DCCTEMPLATE）_09896933.md)
    > - [**ADD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)
    > - [**MOD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/修改融合计费模板（MOD CCT）_09652641.md)
    > - [**RMV CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/删除融合计费模板（RMV CCT）_09653730.md)
    > - [**LST CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/查询融合计费模板（LST CCT）_09653820.md)

**md：`WSFD-109004/激活基于业务流量的计费_74013202.md`**
- 数据规划表（该命令的参数行）：
  | [**MOD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/修改融合计费模板（MOD CCT）_09652641.md) | CCTMPLTNAME（融合计费模板名称） | cct-test | 本端规划 | 配置CCT模板中的流量计费参数。 |
  | [**MOD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/修改融合计费模板（MOD CCT）_09652641.md) | VQT（流量阈值触发百分比（%）） | 30 | 本端规划 | 配置CCT模板中的流量计费参数。 |
- 任务示例脚本（该命令行）：
  `MOD CCT: CCTMPLTNAME="cct-test", VQT=30;`
- 操作步骤上下文（±2 行原文）：
  L46:
    > 2. 修改在线计费模板/融合计费模板，配置基于业务流量的计费。
    >   [**MOD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/修改DCC模板（MOD DCCTEMPLATE）_09896924.md)
    >   [**MOD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/修改融合计费模板（MOD CCT）_09652641.md)
    >   > **说明**
    >   > DCC在线计费模板和融合计费模板均已配置可参见 [激活Gy/Diameter在线计费](../WSFD-109001 Gy_Diameter在线计费/激活Gy_Diameter在线计费_27639894.md) 或 [激活支持融合计费](../WSFD-011206 支持融合计费/激活支持融合计费_73659885.md) ，此处通过MOD命令配置流量相关参数。
  L67:
    > 
    > ```
    > MOD CCT: CCTMPLTNAME="cct-test", VQT=30;
    > ```
    > 

## ④ 自动比对
- 命令真相参数（25）：['BLKFREESRV', 'CCTMPLTNAME', 'FUATERMINATE', 'MAXNUMOFCCC', 'MAXSVCCONTAINER', 'MAXUSEDSRVNUM', 'NOQUOTATRIGGER', 'PDUTIMELIMIT', 'PDUVOLUMELIMIT', 'QFTIMELIMIT', 'QFVOLUMELIMIT', 'QHT', 'QHTEXPIREDRSU', 'QHTRPTTRIGGER', 'RGTIMELIMIT', 'RGVOLUMELIMIT', 'ROAMFUATERMACT', 'ROAMVOLUMELIMIT', 'SECRUTHRESHOLD', 'TIMEFORMAT', 'TQT', 'UCITIMER', 'UQT', 'VQT', 'VT']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 10}（多值→atom 应考虑 decision_driven）
