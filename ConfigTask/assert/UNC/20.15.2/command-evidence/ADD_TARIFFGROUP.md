# 命令证据包：ADD TARIFFGROUP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/费率切换组/配置费率切换组（ADD TARIFFGROUP）_09896836.md`
> 用该命令的特性数：4

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

该命令用来配置费率切换点。如果费率切换点所在的费率切换组不存在，则新建一个费率切换组。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为1000。
- 每个费率切换组可以支持144个费率切换时间段。
- 整系统一共可以支持1000个费率切换组和Charging Characteristic的组合。
- 整系统一共可以支持2000个费率切换点。一个与其它费率点不重复的费率切换段对应两个费率切换点。
- 要求配置CCVALUE和CCMASK取与操作后的值等于CCVALUE。
- 当Gl

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| TARIFFGRPNAME | 费率切换组名 | local_planned | required | 无 | 字符串类型，输入长度范围为1～31。 |
| GLOBALFLG | 全局配置 | local_planned | required | 无 | 枚举类型。 |
| CCVALUE | Charge Characteristic值 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| CCMASK | Charge Characteristic掩码 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| CCPRIORITY | Charge Characteristic优先级 | local_planned | conditional | 无 | 整数类型，取值范围为1～65535。 |
| TARIFFTYPE | 费率类型 | local_planned | required | 无 | 枚举类型。 |
| STARTTIME | 费率切换起始时间 | local_planned | required | 无 | 时间类型，输入格式是HH:MM。 |
| ENDTIME | 费率切换终止时间 | local_planned | required | 无 | 时间类型，输入格式是HH:MM。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L33:
    > - [**ADD FESTIVAL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/节假日/增加计费节假日表（ADD FESTIVAL）_09896827.md)
    > - [**ADD WEEKDAY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/工作日/配置计费星期表（ADD WEEKDAY）_09896831.md)
    > - [**ADD TARIFFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/费率切换组/配置费率切换组（ADD TARIFFGROUP）_09896836.md)
    > - [**SET GLBTARIFFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/全局费率切换组/配置全局费率切换组（SET GLBTARIFFGROUP）_09896840.md)
    > - [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)

**md：`WSFD-011201/配置离线计费费率切换（GGSN_SGW-C_PGW-C）_95923434.md`**
- 数据规划表（该命令的参数行）：
  | **ADD TARIFFGROUP** | 费率切换组名（TARIFFGRPNAME） | testtariff | 本端规划 | 配置费率切换点。<br>- 该命令可以基于计费CC配置。<br>- 由于统一费率计费不涉及费率切换，因此该命令中的**计费属性CC值**不能取值为**0x0200**。**GLOBAL**参数用于为全局用户配置费率切换。如果没有为用户指定费率切换点，则使用全局的费率切换点信息。 |
  | **ADD TARIFFGROUP** | 全局配置（GLOBALFLG） | CHARGE_CHARACT | 本端规划 | 配置费率切换点。<br>- 该命令可以基于计费CC配置。<br>- 由于统一费率计费不涉及费率切换，因此该命令中的**计费属性CC值**不能取值为**0x0200**。**GLOBAL**参数用于为全局用户配置费率切换。如果没有为用户指定费率切换点，则使用全局的费率切换点信息。 |
  | **ADD TARIFFGROUP** | Charge Characteristic值（CCVALUE） | 0x0800 | 本端规划 | 配置费率切换点。<br>- 该命令可以基于计费CC配置。<br>- 由于统一费率计费不涉及费率切换，因此该命令中的**计费属性CC值**不能取值为**0x0200**。**GLOBAL**参数用于为全局用户配置费率切换。如果没有为用户指定费率切换点，则使用全局的费率切换点信息。 |
  | **ADD TARIFFGROUP** | 费率类型（TARIFFTYPE） | FESTIVAL<br>WEEKEND<br>WORKDAY | 全网规划 | 配置费率切换点。<br>- 该命令可以基于计费CC配置。<br>- 由于统一费率计费不涉及费率切换，因此该命令中的**计费属性CC值**不能取值为**0x0200**。**GLOBAL**参数用于为全局用户配置费率切换。如果没有为用户指定费率切换点，则使用全局的费率切换点信息。 |
  | **ADD TARIFFGROUP** | 费率切换起始时间（STARTTIME） | 6:00 | 全网规划 | 配置费率切换点。<br>- 该命令可以基于计费CC配置。<br>- 由于统一费率计费不涉及费率切换，因此该命令中的**计费属性CC值**不能取值为**0x0200**。**GLOBAL**参数用于为全局用户配置费率切换。如果没有为用户指定费率切换点，则使用全局的费率切换点信息。 |
  | **ADD TARIFFGROUP** | 费率切换终止时间（ENDTIME） | 17:00 | 全网规划 | 配置费率切换点。<br>- 该命令可以基于计费CC配置。<br>- 由于统一费率计费不涉及费率切换，因此该命令中的**计费属性CC值**不能取值为**0x0200**。**GLOBAL**参数用于为全局用户配置费率切换。如果没有为用户指定费率切换点，则使用全局的费率切换点信息。 |
