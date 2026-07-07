# 命令证据包：ADD USRPROFGROUP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md`
> 用该命令的特性数：16

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于配置一个用户模板组。可使用该用户模板组绑定多个PccProfile和UserProfile，并将该用户模板组绑定到用户APN。用户激活时，可根据APN选择到用户模板组，从而选择可用策略。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为10000。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| USERPROFGNAME | 用户模板组名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-108002

**md：`WSFD-108002/WSFD-108002 基于预定义规则的分流策略控制参考信息_28860592.md`**
- 操作步骤上下文（±2 行原文）：
  L18:
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)

**md：`WSFD-108002/激活基于预定义规则的分流策略控制_28860590.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md) | 用户模板组名称（USERPROFGNAME） | ulcl_test | 本端规划 | 配置基于DNN UL CL分流的用户模板组，并将DNN绑定至该模板组 |
- 任务示例脚本（该命令行）：
  `ADD USRPROFGROUP:USERPROFGNAME="ulcl_test";`
- 操作步骤上下文（±2 行原文）：
  L89:
    >       [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     b. 配置用户模板组。
    >       [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    >     c. 将上述用户模板绑定至用户模板组。
    >       [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
  L132:
    > ADD RULEBINDING: USERPROFILENAME="testuserprofilename",RULENAME="testrule",POLICYTYPE=ULCL;
    > //配置用户模板组，并将ULCL属性的用户模板绑定至该模板组，再将模板组绑定至指定APN。
    > ADD USRPROFGROUP:USERPROFGNAME="ulcl_test";
    > ADD UPBINDUPG:USERPROFGNAME="ulcl_test",UPBINDTYPE=ULCL,USERPROFILENAME="testuserprofilename";
    > ADD APNUSRPROFG:APN="Huawei.com",USERPROFGNAME="ulcl_test";

### WSFD-223003

**md：`WSFD-223003/WSFD-223003 基于漫游地动态签约的分流策略控制特性参考信息_52923849.md`**
- 操作步骤上下文（±2 行原文）：
  L26:
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)

**md：`WSFD-223003/部署基于漫游地动态签约的分流策略控制（SMF）_82779459.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD USRPROFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md) | 用户模板组名称（USERPROFGNAME） | ulcl_test | 本端规划 | 配置基于专网业务DNN UL CL分流的用户模板组，并将DNN绑定至该模板组 |
- 任务示例脚本（该命令行）：
  `ADD USRPROFGROUP:USERPROFGNAME="ulcl_test";`
- 操作步骤上下文（±2 行原文）：
  L65:
    >       [**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    >     b. 配置用户模板组。
    >       [**ADD USRPROFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    >     c. 将上述用户模板绑定至用户模板组。
    >       [**ADD UPBINDUPG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
  L106:
    > ADD RULEBINDING: USERPROFILENAME="testuserprofilename",RULENAME="testrule";
    > //配置用户模板组，并将ULCL属性的用户模板绑定至该模板组，再将模板组绑定至指定APN。
    > ADD USRPROFGROUP:USERPROFGNAME="ulcl_test";
    > ADD UPBINDUPG:USERPROFGNAME="ulcl_test",UPBINDTYPE=ULCL,USERPROFILENAME="testuserprofilename";
    > ADD APNUSRPROFG:APN="dnn-ar",USERPROFGNAME="ulcl_test";

### WSFD-223101

**md：`WSFD-223101/WSFD-223101 基于预定义规则的分流策略控制(4G)参考信息_11634944.md`**
- 操作步骤上下文（±2 行原文）：
  L18:
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)

### WSFD-109202

**md：`WSFD-109202/WSFD-109202 会话类QOS保证参考信息_28258189.md`**
- 操作步骤上下文（±2 行原文）：
  L23:
    > - [**ADD PRER8REMARK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/PreR8 QoS配置/PreR8 Qos映射ToS_DSCP/增加Pre-R8 QoS到TOS_DSCP的映射规则（ADD PRER8REMARK）_09654400.md)
    > - **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)**
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)

