# 命令证据包：ADD AMUEPLCYCTRL
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/增加AM策略和UE策略控制参数（ADD AMUEPLCYCTRL）_09652143.md`
> 用该命令的特性数：4

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：AMF**

该命令用于为指定的用户（群）或者网络切片配置AM策略和UE策略的控制参数。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 最多可输入128条记录。
- AMF支持基于用户属性（如号段）或网络切片指定AM策略或者UE策略的控制参数，其中基于网络切片的控制方式仅适用于整网用户，且优先级低于基于用户属性的控制方式。
- 当基于“网络切片群组标识”建立AM策略或者UE策略时，需要将用户所有可用切片（Allowed NSSAI）通过ADD PLCYNSGRPMEM配置在同一群组下。
- 本命令

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| SUBRANGE | 用户范围 | global_planned | required | 无 | <br>- “ALL_USER（所有用户）”：所有用户 |
| IMSIPRE | IMSI前缀 | global_planned | conditional | 无 | 字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。 |
| MSISDNPRE | MSISDN前缀 | global_planned | conditional | 无 | 字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。 |
| NSGRPID | 网络切片群组标识 | global_planned | conditional | 0 | 整数类型，取值范围是0~16。0用于表示无效的网络切片群组，即不按照网络切片对AM策略或者UE策略进 |
| ISAMASSOC | 是否建立AM策略偶联 | global_planned | optional | NO | <br>- “NO（否）”：否 |
| ISUEASSOC | 是否建立UE策略偶联 | global_planned | optional | NO | <br>- “NO（否）”：否 |
| AMFAILPLCY | AM策略建立/更新失败处理策略 | global_planned | optional | LOCAL_OR_SUB_AMPLCY | <br>- “LOCAL_OR_SUB_AMPLCY（使用本地配置或签约的AM策略）”：AMF向PC |
| UEFAILPLCY | UE策略建立/更新失败处理策略 | global_planned | optional | NOPROCESS | <br>- “NOPROCESS（不处理异常）”：忽略UE策略创建/更新失败，不进行异常处理，用户移 |
| AMTERPLCY | AM策略终止处理策略 | global_planned | optional | 无 | <br>- “LOCAL_OR_SUB_AMPLCY（使用本地配置或签约的AM策略）”：AMF向PC |
| UETERPLCY | UE策略终止处理策略 | global_planned | optional | 无 | <br>- “NOPROCESS（不处理异常）”：忽略UE策略创建/更新失败，不进行异常处理，用户移 |
| MECTOMALLSW | 是否支持MECToMall | local_planned | optional | 无 | <br>- “NO（否）”：否 |
| NEARBYACCSW | 是否支持就近接入 | global_planned | optional | 无 | <br>- “NO（否）”：否 |
| NEARBYKEYWD | 就近接入关键字 | global_planned | conditional | 无 | 字符串类型，输入长度范围是0~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只 |
| NEARBYHPCFSW | 就近接入是否发现H-PCF | local_planned | conditional | 无 | <br>- “NO（否）”：否 |
| DNNAMPLCYSW | 基于DNN的创建AM策略偶联开关 | global_planned | optional | 无 | <br>- “NO（否）”：否 |
| DNNAMPLCYKEYWD | DNN关键字 | global_planned | conditional | 无 | 字符串类型，输入长度范围是1~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只 |
| REGPDUREASW | INTER注册场景PDU会话重建开关 | local_planned | conditional | NO | <br>- “NO（否）”：否 |
| LOCAMPLCYSW | 跨省漫游用户是否支持MECToMall | global_planned | optional | 无 | <br>- “NO（否）”：否 |
| DNNUEPLCYSW | 基于DNN的创建UE策略偶联开关 | global_planned | optional | 无 | <br>- “NO（否）”：否 |
| DNNUEPLCYKEYWD | UE策略的DNN关键字 | global_planned | conditional | 无 | 字符串类型，输入长度范围是1~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只 |
| DESC | 描述信息 | local_planned | optional | 无 | 字符串类型，输入长度范围是0~32。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-223003

**md：`WSFD-223003/WSFD-223003 基于漫游地动态签约的分流策略控制特性参考信息_52923849.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - **[ADD NGUSRGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/通用配置管理/用户群组标识管理/增加5G用户群（ADD NGUSRGRP）_44006475.md)**
    > - **[ADD NGUSRGRPMEM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/通用配置管理/用户群组成员管理/增加5G用户群成员（ADD NGUSRGRPMEM）_44006476.md)**
    > - **[ADD AMUEPLCYCTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/增加AM策略和UE策略控制参数（ADD AMUEPLCYCTRL）_09652143.md)**
    > - **[ADD PCFSELPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md)**
    > - **[ADD ALLOWDNN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/本地分流管理/增加允许本地专网分流的DNN（ADD ALLOWDNN）_42502264.md)**

