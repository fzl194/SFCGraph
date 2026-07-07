# 命令证据包：ADD RULE
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md`
> 用该命令的特性数：17

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于配置业务策略规则，也就是下文提到的Rule。具体包含规则名称、策略类型、以及全局优先级等。SMF通过信令流程从PCRF/PCF获取预定义规则后会和该命令配置的rule进行匹配，如果匹配上会给UPF下发对应的Rule名称。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 当RULESPECTYPE参数不指定或者指定为DEFAULT时，该命令最大记录数为8000；当RULESPECTYPE参数指定为SPECIFICATION_LIMITED时，该命令最大记录数为100000。当配置记录数大于规格的98%时，会上报“ALM-135602215 配置数量超阈值”告警。当配置记录数小于等于配置规格95%时，恢复“ALM-135602215 

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| RULENAME | 规则名称 | 对端协商 | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| POLICYTYPE | 策略类型 | 对端协商 | required | 无 | 枚举类型。 |
| PRIORITY | 全局优先级 | 对端协商 | optional | 4294967295 | 整数类型，取值范围为1～4294967295。值越小优先级越高。 |
| POLICYNAME | 策略名称 | 对端协商 | conditional | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| FLOWFILTERNAME | 流过滤器名称 | 对端协商 | conditional | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| RULERANGE | 规则生效范围 | global_planned | conditional | ALL | 枚举类型。 |
| RULESPECTYPE | 规则规格类型 | global_planned | optional | DEFAULT | 枚举类型。 |
| NWDAFEVENTS | NWDAF数据分析事件 | global_planned | optional | NULL | 枚举类型。 |
| IPERULEDELYSW | 智能规则传递开关 | global_planned | conditional | DISABLE | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-108002

**md：`WSFD-108002/WSFD-108002 基于预定义规则的分流策略控制参考信息_28860592.md`**
- 操作步骤上下文（±2 行原文）：
  L15:
    > - [**ADD PNFDNAI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端DNAI信息管理/增加对端NF的DNAI信息（ADD PNFDNAI）_09652965.md)
    > - [**ADD ULCLPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/ULCL属性/增加ULCL属性（ADD ULCLPROP）_16935565.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)

**md：`WSFD-108002/激活基于预定义规则的分流策略控制_28860590.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 规则名称（RULENAME） | testrule | 全网规划 | 配置UL CL分流rule以及和App ID的绑定关系。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略类型（POLICYTYPE） | ULCL | 本端规划 | 配置UL CL分流rule以及和App ID的绑定关系。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略名称（POLICYNAME） | testulclpropname | 本端规划 | 配置UL CL分流rule以及和App ID的绑定关系。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 流过滤器名称（FLOWFILTERNAME） | ulcl | 与对端协商 | 配置UL CL分流rule以及和App ID的绑定关系。 |
- 任务示例脚本（该命令行）：
  `ADD RULE:RULENAME="testrule",POLICYTYPE=ULCL, POLICYNAME="testulclpropname", FLOWFILTERNAME="ulcl";`
  `ADD RULE:RULENAME="testrule",POLICYTYPE=ULCL, POLICYNAME="testulclpropname", FLOWFILTERNAME="ulcl";`
  `ADD RULE:RULENAME="testrule",POLICYTYPE=ULCL, POLICYNAME="testulclpropname", FLOWFILTERNAME="ulcl";`
