# 命令证据包：SET CHARGECTRL
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/设置计费控制配置（SET CHARGECTRL）_09896792.md`
> 用该命令的特性数：5

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

![](设置计费控制配置（SET CHARGECTRL）_09896792.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，此操作会影响新激活用户的计费方式(在线、离线、融合)，可能导致用户无法计费。

本命令用来控制是否基于用户漫游、拜访、本地属性来提供在线计费、离线计费和融合计费功能。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | HOMEONLINE | HOMECONVERGED | HOMEOFFLINE | VISITONLINE | VISITOFFLINE | VISITCONVERGED | ROAMONLINE | ROAMOFFLINE | ROAMCONVERGED 

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| HOMEONLINE | 归属地在线用户计费控制 | global_planned | optional | 无 | 枚举类型。 |
| HOMECONVERGED | 归属地融合用户计费控制 | global_planned | optional | 无 | 枚举类型。 |
| HOMEOFFLINE | 归属地离线用户计费控制 | global_planned | optional | 无 | 枚举类型。 |
| VISITONLINE | 拜访地在线计费用户计费控制 | global_planned | optional | 无 | 枚举类型。 |
| VISITOFFLINE | 拜访地离线计费用户计费控制 | global_planned | optional | 无 | 枚举类型。 |
| VISITCONVERGED | 拜访地融合计费用户计费控制 | global_planned | optional | 无 | 枚举类型。 |
| ROAMONLINE | 漫游在线计费用户计费控制 | global_planned | optional | 无 | 枚举类型。 |
| ROAMOFFLINE | 漫游离线计费用户计费控制 | global_planned | optional | 无 | 枚举类型。 |
| ROAMCONVERGED | 漫游融合计费用户计费控制 | global_planned | optional | 无 | 枚举类型。 |
| N40BKPTRAFFIC | 融合计费是否支持处理备份流量 | local_planned | optional | 无 | <br>- DISABLE：不使能。 |
| GAGYBKPTRAFFIC | 在线离线计费是否支持处理备份流量 | local_planned | optional | 无 | <br>- DISABLE：不使能。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - [**SET APNCHARGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md)
    > - [**SET GLBCHARGECHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置对本地用户、漫游用户、拜访用户所采用的计费属性（SET GLBCHARGECHAR）_09896800.md)
    > - [**SET CHARGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/设置计费控制配置（SET CHARGECTRL）_09896792.md)
    > - [**ADD CHARGEMETHOD**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费属性计费控制/增加计费方式（ADD CHARGEMETHOD）_09896795.md)
    > - [**SET SGWCHARGECFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW计费基础参数/SGW计费配置（SET SGWCHARGECFG）_09896989.md)

**md：`WSFD-011201/配置离线_在线计费方式（GGSN_PGW-C）_95923455.md`**
- 数据规划表（该命令的参数行）：
  | **SET CHARGECTRL** | 归属地离线用户计费控制（HOMEOFFLINE） | ENABLE | 全网规划 | 用来控制是否基于用户漫游、拜访、本地属性来提供离线计费。 |
  | **SET CHARGECTRL** | 拜访地离线计费用户计费控制（VISITOFFLINE） | ENABLE | 全网规划 | 用来控制是否基于用户漫游、拜访、本地属性来提供离线计费。 |
  | **SET CHARGECTRL** | 漫游离线计费用户计费控制（ROAMOFFLINE） | ENABLE | 全网规划 | 用来控制是否基于用户漫游、拜访、本地属性来提供离线计费。 |
  | **SET CHARGECTRL** | 归属地在线用户计费控制（HOMEONLINE） | ENABLE | 全网规划 | 用来控制是否基于用户漫游、拜访、本地属性来提供在线计费。 |
  | **SET CHARGECTRL** | 拜访地在线计费用户计费控制（VISITONLINE） | ENABLE | 全网规划 | 用来控制是否基于用户漫游、拜访、本地属性来提供在线计费。 |
  | **SET CHARGECTRL** | 漫游在线计费用户计费控制（ROAMONLINE） | ENABLE | 全网规划 | 用来控制是否基于用户漫游、拜访、本地属性来提供在线计费。 |
- 任务示例脚本（该命令行）：
  `SET CHARGECTRL: HOMEOFFLINE=ENABLE,VISITOFFLINE=ENABLE,ROAMOFFLINE=ENABLE;`
  `SET CHARGECTRL: HOMEOFFLINE=ENABLE,VISITOFFLINE=ENABLE,ROAMOFFLINE=ENABLE;`
  `SET CHARGECTRL: HOMEOFFLINE=ENABLE,VISITOFFLINE=ENABLE,ROAMOFFLINE=ENABLE;`
  `SET CHARGECTRL: HOMEONLINE=ENABLE,VISITONLINE=ENABLE,ROAMONLINE=ENABLE;`
  `SET CHARGECTRL: HOMEONLINE=ENABLE,VISITONLINE=ENABLE,ROAMONLINE=ENABLE;`
  `SET CHARGECTRL: HOMEONLINE=ENABLE,VISITONLINE=ENABLE,ROAMONLINE=ENABLE;`
  `SET CHARGECTRL: HOMEONLINE=ENABLE, HOMEOFFLINE=ENABLE, VISITONLINE=ENABLE, VISITOFFLINE=ENABLE, ROAMONLINE=ENABLE, ROAMOFFLINE=ENABLE;`
  `SET CHARGECTRL: HOMEONLINE=ENABLE, HOMEOFFLINE=ENABLE, VISITONLINE=ENABLE, VISITOFFLINE=ENABLE, ROAMONLINE=ENABLE, ROAMOFFLINE=ENABLE;`
  `SET CHARGECTRL: HOMEONLINE=ENABLE, HOMEOFFLINE=ENABLE, VISITONLINE=ENABLE, VISITOFFLINE=ENABLE, ROAMONLINE=ENABLE, ROAMOFFLINE=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L28:
    >     - 如果网络中未部署PCRF，且RADIUS Server不支持下发OCS-ID，则使用本地配置的在线计费方式。
    > 
    > 其中，根据用户归属属性配置的开关 **SET CHARGECTRL** 是控制在线/离线计费的总开关，是进行相应方式计费的前提和基础，它控制GGSN/PGW-C本地配置的计费开关和RADIUS server下发的计费方式是否有效，PCRF下发计费方式不受此控制。即当总开关使能了在线/离线计费，其他开关的配置才能生效。默认情况下，总开关同时使能在线/离线计费。
    > 
    > 基于此，在线/离线计费选择开关的优先级从高到低依次是：PCRF下发的参数–〉GGSN/PGW-C本地总开关–〉RADIUS下发的参数–〉UserProfile下的配置–〉APN下的配置-〉用户计费属性下的配置。对于GGSN/PGW-C本地配置的各级开关来说，如果高级别的参数没有配置，则依次向下继承低一级别的参数取值。
  L83:
    > 
    > 1. 基于用户归属属性（本地用户、漫游用户、拜访用户）使能GGSN/PGW-C的离线/在线计费方式。
    >   **SET CHARGECTRL**
    >   > **说明**
    >   > 针对同一个用户，不同属性下规划的计费方式要一致，否则用户计费会出错。例如，针对CC取值为NORMAL的本地用户，如果设置NORMAL用户进行离线计费，又设置本地用户进行在线计费，则最终用户计费将出错。
  L127:
    > 
    >   ```
    >   SET CHARGECTRL: HOMEOFFLINE=ENABLE,VISITOFFLINE=ENABLE,ROAMOFFLINE=ENABLE;
    >   ```
    > 