**md：`WSFD-109202/激活会话类QOS保证（适用于GGSN）_28258187.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md) | USERPROFGNAME（用户模板组名称） | usrg | 本端规划 | 配置用户模板组User Profile Group。 |
- 任务示例脚本（该命令行）：
  `ADD USRPROFGROUP:USERPROFGNAME="usrg";`
- 操作步骤上下文（±2 行原文）：
  L92:
    >       [**ADD PRER8REMARK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/PreR8 QoS配置/PreR8 Qos映射ToS_DSCP/增加Pre-R8 QoS到TOS_DSCP的映射规则（ADD PRER8REMARK）_09654400.md)
    >     - 配置用户模板组User Profile Group。
    >       [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    >     - 将UserProfile绑定到用户模板组UserProfileGroup。
    >       [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
  L165:
    >   //配置UserProfile Group。
    >   ```
    >   ADD USRPROFGROUP:USERPROFGNAME="usrg";
    >   ```
    >   //将UserProfile绑定到UserProfileGroup。

**md：`WSFD-109202/激活会话类QOS保证（适用于SGW-C_PGW-C）_28344569.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md) | USERPROFGNAME (用户模板组名称) | usrg | 本端规划 | 配置用户模板组User Profile Group |
- 任务示例脚本（该命令行）：
  `ADD USRPROFGROUP:USERPROFGNAME="usrg";`