- 任务示例脚本（该命令行）：
  `ADD TARIFFGROUP: TARIFFGRPNAME="testtariff",GLOBALFLG=CHARGE_CHARACT,CCVALUE="0x0800",`
  `ADD TARIFFGROUP: TARIFFGRPNAME="testtarif",GLOBALFLG=CHARGE_CHARACT,CCVALUE="0x0800",`
  `ADD TARIFFGROUP: TARIFFGRPNAME="testtarif",GLOBALFLG=CHARGE_CHARACT,CCVALUE="0x0800",`
- 操作步骤上下文（±2 行原文）：
  L63:
    >       **ADD WEEKDAY**
    >     c. 配置节假日，工作日或周末的费率时间段。
    >       **ADD TARIFFGROUP**
    > 2. 配置全局费率切换组。
    >   **SET GLBTARIFFGROUP**
  L125:
    >   //配置节假日和星期的费率时间段。
    >   ```
    >   ADD TARIFFGROUP: TARIFFGRPNAME="testtariff",GLOBALFLG=CHARGE_CHARACT,CCVALUE="0x0800",
    >   TARIFFTYPE=WORKDAY,STARTTIME=06&00,ENDTIME=17&00
    >   ;
  L130:
    >   ```
    >   ```
    >   ADD TARIFFGROUP: TARIFFGRPNAME="testtarif",GLOBALFLG=CHARGE_CHARACT,CCVALUE="0x0800",
    >   TARIFFTYPE=WEEKEND,STARTTIME=06&00,ENDTIME=17&00
    >   ;

**md：`WSFD-011201/调测费率切换功能（GGSN_SGW-C_PGW-C）_95923381.md`**
- 数据规划表（该命令的参数行）：
  | **ADD TARIFFGROUP** | 费率切换组名（TARIFFGRPNAME） | testtariff | 本端规划 | 配置费率切换点 |
  | **ADD TARIFFGROUP** | 全局配置（GLOBALFLG） | CHARGE_CHARACT | 本端规划 | 配置费率切换点 |
  | **ADD TARIFFGROUP** | Charge Characteristic值（CCVALUE） | 0x0800 | 本端规划 | 配置费率切换点 |
  | **ADD TARIFFGROUP** | 费率类型（TARIFFTYPE） | FESTIVAL<br>WEEKEND<br>WORKDAY | 全网规划 | 配置费率切换点 |
  | **ADD TARIFFGROUP** | 费率切换起始时间（STARTTIME） | 6:00 | 全网规划 | 配置费率切换点 |
  | **ADD TARIFFGROUP** | 费率切换终止时间（ENDTIME） | 17:00 | 全网规划 | 配置费率切换点 |

### WSFD-011206

**md：`WSFD-011206/配置费率切换_86411191.md`**
- 数据规划表（该命令的参数行）：
  | **ADD TARIFFGROUP** | 费率切换组名（TARIFFGRPNAME） | tar_nb | 本端规划 | 配置费率切换点。<br>- 该命令可以基于计费CC配置。<br>- 由于统一费率计费不涉及费率切换，因此该命令中的**计费属性CC值**不能取值为**0x0200**。**global**参数用于为全局用户配置费率切换。如果没有为用户指定费率切换点，则使用全局的费率切换点信息。SMF根据计费类型获取费率切换点信息。如果对应某一计费类型的费率切换点没有配置，将使用全局的费率切换点信息。 |
  | **ADD TARIFFGROUP** | 全局配置（GLOBALFLG） | CHARGE_CHARACT | 本端规划 | 配置费率切换点。<br>- 该命令可以基于计费CC配置。<br>- 由于统一费率计费不涉及费率切换，因此该命令中的**计费属性CC值**不能取值为**0x0200**。**global**参数用于为全局用户配置费率切换。如果没有为用户指定费率切换点，则使用全局的费率切换点信息。SMF根据计费类型获取费率切换点信息。如果对应某一计费类型的费率切换点没有配置，将使用全局的费率切换点信息。 |
  | **ADD TARIFFGROUP** | Charge Characteristic值（CCVALUE） | 0x0800 | 本端规划 | 配置费率切换点。<br>- 该命令可以基于计费CC配置。<br>- 由于统一费率计费不涉及费率切换，因此该命令中的**计费属性CC值**不能取值为**0x0200**。**global**参数用于为全局用户配置费率切换。如果没有为用户指定费率切换点，则使用全局的费率切换点信息。SMF根据计费类型获取费率切换点信息。如果对应某一计费类型的费率切换点没有配置，将使用全局的费率切换点信息。 |
  | **ADD TARIFFGROUP** | 费率类型（TARIFFTYPE） | FESTIVAL<br>WEEKEND<br>WORKDAY | 全网规划 | 配置费率切换点。<br>- 该命令可以基于计费CC配置。<br>- 由于统一费率计费不涉及费率切换，因此该命令中的**计费属性CC值**不能取值为**0x0200**。**global**参数用于为全局用户配置费率切换。如果没有为用户指定费率切换点，则使用全局的费率切换点信息。SMF根据计费类型获取费率切换点信息。如果对应某一计费类型的费率切换点没有配置，将使用全局的费率切换点信息。 |
  | **ADD TARIFFGROUP** | 费率切换起始时间（STARTTIME） | 6:00 | 全网规划 | 配置费率切换点。<br>- 该命令可以基于计费CC配置。<br>- 由于统一费率计费不涉及费率切换，因此该命令中的**计费属性CC值**不能取值为**0x0200**。**global**参数用于为全局用户配置费率切换。如果没有为用户指定费率切换点，则使用全局的费率切换点信息。SMF根据计费类型获取费率切换点信息。如果对应某一计费类型的费率切换点没有配置，将使用全局的费率切换点信息。 |
  | **ADD TARIFFGROUP** | 费率切换终止时间（ENDTIME） | 17:00 | 全网规划 | 配置费率切换点。<br>- 该命令可以基于计费CC配置。<br>- 由于统一费率计费不涉及费率切换，因此该命令中的**计费属性CC值**不能取值为**0x0200**。**global**参数用于为全局用户配置费率切换。如果没有为用户指定费率切换点，则使用全局的费率切换点信息。SMF根据计费类型获取费率切换点信息。如果对应某一计费类型的费率切换点没有配置，将使用全局的费率切换点信息。 |
- 任务示例脚本（该命令行）：
  `ADD TARIFFGROUP: TARIFFGRPNAME="tar_nb", GLOBALFLG=CHARGE_CHARACT, CCVALUE="0x0800", TARIFFTYPE=WORKDAY, STARTTIME=06&00, ENDTIME=17&00;`
  `ADD TARIFFGROUP: TARIFFGRPNAME="tar_nb", GLOBALFLG=CHARGE_CHARACT, CCVALUE="0x0800", TARIFFTYPE=WEEKEND, STARTTIME=06&00, ENDTIME=17&00;`
  `ADD TARIFFGROUP: TARIFFGRPNAME="tar_nb", GLOBALFLG=CHARGE_CHARACT, CCVALUE="0x0800", TARIFFTYPE=FESTIVAL, STARTTIME=06&00, ENDTIME=17&00;`
- 操作步骤上下文（±2 行原文）：
  L64:
    >       **ADD WEEKDAY**
    >     c. 配置节假日，工作日或周末的费率时间段。
    >       **ADD TARIFFGROUP**
    >     d. **可选** ：配置费率切换模式。
    >       **SET N40QUOTACTRL**
  L68:
    >       **SET N40QUOTACTRL**
    >       > **说明**
    >       > - 当“TCMODE”参数配置为“DEFAULT”时，表示费率切换发生的时间点按照**ADD TARIFFGROUP**命令配置的费率切换生效。
    >       > - 当“TCMODE”参数配置为“DAILY”时，表示在**ADD TARIFFGROUP**命令的费率切换配置基础上，每天00：00再强制进行费率切换，生效范围为所有用户。
    >       > - 当“TCMODE”参数配置为“MONTHLY”时，表示在**ADD TARIFFGROUP**命令的费率切换配置基础上，月初第一天00：00再强制进行费率切换，生效范围为所有用户。
  L69:
    >       > **说明**
    >       > - 当“TCMODE”参数配置为“DEFAULT”时，表示费率切换发生的时间点按照**ADD TARIFFGROUP**命令配置的费率切换生效。
    >       > - 当“TCMODE”参数配置为“DAILY”时，表示在**ADD TARIFFGROUP**命令的费率切换配置基础上，每天00：00再强制进行费率切换，生效范围为所有用户。
    >       > - 当“TCMODE”参数配置为“MONTHLY”时，表示在**ADD TARIFFGROUP**命令的费率切换配置基础上，月初第一天00：00再强制进行费率切换，生效范围为所有用户。
    > 2. 配置全局费率切换组。

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L45:
    > - [**ADD FESTIVAL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/节假日/增加计费节假日表（ADD FESTIVAL）_09896827.md)
    > - [**ADD WEEKDAY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/工作日/配置计费星期表（ADD WEEKDAY）_09896831.md)
    > - [**ADD TARIFFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/费率切换组/配置费率切换组（ADD TARIFFGROUP）_09896836.md)
    > - [**SET GLBTARIFFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/全局费率切换组/配置全局费率切换组（SET GLBTARIFFGROUP）_09896840.md)
    > - [**ADD IMSIMSISDNSEG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L45:
    > - [**ADD FESTIVAL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/节假日/增加计费节假日表（ADD FESTIVAL）_09896827.md)
    > - [**ADD WEEKDAY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/工作日/配置计费星期表（ADD WEEKDAY）_09896831.md)
    > - [**ADD TARIFFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/费率切换组/配置费率切换组（ADD TARIFFGROUP）_09896836.md)
    > - [**SET GLBTARIFFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/全局费率切换组/配置全局费率切换组（SET GLBTARIFFGROUP）_09896840.md)
    > - [**ADD IMSIMSISDNSEG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)

## ④ 自动比对
- 命令真相参数（8）：['CCMASK', 'CCPRIORITY', 'CCVALUE', 'ENDTIME', 'GLOBALFLG', 'STARTTIME', 'TARIFFGRPNAME', 'TARIFFTYPE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 9, '全网规划': 9}（多值→atom 应考虑 decision_driven）
