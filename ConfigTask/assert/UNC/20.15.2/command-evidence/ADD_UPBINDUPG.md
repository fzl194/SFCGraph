# 命令证据包：ADD UPBINDUPG
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md`
> 用该命令的特性数：17

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

本命令用于将用户模板绑定到用户模板组下，可以配置用户模板优先级和选择用户模板条件，即IMSI/MSISDN号码段名称、IMEISV号码段名称、RAT、漫游属性、计费属性及位置组名称。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 一个“用户模板组”下面最多可以绑定500个UserProfile，优先级唯一，同时还可以给“用户模板组”绑定一个默认的UserProfile，即不配置任何优先级、号码段名称、RAT、“漫游属性”、“计费属性”及“位置组名称”。
- 需要预先配置ADD USRPROFGROUP和ADD USERPROFILE。
- 当UPBINDTYPE指定为SPECIFIC时，“I

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| USERPROFGNAME | 用户模板组名称 | global_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| UPBINDTYPE | 用户模板绑定类型 | global_planned | required | 无 | 枚举类型。 |
| PRIORITY | 优先级 | local_planned | conditional | 无 | 整数类型，取值范围为1～65534。取值范围为1到65534（65535用于用户绑定类型为默认的优先 |
| USERPROFILENAME | 用户模板名称 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| RAT | RAT | global_planned | conditional | 无 | 枚举类型。 |
| ROAMING | 漫游属性 | global_planned | conditional | 无 | 枚举类型。 |
| CCCONFIGMODE | 计费属性配置模式 | global_planned | conditional | 无 | 枚举类型。 |
| CHARGECHAR | 计费属性 | global_planned | conditional | 无 | 字符串类型，输入长度范围为1～6。十六进制，仅支持输入0x/0X、a-f/A-F、0-9，允许不输入 |
| CCMASK | 计费属性掩码 | global_planned | conditional | 0xFFFF | 字符串类型，输入长度范围为1～6。十六进制，仅支持输入0x/0X、a-f/A-F、0-9，允许不输入 |
| IMSIMSSEGNAME | IMSI/MSISDN号段名称 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| IMEISVSEGNAME | IMEISV号段名称 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| LOCGROUPNAME | 位置组名称 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| SEGGROUPNAME | IMSI/MSISDN/IMEISV 号段组名称 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| LOCALPCCSELECT | 本地PCC策略选择模式 | local_planned | optional | INHERIT | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-108002

**md：`WSFD-108002/WSFD-108002 基于预定义规则的分流策略控制参考信息_28860592.md`**
- 操作步骤上下文（±2 行原文）：
  L19:
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)
  L22:
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > 

**md：`WSFD-108002/激活基于预定义规则的分流策略控制_28860590.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | 用户模板组名称（USERPROFGNAME） | ulcl_test | 本端规划 | 配置基于DNN UL CL分流的用户模板组，并将DNN绑定至该模板组 |
  | [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | 用户模板绑定类型（UPBINDTYPE） | ULCL | 本端规划 | 配置基于DNN UL CL分流的用户模板组，并将DNN绑定至该模板组 |
  | [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | 用户模板名称（USERPROFILENAME） | testuserprofilename | 全网规划 | 配置基于DNN UL CL分流的用户模板组，并将DNN绑定至该模板组 |
- 任务示例脚本（该命令行）：
  `ADD UPBINDUPG:USERPROFGNAME="ulcl_test",UPBINDTYPE=ULCL,USERPROFILENAME="testuserprofilename";`
- 操作步骤上下文（±2 行原文）：
  L91:
    >       [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    >     c. 将上述用户模板绑定至用户模板组。
    >       [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    >     d. 将用户模板组绑定至指定APN。
    >       [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
  L133:
    > //配置用户模板组，并将ULCL属性的用户模板绑定至该模板组，再将模板组绑定至指定APN。
    > ADD USRPROFGROUP:USERPROFGNAME="ulcl_test";
    > ADD UPBINDUPG:USERPROFGNAME="ulcl_test",UPBINDTYPE=ULCL,USERPROFILENAME="testuserprofilename";
    > ADD APNUSRPROFG:APN="Huawei.com",USERPROFGNAME="ulcl_test";
    > //配置IPv6会话场景下的分流策略。

### WSFD-223001

**md：`WSFD-223001/WSFD-223001 基于位置信息的分流策略控制参考信息_47717539.md`**
- 操作步骤上下文（±2 行原文）：
  L18:
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD NGPRA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/网络开放管理/5G PRA管理/5G PRA标识管理/增加5G PRA（ADD NGPRA）_44006470.md)
    > - [**ADD NGPRAMEM**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/网络开放管理/5G PRA管理/5G PRA位置成员管理/增加PRA位置区成员（ADD NGPRAMEM）_44006471.md)

### WSFD-223003

**md：`WSFD-223003/WSFD-223003 基于漫游地动态签约的分流策略控制特性参考信息_52923849.md`**
- 操作步骤上下文（±2 行原文）：
  L27:
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**SET SMFFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话管理拓展功能/5GC会话管理拓展功能/设置SMF扩展功能（SET SMFFUNC）_09653731.md)

**md：`WSFD-223003/部署基于漫游地动态签约的分流策略控制（SMF）_82779459.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD UPBINDUPG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | 用户模板组名称（USERPROFGNAME） | ulcl_test | 本端规划 | 配置基于专网业务DNN UL CL分流的用户模板组，并将DNN绑定至该模板组 |
  | [**ADD UPBINDUPG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | 用户模板绑定类型（UPBINDTYPE） | ULCL | 本端规划 | 配置基于专网业务DNN UL CL分流的用户模板组，并将DNN绑定至该模板组 |
  | [**ADD UPBINDUPG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | 用户模板名称（USERPROFILENAME） | testuserprofilename | 全网规划 | 配置基于专网业务DNN UL CL分流的用户模板组，并将DNN绑定至该模板组 |
- 任务示例脚本（该命令行）：
  `ADD UPBINDUPG:USERPROFGNAME="ulcl_test",UPBINDTYPE=ULCL,USERPROFILENAME="testuserprofilename";`
- 操作步骤上下文（±2 行原文）：
  L67:
    >       [**ADD USRPROFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    >     c. 将上述用户模板绑定至用户模板组。
    >       [**ADD UPBINDUPG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    >     d. 将用户模板组绑定至专网DNN。
    >       [**ADD APNUSRPROFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
  L107:
    > //配置用户模板组，并将ULCL属性的用户模板绑定至该模板组，再将模板组绑定至指定APN。
    > ADD USRPROFGROUP:USERPROFGNAME="ulcl_test";
    > ADD UPBINDUPG:USERPROFGNAME="ulcl_test",UPBINDTYPE=ULCL,USERPROFILENAME="testuserprofilename";
    > ADD APNUSRPROFG:APN="dnn-ar",USERPROFGNAME="ulcl_test";
    > //配置IPv6会话场景下的分流策略。

### WSFD-223101

**md：`WSFD-223101/WSFD-223101 基于预定义规则的分流策略控制(4G)参考信息_11634944.md`**
- 操作步骤上下文（±2 行原文）：
  L19:
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)
  L22:
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > 

### WSFD-109202

**md：`WSFD-109202/WSFD-109202 会话类QOS保证参考信息_28258189.md`**
- 操作步骤上下文（±2 行原文）：
  L24:
    > - **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)**
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**SET QOSCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS控制功能/设置QoS控制配置（SET QOSCTRL）_09653269.md)

**md：`WSFD-109202/激活会话类QOS保证（适用于GGSN）_28258187.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | USERPROFGNAME（用户模板组名称） | usrg | 全网规划 | 将UserProfile绑定到用户模板组。 |
  | [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | UPBINDTYPE | DEFAULT | 全网规划 | 将UserProfile绑定到用户模板组。 |
  | [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | USERPROFILENAME（用户模板名称） | profile1 | 本端规划 | 将UserProfile绑定到用户模板组。 |
- 任务示例脚本（该命令行）：
  `ADD UPBINDUPG:USERPROFGNAME="usrg",UPBINDTYPE=DEFAULT,USERPROFILENAME="profile1";`
- 操作步骤上下文（±2 行原文）：
  L94:
    >       [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    >     - 将UserProfile绑定到用户模板组UserProfileGroup。
    >       [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    >     - 配置APN实例。
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
  L169:
    >   //将UserProfile绑定到UserProfileGroup。
    >   ```
    >   ADD UPBINDUPG:USERPROFGNAME="usrg",UPBINDTYPE=DEFAULT,USERPROFILENAME="profile1";
    >   ```
    >   //进入指定APN实例。

**md：`WSFD-109202/激活会话类QOS保证（适用于SGW-C_PGW-C）_28344569.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | USERPROFGNAME (用户模板组名称) | usrg | 全网规划 | 将UserProfile绑定到用户模板组 |
  | [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | UPBINDTYPE | DEFAULT | 全网规划 | 将UserProfile绑定到用户模板组 |
  | [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | USERPROFILENAME（用户模板名称） | profile1 | 本端规划 | 将UserProfile绑定到用户模板组 |
- 任务示例脚本（该命令行）：
  `ADD UPBINDUPG:USERPROFGNAME="usrg",UPBINDTYPE=DEFAULT,USERPROFILENAME="profile1";`
- 操作步骤上下文（±2 行原文）：
  L115:
    >       [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    >     - 将UserProfile绑定到用户模板组UserProfileGroup。
    >       [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    >     - 配置APN实例。
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
  L206:
    >   //将UserProfile绑定到UserProfileGroup。
    >   ```
    >   ADD UPBINDUPG:USERPROFGNAME="usrg",UPBINDTYPE=DEFAULT,USERPROFILENAME="profile1";
    >   ```
    >   //进入指定APN实例。

### WSFD-109203

**md：`WSFD-109203/WSFD-109203 本地QOS控制参考信息_28258574.md`**
- 操作步骤上下文（±2 行原文）：
  L22:
    > - **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)**
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L25:
    > - [**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD USRPROFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD PCCPOLICYGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)

**md：`WSFD-109101/配置本地PCC功能_30805097.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD UPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | 用户模板组名称（USERPROFGNAME） | upg_test | 全网规划 | 将UserProfile绑定到UserProfile Group。 |
  | [**ADD UPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | 用户模板绑定类型（UPBINDTYPE） | DEFAULT | 全网规划 | 将UserProfile绑定到UserProfile Group。 |
  | [**ADD UPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | 用户模板名称（USERPROFILENAME） | up_test | 本端规划 | 将UserProfile绑定到UserProfile Group。 |
- 任务示例脚本（该命令行）：
  `ADD UPBINDUPG:USERPROFGNAME="upg_test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up_test";`
- 操作步骤上下文（±2 行原文）：
  L103:
    >       [**ADD USRPROFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    >     e. 将UserProfile绑定到UserProfile Group。
    >       [**ADD UPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    >       > **说明**
    >       > UserProfile Group中可以绑定多个UserProfile，本地PCC用户激活后，UNC根据 [**ADD UPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) 中的匹配条件最终只能为本地PCC用户安装一个UserProfile，如果要为本地PCC用户安装多个UserProfile，用以区分不同的业务套餐，需要执行 [步骤 6.f](#ZH-CN_OPI_0230805097__stepe) 。
  L105:
    >       [**ADD UPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    >       > **说明**
    >       > UserProfile Group中可以绑定多个UserProfile，本地PCC用户激活后，UNC根据 [**ADD UPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) 中的匹配条件最终只能为本地PCC用户安装一个UserProfile，如果要为本地PCC用户安装多个UserProfile，用以区分不同的业务套餐，需要执行 [步骤 6.f](#ZH-CN_OPI_0230805097__stepe) 。
    >     f. **可选：**将UserProfile绑定到UserProfile Group，为本地PCC用户安装多个UserProfile。
    >       [**ADD PCCPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/用户PCC模板绑定/增加用户模板组和PccProfile的绑定关系（ADD PCCPBINDUPG）_09897037.md)
  L110:
    >       > **说明**
    >       > - 重复执行本步骤可以绑定多个UserProfile，实现为本地PCC用户安装多个UserProfile。
    >       > - 用户激活后优先安装[**ADD PCCPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/用户PCC模板绑定/增加用户模板组和PccProfile的绑定关系（ADD PCCPBINDUPG）_09897037.md)命令绑定的UserProfile，如果[**ADD PCCPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/用户PCC模板绑定/增加用户模板组和PccProfile的绑定关系（ADD PCCPBINDUPG）_09897037.md)命令未绑定任何UserProfile，则使用[**ADD UPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)中绑定的UserProfile。
    >       > - [**ADD PCCPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/用户PCC模板绑定/增加用户模板组和PccProfile的绑定关系（ADD PCCPBINDUPG）_09897037.md)命令配置后，common policy仍使用[**ADD UPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)中配置的匹配条件的UserProfile中的策略。
    >     g. 将UserProfile Group绑定到APN。

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD UPBINDUPG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | 用户模板组名称（USERPROFGNAME） | upg_test | 全网规划 | 将UserProfile绑定到UserProfile Group。 |
  | [**ADD UPBINDUPG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | 用户模板绑定类型（UPBINDTYPE） | DEFAULT | 全网规划 | 将UserProfile绑定到UserProfile Group。 |
  | [**ADD UPBINDUPG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | 用户模板名称（USERPROFILENAME） | up_test | 本端规划 | 将UserProfile绑定到UserProfile Group。 |
- 任务示例脚本（该命令行）：
  `ADD UPBINDUPG:USERPROFGNAME="upg_test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up_test";`
- 操作步骤上下文（±2 行原文）：
  L187:
    >             [**ADD USRPROFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    >           b. 将UserProfile绑定到UserProfile Group。
    >             [**ADD UPBINDUPG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    >           c. 将UserProfile Group绑定到DNN。
    >             [**ADD APNUSRPROFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
  L262:
    > ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";
    > ADD USRPROFGROUP:USERPROFGNAME="upg_test";
    > ADD UPBINDUPG:USERPROFGNAME="upg_test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up_test";
    > ADD APNUSRPROFG:APN="huawei.com",USERPROFGNAME="upg_test";
    > ```

### WSFD-109107

**md：`WSFD-109107/WSFD-109107 业务触发的QoS保证参考信息_85397060.md`**
- 操作步骤上下文（±2 行原文）：
  L19:
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)

**md：`WSFD-109107/激活业务触发的QoS保证_85397058.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | 用户模板组名称（USERPROFGNAME） | upg_test | 全网规划 | 将UserProfile绑定到UserProfile Group。 |
  | [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | 用户模板绑定类型（UPBINDTYPE） | DEFAULT | 全网规划 | 将UserProfile绑定到UserProfile Group。 |
  | [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | 用户模板名称（USERPROFILENAME） | up_test | 本端规划 | 将UserProfile绑定到UserProfile Group。 |
- 任务示例脚本（该命令行）：
  `ADD UPBINDUPG:USERPROFGNAME="upg_test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up_test";`
- 操作步骤上下文（±2 行原文）：
  L91:
    >       [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    >     b. 将UserProfile绑定到UserProfile Group。
    >       [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    >     c. 将UserProfile Group绑定到DNN。
    >       [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
  L160:
    > ```
    > ADD USRPROFGROUP:USERPROFGNAME="upg_test";
    > ADD UPBINDUPG:USERPROFGNAME="upg_test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up_test";
    > ADD APNUSRPROFG:APN="huawei.com",USERPROFGNAME="upg_test";
    > ```

### WSFD-211001

**md：`WSFD-211001/WSFD-211001 基于初始接入位置的策略控制参考信息_27915140.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - [**ADD USRLOCATIONGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/用户位置组/增加用户位置组（ADD USRLOCATIONGRP）_09897148.md)
    > - [**MOD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/修改用户模板组和用户模板的绑定关系（MOD UPBINDUPG）_09897230.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > 

**md：`WSFD-211001/激活基于初始接入位置的策略控制_27915138.md`**
- 操作步骤上下文（±2 行原文）：
  L64:
    >       [**MOD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/修改用户模板组和用户模板的绑定关系（MOD UPBINDUPG）_09897230.md)
    >     - 用户模板和用户模板组未绑定时：
    >       [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > 6. 将用户模板组和APN/DNN绑定。
    >   [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)

### WSFD-211005

**md：`WSFD-211005/WSFD-211005 基于业务感知的带宽控制参考信息_79619228.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > 

**md：`WSFD-211005/激活基于业务感知的带宽控制_79619226.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | 用户模板组名称（USERPROFGNAME） | upg_test | 全网规划 | 将UserProfile绑定到UserProfile Group。 |
  | [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | 用户模板绑定类型（UPBINDTYPE） | DEFAULT | 全网规划 | 将UserProfile绑定到UserProfile Group。 |
  | [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | 用户模板名称（USERPROFILENAME） | up_test | 本端规划 | 将UserProfile绑定到UserProfile Group。 |
- 任务示例脚本（该命令行）：
  `ADD UPBINDUPG:USERPROFGNAME="upg_test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up_test";`
- 操作步骤上下文（±2 行原文）：
  L57:
    >       [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    >     b. 将UserProfile绑定到UserProfile Group。如已配置，请跳过本步骤。
    >       [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    >     c. UserProfile Group绑定到DNN。如已配置，请跳过本步骤。
    >       [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
  L81:
    > ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";
    > ADD USRPROFGROUP:USERPROFGNAME="upg_test";
    > ADD UPBINDUPG:USERPROFGNAME="upg_test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up_test";
    > ADD APNUSRPROFG:APN="huawei.com",USERPROFGNAME="upg_test";
    > ```

### WSFD-011306

**md：`WSFD-011306/WSFD-011306 Radius功能参考信息_15542176.md`**
- 操作步骤上下文（±2 行原文）：
  L48:
    > - **[ADD RULEBINDING](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)**
    > - **[ADD USRPROFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)**
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - **[TST AAA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/RADIUS维护/服务器检测/测试AAA服务器（TST AAA）_09896762.md)**

**md：`WSFD-011306/配置业务触发RADIUS功能_33000859.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD UPBINDUPG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | 用户模板组名称（USERPROFGNAME） | upg_test | 已配置数据中获取 | 已经通过<br>**[ADD USRPROFGROUP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)**<br>命令配置完成，可以使用<br>**[LST USRPROFGROUP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/查询用户模板组（LST USRPROFGROUP）_09897222.md)**<br>查询。 |
  | [**ADD UPBINDUPG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | 用户模板绑定类型（UPBINDTYPE） | DEFAULT | 本端规划 | - |
  | [**ADD UPBINDUPG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | 用户模板名称（USERPROFILENAME） | up_test | 已配置数据中获取 | 已通过<br>[**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)<br>配置，可以使用<br>**[**LST USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/查询用户模板（LST USERPROFILE）_09897214.md)**<br>命令进行查询。<br>。 |
- 任务示例脚本（该命令行）：
  `ADD UPBINDUPG: USERPROFGNAME="upg_test", UPBINDTYPE=DEFAULT, USERPROFILENAME="up_test";`
- 操作步骤上下文（±2 行原文）：
  L68:
    >       **[ADD USRPROFGROUP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)**
    >     d. 将UserProfile绑定到UsrProfGroup。
    >       [**ADD UPBINDUPG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    >     e. 将UsrProfGroup绑定到指定APN。
    >       [**ADD APNUSRPROFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
  L105:
    > ADD RULEBINDING: USERPROFILENAME="up_test", RULENAME="rule_test1";
    > ADD USRPROFGROUP: USERPROFGNAME="upg_test";
    > ADD UPBINDUPG: USERPROFGNAME="upg_test", UPBINDTYPE=DEFAULT, USERPROFILENAME="up_test";
    > ADD APNUSRPROFG: APN="apn-test", USERPROFGNAME="upg_test";
    > ```

### WSFD-011201

**md：`WSFD-011201/配置离线计费参数（GGSN_SGW-C_PGW-C）_95923590.md`**
- 操作步骤上下文（±2 行原文）：
  L97:
    >       **ADD USRPROFGROUP**
    >     d. 将UserProfile绑定到UserProfileGroup。
    >       **ADD UPBINDUPG**
    >     e. 将UserProfileGroup绑定到APN实例下。
    >       **ADD APNUSRPROFG**

**md：`WSFD-011201/配置离线计费的费率标识（GGSN_SGW-C_PGW-C）_98555879.md`**
- 数据规划表（该命令的参数行）：
  | **ADD UPBINDUPG** | 用户模板组名称（USERPROFGNAME） | upg_test | 已配置数据中获取 | 将UserProfile绑定到UserProfile组上。 |
  | **ADD UPBINDUPG** | 用户模板绑定类型（UPBINDTYPE） | DEFAULT | 本端规划 | 将UserProfile绑定到UserProfile组上。 |
  | **ADD UPBINDUPG** | 用户模板名称（USERPROFILENAME） | up_test | 已配置数据中获取 | 将UserProfile绑定到UserProfile组上。 |
- 任务示例脚本（该命令行）：
  `ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";`
  `ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";`
- 操作步骤上下文（±2 行原文）：
  L79:
    >           a. 配置UserProfile组，将UserProfile绑定到UserProfile组上。
    >             **ADD USRPROFGROUP**
    >             **ADD UPBINDUPG**
    >           b. 配置APN，将UserProfile组绑定到指定APN实例上。
    >             **ADD APN**
  L108:
    >           a. 配置UserProfile组，将UserProfile绑定到UserProfile组上。
    >             **ADD USRPROFGROUP**
    >             **ADD UPBINDUPG**
    >           b. 配置APN，将UserProfile组绑定到指定APN实例上。
    >             **ADD APN**
  L142:
    >   SET URRGRPBINDING:USERPROFILENAME="up-test",DFTURRGRPNAME="urrgroup1";
    >   ADD USRPROFGROUP:USERPROFGNAME="upg-test";
    >   ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";
    >   ADD APN:APN="apn-test";
    >   ADD APNUSRPROFG:APN="apn-test",USERPROFGNAME="upg-test";

### WSFD-011206

**md：`WSFD-011206/配置融合计费模板_93400212.md`**
- 数据规划表（该命令的参数行）：
  | **ADD UPBINDUPG** | 用户模板组名称（USERPROFGNAME） | upg_test | 已配置数据中获取 | 将UserProfile绑定到DNN实例。<br>基于UserProfile粒度需要规划。 |
  | **ADD UPBINDUPG** | 用户模板绑定类型（UPBINDTYPE） | DEFAULT | 固定取值 | 将UserProfile绑定到DNN实例。<br>基于UserProfile粒度需要规划。 |
  | **ADD UPBINDUPG** | 用户模板名称（USERPROFILENAME） | up_test | 已配置数据中获取 | 将UserProfile绑定到DNN实例。<br>基于UserProfile粒度需要规划。 |
- 任务示例脚本（该命令行）：
  `ADD UPBINDUPG: USERPROFGNAME="upg_test", UPBINDTYPE=DEFAULT, USERPROFILENAME="userprofile001";`
- 操作步骤上下文（±2 行原文）：
  L97:
    >           a. 配置UserProfile组，将UserProfile绑定到UserProfile组。
    >             **ADD USRPROFGROUP**
    >             **ADD UPBINDUPG**
    >           b. 配置DNN实例，将UserProifle组绑定到DNN实例。
    >             **ADD APN**
  L101:
    >             **ADD APN**
    >             **ADD APNUSRPROFG**
    >             每个DNN实例只能绑定一个UserProfile组。如UserProfile组和DNN实例已配置且已绑定，本步骤只需执行 **ADD UPBINDUPG** 命令，将UserProfile绑定到UserProfile组即可。
    > 
    > ## [任务示例](#ZH-CN_OPI_0193400212)
  L148:
    > ```
    > ADD USRPROFGROUP: USERPROFGNAME="upg_test";
    > ADD UPBINDUPG: USERPROFGNAME="upg_test", UPBINDTYPE=DEFAULT, USERPROFILENAME="userprofile001";
    > ```
    > 

**md：`WSFD-011206/配置融合计费费率标识_93360308.md`**
- 数据规划表（该命令的参数行）：
  | **ADD UPBINDUPG** | 用户模板组名称（USERPROFGNAME） | upg_test | 已配置数据中获取 | 使用<br>**ADD USRPROFGROUP**<br>命令定义的<br>“USERPROFGNAME”<br>。 |
  | **ADD UPBINDUPG** | 用户模板绑定类型（UPBINDTYPE） | SPECIFIC | 固定取值 | - |
  | **ADD UPBINDUPG** | 优先级（PRIORITY） | 10 | 本端规划 | 取值越小，优先级越高。 |
  | **ADD UPBINDUPG** | 用户模板名称（USERPROFILENAME） | userprofile001<br>userprofile002 | 已配置数据中获取 | 使用<br>**ADD USERPROFILE**<br>命令定义的<br>“USERPROFILENAME”<br>。 |
- 任务示例脚本（该命令行）：
  `ADD UPBINDUPG: USERPROFGNAME="upg_test", UPBINDTYPE=SPECIFIC, PRIORITY=10, USERPROFILENAME="userprofile001";`
  `ADD UPBINDUPG: USERPROFGNAME="upg_test", UPBINDTYPE=SPECIFIC, PRIORITY=20, USERPROFILENAME="userprofile002";`
- 操作步骤上下文（±2 行原文）：
  L107:
    >           a. 配置UserProfile组，将UserProfile绑定到UserProfile组。
    >             **ADD USRPROFGROUP**
    >             **ADD UPBINDUPG**
    >           b. 配置DNN实例，将UserProifle组绑定到DNN实例。
    >             **ADD APN**
  L111:
    >             **ADD APN**
    >             **ADD APNUSRPROFG**
    >             每个DNN实例只能绑定一个UserProfile组。如UserProfile组和DNN实例已配置且已绑定，本步骤只需执行 **ADD UPBINDUPG** 命令，将UserProfile绑定到UserProfile组即可。
    >     5. **可选：** 配置在线RG配额耗尽后的默认动作。
    >       **ADD QUOTAEXHAUSTACT**
  L203:
    > ```
    > ADD USRPROFGROUP: USERPROFGNAME="upg_test";
    > ADD UPBINDUPG: USERPROFGNAME="upg_test", UPBINDTYPE=SPECIFIC, PRIORITY=10, USERPROFILENAME="userprofile001";
    > ADD UPBINDUPG: USERPROFGNAME="upg_test", UPBINDTYPE=SPECIFIC, PRIORITY=20, USERPROFILENAME="userprofile002";
    > ```

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    > - [**SET URRGRPBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/设置用户模板的计费属性绑定关系（SET URRGRPBINDING）_09897209.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    > - [**SET URRGRPBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/设置用户模板的计费属性绑定关系（SET URRGRPBINDING）_09897209.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)

**md：`WSFD-109001/配置在线计费模板_95923574.md`**
- 数据规划表（该命令的参数行）：
  | **ADD UPBINDUPG** | 用户模板组名称（USERPROFGNAME） | upg-test | 已配置数据中获取 | 用户模板绑定到用户模板组。 |
  | **ADD UPBINDUPG** | 用户模板绑定类型（UPBINDTYPE） | DEFAULT | 本端规划 | 用户模板绑定到用户模板组。 |
  | **ADD UPBINDUPG** | 用户模板名称（USERPROFILENAME） | up-test | 已配置数据中获取 | 用户模板绑定到用户模板组。 |
- 任务示例脚本（该命令行）：
  `ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";`
- 操作步骤上下文（±2 行原文）：
  L91:
    >       **ADD USRPROFGROUP**
    >     d. 将UserProfile绑定到UserProfileGroup。
    >       **ADD UPBINDUPG**
    >     e. 将UserProfileGroup绑定到APN实例下。
    >       **ADD APNUSRPROFG**
  L158:
    > 
    > ```
    > ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";
    > ```
    > 

**md：`WSFD-109001/配置在线计费的费率标识_95923388.md`**
- 数据规划表（该命令的参数行）：
  | **ADD UPBINDUPG** | 用户模板组名称（USERPROFGNAME） | upg_test | 已配置数据中获取 | 将UserProfile绑定到UserProfile组上。 |
  | **ADD UPBINDUPG** | 用户模板绑定类型（UPBINDTYPE） | DEFAULT | 本端规划 | 将UserProfile绑定到UserProfile组上。 |
  | **ADD UPBINDUPG** | 用户模板名称（USERPROFILENAME） | up_test | 已配置数据中获取 | 将UserProfile绑定到UserProfile组上。 |
- 任务示例脚本（该命令行）：
  `ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";`
  `ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";`
- 操作步骤上下文（±2 行原文）：
  L83:
    >           a. 配置UserProfile组，将UserProfile绑定到UserProfile组上。
    >             **ADD USRPROFGROUP**
    >             **ADD UPBINDUPG**
    >           b. 配置APN，将UserProfile组绑定到指定APN实例上。
    >             **ADD APN**
  L112:
    >           a. 配置UserProfile组，将UserProfile绑定到UserProfile组上。
    >             **ADD USRPROFGROUP**
    >             **ADD UPBINDUPG**
    >           b. 配置APN，将UserProfile组绑定到指定APN实例上。
    >             **ADD APN**
  L146:
    >   SET URRGRPBINDING:USERPROFILENAME="up-test",DFTURRGRPNAME="urrgroup001";
    >   ADD USRPROFGROUP:USERPROFGNAME="upg-test";
    >   ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";
    >   ADD APN:APN="apn-test";
    >   ADD APNUSRPROFG:APN="apn-test",USERPROFGNAME="upg-test";

**md：`WSFD-109001/配置CCR触发场景_95923545.md`**
- 任务示例脚本（该命令行）：
  `ADD UPBINDUPG:USERPROFGNAME="upg_test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up_test";`
- 操作步骤上下文（±2 行原文）：
  L154:
    > 
    > ```
    > ADD UPBINDUPG:USERPROFGNAME="upg_test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up_test";
    > ```
    > 

### WSFD-109007

**md：`WSFD-109007/WSFD-109007 支持事件计费参考信息_74112323.md`**
- 操作步骤上下文（±2 行原文）：
  L23:
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > 

**md：`WSFD-109007/配置事件计费功能_74112321.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | USERPROFGNAME（用户模板组名称） | upg_test | 全网规划 | 将UserProfile绑定到UserProfile组上。 |
  | [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | UPBINDTYPE（用户模板绑定类型） | DEFAULT | 全网规划 | 将UserProfile绑定到UserProfile组上。 |
  | [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md) | USERPROFILENAME（用户模板名称） | up_test | 本端规划 | 将UserProfile绑定到UserProfile组上。 |
- 任务示例脚本（该命令行）：
  `ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";`
- 操作步骤上下文（±2 行原文）：
  L97:
    >     a. 配置UserProfile组，将UserProfile绑定到UserProfile组上。
    >       [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    >       [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    >     b. 配置DNN，将UserProfile组绑定到指定DNN实例上。
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
  L160:
    > ADD RULEBINDING:USERPROFILENAME="up-test",RULENAME="rule-test";
    > ADD USRPROFGROUP:USERPROFGNAME="upg-test";
    > ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";
    > ADD APN:APN="apn-test";
    > ADD APNUSRPROFG:APN="apn-test",USERPROFGNAME="upg-test";

### WSFD-201207

**md：`WSFD-201207/WSFD-201207 语音PCF_PCRF故障Bypass参考信息_85304300.md`**
- 操作步骤上下文（±2 行原文）：
  L130:
    > **[LST APNUSRPROFG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/查询APN用户模板组绑定关系（LST APNUSRPROFG）_09897227.md)**
    > 
    > **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)**
    > 
    > **[MOD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/修改用户模板组和用户模板的绑定关系（MOD UPBINDUPG）_09897230.md)**

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（Gx接口）_60552093.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)** | 用户模板组名称（USERPROFGNAME） | upg_ims | 全网规划 | （可选）将用户模板绑定到用户模板组中。 |
  | **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)** | 用户模板绑定类型（UPBINDTYPE） | SPECIFIC | 全网规划 | （可选）将用户模板绑定到用户模板组中。 |
  | **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)** | 优先级（PRIORITY） | 15 | 本端规划 | （可选）将用户模板绑定到用户模板组中。 |
  | **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)** | 用户模板名称（USERPROFILENAME） | up_ims | 本端规划 | （可选）将用户模板绑定到用户模板组中。 |
  | **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)** | 用户模板组名称（USERPROFGNAME） | upg_ims | 全网规划 | （可选）将用户模板绑定到用户模板组中。 |
  | **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)** | 用户模板绑定类型（UPBINDTYPE） | SPECIFIC | 全网规划 | （可选）将用户模板绑定到用户模板组中。 |
  | **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)** | 优先级（PRIORITY） | 15 | 本端规划 | （可选）将用户模板绑定到用户模板组中。 |
  | **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)** | 用户模板名称（USERPROFILENAME） | up_ims | 本端规划 | （可选）将用户模板绑定到用户模板组中。 |
- 任务示例脚本（该命令行）：
  `ADD UPBINDUPG:USERPROFGNAME="upg_ims", UPBINDTYPE=SPECIFIC, PRIORITY=15, USERPROFILENAME="up_ims";`
- 操作步骤上下文（±2 行原文）：
  L214:
    >       > **说明**
    >       > 如果已配置了APN ims使用的用户模板与模板组的绑定关系，则跳过本步骤。
    >       **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)**
    >     i. **可选：**为APN绑定用户模板组。
    >       > **说明**
  L245:
    >       > **说明**
    >       > 如果已配置了APN ims使用的用户模板与模板组的绑定关系，则跳过本步骤。
    >       **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)**
    >     j. **可选：**为APN绑定用户模板组。
    >       > **说明**
  L341:
    > 
    >       ```
    >       ADD UPBINDUPG:USERPROFGNAME="upg_ims", UPBINDTYPE=SPECIFIC, PRIORITY=15, USERPROFILENAME="up_ims";
    >       ```
    >       //为APN绑定用户模板组。

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（N7接口）_32852169.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)** | 用户模板组名称（USERPROFGNAME） | upg_ims | 全网规划 | （可选）将用户模板绑定到用户模板组中。 |
  | **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)** | 用户模板绑定类型（UPBINDTYPE） | SPECIFIC | 全网规划 | （可选）将用户模板绑定到用户模板组中。 |
  | **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)** | 优先级（PRIORITY） | 15 | 本端规划 | （可选）将用户模板绑定到用户模板组中。 |
  | **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)** | 用户模板名称（USERPROFILENAME） | up_ims | 本端规划 | （可选）将用户模板绑定到用户模板组中。 |
  | **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)** | 用户模板组名称（USERPROFGNAME） | upg_ims | 全网规划 | （可选）将用户模板绑定到用户模板组中。 |
  | **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)** | 用户模板绑定类型（UPBINDTYPE） | SPECIFIC | 全网规划 | （可选）将用户模板绑定到用户模板组中。 |
  | **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)** | 优先级（PRIORITY） | 15 | 本端规划 | （可选）将用户模板绑定到用户模板组中。 |
  | **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)** | 用户模板名称（USERPROFILENAME） | up_ims | 本端规划 | （可选）将用户模板绑定到用户模板组中。 |
- 任务示例脚本（该命令行）：
  `ADD UPBINDUPG:USERPROFGNAME="upg_ims", UPBINDTYPE=SPECIFIC, PRIORITY=15, USERPROFILENAME="up_ims";`
- 操作步骤上下文（±2 行原文）：
  L233:
    >       > **说明**
    >       > 如果已配置了APN ims使用的用户模板与模板组的绑定关系，则跳过本步骤。
    >       **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)**
    >     i. **可选：**为APN绑定用户模板组。
    >       > **说明**
  L264:
    >       > **说明**
    >       > 如果已配置了APN ims使用的用户模板与模板组的绑定关系，则跳过本步骤。
    >       **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)**
    >     j. **可选：**为APN绑定用户模板组。
    >       > **说明**
  L369:
    > 
    >       ```
    >       ADD UPBINDUPG:USERPROFGNAME="upg_ims", UPBINDTYPE=SPECIFIC, PRIORITY=15, USERPROFILENAME="up_ims";
    >       ```
    >       //为APN绑定用户模板组。

## ④ 自动比对
- 命令真相参数（14）：['CCCONFIGMODE', 'CCMASK', 'CHARGECHAR', 'IMEISVSEGNAME', 'IMSIMSSEGNAME', 'LOCALPCCSELECT', 'LOCGROUPNAME', 'PRIORITY', 'RAT', 'ROAMING', 'SEGGROUPNAME', 'UPBINDTYPE', 'USERPROFGNAME', 'USERPROFILENAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 24, '全网规划': 24, '已配置数据中获取': 12, '固定取值': 2}（多值→atom 应考虑 decision_driven）
