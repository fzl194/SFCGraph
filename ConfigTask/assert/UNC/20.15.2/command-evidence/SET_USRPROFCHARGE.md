# 命令证据包：SET USRPROFCHARGE
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md`
> 用该命令的特性数：5

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

该命令用来设置User Profile实例的计费配置，具体为：

1、为User Profile实例配置在线计费、离线计费方式以及融合计费方式。

2、为User Profile实例绑定离线计费模板。

3、为User Profile实例绑定DCC模板。

4、为User Profile实例绑定CC模板。

5、为User Profile实例绑定
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。
- 该命令最大记录数为105000。
- 全局在线模板（DccTemplate名称为global）不允许绑定在User Profile下。
- 当在线计费、离线计费和紧耦合配置为INHERIT则继承基于SET APNCHARGECTRL的配置。
- 模板名不支持包含空格，但是支持仅输入一个空格。当模板名仅输入一个空格时，表示删除该User Profile和对应

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| USRPROFNAME | 用户模板名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。 |
| ONLINESW | 在线计费开关 | local_planned | optional | 无 | 枚举类型。 |
| OFFLINESW | 离线计费开关 | local_planned | optional | 无 | 枚举类型。 |
| CONVERGEDSW | 融合计费开关 | local_planned | optional | 无 | 枚举类型。 |
| PGWOFCTEMPLATE | PGW离线计费模板名 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～63。 |
| SGWOFCTEMPLATE | SGW离线计费模板名 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～63。 |
| GGSNOFCTEMPLATE | GGSN离线计费模板名 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～63。 |
| DCCTEMPLATE | DCC模板名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～63。 |
| TARIFFGRPNAME | 费率切换组名 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。 |
| CCNAME | 计费属性名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。 |
| SMFOFCTEMPLATE | SMF离线计费模板名 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～63。 |
| CCTEMPLATE | 融合计费模板名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～63。 |
| RGAPPLIED | 业务申请上报模式 | global_planned | conditional | 无 | 枚举类型。 |
| QBCSW | QBC计费开关 | global_planned | conditional | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L13:
    > 
    > - **[ADD CHARGECHAR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/增加对本地用户、漫游用户、拜访用户所采用的计费属性（ADD CHARGECHAR）_09896809.md)**
    > - [**SET USRPROFCHARGE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
    > - [**SET APNCHARGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md)
    > - [**SET GLBCHARGECHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置对本地用户、漫游用户、拜访用户所采用的计费属性（SET GLBCHARGECHAR）_09896800.md)

**md：`WSFD-011201/配置离线_在线计费方式（GGSN_PGW-C）_95923455.md`**
- 数据规划表（该命令的参数行）：
  | **SET USRPROFCHARGE** | 用户模板名称（USRPROFNAME） | up-test | 已配置数据中获取 | 配置User Profile实例的计费方式。 |
  | **SET USRPROFCHARGE** | 离线计费开关（OFFLINESW） | ENABLE | 本端规划 | 配置User Profile实例的计费方式。 |
  | **SET USRPROFCHARGE** | 用户模板名称（USRPROFNAME） | up-test | 已配置数据中获取 | 配置User Profile实例的计费方式。 |
  | **SET USRPROFCHARGE** | 在线计费开关（ONLINESW） | ENABLE | 本端规划 | 配置User Profile实例的计费方式。 |
- 任务示例脚本（该命令行）：
  `SET USRPROFCHARGE: USRPROFNAME="up-test", OFFLINESW=ENABLE;`
  `SET USRPROFCHARGE: USRPROFNAME="up-test", ONLINESW=ENABLE;`
  `SET USRPROFCHARGE: USRPROFNAME="up-test", ONLINESW=ENABLE, OFFLINESW=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L87:
    >   > 针对同一个用户，不同属性下规划的计费方式要一致，否则用户计费会出错。例如，针对CC取值为NORMAL的本地用户，如果设置NORMAL用户进行离线计费，又设置本地用户进行在线计费，则最终用户计费将出错。
    > 2. 基于UserProfile配置计费方式。
    >   **SET USRPROFCHARGE**
    > 3. 基于APN使能GGSN/PGW-C的离线/在线计费方式。
    >   **SET APNCHARGECTRL**
  L135:
    > 
    >   ```
    >   SET USRPROFCHARGE: USRPROFNAME="up-test", OFFLINESW=ENABLE;
    >   ```
    >   //任务二：配置基于APN使能GGSN/PGW-C的离线计费方式。
  L171:
    > 
    >   ```
    >   SET USRPROFCHARGE: USRPROFNAME="up-test", ONLINESW=ENABLE;
    >   ```
    >   //任务二：配置基于APN的在线计费方式。

