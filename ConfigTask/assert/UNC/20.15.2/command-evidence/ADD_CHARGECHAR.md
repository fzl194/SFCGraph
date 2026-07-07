# 命令证据包：ADD CHARGECHAR
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/增加对本地用户、漫游用户、拜访用户所采用的计费属性（ADD CHARGECHAR）_09896809.md`
> 用该命令的特性数：5

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

此命令用来添加对本地用户、漫游用户、拜访用户所采用的计费属性。

计费属性指对用户所采用的计费类型，不同计费类型可以有不同的话单生成方式。用户的计费属性可以遵从SGSN/SGW上的属性配置，也可以遵从UNC上的属性配置。本地用户和漫游用户统称本PLMN（Public Land Mobile Network，运营商移动网络标识）的归属用户。UNC支
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为1000。
- 0x0800表示普通计费（normal），基于传输的数据流量或时间长度来进行计费，不区分数据的业务种类。普通计费采用3GPP协议标准。
- 0x0400表示预付费（prepaid），用户在获取某种服务之前需要预先支付一定的费用，如果费用不足以支付某项服务的花销，该项服务将会被强制中止。
- 0x0200表示统一费率（flat-bil

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CCNAME | 计费属性名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～31。 |
| HOME | 本地用户计费属性 | local_planned | optional | 0x0800 | 字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| ROAM | 漫游用户计费属性 | local_planned | optional | 0x0800 | 字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| VISIT | 拜访用户计费属性 | local_planned | optional | 0x0800 | 字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| HOMESGSN | 本地用户使用Serving Node计费属性 | local_planned | optional | ENABLE | 枚举类型。 |
| ROAMSGSN | 漫游用户使用Serving Node计费属性 | local_planned | optional | ENABLE | 枚举类型。 |
| VISITSGSN | 拜访用户使用Serving Node计费属性 | local_planned | optional | ENABLE | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - **[ADD CHARGECHAR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/增加对本地用户、漫游用户、拜访用户所采用的计费属性（ADD CHARGECHAR）_09896809.md)**
    > - [**SET USRPROFCHARGE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
    > - [**SET APNCHARGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md)

**md：`WSFD-011201/配置离线计费参数（GGSN_SGW-C_PGW-C）_95923590.md`**
- 数据规划表（该命令的参数行）：
  | **ADD CHARGECHAR** | 计费属性名称（CCNAME） | testchgcha | 本端规划 | 增加计费属性 |
- 任务示例脚本（该命令行）：
  `ADD CHARGECHAR:CCNAME="testchgcha";`
- 操作步骤上下文（±2 行原文）：
  L107:
    > 4. 配置OFCTemplate模板绑定计费属性CC。
    >     a. 配置计费属性CC。如已配置CC，请跳过该步骤。
    >       **ADD CHARGECHAR**
    >     b. 配置计费属性CC绑定OFCTemplate模板。
    >       **ADD GLBOFCTEMPLATE**
  L164:
    > 4. 任务三：配置计费属性ChargeChar的离线计费参数。
    >   ```
    >   ADD CHARGECHAR:CCNAME="testchgcha";
    >   ```
    >   ```

