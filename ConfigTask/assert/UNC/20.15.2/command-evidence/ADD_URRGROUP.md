# 命令证据包：ADD URRGROUP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md`
> 用该命令的特性数：6

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于新增使用量上报规则组，通过该命令可以指定上下行发起使用的URR名称，配置给用户使用该组规则，指定上下行报文如何进行PCC策略及计费。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为40000。
- 每个“使用量上报规则组”支持在线和离线混合计费。
- 配置使用量上报规则组之前，上下行使用量上报规则信息必须已经预先在ADD URR命令中配置。如果不输入下行使用量上报规则信息，实际使用时采用上行使用量上报规则信息。
- UPURRNAME1，DOWNURRNAME1，UPURRNAME2，DOWNURRNAME2，UPURRNA

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| URRGROUPNAME | 使用量上报规则组名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| UPURRNAME1 | 上行发起URR名称1 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| UPURRNAME2 | 上行发起URR名称2 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| UPURRNAME3 | 上行发起URR名称3 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| DOWNURRNAME1 | 下行发起URR名称1 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| DOWNURRNAME2 | 下行发起URR名称2 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| DOWNURRNAME3 | 下行发起URR名称3 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| NOCHARGINGFLAG | 不计费标记 | local_planned | optional | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-211009

**md：`WSFD-211009/激活基于业务累计流量的策略控制_27915156.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD URRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md) | 使用量上报规则组名称（URRGROUPNAME） | urrgrp_01 | 本端规划 | 存在多条记录时，该参数不能重复。 |
  | [**ADD URRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md) | 上行发起URR名称1（UPURRNAME1） | urr_01 | 已配置数据中获取 | 使用<br>[**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)<br>定义的URRNAME。 |
  | [**ADD URRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md) | 下行发起URR名称1（DOWNURRNAME1） | urr_01 | 已配置数据中获取 | 使用<br>[**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)<br>定义的URRNAME。 |

### WSFD-011201

**md：`WSFD-011201/配置离线计费的费率标识（GGSN_SGW-C_PGW-C）_98555879.md`**
- 数据规划表（该命令的参数行）：
  | **ADD URRGROUP** | 使用量上报规则组名称（URRGROUPNAME） | urrgroup1 | 本端规划 | 配置URR组，将上下行URR绑定到URR组上。<br>如果上下行使用不同的URR，则两者必须同时为在线计费或离线计费。 |
  | **ADD URRGROUP** | 上行发起URR名称1（UPURRNAME1） | offlineURR | 已配置数据中获取 | 配置URR组，将上下行URR绑定到URR组上。<br>如果上下行使用不同的URR，则两者必须同时为在线计费或离线计费。 |
  | **ADD URRGROUP** | 下行发起URR名称1（DOWNURRNAME1） | offlineURR | 已配置数据中获取 | 配置URR组，将上下行URR绑定到URR组上。<br>如果上下行使用不同的URR，则两者必须同时为在线计费或离线计费。 |
- 任务示例脚本（该命令行）：
  `ADD URRGROUP: URRGROUPNAME="urrgroup1", UPURRNAME1="offlineURR", DOWNURRNAME1="offlineURR";`
  `ADD URRGROUP: URRGROUPNAME="urrgroup1", UPURRNAME1="offlineURR", DOWNURRNAME1="offlineURR";`
- 操作步骤上下文（±2 行原文）：
  L70:
    >             **ADD URR**
    >           b. 配置URR组，将上下行URR绑定到URR组上。上下行可以使用不同的URR。
    >             **ADD URRGROUP**
    >     2. 配置没有绑定Rule的UserProfile，绑定UserProfile的缺省URR组。
    >           a. 配置UserProfile，注意该UserProfile不配置Rule。
  L94:
    >             **ADD URR**
    >           b. 配置URR组，将上下行URR绑定到URR组上。上下行可以使用不同的URR。
    >             **ADD URRGROUP**
    >     3. 配置内容计费使用的Rule，将URR组绑定到对应的Rule上。
    >           a. 配置Rule绑定的PCC策略组，将URR组绑定到PCC策略组。
  L135:
    >   ```
    >   ADD URR: URRNAME="offlineURR", URRID=1000, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=RGSID, RG=10, SID=20, OFFMETERINGTYPE=VOLUME;
    >   ADD URRGROUP: URRGROUPNAME="urrgroup1", UPURRNAME1="offlineURR", DOWNURRNAME1="offlineURR";
    >   ```
    >   //配置UserProfile、UserProfile组及APN，依次将URR组绑定到UserProfile、UserProfile组及APN上。

### WSFD-011206

**md：`WSFD-011206/WSFD-011206 支持融合计费参考信息_74013176.md`**
- 操作步骤上下文（±2 行原文）：
  L24:
    > - **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)**
    > - [**SET GLBURRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/全局使用量上报规则组/设置全局使用量上报规则组（SET GLBURRGROUP）_09897187.md)
    > - [**ADD URRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)
    > - [**SET URRGRPBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/设置用户模板的计费属性绑定关系（SET URRGRPBINDING）_09897209.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)

**md：`WSFD-011206/配置SMF与CHF交互的条件和内容_93420840.md`**
- 数据规划表（该命令的参数行）：
  | **ADD URRGROUP** | 使用量上报规则组名称（URRGROUPNAME） | urrgroup_test | 本端规划 | - |
  | **ADD URRGROUP** | 上行发起URR名称1（UPURRNAME1） | urr_test | 已配置数据中获取 | 使用<br>**ADD URR**<br>命令定义的<br>“URRNAME”<br>。<br>上行和下行可以使用相同的URR名称，也可以使用不同的URR名称。<br>上行URR名称不能相同，下行URR名称不能相同。<br>根据业务套餐规划，至少配置1个名称。 |
  | **ADD URRGROUP** | 下行发起URR名称1（DOWNURRNAME1） | urr_test | 已配置数据中获取 | 使用<br>**ADD URR**<br>命令定义的<br>“URRNAME”<br>。<br>上行和下行可以使用相同的URR名称，也可以使用不同的URR名称。<br>上行URR名称不能相同，下行URR名称不能相同。<br>根据业务套餐规划，至少配置1个名称。 |
- 任务示例脚本（该命令行）：
  `ADD URRGROUP: URRGROUPNAME="urrgroup_test", UPURRNAME1="urr_test", DOWNURRNAME1="urr_test";`
- 操作步骤上下文（±2 行原文）：
  L76:
    >     a. 配置URR组合URR，指定需预申请配额的RG。
    >       **ADD URR**
    >       **ADD URRGROUP**
    >     b. 配置UserProfile。
    >       **ADD USERPROFILE**
  L115:
    > ```
    > ADD URR: URRNAME="urr_test", URRID=1111, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=111, ONLMETERINGTYPE=VOLUME;
    > ADD URRGROUP: URRGROUPNAME="urrgroup_test", UPURRNAME1="urr_test", DOWNURRNAME1="urr_test";
    > ADD USERPROFILE: USERPROFILENAME="up_test", UPTYPE=PCC;
    > SET CTXSTARTRATING: USERPROFILENAME="up_test", CTXRURRGRPNAME1="urrgroup_test";