- 操作步骤上下文（±2 行原文）：
  L80:
    >       [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)
    >     c. 配置ULCL分流策略rule。
    >       [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    >     d. 配置ULCL属性的用户模板。
    >       [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
  L127:
    > ADD FLOWFILTER: FLOWFILTERNAME="ulcl"; 
    > //配置ULCL分流策略rule。
    > ADD RULE:RULENAME="testrule",POLICYTYPE=ULCL, POLICYNAME="testulclpropname", FLOWFILTERNAME="ulcl"; 
    > //配置ULCL属性的用户模板，并将ULCL分流策略rule绑定至该模板。
    > ADD USERPROFILE:USERPROFILENAME="testuserprofilename", UPTYPE=ULCL; 
  L153:
    > ADD FLOWFILTER: FLOWFILTERNAME="ulcl"; 
    > //配置ULCL分流策略rule。
    > ADD RULE:RULENAME="testrule",POLICYTYPE=ULCL, POLICYNAME="testulclpropname", FLOWFILTERNAME="ulcl"; 
    > //配置ULCL属性的用户模板，并将ULCL分流策略rule绑定至该模板。
    > ADD USERPROFILE:USERPROFILENAME="testuserprofilename", UPTYPE=ULCL; 

### WSFD-223001

**md：`WSFD-223001/WSFD-223001 基于位置信息的分流策略控制参考信息_47717539.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - [**ADD PNFDNAI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端DNAI信息管理/增加对端NF的DNAI信息（ADD PNFDNAI）_09652965.md)
    > - [**ADD ULCLPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/ULCL属性/增加ULCL属性（ADD ULCLPROP）_16935565.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)

**md：`WSFD-223001/部署基于位置信息的分流策略控制（SMF）_53995959.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 规则名称（RULENAME） | testrule | 全网规划 | 配置UL CL分流rule以及和App ID的绑定关系 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略类型（POLICYTYPE） | ULCL | 本端规划 | 配置UL CL分流rule以及和App ID的绑定关系 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略名称（POLICYNAME） | testulclpropname | 本端规划 | 配置UL CL分流rule以及和App ID的绑定关系 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 流过滤器名称（FLOWFILTERNAME） | ulcl | 与对端协商 | 配置UL CL分流rule以及和App ID的绑定关系 |
- 任务示例脚本（该命令行）：
  `ADD RULE:RULENAME="testrule",POLICYTYPE=ULCL, POLICYNAME="testulclpropname", FLOWFILTERNAME="ulcl";`
- 操作步骤上下文（±2 行原文）：
  L53:
    > ADD FLOWFILTER: FLOWFILTERNAME="ulcl"; 
    > //配置ULCL分流策略rule。
    > ADD RULE:RULENAME="testrule",POLICYTYPE=ULCL, POLICYNAME="testulclpropname", FLOWFILTERNAME="ulcl"; 
    > //配置ULCL属性的用户模板，并将ULCL分流策略rule绑定至该模板。
    > ADD USERPROFILE:USERPROFILENAME="testuserprofilename", UPTYPE=ULCL; 

### WSFD-223003

**md：`WSFD-223003/WSFD-223003 基于漫游地动态签约的分流策略控制特性参考信息_52923849.md`**
- 操作步骤上下文（±2 行原文）：
  L22:
    > - [**ADD ULCLPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/ULCL属性/增加ULCL属性（ADD ULCLPROP）_16935565.md)
    > - [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)

**md：`WSFD-223003/部署基于漫游地动态签约的分流策略控制（PCF）_36539970.md`**
- 任务示例脚本（该命令行）：
  `ADD RULE:RULENAME="Rule_Dnn",TYPE=Amf Pcc Rule 5G,RELATION=AND;`
- 操作步骤上下文（±2 行原文）：
  L182:
    > 
    > ```
    > ADD RULE:RULENAME="Rule_Dnn",TYPE=Amf Pcc Rule 5G,RELATION=AND;
    > ADD RULECONDITIONGROUP:RULENAME="Rule_Dnn",CONDITIONGROUPNAME="CG_Special";
    > ADD RULENGACTION:RULENAME="Rule_Dnn",ACTIONNAME="AG_SpecialDnn";

**md：`WSFD-223003/部署基于漫游地动态签约的分流策略控制（SMF）_82779459.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 规则名称（RULENAME） | testrule | 全网规划 | 配置UL CL分流rule以及和App ID的绑定关系 |
  | [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略类型（POLICYTYPE） | ULCL | 本端规划 | 配置UL CL分流rule以及和App ID的绑定关系 |
  | [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略名称（POLICYNAME） | testulclpropname | 本端规划 | 配置UL CL分流rule以及和App ID的绑定关系 |
  | [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 流过滤器名称（FLOWFILTERNAME） | ulcl | 与对端协商 | 配置UL CL分流rule以及和App ID的绑定关系 |
- 任务示例脚本（该命令行）：
  `ADD RULE:RULENAME="testrule",POLICYTYPE=ULCL, POLICYNAME="testulclpropname", FLOWFILTERNAME="ulcl";`
- 操作步骤上下文（±2 行原文）：
  L56:
    >       [**ADD FLOWFILTER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)
    >     c. 配置ULCL分流策略rule。
    >       [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    >     d. 配置ULCL属性的用户模板。
    >       [**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
  L101:
    > ADD FLOWFILTER: FLOWFILTERNAME="ulcl"; 
    > //配置ULCL分流策略rule。
    > ADD RULE:RULENAME="testrule",POLICYTYPE=ULCL, POLICYNAME="testulclpropname", FLOWFILTERNAME="ulcl"; 
    > //配置ULCL属性的用户模板，并将ULCL分流策略rule绑定至该模板。
    > ADD USERPROFILE:USERPROFILENAME="testuserprofilename", UPTYPE=ULCL; 

### WSFD-223101

**md：`WSFD-223101/WSFD-223101 基于预定义规则的分流策略控制(4G)参考信息_11634944.md`**
- 操作步骤上下文（±2 行原文）：
  L15:
    > - [**ADD PNFDNAI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端DNAI信息管理/增加对端NF的DNAI信息（ADD PNFDNAI）_09652965.md)
    > - [**ADD ULCLPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/ULCL属性/增加ULCL属性（ADD ULCLPROP）_16935565.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)

**md：`WSFD-223101/部署基于预定义规则的分流策略控制(4G)（SMF）_11155006.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 规则名称（RULENAME） | testrule | 全网规划 | 配置UL CL分流rule以及和App ID的绑定关系 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略类型（POLICYTYPE） | ULCL | 本端规划 | 配置UL CL分流rule以及和App ID的绑定关系 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略名称（POLICYNAME） | testulclpropname | 本端规划 | 配置UL CL分流rule以及和App ID的绑定关系 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 流过滤器名称（FLOWFILTERNAME） | ulcl | 与对端协商 | 配置UL CL分流rule以及和App ID的绑定关系 |
- 任务示例脚本（该命令行）：
  `ADD RULE:RULENAME="testrule",POLICYTYPE=ULCL, POLICYNAME="testulclpropname", FLOWFILTERNAME="ulcl";`
- 操作步骤上下文（±2 行原文）：
  L60:
    >       [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)
    >     c. 配置ULCL分流策略rule。
    >       [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    >     d. 配置ULCL属性的用户模板。
    >       [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
  L106:
    > 
    > ```
    > ADD RULE:RULENAME="testrule",POLICYTYPE=ULCL, POLICYNAME="testulclpropname", FLOWFILTERNAME="ulcl";
    > ```
    > 

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L26:
    > - [**ADD USRPROFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD PCCPOLICYGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULEBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)

**md：`WSFD-109101/配置动态PCC功能_30805098.md`**
- 操作步骤上下文（±2 行原文）：
  L135:
    >   > 当配置了specific APN，在上报APN时，specific APN优先级最高，其次是别名APN、虚拟APN、真实APN。
    > 9. PCRF下发预定义规则时，需要在GGSN/PGW-C上配置预定义规则对应的本地业务规则。
    >   [**ADD RULE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > 10. **可选：**配置rule和DNAI关联。可选配置，将rule下发给指定DNAI的辅锚点PGW-U时需要配置。
    >   [**ADD RULEBINDDNAI**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/预定义规则DNAI绑定/增加预定义规则关联的DNAI（ADD RULEBINDDNAI）_27170471.md)

**md：`WSFD-109101/配置本地PCC功能_30805097.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 规则名称（RULENAME） | rule-test | 本端规划 | 增加rule。 |
  | [**ADD RULE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略类型（POLICYTYPE） | PCC | 本端规划 | 增加rule。 |
  | [**ADD RULE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略名称（POLICYNAME） | pccpolicy_group | 已配置数据中获取 | 增加rule。 |
  | [**ADD RULE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 规则生效范围（RULERANGE） | ALL | 全网规划 | PGW-C支持将规则下发给主锚点PGW-U+辅锚点PGW-U、主锚点PGW-U或辅锚点PGW-U。<br>此处以rule同时下发给主锚点PGW-U和辅锚点PGW-U为例。<br>rule只下发给主锚点PGW-U时，需设置为<br>“CENTRAL”<br>；rule只下发给辅锚点PGW-U时，需设置为<br>“LOCAL”<br>。 |
- 任务示例脚本（该命令行）：
  `ADD RULE:RULENAME="rule_test",POLICYTYPE=PCC,POLICYNAME="pccpolicy_group",RULERANGE=ALL;`
- 操作步骤上下文（±2 行原文）：
  L90:
    >       [**ADD PCCPOLICYGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    >     c. 配置本地静态规则
    >       [**ADD RULE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    >     d. **可选：**配置rule和DNAI关联。可选配置，将rule下发给指定DNAI的辅锚点PGW-U时需要配置。
    >       [**ADD RULEBINDDNAI**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/预定义规则DNAI绑定/增加预定义规则关联的DNAI（ADD RULEBINDDNAI）_27170471.md)
  L148:
    >   ```
    >   ```
    >   ADD RULE:RULENAME="rule_test",POLICYTYPE=PCC,POLICYNAME="pccpolicy_group",RULERANGE=ALL;
    >   ```
    > 5. 配置业务策略组合。如配置的Userprofile仅下发给辅锚点PGW-U，则需要将“PROFILERANGE”设置为“LOCAL”；仅下发给主锚点PGW-U则设置为“CENTRAL”。

**md：`WSFD-109101/WSFD-109101 PCC基本功能（5G）参考信息_72466541.md`**
- 操作步骤上下文（±2 行原文）：
  L17:
    > - [**ADD USRPROFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**SET APNPCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    > - [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD APNUSRPROFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**ADD GUAMI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/本局信息管理/AMF/AMF全局标识符管理/增加AMF全局标识（ADD GUAMI）_09653726.md)

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 规则名称（RULENAME） | rule_test | 本端规划 | 存在多条数据时，该参数+策略类型不能完全相同。 |
  | [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略类型（POLICYTYPE） | PCC | 本端规划 | 需根据业务策略选择相应的策略类型。 |
  | [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 全局优先级（PRIORITY） | 10 | 本端规划 | 值越小，优先级越高。 |
  | [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略名称（POLICYNAME） | pccpolicygrp_01 | 已配置数据中获取 | 使用<br>[**ADD PCCPOLICYGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)<br>定义的PCCPOLICYGRPNM。 |
  | [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 规则生效范围（RULERANGE） | ALL | 全网规划 | SMF支持将规则下发给主锚点UPF+辅锚点UPF、主锚点UPF或辅锚点UPF。<br>此处以rule同时下发给主锚点UPF和辅锚点UPF为例。<br>rule只下发给主锚点UPF时，需设置为<br>“CENTRAL”<br>；rule只下发给辅锚点UPF时，需设置为<br>“LOCAL”<br>。 |
- 任务示例脚本（该命令行）：
  `ADD RULE:RULENAME="rule_test",POLICYTYPE=PCC,POLICYNAME="pccpolicy_group",RULERANGE=ALL;`
- 操作步骤上下文（±2 行原文）：
  L173:
    >       [**ADD PCCPOLICYGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    >     12. **可选：**配置SMF上的本地rule。用于动态PCC时PCF下发预定义规则，或本地PCC时的静态规则。
    >       [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    >     13. 将rule下发给指定DNAI的辅锚点UPF时，配置rule和DNAI关联。
    >       [**ADD RULEBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/预定义规则DNAI绑定/增加预定义规则关联的DNAI（ADD RULEBINDDNAI）_27170471.md)
  L253:
    > ```
    > ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicy_group",URRGROUPNAME="urrgrp_01",FUPSESSIONEXC=ENABLE;
    > ADD RULE:RULENAME="rule_test",POLICYTYPE=PCC,POLICYNAME="pccpolicy_group",RULERANGE=ALL;
    > ```
    > 

**md：`WSFD-109101/相关概念_71770360.md`**
- 操作步骤上下文（±2 行原文）：
  L42:
    >   | 动态规则 | 用户的规则内容无法预先确定，需要根据用户访问业务时的协商结果由AF（应用服务器）或其他网元发送请求给PCF，请求建立动态规则的场景。 | - SMF和UPF无需本地配置该规则。<br>- PCF向SMF下发规则名称及具体规则内容，如QoS管理、计费控制策略等，SMF将其传递给UPF后，由UPF按照收到的规则对用户数据进行处理。 |
    >   | 预定义规则 | 需要对报文进行七层解析的业务或运营商预定义的业务，业务规划时针对用户的规则内容在用户激活前可以预先确定，如用户签约套餐中包含指定APP的免费流量等。 | - PCF和SMF上仅配置预定义规则的名称，UPF上配置该预定义规则的名称及具体的规则内容，如QoS管理、计费控制策略等。<br>- PCF仅向SMF下发规则名称，SMF将规则名称传递给UPF后，由UPF按照接收到的规则名称查找UPF本地配置的具体的规则内容，对用户数据进行处理。<br>- 预定义规则可以是一条规则，也可以是一组规则：- 如果为一条规则，则预定义规则名称对应SMF/UPF上本地配置的Rule的名称。<br>- 如果为一组规则，则预定义规则名称对应SMF/UPF上本地配置的UserProfile名称。 |
    >   SMF上可以有多个动态规则或预定义规则，每个规则都对应着一个优先级，该优先级采用全局规划。优先级值越小，优先级越高。动态规则的优先级由PCF下发给SMF，预定义规则的全局优先级通过 [**ADD RULE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) 命令中的 “PRIORITY” 配置。
    >   当一个SDF同时满足多个规则时，优先使用高优先级的规则。当优先级值相同时，动态规则的优先级高于预定义规则的优先级。
    > - 使用本地PCC时的规则

### WSFD-109102

**md：`WSFD-109102/WSFD-109102 ADC基本功能参考信息_92582138.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > 

**md：`WSFD-109102/激活ADC基本功能_92582136.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 规则名称（RULENAME） | rule_test | 本端规划 | 存在多条数据时，该参数+策略类型不能完全相同。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略类型（POLICYTYPE） | ADC | 本端规划 | 需根据业务策略选择相应的策略类型。 |
- 任务示例脚本（该命令行）：
  `ADD RULE:RULENAME="rule_test",POLICYTYPE=ADC;`
- 操作步骤上下文（±2 行原文）：
  L54:
    > 3. PCRF/PCF要下发应用Start和Stop的两个Event Trigger，当PCRF/PCF不通过动态规则下发appid时，请执行本步骤。
    >     a. **可选：**配置SMF上的本地rule。
    >       [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    >     b. **可选：**配置SMF上的UserProfile，将本地rule绑定到UserProfile上。
    >           1. 配置UserProfile。
  L92:
    > 
    > ```
    > ADD RULE:RULENAME="rule_test",POLICYTYPE=ADC;
    > ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC;
    > ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";

**md：`WSFD-109102/调测ADC基本功能_92582137.md`**
- 操作步骤上下文（±2 行原文）：
  L67:
    >       PCF通过预定义规则下发APP_STA/APP_STO时，UPF/SMF/PCF上的规则标识必须一致。
    >           - 是，请执行[步骤 9](#ZH-CN_OPI_0292582137__step114691314193316)。
    >           - 否，请执行[**RMV RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/删除用户模板和规则的绑定关系（RMV RULEBINDING）_09897217.md)命令和[**RMV RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/删除规则（RMV RULE）_09897203.md)后重新执行[**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)和[**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)命令，然后重新执行[步骤 4](#ZH-CN_OPI_0292582137__step2056531835011)。
    > 9. 请联系华为技术支持工程师。
    >     a. 重新执行上述步骤并保存报文。

### WSFD-109103

**md：`WSFD-109103/WSFD-109103 IPv6 SA参考信息_78881328.md`**
- 操作步骤上下文（±2 行原文）：
  L15:
    > - [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    > - [**MOD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_09897174.md)/[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)

**md：`WSFD-109103/调测IPv6 SA_78881327.md`**
- 操作步骤上下文（±2 行原文）：
  L57:
    >     c. 执行 [**LST RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/查询规则（LST RULE）_09897204.md) 命令，检查Rule配置是否正确。
    >           - 是，请执行[步骤 7](#ZH-CN_OPI_0278881327__step114691314193316)。
    >           - 否，请执行[**RMV RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/删除用户模板和规则的绑定关系（RMV RULEBINDING）_09897217.md)命令和[**RMV RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/删除规则（RMV RULE）_09897203.md)后重新执行[**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)和[**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)命令，然后再执行[步骤 4](#ZH-CN_OPI_0278881327__step2056531835011)。
    > 7. 请联系华为技术支持工程师。
    >     a. 重新执行上述步骤并保存报文。

### WSFD-109107

**md：`WSFD-109107/WSFD-109107 业务触发的QoS保证参考信息_85397060.md`**
- 操作步骤上下文（±2 行原文）：
  L15:
    > - [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)
    > - [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)

**md：`WSFD-109107/激活业务触发的QoS保证_85397058.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 规则名称（RULENAME） | rule_test | 本端规划 | 存在多条数据时，该参数+策略类型不能完全相同。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略类型（POLICYTYPE） | PCC | 本端规划 | “POLICYTYPE”<br>设置为<br>“PCC”<br>时，<br>“POLICYNAME”<br>使用<br>[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)<br>定义的PCCPOLICYGRPNM。<br>“POLICYTYPE”<br>设置为<br>“QOS”<br>时，<br>“POLICYNAME”<br>使用<br>[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)<br>定义的QOSPROPNAME。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略名称（POLICYNAME） | pccpolicygrp_01 | 已配置数据中获取 | “POLICYTYPE”<br>设置为<br>“PCC”<br>时，<br>“POLICYNAME”<br>使用<br>[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)<br>定义的PCCPOLICYGRPNM。<br>“POLICYTYPE”<br>设置为<br>“QOS”<br>时，<br>“POLICYNAME”<br>使用<br>[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)<br>定义的QOSPROPNAME。 |
- 任务示例脚本（该命令行）：
  `ADD RULE:RULENAME="rule_test",POLICYTYPE=PCC,POLICYNAME="pccpolicy_group";`
  `ADD RULE:RULENAME="rule_test",POLICYTYPE=QOS,POLICYNAME="qosprop_501";`
- 操作步骤上下文（±2 行原文）：
  L78:
    >   [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > 5. 配置SMF上的本地rule。
    >   [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    >     - 规则通过PCC策略组绑定QoS属性时，“POLICYTYPE”设置为“PCC”，“POLICYNAME”使用[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)命令配置的“PCCPOLICYGRPNM”参数值。
    >     - 规则直接绑定QoS属性时，“POLICYTYPE”设置为“QOS”“POLICYNAME”使用[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)命令配置的“QOSPROPNAME”参数值。
  L140:
    > ```
    > ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicy_group",QOSPROPNAME="qosprop_501";
    > ADD RULE:RULENAME="rule_test",POLICYTYPE=PCC,POLICYNAME="pccpolicy_group";
    > ```
    > 
  L146:
    > 
    > ```
    > ADD RULE:RULENAME="rule_test",POLICYTYPE=QOS,POLICYNAME="qosprop_501";
    > ```
    > 

### WSFD-211005

**md：`WSFD-211005/WSFD-211005 基于业务感知的带宽控制参考信息_79619228.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)

**md：`WSFD-211005/激活基于业务感知的带宽控制_79619226.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 规则名称（RULENAME） | rule_test | 本端规划 | 存在多条数据时，该参数+策略类型不能完全相同。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略类型（POLICYTYPE） | BWM | 本端规划 | 使用样例值。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 全局优先级（PRIORITY） | 10 | 本端规划 | 值越小，优先级越高。 |
- 任务示例脚本（该命令行）：
  `ADD RULE: RULENAME="rule_test", POLICYTYPE=BWM, PRIORITY=10;`
- 操作步骤上下文（±2 行原文）：
  L46:
    > 
    > 1. 配置SMF上的本地rule。用于动态PCC时PCF下发预定义规则，或本地PCC时的静态规则。
    >   [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    >   规则用于带宽控制时， “策略类型（POLICYTYPE）” 设置为 “BWM” 。
    > 2. 配置SMF上的UserProfile，将本地rule绑定到UserProfile上。用于动态PCC时PCF下发预定义规则组，或本地PCC时的静态规则组。
  L72:
    > 
    > ```
    > ADD RULE: RULENAME="rule_test", POLICYTYPE=BWM, PRIORITY=10;
    > ```
    > 

### WSFD-211009

**md：`WSFD-211009/WSFD-211009 基于业务累计流量的策略控制参考信息_27915158.md`**
- 操作步骤上下文（±2 行原文）：
  L15:
    > - [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    > - [**MOD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_09897174.md)/[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)

**md：`WSFD-211009/激活基于业务累计流量的策略控制_27915156.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 规则名称（RULENAME） | rule_test2 | 本端规划 | 存在多条数据时，该参数+策略类型不能完全相同。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略类型（POLICYTYPE） | PCC | 本端规划 | 使用样例值。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 全局优先级（PRIORITY） | 20 | 本端规划 | 仅对PCC用户生效。优先级值越小，优先级越高。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略名称（POLICYNAME） | pccpolicygrp_01 | 已配置数据中获取 | 使用<br>[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)<br>命令定义的PCC策略组名称。 |
- 任务示例脚本（该命令行）：
  `ADD RULE:RULENAME="rule_test2",POLICYTYPE=PCC,PRIORITY=20,POLICYNAME="pccpolicygrp_01";`
- 操作步骤上下文（±2 行原文）：
  L57:
    >   [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > 6. 配置预定义规则。
    >   [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > 7. 配置预定义规则组。
    >     a. 创建用户模板。
  L93:
    > 
    > ```
    > ADD RULE:RULENAME="rule_test2",POLICYTYPE=PCC,PRIORITY=20,POLICYNAME="pccpolicygrp_01";
    > ```
    > 

### WSFD-011306

**md：`WSFD-011306/WSFD-011306 Radius功能参考信息_15542176.md`**
- 操作步骤上下文（±2 行原文）：
  L44:
    > - **[MOD RDSSVRGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器组/修改Radius服务器组（MOD RDSSVRGRP）_09896731.md)**
    > - **[**ADD SPECIFICAPNVAL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/指定上报的APN/增加用户APN与消息交互使用APN的映射关系（ADD SPECIFICAPNVAL）_09653027.md)**
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - **[ADD RULEBINDING](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)**

**md：`WSFD-011306/配置业务触发RADIUS功能_33000859.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 规则名称（RULENAME） | rule_test1 | 本端规划 | 用于对匹配上该规则的业务进行业务触发RADIUS动作，需要与UPF/PGW-U上规划的规则保持一致。 |
  | [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略类型（POLICYTYPE） | SRV_TRIGGER | 本端规划 | 用于对匹配上该规则的业务进行业务触发RADIUS动作，需要与UPF/PGW-U上规划的规则保持一致。 |
  | [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 全局优先级（PRIORITY） | 10 | 本端规划 | 用于对匹配上该规则的业务进行业务触发RADIUS动作，需要与UPF/PGW-U上规划的规则保持一致。 |
- 任务示例脚本（该命令行）：
  `ADD RULE: RULENAME="rule_test1", POLICYTYPE=SRV_TRIGGER, PRIORITY=50;`
- 操作步骤上下文（±2 行原文）：
  L59:
    >   **[**ADD FLOWFILTER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)**
    > 4. 配置业务规则。
    >   [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > 5. 配置业务策略组合。
    >     a. 配置UserProfile模板。
  L96:
    > 
    > ```
    > ADD RULE: RULENAME="rule_test1", POLICYTYPE=SRV_TRIGGER, PRIORITY=50;
    > ```
    > 

### WSFD-011201

**md：`WSFD-011201/配置离线计费的费率标识（GGSN_SGW-C_PGW-C）_98555879.md`**
- 数据规划表（该命令的参数行）：
  | **ADD RULE** | 规则名称（RULENAME） | Rule001 | 本端规划 | 配置内容计费使用的Rule。 |
  | **ADD RULE** | 策略类型（POLICYTYPE） | PCC | 本端规划 | 配置内容计费使用的Rule。 |
  | **ADD RULE** | 策略名称（POLICYNAME） | cg-test | 已配置数据中获取 | 配置内容计费使用的Rule。 |
  | **ADD RULE** | 优先级（PRIORITY） | 110 | 本端规划 | 配置内容计费使用的Rule。 |
- 任务示例脚本（该命令行）：
  `ADD RULE: RULENAME="Rule001", POLICYTYPE=PCC, PRIORITY=110, POLICYNAME="cg-test";`
- 操作步骤上下文（±2 行原文）：
  L99:
    >             **ADD PCCPOLICYGRP**
    >           b. 配置Rule，将PCC策略组绑定到Rule上。
    >             **ADD RULE**
    >     4. 配置绑定Rule的UserProfile。
    >           a. 配置UserProfile。
  L162:
    >   ```
    >   ADD PCCPOLICYGRP: PCCPOLICYGRPNM="cg-test", URRGROUPNAME="urrgroup1";
    >   ADD RULE: RULENAME="Rule001", POLICYTYPE=PCC, PRIORITY=110, POLICYNAME="cg-test";
    >   ```
    >   //配置内容计费的UserProfile。

### WSFD-011206

**md：`WSFD-011206/WSFD-011206 支持融合计费参考信息_74013176.md`**
- 操作步骤上下文（±2 行原文）：
  L26:
    > - [**ADD URRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)
    > - [**SET URRGRPBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/设置用户模板的计费属性绑定关系（SET URRGRPBINDING）_09897209.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)

**md：`WSFD-011206/配置融合计费费率标识_93360308.md`**
- 数据规划表（该命令的参数行）：
  | **ADD RULE** | 规则名称（RULENAME） | Rule001_dns<br>Rule002_IMS<br>Rule003_any<br>Rule003_any_IPv6 | 本端规划 | 配置规则，并绑定已配置的PCC策略组。<br>SMF、UPF上RULENAME以及RULE下配置的POLICYTYPE、POLICYNAME需要保持一致。 |
  | **ADD RULE** | 策略类型（POLICYTYPE） | PCC | 固定取值 | - |
  | **ADD RULE** | 全局优先级（PRIORITY） | 100<br>110<br>65000<br>65010 | 本端规划 | 取值越小，优先级越高。 |
  | **ADD RULE** | 策略名称（POLICYNAME） | pccpolicy_URL<br>pccpolicy_IMS<br>pccpolicy_any | 已配置数据中获取 | 使用<br>**ADD PCCPOLICYGRP**<br>命令定义的<br>“PCCPOLICYGRPNM”<br>。 |
- 任务示例脚本（该命令行）：
  `ADD RULE: RULENAME="Rule001_dns", POLICYTYPE=PCC, PRIORITY=100, POLICYNAME="pccpolicy_URL";`
  `ADD RULE: RULENAME="Rule002_IMS", POLICYTYPE=PCC, PRIORITY=110, POLICYNAME="pccpolicy_IMS";`
  `ADD RULE: RULENAME="Rule003_any", POLICYTYPE=PCC, PRIORITY=65000, POLICYNAME="pccpolicy_any";`
  `ADD RULE: RULENAME="Rule003_any_IPv6", POLICYTYPE=PCC, PRIORITY=65010, POLICYNAME="pccpolicy_any";`
- 操作步骤上下文（±2 行原文）：
  L96:
    >             **ADD PCCPOLICYGRP**
    >           b. 配置Rule，将PCC策略组绑定到Rule上。
    >             **ADD RULE**
    >     3. 配置UserProfile，将Rule绑定到UserProfile上。
    >           a. 配置UserProfile。
  L175:
    > 
    > ```
    > ADD RULE: RULENAME="Rule001_dns", POLICYTYPE=PCC, PRIORITY=100, POLICYNAME="pccpolicy_URL";
    > ADD RULE: RULENAME="Rule002_IMS", POLICYTYPE=PCC, PRIORITY=110, POLICYNAME="pccpolicy_IMS";
    > ADD RULE: RULENAME="Rule003_any", POLICYTYPE=PCC, PRIORITY=65000, POLICYNAME="pccpolicy_any";
  L176:
    > ```
    > ADD RULE: RULENAME="Rule001_dns", POLICYTYPE=PCC, PRIORITY=100, POLICYNAME="pccpolicy_URL";
    > ADD RULE: RULENAME="Rule002_IMS", POLICYTYPE=PCC, PRIORITY=110, POLICYNAME="pccpolicy_IMS";
    > ADD RULE: RULENAME="Rule003_any", POLICYTYPE=PCC, PRIORITY=65000, POLICYNAME="pccpolicy_any";
    > ADD RULE: RULENAME="Rule003_any_IPv6", POLICYTYPE=PCC, PRIORITY=65010, POLICYNAME="pccpolicy_any";

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L41:
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD FESTIVAL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/节假日/增加计费节假日表（ADD FESTIVAL）_09896827.md)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L41:
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD FESTIVAL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/节假日/增加计费节假日表（ADD FESTIVAL）_09896827.md)

**md：`WSFD-109001/配置在线计费的费率标识_95923388.md`**
- 数据规划表（该命令的参数行）：
  | **ADD RULE** | 规则名称（RULENAME） | Rule002 | 本端规划 | 配置内容计费使用的Rule。 |
  | **ADD RULE** | 策略类型（POLICYTYPE） | PCC | 本端规划 | 配置内容计费使用的Rule。 |
  | **ADD RULE** | 策略名称（POLICYNAME） | cg-test | 已配置数据中获取 | 配置内容计费使用的Rule。 |
  | **ADD RULE** | 优先级（PRIORITY） | 120 | 本端规划 | 配置内容计费使用的Rule。 |
- 任务示例脚本（该命令行）：
  `ADD RULE: RULENAME="Rule002", POLICYTYPE=PCC, POLICYNAME="cg-test",PRIORITY=120;`
- 操作步骤上下文（±2 行原文）：
  L103:
    >             **ADD PCCPOLICYGRP**
    >           b. 配置Rule，将PCC策略组绑定到Rule上。
    >             **ADD RULE**
    >     4. 配置绑定Rule的UserProfile。
    >           a. 配置UserProfile。
  L167:
    >   ```
    >   ADD PCCPOLICYGRP: PCCPOLICYGRPNM="cg-test", URRGROUPNAME="urrgroup001";
    >   ADD RULE: RULENAME="Rule002", POLICYTYPE=PCC, POLICYNAME="cg-test",PRIORITY=120;
    >   ```
    >   //配置内容计费的UserProfile。

### WSFD-109007

**md：`WSFD-109007/WSFD-109007 支持事件计费参考信息_74112323.md`**
- 操作步骤上下文（±2 行原文）：
  L17:
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)
    > - [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)

**md：`WSFD-109007/配置事件计费功能_74112321.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | RULENAME（规则名称） | rule-test | 本端规划 | 配置事件计费使用的Rule。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | POLICYTYPE（策略类型） | PCC | 本端规划 | 配置事件计费使用的Rule。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | POLICYNAME（策略名称） | cg-test | 本端规划 | 配置事件计费使用的Rule。 |
- 任务示例脚本（该命令行）：
  `ADD RULE: RULENAME="rule-test", POLICYTYPE=PCC, POLICYNAME="cg-test";`
- 操作步骤上下文（±2 行原文）：
  L84:
    >       [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    >     b. 配置Rule，将PCC策略组绑定到Rule上。
    >       [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > 6. 配置融合计费模板或在线计费模板。
    >     - 配置融合计费模板。
  L138:
    > ```
    > ADD PCCPOLICYGRP: PCCPOLICYGRPNM="cg-test", URRGROUPNAME="urrgroup1";
    > ADD RULE: RULENAME="rule-test", POLICYTYPE=PCC, POLICYNAME="cg-test";
    > ```
    > 

### WSFD-201207

**md：`WSFD-201207/WSFD-201207 语音PCF_PCRF故障Bypass参考信息_85304300.md`**
- 操作步骤上下文（±2 行原文）：
  L44:
    > **[LST PCCPOLICYGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/查询PCC策略组（LST PCCPOLICYGRP）_09897176.md)**
    > 
    > [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > 
    > **[MOD RULE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/修改规则（MOD RULE）_09897202.md)**

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（Gx接口）_60552093.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 规则名称（RULENAME） | rule_ims_signaling | 本端规划 | 配置业务策略规则。存在多条数据时，规则名称+策略类型不能完全相同。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略类型（POLICYTYPE） | PCC | 本端规划 | - “POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)定义的PCCPOLICYGRPNM。<br>- “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)定义的QOSPROPNAME。<br>- 配置“PRIORITY”时需要注意：PCRF下发的用于创建语音专有承载的规则的优先级高于本地配置的用于创建语音专有承载的规则；本地配置的用于创建语音/专有承载的规则优先级高于PCRF下发的any to any的动态规则和本地配置的any to any的预定义规则。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 全局优先级（PRIORITY） | 65535 | 与对端协商 | - “POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)定义的PCCPOLICYGRPNM。<br>- “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)定义的QOSPROPNAME。<br>- 配置“PRIORITY”时需要注意：PCRF下发的用于创建语音专有承载的规则的优先级高于本地配置的用于创建语音专有承载的规则；本地配置的用于创建语音/专有承载的规则优先级高于PCRF下发的any to any的动态规则和本地配置的any to any的预定义规则。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略名称（POLICYNAME） | pccpolicygrp_signaling | 已配置数据中获取 | - “POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)定义的PCCPOLICYGRPNM。<br>- “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)定义的QOSPROPNAME。<br>- 配置“PRIORITY”时需要注意：PCRF下发的用于创建语音专有承载的规则的优先级高于本地配置的用于创建语音专有承载的规则；本地配置的用于创建语音/专有承载的规则优先级高于PCRF下发的any to any的动态规则和本地配置的any to any的预定义规则。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 规则名称（RULENAME） | rule_ims_voice | 本端规划 | 配置业务策略规则。存在多条数据时，规则名称+策略类型不能完全相同。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略类型（POLICYTYPE） | PCC | 本端规划 | - “POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)定义的PCCPOLICYGRPNM。<br>- “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)定义的QOSPROPNAME。<br>- 配置“PRIORITY”时需要注意：PCF下发的用于创建语音专有QoS Flow/专有承载的规则的优先级高于本地配置的用于创建语音专有QoS Flow/专有承载的规则；本地配置的用于创建语音专有QoS Flow/专有承载的规则优先级高于PCF下发的any to any的动态规则和本地配置的any to any的预定义规则。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 全局优先级（PRIORITY） | 65535 | 与对端协商 | - “POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)定义的PCCPOLICYGRPNM。<br>- “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)定义的QOSPROPNAME。<br>- 配置“PRIORITY”时需要注意：PCF下发的用于创建语音专有QoS Flow/专有承载的规则的优先级高于本地配置的用于创建语音专有QoS Flow/专有承载的规则；本地配置的用于创建语音专有QoS Flow/专有承载的规则优先级高于PCF下发的any to any的动态规则和本地配置的any to any的预定义规则。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略名称（POLICYNAME） | pccpolicygrp_voice | 已配置数据中获取 | - “POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)定义的PCCPOLICYGRPNM。<br>- “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)定义的QOSPROPNAME。<br>- 配置“PRIORITY”时需要注意：PCF下发的用于创建语音专有QoS Flow/专有承载的规则的优先级高于本地配置的用于创建语音专有QoS Flow/专有承载的规则；本地配置的用于创建语音专有QoS Flow/专有承载的规则优先级高于PCF下发的any to any的动态规则和本地配置的any to any的预定义规则。 |
- 任务示例脚本（该命令行）：
  `ADD RULE:RULENAME="rule_ims_signaling", POLICYTYPE=PCC, PRIORITY=65535, POLICYNAME="pccpolicygrp_signaling";`
  `ADD RULE:RULENAME="rule_ims_voice", POLICYTYPE=PCC, PRIORITY=65535, POLICYNAME="pccpolicygrp_voice";`
  `ADD RULE:RULENAME="rule_ims_voice", POLICYTYPE=PCC, PRIORITY=65535, POLICYNAME="pccpolicygrp_voice";`
- 操作步骤上下文（±2 行原文）：
  L200:
    >       [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    >     d. 配置业务策略规则。
    >       [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    >     e. **可选：**配置用户模板。
    >       > **说明**
  L231:
    >       [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    >     e. 配置业务策略规则。
    >       [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    >     f. **可选：**配置用户模板。
    >       > **说明**
  L321:
    > 
    >       ```
    >       ADD RULE:RULENAME="rule_ims_signaling", POLICYTYPE=PCC, PRIORITY=65535, POLICYNAME="pccpolicygrp_signaling";
    >       ```
    >       //配置用户模板。

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（N7接口）_32852169.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 规则名称（RULENAME） | rule_ims_signaling | 本端规划 | 配置业务策略规则。存在多条数据时，规则名称+策略类型不能完全相同。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略类型（POLICYTYPE） | PCC | 本端规划 | - “POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)定义的PCCPOLICYGRPNM。<br>- “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)定义的QOSPROPNAME。<br>- 配置“PRIORITY”时需要注意：PCF下发的用于创建语音专有QoS Flow/专有承载的规则的优先级高于本地配置的用于创建语音专有QoS Flow/专有承载的规则；本地配置的用于创建语音专有QoS Flow/专有承载的规则优先级高于PCF下发的any to any的动态规则和本地配置的any to any的预定义规则。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 全局优先级（PRIORITY） | 65535 | 与对端协商 | - “POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)定义的PCCPOLICYGRPNM。<br>- “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)定义的QOSPROPNAME。<br>- 配置“PRIORITY”时需要注意：PCF下发的用于创建语音专有QoS Flow/专有承载的规则的优先级高于本地配置的用于创建语音专有QoS Flow/专有承载的规则；本地配置的用于创建语音专有QoS Flow/专有承载的规则优先级高于PCF下发的any to any的动态规则和本地配置的any to any的预定义规则。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略名称（POLICYNAME） | pccpolicygrp_signaling | 已配置数据中获取 | - “POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)定义的PCCPOLICYGRPNM。<br>- “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)定义的QOSPROPNAME。<br>- 配置“PRIORITY”时需要注意：PCF下发的用于创建语音专有QoS Flow/专有承载的规则的优先级高于本地配置的用于创建语音专有QoS Flow/专有承载的规则；本地配置的用于创建语音专有QoS Flow/专有承载的规则优先级高于PCF下发的any to any的动态规则和本地配置的any to any的预定义规则。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 规则名称（RULENAME） | rule_ims_voice | 本端规划 | 配置业务策略规则。存在多条数据时，规则名称+策略类型不能完全相同。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略类型（POLICYTYPE） | PCC | 本端规划 | - “POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)定义的PCCPOLICYGRPNM。<br>- “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)定义的QOSPROPNAME。<br>- 配置“PRIORITY”时需要注意：PCF下发的用于创建语音专有QoS Flow/专有承载的规则的优先级高于本地配置的用于创建语音专有QoS Flow/专有承载的规则；本地配置的用于创建语音专有QoS Flow/专有承载的规则优先级高于PCF下发的any to any的动态规则和本地配置的any to any的预定义规则。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 全局优先级（PRIORITY） | 65535 | 与对端协商 | - “POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)定义的PCCPOLICYGRPNM。<br>- “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)定义的QOSPROPNAME。<br>- 配置“PRIORITY”时需要注意：PCF下发的用于创建语音专有QoS Flow/专有承载的规则的优先级高于本地配置的用于创建语音专有QoS Flow/专有承载的规则；本地配置的用于创建语音专有QoS Flow/专有承载的规则优先级高于PCF下发的any to any的动态规则和本地配置的any to any的预定义规则。 |
  | [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略名称（POLICYNAME） | pccpolicygrp_voice | 已配置数据中获取 | - “POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)定义的PCCPOLICYGRPNM。<br>- “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)定义的QOSPROPNAME。<br>- 配置“PRIORITY”时需要注意：PCF下发的用于创建语音专有QoS Flow/专有承载的规则的优先级高于本地配置的用于创建语音专有QoS Flow/专有承载的规则；本地配置的用于创建语音专有QoS Flow/专有承载的规则优先级高于PCF下发的any to any的动态规则和本地配置的any to any的预定义规则。 |
- 任务示例脚本（该命令行）：
  `ADD RULE:RULENAME="rule_ims_signaling", POLICYTYPE=PCC, PRIORITY=65535, POLICYNAME="pccpolicygrp_signaling";`
  `ADD RULE:RULENAME="rule_ims_voice", POLICYTYPE=PCC, PRIORITY=65535, POLICYNAME="pccpolicygrp_voice";`
  `ADD RULE:RULENAME="rule_ims_voice", POLICYTYPE=PCC, PRIORITY=65535, POLICYNAME="pccpolicygrp_voice";`
- 操作步骤上下文（±2 行原文）：
  L219:
    >       [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    >     d. 配置业务策略规则。
    >       [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    >     e. **可选：**配置用户模板。
    >       > **说明**
  L250:
    >       [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    >     e. 配置业务策略规则。
    >       [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    >     f. **可选：**配置用户模板。
    >       > **说明**
  L349:
    > 
    >       ```
    >       ADD RULE:RULENAME="rule_ims_signaling", POLICYTYPE=PCC, PRIORITY=65535, POLICYNAME="pccpolicygrp_signaling";
    >       ```
    >       //配置用户模板。

## ④ 自动比对
- 命令真相参数（9）：['FLOWFILTERNAME', 'IPERULEDELYSW', 'NWDAFEVENTS', 'POLICYNAME', 'POLICYTYPE', 'PRIORITY', 'RULENAME', 'RULERANGE', 'RULESPECTYPE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 6, '本端规划': 45, '与对端协商': 8, '已配置数据中获取': 11, '固定取值': 1}（多值→atom 应考虑 decision_driven）