**md：`WSFD-011201/配置离线计费费率切换（GGSN_SGW-C_PGW-C）_95923434.md`**
- 数据规划表（该命令的参数行）：
  | **ADD CHARGECHAR** | 计费属性名称（CCNAME） | testchgcha | 已配置数据中获取 | 该参数已在<br>[配置计费属性CC（GGSN/SGW-C/PGW-C）](配置计费属性CC（GGSN_SGW-C_PGW-C）_95923501.md)<br>中通过命令<br>**ADD CHARGECHAR**<br>配置，可以使用命令<br>**LST CHARGECHAR**<br>进行查询。 |
  | **ADD CHARGECHAR** | 本地用户计费属性（HOME） | 0x0800 | 已配置数据中获取 | 该参数已在<br>[配置计费属性CC（GGSN/SGW-C/PGW-C）](配置计费属性CC（GGSN_SGW-C_PGW-C）_95923501.md)<br>中通过命令<br>**ADD CHARGECHAR**<br>配置，可以使用命令<br>**LST CHARGECHAR**<br>进行查询。 |
  | **ADD CHARGECHAR** | 漫游用户计费属性（ROAM） | 0x0800 | 已配置数据中获取 | 该参数已在<br>[配置计费属性CC（GGSN/SGW-C/PGW-C）](配置计费属性CC（GGSN_SGW-C_PGW-C）_95923501.md)<br>中通过命令<br>**ADD CHARGECHAR**<br>配置，可以使用命令<br>**LST CHARGECHAR**<br>进行查询。 |
  | **ADD CHARGECHAR** | 拜访用户计费属性（VISIT） | 0x0800 | 已配置数据中获取 | 该参数已在<br>[配置计费属性CC（GGSN/SGW-C/PGW-C）](配置计费属性CC（GGSN_SGW-C_PGW-C）_95923501.md)<br>中通过命令<br>**ADD CHARGECHAR**<br>配置，可以使用命令<br>**LST CHARGECHAR**<br>进行查询。 |

**md：`WSFD-011201/配置计费属性CC（GGSN_SGW-C_PGW-C）_95923501.md`**
- 数据规划表（该命令的参数行）：
  | **ADD CHARGECHAR** | 计费属性名称（CCNAME） | testchgcha | 本端规划 | 配置CC实例。 |
  | **ADD CHARGECHAR** | 拜访用户计费属性（VISIT） | 0x0800 | 本端规划 | 配置CC实例。 |
  | **ADD CHARGECHAR** | 本地用户计费属性（HOME） | 0x0800 | 本端规划 | 配置CC实例。 |
  | **ADD CHARGECHAR** | 漫游用户计费属性（ROAM） | 0x0800 | 本端规划 | 配置CC实例。 |
  | **ADD CHARGECHAR** | 本地用户使用Serving Node计费属性（HOMESGSN） | ENABLE | 本端规划 | 配置CC实例。 |
  | **ADD CHARGECHAR** | 漫游用户使用Serving Node计费属性（ROAMSGSN） | ENABLE | 本端规划 | 配置CC实例。 |
  | **ADD CHARGECHAR** | 拜访用户使用Serving Node计费属性（VISITSGSN） | ENABLE | 本端规划 | 配置CC实例。 |
