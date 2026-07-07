# 命令证据包：SET URRGRPBINDING
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/设置用户模板的计费属性绑定关系（SET URRGRPBINDING）_09897209.md`
> 用该命令的特性数：4

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于设置用户模板的计费属性绑定关系。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 如果UserProfile下不绑定默认计费属性，用户的数据包按全局计费属性计费，否则不计费。
- 该命令设定后的数据，需要通过LST USERPROFILE命令进行查看。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| USERPROFILENAME | 用户模板名称 | global_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| DFTURRGRPNAME | 缺省URR组名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/配置离线计费的费率标识（GGSN_SGW-C_PGW-C）_98555879.md`**
- 数据规划表（该命令的参数行）：
  | **SET URRGRPBINDING** | 用户模板名称（USERPROFILENAME） | up-test | 已配置数据中获取 | 将URR组绑定到UserProfile上。 |
  | **SET URRGRPBINDING** | 缺省URR组名称（DFTURRGRPNAME） | urrgroup1 | 已配置数据中获取 | 将URR组绑定到UserProfile上。 |
- 任务示例脚本（该命令行）：
  `SET URRGRPBINDING:USERPROFILENAME="up-test",DFTURRGRPNAME="urrgroup1";`
- 操作步骤上下文（±2 行原文）：
  L75:
    >             **ADD USERPROFILE**
    >           b. 绑定该UserProfile的缺省URR组。
    >             **SET URRGRPBINDING**
    >     3. 配置UserProfile绑定的UserProfile组及APN实例。
    >           a. 配置UserProfile组，将UserProfile绑定到UserProfile组上。
  L140:
    >   ```
    >   ADD USERPROFILE:USERPROFILENAME="up-test", UPTYPE=PCC;
    >   SET URRGRPBINDING:USERPROFILENAME="up-test",DFTURRGRPNAME="urrgroup1";
    >   ADD USRPROFGROUP:USERPROFGNAME="upg-test";
    >   ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";

### WSFD-011206

**md：`WSFD-011206/WSFD-011206 支持融合计费参考信息_74013176.md`**
- 操作步骤上下文（±2 行原文）：
  L25:
    > - [**SET GLBURRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/全局使用量上报规则组/设置全局使用量上报规则组（SET GLBURRGROUP）_09897187.md)
    > - [**ADD URRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)
    > - [**SET URRGRPBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/设置用户模板的计费属性绑定关系（SET URRGRPBINDING）_09897209.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)

**md：`WSFD-011206/配置融合计费费率标识_93360308.md`**
- 数据规划表（该命令的参数行）：
  | **SET URRGRPBINDING** | 用户模板名称（USERPROFILENAME） | userprofile001<br>userprofile002 | 本端规划 | 设置用户模板的计费属性绑定关系。如果UserProfile下不绑定默认计费属性，用户的数据包按全局计费属性计费，否则不计费。 |
  | **SET URRGRPBINDING** | 缺省URR组名称（DFTURRGRPNAME） | UrrGp_abnormal | 已配置数据中获取 | 指定缺省URR组名称，使用<br>**ADD URRGROUP**<br>命令配置生成。 |
- 任务示例脚本（该命令行）：
  `SET URRGRPBINDING:USERPROFILENAME="userprofile001",DFTURRGRPNAME="UrrGp_abnormal";`
  `SET URRGRPBINDING:USERPROFILENAME="userprofile002",DFTURRGRPNAME="UrrGp_abnormal";`
- 操作步骤上下文（±2 行原文）：
  L101:
    >             **ADD USERPROFILE**
    >           b. 绑定该UserProfile的缺省URR组，建议每个UserProfile都绑定缺省费率URR组。
    >             **SET URRGRPBINDING**
    >           c. 将Rule绑定到UserProfile上。
    >             **ADD RULEBINDING**
  L195:
    > 
    > ```
    > SET URRGRPBINDING:USERPROFILENAME="userprofile001",DFTURRGRPNAME="UrrGp_abnormal";
    > SET URRGRPBINDING:USERPROFILENAME="userprofile002",DFTURRGRPNAME="UrrGp_abnormal";
    > ```
  L196:
    > ```
    > SET URRGRPBINDING:USERPROFILENAME="userprofile001",DFTURRGRPNAME="UrrGp_abnormal";
    > SET URRGRPBINDING:USERPROFILENAME="userprofile002",DFTURRGRPNAME="UrrGp_abnormal";
    > ```
    > 

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > - [**SET GLBURRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/全局使用量上报规则组/设置全局使用量上报规则组（SET GLBURRGROUP）_09897187.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**SET URRGRPBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/设置用户模板的计费属性绑定关系（SET URRGRPBINDING）_09897209.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > - [**SET GLBURRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/全局使用量上报规则组/设置全局使用量上报规则组（SET GLBURRGROUP）_09897187.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**SET URRGRPBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/设置用户模板的计费属性绑定关系（SET URRGRPBINDING）_09897209.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)

**md：`WSFD-109001/配置在线计费的费率标识_95923388.md`**
- 数据规划表（该命令的参数行）：
  | **SET URRGRPBINDING** | 用户模板名称（USERPROFILENAME） | up-test | 已配置数据中获取 | 将URR组绑定到UserProfile上。 |
  | **SET URRGRPBINDING** | 缺省URR组名称（DFTURRGRPNAME） | urrgroup001 | 已配置数据中获取 | 将URR组绑定到UserProfile上。 |
- 任务示例脚本（该命令行）：
  `SET URRGRPBINDING:USERPROFILENAME="up-test",DFTURRGRPNAME="urrgroup001";`
- 操作步骤上下文（±2 行原文）：
  L79:
    >             **ADD USERPROFILE**
    >           b. 绑定该UserProfile的缺省URR组。
    >             **SET URRGRPBINDING**
    >     3. 配置UserProfile绑定的UserProfile组及APN实例。
    >           a. 配置UserProfile组，将UserProfile绑定到UserProfile组上。
  L144:
    >   ```
    >   ADD USERPROFILE:USERPROFILENAME="up-test", UPTYPE=PCC;
    >   SET URRGRPBINDING:USERPROFILENAME="up-test",DFTURRGRPNAME="urrgroup001";
    >   ADD USRPROFGROUP:USERPROFGNAME="upg-test";
    >   ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";

**md：`WSFD-109001/配置CCR触发场景_95923545.md`**
- 任务示例脚本（该命令行）：
  `SET URRGRPBINDING: USERPROFILENAME="up-test", DFTURRGRPNAME="urrgroup1";`
- 操作步骤上下文（±2 行原文）：
  L134:
    > 
    > ```
    > SET URRGRPBINDING: USERPROFILENAME="up-test", DFTURRGRPNAME="urrgroup1";
    > ```
    > 

## ④ 自动比对
- 命令真相参数（2）：['DFTURRGRPNAME', 'USERPROFILENAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 5, '本端规划': 1}（多值→atom 应考虑 decision_driven）