**md：`WSFD-223003/部署基于漫游地动态签约的分流策略控制（AMF）_82619543.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD AMUEPLCYCTRL](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/增加AM策略和UE策略控制参数（ADD AMUEPLCYCTRL）_09652143.md)** | SUBRANGE（用户范围） | IMSI_PREFIX | 全网规划 | 配置AM策略。 |
  | **[ADD AMUEPLCYCTRL](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/增加AM策略和UE策略控制参数（ADD AMUEPLCYCTRL）_09652143.md)** | IMSIPRE（IMSI前缀） | 123456 | 全网规划 | 配置AM策略。 |
  | **[ADD AMUEPLCYCTRL](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/增加AM策略和UE策略控制参数（ADD AMUEPLCYCTRL）_09652143.md)** | ISAMASSOC（是否建立AM策略偶联） | YES | 全网规划 | 配置AM策略。 |
- 任务示例脚本（该命令行）：
  `ADD AMUEPLCYCTRL: SUBRANGE=IMSI_PREFIX, IMSIPRE="123456", ISUEASSOC=YES;`
- 操作步骤上下文（±2 行原文）：
  L57:
    > 
    > ```
    > ADD AMUEPLCYCTRL: SUBRANGE=IMSI_PREFIX, IMSIPRE="123456", ISUEASSOC=YES;
    > ```
    > 

### WSFD-010201

**md：`WSFD-010201/初始注册_19356600.md`**
- 操作步骤上下文（±2 行原文）：
  L263:
    >   | userLoc | 表示用户上线时所在的位置。 |
    >   | suppFeat | 表示PCF和AMF之间协商的N15接口能力，支持的功能列表。 |
    >   相关配置：UE策略关联相关配置参见UNC命令：ADD AMUEPLCYCTRL。
    > 37. 消息交互：PCF发送[Npcf_UEPolicyControl_Create](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Npcf/N15/Npcf_UEPolicyControl_Create_17785211.md)给新侧AMF。
    >   关键信元：

**md：`WSFD-010201/移动注册更新_69433041.md`**
- 操作步骤上下文（±2 行原文）：
  L240:
    >   | userLoc | 表示用户上线时所在的位置。 |
    >   | suppFeat | 表示PCF和AMF之间协商的N15接口能力，支持的功能列表。 |
    >   相关配置：UE策略关联相关配置参见UNC命令：ADD AMUEPLCYCTRL。
    > 34. 消息交互：PCF发送[Npcf_UEPolicyControl_Create](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Npcf/N15/Npcf_UEPolicyControl_Create_17785211.md)给新侧AMF。
    >   触发条件：PCF收到请求消息后进行响应，返回建立结果。

### WSFD-230001

**md：`WSFD-230001/WSFD-230001 动态UE Logo下发参考信息_45929684.md`**
- 操作步骤上下文（±2 行原文）：
  L23:
    > - [ADD PCFSELPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md)
    > - [ADD NITZPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NITZ管理/NITZ策略管理/增加NITZ策略（ADD NITZPLCY）_09652255.md)
    > - [ADD AMUEPLCYCTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/增加AM策略和UE策略控制参数（ADD AMUEPLCYCTRL）_09652143.md)
    > - [MOD NGMNO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/运营商管理/5G 移动网络运营商管理/修改5G模式移动网络运营商信息（MOD NGMNO）_09654365.md)
    > - [SET AMFSBICMPT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/AMF服务化接口兼容性参数管理/设置AMF服务化接口兼容性参数（SET AMFSBICMPT）_98011756.md)

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（5G）参考信息_72466541.md`**
- 操作步骤上下文（±2 行原文）：
  L21:
    > - [**ADD GUAMI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/本局信息管理/AMF/AMF全局标识符管理/增加AMF全局标识（ADD GUAMI）_09653726.md)
    > - [**ADD PCFSELPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md)
    > - [**ADD AMUEPLCYCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/增加AM策略和UE策略控制参数（ADD AMUEPLCYCTRL）_09652143.md)
    > - [**MOD AMUEPLCYCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/修改AM策略和UE策略控制参数（MOD AMUEPLCYCTRL）_09654427.md)
    > - [**SET AMFPLCYFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AMF策略功能管理/设置AMF策略功能（SET AMFPLCYFUNC）_96792665.md)

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD AMUEPLCYCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/增加AM策略和UE策略控制参数（ADD AMUEPLCYCTRL）_09652143.md) | 用户范围（SUBRANGE） | HOME_USER | 全网规划 | 在AMF上配置AM策略和UE策略控制参数的用户范围。 |
  | [**ADD AMUEPLCYCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/增加AM策略和UE策略控制参数（ADD AMUEPLCYCTRL）_09652143.md) | 网络切片群组标识（NSGRPID） | 0 | 全网规划 | 0用于表示无效的网络切片群组，即不按照网络切片对AM策略或者UE策略进行控制。 |
  | [**ADD AMUEPLCYCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/增加AM策略和UE策略控制参数（ADD AMUEPLCYCTRL）_09652143.md) | 是否建立AM策略偶联（ISAMASSOC） | YES | 全网规划 | 针对指定的5G用户应用网络侧规划的AM策略时，设置为<br>“YES”<br>。 |
  | [**ADD AMUEPLCYCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/增加AM策略和UE策略控制参数（ADD AMUEPLCYCTRL）_09652143.md) | 是否建立UE策略偶联（ISUEASSOC） | YES | 全网规划 | 针对指定的5G用户应用网络侧规划的UE策略时，设置为<br>“YES”<br>。 |
  | [**ADD AMUEPLCYCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/增加AM策略和UE策略控制参数（ADD AMUEPLCYCTRL）_09652143.md) | 描述信息（DESC） | Enable UE Policy for Home Subscribers | 本端规划 | 描述配置AM策略和UE策略控制参数的用户（群），便于记忆。 |
