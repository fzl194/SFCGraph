# 命令证据包：SET GLBURRGROUP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/全局使用量上报规则组/设置全局使用量上报规则组（SET GLBURRGROUP）_09897187.md`
> 用该命令的特性数：4

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

本条命令用于PDP用户设置全局使用量上报规则组，指定上下行发起使用的URR，即指定上下行报文是如何计费的。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为1。
- 不允许只配置下行URR，不配置上行URR。
- 不允许离线的URR既绑定到URRGroup又绑定到GlbURRGroup下。
- 当前版本不支持此命令。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | NOCHARGINGFLAG |
| --- | --- |
| 初始值 | NONE |

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| UPOFFURRNAME | 上行发起离线URR名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| DOWNOFFURRNAME | 下行发起离线URR名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| UPONLURRNAME | 上行发起在线URR名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| DNONLURRNAME | 下行发起在线URR名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| NOCHARGINGFLAG | 不计费标记 | local_planned | optional | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/配置离线计费的费率标识（GGSN_SGW-C_PGW-C）_98555879.md`**
- 数据规划表（该命令的参数行）：
  | **SET GLBURRGROUP** | 上行发起离线URR名称（UPOFFURRNAME） | offlineURR | 已配置数据中获取 | 将URR绑定到全局URR组上。如果上下行使用不同的URR，则两者必须同时为在线计费或离线计费。 |
  | **SET GLBURRGROUP** | 下行发起离线URR名称（DOWNOFFURRNAME） | offlineURR | 已配置数据中获取 | 将URR绑定到全局URR组上。如果上下行使用不同的URR，则两者必须同时为在线计费或离线计费。 |
- 任务示例脚本（该命令行）：
  `SET GLBURRGROUP:UPOFFURRNAME="offlineURR", DOWNOFFURRNAME="offlineURR";`
- 操作步骤上下文（±2 行原文）：
  L64:
    >       **ADD URR**
    >     2. 将全局URR绑定到全局URR组上，上下行可以使用不同的URR。
    >       **SET GLBURRGROUP**
    > - 配置UserProfile粒度的Session级计费费率标识。配置方法为将URR绑定到没有绑定Rule的UserProfile上，再将UserProfile绑定到指定APN实例上。
    >     1. 配置UserProfile下绑定的缺省URR组及相应URR，从而配置相应的计费费率标识。
  L128:
    >   ```
    >   ADD URR: URRNAME="offlineURR", URRID=1000, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=RGSID, RG=10, SID=20, OFFMETERINGTYPE=VOLUME;
    >   SET GLBURRGROUP:UPOFFURRNAME="offlineURR", DOWNOFFURRNAME="offlineURR";
    >   ```
    > 2. 任务二：配置离线计费、且费率标识为（RG，SID）=（10,20）的URR，并将该URR作为缺省上下行URR绑定到名为"up-test"的UserProfile实例上。

### WSFD-011206

**md：`WSFD-011206/WSFD-011206 支持融合计费参考信息_74013176.md`**
- 操作步骤上下文（±2 行原文）：
  L23:
    > - [**ADD SELECTCHFGBYCC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/CHF选择/增加基于CC选择CHF处理（ADD SELECTCHFGBYCC）_09652118.md)
    > - **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)**
    > - [**SET GLBURRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/全局使用量上报规则组/设置全局使用量上报规则组（SET GLBURRGROUP）_09897187.md)
    > - [**ADD URRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)
    > - [**SET URRGRPBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/设置用户模板的计费属性绑定关系（SET URRGRPBINDING）_09897209.md)

**md：`WSFD-011206/使用全局CCT模板进行融合计费实例_93029782.md`**
- 数据规划表（该命令的参数行）：
  | **SET GLBURRGROUP** | UPONLURRNAME（上行发起在线URR名称） | urr1 | 本端规划 | 将URR绑定到全局URR组上。如果上下行使用不同的URR，则两者必须同时为在线计费或离线计费。 |
  | **SET GLBURRGROUP** | DNONLURRNAME（下行发起在线URR名称） | urr1 | 本端规划 | 将URR绑定到全局URR组上。如果上下行使用不同的URR，则两者必须同时为在线计费或离线计费。 |
- 任务示例脚本（该命令行）：
  `SET GLBURRGROUP:UPONLURRNAME = "urr1", DNONLURRNAME = "urr1";`
- 操作步骤上下文（±2 行原文）：
  L71:
    > ```
    > ADD URR: URRNAME="urr1", URRID=1, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=RGSID, ONLINERG=10, ONLINESID=20, ONLMETERINGTYPE=VOLUME; 
    > SET GLBURRGROUP:UPONLURRNAME = "urr1", DNONLURRNAME = "urr1";
    > ```
    > 

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L34:
    > - [**SET GLBCHARGECHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置对本地用户、漫游用户、拜访用户所采用的计费属性（SET GLBCHARGECHAR）_09896800.md)
    > - [**ADD CHARGEMETHOD**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费属性计费控制/增加计费方式（ADD CHARGEMETHOD）_09896795.md)
    > - [**SET GLBURRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/全局使用量上报规则组/设置全局使用量上报规则组（SET GLBURRGROUP）_09897187.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**SET URRGRPBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/设置用户模板的计费属性绑定关系（SET URRGRPBINDING）_09897209.md)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L34:
    > - [**SET GLBCHARGECHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置对本地用户、漫游用户、拜访用户所采用的计费属性（SET GLBCHARGECHAR）_09896800.md)
    > - [**ADD CHARGEMETHOD**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费属性计费控制/增加计费方式（ADD CHARGEMETHOD）_09896795.md)
    > - [**SET GLBURRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/全局使用量上报规则组/设置全局使用量上报规则组（SET GLBURRGROUP）_09897187.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**SET URRGRPBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/设置用户模板的计费属性绑定关系（SET URRGRPBINDING）_09897209.md)

**md：`WSFD-109001/配置在线计费的费率标识_95923388.md`**
- 数据规划表（该命令的参数行）：
  | **SET GLBURRGROUP** | 上行发起在线URR名称（UPONLURRNAME） | onlineURR | 已配置数据中获取 | 将URR绑定到全局URR组上。如果上下行使用不同的URR，则两者必须同时为在线计费或离线计费。 |
  | **SET GLBURRGROUP** | 下行发起在线URR名称（DNONLURRNAME） | onlineURR | 已配置数据中获取 | 将URR绑定到全局URR组上。如果上下行使用不同的URR，则两者必须同时为在线计费或离线计费。 |
- 任务示例脚本（该命令行）：
  `SET GLBURRGROUP:UPONLURRNAME="onlineURR", DNONLURRNAME="onlineURR";`
- 操作步骤上下文（±2 行原文）：
  L68:
    >       > - 当OCS和GGSN/PGW-C都配置有费率下发/申请的配额数时，OCS上的配置优先级高。
    >     2. 将全局URR绑定到全局URR组上，上下行可以使用不同的URR。
    >       **SET GLBURRGROUP**
    > - 配置UserProfile粒度的Session级计费费率标识。配置方法为将URR绑定到没有绑定Rule的UserProfile上，再将UserProfile绑定到指定APN实例上。
    >     1. 配置UserProfile下绑定的缺省URR组及相应URR，从而配置相应的计费费率标识。
  L132:
    >   ```
    >   ADD URR: URRNAME="onlineURR", URRID=1100, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=RGSID, ONLINERG=10, ONLINESID=20, ONLMETERINGTYPE=EVENT_VOLUME_TIME;
    >   SET GLBURRGROUP:UPONLURRNAME="onlineURR", DNONLURRNAME="onlineURR";
    >   ```
    > 2. 任务二：配置在线计费、且费率标识为（RG，SID）=（10,20）的URR，并将该URR作为缺省上下行URR绑定到名为"up-test"的UserProfile实例上。

## ④ 自动比对
- 命令真相参数（5）：['DNONLURRNAME', 'DOWNOFFURRNAME', 'NOCHARGINGFLAG', 'UPOFFURRNAME', 'UPONLURRNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 4, '本端规划': 2}（多值→atom 应考虑 decision_driven）
