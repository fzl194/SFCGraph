# 命令证据包：SET APNCHARGECTRL
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md`
> 用该命令的特性数：6

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

该命令用来为APN实例设置计费参数。

此命令可以为APN实例绑定离线计费模板、话单字段模板、计费属性模板、费率切换组、DCC模板、CCT模板以及配置在线计费、离线计费和融合计费方式。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为20000。
- 全局在线模板（DccTemplate名称为global）不允许绑定在APN下。
- 模板名不支持包含空格，但是支持仅输入一个空格。当模板名仅输入一个空格时，表示删除该APN和对应模板的绑定关系。
- 当前版本不支持此命令的SMFOFCTEMPLATE参数。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | 

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| APN | APN名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不 |
| ONLINESW | 在线计费开关 | local_planned | optional | 无 | 枚举类型。 |
| OFFLINESW | 离线计费开关 | local_planned | optional | 无 | 枚举类型。 |
| CONVERGEDSW | 融合计费开关 | local_planned | optional | 无 | 枚举类型。 |
| PGWOFCTEMPLATE | PGW离线计费模板名 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～63。不支持空格。 |
| SGWOFCTEMPLATE | SGW离线计费模板名 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～63。不支持空格。 |
| GGSNOFCTEMPLATE | GGSN离线计费模板名 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～63。不支持空格。 |
| PGWCDRTEMPLATE | PGW-CDR话单字段模板名 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～63。 |
| SGWCDRTEMPLATE | SGW-CDR话单字段模板名 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～63。 |
| GCDRTEMPLATE | G-CDR话单字段模板名 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～63。 |
| DCCTEMPLATE | DCC模板名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～63。 |
| TARIFFGRPNAME | 费率切换组名 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。 |
| CCNAME | 计费属性名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。 |
| CCTEMPLATE | 融合计费模板 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～63。 |
| SMFOFCTEMPLATE | SMF离线计费模板名 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～63。不支持空格。 |
| RGAPPLIED | 业务申请上报模式 | global_planned | conditional | 无 | 枚举类型。 |
| N40MSGTEMP | N40消息属性模板 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～63。 |
| QBCSW | QBC计费开关 | global_planned | conditional | 无 | 枚举类型。 |
| SERVINGCCT | I-SMF/SGW使用的融合计费模板名称 | local_planned | optional | 无 | 字符串类型，输入长度为1~63。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - **[ADD CHARGECHAR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/增加对本地用户、漫游用户、拜访用户所采用的计费属性（ADD CHARGECHAR）_09896809.md)**
    > - [**SET USRPROFCHARGE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
    > - [**SET APNCHARGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md)
    > - [**SET GLBCHARGECHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置对本地用户、漫游用户、拜访用户所采用的计费属性（SET GLBCHARGECHAR）_09896800.md)
    > - [**SET CHARGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/设置计费控制配置（SET CHARGECTRL）_09896792.md)

**md：`WSFD-011201/配置离线_在线计费方式（GGSN_PGW-C）_95923455.md`**
- 数据规划表（该命令的参数行）：
  | **SET APNCHARGECTRL** | APN名称（APN） | apn-test | 已配置数据中获取 | 配置APN实例得离线计费方式。<br>- OFFLINESW默认值都是INHERIT。<br>- 在APN中配置INHERIT则计费方式继承基于计费属性的配置。 |
  | **SET APNCHARGECTRL** | 离线计费开关（OFFLINESW） | ENABLE | 全网规划 | 配置APN实例得离线计费方式。<br>- OFFLINESW默认值都是INHERIT。<br>- 在APN中配置INHERIT则计费方式继承基于计费属性的配置。 |
  | **SET APNCHARGECTRL** | APN名称（APN） | apn-test | 已配置数据中获取 | 配置APN实例的在线计费方式。<br>- ONLINESW默认值都是INHERIT。<br>- 在APN中配置INHERIT则计费方式继承基于计费属性的配置。 |
  | **SET APNCHARGECTRL** | 在线计费开关（ONLINESW） | ENABLE | 全网规划 | 配置APN实例的在线计费方式。<br>- ONLINESW默认值都是INHERIT。<br>- 在APN中配置INHERIT则计费方式继承基于计费属性的配置。 |
- 任务示例脚本（该命令行）：
  `SET APNCHARGECTRL: APN="apn-test",OFFLINESW=ENABLE;`
  `SET APNCHARGECTRL: APN="apn-test", ONLINESW=ENABLE;`
  `SET APNCHARGECTRL: APN="apn-test",ONLINESW=ENABLE, OFFLINESW=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L89:
    >   **SET USRPROFCHARGE**
    > 3. 基于APN使能GGSN/PGW-C的离线/在线计费方式。
    >   **SET APNCHARGECTRL**
    > 4. 基于用户计费属性使能GGSN/PGW-C的离线/在线计费方式。
    >   **ADD CHARGEMETHOD**
  L148:
    > 
    >   ```
    >   SET APNCHARGECTRL: APN="apn-test",OFFLINESW=ENABLE;
    >   ```
    >   //任务三：配置基于用户计费属性使能GGSN/PGW-C的离线计费方式。
  L184:
    > 
    >   ```
    >   SET APNCHARGECTRL: APN="apn-test", ONLINESW=ENABLE;
    >   ```
    >   //任务三：配置基于用户计费属性的在线计费方式。