- 任务示例脚本（该命令行）：
  `ADD AMUEPLCYCTRL: SUBRANGE=HOME_USER, NSGRPID=0, ISAMASSOC=YES, ISUEASSOC=YES, DESC="Enable UE Policy for Home Subscribers";`
  `ADD AMUEPLCYCTRL: SUBRANGE=HOME_USER, NSGRPID=0, ISAMASSOC=YES, ISUEASSOC=YES, DESC="Enable UE Policy for Home Subscribers";`
- 操作步骤上下文（±2 行原文）：
  L117:
    >       [**ADD PCFSELPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md)
    >     4. 配置应用网络侧规划的AM策略/UE策略的用户群。默认不使用网络侧规划的AM策略/UE策略。
    >       [**ADD AMUEPLCYCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/增加AM策略和UE策略控制参数（ADD AMUEPLCYCTRL）_09652143.md)
    >           - 应用网络侧规划的AM策略时，将“ISAMASSOC”设置为“YES”。
    >           - 应用网络侧规划的UE策略时，将“ISUEASSOC”设置为“YES”。
  L284:
    > 
    > ```
    > ADD AMUEPLCYCTRL: SUBRANGE=HOME_USER, NSGRPID=0, ISAMASSOC=YES, ISUEASSOC=YES, DESC="Enable UE Policy for Home Subscribers";
    > ```
    > 
  L331:
    > 
    > ```
    > ADD AMUEPLCYCTRL: SUBRANGE=HOME_USER, NSGRPID=0, ISAMASSOC=YES, ISUEASSOC=YES, DESC="Enable UE Policy for Home Subscribers";
    > ```
    > 

## ④ 自动比对
- 命令真相参数（21）：['AMFAILPLCY', 'AMTERPLCY', 'DESC', 'DNNAMPLCYKEYWD', 'DNNAMPLCYSW', 'DNNUEPLCYKEYWD', 'DNNUEPLCYSW', 'IMSIPRE', 'ISAMASSOC', 'ISUEASSOC', 'LOCAMPLCYSW', 'MECTOMALLSW', 'MSISDNPRE', 'NEARBYACCSW', 'NEARBYHPCFSW', 'NEARBYKEYWD', 'NSGRPID', 'REGPDUREASW', 'SUBRANGE', 'UEFAILPLCY', 'UETERPLCY']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 7, '本端规划': 1}（多值→atom 应考虑 decision_driven）
