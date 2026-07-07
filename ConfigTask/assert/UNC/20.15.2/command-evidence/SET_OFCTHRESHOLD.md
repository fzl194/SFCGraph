# 命令证据包：SET OFCTHRESHOLD
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/设置离线计费阈值（SET OFCTHRESHOLD）_09896910.md`
> 用该命令的特性数：4

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

该命令用来配置控制话单生成条件中的计费阈值，包括时间阈值、流量阈值、计费条件改变次数、话单最多携带的容器数、MME/SGSN/SGW/ePDG地址改变次数等。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为100。
- 如果GPRS/UMTS接入的离线计费模板和PGW离线计费模板中的时间、流量、最小流量阈值不同，当发生2/3G与4G的切换时，切换后新建话单受切换后RAT对应的模板阈值控制。
- 如果阈值配置过小（时间阈值小于10分钟、流量阈值小于10MB）会导致话单产生过多而引起性能下降。
- 如果配置的流量阈值超过0xC0000000（3G）时，请

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| OFCTEMPLATENAME | 离线计费模板名 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格。 |
| THRESHINHERIT | 继承上一级配置 | local_planned | optional | 无 | 枚举类型。 |
| TIMETHRESHOLD | 时长阈值（分） | local_planned | conditional | 无 | 整数类型，取值范围为0～1440，单位是分钟。 |
| VOLUMETHRESHOLD | 流量阈值（千字节） | local_planned | conditional | 无 | 整数类型，取值范围为0，20～9000000000，单位是千字节。 |
| MINVOLTHRESHOLD | 最小流量阈值（千字节） | local_planned | conditional | 无 | 整数类型，取值范围为0～65535，单位是千字节。 |
| CONDITIONCHANGE | 计费条件改变阈值 | local_planned | conditional | 无 | 整数类型，取值范围为1～10。 |
| SERVINGNODECHNG | Serving Node改变次数阈值 | local_planned | conditional | 无 | 整数类型，取值范围为0～5。 |
| MAXSVCCONTAINER | 最大携带的业务容器数量 | local_planned | conditional | 无 | 整数类型，取值范围为1～40。 |
| TIMETHRESHCCFH | 在线计费转离线计费后的时长阈值（分钟） | local_planned | conditional | 无 | 整数类型，取值范围为0～1440，4294967295，单位是分钟。 |
| VOLTHRESHCCFH | 在线计费转离线计费后的流量阈值（千字节） | local_planned | conditional | 无 | 整数类型，取值范围为0，20～9000000000，9000000001，单位是千字节。 |
| SECRUTHRESHOLD | RAN-SecondaryRAT-Usage-Report生成话单的阈值 | local_planned | conditional | 无 | 整数类型，取值范围为1～10。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011511

**md：`WSFD-011511/WSFD-011511 NSA用户数据话单生成和上报参考信息_28784144.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - **[**RMV CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/删除话单字段模板（RMV CDRFIELDTEMP）_09896892.md)**
    > - **[**LST CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/查询话单字段模板（LST CDRFIELDTEMP）_09896893.md)**
    > - **[**SET OFCTHRESHOLD**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/设置离线计费阈值（SET OFCTHRESHOLD）_09896910.md)**
    > - **[**SET OFCCDRPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)**
    > - **[**LST OFCCDRPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/显示离线计费话单参数（LST OFCCDRPARA）_09896906.md)**

**md：`WSFD-011511/激活NSA用户数据话单生成和上报_28784142.md`**
- 数据规划表（该命令的参数行）：
  | [**SET OFCTHRESHOLD**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/设置离线计费阈值（SET OFCTHRESHOLD）_09896910.md) | 离线计费模板名（OFCTEMPLATENAME） | offlinecharge-test | 本端规划 | 配置离线计费模板名<br>说明：可使用<br>**[**LST OFCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/显示离线计费模板（LST OFCTEMPLATE）_09896914.md)**<br>查询已配置的离线计费模板名 |
  | [**SET OFCTHRESHOLD**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/设置离线计费阈值（SET OFCTHRESHOLD）_09896910.md) | 继承上一级配置（THRESHINHERIT） | NON_INHERIT | 本端规划 | 配置为NON_INHERIT |
  | [**SET OFCTHRESHOLD**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/设置离线计费阈值（SET OFCTHRESHOLD）_09896910.md) | RAN-SecondaryRAT-Usage-Report生成话单的阈值（SECRUTHRESHOLD） | 3 | 本端规划 | 配置RAN-SecondaryRAT-Usage-Report触发生成话单的阈值 |
