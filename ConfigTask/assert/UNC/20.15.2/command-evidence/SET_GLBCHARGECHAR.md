# 命令证据包：SET GLBCHARGECHAR
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置对本地用户、漫游用户、拜访用户所采用的计费属性（SET GLBCHARGECHAR）_09896800.md`
> 用该命令的特性数：4

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于设置对本地用户、漫游用户、拜访用户所采用的计费属性。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。
- 该命令最大记录数为1。
- 基于用户漫游、拜访、本地属性来控制是否提供在线计费和离线计费功能时需要使用SET GLBCHARGECHAR。
- 在5G网络中，当UDM下发签约CC、并且本地基于全局配置CC场景下，本地、漫游、拜访用户选择CC由SET GLBCHARGECHAR命令的HOMESGSN、ROAMSGSN、VISITSGSN控制，当对应参数配置为

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| HOME | 本地用户计费类型 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| ROAM | 漫游用户计费类型 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| VISIT | 拜访用户计费类型 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| HOMESGSN | 本地用户使用SGSN计费属性标志 | local_planned | optional | 无 | 枚举类型。 |
| ROAMSGSN | 漫游用户使用SGSN计费属性标志 | local_planned | optional | 无 | 枚举类型。 |
| VISITSGSN | 拜访用户使用SGSN计费属性标志 | local_planned | optional | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L15:
    > - [**SET USRPROFCHARGE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
    > - [**SET APNCHARGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md)
    > - [**SET GLBCHARGECHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置对本地用户、漫游用户、拜访用户所采用的计费属性（SET GLBCHARGECHAR）_09896800.md)
    > - [**SET CHARGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/设置计费控制配置（SET CHARGECTRL）_09896792.md)
    > - [**ADD CHARGEMETHOD**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费属性计费控制/增加计费方式（ADD CHARGEMETHOD）_09896795.md)

**md：`WSFD-011201/配置计费属性CC（GGSN_SGW-C_PGW-C）_95923501.md`**
- 数据规划表（该命令的参数行）：
  | **SET GLBCHARGECHAR** | 本地用户计费类型（HOME） | 0x0100 | 本端规划 | 配置全局CC。 |
  | **SET GLBCHARGECHAR** | 漫游用户计费类型（ROAM） | 0x0100 | 本端规划 | 配置全局CC。 |
  | **SET GLBCHARGECHAR** | 拜访用户计费类型（VISIT） | 0x0100 | 本端规划 | 配置全局CC。 |
  | **SET GLBCHARGECHAR** | 本地用户使用SGSN计费属性标志（HOMESGSN） | ENABLE | 本端规划 | 配置全局CC。 |
  | **SET GLBCHARGECHAR** | 漫游用户使用SGSN计费属性标志（ROAMSGSN） | ENABLE | 本端规划 | 配置全局CC。 |
  | **SET GLBCHARGECHAR** | 拜访用户使用SGSN计费属性标志（VISITSGSN） | ENABLE | 本端规划 | 配置全局CC。 |
- 任务示例脚本（该命令行）：
  `SET GLBCHARGECHAR: HOME="0x0100", ROAM="0x0100", VISIT="0x0100", HOMESGSN=ENABLE, ROAMSGSN=ENABLE, VISITSGSN=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L13:
    > 
    > - 当左侧网元携带签约CC、并且本地基于UserProfile、APN配置CC场景下，本地、漫游、拜访用户选择CC由**ADD CHARGECHAR**命令的HOMESGSN、ROAMSGSN、VISITSGSN控制，当对应参数配置为ENABLE时，表示使用签约下发的CC，当配置为DISABLE时，表示使用本地配置的CC。
    > - 当左侧网元携带签约CC、并且本地基于全局配置CC场景下，本地、漫游、拜访用户选择CC由**SET GLBCHARGECHAR**命令的HOMESGSN、ROAMSGSN、VISITSGSN控制，当对应参数配置为ENABLE时，表示使用签约下发的CC，当配置为DISABLE时，表示使用本地全局配置的CC。
    >   > **说明**
    >   > - 4G网络中，在SP合设场景，即UNC作为SGW-C和PGW-C时，由左侧MME携带CC（MME从HSS获取的签约CC）；在SP分离部署场景，当UNC单独作为SGW-C时由左侧MME携带CC（MME从HSS获取的签约CC），当UNC单独作为PGW-C时由左侧SGW-C携带CC（SGW-C通过MME得到签约CC）。即4G网络中签约CC由左侧MME/SGW-C携带。
  L64:
    > 
    > - 配置全局CC。
    >   **SET GLBCHARGECHAR**
    > - 配置APN下的CC。
    >     1. 配置CC实例。
  L95:
    > 
    > ```
    > SET GLBCHARGECHAR: HOME="0x0100", ROAM="0x0100", VISIT="0x0100", HOMESGSN=ENABLE, ROAMSGSN=ENABLE, VISITSGSN=ENABLE;
    > ```
    > 