**md：`WSFD-011206/配置融合计费费率标识_93360308.md`**
- 数据规划表（该命令的参数行）：
  | **ADD URRGROUP** | 使用量上报规则组名称（URRGROUPNAME） | UrrGp_URL<br>UrrGp_IMS<br>UrrGp_any<br>UrrGp_abnormal | 本端规划 | 配置URRGROUP。<br>说明：- 当**SET USRPROFCHARGE**、**SET APNCHARGECTRL**、**ADD CHARGEMETHOD**命令的“RGAPPLIED”配置为“DEFAULT”时，URRGROUP下不能同时配置离线和在线URR。<br>- 当“RGAPPLIED”配置为“ONLINERGONLY”或“OFFLINERGONLY”时，URRGROUP下建议同时配置离线和在线URR。 |
  | **ADD URRGROUP** | 上行发起URR名称1（UPURRNAME1） | urr_online_URL<br>urr_online_IMS<br>urr_online_any<br>URR_abnormal_online | 已配置数据中获取 | 配置URRGROUP。<br>说明：- 当**SET USRPROFCHARGE**、**SET APNCHARGECTRL**、**ADD CHARGEMETHOD**命令的“RGAPPLIED”配置为“DEFAULT”时，URRGROUP下不能同时配置离线和在线URR。<br>- 当“RGAPPLIED”配置为“ONLINERGONLY”或“OFFLINERGONLY”时，URRGROUP下建议同时配置离线和在线URR。 |
  | **ADD URRGROUP** | 下行发起URR名称1（DOWNURRNAME1） | urr_online_URL<br>urr_online_IMS<br>urr_online_any<br>URR_abnormal_online | 已配置数据中获取 | 配置URRGROUP。<br>说明：- 当**SET USRPROFCHARGE**、**SET APNCHARGECTRL**、**ADD CHARGEMETHOD**命令的“RGAPPLIED”配置为“DEFAULT”时，URRGROUP下不能同时配置离线和在线URR。<br>- 当“RGAPPLIED”配置为“ONLINERGONLY”或“OFFLINERGONLY”时，URRGROUP下建议同时配置离线和在线URR。 |
  | **ADD URRGROUP** | 上行发起URR名称2（UPURRNAME2） | urr_offline_URL<br>urr_offline_IMS<br>urr_offline_any<br>URR_abnormal_offline | 已配置数据中获取 | 配置URRGROUP。<br>说明：- 当**SET USRPROFCHARGE**、**SET APNCHARGECTRL**、**ADD CHARGEMETHOD**命令的“RGAPPLIED”配置为“DEFAULT”时，URRGROUP下不能同时配置离线和在线URR。<br>- 当“RGAPPLIED”配置为“ONLINERGONLY”或“OFFLINERGONLY”时，URRGROUP下建议同时配置离线和在线URR。 |
  | **ADD URRGROUP** | 下行发起URR名称2（DOWNURRNAME2） | urr_offline_URL<br>urr_offline_IMS<br>urr_offline_any<br>URR_abnormal_offline | 已配置数据中获取 | 配置URRGROUP。<br>说明：- 当**SET USRPROFCHARGE**、**SET APNCHARGECTRL**、**ADD CHARGEMETHOD**命令的“RGAPPLIED”配置为“DEFAULT”时，URRGROUP下不能同时配置离线和在线URR。<br>- 当“RGAPPLIED”配置为“ONLINERGONLY”或“OFFLINERGONLY”时，URRGROUP下建议同时配置离线和在线URR。 |
