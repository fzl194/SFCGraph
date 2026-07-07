# 命令证据包：ADD WEEKDAY
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/工作日/配置计费星期表（ADD WEEKDAY）_09896831.md`
> 用该命令的特性数：4

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

该命令用来配置计费星期表记录，配置指定每周的费率类型为工作日或周末。

UNC支持费率时间段配置，即可以根据不同费率类型（包括节假日、工作日和周末三种费率类型）的时间段来配置不同的费率。节假日的配置见命令：ADD FESTIVAL。

配置本命令后，当用户持续在线，会出现跨费率类型的切换。切换的时间点为00:00:00。如用户在星期五和星期六两天
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为119。
- 系统支持对星期内的每一天最大可配置17条记录，总共可配置7*17=119条记录。
- 不允许配置CCVALUE和CCMASK取与操作后的值不等于CCVALUE。
- 当GLOBALFLG为CHARGE_CHARACR时，不允许配置CCVALUE和CCMASK取与后的值与当前已有配置CCVALUE和CCMASK取与后的值相等。
- 该命

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| GLOBALFLG | 全局配置 | global_planned | required | 无 | 枚举类型。 |
| CCVALUE | 计费属性值 | global_planned | conditional | 无 | 字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| CCMASK | 计费属性掩码 | global_planned | conditional | 无 | 字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| CCPRIORITY | 计费属性优先级 | global_planned | conditional | 无 | 整数类型，取值范围为0～65535。 |
| DAYOFWEEK | 周日期 | global_planned | required | 无 | 枚举类型。 |
| TARIFFTYPE | 费率类型 | global_planned | required | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L32:
    > - [**ADD GLBOFCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/全局离线计费模板/增加全局离线计费模板（ADD GLBOFCTEMPLATE）_09896916.md)
    > - [**ADD FESTIVAL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/节假日/增加计费节假日表（ADD FESTIVAL）_09896827.md)
    > - [**ADD WEEKDAY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/工作日/配置计费星期表（ADD WEEKDAY）_09896831.md)
    > - [**ADD TARIFFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/费率切换组/配置费率切换组（ADD TARIFFGROUP）_09896836.md)
    > - [**SET GLBTARIFFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/全局费率切换组/配置全局费率切换组（SET GLBTARIFFGROUP）_09896840.md)

**md：`WSFD-011201/配置离线计费费率切换（GGSN_SGW-C_PGW-C）_95923434.md`**
- 数据规划表（该命令的参数行）：
  | **ADD WEEKDAY** | 全局配置（GLOBALFLG） | CHARGE_CHARACT | 本端规划 | 配置指定周日期的费率类型为工作日或周末。<br>- 该命令可以基于计费CC配置。<br>- 由于统一费率计费不涉及费率切换，因此该命令中的计费类型不包括统一费率计费。**global**参数用于为全局用户配置费率切换。如果没有为用户指定工作日或周末，将使用全局的工作日或周末信息。 |
  | **ADD WEEKDAY** | 计费属性值（CCVALUE） | 0x0800 | 本端规划 | 配置指定周日期的费率类型为工作日或周末。<br>- 该命令可以基于计费CC配置。<br>- 由于统一费率计费不涉及费率切换，因此该命令中的计费类型不包括统一费率计费。**global**参数用于为全局用户配置费率切换。如果没有为用户指定工作日或周末，将使用全局的工作日或周末信息。 |
  | **ADD WEEKDAY** | 周日期（DAYOFWEEK） | MONDAY<br>TUESDAY<br>WEDNESDAY<br>THURSDAY<br>FRIDAY<br>SATURDAY<br>SUNDAY | 全网规划 | 配置指定周日期的费率类型为工作日或周末。<br>- 该命令可以基于计费CC配置。<br>- 由于统一费率计费不涉及费率切换，因此该命令中的计费类型不包括统一费率计费。**global**参数用于为全局用户配置费率切换。如果没有为用户指定工作日或周末，将使用全局的工作日或周末信息。 |
  | **ADD WEEKDAY** | 费率类型（TARIFFTYPE） | WORKDAY<br>WEEKEND | 全网规划 | 配置指定周日期的费率类型为工作日或周末。<br>- 该命令可以基于计费CC配置。<br>- 由于统一费率计费不涉及费率切换，因此该命令中的计费类型不包括统一费率计费。**global**参数用于为全局用户配置费率切换。如果没有为用户指定工作日或周末，将使用全局的工作日或周末信息。 |
- 任务示例脚本（该命令行）：
  `ADD WEEKDAY: GLOBALFLG=CHARGE_CHARACT,CCVALUE="0x0800",DAYOFWEEK=MONDAY,TARIFFTYPE=WORKDAY;`
  `ADD WEEKDAY: GLOBALFLG=CHARGE_CHARACT,CCVALUE="0x0800",DAYOFWEEK=TUESDAY,TARIFFTYPE=WORKDAY;`
  `ADD WEEKDAY: GLOBALFLG=CHARGE_CHARACT,CCVALUE="0x0800",DAYOFWEEK=WEDNESDAY,TARIFFTYPE=WORKDAY;`
  `ADD WEEKDAY: GLOBALFLG=CHARGE_CHARACT,CCVALUE="0x0800",DAYOFWEEK=THURSDAY,TARIFFTYPE=WORKDAY;`
  `ADD WEEKDAY: GLOBALFLG=CHARGE_CHARACT,CCVALUE="0x0800",DAYOFWEEK=FRIDAY,TARIFFTYPE=WORKDAY;`
  `ADD WEEKDAY: GLOBALFLG=CHARGE_CHARACT,CCVALUE="0x0800",DAYOFWEEK=SATURDAY,TARIFFTYPE=WEEKEND;`
  `ADD WEEKDAY: GLOBALFLG=CHARGE_CHARACT,CCVALUE="0x0800",DAYOFWEEK=SUNDAY,TARIFFTYPE=WEEKEND;`
- 操作步骤上下文（±2 行原文）：
  L61:
    >       **ADD FESTIVAL**
    >     b. 配置星期表信息，即设置指定星期的费率类型为工作日或周末。
    >       **ADD WEEKDAY**
    >     c. 配置节假日，工作日或周末的费率时间段。
    >       **ADD TARIFFGROUP**
  L103:
    >   //配置星期。
    >   ```
    >   ADD WEEKDAY: GLOBALFLG=CHARGE_CHARACT,CCVALUE="0x0800",DAYOFWEEK=MONDAY,TARIFFTYPE=WORKDAY;
    >   ```
    >   ```
  L106:
    >   ```
    >   ```
    >   ADD WEEKDAY: GLOBALFLG=CHARGE_CHARACT,CCVALUE="0x0800",DAYOFWEEK=TUESDAY,TARIFFTYPE=WORKDAY;
    >   ```
    >   ```