- 任务示例脚本（该命令行）：
  `ADD CHARGECHAR: CCNAME="testchgcha", HOME="0x0800", ROAM="0x0800", VISIT="0x0800", HOMESGSN=ENABLE, ROAMSGSN=ENABLE, VISITSGSN=ENABLE;`
  `ADD CHARGECHAR: CCNAME="testchgcha", HOME="0x0800", ROAM="0x0800", VISIT="0x0800", HOMESGSN=ENABLE, ROAMSGSN=ENABLE, VISITSGSN=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L12:
    > CC可以由RADIUS Server下发，可以在HLR/HSS上签约，也可以在UNC上本地配置，UNC支持基于UserProfile、APN、全局配置三种计费属性Charging Characteristics（CC）。其中，RADIUS Server下发CC优先级大于UNC本地配置，UNC上CC的优先级从高到低依次是：UserProflie下的配置 > APN下的配置 > 全局配置 > normal（缺省：普通计费）。如果高级别的参数没有配置，则依次向下使用低一级别的参数取值。 [图1](#ZH-CN_OPI_0295923501__fig172861639154319) 呈现了CC的选择逻辑图。
    > 
    > - 当左侧网元携带签约CC、并且本地基于UserProfile、APN配置CC场景下，本地、漫游、拜访用户选择CC由**ADD CHARGECHAR**命令的HOMESGSN、ROAMSGSN、VISITSGSN控制，当对应参数配置为ENABLE时，表示使用签约下发的CC，当配置为DISABLE时，表示使用本地配置的CC。
    > - 当左侧网元携带签约CC、并且本地基于全局配置CC场景下，本地、漫游、拜访用户选择CC由**SET GLBCHARGECHAR**命令的HOMESGSN、ROAMSGSN、VISITSGSN控制，当对应参数配置为ENABLE时，表示使用签约下发的CC，当配置为DISABLE时，表示使用本地全局配置的CC。
    >   > **说明**
  L67:
    > - 配置APN下的CC。
    >     1. 配置CC实例。
    >       **ADD CHARGECHAR**
    >     2. 配置APN。如已配置APN，请跳过该步骤。
    >       **ADD APN**
  L74:
    > - 配置UserProflie下的CC。
    >     1. 配置CC实例。
    >       **ADD CHARGECHAR**
    >     2. 配置UserProflie。如已配置UserProflie，请跳过该步骤。
    >       **ADD USERPROFILE**

**md：`WSFD-011201/调测费率切换功能（GGSN_SGW-C_PGW-C）_95923381.md`**
- 数据规划表（该命令的参数行）：
  | **ADD CHARGECHAR** | 计费属性名称（CCNAME） | testchgcha | 已配置数据中获取 | 该参数已在<br>[配置计费属性CC（GGSN/SGW-C/PGW-C）](../激活离线计费/配置计费属性CC（GGSN_SGW-C_PGW-C）_95923501.md)<br>中通过命令<br>**ADD CHARGECHAR**<br>配置，可以使用命令<br>**LST CHARGECHAR**<br>进行查询。 |
  | **ADD CHARGECHAR** | 本地用户计费属性（HOME） | 0x0800 | 已配置数据中获取 | 该参数已在<br>[配置计费属性CC（GGSN/SGW-C/PGW-C）](../激活离线计费/配置计费属性CC（GGSN_SGW-C_PGW-C）_95923501.md)<br>中通过命令<br>**ADD CHARGECHAR**<br>配置，可以使用命令<br>**LST CHARGECHAR**<br>进行查询。 |
  | **ADD CHARGECHAR** | 漫游用户计费属性（ROAM） | 0x0800 | 已配置数据中获取 | 该参数已在<br>[配置计费属性CC（GGSN/SGW-C/PGW-C）](../激活离线计费/配置计费属性CC（GGSN_SGW-C_PGW-C）_95923501.md)<br>中通过命令<br>**ADD CHARGECHAR**<br>配置，可以使用命令<br>**LST CHARGECHAR**<br>进行查询。 |
  | **ADD CHARGECHAR** | 拜访用户计费属性（VISIT） | 0x0800 | 已配置数据中获取 | 该参数已在<br>[配置计费属性CC（GGSN/SGW-C/PGW-C）](../激活离线计费/配置计费属性CC（GGSN_SGW-C_PGW-C）_95923501.md)<br>中通过命令<br>**ADD CHARGECHAR**<br>配置，可以使用命令<br>**LST CHARGECHAR**<br>进行查询。 |

### WSFD-011202

**md：`WSFD-011202/WSFD-011202 支持热计费功能（适用于GGSN、SGW-C、PGW-C）参考信息_28072079.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - **[增加对本地用户、漫游用户、拜访用户所采用的计费属性（ADD CHARGECHAR）](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/增加对本地用户、漫游用户、拜访用户所采用的计费属性（ADD CHARGECHAR）_09896809.md)**
    > - **[删除对本地用户、漫游用户、拜访用户所采用的计费属性（RMV CHARGECHAR）](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/删除对本地用户、漫游用户、拜访用户所采用的计费属性（RMV CHARGECHAR）_09896811.md)**
    > - **[修改对本地用户、漫游用户、拜访用户所采用的计费属性（MOD CHARGECHAR）](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/修改对本地用户、漫游用户、拜访用户所采用的计费属性（MOD CHARGECHAR）_09896810.md)**