### WSFD-011202

**md：`WSFD-011202/WSFD-011202 支持热计费功能（适用于GGSN、SGW-C、PGW-C）参考信息_28072079.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - **[修改对本地用户、漫游用户、拜访用户所采用的计费属性（MOD CHARGECHAR）](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/修改对本地用户、漫游用户、拜访用户所采用的计费属性（MOD CHARGECHAR）_09896810.md)**
    > - **[查询对本地用户、漫游用户、拜访用户所采用的计费属性（LST CHARGECHAR）](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/查询对本地用户、漫游用户、拜访用户所采用的计费属性（LST CHARGECHAR）_09896812.md)**
    > - **[设置计费控制配置（SET CHARGECTRL）](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/设置计费控制配置（SET CHARGECTRL）_09896792.md)**
    > - **[查询计费控制配置（LST CHARGECTRL）](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/查询计费控制配置（LST CHARGECTRL）_09896793.md)**
    > - **[设置离线计费阈值（SET OFCTHRESHOLD）](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/设置离线计费阈值（SET OFCTHRESHOLD）_09896910.md)**

**md：`WSFD-011202/激活支持热计费功能_28072077.md`**
- 数据规划表（该命令的参数行）：
  | **[SET CHARGECTRL](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/设置计费控制配置（SET CHARGECTRL）_09896792.md)** | 归属地离线用户计费控制（HOMEOFFLINE）<br>拜访地离线计费用户计费控制（VISITOFFLINE）<br>漫游离线计费用户计费控制（ROAMOFFLINE） | ENABLE<br>ENABLE<br>ENABLE | 本端规划 | 计费方式配置为离线计费。 |
- 任务示例脚本（该命令行）：
  `SET CHARGECTRL:HOMEOFFLINE=ENABLE,VISITOFFLINE=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L57:
    > 
    > ```
    > SET CHARGECTRL:HOMEOFFLINE=ENABLE,VISITOFFLINE=ENABLE;
    > ```
    > 