**md：`WSFD-011201/配置离线计费参数（GGSN_SGW-C_PGW-C）_95923590.md`**
- 数据规划表（该命令的参数行）：
  | **SET APNCHARGECTRL** | APN名称（APN） | apn-test | 已配置数据中获取 | 配置APN实例绑定OFCTemplate模板 |
  | **SET APNCHARGECTRL** | PGW离线计费模板名（PGWOFCTEMPLATE） | offlinecharge-test | 已配置数据中获取 | 配置APN实例绑定OFCTemplate模板 |
  | **SET APNCHARGECTRL** | SGW离线计费模板名（SGWOFCTEMPLATE） | offlinecharge-test | 已配置数据中获取 | 配置APN实例绑定OFCTemplate模板 |
- 任务示例脚本（该命令行）：
  `SET APNCHARGECTRL: APN="apn-test",PGWOFCTEMPLATE="offlinecharge-test",SGWOFCTEMPLATE="offlinecharge-test";`
- 操作步骤上下文（±2 行原文）：
  L104:
    >       **ADD APN**
    >     b. 配置APN实例绑定OFCTemplate模板。
    >       **SET APNCHARGECTRL**
    > 4. 配置OFCTemplate模板绑定计费属性CC。
    >     a. 配置计费属性CC。如已配置CC，请跳过该步骤。
  L160:
    >   ```
    >   ```
    >   SET APNCHARGECTRL: APN="apn-test",PGWOFCTEMPLATE="offlinecharge-test",SGWOFCTEMPLATE="offlinecharge-test";
    >   ```
    > 4. 任务三：配置计费属性ChargeChar的离线计费参数。

**md：`WSFD-011201/配置离线计费费率切换（GGSN_SGW-C_PGW-C）_95923434.md`**
- 数据规划表（该命令的参数行）：
  | **SET APNCHARGECTRL** | APN名称（APN） | apn-test | 已配置数据中获取 | 每个APN只能绑定一个费率切换组。如果APN已绑定了费率切换组，要修改为绑定其他的费率切换组，必须先执行<br>**SET APNCHARGECTRL**<br>命令修改原来的绑定关系。 |
  | **SET APNCHARGECTRL** | 费率切换组名（TARIFFGRPNAME） | testtariff | 已配置数据中获取 | 每个APN只能绑定一个费率切换组。如果APN已绑定了费率切换组，要修改为绑定其他的费率切换组，必须先执行<br>**SET APNCHARGECTRL**<br>命令修改原来的绑定关系。 |
- 任务示例脚本（该命令行）：
  `SET APNCHARGECTRL:APN="apn-test",TARIFFGRPNAME="testtarif";`
- 操作步骤上下文（±2 行原文）：
  L70:
    >       **ADD APN**
    >     b. 配置APN实例下的费率切换组。
    >       **SET APNCHARGECTRL**
    > 4. 配置UserProfile下的费率切换组。
    >     a. 配置UserProfile。如已配置UserProfile，请跳过该步骤。
  L148:
    >   ```
    >   ```
    >   SET APNCHARGECTRL:APN="apn-test",TARIFFGRPNAME="testtarif";
    >   ```
    > 4. 任务三：基于UserProfile配置费率切换组。