**md：`WSFD-011202/激活支持热计费功能_28072077.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD CHARGECHAR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/增加对本地用户、漫游用户、拜访用户所采用的计费属性（ADD CHARGECHAR）_09896809.md)** | 计费属性名称（CCNAME） | HOTBILLING | 全网规划 | 配置计费属性名称。 |
  | **[ADD CHARGECHAR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/增加对本地用户、漫游用户、拜访用户所采用的计费属性（ADD CHARGECHAR）_09896809.md)** | 本地用户计费属性（HOME）<br>漫游用户计费属性（ROAM）<br>拜访用户计费属性（VISIT） | 0x100<br>0x100<br>0x100 | 全网规划 | 配置用户计费属性的计费类型为热计费 |
  | **[ADD CHARGECHAR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/增加对本地用户、漫游用户、拜访用户所采用的计费属性（ADD CHARGECHAR）_09896809.md)** | 本地用户使用Serving Node计费属性（HOMESGSN）<br>漫游用户使用Serving Node计费属性（ROAMSGSN）<br>拜访用户使用Serving Node计费属性（VISITSGSN） | DISABLE<br>DISABLE<br>DISABLE | 全网规划 | 用户的计费属性使用本地配置的属性。 |
- 任务示例脚本（该命令行）：
  `ADD CHARGECHAR: CCNAME="testchgcha", HOME="0x100", ROAM="0x100", VISIT="0x100", HOMESGSN=DISABLE, ROAMSGSN=DISABLE, VISITSGSN=DISABLE;`
- 操作步骤上下文（±2 行原文）：
  L61:
    > 
    > ```
    > ADD CHARGECHAR: CCNAME="testchgcha", HOME="0x100", ROAM="0x100", VISIT="0x100", HOMESGSN=DISABLE, ROAMSGSN=DISABLE, VISITSGSN=DISABLE;
    > ```
    > 

**md：`WSFD-011202/调测支持热计费功能_28072078.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD CHARGECHAR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/增加对本地用户、漫游用户、拜访用户所采用的计费属性（ADD CHARGECHAR）_09896809.md)** | 本地用户计费属性（HOME）<br>漫游用户计费属性（ROAM）<br>拜访用户计费属性（VISIT） | 0x100<br>0x100<br>0x100 | 已配置数据中获取 | 计费类型 |

### WSFD-011206