**md：`WSFD-011201/调测费率切换功能（GGSN_SGW-C_PGW-C）_95923381.md`**
- 数据规划表（该命令的参数行）：
  | **ADD WEEKDAY** | 全局配置（GLOBALFLG） | CHARGE_CHARACT | 本端规划 | 配置指定周日期的费率类型为工作日或周末。 |
  | **ADD WEEKDAY** | 计费属性值（CCVALUE） | 0x0800 | 本端规划 | 配置指定周日期的费率类型为工作日或周末。 |
  | **ADD WEEKDAY** | 周日期（DAYOFWEEK） | MONDAY<br>TUESDAY<br>WEDNESDAY<br>THURSDAY<br>FRIDAY<br>SATURDAY<br>SUNDAY | 全网规划 | 配置指定周日期的费率类型为工作日或周末。 |
  | **ADD WEEKDAY** | 费率类型（TARIFFTYPE） | WORKDAY<br>WEEKEND | 全网规划 | 配置指定周日期的费率类型为工作日或周末。 |

### WSFD-011206

**md：`WSFD-011206/配置费率切换_86411191.md`**
- 数据规划表（该命令的参数行）：
  | **ADD WEEKDAY** | 全局配置（GLOBALFLG） | CHARGE_CHARACT | 本端规划 | 配置指定周日期的费率类型为工作日或周末。<br>- 该命令可以基于计费CC配置。<br>- 由于统一费率计费不涉及费率切换，因此该命令中的计费类型不包括统一费率计费。**global**参数用于为全局用户配置费率切换。如果没有为用户指定工作日或周末，将使用全局的工作日或周末信息。 |
  | **ADD WEEKDAY** | 计费属性值（CCVALUE） | 0x0800 | 本端规划 | 配置指定周日期的费率类型为工作日或周末。<br>- 该命令可以基于计费CC配置。<br>- 由于统一费率计费不涉及费率切换，因此该命令中的计费类型不包括统一费率计费。**global**参数用于为全局用户配置费率切换。如果没有为用户指定工作日或周末，将使用全局的工作日或周末信息。 |
  | **ADD WEEKDAY** | 周日期（DAYOFWEEK） | MONDAY<br>TUESDAY<br>WEDNESDAY<br>THURSDAY<br>FRIDAY<br>SATURDAY<br>SUNDAY | 全网规划 | 配置指定周日期的费率类型为工作日或周末。<br>- 该命令可以基于计费CC配置。<br>- 由于统一费率计费不涉及费率切换，因此该命令中的计费类型不包括统一费率计费。**global**参数用于为全局用户配置费率切换。如果没有为用户指定工作日或周末，将使用全局的工作日或周末信息。 |
  | **ADD WEEKDAY** | 费率类型（TARIFFTYPE） | WORKDAY<br>WEEKEND | 全网规划 | 配置指定周日期的费率类型为工作日或周末。<br>- 该命令可以基于计费CC配置。<br>- 由于统一费率计费不涉及费率切换，因此该命令中的计费类型不包括统一费率计费。**global**参数用于为全局用户配置费率切换。如果没有为用户指定工作日或周末，将使用全局的工作日或周末信息。 |