**md：`WSFD-011201/配置离线计费参数（GGSN_SGW-C_PGW-C）_95923590.md`**
- 数据规划表（该命令的参数行）：
  | **SET USRPROFCHARGE** | 用户模板名称（USRPROFNAME） | up-test | 已配置数据中获取 | 配置UserProfile对象绑定OFCTemplate模板 |
  | **SET USRPROFCHARGE** | PGW离线计费模板名（PGWOFCTEMPLATE） | offlinecharge-test | 已配置数据中获取 | 配置UserProfile对象绑定OFCTemplate模板 |
  | **SET USRPROFCHARGE** | SGW离线计费模板名（SGWOFCTEMPLATE） | offlinecharge-test | 已配置数据中获取 | 配置UserProfile对象绑定OFCTemplate模板 |
- 任务示例脚本（该命令行）：
  `SET USRPROFCHARGE:USRPROFNAME="up-test",PGWOFCTEMPLATE="offlinecharge-test",SGWOFCTEMPLATE="offlinecharge-test";`
- 操作步骤上下文（±2 行原文）：
  L93:
    >       **ADD USERPROFILE**
    >     b. 配置UserProfile对象绑定OFCTemplate模板。
    >       **SET USRPROFCHARGE**
    >     c. 配置UserProfileGroup。
    >       **ADD USRPROFGROUP**
  L153:
    >   ```
    >   ```
    >   SET USRPROFCHARGE:USRPROFNAME="up-test",PGWOFCTEMPLATE="offlinecharge-test",SGWOFCTEMPLATE="offlinecharge-test";
    >   ```
    > 3. 任务二：配置APN实例 **apn-test** 的离线计费参数。

**md：`WSFD-011201/配置离线计费费率切换（GGSN_SGW-C_PGW-C）_95923434.md`**
- 数据规划表（该命令的参数行）：
  | **SET USRPROFCHARGE** | 用户模板名称（USRPROFNAME） | up-test | 已配置数据中获取 | 每个UserProfile只能绑定一个费率切换组。如果UserProfile下已绑定了费率切换组，要修改为绑定其他的费率切换组，必须先执行<br>**SET USRPROFCHARGE**<br>命令修改原来的绑定关系。 |
  | **SET USRPROFCHARGE** | 费率切换组名（TARIFFGRPNAME） | testtariff | 已配置数据中获取 | 每个UserProfile只能绑定一个费率切换组。如果UserProfile下已绑定了费率切换组，要修改为绑定其他的费率切换组，必须先执行<br>**SET USRPROFCHARGE**<br>命令修改原来的绑定关系。 |
- 任务示例脚本（该命令行）：
  `SET USRPROFCHARGE: USRPROFNAME="up-test", TARIFFGRPNAME="testtarif";`
- 操作步骤上下文（±2 行原文）：
  L75:
    >       **ADD USERPROFILE**
    >     b. 配置UserProfile实例下的费率切换组。
    >       **SET USRPROFCHARGE**
    > 
    > ## [任务示例](#ZH-CN_OPI_0295923434)
  L155:
    >   ```
    >   ```
    >   SET USRPROFCHARGE: USRPROFNAME="up-test", TARIFFGRPNAME="testtarif";
    >   ```

**md：`WSFD-011201/配置计费属性CC（GGSN_SGW-C_PGW-C）_95923501.md`**
- 数据规划表（该命令的参数行）：
  | **SET USRPROFCHARGE** | 用户模板名称（USRPROFNAME） | up-test | 已配置数据中获取 | 将CC绑定到UserProflie上。每个UserProflie只能绑定一个计费属性。如果UserProflie已绑定了计费属性，要绑定其他的计费属性，必须调用<br>**SET USRPROFCHARGE**<br>命令修改绑定关系。 |
  | **SET USRPROFCHARGE** | 计费属性名称（CCNAME） | testchgcha | 已配置数据中获取 | 将CC绑定到UserProflie上。每个UserProflie只能绑定一个计费属性。如果UserProflie已绑定了计费属性，要绑定其他的计费属性，必须调用<br>**SET USRPROFCHARGE**<br>命令修改绑定关系。 |