**md：`WSFD-011201/配置计费属性CC（GGSN_SGW-C_PGW-C）_95923501.md`**
- 数据规划表（该命令的参数行）：
  | **SET APNCHARGECTRL** | APN名称（APN） | apn-test | 已配置数据中获取 | 将CC绑定到APN上。每个APN只能绑定一个计费属性。如果APN已绑定了计费属性，要绑定其他的计费属性，必须调用<br>**SET APNCHARGECTRL**<br>命令修改绑定关系。 |
  | **SET APNCHARGECTRL** | 计费属性名称（CCNAME） | testchgcha | 已配置数据中获取 | 将CC绑定到APN上。每个APN只能绑定一个计费属性。如果APN已绑定了计费属性，要绑定其他的计费属性，必须调用<br>**SET APNCHARGECTRL**<br>命令修改绑定关系。 |
- 任务示例脚本（该命令行）：
  `SET APNCHARGECTRL: APN="apn-test", CCNAME="testchgcha";`
- 操作步骤上下文（±2 行原文）：
  L71:
    >       **ADD APN**
    >     3. 将CC绑定到APN上。
    >       **SET APNCHARGECTRL** :
    > - 配置UserProflie下的CC。
    >     1. 配置CC实例。
  L109:
    > 
    > ```
    > SET APNCHARGECTRL: APN="apn-test", CCNAME="testchgcha";
    > ```
    > 

**md：`WSFD-011201/配置话单字段（GGSN_SGW-C_PGW-C）_95923364.md`**
- 数据规划表（该命令的参数行）：
  | **SET APNCHARGECTRL** | APN名称（APN） | apn-test | 已配置数据中获取 | 为APN实例绑定话单字段模板。 |
  | **SET APNCHARGECTRL** | PGW-CDR话单字段模板名（PGWCDRTEMPLATE） | cdrfield-test | 本端规划 | 为APN实例绑定话单字段模板。 |
- 任务示例脚本（该命令行）：
  `SET APNCHARGECTRL: APN="apn-test",PGWCDRTEMPLATE="cdrfield-test";`
- 操作步骤上下文（±2 行原文）：
  L103:
    >       **ADD APN**
    >     b. 配置APN实例绑定话单字段模板。
    >       **SET APNCHARGECTRL**
    > 
    > ## [任务示例](#ZH-CN_OPI_0295923364)
  L136:
    > 
    > ```
    > SET APNCHARGECTRL: APN="apn-test",PGWCDRTEMPLATE="cdrfield-test";
    > ```

**md：`WSFD-011201/调测费率切换功能（GGSN_SGW-C_PGW-C）_95923381.md`**
- 数据规划表（该命令的参数行）：
  | **SET APNCHARGECTRL** | APN名称（APN） | apn-test | 已配置数据中获取 | 每个APN只能绑定一个费率切换组。 |
  | **SET APNCHARGECTRL** | 费率切换组名（TARIFFGRPNAME） | testtariff | 已配置数据中获取 | 每个APN只能绑定一个费率切换组。 |

### WSFD-011202

**md：`WSFD-011202/激活支持热计费功能_28072077.md`**
- 任务示例脚本（该命令行）：
  `SET APNCHARGECTRL: APN="apn-test", ONLINESW=DISABLE, OFFLINESW=ENABLE, PGWOFCTEMPLATE="offlinecharg-test", SGWOFCTEMPLATE="offlinecharg-test", GGSNOFCTEMPLATE="offlinecharg-test", CCNAME="testchgcha";`