- 操作步骤上下文（±2 行原文）：
  L113:
    >       **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)**
    >     - 配置用户模板组User Profile Group。
    >       [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    >     - 将UserProfile绑定到用户模板组UserProfileGroup。
    >       [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
  L202:
    >   //配置UserProfile Group。
    >   ```
    >   ADD USRPROFGROUP:USERPROFGNAME="usrg";
    >   ```
    >   //将UserProfile绑定到UserProfileGroup。

### WSFD-109203

**md：`WSFD-109203/WSFD-109203 本地QOS控制参考信息_28258574.md`**
- 操作步骤上下文（±2 行原文）：
  L21:
    > - [**ADD PRER8REMARK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/PreR8 QoS配置/PreR8 Qos映射ToS_DSCP/增加Pre-R8 QoS到TOS_DSCP的映射规则（ADD PRER8REMARK）_09654400.md)
    > - **[ADD EPSREMARK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)**
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L24:
    > - [**SET APNPCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    > - [**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD USRPROFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)

**md：`WSFD-109101/配置本地PCC功能_30805097.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD USRPROFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md) | 用户模板组名称（USERPROFGNAME） | upg_test | 本端规划 | 配置UserProfile Group。 |
- 任务示例脚本（该命令行）：
  `ADD USRPROFGROUP:USERPROFGNAME="upg_test";`
- 操作步骤上下文（±2 行原文）：
  L101:
    >       [**ADD RULEBINDING**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    >     d. 配置UserProfile Group。
    >       [**ADD USRPROFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    >     e. 将UserProfile绑定到UserProfile Group。
    >       [**ADD UPBINDUPG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
  L158:
    >   ```
    >   ```
    >   ADD USRPROFGROUP:USERPROFGNAME="upg_test";
    >   ```
    >   ```

**md：`WSFD-109101/WSFD-109101 PCC基本功能（5G）参考信息_72466541.md`**
- 操作步骤上下文（±2 行原文）：
  L15:
    > - [**ADD PCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)
    > - [**ADD USERPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD USRPROFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**SET APNPCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    > - [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD USRPROFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md) | 用户模板组名称（USERPROFGNAME） | upg_test | 本端规划 | 配置UserProfile Group。 |
- 任务示例脚本（该命令行）：
  `ADD USRPROFGROUP:USERPROFGNAME="upg_test";`
- 操作步骤上下文（±2 行原文）：
  L185:
    >     15. **可选：**配置UserProfile组，将UserProfile绑定到UserProfile组，再将UserProfile组绑定到DNN实例上。用于动态PCC或本地PCC。
    >           a. 配置UserProfile Group。
    >             [**ADD USRPROFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    >           b. 将UserProfile绑定到UserProfile Group。
    >             [**ADD UPBINDUPG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
  L261:
    > ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC,PROFILERANGE=ALL;
    > ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";
    > ADD USRPROFGROUP:USERPROFGNAME="upg_test";
    > ADD UPBINDUPG:USERPROFGNAME="upg_test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up_test";
    > ADD APNUSRPROFG:APN="huawei.com",USERPROFGNAME="upg_test";

### WSFD-109102

**md：`WSFD-109102/WSFD-109102 ADC基本功能参考信息_92582138.md`**
- 操作步骤上下文（±2 行原文）：
  L13:
    > 
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)

### WSFD-109107

**md：`WSFD-109107/WSFD-109107 业务触发的QoS保证参考信息_85397060.md`**
- 操作步骤上下文（±2 行原文）：
  L18:
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)

**md：`WSFD-109107/激活业务触发的QoS保证_85397058.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md) | 用户模板组名称（USERPROFGNAME） | upg_test | 本端规划 | 配置UserProfile Group。 |
- 任务示例脚本（该命令行）：
  `ADD USRPROFGROUP:USERPROFGNAME="upg_test";`
- 操作步骤上下文（±2 行原文）：
  L89:
    > 7. **可选：**（无可用PCRF/PCF时使用）配置UserProfile组，将UserProfile绑定到UserProfile组，再将UserProfile组绑定到DNN实例上。用于本地PCC的静态规则。如UserProfile已配置，请跳过本步骤。
    >     a. 配置UserProfile Group。
    >       [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    >     b. 将UserProfile绑定到UserProfile Group。
    >       [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
  L159:
    > 
    > ```
    > ADD USRPROFGROUP:USERPROFGNAME="upg_test";
    > ADD UPBINDUPG:USERPROFGNAME="upg_test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up_test";
    > ADD APNUSRPROFG:APN="huawei.com",USERPROFGNAME="upg_test";

### WSFD-211005

**md：`WSFD-211005/WSFD-211005 基于业务感知的带宽控制参考信息_79619228.md`**
- 操作步骤上下文（±2 行原文）：
  L15:
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)

**md：`WSFD-211005/激活基于业务感知的带宽控制_79619226.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md) | 用户模板组名称（USERPROFGNAME） | upg_test | 本端规划 | 配置UserProfile Group。 |
- 任务示例脚本（该命令行）：
  `ADD USRPROFGROUP:USERPROFGNAME="upg_test";`
- 操作步骤上下文（±2 行原文）：
  L55:
    > 3. 配置UserProfile组，将UserProfile绑定到UserProfile组，再将UserProfile组绑定到DNN实例上。用于动态PCC或本地PCC。
    >     a. 配置UserProfile Group。如已配置，请跳过本步骤。
    >       [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    >     b. 将UserProfile绑定到UserProfile Group。如已配置，请跳过本步骤。
    >       [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
  L80:
    > ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC;
    > ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";
    > ADD USRPROFGROUP:USERPROFGNAME="upg_test";
    > ADD UPBINDUPG:USERPROFGNAME="upg_test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up_test";
    > ADD APNUSRPROFG:APN="huawei.com",USERPROFGNAME="upg_test";

### WSFD-011306

**md：`WSFD-011306/WSFD-011306 Radius功能参考信息_15542176.md`**
- 操作步骤上下文（±2 行原文）：
  L47:
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - **[ADD RULEBINDING](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)**
    > - **[ADD USRPROFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)**
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)

**md：`WSFD-011306/配置业务触发RADIUS功能_33000859.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD USRPROFGROUP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)** | 用户模板组名称（USERPROFGNAME） | upg_test | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD USRPROFGROUP: USERPROFGNAME="upg_test";`
- 操作步骤上下文（±2 行原文）：
  L66:
    >       **[ADD RULEBINDING](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)**
    >     c. 配置UsrProfGroup。
    >       **[ADD USRPROFGROUP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)**
    >     d. 将UserProfile绑定到UsrProfGroup。
    >       [**ADD UPBINDUPG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
  L104:
    > ADD USERPROFILE: USERPROFILENAME="up_test", UPTYPE=PCC;
    > ADD RULEBINDING: USERPROFILENAME="up_test", RULENAME="rule_test1";
    > ADD USRPROFGROUP: USERPROFGNAME="upg_test";
    > ADD UPBINDUPG: USERPROFGNAME="upg_test", UPBINDTYPE=DEFAULT, USERPROFILENAME="up_test";
    > ADD APNUSRPROFG: APN="apn-test", USERPROFGNAME="upg_test";

### WSFD-011201

**md：`WSFD-011201/配置离线计费参数（GGSN_SGW-C_PGW-C）_95923590.md`**
- 操作步骤上下文（±2 行原文）：
  L95:
    >       **SET USRPROFCHARGE**
    >     c. 配置UserProfileGroup。
    >       **ADD USRPROFGROUP**
    >     d. 将UserProfile绑定到UserProfileGroup。
    >       **ADD UPBINDUPG**

**md：`WSFD-011201/配置离线计费的费率标识（GGSN_SGW-C_PGW-C）_98555879.md`**
- 数据规划表（该命令的参数行）：
  | **ADD USRPROFGROUP** | 用户模板组名称（USERPROFGNAME） | upg-test | 本端规划 | 配置UserProfile组。 |
- 任务示例脚本（该命令行）：
  `ADD USRPROFGROUP:USERPROFGNAME="upg-test";`
  `ADD USRPROFGROUP:USERPROFGNAME="upg-test";`
- 操作步骤上下文（±2 行原文）：
  L78:
    >     3. 配置UserProfile绑定的UserProfile组及APN实例。
    >           a. 配置UserProfile组，将UserProfile绑定到UserProfile组上。
    >             **ADD USRPROFGROUP**
    >             **ADD UPBINDUPG**
    >           b. 配置APN，将UserProfile组绑定到指定APN实例上。
  L107:
    >     5. 配置UserProfile绑定的UserProfile组及APN实例。
    >           a. 配置UserProfile组，将UserProfile绑定到UserProfile组上。
    >             **ADD USRPROFGROUP**
    >             **ADD UPBINDUPG**
    >           b. 配置APN，将UserProfile组绑定到指定APN实例上。
  L141:
    >   ADD USERPROFILE:USERPROFILENAME="up-test", UPTYPE=PCC;
    >   SET URRGRPBINDING:USERPROFILENAME="up-test",DFTURRGRPNAME="urrgroup1";
    >   ADD USRPROFGROUP:USERPROFGNAME="upg-test";
    >   ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";
    >   ADD APN:APN="apn-test";

### WSFD-011206

**md：`WSFD-011206/配置融合计费模板_93400212.md`**
- 数据规划表（该命令的参数行）：
  | **ADD USRPROFGROUP** | 用户模板组名称（USERPROFGNAME） | upg_test | 本端规划 | 将UserProfile绑定到DNN实例。<br>基于UserProfile粒度需要规划。 |
- 任务示例脚本（该命令行）：
  `ADD USRPROFGROUP: USERPROFGNAME="upg_test";`
- 操作步骤上下文（±2 行原文）：
  L96:
    >     3. 配置UserProfile组及DNN实例。
    >           a. 配置UserProfile组，将UserProfile绑定到UserProfile组。
    >             **ADD USRPROFGROUP**
    >             **ADD UPBINDUPG**
    >           b. 配置DNN实例，将UserProifle组绑定到DNN实例。
  L147:
    > 
    > ```
    > ADD USRPROFGROUP: USERPROFGNAME="upg_test";
    > ADD UPBINDUPG: USERPROFGNAME="upg_test", UPBINDTYPE=DEFAULT, USERPROFILENAME="userprofile001";
    > ```

**md：`WSFD-011206/配置融合计费费率标识_93360308.md`**
- 数据规划表（该命令的参数行）：
  | **ADD USRPROFGROUP** | 用户模板组名称（USERPROFGNAME） | upg_test | 本端规划 | 配置一个用户模板组。 |
- 任务示例脚本（该命令行）：
  `ADD USRPROFGROUP: USERPROFGNAME="upg_test";`
- 操作步骤上下文（±2 行原文）：
  L106:
    >     4. 配置UserProfile组及DNN实例。
    >           a. 配置UserProfile组，将UserProfile绑定到UserProfile组。
    >             **ADD USRPROFGROUP**
    >             **ADD UPBINDUPG**
    >           b. 配置DNN实例，将UserProifle组绑定到DNN实例。
  L202:
    > 
    > ```
    > ADD USRPROFGROUP: USERPROFGNAME="upg_test";
    > ADD UPBINDUPG: USERPROFGNAME="upg_test", UPBINDTYPE=SPECIFIC, PRIORITY=10, USERPROFILENAME="userprofile001";
    > ADD UPBINDUPG: USERPROFGNAME="upg_test", UPBINDTYPE=SPECIFIC, PRIORITY=20, USERPROFILENAME="userprofile002";

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L37:
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**SET URRGRPBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/设置用户模板的计费属性绑定关系（SET URRGRPBINDING）_09897209.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L37:
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**SET URRGRPBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/设置用户模板的计费属性绑定关系（SET URRGRPBINDING）_09897209.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)

**md：`WSFD-109001/配置在线计费模板_95923574.md`**
- 数据规划表（该命令的参数行）：
  | **ADD USRPROFGROUP** | 用户模板组名称（USERPROFGNAME） | upg-test | 本端规划 | 配置用户模板组。 |
- 任务示例脚本（该命令行）：
  `ADD USRPROFGROUP:USERPROFGNAME="upg-test";`
- 操作步骤上下文（±2 行原文）：
  L89:
    >       **SET USRPROFCHARGE**
    >     c. 配置UserProfileGroup。
    >       **ADD USRPROFGROUP**
    >     d. 将UserProfile绑定到UserProfileGroup。
    >       **ADD UPBINDUPG**
  L154:
    > 
    > ```
    > ADD USRPROFGROUP:USERPROFGNAME="upg-test";
    > ```
    > 

**md：`WSFD-109001/配置在线计费的费率标识_95923388.md`**
- 数据规划表（该命令的参数行）：
  | **ADD USRPROFGROUP** | 用户模板组名称（USERPROFGNAME） | upg-test | 本端规划 | 配置UserProfile组。 |
- 任务示例脚本（该命令行）：
  `ADD USRPROFGROUP:USERPROFGNAME="upg-test";`
  `ADD USRPROFGROUP:USERPROFGNAME="upg-test";`
- 操作步骤上下文（±2 行原文）：
  L82:
    >     3. 配置UserProfile绑定的UserProfile组及APN实例。
    >           a. 配置UserProfile组，将UserProfile绑定到UserProfile组上。
    >             **ADD USRPROFGROUP**
    >             **ADD UPBINDUPG**
    >           b. 配置APN，将UserProfile组绑定到指定APN实例上。
  L111:
    >     5. 配置UserProfile绑定的UserProfile组及APN实例。
    >           a. 配置UserProfile组，将UserProfile绑定到UserProfile组上。
    >             **ADD USRPROFGROUP**
    >             **ADD UPBINDUPG**
    >           b. 配置APN，将UserProfile组绑定到指定APN实例上。
  L145:
    >   ADD USERPROFILE:USERPROFILENAME="up-test", UPTYPE=PCC;
    >   SET URRGRPBINDING:USERPROFILENAME="up-test",DFTURRGRPNAME="urrgroup001";
    >   ADD USRPROFGROUP:USERPROFGNAME="upg-test";
    >   ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";
    >   ADD APN:APN="apn-test";

**md：`WSFD-109001/配置CCR触发场景_95923545.md`**
- 任务示例脚本（该命令行）：
  `ADD USRPROFGROUP:USERPROFGNAME="upg-test";`
- 操作步骤上下文（±2 行原文）：
  L150:
    > 
    > ```
    > ADD USRPROFGROUP:USERPROFGNAME="upg-test";
    > ```
    > 

### WSFD-109007

**md：`WSFD-109007/WSFD-109007 支持事件计费参考信息_74112323.md`**
- 操作步骤上下文（±2 行原文）：
  L22:
    > - [**ADD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)

**md：`WSFD-109007/配置事件计费功能_74112321.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md) | USERPROFGNAME（用户模板组名称） | upg-test | 本端规划 | 将Rule绑定到UserProfile上。 |
- 任务示例脚本（该命令行）：
  `ADD USRPROFGROUP:USERPROFGNAME="upg-test";`
- 操作步骤上下文（±2 行原文）：
  L96:
    > 8. 配置UserProfile绑定的UserProfile组及DNN实例。
    >     a. 配置UserProfile组，将UserProfile绑定到UserProfile组上。
    >       [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    >       [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    >     b. 配置DNN，将UserProfile组绑定到指定DNN实例上。
  L159:
    > ```
    > ADD RULEBINDING:USERPROFILENAME="up-test",RULENAME="rule-test";
    > ADD USRPROFGROUP:USERPROFGNAME="upg-test";
    > ADD UPBINDUPG:USERPROFGNAME="upg-test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up-test";
    > ADD APN:APN="apn-test";

### WSFD-201207

**md：`WSFD-201207/WSFD-201207 语音PCF_PCRF故障Bypass参考信息_85304300.md`**
- 操作步骤上下文（±2 行原文）：
  L116:
    > **[LST USERPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/查询用户模板（LST USERPROFILE）_09897214.md)**
    > 
    > [**ADD USRPROFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)
    > 
    > **[RMV USRPROFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/删除用户模板组（RMV USRPROFGROUP）_09897221.md)**

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（Gx接口）_60552093.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD USRPROFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)** | 用户模板组名称（USERPROFGNAME） | upg_ims | 全网规划 | （可选）配置用户模板组。 |
  | **[ADD USRPROFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)** | 用户模板组名称（USERPROFGNAME） | upg_ims | 全网规划 | （可选）配置用户模板组。 |
- 任务示例脚本（该命令行）：
  `ADD USRPROFGROUP:USERPROFGNAME="upg_ims";`
- 操作步骤上下文（±2 行原文）：
  L210:
    >       > **说明**
    >       > 如果已配置了APN ims使用的用户模板组，则跳过本步骤。
    >       **[ADD USRPROFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)**
    >     h. **可选：**将用户模板绑定到用户模板组中。
    >       > **说明**
  L241:
    >       > **说明**
    >       > 如果已配置了APN ims使用的用户模板组，则跳过本步骤。
    >       **[ADD USRPROFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)**
    >     i. **可选：**将用户模板绑定到用户模板组中。
    >       > **说明**
  L336:
    > 
    >       ```
    >       ADD USRPROFGROUP:USERPROFGNAME="upg_ims";
    >       ```
    >       //把用户模板绑定到用户模板组中。

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（N7接口）_32852169.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD USRPROFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)** | 用户模板组名称（USERPROFGNAME） | upg_ims | 全网规划 | （可选）配置用户模板组。 |
  | **[ADD USRPROFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)** | 用户模板组名称（USERPROFGNAME） | upg_ims | 全网规划 | （可选）配置用户模板组。 |
- 任务示例脚本（该命令行）：
  `ADD USRPROFGROUP:USERPROFGNAME="upg_ims";`
- 操作步骤上下文（±2 行原文）：
  L229:
    >       > **说明**
    >       > 如果已配置了APN ims使用的用户模板组，则跳过本步骤。
    >       **[ADD USRPROFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)**
    >     h. **可选：**将用户模板绑定到用户模板组中。
    >       > **说明**
  L260:
    >       > **说明**
    >       > 如果已配置了APN ims使用的用户模板组，则跳过本步骤。
    >       **[ADD USRPROFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)**
    >     i. **可选：**将用户模板绑定到用户模板组中。
    >       > **说明**
  L364:
    > 
    >       ```
    >       ADD USRPROFGROUP:USERPROFGNAME="upg_ims";
    >       ```
    >       //把用户模板绑定到用户模板组中。

## ④ 自动比对
- 命令真相参数（1）：['USERPROFGNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 15, '全网规划': 4}（多值→atom 应考虑 decision_driven）
