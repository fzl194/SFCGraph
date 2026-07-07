# 命令证据包：ADD RULEBINDING
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md`
> 用该命令的特性数：17

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于增加用户模板与规则的绑定关系，当用户数据报文可以匹配到多个规则时，需要将多个规则绑定到用户模板下。SMF给UPF下发规则时，下发用户模板即可使多个规则同时生效。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为200000。
- 同一ULCL类型的用户模板下最多可绑定512个规则。
- 执行此命令前，需要先执行ADD USERPROFILE和ADD RULE命令。
- 当UPSPECTYPE为SPECIFICATION_LIMITED时，单个用户模板最多可绑定100个规则。
- 当UPSPECTYPE参数不指定或者指定为DEFAULT时，单个用户模板最多

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| USERPROFILENAME | 用户模板名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| RULENAME | 规则名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| POLICYTYPE | 策略类型 | local_planned | optional | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-108002

**md：`WSFD-108002/WSFD-108002 基于预定义规则的分流策略控制参考信息_28860592.md`**
- 操作步骤上下文（±2 行原文）：
  L17:
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)

**md：`WSFD-108002/激活基于预定义规则的分流策略控制_28860590.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 用户模板名称（USERPROFILENAME） | testuserprofilename | 全网规划 | 将UL CL属性的User Profile和rule进行绑定 |
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 规则名称（RULENAME） | testrule | 本端规划 | 将UL CL属性的User Profile和rule进行绑定 |
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 策略类型（POLICYTYPE） | ULCL | 本端规划 | 将UL CL属性的User Profile和rule进行绑定 |
- 任务示例脚本（该命令行）：
  `ADD RULEBINDING: USERPROFILENAME="testuserprofilename",RULENAME="testrule",POLICYTYPE=ULCL;`
  `ADD RULEBINDING: USERPROFILENAME="testuserprofilename",RULENAME="testrule",POLICYTYPE=ULCL;`
  `ADD RULEBINDING: USERPROFILENAME="testuserprofilename",RULENAME="testrule",POLICYTYPE=ULCL;`