### WSFD-011206

**md：`WSFD-011206/WSFD-011206 支持融合计费参考信息_74013176.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
    > - [**SET APNCHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md)
    > - [**SET GLBCHARGECHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置对本地用户、漫游用户、拜访用户所采用的计费属性（SET GLBCHARGECHAR）_09896800.md)
    > - [**ADD TNFINS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例管理/增加目标NF实例（ADD TNFINS）_09652354.md)
    > - [**ADD TNFINSIP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例IP地址管理/增加目标NF实例IP地址（ADD TNFINSIP）_09654443.md)

**md：`WSFD-011206/配置计费属性CC_90776700.md`**
- 数据规划表（该命令的参数行）：
  | **SET GLBCHARGECHAR** | 本地用户计费类型（HOME） | 0x0100 | 本端规划 | 配置全局CC。 |
  | **SET GLBCHARGECHAR** | 漫游用户计费类型（ROAM） | 0x0100 | 本端规划 | 配置全局CC。 |
  | **SET GLBCHARGECHAR** | 拜访用户计费类型（VISIT） | 0x0100 | 本端规划 | 配置全局CC。 |
  | **SET GLBCHARGECHAR** | 本地用户使用SGSN计费属性标志（HOMESGSN） | DISABLE | 本端规划 | 配置全局CC。 |
  | **SET GLBCHARGECHAR** | 漫游用户使用SGSN计费属性标志（ROAMSGSN） | DISABLE | 本端规划 | 配置全局CC。 |
  | **SET GLBCHARGECHAR** | 拜访用户使用SGSN计费属性标志（VISITSGSN） | DISABLE | 本端规划 | 配置全局CC。 |
- 任务示例脚本（该命令行）：
  `SET GLBCHARGECHAR: HOME="0x0100", ROAM="0x0100", VISIT="0x0100", HOMESGSN=DISABLE, ROAMSGSN=DISABLE, VISITSGSN=DISABLE;`
- 操作步骤上下文（±2 行原文）：
  L13:
    > 
    > - 当UDM下发签约CC、并且本地基于UserProfile、DNN配置CC场景下，由**ADD CHARGECHAR**命令的HOMESGSN、ROAMSGSN、VISITSGSN控制本地、漫游、拜访用户是否使用签约下发的计费属性CC。当对应参数配置为ENABLE时，表示使用UDM签约下发的CC；当配置为DISABLE时，表示使用本地配置的CC。从UDM获取签约CC时，SMF直接动态获取计费属性信息，与本地配置CC无关。
    > - 当UDM下发签约CC、并且本地基于全局配置CC场景下，由**SET GLBCHARGECHAR**命令的HOMESGSN、ROAMSGSN、VISITSGSN控制本地、漫游、拜访用户是否使用签约下发的计费属性CC。当对应参数配置为ENABLE时，表示使用UDM签约下发的CC；当配置为DISABLE时，表示使用本地全局配置的CC。从UDM获取签约CC时，SMF直接动态获取计费属性信息，与本地配置CC无关。
    > 
    > **图1** Charging Characteristics选择图
  L61:
    >     1. 进入 “MML命令行-UNC” 窗口。
    >     2. 配置全局CC。
    >       **SET GLBCHARGECHAR**
    > - 配置DNN下的CC。
    >     1. 进入 “MML命令行-UNC” 窗口。
  L94:
    > 
    > ```
    > SET GLBCHARGECHAR: HOME="0x0100", ROAM="0x0100", VISIT="0x0100", HOMESGSN=DISABLE, ROAMSGSN=DISABLE, VISITSGSN=DISABLE;
    > ```
    > 

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L32:
    > - [**ADD OCSBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS绑定OCS Group/增加Ocs绑定关系（ADD OCSBINDING）_09896963.md)
    > - [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
    > - [**SET GLBCHARGECHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置对本地用户、漫游用户、拜访用户所采用的计费属性（SET GLBCHARGECHAR）_09896800.md)
    > - [**ADD CHARGEMETHOD**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费属性计费控制/增加计费方式（ADD CHARGEMETHOD）_09896795.md)
    > - [**SET GLBURRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/全局使用量上报规则组/设置全局使用量上报规则组（SET GLBURRGROUP）_09897187.md)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L32:
    > - [**ADD OCSBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS绑定OCS Group/增加Ocs绑定关系（ADD OCSBINDING）_09896963.md)
    > - [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
    > - [**SET GLBCHARGECHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置对本地用户、漫游用户、拜访用户所采用的计费属性（SET GLBCHARGECHAR）_09896800.md)
    > - [**ADD CHARGEMETHOD**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费属性计费控制/增加计费方式（ADD CHARGEMETHOD）_09896795.md)
    > - [**SET GLBURRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/全局使用量上报规则组/设置全局使用量上报规则组（SET GLBURRGROUP）_09897187.md)

**md：`WSFD-109001/配置计费属性CC（GGSN_SGW-C_PGW-C）_15408915.md`**
- 数据规划表（该命令的参数行）：
  | **SET GLBCHARGECHAR** | 本地用户计费类型（HOME） | 0x0100 | 本端规划 | 配置全局CC。 |
  | **SET GLBCHARGECHAR** | 漫游用户计费类型（ROAM） | 0x0100 | 本端规划 | 配置全局CC。 |
  | **SET GLBCHARGECHAR** | 拜访用户计费类型（VISIT） | 0x0100 | 本端规划 | 配置全局CC。 |
  | **SET GLBCHARGECHAR** | 本地用户使用SGSN计费属性标志（HOMESGSN） | ENABLE | 本端规划 | 配置全局CC。 |
  | **SET GLBCHARGECHAR** | 漫游用户使用SGSN计费属性标志（ROAMSGSN） | ENABLE | 本端规划 | 配置全局CC。 |
  | **SET GLBCHARGECHAR** | 拜访用户使用SGSN计费属性标志（VISITSGSN） | ENABLE | 本端规划 | 配置全局CC。 |
- 任务示例脚本（该命令行）：
  `SET GLBCHARGECHAR: HOME="0x0100", ROAM="0x0100", VISIT="0x0100", HOMESGSN=ENABLE, ROAMSGSN=ENABLE, VISITSGSN=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L13:
    > 
    > - 当左侧网元携带签约CC、并且本地基于UserProfile、APN配置CC场景下，本地、漫游、拜访用户选择CC由**ADD CHARGECHAR**命令的HOMESGSN、ROAMSGSN、VISITSGSN控制，当对应参数配置为ENABLE时，表示使用签约下发的CC，当配置为DISABLE时，表示使用本地配置的CC。
    > - 当左侧网元携带签约CC、并且本地基于全局配置CC场景下，本地、漫游、拜访用户选择CC由**SET GLBCHARGECHAR**命令的HOMESGSN、ROAMSGSN、VISITSGSN控制，当对应参数配置为ENABLE时，表示使用签约下发的CC，当配置为DISABLE时，表示使用本地全局配置的CC。
    >   > **说明**
    >   > - 4G网络中，在SP合设场景，即UNC作为SGW-C和PGW-C时，由左侧MME携带CC（MME从HSS获取的签约CC）；在SP分离部署场景，当UNC单独作为SGW-C时由左侧MME携带CC（MME从HSS获取的签约CC），当UNC单独作为PGW-C时由左侧SGW-C携带CC（SGW-C通过MME得到签约CC）。即4G网络中签约CC由左侧MME/SGW-C携带。
  L64:
    > 
    > - 配置全局CC。
    >   **SET GLBCHARGECHAR**
    > - 配置APN下的CC。
    >     1. 配置CC实例。
  L95:
    > 
    > ```
    > SET GLBCHARGECHAR: HOME="0x0100", ROAM="0x0100", VISIT="0x0100", HOMESGSN=ENABLE, ROAMSGSN=ENABLE, VISITSGSN=ENABLE;
    > ```
    > 

## ④ 自动比对
- 命令真相参数（6）：['HOME', 'HOMESGSN', 'ROAM', 'ROAMSGSN', 'VISIT', 'VISITSGSN']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 18}（多值→atom 应考虑 decision_driven）