- 任务示例脚本（该命令行）：
  `ADD URRGROUP: URRGROUPNAME="UrrGp_URL", UPURRNAME1="urr_online_URL", DOWNURRNAME1="urr_online_URL", UPURRNAME2="urr_offline_URL", DOWNURRNAME2="urr_offline_URL";`
  `ADD URRGROUP: URRGROUPNAME="UrrGp_IMS", UPURRNAME1="urr_online_IMS", DOWNURRNAME1="urr_online_IMS", UPURRNAME2="urr_offline_IMS", DOWNURRNAME2="urr_offline_IMS";`
  `ADD URRGROUP: URRGROUPNAME="UrrGp_any", UPURRNAME1="urr_online_any", DOWNURRNAME1="urr_online_any", UPURRNAME2="urr_offline_any", DOWNURRNAME2="urr_offline_any";`
  `ADD URRGROUP: URRGROUPNAME="UrrGp_abnormal", UPURRNAME1="URR_abnormal_online", DOWNURRNAME1="URR_abnormal_online", UPURRNAME2="URR_abnormal_offline", DOWNURRNAME2="URR_abnormal_offline";`
- 操作步骤上下文（±2 行原文）：
  L91:
    >             **ADD URR**
    >           b. 配置URR组，将URR绑定到URR组上。
    >             **ADD URRGROUP**
    >     2. 配置内容计费使用的Rule，将URR组绑定到对应的Rule上。
    >           a. 配置PCC策略组，将URR组绑定到PCC策略组。
  L158:
    > 
    > ```
    > ADD URRGROUP: URRGROUPNAME="UrrGp_URL", UPURRNAME1="urr_online_URL", DOWNURRNAME1="urr_online_URL", UPURRNAME2="urr_offline_URL", DOWNURRNAME2="urr_offline_URL";
    > ADD URRGROUP: URRGROUPNAME="UrrGp_IMS", UPURRNAME1="urr_online_IMS", DOWNURRNAME1="urr_online_IMS", UPURRNAME2="urr_offline_IMS", DOWNURRNAME2="urr_offline_IMS";
    > ADD URRGROUP: URRGROUPNAME="UrrGp_any", UPURRNAME1="urr_online_any", DOWNURRNAME1="urr_online_any", UPURRNAME2="urr_offline_any", DOWNURRNAME2="urr_offline_any";
  L159:
    > ```
    > ADD URRGROUP: URRGROUPNAME="UrrGp_URL", UPURRNAME1="urr_online_URL", DOWNURRNAME1="urr_online_URL", UPURRNAME2="urr_offline_URL", DOWNURRNAME2="urr_offline_URL";
    > ADD URRGROUP: URRGROUPNAME="UrrGp_IMS", UPURRNAME1="urr_online_IMS", DOWNURRNAME1="urr_online_IMS", UPURRNAME2="urr_offline_IMS", DOWNURRNAME2="urr_offline_IMS";
    > ADD URRGROUP: URRGROUPNAME="UrrGp_any", UPURRNAME1="urr_online_any", DOWNURRNAME1="urr_online_any", UPURRNAME2="urr_offline_any", DOWNURRNAME2="urr_offline_any";
    > ADD URRGROUP: URRGROUPNAME="UrrGp_abnormal", UPURRNAME1="URR_abnormal_online", DOWNURRNAME1="URR_abnormal_online", UPURRNAME2="URR_abnormal_offline", DOWNURRNAME2="URR_abnormal_offline";