**md：`WSFD-011206/WSFD-011206 支持融合计费参考信息_74013176.md`**
- 操作步骤上下文（±2 行原文）：
  L13:
    > 
    > - [**SET N40APIVER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/N40 API版本/设置N40接口协议版本和需要使用的FeatureList（SET N40APIVER）_31773565.md)
    > - **[ADD CHARGECHAR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/增加对本地用户、漫游用户、拜访用户所采用的计费属性（ADD CHARGECHAR）_09896809.md)**
    > - [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
    > - [**SET APNCHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md)

**md：`WSFD-011206/配置计费属性CC_90776700.md`**
- 数据规划表（该命令的参数行）：
  | **ADD CHARGECHAR** | 计费属性名称（CCNAME） | testchgcha | 本端规划 | 配置CC实例。 |
  | **ADD CHARGECHAR** | 拜访用户计费属性（VISIT） | 0x0800 | 本端规划 | 本地、漫游、拜访用户的计费属性。 |
  | **ADD CHARGECHAR** | 本地用户计费属性（HOME） | 0x0800 | 本端规划 | 本地、漫游、拜访用户的计费属性。 |
  | **ADD CHARGECHAR** | 漫游用户计费属性（ROAM） | 0x0800 | 本端规划 | 本地、漫游、拜访用户的计费属性。 |
  | **ADD CHARGECHAR** | 本地用户使用Serving Node计费属性（HOMESGSN） | DISABLE | 本端规划 | - 当配置为ENABLE时，表示使用UDM下发的CC。<br>- 当配置为DISABLE时，表示使用本地配置的CC。 |
  | **ADD CHARGECHAR** | 漫游用户使用Serving Node计费属性（ROAMSGSN） | DISABLE | 本端规划 | - 当配置为ENABLE时，表示使用UDM下发的CC。<br>- 当配置为DISABLE时，表示使用本地配置的CC。 |
  | **ADD CHARGECHAR** | 拜访用户使用Serving Node计费属性（VISITSGSN） | DISABLE | 本端规划 | - 当配置为ENABLE时，表示使用UDM下发的CC。<br>- 当配置为DISABLE时，表示使用本地配置的CC。 |
- 任务示例脚本（该命令行）：
  `ADD CHARGECHAR: CCNAME="testchgcha", HOME="0x0800", ROAM="0x0800", VISIT="0x0800", HOMESGSN=DISABLE, ROAMSGSN=DISABLE, VISITSGSN=DISABLE;`
  `ADD CHARGECHAR: CCNAME="testchgcha", HOME="0x0800", ROAM="0x0800", VISIT="0x0800", HOMESGSN=DISABLE, ROAMSGSN=DISABLE, VISITSGSN=DISABLE;`
- 操作步骤上下文（±2 行原文）：
  L12:
    > Charging Characteristics（CC）是3GPP协议定义的一种用户签约付费属性，不属于计费功能。CC的取值有热计费(Hot Billing 0x0100)、统一费率（Flat Rate 0x0200）、预付费（Prepaid Service 0x0400）、普通计费(Normal Billing 0x0800)和自定义取值。CC可以由RADIUS Server下发，可以在UDM上签约，也可以在UNC上本地配置，UNC支持基于UserProfile、DNN、全局配置三种计费属性CC。其中，RADIUS Server下发CC优先级大于UNC本地配置，UNC上CC的优先级从高到低依次是：UserProflie下的配置 > DNN下的配置 > 全局配置 > normal（缺省：普通计费）。如果高级别的计费属性没有配置，则依次使用低一级别的计费属性。 [图1](#ZH-CN_OPI_0190776700__fig172861639154319) 呈现了CC的选择逻辑图。
    > 
    > - 当UDM下发签约CC、并且本地基于UserProfile、DNN配置CC场景下，由**ADD CHARGECHAR**命令的HOMESGSN、ROAMSGSN、VISITSGSN控制本地、漫游、拜访用户是否使用签约下发的计费属性CC。当对应参数配置为ENABLE时，表示使用UDM签约下发的CC；当配置为DISABLE时，表示使用本地配置的CC。从UDM获取签约CC时，SMF直接动态获取计费属性信息，与本地配置CC无关。
    > - 当UDM下发签约CC、并且本地基于全局配置CC场景下，由**SET GLBCHARGECHAR**命令的HOMESGSN、ROAMSGSN、VISITSGSN控制本地、漫游、拜访用户是否使用签约下发的计费属性CC。当对应参数配置为ENABLE时，表示使用UDM签约下发的CC；当配置为DISABLE时，表示使用本地全局配置的CC。从UDM获取签约CC时，SMF直接动态获取计费属性信息，与本地配置CC无关。
    > 
  L65:
    >     1. 进入 “MML命令行-UNC” 窗口。
    >     2. 配置CC实例。
    >       **ADD CHARGECHAR**
    >     3. 配置DNN。如已配置DNN，请跳过该步骤。
    >       **ADD APN**
  L73:
    >     1. 进入 “MML命令行-UNC” 窗口。
    >     2. 配置CC实例。
    >       **ADD CHARGECHAR**
    >     3. 配置UserProfile。如已配置UserProfile，请跳过该步骤。
    >       **ADD USERPROFILE**

**md：`WSFD-011206/配置费率切换_86411191.md`**
- 数据规划表（该命令的参数行）：
  | **ADD CHARGECHAR** | 计费属性名称（CCNAME） | testchgcha | 已配置数据中获取 | 已通过命令<br>**ADD CHARGECHAR**<br>配置，可以使用命令<br>**LST CHARGECHAR**<br>进行查询。 |
  | **ADD CHARGECHAR** | 本地用户计费属性（HOME） | 0x0800 | 已配置数据中获取 | 已通过命令<br>**ADD CHARGECHAR**<br>配置，可以使用命令<br>**LST CHARGECHAR**<br>进行查询。 |
  | **ADD CHARGECHAR** | 漫游用户计费属性（ROAM） | 0x0800 | 已配置数据中获取 | 已通过命令<br>**ADD CHARGECHAR**<br>配置，可以使用命令<br>**LST CHARGECHAR**<br>进行查询。 |
  | **ADD CHARGECHAR** | 拜访用户计费属性（VISIT） | 0x0800 | 已配置数据中获取 | 已通过命令<br>**ADD CHARGECHAR**<br>配置，可以使用命令<br>**LST CHARGECHAR**<br>进行查询。 |

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - **[ADD CHARGECHAR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/增加对本地用户、漫游用户、拜访用户所采用的计费属性（ADD CHARGECHAR）_09896809.md)**
    > - [**SET CHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/设置计费控制配置（SET CHARGECTRL）_09896792.md)
    > - [**SET APNCHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - **[ADD CHARGECHAR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/增加对本地用户、漫游用户、拜访用户所采用的计费属性（ADD CHARGECHAR）_09896809.md)**
    > - [**SET CHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/设置计费控制配置（SET CHARGECTRL）_09896792.md)
    > - [**SET APNCHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md)

**md：`WSFD-109001/配置普通在线计费实例_95923459.md`**
- 数据规划表（该命令的参数行）：
  | **ADD CHARGECHAR** | 计费属性名称（CCNAME） | testchgcha | 本端规划 | 计费属性。 |
  | **ADD CHARGECHAR** | 拜访用户计费属性（VISIT） | 0x0800 | 全网规划 | 计费属性。 |
  | **ADD CHARGECHAR** | 本地用户计费属性（HOME） | 0x0800 | 全网规划 | 计费属性。 |
  | **ADD CHARGECHAR** | 漫游用户计费属性（ROAM） | 0x0800 | 全网规划 | 计费属性。 |
  | **ADD CHARGECHAR** | 本地用户使用Serving Node计费属性（HOMESGSN） | ENABLE | 全网规划 | 计费属性。 |
  | **ADD CHARGECHAR** | 漫游用户使用Serving Node计费属性（ROAMSGSN） | ENABLE | 全网规划 | 计费属性。 |
  | **ADD CHARGECHAR** | 拜访用户使用Serving Node计费属性（VISITSGSN） | ENABLE | 全网规划 | 计费属性。 |
- 任务示例脚本（该命令行）：
  `ADD CHARGECHAR:CCNAME="testchgcha", HOME="0x0800", ROAM="0x0800", VISIT="0x0800", HOMESGSN=ENABLE, ROAMSGSN=ENABLE, VISITSGSN=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L82:
    > 
    > 1. 配置计费属性。
    >   **ADD CHARGECHAR**
    >   > **说明**
    >   > 如果该计费属性实例没有绑定APN实例或者UserProfile实例，则配置的计费属性不生效。
  L130:
    >   **SET APNCHARGECTRL**
    >   > **说明**
    >   > 针对同一个用户， **ADD CHARGECHAR** 和 **ADD CHARGEMETHOD** 配置的结果要保持一致，要么是 “ONLINE” ，要么是 “OFFLINE” ，或者两者同时使能，如果不一致将导致用户计费方式错误。
    > 
    > ## [任务示例](#ZH-CN_OPI_0295923459)
  L142:
    > 1. 配置计费属性。
    >   ```
    >   ADD CHARGECHAR:CCNAME="testchgcha", HOME="0x0800", ROAM="0x0800", VISIT="0x0800", HOMESGSN=ENABLE, ROAMSGSN=ENABLE, VISITSGSN=ENABLE;
    >   ```
    > 2. 配置用户的计费方式是在线计费。

**md：`WSFD-109001/配置计费属性CC（GGSN_SGW-C_PGW-C）_15408915.md`**
- 数据规划表（该命令的参数行）：
  | **ADD CHARGECHAR** | 计费属性名称（CCNAME） | testchgcha | 本端规划 | 配置CC实例。 |
  | **ADD CHARGECHAR** | 拜访用户计费属性（VISIT） | 0x0800 | 本端规划 | 配置CC实例。 |
  | **ADD CHARGECHAR** | 本地用户计费属性（HOME） | 0x0800 | 本端规划 | 配置CC实例。 |
  | **ADD CHARGECHAR** | 漫游用户计费属性（ROAM） | 0x0800 | 本端规划 | 配置CC实例。 |
  | **ADD CHARGECHAR** | 本地用户使用Serving Node计费属性（HOMESGSN） | ENABLE | 本端规划 | 配置CC实例。 |
  | **ADD CHARGECHAR** | 漫游用户使用Serving Node计费属性（ROAMSGSN） | ENABLE | 本端规划 | 配置CC实例。 |
  | **ADD CHARGECHAR** | 拜访用户使用Serving Node计费属性（VISITSGSN） | ENABLE | 本端规划 | 配置CC实例。 |
- 任务示例脚本（该命令行）：
  `ADD CHARGECHAR: CCNAME="testchgcha", HOME="0x0800", ROAM="0x0800", VISIT="0x0800", HOMESGSN=ENABLE, ROAMSGSN=ENABLE, VISITSGSN=ENABLE;`
  `ADD CHARGECHAR: CCNAME="testchgcha", HOME="0x0800", ROAM="0x0800", VISIT="0x0800", HOMESGSN=ENABLE, ROAMSGSN=ENABLE, VISITSGSN=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L12:
    > CC可以由RADIUS Server下发，可以在HLR/HSS上签约，也可以在UNC上本地配置，UNC支持基于UserProfile、APN、全局配置三种计费属性Charging Characteristics（CC）。其中，RADIUS Server下发CC优先级大于UNC本地配置，UNC上CC的优先级从高到低依次是：UserProflie下的配置 > APN下的配置 > 全局配置 > normal（缺省：普通计费）。如果高级别的参数没有配置，则依次向下使用低一级别的参数取值。 [图1](#ZH-CN_OPI_0315408915__zh-cn_opi_0295923501_fig172861639154319) 呈现了CC的选择逻辑图。
    > 
    > - 当左侧网元携带签约CC、并且本地基于UserProfile、APN配置CC场景下，本地、漫游、拜访用户选择CC由**ADD CHARGECHAR**命令的HOMESGSN、ROAMSGSN、VISITSGSN控制，当对应参数配置为ENABLE时，表示使用签约下发的CC，当配置为DISABLE时，表示使用本地配置的CC。
    > - 当左侧网元携带签约CC、并且本地基于全局配置CC场景下，本地、漫游、拜访用户选择CC由**SET GLBCHARGECHAR**命令的HOMESGSN、ROAMSGSN、VISITSGSN控制，当对应参数配置为ENABLE时，表示使用签约下发的CC，当配置为DISABLE时，表示使用本地全局配置的CC。
    >   > **说明**
  L67:
    > - 配置APN下的CC。
    >     1. 配置CC实例。
    >       **ADD CHARGECHAR**
    >     2. 配置APN。如已配置APN，请跳过该步骤。
    >       **ADD APN**
  L74:
    > - 配置UserProflie下的CC。
    >     1. 配置CC实例。
    >       **ADD CHARGECHAR**
    >     2. 配置UserProflie。如已配置UserProflie，请跳过该步骤。
    >       **ADD USERPROFILE**

## ④ 自动比对
- 命令真相参数（7）：['CCNAME', 'HOME', 'HOMESGSN', 'ROAM', 'ROAMSGSN', 'VISIT', 'VISITSGSN']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 23, '已配置数据中获取': 13, '全网规划': 9}（多值→atom 应考虑 decision_driven）
