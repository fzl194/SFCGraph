# 命令证据包：ADD USERPROFILE
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md`
> 用该命令的特性数：17

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于增加用户模板。用户模板可用于设置免费业务是否进行在线、离线计费和融合计费功能。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 当UPSPECTYPE参数不指定或者指定为DEFAULT时，该命令最大记录数为5000；当UPSPECTYPE参数指定为SPECIFICATION_LIMITED时，该命令最大记录数为100000。当配置记录数大于规格的98%时，会上报“ALM-135602215 配置数量超阈值”告警。当配置记录数小于等于配置规格95%时，恢复“ALM-135602215 配置数量

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| USERPROFILENAME | 用户模板名称 | global_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| UPTYPE | 用户模板类型 | global_planned | required | PCC | 枚举类型。 |
| FREESERONLCHG | 免费业务在线计费标识 | local_planned | optional | ENABLE | 枚举类型。 |
| FREESEROFFCHG | 免费业务离线计费标识 | local_planned | optional | ENABLE | 枚举类型。 |
| FREESERCVGCHG | 免费业务融合计费标识 | local_planned | optional | ENABLE | 枚举类型。 |
| PROFILERANGE | 模板生效范围 | global_planned | conditional | ALL | 枚举类型。 |
| UPSPECTYPE | 用户模板规格类型 | global_planned | optional | DEFAULT | 枚举类型。 |
| QOSANASW | 质差分析开关 | global_planned | optional | DISABLE | 枚举类型。 |
| FREEONLFLAGSW | 免费在线业务携带在线相关标识开关 | local_planned | conditional | INHERIT | 枚举类型。 |
| RELAYSW | 媒体中继开关 | local_planned | optional | DISABLE | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-108002

**md：`WSFD-108002/WSFD-108002 基于预定义规则的分流策略控制参考信息_28860592.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - [**ADD ULCLPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/ULCL属性/增加ULCL属性（ADD ULCLPROP）_16935565.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)

**md：`WSFD-108002/激活基于预定义规则的分流策略控制_28860590.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | 用户模板名称（USERPROFILENAME） | testuserprofilename | 全网规划 | 配置UL CL属性的User Profile |
  | [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | 用户模板类型（UPTYPE） | ULCL | 本端规划 | 配置UL CL属性的User Profile |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE:USERPROFILENAME="testuserprofilename", UPTYPE=ULCL;`
  `ADD USERPROFILE:USERPROFILENAME="testuserprofilename", UPTYPE=ULCL;`
  `ADD USERPROFILE:USERPROFILENAME="testuserprofilename", UPTYPE=ULCL;`