### WSFD-109001

**md：`WSFD-109001/配置在线计费的费率标识_95923388.md`**
- 数据规划表（该命令的参数行）：
  | **ADD URRGROUP** | 使用量上报规则组名称（URRGROUPNAME） | urrgroup001 | 本端规划 | 配置URR组，将上下行URR绑定到URR组上。<br>如果上下行使用不同的URR，则两者必须同时为在线计费或离线计费。 |
  | **ADD URRGROUP** | 上行发起URR名称1（UPURRNAME1） | onlineURR | 已配置数据中获取 | 配置URR组，将上下行URR绑定到URR组上。<br>如果上下行使用不同的URR，则两者必须同时为在线计费或离线计费。 |
  | **ADD URRGROUP** | 下行发起URR名称1（DOWNURRNAME1） | onlineURR | 已配置数据中获取 | 配置URR组，将上下行URR绑定到URR组上。<br>如果上下行使用不同的URR，则两者必须同时为在线计费或离线计费。 |
- 任务示例脚本（该命令行）：
  `ADD URRGROUP: URRGROUPNAME="urrgroup001", UPURRNAME1="onlineURR", DOWNURRNAME1="onlineURR";`
  `ADD URRGROUP: URRGROUPNAME="urrgroup001", UPURRNAME1="onlineURR", DOWNURRNAME1="onlineURR";`