- 任务示例脚本（该命令行）：
  `SET OFCTHRESHOLD:OFCTEMPLATENAME="offlinecharge-test",THRESHINHERIT=NON_INHERIT,SECRUTHRESHOLD=3;`
- 操作步骤上下文（±2 行原文）：
  L43:
    >   > “话单字段模板名”参数在 [激活离线计费](../../计费管理功能/WSFD-011201 支持离线计费/激活离线计费_25768943.md) 已经配置，可使用 [**LST CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/查询话单字段模板（LST CDRFIELDTEMP）_09896893.md) 查询，此处使用 [**MOD CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/修改话单字段模板（MOD CDRFIELDTEMP）_09896891.md) 命令增加“RAN-SecondaryRAT-Usage-Report”参数。
    > 3. 配置话单最多携带的RAN-SecondaryRAT-Usage-Report个数。
    >   [**SET OFCTHRESHOLD**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/设置离线计费阈值（SET OFCTHRESHOLD）_09896910.md)
    > 4. （可选配置）配置SGW-CDR和PGW-CDR话单中携带扩展Qos参数。
    >   [**SET OFCCDRPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)
  L64:
    > 
    > ```
    > SET OFCTHRESHOLD:OFCTEMPLATENAME="offlinecharge-test",THRESHINHERIT=NON_INHERIT,SECRUTHRESHOLD=3;
    > ```
    > 

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L22:
    > - [**SET SGWCHGMETH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/计费属性控制/设置SGW Charge Method（SET SGWCHGMETH）_09896985.md)
    > - [**ADD OFCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/增加离线计费模板（ADD OFCTEMPLATE）_09896908.md)
    > - [**SET OFCTHRESHOLD**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/设置离线计费阈值（SET OFCTHRESHOLD）_09896910.md)
    > - [**SET CDRTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/配置离线计费话单产生开关（SET CDRTRIGGER）_09896911.md)
    > - [**SET CONTAINERTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/配置离线计费容器产生开关（SET CONTAINERTRIGGER）_09896912.md)

**md：`WSFD-011201/配置离线计费参数（GGSN_SGW-C_PGW-C）_95923590.md`**
- 数据规划表（该命令的参数行）：
  | **SET OFCTHRESHOLD** | 离线计费模板名（OFCTEMPLATENAME） | offlinecharge-test | 已配置数据中获取 | 配置控制话单生成条件中的计费阈值 |
  | **SET OFCTHRESHOLD** | 继承上一级配置（THRESHINHERIT） | NON_INHERIT | 本端规划 | 配置控制话单生成条件中的计费阈值 |
  | **SET OFCTHRESHOLD** | 计费条件改变阈值（CONDITIONCHANGE） | 3 | 本端规划 | 配置控制话单生成条件中的计费阈值 |
  | **SET OFCTHRESHOLD** | 流量阈值（千字节）（VOLUMETHRESHOLD） | 20 | 本端规划 | 配置控制话单生成条件中的计费阈值 |
  | **SET OFCTHRESHOLD** | 时长阈值（分）（TIMETHRESHOLD） | 30 | 本端规划 | 配置控制话单生成条件中的计费阈值 |
  | **SET OFCTHRESHOLD** | Serving Node改变次数阈值（SERVINGNODECHNG） | 3 | 本端规划 | 配置控制话单生成条件中的计费阈值 |