- 操作步骤上下文（±2 行原文）：
  L82:
    >       [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    >     d. 配置ULCL属性的用户模板。
    >       [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    >     e. 将上述rule绑定至用户模板。
    >       [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
  L129:
    > ADD RULE:RULENAME="testrule",POLICYTYPE=ULCL, POLICYNAME="testulclpropname", FLOWFILTERNAME="ulcl"; 
    > //配置ULCL属性的用户模板，并将ULCL分流策略rule绑定至该模板。
    > ADD USERPROFILE:USERPROFILENAME="testuserprofilename", UPTYPE=ULCL; 
    > ADD RULEBINDING: USERPROFILENAME="testuserprofilename",RULENAME="testrule",POLICYTYPE=ULCL;
    > //配置用户模板组，并将ULCL属性的用户模板绑定至该模板组，再将模板组绑定至指定APN。
  L155:
    > ADD RULE:RULENAME="testrule",POLICYTYPE=ULCL, POLICYNAME="testulclpropname", FLOWFILTERNAME="ulcl"; 
    > //配置ULCL属性的用户模板，并将ULCL分流策略rule绑定至该模板。
    > ADD USERPROFILE:USERPROFILENAME="testuserprofilename", UPTYPE=ULCL; 
    > ADD RULEBINDING: USERPROFILENAME="testuserprofilename",RULENAME="testrule",POLICYTYPE=ULCL;
    > //配置IPv6会话场景下的分流策略。

### WSFD-223001

**md：`WSFD-223001/WSFD-223001 基于位置信息的分流策略控制参考信息_47717539.md`**
- 操作步骤上下文（±2 行原文）：
  L15:
    > - [**ADD ULCLPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/ULCL属性/增加ULCL属性（ADD ULCLPROP）_16935565.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)

**md：`WSFD-223001/部署基于位置信息的分流策略控制（SMF）_53995959.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | 用户模板名称（USERPROFILENAME） | testuserprofilename | 全网规划 | 配置UL CL属性的User Profile |
  | [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | 用户模板类型（UPTYPE） | ULCL | 本端规划 | 配置UL CL属性的User Profile |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE:USERPROFILENAME="testuserprofilename", UPTYPE=ULCL;`
- 操作步骤上下文（±2 行原文）：
  L55:
    > ADD RULE:RULENAME="testrule",POLICYTYPE=ULCL, POLICYNAME="testulclpropname", FLOWFILTERNAME="ulcl"; 
    > //配置ULCL属性的用户模板，并将ULCL分流策略rule绑定至该模板。
    > ADD USERPROFILE:USERPROFILENAME="testuserprofilename", UPTYPE=ULCL; 
    > ADD RULEBINDING: USERPROFILENAME="testuserprofilename",RULENAME="testrule";
    > //配置IPv6会话场景下的分流策略。

### WSFD-223003

**md：`WSFD-223003/WSFD-223003 基于漫游地动态签约的分流策略控制特性参考信息_52923849.md`**
- 操作步骤上下文（±2 行原文）：
  L23:
    > - [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)

**md：`WSFD-223003/部署基于漫游地动态签约的分流策略控制（SMF）_82779459.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | 用户模板名称（USERPROFILENAME） | testuserprofilename | 全网规划 | 配置UL CL属性的User Profile |
  | [**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | 用户模板类型（UPTYPE） | ULCL | 本端规划 | 配置UL CL属性的User Profile |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE:USERPROFILENAME="testuserprofilename", UPTYPE=ULCL;`
- 操作步骤上下文（±2 行原文）：
  L58:
    >       [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    >     d. 配置ULCL属性的用户模板。
    >       [**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    >     e. 将上述rule绑定至用户模板。
    >       [**ADD RULEBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
  L103:
    > ADD RULE:RULENAME="testrule",POLICYTYPE=ULCL, POLICYNAME="testulclpropname", FLOWFILTERNAME="ulcl"; 
    > //配置ULCL属性的用户模板，并将ULCL分流策略rule绑定至该模板。
    > ADD USERPROFILE:USERPROFILENAME="testuserprofilename", UPTYPE=ULCL; 
    > ADD RULEBINDING: USERPROFILENAME="testuserprofilename",RULENAME="testrule";
    > //配置用户模板组，并将ULCL属性的用户模板绑定至该模板组，再将模板组绑定至指定APN。

### WSFD-223101

**md：`WSFD-223101/WSFD-223101 基于预定义规则的分流策略控制(4G)参考信息_11634944.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - [**ADD ULCLPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/ULCL属性/增加ULCL属性（ADD ULCLPROP）_16935565.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)

**md：`WSFD-223101/部署基于预定义规则的分流策略控制(4G)（SMF）_11155006.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | 用户模板名称（USERPROFILENAME） | testuserprofilename | 全网规划 | 配置UL CL属性的User Profile |
  | [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | 用户模板类型（UPTYPE） | ULCL | 本端规划 | 配置UL CL属性的User Profile |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE:USERPROFILENAME="testuserprofilename", UPTYPE=ULCL;`
- 操作步骤上下文（±2 行原文）：
  L62:
    >       [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    >     d. 配置ULCL属性的用户模板。
    >       [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    >     e. 将上述rule绑定至用户模板。
    >       [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
  L112:
    > 
    > ```
    > ADD USERPROFILE:USERPROFILENAME="testuserprofilename", UPTYPE=ULCL; 
    > ADD RULEBINDING: USERPROFILENAME="testuserprofilename",RULENAME="testrule",POLICYTYPE=ULCL;
    > ```

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L23:
    > - [**ADD PCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)
    > - [**SET APNPCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    > - [**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD USRPROFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)

**md：`WSFD-109101/配置动态PCC功能_30805098.md`**
- 操作步骤上下文（±2 行原文）：
  L140:
    > 11. PCRF下发预定义规则组时，需要在GGSN/PGW-C上配置预定义规则组对应的本地业务策略组合。
    >     a. 配置UserProfile。
    >       [**ADD USERPROFILE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    >     b. **可选：**配置UserProfile和DNAI关联。可选配置，将UserProfile下发给指定DNAI的辅锚点PGW-U时需要配置。
    >       [**ADD USRPROBINDDNAI**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板DNAI绑定/增加用户模板关联的DNAI （ADD USRPROBINDDNAI）_27051919.md)

**md：`WSFD-109101/配置本地PCC功能_30805097.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD USERPROFILE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | 用户模板名称（USERPROFILENAME） | up_test | 全网规划 | 配置GGSN/PGW-C上的UserProfile，将本地rule绑定到UserProfile上。 |
  | [**ADD USERPROFILE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | 用户模板类型（UPTYPE） | PCC | 固定取值 | 配置GGSN/PGW-C上的UserProfile，将本地rule绑定到UserProfile上。 |
  | [**ADD USERPROFILE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | 模板生效范围（PROFILERANGE） | ALL | 全网规划 | PGW-C支持将UserProfile下发给主锚点PGW-U+辅锚点PGW-U、主锚点PGW-U或辅锚点PGW-U。<br>此处以Userprofile同时下发给主锚点PGW-U和辅锚点PGW-U为例。<br>Userprofile只下发给主锚点PGW-U时，需设置为“CENTRAL”；Userprofile只下发给辅锚点PGW-U时，需设置为“LOCAL”。 |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC,PROFILERANGE=ALL;`
- 操作步骤上下文（±2 行原文）：
  L95:
    > 6. 配置业务策略组合。
    >     a. 配置UserProfile。
    >       [**ADD USERPROFILE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    >     b. **可选：**将UserProfile下发给指定DNAI的辅锚点PGW-U时，配置UserProfile和DNAI关联。
    >       [**ADD USRPROBINDDNAI**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板DNAI绑定/增加用户模板关联的DNAI （ADD USRPROBINDDNAI）_27051919.md)
  L152:
    > 5. 配置业务策略组合。如配置的Userprofile仅下发给辅锚点PGW-U，则需要将“PROFILERANGE”设置为“LOCAL”；仅下发给主锚点PGW-U则设置为“CENTRAL”。
    >   ```
    >   ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC,PROFILERANGE=ALL;
    >   ```
    >   ```

**md：`WSFD-109101/WSFD-109101 PCC基本功能（5G）参考信息_72466541.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - [**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > - [**ADD PCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)
    > - [**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD USRPROFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**SET APNPCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | 用户模板名称（USERPROFILENAME） | up_test | 全网规划 | 配置SMF上的UserProfile。 |
  | [**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | 用户模板类型（UPTYPE） | PCC | 固定取值 | 配置SMF上的UserProfile。 |
  | [**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | 模板生效范围（PROFILERANGE） | ALL | 全网规划 | SMF支持将UserProfile下发给主锚点UPF+辅锚点UPF、主锚点UPF或辅锚点UPF。<br>此处以Userprofile同时下发给主锚点UPF和辅锚点UPF为例。<br>Userprofile只下发给主锚点UPF时，需设置为“CENTRAL”；Userprofile只下发给辅锚点UPF时，需设置为“LOCAL”。 |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC,PROFILERANGE=ALL;`
- 操作步骤上下文（±2 行原文）：
  L178:
    >     14. **可选：**配置SMF上的UserProfile，将本地rule绑定到UserProfile上。用于动态PCC时PCF下发预定义规则组，或本地PCC时的静态规则组。
    >           a. 配置UserProfile。
    >             [**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    >           b. 将UserProfile下发给指定DNAI的辅锚点UPF时，配置UserProfile和DNAI关联。
    >             [**ADD USRPROBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板DNAI绑定/增加用户模板关联的DNAI （ADD USRPROBINDDNAI）_27051919.md)
  L259:
    > 
    > ```
    > ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC,PROFILERANGE=ALL;
    > ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";
    > ADD USRPROFGROUP:USERPROFGNAME="upg_test";

### WSFD-109102

**md：`WSFD-109102/WSFD-109102 ADC基本功能参考信息_92582138.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)

**md：`WSFD-109102/激活ADC基本功能_92582136.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | 用户模板名称（USERPROFILENAME） | up_test | 全网规划 | 配置GGSN-C/PGW-C/SMF上的UserProfile。 |
  | [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | 用户模板类型（UPTYPE） | PCC | 固定取值 | 配置GGSN-C/PGW-C/SMF上的UserProfile。 |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC;`
- 操作步骤上下文（±2 行原文）：
  L57:
    >     b. **可选：**配置SMF上的UserProfile，将本地rule绑定到UserProfile上。
    >           1. 配置UserProfile。
    >             [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    >           2. 将rule绑定到UserProfile。
    >             [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
  L93:
    > ```
    > ADD RULE:RULENAME="rule_test",POLICYTYPE=ADC;
    > ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC;
    > ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";
    > ```

### WSFD-109103

**md：`WSFD-109103/WSFD-109103 IPv6 SA参考信息_78881328.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - [**MOD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_09897174.md)/[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > 

### WSFD-109107

**md：`WSFD-109107/WSFD-109107 业务触发的QoS保证参考信息_85397060.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)

**md：`WSFD-109107/激活业务触发的QoS保证_85397058.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | 用户模板名称（USERPROFILENAME） | up_test | 全网规划 | 配置SMF上的UserProfile。 |
  | [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | 用户模板类型（UPTYPE） | PCC | 固定取值 | 配置SMF上的UserProfile。 |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC;`
- 操作步骤上下文（±2 行原文）：
  L84:
    > 6. 配置SMF上的UserProfile，将本地rule绑定到UserProfile上。用于动态PCC时PCF下发预定义规则组，或本地PCC时的静态规则组。
    >     a. 配置UserProfile。
    >       [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    >     b. 将rule绑定到UserProfile。
    >       [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
  L152:
    > 
    > ```
    > ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC;
    > ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test",POLICYTYPE=QOS;
    > ```

### WSFD-211005

**md：`WSFD-211005/WSFD-211005 基于业务感知的带宽控制参考信息_79619228.md`**
- 操作步骤上下文（±2 行原文）：
  L13:
    > 
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)

**md：`WSFD-211005/激活基于业务感知的带宽控制_79619226.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | 用户模板名称（USERPROFILENAME） | up_test | 全网规划 | 配置UserProfile。 |
  | [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | 用户模板类型（UPTYPE） | PCC | 固定取值 | 配置UserProfile。 |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC;`
- 操作步骤上下文（±2 行原文）：
  L50:
    > 2. 配置SMF上的UserProfile，将本地rule绑定到UserProfile上。用于动态PCC时PCF下发预定义规则组，或本地PCC时的静态规则组。
    >     a. 配置UserProfile。如已配置，请跳过本步骤。
    >       [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    >     b. 将rule绑定到UserProfile。
    >       [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
  L78:
    > 
    > ```
    > ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC;
    > ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";
    > ADD USRPROFGROUP:USERPROFGNAME="upg_test";

### WSFD-211009

**md：`WSFD-211009/WSFD-211009 基于业务累计流量的策略控制参考信息_27915158.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - [**MOD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_09897174.md)/[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > 

**md：`WSFD-211009/激活基于业务累计流量的策略控制_27915156.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | 用户模板名称(USERPROFILENAME) | up_test | 与对端协商 | 与UPF上配置的用户模板名称保持一致。 |
  | [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | 用户模板类型(UPTYPE ) | PCC | 固定取值 | - |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC;`
- 操作步骤上下文（±2 行原文）：
  L60:
    > 7. 配置预定义规则组。
    >     a. 创建用户模板。
    >       [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    >     b. 将已配置的规则绑定到用户模板。
    >       [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
  L99:
    > 
    > ```
    > ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC;
    > ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test2";
    > ```

### WSFD-011306

**md：`WSFD-011306/WSFD-011306 Radius功能参考信息_15542176.md`**
- 操作步骤上下文（±2 行原文）：
  L45:
    > - **[**ADD SPECIFICAPNVAL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/指定上报的APN/增加用户APN与消息交互使用APN的映射关系（ADD SPECIFICAPNVAL）_09653027.md)**
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - **[ADD RULEBINDING](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)**
    > - **[ADD USRPROFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)**

**md：`WSFD-011306/配置业务触发RADIUS功能_33000859.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | 用户模板名称（USERPROFILENAME） | up_test | 本端规划 | - |
  | [**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | 用户模板类型（UPTYPE） | PCC | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE: USERPROFILENAME="up_test", UPTYPE=PCC;`
- 操作步骤上下文（±2 行原文）：
  L62:
    > 5. 配置业务策略组合。
    >     a. 配置UserProfile模板。
    >       [**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    >     b. 将已配置的Rule绑定到UserProfile。
    >       **[ADD RULEBINDING](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)**
  L102:
    > 
    > ```
    > ADD USERPROFILE: USERPROFILENAME="up_test", UPTYPE=PCC;
    > ADD RULEBINDING: USERPROFILENAME="up_test", RULENAME="rule_test1";
    > ADD USRPROFGROUP: USERPROFGNAME="upg_test";

### WSFD-011201

**md：`WSFD-011201/配置离线_在线计费方式（GGSN_PGW-C）_95923455.md`**
- 数据规划表（该命令的参数行）：
  | **ADD USERPROFILE** | 用户模板名称（USERPROFILENAME） | up-test | 全网规划 | 配置UserProflie。 |
  | **ADD USERPROFILE** | 用户模板类型（UPTYPE） | PCC | 全网规划 | 配置UserProflie。 |
  | **ADD USERPROFILE** | 用户模板名称（USERPROFILENAME） | up-test | 全网规划 | 配置UserProflie。 |
  | **ADD USERPROFILE** | 用户模板类型（UPTYPE） | PCC | 全网规划 | 配置UserProflie。 |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE: USERPROFILENAME="up-test", UPTYPE=PCC;`
  `ADD USERPROFILE: USERPROFILENAME="up-test", UPTYPE=PCC;`
  `ADD USERPROFILE: USERPROFILENAME="up-test", UPTYPE=PCC;`
- 操作步骤上下文（±2 行原文）：
  L100:
    >       > 在线计费：参数 “USAGERPTMODE” 设置为 “ONLINE” ， “ONLMETERINGTYPE” 设置为 **“FREE”** 。
    >     b. 配置UserProfile免费业务的计费方式。
    >       **ADD USERPROFILE**
    >       > **说明**
    >       > 对于UserProfile中计费属性的 “FREESERONLCHG” 或 “FREESEROFFCHG” 配置为 “ENABLE” 的业务即免费业务，如果要想在CG离线话单或在线计费配额上报消息中观察到这些业务的计费信息，则必须在其所在的UserProfile下用 **ADD USERPROFILE** 命令使能offline或online计费，系统缺省已经使能online和offline计费。
  L102:
    >       **ADD USERPROFILE**
    >       > **说明**
    >       > 对于UserProfile中计费属性的 “FREESERONLCHG” 或 “FREESEROFFCHG” 配置为 “ENABLE” 的业务即免费业务，如果要想在CG离线话单或在线计费配额上报消息中观察到这些业务的计费信息，则必须在其所在的UserProfile下用 **ADD USERPROFILE** 命令使能offline或online计费，系统缺省已经使能online和offline计费。
    > 
    > ## [任务示例](#ZH-CN_OPI_0295923455)
  L131:
    > 
    >   ```
    >   ADD USERPROFILE: USERPROFILENAME="up-test", UPTYPE=PCC;
    >   ```
    > 

**md：`WSFD-011201/配置离线计费参数（GGSN_SGW-C_PGW-C）_95923590.md`**
- 数据规划表（该命令的参数行）：
  | **ADD USERPROFILE** | 用户模板名称（USERPROFILENAME） | up-test | 全网规划 | 配置UserProfile |
  | **ADD USERPROFILE** | 用户模板类型（UPTYPE） | PCC | 全网规划 | 配置UserProfile |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE: USERPROFILENAME="up-test", UPTYPE=PCC;`
- 操作步骤上下文（±2 行原文）：
  L91:
    > 2. 配置OFCTemplate模板绑定UserProfile对象。
    >     a. 配置UserProfile。如已配置UserProfile，请跳过该步骤。
    >       **ADD USERPROFILE**
    >     b. 配置UserProfile对象绑定OFCTemplate模板。
    >       **SET USRPROFCHARGE**
  L150:
    > 2. 任务一：配置UserProfile的离线计费参数。
    >   ```
    >   ADD USERPROFILE: USERPROFILENAME="up-test", UPTYPE=PCC;
    >   ```
    >   ```

**md：`WSFD-011201/配置离线计费的费率标识（GGSN_SGW-C_PGW-C）_98555879.md`**
- 数据规划表（该命令的参数行）：
  | **ADD USERPROFILE** | 用户模板名称（USERPROFILENAME） | up-test | 本端规划 | 配置UserProfile。 |
  | **ADD USERPROFILE** | 用户模板类型（UPTYPE） | PCC | 本端规划 | 配置UserProfile。 |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE:USERPROFILENAME="up-test", UPTYPE=PCC;`
  `ADD USERPROFILE:USERPROFILENAME="up-test", UPTYPE=PCC;`
- 操作步骤上下文（±2 行原文）：
  L73:
    >     2. 配置没有绑定Rule的UserProfile，绑定UserProfile的缺省URR组。
    >           a. 配置UserProfile，注意该UserProfile不配置Rule。
    >             **ADD USERPROFILE**
    >           b. 绑定该UserProfile的缺省URR组。
    >             **SET URRGRPBINDING**
  L102:
    >     4. 配置绑定Rule的UserProfile。
    >           a. 配置UserProfile。
    >             **ADD USERPROFILE**
    >           b. 绑定该UserProfile使用的Rule。
    >             **ADD RULEBINDING**
  L139:
    >   //配置UserProfile、UserProfile组及APN，依次将URR组绑定到UserProfile、UserProfile组及APN上。
    >   ```
    >   ADD USERPROFILE:USERPROFILENAME="up-test", UPTYPE=PCC;
    >   SET URRGRPBINDING:USERPROFILENAME="up-test",DFTURRGRPNAME="urrgroup1";
    >   ADD USRPROFGROUP:USERPROFGNAME="upg-test";

**md：`WSFD-011201/配置离线计费费率切换（GGSN_SGW-C_PGW-C）_95923434.md`**
- 数据规划表（该命令的参数行）：
  | **ADD USERPROFILE** | 用户模板名称（USERPROFILENAME） | up-test | 全网规划 | 配置UserProfile。 |
  | **ADD USERPROFILE** | 用户模板类型（UPTYPE） | PCC | 全网规划 | 配置UserProfile。 |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE: USERPROFILENAME="up-test", UPTYPE=PCC;`
- 操作步骤上下文（±2 行原文）：
  L73:
    > 4. 配置UserProfile下的费率切换组。
    >     a. 配置UserProfile。如已配置UserProfile，请跳过该步骤。
    >       **ADD USERPROFILE**
    >     b. 配置UserProfile实例下的费率切换组。
    >       **SET USRPROFCHARGE**
  L152:
    > 4. 任务三：基于UserProfile配置费率切换组。
    >   ```
    >   ADD USERPROFILE: USERPROFILENAME="up-test", UPTYPE=PCC;
    >   ```
    >   ```

**md：`WSFD-011201/配置计费属性CC（GGSN_SGW-C_PGW-C）_95923501.md`**
- 数据规划表（该命令的参数行）：
  | **ADD USERPROFILE** | 用户模板名称（USERPROFILENAME） | up-test | 全网规划 | 配置UserProflie。 |
  | **ADD USERPROFILE** | 用户模板类型（UPTYPE） | PCC | 全网规划 | 配置UserProflie。 |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE: USERPROFILENAME="up-test", UPTYPE=PCC;`
- 操作步骤上下文（±2 行原文）：
  L76:
    >       **ADD CHARGECHAR**
    >     2. 配置UserProflie。如已配置UserProflie，请跳过该步骤。
    >       **ADD USERPROFILE**
    >     3. 将CC绑定到UserProflie上。
    >       **SET USRPROFCHARGE**
  L119:
    > 
    > ```
    > ADD USERPROFILE: USERPROFILENAME="up-test", UPTYPE=PCC;
    > ```
    > 

### WSFD-011206

**md：`WSFD-011206/使能融合计费功能_77691175.md`**
- 数据规划表（该命令的参数行）：
  | **ADD USERPROFILE** | 用户模板名称（USERPROFILENAME） | up-test | 全网规划 | 配置UserProflie。 |
  | **ADD USERPROFILE** | 用户模板类型（UPTYPE） | PCC | 全网规划 | 配置UserProflie。 |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE: USERPROFILENAME="up-test", UPTYPE=PCC;`
- 操作步骤上下文（±2 行原文）：
  L85:
    > 
    > ```
    > ADD USERPROFILE: USERPROFILENAME="up-test", UPTYPE=PCC;
    > ```
    > 

**md：`WSFD-011206/配置SMF与CHF交互的条件和内容_93420840.md`**
- 数据规划表（该命令的参数行）：
  | **ADD USERPROFILE** | 用户模板名称（USERPROFILENAME） | up_test | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE: USERPROFILENAME="up_test", UPTYPE=PCC;`
- 操作步骤上下文（±2 行原文）：
  L78:
    >       **ADD URRGROUP**
    >     b. 配置UserProfile。
    >       **ADD USERPROFILE**
    >     c. 绑定UserProfile与URR组，从而使SMF在与CHF建立计费会话时，为该用户模板的用户携带相应的URR组中的RG。
    >       **SET CTXSTARTRATING**
  L116:
    > ADD URR: URRNAME="urr_test", URRID=1111, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=111, ONLMETERINGTYPE=VOLUME;
    > ADD URRGROUP: URRGROUPNAME="urrgroup_test", UPURRNAME1="urr_test", DOWNURRNAME1="urr_test";
    > ADD USERPROFILE: USERPROFILENAME="up_test", UPTYPE=PCC;
    > SET CTXSTARTRATING: USERPROFILENAME="up_test", CTXRURRGRPNAME1="urrgroup_test";
    > ```

**md：`WSFD-011206/配置融合计费模板_93400212.md`**
- 数据规划表（该命令的参数行）：
  | **ADD USERPROFILE** | 用户模板名称（USERPROFILENAME） | up_test | 全网规划 | 基于UserProfile粒度，将CCT绑定到特定UserProfile下。 |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE: USERPROFILENAME="up_test", UPTYPE=PCC;`
- 操作步骤上下文（±2 行原文）：
  L91:
    >     2. 配置UserProfile，将CCT绑定到UserProfile上。
    >           a. 配置UserProfile。
    >             **ADD USERPROFILE**
    >           b. 将CCT绑定到UserProfile上。
    >             **SET USRPROFCHARGE**
  L140:
    > 
    > ```
    > ADD USERPROFILE: USERPROFILENAME="up_test", UPTYPE=PCC;
    > SET USRPROFCHARGE: USRPROFNAME="up_test", CCTEMPLATE="cct_test";
    > ```

**md：`WSFD-011206/配置融合计费费率标识_93360308.md`**
- 数据规划表（该命令的参数行）：
  | **ADD USERPROFILE** | 用户模板名称（USERPROFILENAME） | userprofile001<br>userprofile002 | 本端规划 | 添加User Profile。<br>USERPROFILE的名称统一规划，保证在PCF、SMF、UPF间名称一致。不一致时PCF下发的策略无法生效。 |
  | **ADD USERPROFILE** | 用户模板类型（UPTYPE） | PCC | 全网规划 | 指定PCC类型用户模板。 |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE: USERPROFILENAME="userprofile001", UPTYPE=PCC;`
  `ADD USERPROFILE: USERPROFILENAME="userprofile002", UPTYPE=PCC;`
- 操作步骤上下文（±2 行原文）：
  L99:
    >     3. 配置UserProfile，将Rule绑定到UserProfile上。
    >           a. 配置UserProfile。
    >             **ADD USERPROFILE**
    >           b. 绑定该UserProfile的缺省URR组，建议每个UserProfile都绑定缺省费率URR组。
    >             **SET URRGRPBINDING**
  L184:
    > 
    > ```
    > ADD USERPROFILE: USERPROFILENAME="userprofile001", UPTYPE=PCC;
    > ADD USERPROFILE: USERPROFILENAME="userprofile002", UPTYPE=PCC;
    > ADD RULEBINDING: USERPROFILENAME="userprofile001", RULENAME="Rule001_dns";
  L185:
    > ```
    > ADD USERPROFILE: USERPROFILENAME="userprofile001", UPTYPE=PCC;
    > ADD USERPROFILE: USERPROFILENAME="userprofile002", UPTYPE=PCC;
    > ADD RULEBINDING: USERPROFILENAME="userprofile001", RULENAME="Rule001_dns";
    > ADD RULEBINDING: USERPROFILENAME="userprofile001", RULENAME="Rule003_any";

**md：`WSFD-011206/配置计费属性CC_90776700.md`**
- 数据规划表（该命令的参数行）：
  | **ADD USERPROFILE** | 用户模板名称（USERPROFILENAME） | up-test | 全网规划 | 配置UserProflie。 |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE: USERPROFILENAME="up-test",UPTYPE=PCC;`
- 操作步骤上下文（±2 行原文）：
  L75:
    >       **ADD CHARGECHAR**
    >     3. 配置UserProfile。如已配置UserProfile，请跳过该步骤。
    >       **ADD USERPROFILE**
    >     4. 将CC绑定到UserProfile上。
    >       **SET USRPROFCHARGE**
  L109:
    > ```
    > ADD CHARGECHAR: CCNAME="testchgcha", HOME="0x0800", ROAM="0x0800", VISIT="0x0800", HOMESGSN=DISABLE, ROAMSGSN=DISABLE, VISITSGSN=DISABLE;
    > ADD USERPROFILE: USERPROFILENAME="up-test",UPTYPE=PCC;
    > SET USRPROFCHARGE: USRPROFNAME="up-test", CCNAME="testchgcha";
    > ```

**md：`WSFD-011206/配置费率切换_86411191.md`**
- 数据规划表（该命令的参数行）：
  | **ADD USERPROFILE** | 用户模板名称（USERPROFILENAME） | up-test | 全网规划 | 配置UserProfile。 |
  | **ADD USERPROFILE** | 用户模板类型（UPTYPE） | PCC | 全网规划 | 配置UserProfile。 |

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L35:
    > - [**ADD CHARGEMETHOD**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费属性计费控制/增加计费方式（ADD CHARGEMETHOD）_09896795.md)
    > - [**SET GLBURRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/全局使用量上报规则组/设置全局使用量上报规则组（SET GLBURRGROUP）_09897187.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**SET URRGRPBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/设置用户模板的计费属性绑定关系（SET URRGRPBINDING）_09897209.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L35:
    > - [**ADD CHARGEMETHOD**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费属性计费控制/增加计费方式（ADD CHARGEMETHOD）_09896795.md)
    > - [**SET GLBURRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/全局使用量上报规则组/设置全局使用量上报规则组（SET GLBURRGROUP）_09897187.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**SET URRGRPBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/设置用户模板的计费属性绑定关系（SET URRGRPBINDING）_09897209.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)

**md：`WSFD-109001/配置在线计费模板_95923574.md`**
- 数据规划表（该命令的参数行）：
  | **ADD USERPROFILE** | 用户模板名称（USERPROFILENAME） | up-test | 全网规划 | 配置UserProflie。 |
  | **ADD USERPROFILE** | 用户模板类型（UPTYPE） | PCC | 全网规划 | 配置UserProflie。 |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE: USERPROFILENAME="up-test", UPTYPE=PCC;`
- 操作步骤上下文（±2 行原文）：
  L85:
    > 4. 配置DCC Template模板绑定UserProfile实例。
    >     a. 指定UserProfile实例。
    >       **ADD USERPROFILE**
    >     b. 配置DCC Template模板绑定UserProfile实例。
    >       **SET USRPROFCHARGE**
  L146:
    > 
    > ```
    > ADD USERPROFILE: USERPROFILENAME="up-test", UPTYPE=PCC;
    > ```
    > 

**md：`WSFD-109001/配置在线计费的费率标识_95923388.md`**
- 数据规划表（该命令的参数行）：
  | **ADD USERPROFILE** | 用户模板名称（USERPROFILENAME） | up-test | 本端规划 | 配置UserProfile。 |
  | **ADD USERPROFILE** | 用户模板类型（UPTYPE） | PCC | 本端规划 | 配置UserProfile。 |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE:USERPROFILENAME="up-test", UPTYPE=PCC;`
  `ADD USERPROFILE:USERPROFILENAME="up-test", UPTYPE=PCC;`
- 操作步骤上下文（±2 行原文）：
  L77:
    >     2. 配置没有绑定Rule的UserProfile，绑定UserProfile的缺省URR组。
    >           a. 配置UserProfile，注意该UserProfile不配置Rule。
    >             **ADD USERPROFILE**
    >           b. 绑定该UserProfile的缺省URR组。
    >             **SET URRGRPBINDING**
  L106:
    >     4. 配置绑定Rule的UserProfile。
    >           a. 配置UserProfile。
    >             **ADD USERPROFILE**
    >           b. 绑定该UserProfile使用的Rule。
    >             **ADD RULEBINDING**
  L143:
    >   //配置UserProfile、UserProfile组及APN，依次将URR组绑定到UserProfile、UserProfile组及APN上。
    >   ```
    >   ADD USERPROFILE:USERPROFILENAME="up-test", UPTYPE=PCC;
    >   SET URRGRPBINDING:USERPROFILENAME="up-test",DFTURRGRPNAME="urrgroup001";
    >   ADD USRPROFGROUP:USERPROFGNAME="upg-test";

**md：`WSFD-109001/配置离线_在线计费方式（GGSN_PGW-C）_15408914.md`**
- 数据规划表（该命令的参数行）：
  | **ADD USERPROFILE** | 用户模板名称（USERPROFILENAME） | up-test | 全网规划 | 配置UserProflie。 |
  | **ADD USERPROFILE** | 用户模板类型（UPTYPE） | PCC | 全网规划 | 配置UserProflie。 |
  | **ADD USERPROFILE** | 用户模板名称（USERPROFILENAME） | up-test | 全网规划 | 配置UserProflie。 |
  | **ADD USERPROFILE** | 用户模板类型（UPTYPE） | PCC | 全网规划 | 配置UserProflie。 |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE: USERPROFILENAME="up-test", UPTYPE=PCC;`
  `ADD USERPROFILE: USERPROFILENAME="up-test", UPTYPE=PCC;`
  `ADD USERPROFILE: USERPROFILENAME="up-test", UPTYPE=PCC;`
- 操作步骤上下文（±2 行原文）：
  L100:
    >       > 在线计费：参数 “USAGERPTMODE” 设置为 “ONLINE” ， “ONLMETERINGTYPE” 设置为 **“FREE”** 。
    >     b. 配置UserProfile免费业务的计费方式。
    >       **ADD USERPROFILE**
    >       > **说明**
    >       > 对于UserProfile中计费属性的 “FREESERONLCHG” 或 “FREESEROFFCHG” 配置为 “ENABLE” 的业务即免费业务，如果要想在CG离线话单或在线计费配额上报消息中观察到这些业务的计费信息，则必须在其所在的UserProfile下用 **ADD USERPROFILE** 命令使能offline或online计费，系统缺省已经使能online和offline计费。
  L102:
    >       **ADD USERPROFILE**
    >       > **说明**
    >       > 对于UserProfile中计费属性的 “FREESERONLCHG” 或 “FREESEROFFCHG” 配置为 “ENABLE” 的业务即免费业务，如果要想在CG离线话单或在线计费配额上报消息中观察到这些业务的计费信息，则必须在其所在的UserProfile下用 **ADD USERPROFILE** 命令使能offline或online计费，系统缺省已经使能online和offline计费。
    > 
    > ## [任务示例](#ZH-CN_OPI_0315408914)
  L131:
    > 
    >   ```
    >   ADD USERPROFILE: USERPROFILENAME="up-test", UPTYPE=PCC;
    >   ```
    > 

**md：`WSFD-109001/配置计费属性CC（GGSN_SGW-C_PGW-C）_15408915.md`**
- 数据规划表（该命令的参数行）：
  | **ADD USERPROFILE** | 用户模板名称（USERPROFILENAME） | up-test | 全网规划 | 配置UserProflie。 |
  | **ADD USERPROFILE** | 用户模板类型（UPTYPE） | PCC | 全网规划 | 配置UserProflie。 |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE: USERPROFILENAME="up-test", UPTYPE=PCC;`
- 操作步骤上下文（±2 行原文）：
  L76:
    >       **ADD CHARGECHAR**
    >     2. 配置UserProflie。如已配置UserProflie，请跳过该步骤。
    >       **ADD USERPROFILE**
    >     3. 将CC绑定到UserProflie上。
    >       **SET USRPROFCHARGE**
  L119:
    > 
    > ```
    > ADD USERPROFILE: USERPROFILENAME="up-test", UPTYPE=PCC;
    > ```
    > 

**md：`WSFD-109001/配置CCR触发场景_95923545.md`**
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE:USERPROFILENAME="up-test", UPTYPE=PCC;`
- 操作步骤上下文（±2 行原文）：
  L130:
    > 
    > ```
    > ADD USERPROFILE:USERPROFILENAME="up-test", UPTYPE=PCC;
    > ```
    > 

### WSFD-109007

**md：`WSFD-109007/WSFD-109007 支持事件计费参考信息_74112323.md`**
- 操作步骤上下文（±2 行原文）：
  L15:
    > - **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)**
    > - [**ADD URRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)

**md：`WSFD-109007/配置事件计费功能_74112321.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md) | USERPROFILENAME（用户模板名称） | up-test | 全网规划 | 配置融合计费和在线计费的URR Group和User Profile。 |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE:USERPROFILENAME="up-test", UPTYPE=PCC;`
- 操作步骤上下文（±2 行原文）：
  L79:
    >       [**ADD URRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)
    >     b. 配置UserProfile。
    >       [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > 5. 配置事件计费使用的Rule，将URR组绑定到对应的Rule上。
    >     a. 配置Rule绑定的PCC策略组，将URR组绑定到PCC策略组。
  L131:
    > ADD URR: URRNAME="urr1", URRID=1000, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=100, ONLMETERINGTYPE=EVENT;
    > ADD URRGROUP: URRGROUPNAME="urrgroup1", UPURRNAME1="urr1", DOWNURRNAME1="urr1";
    > ADD USERPROFILE:USERPROFILENAME="up-test", UPTYPE=PCC;
    > ```
    > 

### WSFD-201207

**md：`WSFD-201207/WSFD-201207 语音PCF_PCRF故障Bypass参考信息_85304300.md`**
- 操作步骤上下文（±2 行原文）：
  L108:
    > **[LST DEACTQFPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/查询去活用户面专有QoS Flow策略（LST DEACTQFPLCY）_92022694.md)**
    > 
    > [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > 
    > **[RMV USERPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/删除用户模板（RMV USERPROFILE）_09897213.md)**

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（Gx接口）_60552093.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD USERPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)** | 用户模板名称（USERPROFILENAME） | up_ims | 全网规划 | （可选）配置用户模板。 |
  | **[ADD USERPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)** | 用户模板名称（USERPROFILENAME） | up_ims | 全网规划 | （可选）配置用户模板。 |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE:USERPROFILENAME="up_ims";`
- 操作步骤上下文（±2 行原文）：
  L204:
    >       > **说明**
    >       > 如果已配置了APN ims使用的用户模板，则跳过本步骤。
    >       **[ADD USERPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)**
    >     f. 增加用户模板与规则的绑定关系。
    >       [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
  L235:
    >       > **说明**
    >       > 如果已配置了APN ims使用的用户模板，则跳过本步骤。
    >       **[ADD USERPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)**
    >     g. 增加用户模板与规则的绑定关系。
    >       [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
  L326:
    > 
    >       ```
    >       ADD USERPROFILE:USERPROFILENAME="up_ims";
    >       ```
    >       //增加用户模板与规则的绑定关系。

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（N7接口）_32852169.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD USERPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)** | 用户模板名称（USERPROFILENAME） | up_ims | 全网规划 | （可选）配置用户模板。 |
  | **[ADD USERPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)** | 用户模板名称（USERPROFILENAME） | up_ims | 全网规划 | （可选）配置用户模板。 |
- 任务示例脚本（该命令行）：
  `ADD USERPROFILE:USERPROFILENAME="up_ims";`
- 操作步骤上下文（±2 行原文）：
  L223:
    >       > **说明**
    >       > 如果已配置了APN ims使用的用户模板，则跳过本步骤。
    >       **[ADD USERPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)**
    >     f. 增加用户模板与规则的绑定关系。
    >       [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
  L254:
    >       > **说明**
    >       > 如果已配置了APN ims使用的用户模板，则跳过本步骤。
    >       **[ADD USERPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)**
    >     g. 增加用户模板与规则的绑定关系。
    >       [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
  L354:
    > 
    >       ```
    >       ADD USERPROFILE:USERPROFILENAME="up_ims";
    >       ```
    >       //增加用户模板与规则的绑定关系。

## ④ 自动比对
- 命令真相参数（10）：['FREEONLFLAGSW', 'FREESERCVGCHG', 'FREESEROFFCHG', 'FREESERONLCHG', 'PROFILERANGE', 'QOSANASW', 'RELAYSW', 'UPSPECTYPE', 'UPTYPE', 'USERPROFILENAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 41, '本端规划': 12, '固定取值': 6, '与对端协商': 1}（多值→atom 应考虑 decision_driven）
