# 命令证据包：ADD OFCTEMPLATE
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/增加离线计费模板（ADD OFCTEMPLATE）_09896908.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

此命令用于增加离线计费模板。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为100。
- 当前版本不支持此命令的BTIVALUE参数。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| OFCTEMPLATENAME | 离线计费模板名 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格。 |
| GCDRVERSION | G-CDR版本 | 对端协商 | optional | R7V740_EGCDR | 枚举类型。 |
| PGWCDRVERSION | PGW-CDR版本 | 对端协商 | optional | R8V850_PGW_CDR | 枚举类型。 |
| SGWCDRVERSION | SGW-CDR版本 | local_planned | optional | R8V850_SGW_CDR | 枚举类型。 |
| RECORDSEQNUMBER | Record Sequence Number字段起始值 | local_planned | optional | 0 | 整数类型，取值范围为0～1。1、0表示CDR话单中Record Sequence Number字段的 |
| TQM | 时长配额机制 | local_planned | optional | QCT | 枚举类型。 |
| QCTVALUE | QCT时长（秒） | local_planned | conditional | 0 | 整数类型，取值范围为0～200，单位是秒。 |
| BTIVALUE | BTI时长（秒） | local_planned | conditional | 60 | 整数类型，取值范围为60～86400，单位是秒。 |
| QHTVALUE | QHT时长（秒） | local_planned | optional | 0 | 整数类型，取值范围为0～3600，单位是秒。 |
| CDRTIMEFORMAT | 话单时间格式 | local_planned | optional | LOCAL_TIME | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L21:
    > - [**SET SGWAPNCHGMETH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW APN计费方式/设置SGW APN计费方式（SET SGWAPNCHGMETH）_09896992.md)
    > - [**SET SGWCHGMETH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/计费属性控制/设置SGW Charge Method（SET SGWCHGMETH）_09896985.md)
    > - [**ADD OFCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/增加离线计费模板（ADD OFCTEMPLATE）_09896908.md)
    > - [**SET OFCTHRESHOLD**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/设置离线计费阈值（SET OFCTHRESHOLD）_09896910.md)
    > - [**SET CDRTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/配置离线计费话单产生开关（SET CDRTRIGGER）_09896911.md)