### WSFD-011206

**md：`WSFD-011206/使能融合计费功能_77691175.md`**
- 数据规划表（该命令的参数行）：
  | **SET CHARGECTRL** | 归属地融合用户计费控制（HOMECONVERGED） | ENABLE | 全网规划 | 用来控制是否基于用户漫游、拜访、本地属性来提供融合计费。 |
  | **SET CHARGECTRL** | 拜访地融合计费用户计费控制（VISITCONVERGED） | ENABLE | 全网规划 | 用来控制是否基于用户漫游、拜访、本地属性来提供融合计费。 |
  | **SET CHARGECTRL** | 漫游融合计费用户计费控制（ROAMCONVERGED） | ENABLE | 全网规划 | 用来控制是否基于用户漫游、拜访、本地属性来提供融合计费。 |
- 任务示例脚本（该命令行）：
  `SET CHARGECTRL: HOMECONVERGED=ENABLE,VISITCONVERGED=ENABLE,ROAMCONVERGED=ENABLE;`
  `SET CHARGECTRL: HOMEOFFLINE=ENABLE,VISITOFFLINE=ENABLE,ROAMOFFLINE=ENABLE;`
  `SET CHARGECTRL: HOMEOFFLINE=ENABLE,VISITOFFLINE=ENABLE,ROAMOFFLINE=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L16:
    > - 指定CC使能融合计费开关。
    > 
    > 如果网络中部署了PCF控制融合计费方式，则PCF在Npcf_SMPolicyControl_Create Response消息中携带online/offline指示是否使能融合计费。根据用户归属属性（本地用户，漫游用户和拜访用户）配置的开关 **SET CHARGECTRL** 是控制SMF本地配置的融合计费开关是否有效的总开关，当总开关使能了融合计费，其他开关的配置才能生效。默认情况下，总开关同时使能在线/离线/融合计费。 [使能融合计费功能](使能融合计费功能_77691175.md) 为SMF的融合计费方式选择图。
    > 
    > **图1** 融合计费方式选择图
  L58:
    > 
    > 1. 基于用户归属属性配置计费方式。
    >   **SET CHARGECTRL**
    >   > **说明**
    >   > **SET CHARGECTRL** 根据用户漫游属性设置计费方式， **ADD CHARGEMETHOD** 根据CC属性设置计费方式，针对同一个用户，两者规划的计费方式要一致，否则用户计费会出错。例如，针对CC是normal的本地用户，如果设置本地用户进行在线计费，又设置normal用户进行离线计费，那用户最终计费结果将出错。
  L60:
    >   **SET CHARGECTRL**
    >   > **说明**
    >   > **SET CHARGECTRL** 根据用户漫游属性设置计费方式， **ADD CHARGEMETHOD** 根据CC属性设置计费方式，针对同一个用户，两者规划的计费方式要一致，否则用户计费会出错。例如，针对CC是normal的本地用户，如果设置本地用户进行在线计费，又设置normal用户进行离线计费，那用户最终计费结果将出错。
    > 2. 基于UserProfile配置计费方式。
    >   **SET USRPROFCHARGE**

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
  L13:
    > 
    > - **[ADD CHARGECHAR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/增加对本地用户、漫游用户、拜访用户所采用的计费属性（ADD CHARGECHAR）_09896809.md)**
    > - [**SET CHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/设置计费控制配置（SET CHARGECTRL）_09896792.md)
    > - [**SET APNCHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md)
    > - **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)**

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L13:
    > 
    > - **[ADD CHARGECHAR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/增加对本地用户、漫游用户、拜访用户所采用的计费属性（ADD CHARGECHAR）_09896809.md)**
    > - [**SET CHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/设置计费控制配置（SET CHARGECTRL）_09896792.md)
    > - [**SET APNCHARGECTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md)
    > - **[ADD URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)**

**md：`WSFD-109001/配置DCC处理动作_95923447.md`**
- 操作步骤上下文（±2 行原文）：
  L69:
    >       **ADD DCCTEMPLATE**
    >       > **说明**
    >       > 本命令只针对在线计费用户生效，且在 [配置离线/在线计费方式（GGSN/PGW-C）](../../WSFD-011201 支持离线计费/激活离线计费/配置离线_在线计费方式（GGSN_PGW-C）_95923455.md) 中根据用户归属属性配置的离线计费开关 **SET CHARGECTRL** 必须使能。
    >     5. 配置Tx定时器的时长。
    >       **SET TXTIMER**

**md：`WSFD-109001/配置普通在线计费实例_95923459.md`**
- 数据规划表（该命令的参数行）：
  | **SET CHARGECTRL** | 归属地在线用户计费控制（HOMEONLINE） | ENABLE | 全网规划 | 用来控制是否基于用户漫游、拜访、本地属性来提供在线计费。 |
  | **SET CHARGECTRL** | 拜访地在线计费用户计费控制（VISITONLINE） | ENABLE | 全网规划 | 用来控制是否基于用户漫游、拜访、本地属性来提供在线计费。 |
  | **SET CHARGECTRL** | 漫游在线计费用户计费控制（ROAMONLINE） | ENABLE | 全网规划 | 用来控制是否基于用户漫游、拜访、本地属性来提供在线计费。 |
- 任务示例脚本（该命令行）：
  `SET CHARGECTRL: HOMEONLINE=ENABLE, VISITONLINE=ENABLE, ROAMONLINE=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L86:
    >   > 如果该计费属性实例没有绑定APN实例或者UserProfile实例，则配置的计费属性不生效。
    > 2. 配置用户的计费方式是在线计费。
    >   **SET CHARGECTRL**
    > 3. 配置在线计费的费率标识。
    >     a. 配置URR，从而配置相应的计费费率标识，包括必须配置的RG和可选配置的SID。
  L146:
    > 2. 配置用户的计费方式是在线计费。
    >   ```
    >   SET CHARGECTRL: HOMEONLINE=ENABLE, VISITONLINE=ENABLE, ROAMONLINE=ENABLE;
    >   ```
    > 3. 配置在线计费的费率标识。