- 任务示例脚本（该命令行）：
  `SET USRPROFCHARGE: USRPROFNAME="up-test", CCNAME="testchgcha";`
- 操作步骤上下文（±2 行原文）：
  L78:
    >       **ADD USERPROFILE**
    >     3. 将CC绑定到UserProflie上。
    >       **SET USRPROFCHARGE**
    > 
    > ## [任务示例](#ZH-CN_OPI_0295923501)
  L123:
    > 
    > ```
    > SET USRPROFCHARGE: USRPROFNAME="up-test", CCNAME="testchgcha";
    > ```

### WSFD-011206

**md：`WSFD-011206/WSFD-011206 支持融合计费参考信息_74013176.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - [**SET N40APIVER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/N40 API版本/设置N40接口协议版本和需要使用的FeatureList（SET N40APIVER）_31773565.md)
    > - **[ADD CHARGECHAR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/增加对本地用户、漫游用户、拜访用户所采用的计费属性（ADD CHARGECHAR）_09896809.md)**
    > - [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
    > - [**SET APNCHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md)
    > - [**SET GLBCHARGECHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置对本地用户、漫游用户、拜访用户所采用的计费属性（SET GLBCHARGECHAR）_09896800.md)

**md：`WSFD-011206/使能融合计费功能_77691175.md`**
- 数据规划表（该命令的参数行）：
  | **SET USRPROFCHARGE** | 用户模板名称（USRPROFNAME） | up-test | 已配置数据中获取 | 配置User Profile实例的计费方式。 |
  | **SET USRPROFCHARGE** | 融合计费开关（CONVERGEDSW） | ENABLE | 本端规划 | 配置User Profile实例的计费方式。 |
  | **SET USRPROFCHARGE** | 业务申请上报模式（RGAPPLIED） | ONLINERGONLY | 全网规划 | 说明：- 当“RGAPPLIED”配置为“DEFAULT”时，当URRGROUP下同时配置离线和在线URR，会优先选择在线URR。<br>- 当“RGAPPLIED”配置为“ONLINERGONLY”或“OFFLINERGONLY”时，URRGROUP下建议同时配置离线和在线URR。 |
- 任务示例脚本（该命令行）：
  `SET USRPROFCHARGE: USRPROFNAME="up-test",CONVERGEDSW=ENABLE,RGAPPLIED=ONLINERGONLY;`
- 操作步骤上下文（±2 行原文）：
  L62:
    >   > **SET CHARGECTRL** 根据用户漫游属性设置计费方式， **ADD CHARGEMETHOD** 根据CC属性设置计费方式，针对同一个用户，两者规划的计费方式要一致，否则用户计费会出错。例如，针对CC是normal的本地用户，如果设置本地用户进行在线计费，又设置normal用户进行离线计费，那用户最终计费结果将出错。
    > 2. 基于UserProfile配置计费方式。
    >   **SET USRPROFCHARGE**
    > 3. 基于DNN配置计费方式。
    >   **SET APNCHARGECTRL**
  L89:
    > 
    > ```
    > SET USRPROFCHARGE: USRPROFNAME="up-test",CONVERGEDSW=ENABLE,RGAPPLIED=ONLINERGONLY;
    > ```
    > 

**md：`WSFD-011206/配置融合计费模板_93400212.md`**
- 数据规划表（该命令的参数行）：
  | **SET USRPROFCHARGE** | 用户模板名称（USRPROFNAME） | up_test | 已配置数据中获取 | 基于UserProfile粒度，将CCT绑定到特定UserProfile下。 |
  | **SET USRPROFCHARGE** | 融合计费模板名称（CCTEMPLATE） | cct_test | 已配置数据中获取 | 基于UserProfile粒度，将CCT绑定到特定UserProfile下。 |
- 任务示例脚本（该命令行）：
  `SET USRPROFCHARGE: USRPROFNAME="up_test", CCTEMPLATE="cct_test";`
- 操作步骤上下文（±2 行原文）：
  L93:
    >             **ADD USERPROFILE**
    >           b. 将CCT绑定到UserProfile上。
    >             **SET USRPROFCHARGE**
    >     3. 配置UserProfile组及DNN实例。
    >           a. 配置UserProfile组，将UserProfile绑定到UserProfile组。
  L141:
    > ```
    > ADD USERPROFILE: USERPROFILENAME="up_test", UPTYPE=PCC;
    > SET USRPROFCHARGE: USRPROFNAME="up_test", CCTEMPLATE="cct_test";
    > ```
    > 

**md：`WSFD-011206/配置计费属性CC_90776700.md`**
- 数据规划表（该命令的参数行）：
  | **SET USRPROFCHARGE** | 用户模板名称（USRPROFNAME） | up-test | 已配置数据中获取 | 将CC绑定到UserProflie上。每个UserProflie只能绑定一个计费属性。如果UserProflie已绑定了计费属性，要绑定其他的计费属性，必须调用<br>**SET USRPROFCHARGE**<br>命令修改绑定关系。 |
  | **SET USRPROFCHARGE** | 计费属性名称（CCNAME） | testchgcha | 已配置数据中获取 | 将CC绑定到UserProflie上。每个UserProflie只能绑定一个计费属性。如果UserProflie已绑定了计费属性，要绑定其他的计费属性，必须调用<br>**SET USRPROFCHARGE**<br>命令修改绑定关系。 |
- 任务示例脚本（该命令行）：
  `SET USRPROFCHARGE: USRPROFNAME="up-test", CCNAME="testchgcha";`
- 操作步骤上下文（±2 行原文）：
  L77:
    >       **ADD USERPROFILE**
    >     4. 将CC绑定到UserProfile上。
    >       **SET USRPROFCHARGE**
    > 
    > ## [任务示例](#ZH-CN_OPI_0190776700)
  L110:
    > ADD CHARGECHAR: CCNAME="testchgcha", HOME="0x0800", ROAM="0x0800", VISIT="0x0800", HOMESGSN=DISABLE, ROAMSGSN=DISABLE, VISITSGSN=DISABLE;
    > ADD USERPROFILE: USERPROFILENAME="up-test",UPTYPE=PCC;
    > SET USRPROFCHARGE: USRPROFNAME="up-test", CCNAME="testchgcha";
    > ```