- 操作步骤上下文（±2 行原文）：
  L74:
    >             **ADD URR**
    >           b. 配置URR组，将上下行URR绑定到URR组上。上下行可以使用不同的URR。
    >             **ADD URRGROUP**
    >     2. 配置没有绑定Rule的UserProfile，绑定UserProfile的缺省URR组。
    >           a. 配置UserProfile，注意该UserProfile不配置Rule。
  L98:
    >             **ADD URR**
    >           b. 配置URR组，将上下行URR绑定到URR组上。上下行可以使用不同的URR。
    >             **ADD URRGROUP**
    >     3. 配置内容计费使用的Rule，将URR组绑定到对应的Rule上。
    >           a. 配置Rule绑定的PCC策略组，将URR组绑定到PCC策略组。
  L139:
    >   ```
    >   ADD URR: URRNAME="onlineURR", URRID=1100, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=RGSID, ONLINERG=10, ONLINESID=20, ONLMETERINGTYPE=EVENT_VOLUME_TIME;
    >   ADD URRGROUP: URRGROUPNAME="urrgroup001", UPURRNAME1="onlineURR", DOWNURRNAME1="onlineURR";
    >   ```
    >   //配置UserProfile、UserProfile组及APN，依次将URR组绑定到UserProfile、UserProfile组及APN上。

**md：`WSFD-109001/配置普通在线计费实例_95923459.md`**
- 数据规划表（该命令的参数行）：
  | **ADD URRGROUP** | 使用量上报规则组名称（URRGROUPNAME） | urrgroup1 | 本端规划 | 配置URR组，将上下行URR绑定到URR组上。<br>如果上下行使用不同的URR，则两者必须同时为在线计费或离线计费。 |
  | **ADD URRGROUP** | 上行发起URR名称1（UPURRNAME1） | onlineURR | 已配置数据中获取 | 配置URR组，将上下行URR绑定到URR组上。<br>如果上下行使用不同的URR，则两者必须同时为在线计费或离线计费。 |
  | **ADD URRGROUP** | 下行发起URR名称1（DOWNURRNAME1） | onlineURR | 已配置数据中获取 | 配置URR组，将上下行URR绑定到URR组上。<br>如果上下行使用不同的URR，则两者必须同时为在线计费或离线计费。 |
- 任务示例脚本（该命令行）：
  `ADD URRGROUP: URRGROUPNAME="urrgroup1", UPURRNAME1="onlineURR", DOWNURRNAME1="onlineURR";`
- 操作步骤上下文（±2 行原文）：
  L91:
    >       **ADD URR**
    >     b. 配置URR组，将上下行URR绑定到URR组上。上下行可以使用不同的URR。
    >       **ADD URRGROUP**
    > 4. 配置DCC模板。
    >     a. 全局DCC模板。
  L153:
    >   ```
    >   ```
    >   ADD URRGROUP: URRGROUPNAME="urrgroup1", UPURRNAME1="onlineURR", DOWNURRNAME1="onlineURR";
    >   ```
    > 4. 配置DCC模板（配额门限、CCR触发机制）。

**md：`WSFD-109001/配置CCR触发场景_95923545.md`**
- 任务示例脚本（该命令行）：
  `ADD URRGROUP: URRGROUPNAME="urrgroup1", UPURRNAME1="onlineURR", DOWNURRNAME1="onlineURR";`
- 操作步骤上下文（±2 行原文）：
  L94:
    >             **ADD URR**
    >           b. 配置上行和下行发起的业务对应的URR。
    >             **ADD URRGROUP**
    >     3. 配置在线计费用户激活时CCR-I消息中携带指定的费率标识。
    >       **SET CTXSTARTRATING**
  L126:
    > 
    > ```
    > ADD URRGROUP: URRGROUPNAME="urrgroup1", UPURRNAME1="onlineURR", DOWNURRNAME1="onlineURR";
    > ```
    > 

### WSFD-109007

**md：`WSFD-109007/WSFD-109007 支持事件计费参考信息_74112323.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - [**SET CHFINIT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/设置融合计费模板中用户激活相关参数（SET CHFINIT）_09653178.md)
    > - **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)**
    > - [**ADD URRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)