**md：`WSFD-109001/配置离线_在线计费方式（GGSN_PGW-C）_15408914.md`**
- 数据规划表（该命令的参数行）：
  | **SET CHARGECTRL** | 归属地离线用户计费控制（HOMEOFFLINE） | ENABLE | 全网规划 | 用来控制是否基于用户漫游、拜访、本地属性来提供离线计费。 |
  | **SET CHARGECTRL** | 拜访地离线计费用户计费控制（VISITOFFLINE） | ENABLE | 全网规划 | 用来控制是否基于用户漫游、拜访、本地属性来提供离线计费。 |
  | **SET CHARGECTRL** | 漫游离线计费用户计费控制（ROAMOFFLINE） | ENABLE | 全网规划 | 用来控制是否基于用户漫游、拜访、本地属性来提供离线计费。 |
  | **SET CHARGECTRL** | 归属地在线用户计费控制（HOMEONLINE） | ENABLE | 全网规划 | 用来控制是否基于用户漫游、拜访、本地属性来提供在线计费。 |
  | **SET CHARGECTRL** | 拜访地在线计费用户计费控制（VISITONLINE） | ENABLE | 全网规划 | 用来控制是否基于用户漫游、拜访、本地属性来提供在线计费。 |
  | **SET CHARGECTRL** | 漫游在线计费用户计费控制（ROAMONLINE） | ENABLE | 全网规划 | 用来控制是否基于用户漫游、拜访、本地属性来提供在线计费。 |