**md：`WSFD-011201/离线计费话单（GGSN_SGW-C_PGW-C）_92172742.md`**
- 操作步骤上下文（±2 行原文）：
  L21:
    > #### [话单类型和话单版本](#ZH-CN_TOPIC_0292172742)
    > 
    > GGSN/SGW-C/PGW-C与CG可以产生 [表1](#ZH-CN_TOPIC_0292172742__table_03C48215) 所示的多种类型的话单（通过 **ADD OFCTEMPLATE** 配置）。
    > 
    > *表1 话单类型、话单版本及其描述*

**md：`WSFD-011201/配置离线计费参数（GGSN_SGW-C_PGW-C）_95923590.md`**
- 数据规划表（该命令的参数行）：
  | **ADD OFCTEMPLATE** | 离线计费模板名（OFCTEMPLATENAME） | offlinecharge-test | 本端规划 | 计费模板 |
  | **ADD OFCTEMPLATE** | 时长配额机制（TQM） | QCT | 本端规划 | 计费方式 |
  | **ADD OFCTEMPLATE** | QCT时长（秒）（QCTVALUE） | 0 | 本端规划 | 计费方式 |
  | **ADD OFCTEMPLATE** | QHT时长（秒）（QHTVALUE） | 30 | 本端规划 | 定时器信息 |
  | **ADD OFCTEMPLATE** | G-CDR版本（GCDRVERSION） | R7V740_GCDR | 全网规划 | 话单协议版本<br>说明：如果部署GUL切换网络，话单版本应该配置为R8及以后的版本。 |
  | **ADD OFCTEMPLATE** | PGW-CDR版本（PGWCDRVERSION） | R8V850_PGW_CDR | 全网规划 | 话单协议版本<br>说明：如果部署GUL切换网络，话单版本应该配置为R8及以后的版本。 |
  | **ADD OFCTEMPLATE** | SGW-CDR版本（SGWCDRVERSION） | R8V850_SGW_CDR | 全网规划 | 话单协议版本<br>说明：如果部署GUL切换网络，话单版本应该配置为R8及以后的版本。 |
  | **ADD OFCTEMPLATE** | Record Sequence Number字段起始值（RECORDSEQNUMBER） | 0 | 本端规划 | Record Sequence Number字段起始值 |
- 任务示例脚本（该命令行）：
  `ADD OFCTEMPLATE: OFCTEMPLATENAME="offlinecharge-test",TQM=QCT,QCTVALUE=0;`
- 操作步骤上下文（±2 行原文）：
  L82:
    > 1. 配置OFCTemplate模板下的计费参数。
    >     a. 配置话单版本信息、产生话单的时间格式、Record Sequence Number字段的起始值、定时器QHT信息和计费方式。
    >       **ADD OFCTEMPLATE**
    >     b. 配置阈值信息。
    >       **SET OFCTHRESHOLD**
  L137:
    > 1. 配置计费参数模板。
    >   ```
    >   ADD OFCTEMPLATE: OFCTEMPLATENAME="offlinecharge-test",TQM=QCT,QCTVALUE=0;
    >   ```
    >   ```

**md：`WSFD-011201/配置话单可选功能（GGSN_SGW-C_PGW-C）_95923448.md`**
- 数据规划表（该命令的参数行）：
  | **ADD OFCTEMPLATE** | 离线计费模板名（OFCTEMPLATENAME） | offlinecharge-test | 已配置数据中获取 | LastActivity计费只有在UTC时间格式下生效。<br>在<br>[配置离线计费参数（GGSN/SGW-C/PGW-C）](配置离线计费参数（GGSN_SGW-C_PGW-C）_95923590.md)<br>中已通过命令<br>**ADD OFCTEMPLATE**<br>进行配置，可以使用命令<br>**LST OFCTEMPLATE**<br>查询。 |
  | **ADD OFCTEMPLATE** | 话单时间格式（CDRTIMEFORMAT） | UTC | 已配置数据中获取 | LastActivity计费只有在UTC时间格式下生效。<br>在<br>[配置离线计费参数（GGSN/SGW-C/PGW-C）](配置离线计费参数（GGSN_SGW-C_PGW-C）_95923590.md)<br>中已通过命令<br>**ADD OFCTEMPLATE**<br>进行配置，可以使用命令<br>**LST OFCTEMPLATE**<br>查询。 |

### WSFD-011202

**md：`WSFD-011202/激活支持热计费功能_28072077.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD OFCTEMPLATE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/增加离线计费模板（ADD OFCTEMPLATE）_09896908.md)** | G-CDR版本(GCDRVERSION) | R7V740_EGCDR | 全网规划 | 配置话单版本。 |
- 任务示例脚本（该命令行）：
  `ADD OFCTEMPLATE:OFCTEMPLATENAME="offlinecharg-test",GCDRVERSION=R7V740_EGCDR,TQM=QCT,QCTVALUE=30;`
- 操作步骤上下文（±2 行原文）：
  L67:
    > 
    > ```
    > ADD OFCTEMPLATE:OFCTEMPLATENAME="offlinecharg-test",GCDRVERSION=R7V740_EGCDR,TQM=QCT,QCTVALUE=30;
    > ```
    > 

### WSFD-109003

**md：`WSFD-109003/WSFD-109003 基于业务时长的计费参考信息_74013180.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - [**RMV DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/删除DCC模板（RMV DCCTEMPLATE）_09896925.md)
    > - [**LST DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/查询DCC模板（LST DCCTEMPLATE）_09896933.md)
    > - [**ADD OFCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/增加离线计费模板（ADD OFCTEMPLATE）_09896908.md)
    > - [**MOD OFCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/修改离线计费模板（MOD OFCTEMPLATE）_09896909.md)
    > - [**LST OFCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/显示离线计费模板（LST OFCTEMPLATE）_09896914.md)

**md：`WSFD-109003/基于业务时长的计费（适用于离线计费）_66402115.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > **时长计费的方式**
    > 
    > 支持2种类型的时长计费：连续时长计费、QCT（Quota-Consumption-Time）时长计费。每种方式统计时长的方法不一样。离线计费的时长计费方式可以通过本地配置 [**ADD OFCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/增加离线计费模板（ADD OFCTEMPLATE）_09896908.md) 中参数 “TQM” 选择。离线计费系统中，QCT参数取值通过本地配置 [**ADD OFCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/增加离线计费模板（ADD OFCTEMPLATE）_09896908.md) 中参数 “QCTVALUE” 获取。
    > 
    > 从计费精细度方面而言，QCT方式精度最高，连续时长计费其次。

## ④ 自动比对
- 命令真相参数（10）：['BTIVALUE', 'CDRTIMEFORMAT', 'GCDRVERSION', 'OFCTEMPLATENAME', 'PGWCDRVERSION', 'QCTVALUE', 'QHTVALUE', 'RECORDSEQNUMBER', 'SGWCDRVERSION', 'TQM']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 5, '全网规划': 4, '已配置数据中获取': 2}（多值→atom 应考虑 decision_driven）