**md：`WSFD-109007/配置事件计费功能_74112321.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD URRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md) | URRGROUPNAME（使用量上报规则组名称） | urrgroup1 | 本端规划 | 配置融合计费和在线计费的URR Group和User Profile。 |
  | [**ADD URRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md) | UPURRNAME1（上行发起URR名称1） | urr1 | 本端规划 | 配置融合计费和在线计费的URR Group和User Profile。 |
  | [**ADD URRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md) | DOWNURRNAME1（下行发起URR名称1） | urr1 | 本端规划 | 配置融合计费和在线计费的URR Group和User Profile。 |
- 任务示例脚本（该命令行）：
  `ADD URRGROUP: URRGROUPNAME="urrgroup1", UPURRNAME1="urr1", DOWNURRNAME1="urr1";`
- 操作步骤上下文（±2 行原文）：
  L77:
    >     a. 配置事件计费的RG使用的URR组及相应URR。
    >       **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)**
    >       [**ADD URRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)
    >     b. 配置UserProfile。
    >       [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
  L130:
    > ```
    > ADD URR: URRNAME="urr1", URRID=1000, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=100, ONLMETERINGTYPE=EVENT;
    > ADD URRGROUP: URRGROUPNAME="urrgroup1", UPURRNAME1="urr1", DOWNURRNAME1="urr1";
    > ADD USERPROFILE:USERPROFILENAME="up-test", UPTYPE=PCC;
    > ```

### WSFD-201207

**md：`WSFD-201207/WSFD-201207 语音PCF_PCRF故障Bypass参考信息_85304300.md`**
- 操作步骤上下文（±2 行原文）：
  L20:
    > **[LST URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/查询URR（LST URR）_09897161.md)**
    > 
    > **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)**
    > 
    > **[RMV URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/删除URR组（RMV URRGROUP）_09897195.md)**

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（Gx接口）_60552093.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 使用量上报规则组名称（URRGROUPNAME） | urrg_signaling_01 | 本端规划 | 增加使用量上报规则组。 |
  | **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 上行发起URR名称1（UPURRNAME1） | urr_signaling_offline | 本端规划 | 增加使用量上报规则组。 |
  | **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 下行发起URR名称1（DOWNURRNAME1） | urr_signaling_offline | 本端规划 | 增加使用量上报规则组。 |
  | **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 上行发起URR名称2（UPURRNAME2） | urr_signaling_online | 本端规划 | 增加使用量上报规则组。 |
  | **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 下行发起URR名称2（DOWNURRNAME2） | urr_signaling_online | 本端规划 | 增加使用量上报规则组。 |
  | **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 使用量上报规则组名称（URRGROUPNAME） | urrg_voice_01 | 本端规划 | 增加使用量上报规则组。 |
  | **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 上行发起URR名称1（UPURRNAME1） | urr_voice_offline | 本端规划 | 增加使用量上报规则组。 |
  | **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 下行发起URR名称1（DOWNURRNAME1） | urr_voice_offline | 本端规划 | 增加使用量上报规则组。 |
  | **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 上行发起URR名称2（UPURRNAME2） | urr_voice_online | 本端规划 | 增加使用量上报规则组。 |
  | **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 下行发起URR名称2（DOWNURRNAME2） | urr_voice_online | 本端规划 | 增加使用量上报规则组。 |
- 任务示例脚本（该命令行）：
  `ADD URRGROUP:URRGROUPNAME="urrg_signaling_01", UPURRNAME1="urr_signaling_offline", DOWNURRNAME1="urr_signaling_offline", UPURRNAME2="urr_signaling_online", DOWNURRNAME2="urr_signaling_online";`
  `ADD URRGROUP:URRGROUPNAME="urrg_voice_01", UPURRNAME1="urr_voice_offline", DOWNURRNAME1="urr_voice_offline", UPURRNAME2="urr_voice_online", DOWNURRNAME2="urr_voice_online";`
  `ADD URRGROUP:URRGROUPNAME="urrg_voice_01", UPURRNAME1="urr_voice_offline", DOWNURRNAME1="urr_voice_offline", UPURRNAME2="urr_voice_online", DOWNURRNAME2="urr_voice_online";`
- 操作步骤上下文（±2 行原文）：
  L196:
    >       [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    >     b. 增加使用量上报规则组。
    >       **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)**
    >     c. 配置PCC策略组。
    >       [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
  L225:
    >       [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    >     b. 增加使用量上报规则组。
    >       **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)**
    >     c. 配置静态PCC策略的QoS参数。
    >       [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)
  L311:
    > 
    >       ```
    >       ADD URRGROUP:URRGROUPNAME="urrg_signaling_01", UPURRNAME1="urr_signaling_offline", DOWNURRNAME1="urr_signaling_offline", UPURRNAME2="urr_signaling_online", DOWNURRNAME2="urr_signaling_online";
    >       ```
    >       //配置PCC策略组。

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（N7接口）_32852169.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 使用量上报规则组名称（URRGROUPNAME） | urrg_signaling_01 | 本端规划 | 增加使用量上报规则组。 |
  | **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 上行发起URR名称1（UPURRNAME1） | urr_signaling_offline | 本端规划 | 增加使用量上报规则组。 |
  | **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 下行发起URR名称1（DOWNURRNAME1） | urr_signaling_offline | 本端规划 | 增加使用量上报规则组。 |
  | **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 上行发起URR名称2（UPURRNAME2） | urr_signaling_online | 本端规划 | 增加使用量上报规则组。 |
  | **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 下行发起URR名称2（DOWNURRNAME2） | urr_signaling_online | 本端规划 | 增加使用量上报规则组。 |
  | **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 使用量上报规则组名称（URRGROUPNAME） | urrg_voice_01 | 本端规划 | 增加使用量上报规则组。 |
  | **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 上行发起URR名称1（UPURRNAME1） | urr_voice_offline | 本端规划 | 增加使用量上报规则组。 |
  | **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 下行发起URR名称1（DOWNURRNAME1） | urr_voice_offline | 本端规划 | 增加使用量上报规则组。 |
  | **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 上行发起URR名称2（UPURRNAME2） | urr_voice_online | 本端规划 | 增加使用量上报规则组。 |
  | **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 下行发起URR名称2（DOWNURRNAME2） | urr_voice_online | 本端规划 | 增加使用量上报规则组。 |
- 任务示例脚本（该命令行）：
  `ADD URRGROUP:URRGROUPNAME="urrg_signaling_01", UPURRNAME1="urr_signaling_offline", DOWNURRNAME1="urr_signaling_offline", UPURRNAME2="urr_signaling_online", DOWNURRNAME2="urr_signaling_online";`
  `ADD URRGROUP:URRGROUPNAME="urrg_voice_01", UPURRNAME1="urr_voice_offline", DOWNURRNAME1="urr_voice_offline", UPURRNAME2="urr_voice_online", DOWNURRNAME2="urr_voice_online";`
  `ADD URRGROUP:URRGROUPNAME="urrg_voice_01", UPURRNAME1="urr_voice_offline", DOWNURRNAME1="urr_voice_offline", UPURRNAME2="urr_voice_online", DOWNURRNAME2="urr_voice_online";`
- 操作步骤上下文（±2 行原文）：
  L215:
    >       [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    >     b. 增加使用量上报规则组。
    >       **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)**
    >     c. 配置PCC策略组。
    >       [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
  L244:
    >       [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    >     b. 增加使用量上报规则组。
    >       **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)**
    >     c. 配置静态PCC策略的QoS参数。
    >       [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)
  L339:
    > 
    >       ```
    >       ADD URRGROUP:URRGROUPNAME="urrg_signaling_01", UPURRNAME1="urr_signaling_offline", DOWNURRNAME1="urr_signaling_offline", UPURRNAME2="urr_signaling_online", DOWNURRNAME2="urr_signaling_online";
    >       ```
    >       //配置PCC策略组。

## ④ 自动比对
- 命令真相参数（8）：['DOWNURRNAME1', 'DOWNURRNAME2', 'DOWNURRNAME3', 'NOCHARGINGFLAG', 'UPURRNAME1', 'UPURRNAME2', 'UPURRNAME3', 'URRGROUPNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 29, '已配置数据中获取': 14}（多值→atom 应考虑 decision_driven）