- 操作步骤上下文（±2 行原文）：
  L84:
    >       [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    >     e. 将上述rule绑定至用户模板。
    >       [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > 3. 配置基于DNN的分流，将DNN绑定至UL CL分流规则中。
    >     a. 配置使能SMF上的ULCL功能。
  L130:
    > //配置ULCL属性的用户模板，并将ULCL分流策略rule绑定至该模板。
    > ADD USERPROFILE:USERPROFILENAME="testuserprofilename", UPTYPE=ULCL; 
    > ADD RULEBINDING: USERPROFILENAME="testuserprofilename",RULENAME="testrule",POLICYTYPE=ULCL;
    > //配置用户模板组，并将ULCL属性的用户模板绑定至该模板组，再将模板组绑定至指定APN。
    > ADD USRPROFGROUP:USERPROFGNAME="ulcl_test";
  L156:
    > //配置ULCL属性的用户模板，并将ULCL分流策略rule绑定至该模板。
    > ADD USERPROFILE:USERPROFILENAME="testuserprofilename", UPTYPE=ULCL; 
    > ADD RULEBINDING: USERPROFILENAME="testuserprofilename",RULENAME="testrule",POLICYTYPE=ULCL;
    > //配置IPv6会话场景下的分流策略。
    > SET SMFFUNC: IPV6LOCALUP=UlClPrefer;

### WSFD-223001

**md：`WSFD-223001/WSFD-223001 基于位置信息的分流策略控制参考信息_47717539.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)

**md：`WSFD-223001/部署基于位置信息的分流策略控制（SMF）_53995959.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 用户模板名称（USERPROFILENAME） | testuserprofilename | 全网规划 | 将UL CL属性的User Profile和rule进行绑定 |
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 规则名称（RULENAME） | testrule | 本端规划 | 将UL CL属性的User Profile和rule进行绑定 |
- 任务示例脚本（该命令行）：
  `ADD RULEBINDING: USERPROFILENAME="testuserprofilename",RULENAME="testrule";`
- 操作步骤上下文（±2 行原文）：
  L56:
    > //配置ULCL属性的用户模板，并将ULCL分流策略rule绑定至该模板。
    > ADD USERPROFILE:USERPROFILENAME="testuserprofilename", UPTYPE=ULCL; 
    > ADD RULEBINDING: USERPROFILENAME="testuserprofilename",RULENAME="testrule";
    > //配置IPv6会话场景下的分流策略。
    > SET SMFFUNC: IPV6LOCALUP=UlClPrefer;

### WSFD-223003

**md：`WSFD-223003/WSFD-223003 基于漫游地动态签约的分流策略控制特性参考信息_52923849.md`**
- 操作步骤上下文（±2 行原文）：
  L24:
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)

**md：`WSFD-223003/部署基于漫游地动态签约的分流策略控制（SMF）_82779459.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULEBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 用户模板名称（USERPROFILENAME） | testuserprofilename | 全网规划 | 将UL CL属性的User Profile和rule进行绑定 |
  | [**ADD RULEBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 规则名称（RULENAME） | testrule | 本端规划 | 将UL CL属性的User Profile和rule进行绑定 |
- 任务示例脚本（该命令行）：
  `ADD RULEBINDING: USERPROFILENAME="testuserprofilename",RULENAME="testrule";`
- 操作步骤上下文（±2 行原文）：
  L60:
    >       [**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    >     e. 将上述rule绑定至用户模板。
    >       [**ADD RULEBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > 3. 配置基于DNN的分流，将专网DNN绑定至UL CL分流规则中。
    >     a. 配置使能SMF上的ULCL功能。
  L104:
    > //配置ULCL属性的用户模板，并将ULCL分流策略rule绑定至该模板。
    > ADD USERPROFILE:USERPROFILENAME="testuserprofilename", UPTYPE=ULCL; 
    > ADD RULEBINDING: USERPROFILENAME="testuserprofilename",RULENAME="testrule";
    > //配置用户模板组，并将ULCL属性的用户模板绑定至该模板组，再将模板组绑定至指定APN。
    > ADD USRPROFGROUP:USERPROFGNAME="ulcl_test";

### WSFD-223101

**md：`WSFD-223101/WSFD-223101 基于预定义规则的分流策略控制(4G)参考信息_11634944.md`**
- 操作步骤上下文（±2 行原文）：
  L17:
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)

**md：`WSFD-223101/部署基于预定义规则的分流策略控制(4G)（SMF）_11155006.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 用户模板名称（USERPROFILENAME） | testuserprofilename | 全网规划 | 将UL CL属性的User Profile和rule进行绑定 |
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 规则名称（RULENAME） | testrule | 本端规划 | 将UL CL属性的User Profile和rule进行绑定 |
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 策略类型（POLICYTYPE） | ULCL | 本端规划 | 将UL CL属性的User Profile和rule进行绑定 |
- 任务示例脚本（该命令行）：
  `ADD RULEBINDING: USERPROFILENAME="testuserprofilename",RULENAME="testrule",POLICYTYPE=ULCL;`
- 操作步骤上下文（±2 行原文）：
  L64:
    >       [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    >     e. 将上述rule绑定至用户模板。
    >       [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > 4. **可选：**配置DNAI关联的位置区域。当采用基于SMF本地DNN使能UL CL分流方式时，需要配置此步骤。
    >     a. 配置DNAI对应的服务区域。
  L113:
    > ```
    > ADD USERPROFILE:USERPROFILENAME="testuserprofilename", UPTYPE=ULCL; 
    > ADD RULEBINDING: USERPROFILENAME="testuserprofilename",RULENAME="testrule",POLICYTYPE=ULCL;
    > ```
    > 

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L28:
    > - [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD PCCPOLICYGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULEBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD APNUSRPROFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**ADD IMSIMSISDNSEG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)

**md：`WSFD-109101/配置动态PCC功能_30805098.md`**
- 操作步骤上下文（±2 行原文）：
  L144:
    >       [**ADD USRPROBINDDNAI**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板DNAI绑定/增加用户模板关联的DNAI （ADD USRPROBINDDNAI）_27051919.md)
    >     c. 将已配置的rule绑定到UserProfile。
    >       [**ADD RULEBINDING**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0230805098)

**md：`WSFD-109101/配置本地PCC功能_30805097.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULEBINDING**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | USERPROFILENAME（用户模板名称） | up-test | 已配置数据中获取 | 将Rule绑定到UserProfile上。 |
  | [**ADD RULEBINDING**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | RULENAME（规则名称） | rule-test | 已配置数据中获取 | 将Rule绑定到UserProfile上。 |
- 任务示例脚本（该命令行）：
  `ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";`
- 操作步骤上下文（±2 行原文）：
  L99:
    >       [**ADD USRPROBINDDNAI**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板DNAI绑定/增加用户模板关联的DNAI （ADD USRPROBINDDNAI）_27051919.md)
    >     c. 将已配置的rule绑定到UserProfile。
    >       [**ADD RULEBINDING**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    >     d. 配置UserProfile Group。
    >       [**ADD USRPROFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
  L155:
    >   ```
    >   ```
    >   ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";
    >   ```
    >   ```

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULEBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 用户模板名称(USERPROFILENAME) | up_test | 已配置数据中获取 | 将本地rule/预定义规则rule绑定到UserProfile上。 |
  | [**ADD RULEBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 规则名称(RULENAME) | rule_test | 已配置数据中获取 | 将本地rule/预定义规则rule绑定到UserProfile上。 |
  | [**ADD RULEBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 策略类型 | PCC | 本端规划 | 如果不指定策略类型，则把规则名称相同的所有策略类型的规则绑定到用户模板上。 |
- 任务示例脚本（该命令行）：
  `ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";`
- 操作步骤上下文（±2 行原文）：
  L182:
    >             [**ADD USRPROBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板DNAI绑定/增加用户模板关联的DNAI （ADD USRPROBINDDNAI）_27051919.md)
    >           c. 将rule绑定到UserProfile。
    >             [**ADD RULEBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    >     15. **可选：**配置UserProfile组，将UserProfile绑定到UserProfile组，再将UserProfile组绑定到DNN实例上。用于动态PCC或本地PCC。
    >           a. 配置UserProfile Group。
  L260:
    > ```
    > ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC,PROFILERANGE=ALL;
    > ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";
    > ADD USRPROFGROUP:USERPROFGNAME="upg_test";
    > ADD UPBINDUPG:USERPROFGNAME="upg_test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up_test";

### WSFD-109102

**md：`WSFD-109102/激活ADC基本功能_92582136.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 用户模板名称(USERPROFILENAME) | up_test | 已配置数据中获取 | 将本地rule/预定义规则rule绑定到UserProfile上。 |
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 规则名称(RULENAME) | rule_test | 已配置数据中获取 | 将本地rule/预定义规则rule绑定到UserProfile上。 |
- 任务示例脚本（该命令行）：
  `ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";`
- 操作步骤上下文（±2 行原文）：
  L59:
    >             [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    >           2. 将rule绑定到UserProfile。
    >             [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0292582136)
  L94:
    > ADD RULE:RULENAME="rule_test",POLICYTYPE=ADC;
    > ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC;
    > ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";
    > ```

**md：`WSFD-109102/调测ADC基本功能_92582137.md`**
- 操作步骤上下文（±2 行原文）：
  L63:
    >       PCF通过预定义规则组下发APP_STA/APP_STO时，UPF/SMF/PCF上的规则组标识必须一致。
    >           - 是，请执行[步骤 8.d](#ZH-CN_OPI_0292582137__substep11878176105)。
    >           - 否，请执行[**RMV RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/删除用户模板和规则的绑定关系（RMV RULEBINDING）_09897217.md)命令后重新执行[**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)命令，然后重新执行[步骤 4](#ZH-CN_OPI_0292582137__step2056531835011)。
    >     d. 执行 [**LST RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/查询规则（LST RULE）_09897204.md) 命令，检查Rule配置是否正确。
    >       PCF通过预定义规则下发APP_STA/APP_STO时，UPF/SMF/PCF上的规则标识必须一致。
  L67:
    >       PCF通过预定义规则下发APP_STA/APP_STO时，UPF/SMF/PCF上的规则标识必须一致。
    >           - 是，请执行[步骤 9](#ZH-CN_OPI_0292582137__step114691314193316)。
    >           - 否，请执行[**RMV RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/删除用户模板和规则的绑定关系（RMV RULEBINDING）_09897217.md)命令和[**RMV RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/删除规则（RMV RULE）_09897203.md)后重新执行[**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)和[**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)命令，然后重新执行[步骤 4](#ZH-CN_OPI_0292582137__step2056531835011)。
    > 9. 请联系华为技术支持工程师。
    >     a. 重新执行上述步骤并保存报文。

### WSFD-109103

**md：`WSFD-109103/WSFD-109103 IPv6 SA参考信息_78881328.md`**
- 操作步骤上下文（±2 行原文）：
  L17:
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0278881328)

**md：`WSFD-109103/调测IPv6 SA_78881327.md`**
- 操作步骤上下文（±2 行原文）：
  L54:
    >     b. 执行 [**LST RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/查询用户模板和规则的绑定关系（LST RULEBINDING）_09897218.md) 命令，查询UserProfile绑定的Rule是否正确。
    >           - 是，请执行[步骤 6.c](#ZH-CN_OPI_0278881327__substep11878176105)。
    >           - 否，请执行[**RMV RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/删除用户模板和规则的绑定关系（RMV RULEBINDING）_09897217.md)命令后重新执行[**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)命令，然后再执行[步骤 4](#ZH-CN_OPI_0278881327__step2056531835011)。
    >     c. 执行 [**LST RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/查询规则（LST RULE）_09897204.md) 命令，检查Rule配置是否正确。
    >           - 是，请执行[步骤 7](#ZH-CN_OPI_0278881327__step114691314193316)。
  L57:
    >     c. 执行 [**LST RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/查询规则（LST RULE）_09897204.md) 命令，检查Rule配置是否正确。
    >           - 是，请执行[步骤 7](#ZH-CN_OPI_0278881327__step114691314193316)。
    >           - 否，请执行[**RMV RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/删除用户模板和规则的绑定关系（RMV RULEBINDING）_09897217.md)命令和[**RMV RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/删除规则（RMV RULE）_09897203.md)后重新执行[**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)和[**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)命令，然后再执行[步骤 4](#ZH-CN_OPI_0278881327__step2056531835011)。
    > 7. 请联系华为技术支持工程师。
    >     a. 重新执行上述步骤并保存报文。

### WSFD-109107

**md：`WSFD-109107/WSFD-109107 业务触发的QoS保证参考信息_85397060.md`**
- 操作步骤上下文（±2 行原文）：
  L17:
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)

**md：`WSFD-109107/激活业务触发的QoS保证_85397058.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 用户模板名称(USERPROFILENAME) | up_test | 已配置数据中获取 | 将本地rule/预定义规则rule绑定到UserProfile上。 |
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 规则名称(RULENAME) | rule_test | 已配置数据中获取 | 将本地rule/预定义规则rule绑定到UserProfile上。 |
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 策略类型（POLICYTYPE） | QOS | 本端规划 | 如果不指定策略类型，则把规则名称相同的所有策略类型的规则绑定到用户模板上。 |
- 任务示例脚本（该命令行）：
  `ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test",POLICYTYPE=QOS;`
- 操作步骤上下文（±2 行原文）：
  L86:
    >       [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    >     b. 将rule绑定到UserProfile。
    >       [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > 7. **可选：**（无可用PCRF/PCF时使用）配置UserProfile组，将UserProfile绑定到UserProfile组，再将UserProfile组绑定到DNN实例上。用于本地PCC的静态规则。如UserProfile已配置，请跳过本步骤。
    >     a. 配置UserProfile Group。
  L153:
    > ```
    > ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC;
    > ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test",POLICYTYPE=QOS;
    > ```
    > 

### WSFD-211005

**md：`WSFD-211005/WSFD-211005 基于业务感知的带宽控制参考信息_79619228.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)

**md：`WSFD-211005/激活基于业务感知的带宽控制_79619226.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 用户模板名称(USERPROFILENAME) | up_test | 已配置数据中获取 | 将本地rule/预定义规则rule绑定到UserProfile上。 |
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 规则名称(RULENAME) | rule_test | 已配置数据中获取 | 将本地rule/预定义规则rule绑定到UserProfile上。 |
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 策略类型 | BWM | 本端规划 | 如果不指定策略类型，则把规则名称相同的所有策略类型的规则绑定到用户模板上。 |
- 任务示例脚本（该命令行）：
  `ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";`
- 操作步骤上下文（±2 行原文）：
  L52:
    >       [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    >     b. 将rule绑定到UserProfile。
    >       [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > 3. 配置UserProfile组，将UserProfile绑定到UserProfile组，再将UserProfile组绑定到DNN实例上。用于动态PCC或本地PCC。
    >     a. 配置UserProfile Group。如已配置，请跳过本步骤。
  L79:
    > ```
    > ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC;
    > ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";
    > ADD USRPROFGROUP:USERPROFGNAME="upg_test";
    > ADD UPBINDUPG:USERPROFGNAME="upg_test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up_test";

### WSFD-211009

**md：`WSFD-211009/WSFD-211009 基于业务累计流量的策略控制参考信息_27915158.md`**
- 操作步骤上下文（±2 行原文）：
  L17:
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0227915158)

**md：`WSFD-211009/激活基于业务累计流量的策略控制_27915156.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 用户模板名称(USERPROFILENAME) | up_test | 已配置数据中获取 | 使用<br>[**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)<br>命令定义的用户模板名称。 |
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 规则名称(RULENAME) | rule_test2 | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test2";`
- 操作步骤上下文（±2 行原文）：
  L62:
    >       [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    >     b. 将已配置的规则绑定到用户模板。
    >       [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0227915156)
  L100:
    > ```
    > ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC;
    > ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test2";
    > ```

### WSFD-011306

**md：`WSFD-011306/WSFD-011306 Radius功能参考信息_15542176.md`**
- 操作步骤上下文（±2 行原文）：
  L46:
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - **[ADD RULEBINDING](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)**
    > - **[ADD USRPROFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)**
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)

**md：`WSFD-011306/配置业务触发RADIUS功能_33000859.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD RULEBINDING](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)** | 规则名称（RULENAME） | rule_test1 | 已配置数据中获取 | User Profile绑定的业务规则，已通过<br>[**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)<br>配置，可以使用<br>**[LST RULE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/查询规则（LST RULE）_09897204.md)**<br>命令进行查询。 |
  | **[ADD RULEBINDING](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)** | 用户模板名称（USERPROFILENAME） | up_test | 已配置数据中获取 | 已通过<br>[**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)<br>配置，可以使用<br>**[**LST USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/查询用户模板（LST USERPROFILE）_09897214.md)**<br>命令进行查询。 |
- 任务示例脚本（该命令行）：
  `ADD RULEBINDING: USERPROFILENAME="up_test", RULENAME="rule_test1";`
- 操作步骤上下文（±2 行原文）：
  L64:
    >       [**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    >     b. 将已配置的Rule绑定到UserProfile。
    >       **[ADD RULEBINDING](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)**
    >     c. 配置UsrProfGroup。
    >       **[ADD USRPROFGROUP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)**
  L103:
    > ```
    > ADD USERPROFILE: USERPROFILENAME="up_test", UPTYPE=PCC;
    > ADD RULEBINDING: USERPROFILENAME="up_test", RULENAME="rule_test1";
    > ADD USRPROFGROUP: USERPROFGNAME="upg_test";
    > ADD UPBINDUPG: USERPROFGNAME="upg_test", UPBINDTYPE=DEFAULT, USERPROFILENAME="up_test";

### WSFD-011201

**md：`WSFD-011201/配置离线计费的费率标识（GGSN_SGW-C_PGW-C）_98555879.md`**
- 数据规划表（该命令的参数行）：
  | **ADD RULEBINDING** | USERPROFILENAME（用户模板名称） | up-test | 已配置数据中获取 | 将Rule绑定到UserProfile上。 |
  | **ADD RULEBINDING** | RULENAME（规则名称） | Rule001 | 已配置数据中获取 | 将Rule绑定到UserProfile上。 |
- 任务示例脚本（该命令行）：
  `ADD RULEBINDING:USERPROFILENAME="up-test",RULENAME="Rule001";`
- 操作步骤上下文（±2 行原文）：
  L104:
    >             **ADD USERPROFILE**
    >           b. 绑定该UserProfile使用的Rule。
    >             **ADD RULEBINDING**
    >     5. 配置UserProfile绑定的UserProfile组及APN实例。
    >           a. 配置UserProfile组，将UserProfile绑定到UserProfile组上。
  L168:
    >   ```
    >   ADD USERPROFILE:USERPROFILENAME="up-test", UPTYPE=PCC;
    >   ADD RULEBINDING:USERPROFILENAME="up-test",RULENAME="Rule001";
    >   ADD USRPROFGROUP:USERPROFGNAME="upg-test";
    >   ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";

### WSFD-011206

**md：`WSFD-011206/WSFD-011206 支持融合计费参考信息_74013176.md`**
- 操作步骤上下文（±2 行原文）：
  L27:
    > - [**SET URRGRPBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/设置用户模板的计费属性绑定关系（SET URRGRPBINDING）_09897209.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)
    > - [**ADD SELECTCCTBYCC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板绑定/增加基于CC配置融合计费模板处理（ADD SELECTCCTBYCC）_09654384.md)

**md：`WSFD-011206/配置融合计费费率标识_93360308.md`**
- 数据规划表（该命令的参数行）：
  | **ADD RULEBINDING** | 用户模板名称（USERPROFILENAME） | userprofile001 | 已配置数据中获取 | 使用<br>**ADD USERPROFILE**<br>命令定义的<br>“USERPROFILENAME”<br>。 |
  | **ADD RULEBINDING** | 规则名称（RULENAME） | Rule001_dns<br>Rule003_any<br>Rule003_any_IPv6 | 已配置数据中获取 | 使用<br>**ADD RULE**<br>命令定义的<br>**RULENAME**<br>。 |
  | **ADD RULEBINDING** | 用户模板名称（USERPROFILENAME） | userprofile002 | 已配置数据中获取 | 使用<br>**ADD USERPROFILE**<br>命令定义的<br>“USERPROFILENAME”<br>。 |
  | **ADD RULEBINDING** | 规则名称（RULENAME） | Rule002_IMS | 已配置数据中获取 | 使用<br>**ADD RULE**<br>命令定义的<br>**RULENAME**<br>。<br>SMF、UPF上USERPROFILE下绑定的RULENAME、POLICYTYPE需要保持一致。 |
- 任务示例脚本（该命令行）：
  `ADD RULEBINDING: USERPROFILENAME="userprofile001", RULENAME="Rule001_dns";`
  `ADD RULEBINDING: USERPROFILENAME="userprofile001", RULENAME="Rule003_any";`
  `ADD RULEBINDING: USERPROFILENAME="userprofile001", RULENAME="Rule003_any_IPv6";`
  `ADD RULEBINDING: USERPROFILENAME="userprofile002", RULENAME="Rule002_IMS";`
- 操作步骤上下文（±2 行原文）：
  L103:
    >             **SET URRGRPBINDING**
    >           c. 将Rule绑定到UserProfile上。
    >             **ADD RULEBINDING**
    >     4. 配置UserProfile组及DNN实例。
    >           a. 配置UserProfile组，将UserProfile绑定到UserProfile组。
  L186:
    > ADD USERPROFILE: USERPROFILENAME="userprofile001", UPTYPE=PCC;
    > ADD USERPROFILE: USERPROFILENAME="userprofile002", UPTYPE=PCC;
    > ADD RULEBINDING: USERPROFILENAME="userprofile001", RULENAME="Rule001_dns";
    > ADD RULEBINDING: USERPROFILENAME="userprofile001", RULENAME="Rule003_any";
    > ADD RULEBINDING: USERPROFILENAME="userprofile001", RULENAME="Rule003_any_IPv6";
  L187:
    > ADD USERPROFILE: USERPROFILENAME="userprofile002", UPTYPE=PCC;
    > ADD RULEBINDING: USERPROFILENAME="userprofile001", RULENAME="Rule001_dns";
    > ADD RULEBINDING: USERPROFILENAME="userprofile001", RULENAME="Rule003_any";
    > ADD RULEBINDING: USERPROFILENAME="userprofile001", RULENAME="Rule003_any_IPv6";
    > ADD RULEBINDING: USERPROFILENAME="userprofile002", RULENAME="Rule002_IMS";

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L42:
    > - [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD FESTIVAL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/节假日/增加计费节假日表（ADD FESTIVAL）_09896827.md)
    > - [**ADD WEEKDAY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/工作日/配置计费星期表（ADD WEEKDAY）_09896831.md)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L42:
    > - [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD FESTIVAL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/节假日/增加计费节假日表（ADD FESTIVAL）_09896827.md)
    > - [**ADD WEEKDAY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/工作日/配置计费星期表（ADD WEEKDAY）_09896831.md)

**md：`WSFD-109001/配置在线计费的费率标识_95923388.md`**
- 数据规划表（该命令的参数行）：
  | **ADD RULEBINDING** | USERPROFILENAME（用户模板名称） | up-test | 已配置数据中获取 | 将Rule绑定到UserProfile上。 |
  | **ADD RULEBINDING** | RULENAME（规则名称） | Rule002 | 已配置数据中获取 | 将Rule绑定到UserProfile上。 |
- 任务示例脚本（该命令行）：
  `ADD RULEBINDING:USERPROFILENAME="up-test",RULENAME="Rule002";`
- 操作步骤上下文（±2 行原文）：
  L108:
    >             **ADD USERPROFILE**
    >           b. 绑定该UserProfile使用的Rule。
    >             **ADD RULEBINDING**
    >     5. 配置UserProfile绑定的UserProfile组及APN实例。
    >           a. 配置UserProfile组，将UserProfile绑定到UserProfile组上。
  L173:
    >   ```
    >   ADD USERPROFILE:USERPROFILENAME="up-test", UPTYPE=PCC;
    >   ADD RULEBINDING:USERPROFILENAME="up-test",RULENAME="Rule002";
    >   ADD USRPROFGROUP:USERPROFGNAME="upg-test";
    >   ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";

### WSFD-109007

**md：`WSFD-109007/WSFD-109007 支持事件计费参考信息_74112323.md`**
- 操作步骤上下文（±2 行原文）：
  L21:
    > - [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
    > - [**ADD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)

**md：`WSFD-109007/配置事件计费功能_74112321.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | USERPROFILENAME（用户模板名称） | up-test | 本端规划 | 将Rule绑定到UserProfile上。 |
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | RULENAME（规则名称） | rule-test | 本端规划 | 将Rule绑定到UserProfile上。 |
- 任务示例脚本（该命令行）：
  `ADD RULEBINDING:USERPROFILENAME="up-test",RULENAME="rule-test";`
- 操作步骤上下文（±2 行原文）：
  L93:
    >       [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
    > 7. 绑定该UserProfile使用的Rule。
    >   [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > 8. 配置UserProfile绑定的UserProfile组及DNN实例。
    >     a. 配置UserProfile组，将UserProfile绑定到UserProfile组上。
  L158:
    > 
    > ```
    > ADD RULEBINDING:USERPROFILENAME="up-test",RULENAME="rule-test";
    > ADD USRPROFGROUP:USERPROFGNAME="upg-test";
    > ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";

### WSFD-201207

**md：`WSFD-201207/WSFD-201207 语音PCF_PCRF故障Bypass参考信息_85304300.md`**
- 操作步骤上下文（±2 行原文）：
  L52:
    > **[LST RULE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/查询规则（LST RULE）_09897204.md)**
    > 
    > [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > 
    > **[RMV RULEBINDING](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/删除用户模板和规则的绑定关系（RMV RULEBINDING）_09897217.md)**

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（Gx接口）_60552093.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 用户模板名称(USERPROFILENAME) | up_ims | 已配置数据中获取 | 增加用户模板与规则的绑定关系，将本地rule/预定义规则rule绑定到UserProfile上。 |
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 规则名称(RULENAME) | rule_ims_signaling | 已配置数据中获取 | 增加用户模板与规则的绑定关系，将本地rule/预定义规则rule绑定到UserProfile上。 |
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 策略类型（POLICYTYPE） | PCC | 本端规划 | 如果不指定策略类型，则把规则名称相同的所有策略类型的规则绑定到用户模板上。 |
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 用户模板名称(USERPROFILENAME) | up_ims | 已配置数据中获取 | 增加用户模板与规则的绑定关系，将本地rule/预定义规则rule绑定到UserProfile上。 |
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 规则名称(RULENAME) | rule_ims_voice | 已配置数据中获取 | 增加用户模板与规则的绑定关系，将本地rule/预定义规则rule绑定到UserProfile上。 |
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 策略类型（POLICYTYPE） | PCC | 本端规划 | 如果不指定策略类型，则把规则名称相同的所有策略类型的规则绑定到用户模板上。 |
- 任务示例脚本（该命令行）：
  `ADD RULEBINDING:USERPROFILENAME="up_ims", RULENAME="rule_ims_signaling", POLICYTYPE=PCC;`
  `ADD RULEBINDING:USERPROFILENAME="up_ims", RULENAME="rule_ims_voice", POLICYTYPE=PCC;`
  `ADD RULEBINDING:USERPROFILENAME="up_ims", RULENAME="rule_ims_voice", POLICYTYPE=PCC;`
- 操作步骤上下文（±2 行原文）：
  L206:
    >       **[ADD USERPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)**
    >     f. 增加用户模板与规则的绑定关系。
    >       [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    >     g. **可选：**配置用户模板组。
    >       > **说明**
  L237:
    >       **[ADD USERPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)**
    >     g. 增加用户模板与规则的绑定关系。
    >       [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    >     h. **可选：**配置用户模板组。
    >       > **说明**
  L331:
    > 
    >       ```
    >       ADD RULEBINDING:USERPROFILENAME="up_ims", RULENAME="rule_ims_signaling", POLICYTYPE=PCC;
    >       ```
    >       //配置用户模板组。

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（N7接口）_32852169.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 用户模板名称(USERPROFILENAME) | up_ims | 已配置数据中获取 | 增加用户模板与规则的绑定关系，将本地rule/预定义规则rule绑定到UserProfile上。 |
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 规则名称(RULENAME) | rule_ims_signaling | 已配置数据中获取 | 增加用户模板与规则的绑定关系，将本地rule/预定义规则rule绑定到UserProfile上。 |
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 策略类型（POLICYTYPE） | PCC | 本端规划 | 如果不指定策略类型，则把规则名称相同的所有策略类型的规则绑定到用户模板上。 |
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 用户模板名称(USERPROFILENAME) | up_ims | 已配置数据中获取 | 增加用户模板与规则的绑定关系，将本地rule/预定义规则rule绑定到UserProfile上。 |
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 规则名称(RULENAME) | rule_ims_voice | 已配置数据中获取 | 增加用户模板与规则的绑定关系，将本地rule/预定义规则rule绑定到UserProfile上。 |
  | [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 策略类型（POLICYTYPE） | PCC | 本端规划 | 如果不指定策略类型，则把规则名称相同的所有策略类型的规则绑定到用户模板上。 |
- 任务示例脚本（该命令行）：
  `ADD RULEBINDING:USERPROFILENAME="up_ims", RULENAME="rule_ims_signaling", POLICYTYPE=PCC;`
  `ADD RULEBINDING:USERPROFILENAME="up_ims", RULENAME="rule_ims_voice", POLICYTYPE=PCC;`
  `ADD RULEBINDING:USERPROFILENAME="up_ims", RULENAME="rule_ims_voice", POLICYTYPE=PCC;`
- 操作步骤上下文（±2 行原文）：
  L225:
    >       **[ADD USERPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)**
    >     f. 增加用户模板与规则的绑定关系。
    >       [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    >     g. **可选：**配置用户模板组。
    >       > **说明**
  L256:
    >       **[ADD USERPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)**
    >     g. 增加用户模板与规则的绑定关系。
    >       [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    >     h. **可选：**配置用户模板组。
    >       > **说明**
  L359:
    > 
    >       ```
    >       ADD RULEBINDING:USERPROFILENAME="up_ims", RULENAME="rule_ims_signaling", POLICYTYPE=PCC;
    >       ```
    >       //配置用户模板组。

## ④ 自动比对
- 命令真相参数（3）：['POLICYTYPE', 'RULENAME', 'USERPROFILENAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 4, '本端规划': 16, '已配置数据中获取': 29}（多值→atom 应考虑 decision_driven）