- 任务示例脚本（该命令行）：
  `SET CHARGECTRL: HOMEOFFLINE=ENABLE,VISITOFFLINE=ENABLE,ROAMOFFLINE=ENABLE;`
  `SET CHARGECTRL: HOMEOFFLINE=ENABLE,VISITOFFLINE=ENABLE,ROAMOFFLINE=ENABLE;`
  `SET CHARGECTRL: HOMEOFFLINE=ENABLE,VISITOFFLINE=ENABLE,ROAMOFFLINE=ENABLE;`
  `SET CHARGECTRL: HOMEONLINE=ENABLE,VISITONLINE=ENABLE,ROAMONLINE=ENABLE;`
  `SET CHARGECTRL: HOMEONLINE=ENABLE,VISITONLINE=ENABLE,ROAMONLINE=ENABLE;`
  `SET CHARGECTRL: HOMEONLINE=ENABLE,VISITONLINE=ENABLE,ROAMONLINE=ENABLE;`
  `SET CHARGECTRL: HOMEONLINE=ENABLE, HOMEOFFLINE=ENABLE, VISITONLINE=ENABLE, VISITOFFLINE=ENABLE, ROAMONLINE=ENABLE, ROAMOFFLINE=ENABLE;`
  `SET CHARGECTRL: HOMEONLINE=ENABLE, HOMEOFFLINE=ENABLE, VISITONLINE=ENABLE, VISITOFFLINE=ENABLE, ROAMONLINE=ENABLE, ROAMOFFLINE=ENABLE;`
  `SET CHARGECTRL: HOMEONLINE=ENABLE, HOMEOFFLINE=ENABLE, VISITONLINE=ENABLE, VISITOFFLINE=ENABLE, ROAMONLINE=ENABLE, ROAMOFFLINE=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L28:
    >     - 如果网络中未部署PCRF，且RADIUS Server不支持下发OCS-ID，则使用本地配置的在线计费方式。
    > 
    > 其中，根据用户归属属性配置的开关 **SET CHARGECTRL** 是控制在线/离线计费的总开关，是进行相应方式计费的前提和基础，它控制GGSN/PGW-C本地配置的计费开关和RADIUS server下发的计费方式是否有效，PCRF下发计费方式不受此控制。即当总开关使能了在线/离线计费，其他开关的配置才能生效。默认情况下，总开关同时使能在线/离线计费。
    > 
    > 基于此，在线/离线计费选择开关的优先级从高到低依次是：PCRF下发的参数–〉GGSN/PGW-C本地总开关–〉RADIUS下发的参数–〉UserProfile下的配置–〉APN下的配置-〉用户计费属性下的配置。对于GGSN/PGW-C本地配置的各级开关来说，如果高级别的参数没有配置，则依次向下继承低一级别的参数取值。
  L83:
    > 
    > 1. 基于用户归属属性（本地用户、漫游用户、拜访用户）使能GGSN/PGW-C的离线/在线计费方式。
    >   **SET CHARGECTRL**
    >   > **说明**
    >   > 针对同一个用户，不同属性下规划的计费方式要一致，否则用户计费会出错。例如，针对CC取值为NORMAL的本地用户，如果设置NORMAL用户进行离线计费，又设置本地用户进行在线计费，则最终用户计费将出错。
  L127:
    > 
    >   ```
    >   SET CHARGECTRL: HOMEOFFLINE=ENABLE,VISITOFFLINE=ENABLE,ROAMOFFLINE=ENABLE;
    >   ```
    > 

**md：`WSFD-109001/配置OCS Failover功能_95923411.md`**
- 操作步骤上下文（±2 行原文）：
  L92:
    >       **ADD DCCTEMPLATE**
    >       > **说明**
    >       > 本命令只针对在线计费用户生效，且在 [配置离线/在线计费方式（GGSN/PGW-C）](../../../WSFD-011201 支持离线计费/激活离线计费/配置离线_在线计费方式（GGSN_PGW-C）_95923455.md) 中根据用户归属属性配置的离线计费开关 **SET CHARGECTRL** 必须使能。
    >     f. 配置Tx定时器的时长。
    >       **SET TXTIMER**

## ④ 自动比对
- 命令真相参数（11）：['GAGYBKPTRAFFIC', 'HOMECONVERGED', 'HOMEOFFLINE', 'HOMEONLINE', 'N40BKPTRAFFIC', 'ROAMCONVERGED', 'ROAMOFFLINE', 'ROAMONLINE', 'VISITCONVERGED', 'VISITOFFLINE', 'VISITONLINE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 18, '本端规划': 1}（多值→atom 应考虑 decision_driven）