- 任务示例脚本（该命令行）：
  `SET OFCTHRESHOLD: OFCTEMPLATENAME="offlinecharge-test",THRESHINHERIT=NON_INHERIT,TIMETHRESHOLD=30,VOLUMETHRESHOLD=20,CONDITIONCHANGE=3,SERVINGNODECHNG=5;`
- 操作步骤上下文（±2 行原文）：
  L84:
    >       **ADD OFCTEMPLATE**
    >     b. 配置阈值信息。
    >       **SET OFCTHRESHOLD**
    >     c. 配置话单产生条件。
    >       **SET CDRTRIGGER**
  L140:
    >   ```
    >   ```
    >   SET OFCTHRESHOLD: OFCTEMPLATENAME="offlinecharge-test",THRESHINHERIT=NON_INHERIT,TIMETHRESHOLD=30,VOLUMETHRESHOLD=20,CONDITIONCHANGE=3,SERVINGNODECHNG=5;
    >   ```
    >   ```

**md：`WSFD-011201/调测时间阈值功能_95923374.md`**
- 操作步骤上下文（±2 行原文）：
  L46:
    > 
    > 1. 进入 “MML命令行-UNC” 窗口。 设置时间阈值是5分钟，流量阈值不生效。
    >   **SET OFCTHRESHOLD**
    >   > **说明**
    >   > 离线计费默认使能时长计费和流量计费，同时设置了时长阈值和流量阈值，当其中一个阈值先达到，则按此阈值生成话单，此后新产生的话单两种阈值重置，不进行累计。

**md：`WSFD-011201/调测流量阈值功能_95923507.md`**
- 操作步骤上下文（±2 行原文）：
  L46:
    > 
    > 1. 进入 “MML命令行-UNC” 窗口。 设置流量阈值是20KByte，时间阈值不生效。
    >   **SET OFCTHRESHOLD**
    >   > **说明**
    >   > 离线计费默认使能时长计费和流量计费，同时设置了时长阈值和流量阈值，当其中一个阈值先达到，则按此阈值生成话单，此后新产生的话单两种阈值重置，不进行累计。