- 任务示例脚本（该命令行）：
  `ADD WEEKDAY: GLOBALFLG=CHARGE_CHARACT, CCVALUE="0x0800", DAYOFWEEK=MONDAY, TARIFFTYPE=WORKDAY;`
  `ADD WEEKDAY: GLOBALFLG=CHARGE_CHARACT, CCVALUE="0x0800", DAYOFWEEK=TUESDAY, TARIFFTYPE=WORKDAY;`
  `ADD WEEKDAY: GLOBALFLG=CHARGE_CHARACT, CCVALUE="0x0800", DAYOFWEEK=WEDNESDAY, TARIFFTYPE=WORKDAY;`
  `ADD WEEKDAY: GLOBALFLG=CHARGE_CHARACT, CCVALUE="0x0800", DAYOFWEEK=THURSDAY, TARIFFTYPE=WORKDAY;`
  `ADD WEEKDAY: GLOBALFLG=CHARGE_CHARACT, CCVALUE="0x0800", DAYOFWEEK=FRIDAY, TARIFFTYPE=WORKDAY;`
  `ADD WEEKDAY: GLOBALFLG=CHARGE_CHARACT, CCVALUE="0x0800", DAYOFWEEK=SATURDAY, TARIFFTYPE=WEEKEND;`
  `ADD WEEKDAY: GLOBALFLG=CHARGE_CHARACT, CCVALUE="0x0800", DAYOFWEEK=SUNDAY, TARIFFTYPE=WEEKEND;`
- 操作步骤上下文（±2 行原文）：
  L62:
    >       **ADD FESTIVAL**
    >     b. 配置星期表信息，即设置指定星期的费率类型为工作日或周末。
    >       **ADD WEEKDAY**
    >     c. 配置节假日，工作日或周末的费率时间段。
    >       **ADD TARIFFGROUP**
  L95:
    >   //配置星期。
    >   ```
    >   ADD WEEKDAY: GLOBALFLG=CHARGE_CHARACT, CCVALUE="0x0800", DAYOFWEEK=MONDAY, TARIFFTYPE=WORKDAY;
    >   ```
    >   ```
  L98:
    >   ```
    >   ```
    >   ADD WEEKDAY: GLOBALFLG=CHARGE_CHARACT, CCVALUE="0x0800", DAYOFWEEK=TUESDAY, TARIFFTYPE=WORKDAY;
    >   ```
    >   ```

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L44:
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD FESTIVAL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/节假日/增加计费节假日表（ADD FESTIVAL）_09896827.md)
    > - [**ADD WEEKDAY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/工作日/配置计费星期表（ADD WEEKDAY）_09896831.md)
    > - [**ADD TARIFFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/费率切换组/配置费率切换组（ADD TARIFFGROUP）_09896836.md)
    > - [**SET GLBTARIFFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/全局费率切换组/配置全局费率切换组（SET GLBTARIFFGROUP）_09896840.md)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L44:
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD FESTIVAL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/节假日/增加计费节假日表（ADD FESTIVAL）_09896827.md)
    > - [**ADD WEEKDAY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/工作日/配置计费星期表（ADD WEEKDAY）_09896831.md)
    > - [**ADD TARIFFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/费率切换组/配置费率切换组（ADD TARIFFGROUP）_09896836.md)
    > - [**SET GLBTARIFFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/全局费率切换组/配置全局费率切换组（SET GLBTARIFFGROUP）_09896840.md)

## ④ 自动比对
- 命令真相参数（6）：['CCMASK', 'CCPRIORITY', 'CCVALUE', 'DAYOFWEEK', 'GLOBALFLG', 'TARIFFTYPE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 6, '全网规划': 6}（多值→atom 应考虑 decision_driven）