**md：`WSFD-011206/配置费率切换_86411191.md`**
- 数据规划表（该命令的参数行）：
  | **SET USRPROFCHARGE** | 用户模板名称（USRPROFNAME） | up-test | 已配置数据中获取 | 每个UserProfile只能绑定一个费率切换组。如果UserProfile下已绑定了费率切换组，要修改为绑定其他的费率切换组，必须先执行<br>**SET USRPROFCHARGE**<br>命令修改原来的绑定关系。 |
  | **SET USRPROFCHARGE** | 费率切换组名（TARIFFGRPNAME） | tar_nb | 已配置数据中获取 | 每个UserProfile只能绑定一个费率切换组。如果UserProfile下已绑定了费率切换组，要修改为绑定其他的费率切换组，必须先执行<br>**SET USRPROFCHARGE**<br>命令修改原来的绑定关系。 |

**md：`WSFD-011206/调测融合计费的计费会话创建功能_89257219.md`**
- 操作步骤上下文（±2 行原文）：
  L54:
    >           - 如果使能融合计费，请执行[步骤 8](#ZH-CN_OPI_0289257219__step261013496208)。
    >           - 如果未使能融合计费，请执行[步骤 7.b](#ZH-CN_OPI_0289257219__substep1784820385463)。
    >     b. 执行 [**SET CHARGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/设置计费控制配置（SET CHARGECTRL）_09896792.md) 命令，配置当前用户漫游、拜访、本地属性使能N40接口融合计费；执行 [**SET USRPROFCHARGE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md) 、 [**SET APNCHARGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md) 、 [**MOD CHARGEMETHOD**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费属性计费控制/修改计费方式（MOD CHARGEMETHOD）_09896796.md) 命令，配置当前用户按照规划基于User Profile或DNN或CC使能融合计费，请再次执行 [步骤 3](#ZH-CN_OPI_0289257219__step2585105420194) 。
    > 8. 检查用户N40接口是否开启了用户激活创建计费会话功能。
    >     a. 执行 [**LST CCT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/查询融合计费模板（LST CCT）_09653820.md) 命令，查询与当前用户所使用的融合计费模板对应的 “CHF交互使能开关” 是否为 “激活发送” 。

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L31:
    > - [**ADD OCSGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Group/增加Ocs组（ADD OCSGROUP）_09896959.md)
    > - [**ADD OCSBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS绑定OCS Group/增加Ocs绑定关系（ADD OCSBINDING）_09896963.md)
    > - [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
    > - [**SET GLBCHARGECHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置对本地用户、漫游用户、拜访用户所采用的计费属性（SET GLBCHARGECHAR）_09896800.md)
    > - [**ADD CHARGEMETHOD**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费属性计费控制/增加计费方式（ADD CHARGEMETHOD）_09896795.md)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L31:
    > - [**ADD OCSGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Group/增加Ocs组（ADD OCSGROUP）_09896959.md)
    > - [**ADD OCSBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS绑定OCS Group/增加Ocs绑定关系（ADD OCSBINDING）_09896963.md)
    > - [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
    > - [**SET GLBCHARGECHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置对本地用户、漫游用户、拜访用户所采用的计费属性（SET GLBCHARGECHAR）_09896800.md)
    > - [**ADD CHARGEMETHOD**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费属性计费控制/增加计费方式（ADD CHARGEMETHOD）_09896795.md)

**md：`WSFD-109001/配置在线计费模板_95923574.md`**
- 数据规划表（该命令的参数行）：
  | **SET USRPROFCHARGE** | 用户模板名称（USRPROFNAME） | up-test | 已配置数据中获取 | User Profile实例绑定DCC模板。 |
  | **SET USRPROFCHARGE** | DCC模板名称（DCCTEMPLATE） | dcc-test | 已配置数据中获取 | User Profile实例绑定DCC模板。 |
- 任务示例脚本（该命令行）：
  `SET USRPROFCHARGE: USRPROFNAME="up-test", DCCTEMPLATE="dcc-test";`
- 操作步骤上下文（±2 行原文）：
  L87:
    >       **ADD USERPROFILE**
    >     b. 配置DCC Template模板绑定UserProfile实例。
    >       **SET USRPROFCHARGE**
    >     c. 配置UserProfileGroup。
    >       **ADD USRPROFGROUP**
  L150:
    > 
    > ```
    > SET USRPROFCHARGE: USRPROFNAME="up-test", DCCTEMPLATE="dcc-test";
    > ```
    > 

**md：`WSFD-109001/配置离线_在线计费方式（GGSN_PGW-C）_15408914.md`**
- 数据规划表（该命令的参数行）：
  | **SET USRPROFCHARGE** | 用户模板名称（USRPROFNAME） | up-test | 已配置数据中获取 | 配置User Profile实例的计费方式。 |
  | **SET USRPROFCHARGE** | 离线计费开关（OFFLINESW） | ENABLE | 本端规划 | 配置User Profile实例的计费方式。 |
  | **SET USRPROFCHARGE** | 用户模板名称（USRPROFNAME） | up-test | 已配置数据中获取 | 配置User Profile实例的计费方式。 |
  | **SET USRPROFCHARGE** | 在线计费开关（ONLINESW） | ENABLE | 本端规划 | 配置User Profile实例的计费方式。 |
- 任务示例脚本（该命令行）：
  `SET USRPROFCHARGE: USRPROFNAME="up-test", OFFLINESW=ENABLE;`
  `SET USRPROFCHARGE: USRPROFNAME="up-test", ONLINESW=ENABLE;`
  `SET USRPROFCHARGE: USRPROFNAME="up-test", ONLINESW=ENABLE, OFFLINESW=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L87:
    >   > 针对同一个用户，不同属性下规划的计费方式要一致，否则用户计费会出错。例如，针对CC取值为NORMAL的本地用户，如果设置NORMAL用户进行离线计费，又设置本地用户进行在线计费，则最终用户计费将出错。
    > 2. 基于UserProfile配置计费方式。
    >   **SET USRPROFCHARGE**
    > 3. 基于APN使能GGSN/PGW-C的离线/在线计费方式。
    >   **SET APNCHARGECTRL**
  L135:
    > 
    >   ```
    >   SET USRPROFCHARGE: USRPROFNAME="up-test", OFFLINESW=ENABLE;
    >   ```
    >   //任务二：配置基于APN使能GGSN/PGW-C的离线计费方式。
  L171:
    > 
    >   ```
    >   SET USRPROFCHARGE: USRPROFNAME="up-test", ONLINESW=ENABLE;
    >   ```
    >   //任务二：配置基于APN的在线计费方式。

**md：`WSFD-109001/配置计费属性CC（GGSN_SGW-C_PGW-C）_15408915.md`**
- 数据规划表（该命令的参数行）：
  | **SET USRPROFCHARGE** | 用户模板名称（USRPROFNAME） | up-test | 已配置数据中获取 | 将CC绑定到UserProflie上。每个UserProflie只能绑定一个计费属性。如果UserProflie已绑定了计费属性，要绑定其他的计费属性，必须调用<br>**SET USRPROFCHARGE**<br>命令修改绑定关系。 |
  | **SET USRPROFCHARGE** | 计费属性名称（CCNAME） | testchgcha | 已配置数据中获取 | 将CC绑定到UserProflie上。每个UserProflie只能绑定一个计费属性。如果UserProflie已绑定了计费属性，要绑定其他的计费属性，必须调用<br>**SET USRPROFCHARGE**<br>命令修改绑定关系。 |
- 任务示例脚本（该命令行）：
  `SET USRPROFCHARGE: USRPROFNAME="up-test", CCNAME="testchgcha";`
- 操作步骤上下文（±2 行原文）：
  L78:
    >       **ADD USERPROFILE**
    >     3. 将CC绑定到UserProflie上。
    >       **SET USRPROFCHARGE**
    > 
    > ## [任务示例](#ZH-CN_OPI_0315408915)
  L123:
    > 
    > ```
    > SET USRPROFCHARGE: USRPROFNAME="up-test", CCNAME="testchgcha";
    > ```

### WSFD-109007

**md：`WSFD-109007/WSFD-109007 支持事件计费参考信息_74112323.md`**
- 操作步骤上下文（±2 行原文）：
  L19:
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)
    > - [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
    > - [**ADD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)

**md：`WSFD-109007/配置事件计费功能_74112321.md`**
- 数据规划表（该命令的参数行）：
  | [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md) | USRPROFNAME（用户模板名称） | up-test | 本端规划 | 配置融合计费的CCT模板。 |
  | [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md) | CCTEMPLATE（融合计费模板名称） | cct-test | 本端规划 | 配置融合计费的CCT模板。 |
  | [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md) | USRPROFNAME（用户模板名称） | up-test | 本端规划 | 配置在线计费的DCC模板。 |
  | [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md) | DCCTEMPLATE（DCC模板名称） | dcc-test | 本端规划 | 配置在线计费的DCC模板。 |
- 任务示例脚本（该命令行）：
  `SET USRPROFCHARGE: USRPROFNAME="up-test", CCTEMPLATE="cct-test";`
  `SET USRPROFCHARGE: USRPROFNAME="up-test", DCCTEMPLATE="dcc-test";`
- 操作步骤上下文（±2 行原文）：
  L88:
    >     - 配置融合计费模板。
    >       [**ADD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)
    >       [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
    >     - 配置在线计费模板。
    >       [**ADD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
  L91:
    >     - 配置在线计费模板。
    >       [**ADD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
    >       [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
    > 7. 绑定该UserProfile使用的Rule。
    >   [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
  L145:
    > ```
    > ADD CCT: CCTMPLTNAME="cct-test";
    > SET USRPROFCHARGE: USRPROFNAME="up-test", CCTEMPLATE="cct-test";
    > ```
    > 

## ④ 自动比对
- 命令真相参数（14）：['CCNAME', 'CCTEMPLATE', 'CONVERGEDSW', 'DCCTEMPLATE', 'GGSNOFCTEMPLATE', 'OFFLINESW', 'ONLINESW', 'PGWOFCTEMPLATE', 'QBCSW', 'RGAPPLIED', 'SGWOFCTEMPLATE', 'SMFOFCTEMPLATE', 'TARIFFGRPNAME', 'USRPROFNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 22, '本端规划': 9, '全网规划': 1}（多值→atom 应考虑 decision_driven）
