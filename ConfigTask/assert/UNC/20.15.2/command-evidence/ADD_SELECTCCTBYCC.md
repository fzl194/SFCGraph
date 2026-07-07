# 命令证据包：ADD SELECTCCTBYCC
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板绑定/增加基于CC配置融合计费模板处理（ADD SELECTCCTBYCC）_09654384.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF、SGW-C**

该命令用于增加基于CC配置融合计费模板处理。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 最多可输入101条记录。
- 不允许配置的CCVALUE和掩码CCMASK取与后的值不等于CCVALUE。
- 不允许配置的CCVALUE和掩码CCMASK取与后的值，与当前已有配置的CCVALUE和对应的CCMASK取与后的值相等。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CCTYPE | CC类型 | global_planned | required | 无 | <br>- DEFAULT（未指定Charge Characteristic的值） |
| CCVALUE | Charge Characteristic值 | global_planned | conditional | 无 | 字符串类型，输入长度范围是1~6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| MASK | Charge Characteristic特定值掩码 | global_planned | conditional | 无 | 字符串类型，输入长度范围是1~6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| PRIORITY | Charge Characteristic优先级 | global_planned | conditional | 无 | 整数类型，取值范围是1~65535。 |
| CCTMPLTNAME | 融合计费模板名称 | global_planned | optional | 无 | 字符串类型，输入长度范围是1~63。不区分大小写。 |
| SERVINGCCT | I-SMF/SGW使用的融合计费模板名称 | global_planned | optional | 无 | 字符串类型，输入长度范围是0~63。不区分大小写。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/WSFD-011206 支持融合计费参考信息_74013176.md`**
- 操作步骤上下文（±2 行原文）：
  L29:
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)
    > - [**ADD SELECTCCTBYCC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板绑定/增加基于CC配置融合计费模板处理（ADD SELECTCCTBYCC）_09654384.md)
    > - [**ADD PDUTRIGGER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/PDU级Trigger/增加PDU会话级的trigger参数（ADD PDUTRIGGER）_09653225.md)
    > - [**ADD RGTRIGGER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/RG级Trigger/增加RG级的trigger参数（ADD RGTRIGGER）_09653787.md)

**md：`WSFD-011206/配置融合计费模板_93400212.md`**
- 数据规划表（该命令的参数行）：
  | **ADD SELECTCCTBYCC** | Charge Characteristic类型（CCTYPE） | VALUE | 本端规划 | 基于CC粒度，将CCT绑定到特定CC下。 |
  | **ADD SELECTCCTBYCC** | Charge Characteristic值（CCVALUE） | 0x0800 | 全网规划 | 基于CC粒度，将CCT绑定到特定CC下。 |
  | **ADD SELECTCCTBYCC** | 融合计费模板名称（CCTEMPLATENAME） | cct_test | 已配置数据中获取 | 基于CC粒度，将CCT绑定到特定CC下。 |
- 任务示例脚本（该命令行）：
  `ADD SELECTCCTBYCC: CCTYPE=VALUE, CCVALUE="0x0800", CCTMPLTNAME="cct_test";`
- 操作步骤上下文（±2 行原文）：
  L78:
    >       请参见 [配置计费属性CC](配置计费属性CC_90776700.md) 。
    >     3. 配置CCT模板绑定CC。
    >       **ADD SELECTCCTBYCC**
    > - 配置DNN粒度的CCT。
    >     1. 配置CCT模板。
  L127:
    > ```
    > ADD CCT: CCTMPLTNAME="cct_test", QHT=0, VQT=20, TQT=20, UQT=0, VT=30, MAXNUMOFCCC=3, PDUVOLUMELIMIT=500, PDUTIMELIMIT=30, RGVOLUMELIMIT=500, RGTIMELIMIT=30, FUATERMINATE=TERM_SERVICE, TIMEFORMAT=LocalTime, MAXSVCCONTAINER=100, SECRUTHRESHOLD=100;
    > ADD SELECTCCTBYCC: CCTYPE=VALUE, CCVALUE="0x0800", CCTMPLTNAME="cct_test";
    > ```
    > 

## ④ 自动比对
- 命令真相参数（6）：['CCTMPLTNAME', 'CCTYPE', 'CCVALUE', 'MASK', 'PRIORITY', 'SERVINGCCT']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 1, '全网规划': 1, '已配置数据中获取': 1}（多值→atom 应考虑 decision_driven）