**md：`WSFD-011201/调测费率切换功能（GGSN_SGW-C_PGW-C）_95923381.md`**
- 操作步骤上下文（±2 行原文）：
  L65:
    > 
    > 1. 进入 “MML命令行-UNC” 窗口。 设置合适的话单时长阈值，本调测设置话单的时长阈值是15分钟。
    >   **SET OFCTHRESHOLD**
    > 2. 在配置的费率切换点前激活用户，该用户计费属性是normal， 测试终端 使用“apn-test”APN接入网络，访问业务。本调测任务是在05:40激活用户。
    >     - 如果测试终端成功接入网络，请执行[步骤 3](#ZH-CN_OPI_0295923381__step30-1)。

### WSFD-011202

**md：`WSFD-011202/WSFD-011202 支持热计费功能（适用于GGSN、SGW-C、PGW-C）参考信息_28072079.md`**
- 操作步骤上下文（±2 行原文）：
  L18:
    > - **[设置计费控制配置（SET CHARGECTRL）](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/设置计费控制配置（SET CHARGECTRL）_09896792.md)**
    > - **[查询计费控制配置（LST CHARGECTRL）](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/查询计费控制配置（LST CHARGECTRL）_09896793.md)**
    > - **[设置离线计费阈值（SET OFCTHRESHOLD）](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/设置离线计费阈值（SET OFCTHRESHOLD）_09896910.md)**
    > 
    > #### [告警](#ZH-CN_TOPIC_0228072079)

**md：`WSFD-011202/激活支持热计费功能_28072077.md`**
- 数据规划表（该命令的参数行）：
  | **[SET OFCTHRESHOLD](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/设置离线计费阈值（SET OFCTHRESHOLD）_09896910.md)** | 计费条件改变阈值（CONDITIONCHANGE） | 3 | 本端规划 | 计费参数可基于指定APN实例、指定计费属性和通用计费进行配置，这些参数可选配置，如果不配置，有默认值。具体的参数解释、缺省值、取值范围及使用指南请参见命令帮助。 |
  | **[SET OFCTHRESHOLD](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/设置离线计费阈值（SET OFCTHRESHOLD）_09896910.md)** | 流量阈值(VOLUMETHRESHOLD) | 1000 | 本端规划 | 计费参数可基于指定APN实例、指定计费属性和通用计费进行配置，这些参数可选配置，如果不配置，有默认值。具体的参数解释、缺省值、取值范围及使用指南请参见命令帮助。 |
  | **[SET OFCTHRESHOLD](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/设置离线计费阈值（SET OFCTHRESHOLD）_09896910.md)** | 时长阈值(TIMETHRESHOLD) | 30 | 本端规划 | 计费参数可基于指定APN实例、指定计费属性和通用计费进行配置，这些参数可选配置，如果不配置，有默认值。具体的参数解释、缺省值、取值范围及使用指南请参见命令帮助。 |
  | **[SET OFCTHRESHOLD](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/设置离线计费阈值（SET OFCTHRESHOLD）_09896910.md)** | Serving Node改变次数阈值（SERVINGNODECHNG） | 3 | 本端规划 | 计费参数可基于指定APN实例、指定计费属性和通用计费进行配置，这些参数可选配置，如果不配置，有默认值。具体的参数解释、缺省值、取值范围及使用指南请参见命令帮助。 |
- 任务示例脚本（该命令行）：
  `SET OFCTHRESHOLD:OFCTEMPLATENAME="offlinecharg-test",THRESHINHERIT=NON_INHERIT,CONDITIONCHANGE=3,VOLUMETHRESHOLD=1000,TIMETHRESHOLD=30,SERVINGNODECHNG=3;`
- 操作步骤上下文（±2 行原文）：
  L71:
    > 
    > ```
    > SET OFCTHRESHOLD:OFCTEMPLATENAME="offlinecharg-test",THRESHINHERIT=NON_INHERIT,CONDITIONCHANGE=3,VOLUMETHRESHOLD=1000,TIMETHRESHOLD=30,SERVINGNODECHNG=3;
    > ```
    > 

**md：`WSFD-011202/调测支持热计费功能_28072078.md`**
- 数据规划表（该命令的参数行）：
  | **[SET OFCTHRESHOLD](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/设置离线计费阈值（SET OFCTHRESHOLD）_09896910.md)** | 流量阈值(VOLUMETHRESHOLD) | 1000 | 已配置数据中获取 | 话单产生阈值 |
  | **[SET OFCTHRESHOLD](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/设置离线计费阈值（SET OFCTHRESHOLD）_09896910.md)** | 时长阈值(TIMETHRESHOLD) | 30 | 已配置数据中获取 | 话单产生阈值 |

### WSFD-109001

**md：`WSFD-109001/配置DCC处理动作_95923447.md`**
- 操作步骤上下文（±2 行原文）：
  L80:
    >       > - 当Tx定时器超时后的处理方式为“CONTINUE”时，允许用户保持业务的时长，超出该时长则去激活用户。当配置为0分钟表示允许用户永久保持在线进行业务。
    >     8. **可选：**配置在线计费用户转为离线计费用户后，是否对该用户执行不同的时长、流量阈值。
    >       **SET OFCTHRESHOLD**
    >       > **说明**
    >       > 本命令中 “TIMETHRESHCCFH” 、 “VOLTHRESHCCFH” 参数配置的时长、流量阈值只针对已转离线计费的在线计费用户生效。若参数未配置，则默认为使用原有的离线计费阈值。

## ④ 自动比对
- 命令真相参数（11）：['CONDITIONCHANGE', 'MAXSVCCONTAINER', 'MINVOLTHRESHOLD', 'OFCTEMPLATENAME', 'SECRUTHRESHOLD', 'SERVINGNODECHNG', 'THRESHINHERIT', 'TIMETHRESHCCFH', 'TIMETHRESHOLD', 'VOLTHRESHCCFH', 'VOLUMETHRESHOLD']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 12, '已配置数据中获取': 3}（多值→atom 应考虑 decision_driven）