- 操作步骤上下文（±2 行原文）：
  L81:
    > 
    > ```
    > SET APNCHARGECTRL: APN="apn-test", ONLINESW=DISABLE, OFFLINESW=ENABLE, PGWOFCTEMPLATE="offlinecharg-test", SGWOFCTEMPLATE="offlinecharg-test", GGSNOFCTEMPLATE="offlinecharg-test", CCNAME="testchgcha";
    > ```

### WSFD-011206

**md：`WSFD-011206/WSFD-011206 支持融合计费参考信息_74013176.md`**
- 操作步骤上下文（±2 行原文）：
  L15:
    > - **[ADD CHARGECHAR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/增加对本地用户、漫游用户、拜访用户所采用的计费属性（ADD CHARGECHAR）_09896809.md)**
    > - [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
    > - [**SET APNCHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md)
    > - [**SET GLBCHARGECHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置对本地用户、漫游用户、拜访用户所采用的计费属性（SET GLBCHARGECHAR）_09896800.md)
    > - [**ADD TNFINS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例管理/增加目标NF实例（ADD TNFINS）_09652354.md)

**md：`WSFD-011206/使能融合计费功能_77691175.md`**
- 数据规划表（该命令的参数行）：
  | **SET APNCHARGECTRL** | APN名称（APN） | apn-test | 已配置数据中获取 | 配置DNN实例的融合计费方式。在DNN中配置INHERIT则计费方式继承基于计费属性的配置。 |
  | **SET APNCHARGECTRL** | 融合计费开关（CONVERGEDSW） | ENABLE | 全网规划 | 配置DNN实例的融合计费方式。在DNN中配置INHERIT则计费方式继承基于计费属性的配置。 |
  | **SET APNCHARGECTRL** | 业务申请上报模式（RGAPPLIED） | ONLINERGONLY | 全网规划 | 说明：- 当“RGAPPLIED”配置为“DEFAULT”时，当URRGROUP下同时配置离线和在线URR，会优先选择在线URR。<br>- 当“RGAPPLIED”配置为“ONLINERGONLY”或“OFFLINERGONLY”时，URRGROUP下建议同时配置离线和在线URR。 |
- 任务示例脚本（该命令行）：
  `SET APNCHARGECTRL: APN="apn-test",CONVERGEDSW=ENABLE,RGAPPLIED=ONLINERGONLY;`
- 操作步骤上下文（±2 行原文）：
  L64:
    >   **SET USRPROFCHARGE**
    > 3. 基于DNN配置计费方式。
    >   **SET APNCHARGECTRL**
    > 4. 基于用户计费属性配置计费方式。
    >   **ADD CHARGEMETHOD**
  L103:
    > 
    > ```
    > SET APNCHARGECTRL: APN="apn-test",CONVERGEDSW=ENABLE,RGAPPLIED=ONLINERGONLY;
    > ```
    > 

**md：`WSFD-011206/配置融合计费模板_93400212.md`**
- 数据规划表（该命令的参数行）：
  | **SET APNCHARGECTRL** | APN名称（APN） | apn-test | 已配置数据中获取 | 基于DNN粒度，将CCT绑定到特定DNN下。 |
  | **SET APNCHARGECTRL** | 融合计费模板（CCTEMPLATE） | cct_test | 已配置数据中获取 | 基于DNN粒度，将CCT绑定到特定DNN下。 |
- 任务示例脚本（该命令行）：
  `SET APNCHARGECTRL: APN="apn-test", CCTEMPLATE="cct_test";`
- 操作步骤上下文（±2 行原文）：
  L85:
    >       **ADD APN**
    >     3. 配置CCT模板绑定DNN。
    >       **SET APNCHARGECTRL**
    > - 配置UserProfile粒度的CCT。
    >     1. 配置CCT模板。
  L134:
    > ```
    > ADD APN: APN="apn-test", HASVPN=DISABLE, HASVPNIPV6=DISABLE, RESTORPGWSWITCH=INHERIT;
    > SET APNCHARGECTRL: APN="apn-test", CCTEMPLATE="cct_test";
    > ```
    > 

**md：`WSFD-011206/配置计费属性CC_90776700.md`**
- 数据规划表（该命令的参数行）：
  | **SET APNCHARGECTRL** | APN名称（APN） | apn-test | 已配置数据中获取 | 将CC绑定到DNN上。每个DNN只能绑定一个计费属性。如果DNN已绑定了计费属性，要绑定其他的计费属性，必须调用<br>**SET APNCHARGECTRL**<br>命令修改绑定关系。 |
  | **SET APNCHARGECTRL** | 计费属性名称（CCNAME） | testchgcha | 已配置数据中获取 | 将CC绑定到DNN上。每个DNN只能绑定一个计费属性。如果DNN已绑定了计费属性，要绑定其他的计费属性，必须调用<br>**SET APNCHARGECTRL**<br>命令修改绑定关系。 |
- 任务示例脚本（该命令行）：
  `SET APNCHARGECTRL: APN="apn-test", CCNAME="testchgcha";`
- 操作步骤上下文（±2 行原文）：
  L69:
    >       **ADD APN**
    >     4. 将CC绑定到DNN上。
    >       **SET APNCHARGECTRL**
    > - 配置UserProfile下的CC。
    >     1. 进入 “MML命令行-UNC” 窗口。
  L102:
    > ADD CHARGECHAR: CCNAME="testchgcha", HOME="0x0800", ROAM="0x0800", VISIT="0x0800", HOMESGSN=DISABLE, ROAMSGSN=DISABLE, VISITSGSN=DISABLE;
    > ADD APN: APN="apn-test", HASVPN=DISABLE, HASVPNIPV6=DISABLE, RESTORPGWSWITCH=INHERIT;
    > SET APNCHARGECTRL: APN="apn-test", CCNAME="testchgcha";
    > ```
    > 

**md：`WSFD-011206/配置费率切换_86411191.md`**
- 数据规划表（该命令的参数行）：
  | **SET APNCHARGECTRL** | APN名称（APN） | apn-test | 已配置数据中获取 | 每个DNN只能绑定一个费率切换组。如果DNN已绑定了费率切换组，要修改为绑定其他的费率切换组，必须先执行<br>**SET APNCHARGECTRL**<br>命令修改原来的绑定关系。 |
  | **SET APNCHARGECTRL** | 费率切换组名（TARIFFGRPNAME） | tar_nb | 已配置数据中获取 | 每个DNN只能绑定一个费率切换组。如果DNN已绑定了费率切换组，要修改为绑定其他的费率切换组，必须先执行<br>**SET APNCHARGECTRL**<br>命令修改原来的绑定关系。 |

**md：`WSFD-011206/调测融合计费的计费会话创建功能_89257219.md`**
- 操作步骤上下文（±2 行原文）：
  L54:
    >           - 如果使能融合计费，请执行[步骤 8](#ZH-CN_OPI_0289257219__step261013496208)。
    >           - 如果未使能融合计费，请执行[步骤 7.b](#ZH-CN_OPI_0289257219__substep1784820385463)。
    >     b. 执行 [**SET CHARGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/设置计费控制配置（SET CHARGECTRL）_09896792.md) 命令，配置当前用户漫游、拜访、本地属性使能N40接口融合计费；执行 [**SET USRPROFCHARGE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md) 、 [**SET APNCHARGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md) 、 [**MOD CHARGEMETHOD**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费属性计费控制/修改计费方式（MOD CHARGEMETHOD）_09896796.md) 命令，配置当前用户按照规划基于User Profile或DNN或CC使能融合计费，请再次执行 [步骤 3](#ZH-CN_OPI_0289257219__step2585105420194) 。
    > 8. 检查用户N40接口是否开启了用户激活创建计费会话功能。
    >     a. 执行 [**LST CCT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/查询融合计费模板（LST CCT）_09653820.md) 命令，查询与当前用户所使用的融合计费模板对应的 “CHF交互使能开关” 是否为 “激活发送” 。

### WSFD-011309

**md：`WSFD-011309/激活支持用户属性反射_28361026.md`**
- 任务示例脚本（该命令行）：
  `SET APNCHARGECTRL:APN="apn-test", GCDRTEMPLATE="cdr-field-test", PGWCDRTEMPLATE="cdr-field-test", SGWCDRTEMPLATE="cdr-field-test";`
- 操作步骤上下文（±2 行原文）：
  L52:
    >   [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > 7. 配置APN实例绑定话单字段模板。
    >   [**SET APNCHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0228361026)
  L95:
    > 
    > ```
    > SET APNCHARGECTRL:APN="apn-test", GCDRTEMPLATE="cdr-field-test", PGWCDRTEMPLATE="cdr-field-test", SGWCDRTEMPLATE="cdr-field-test";
    > ```

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - **[ADD CHARGECHAR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/增加对本地用户、漫游用户、拜访用户所采用的计费属性（ADD CHARGECHAR）_09896809.md)**
    > - [**SET CHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/设置计费控制配置（SET CHARGECTRL）_09896792.md)
    > - [**SET APNCHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md)
    > - **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)**
    > - [**ADD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - **[ADD CHARGECHAR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/增加对本地用户、漫游用户、拜访用户所采用的计费属性（ADD CHARGECHAR）_09896809.md)**
    > - [**SET CHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/设置计费控制配置（SET CHARGECTRL）_09896792.md)
    > - [**SET APNCHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md)
    > - **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)**
    > - [**ADD DCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)

**md：`WSFD-109001/配置在线计费模板_95923574.md`**
- 数据规划表（该命令的参数行）：
  | **SET APNCHARGECTRL** | APN名称（APN） | apn-test | 已配置数据中获取 | APN实例绑定DCC Template模板。 |
  | **SET APNCHARGECTRL** | DCC模板名称（DCCTEMPLATE） | dcc-test | 已配置数据中获取 | APN实例绑定DCC Template模板。 |
- 任务示例脚本（该命令行）：
  `SET APNCHARGECTRL:APN="apn-test",DCCTEMPLATE="dcc-test";`
- 操作步骤上下文（±2 行原文）：
  L82:
    >   **ADD GLBDCCTEMPLATE**
    > 3. 配置DCC Template模板绑定APN实例。
    >   **SET APNCHARGECTRL**
    > 4. 配置DCC Template模板绑定UserProfile实例。
    >     a. 指定UserProfile实例。
  L136:
    > 
    > ```
    > SET APNCHARGECTRL:APN="apn-test",DCCTEMPLATE="dcc-test";
    > ```
    > 

**md：`WSFD-109001/配置普通在线计费实例_95923459.md`**
- 数据规划表（该命令的参数行）：
  | **SET APNCHARGECTRL** | APN名称（APN） | apn-test | 本端规划 | 配置APN实例得在线计费方式。 |
  | **SET APNCHARGECTRL** | 在线计费开关（ONLINESW） | ENABLE | 本端规划 | 配置APN实例得在线计费方式。 |
  | **SET APNCHARGECTRL** | DCC模板名称（DCCTEMPLATE） | dcc-test | 已配置数据中获取 | 配置APN实例得在线计费方式。 |
  | **SET APNCHARGECTRL** | 计费属性名称（CCNAME） | testchgcha | 已配置数据中获取 | 配置APN实例得在线计费方式。 |
- 任务示例脚本（该命令行）：
  `SET APNCHARGECTRL: APN="apn-test", ONLINESW=ENABLE, DCCTEMPLATE="dcc-test", CCNAME="testchgcha";`
- 操作步骤上下文（±2 行原文）：
  L128:
    >   > 对于全局粒度的普通在线计费配置步骤，没有绑定动作，不同的是采用的是全局DCC模板 **MOD DCCTEMPLATE** 。
    >   为APN实例"apn-test"绑定计费属性、计费方式、计费模板。
    >   **SET APNCHARGECTRL**
    >   > **说明**
    >   > 针对同一个用户， **ADD CHARGECHAR** 和 **ADD CHARGEMETHOD** 配置的结果要保持一致，要么是 “ONLINE” ，要么是 “OFFLINE” ，或者两者同时使能，如果不一致将导致用户计费方式错误。
  L192:
    > 8. 为APN实例"apn-test"绑定计费属性、计费方式、DCC模板。
    >   ```
    >   SET APNCHARGECTRL: APN="apn-test", ONLINESW=ENABLE, DCCTEMPLATE="dcc-test", CCNAME="testchgcha";
    >   ```

**md：`WSFD-109001/配置离线_在线计费方式（GGSN_PGW-C）_15408914.md`**
- 数据规划表（该命令的参数行）：
  | **SET APNCHARGECTRL** | APN名称（APN） | apn-test | 已配置数据中获取 | 配置APN实例得离线计费方式。<br>- OFFLINESW默认值都是INHERIT。<br>- 在APN中配置INHERIT则计费方式继承基于计费属性的配置。 |
  | **SET APNCHARGECTRL** | 离线计费开关（OFFLINESW） | ENABLE | 全网规划 | 配置APN实例得离线计费方式。<br>- OFFLINESW默认值都是INHERIT。<br>- 在APN中配置INHERIT则计费方式继承基于计费属性的配置。 |
  | **SET APNCHARGECTRL** | APN名称（APN） | apn-test | 已配置数据中获取 | 配置APN实例的在线计费方式。<br>- ONLINESW默认值都是INHERIT。<br>- 在APN中配置INHERIT则计费方式继承基于计费属性的配置。 |
  | **SET APNCHARGECTRL** | 在线计费开关（ONLINESW） | ENABLE | 全网规划 | 配置APN实例的在线计费方式。<br>- ONLINESW默认值都是INHERIT。<br>- 在APN中配置INHERIT则计费方式继承基于计费属性的配置。 |
- 任务示例脚本（该命令行）：
  `SET APNCHARGECTRL: APN="apn-test",OFFLINESW=ENABLE;`
  `SET APNCHARGECTRL: APN="apn-test", ONLINESW=ENABLE;`
  `SET APNCHARGECTRL: APN="apn-test",ONLINESW=ENABLE, OFFLINESW=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L89:
    >   **SET USRPROFCHARGE**
    > 3. 基于APN使能GGSN/PGW-C的离线/在线计费方式。
    >   **SET APNCHARGECTRL**
    > 4. 基于用户计费属性使能GGSN/PGW-C的离线/在线计费方式。
    >   **ADD CHARGEMETHOD**
  L148:
    > 
    >   ```
    >   SET APNCHARGECTRL: APN="apn-test",OFFLINESW=ENABLE;
    >   ```
    >   //任务三：配置基于用户计费属性使能GGSN/PGW-C的离线计费方式。
  L184:
    > 
    >   ```
    >   SET APNCHARGECTRL: APN="apn-test", ONLINESW=ENABLE;
    >   ```
    >   //任务三：配置基于用户计费属性的在线计费方式。

**md：`WSFD-109001/配置计费属性CC（GGSN_SGW-C_PGW-C）_15408915.md`**
- 数据规划表（该命令的参数行）：
  | **SET APNCHARGECTRL** | APN名称（APN） | apn-test | 已配置数据中获取 | 将CC绑定到APN上。每个APN只能绑定一个计费属性。如果APN已绑定了计费属性，要绑定其他的计费属性，必须调用<br>**SET APNCHARGECTRL**<br>命令修改绑定关系。 |
  | **SET APNCHARGECTRL** | 计费属性名称（CCNAME） | testchgcha | 已配置数据中获取 | 将CC绑定到APN上。每个APN只能绑定一个计费属性。如果APN已绑定了计费属性，要绑定其他的计费属性，必须调用<br>**SET APNCHARGECTRL**<br>命令修改绑定关系。 |
- 任务示例脚本（该命令行）：
  `SET APNCHARGECTRL: APN="apn-test", CCNAME="testchgcha";`
- 操作步骤上下文（±2 行原文）：
  L71:
    >       **ADD APN**
    >     3. 将CC绑定到APN上。
    >       **SET APNCHARGECTRL** :
    > - 配置UserProflie下的CC。
    >     1. 配置CC实例。
  L109:
    > 
    > ```
    > SET APNCHARGECTRL: APN="apn-test", CCNAME="testchgcha";
    > ```
    > 

**md：`WSFD-109001/配置基于CC+用户号段选择OCS_95923602.md`**
- 数据规划表（该命令的参数行）：
  | **SET APNCHARGECTRL** | APN名称（APN） | apn2<br>apn3 | 已配置数据中获取 | APN实例绑定DCC Template模板。 |
  | **SET APNCHARGECTRL** | DCC模板名称（DCCTEMPLATE） | dcctemp01<br>dcctemp02 | 已配置数据中获取 | APN实例绑定DCC Template模板。 |
- 任务示例脚本（该命令行）：
  `SET APNCHARGECTRL:APN="apn2",DCCTEMPLATE="dcctemp01";`
  `SET APNCHARGECTRL:APN="apn3",DCCTEMPLATE="dcctemp02";`
- 操作步骤上下文（±2 行原文）：
  L92:
    >       **ADD APN**
    >     b. 绑定DCC模板。
    >       **SET APNCHARGECTRL**
    > 
    > ## [任务示例](#ZH-CN_OPI_0295923602)
  L187:
    >   ```
    >   ```
    >   SET APNCHARGECTRL:APN="apn2",DCCTEMPLATE="dcctemp01";
    >   ```
    >   ```
  L193:
    >   ```
    >   ```
    >   SET APNCHARGECTRL:APN="apn3",DCCTEMPLATE="dcctemp02";
    >   ```
    > 5. 配置虚拟APN。

**md：`WSFD-109001/配置CCR消息中携带的参数_95923469.md`**
- 数据规划表（该命令的参数行）：
  | **SET APNCHARGECTRL** | APN名称（APN） | apn-test | 已配置数据中获取 | APN实例绑定DCC Template模板。 |
  | **SET APNCHARGECTRL** | DCC模板名称（DCCTEMPLATE） | dcc-test | 已配置数据中获取 | APN实例绑定DCC Template模板。 |
- 任务示例脚本（该命令行）：
  `SET APNCHARGECTRL:APN="apn-test",DCCTEMPLATE="dcc-test";`
- 操作步骤上下文（±2 行原文）：
  L81:
    > 2. 为APN实例apn-test绑定DCC template模板。
    >   ```
    >   SET APNCHARGECTRL:APN="apn-test",DCCTEMPLATE="dcc-test";
    >   ```

**md：`WSFD-109001/配置CCR触发场景_95923545.md`**
- 数据规划表（该命令的参数行）：
  | **SET APNCHARGECTRL** | APN名称（APN） | apn-test | 已配置数据中获取 | APN实例绑定DCC Template模板。 |
  | **SET APNCHARGECTRL** | DCC模板名称（DCCTEMPLATE） | dcc-test | 已配置数据中获取 | APN实例绑定DCC Template模板。 |
- 任务示例脚本（该命令行）：
  `SET APNCHARGECTRL:APN="apn-test",DCCTEMPLATE="dcc-test";`
- 操作步骤上下文（±2 行原文）：
  L144:
    > 
    > ```
    > SET APNCHARGECTRL:APN="apn-test",DCCTEMPLATE="dcc-test";
    > ```
    > 

## ④ 自动比对
- 命令真相参数（19）：['APN', 'CCNAME', 'CCTEMPLATE', 'CONVERGEDSW', 'DCCTEMPLATE', 'GCDRTEMPLATE', 'GGSNOFCTEMPLATE', 'N40MSGTEMP', 'OFFLINESW', 'ONLINESW', 'PGWCDRTEMPLATE', 'PGWOFCTEMPLATE', 'QBCSW', 'RGAPPLIED', 'SERVINGCCT', 'SGWCDRTEMPLATE', 'SGWOFCTEMPLATE', 'SMFOFCTEMPLATE', 'TARIFFGRPNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 33, '全网规划': 6, '本端规划': 3}（多值→atom 应考虑 decision_driven）
