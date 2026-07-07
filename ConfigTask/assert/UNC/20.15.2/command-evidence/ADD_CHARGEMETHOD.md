# 命令证据包：ADD CHARGEMETHOD
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费属性计费控制/增加计费方式（ADD CHARGEMETHOD）_09896795.md`
> 用该命令的特性数：4

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

ADD CHARGEMETHOD命令用来基于用户计费属性配置在线计费、离线计费和融合计费方式。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。
- 该命令最大记录数为17。
- 输入normal、hotbilling、prepaid和flat-billing关键字时不允许配置掩码和优先级。但通过specificvalue允许输入0x0800、0x0400、0x0200、0x0100，并且可以配置掩码和优先级。
- 当增加、删除和修改该命令时，只对新激活的用户生效。已经激活的用户，仍保留原有的在线离线计

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CHARGECHARACT | 计费属性 | global_planned | required | 无 | 枚举类型。 |
| CCVALUE | 计费属性值 | global_planned | conditional | 无 | 字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| MASK | 计费属性掩码 | global_planned | conditional | 无 | 字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| PRIORITY | 计费属性优先级 | global_planned | conditional | 无 | 整数类型，取值范围为1～65535。 |
| ONLINE | 在线计费开关 | global_planned | optional | DISABLE | 枚举类型。 |
| OFFLINE | 离线计费开关 | global_planned | optional | ENABLE | 枚举类型。 |
| CONVERGED | 融合计费开关 | global_planned | optional | ENABLE | 枚举类型。 |
| RGAPPLIED | 业务申请上报模式 | global_planned | conditional | DEFAULT | 枚举类型。 |
| QBCSW | QBC计费开关 | global_planned | conditional | ENABLE | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L17:
    > - [**SET GLBCHARGECHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置对本地用户、漫游用户、拜访用户所采用的计费属性（SET GLBCHARGECHAR）_09896800.md)
    > - [**SET CHARGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/设置计费控制配置（SET CHARGECTRL）_09896792.md)
    > - [**ADD CHARGEMETHOD**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费属性计费控制/增加计费方式（ADD CHARGEMETHOD）_09896795.md)
    > - [**SET SGWCHARGECFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW计费基础参数/SGW计费配置（SET SGWCHARGECFG）_09896989.md)
    > - [**SET SGWAPNCHGMETH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW APN计费方式/设置SGW APN计费方式（SET SGWAPNCHGMETH）_09896992.md)

**md：`WSFD-011201/配置离线_在线计费方式（GGSN_PGW-C）_95923455.md`**
- 数据规划表（该命令的参数行）：
  | **ADD CHARGEMETHOD** | 计费属性（CHARGECHARACT） | NORMAL | 全网规划 | 基于用户计费属性配置离线计费。 |
  | **ADD CHARGEMETHOD** | 计费属性值（CCVALUE） | 0x0400 | 全网规划 | 基于用户计费属性配置离线计费。 |
  | **ADD CHARGEMETHOD** | 离线计费开关（OFFLINE） | ENABLE | 全网规划 | 基于用户计费属性配置离线计费。 |
  | **ADD CHARGEMETHOD** | 计费属性（CHARGECHARACT） | NORMAL | 全网规划 | 基于用户计费属性配置在线计费。 |
  | **ADD CHARGEMETHOD** | 计费属性值（CCVALUE） | 0x0400 | 全网规划 | 基于用户计费属性配置在线计费。 |
  | **ADD CHARGEMETHOD** | 在线计费开关（ONLINE） | ENABLE | 全网规划 | 基于用户计费属性配置在线计费。 |
- 任务示例脚本（该命令行）：
  `ADD CHARGEMETHOD: CHARGECHARACT=SPECIFIC_VALUE, CCVALUE="0x0400", MASK="0x0400", PRIORITY=2, OFFLINE=ENABLE;`
  `ADD CHARGEMETHOD: CHARGECHARACT=SPECIFIC_VALUE, CCVALUE="0x0400", MASK="0x0400", PRIORITY=2, ONLINE=ENABLE;`
  `ADD CHARGEMETHOD: CHARGECHARACT=SPECIFIC_VALUE, CCVALUE="0x0400", MASK="0x0400", PRIORITY=2, ONLINE=ENABLE, OFFLINE=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L91:
    >   **SET APNCHARGECTRL**
    > 4. 基于用户计费属性使能GGSN/PGW-C的离线/在线计费方式。
    >   **ADD CHARGEMETHOD**
    > 5. 配置免费业务的计费方式。
    >     a. 配置免费业务的计费模式。
  L157:
    > 
    >   ```
    >   ADD CHARGEMETHOD: CHARGECHARACT=SPECIFIC_VALUE, CCVALUE="0x0400", MASK="0x0400", PRIORITY=2, OFFLINE=ENABLE;
    >   ```
    > 2. 使能GGSN/PGW-C的在线计费。
  L193:
    > 
    >   ```
    >   ADD CHARGEMETHOD: CHARGECHARACT=SPECIFIC_VALUE, CCVALUE="0x0400", MASK="0x0400", PRIORITY=2, ONLINE=ENABLE;
    >   ```
    > 3. 使能GGSN/PGW-C的离线和在线计费。

### WSFD-011206

**md：`WSFD-011206/使能融合计费功能_77691175.md`**
- 数据规划表（该命令的参数行）：
  | **ADD CHARGEMETHOD** | 计费属性（CHARGECHARACT） | SPECIFIC_VALUE | 全网规划 | 基于用户计费属性配置融合计费。 |
  | **ADD CHARGEMETHOD** | 计费属性值（CCVALUE） | 0x0400 | 全网规划 | 基于用户计费属性配置融合计费。 |
  | **ADD CHARGEMETHOD** | 融合计费开关（CONVERGED） | ENABLE | 全网规划 | 基于用户计费属性配置融合计费。 |
  | **ADD CHARGEMETHOD** | 业务申请上报模式（RGAPPLIED） | ONLINERGONLY | 全网规划 | 说明：- 当“RGAPPLIED”配置为“DEFAULT”时，当URRGROUP下同时配置离线和在线URR，会优先选择在线URR。<br>- 当“RGAPPLIED”配置为“ONLINERGONLY”或“OFFLINERGONLY”时，URRGROUP下建议同时配置离线和在线URR。 |
- 任务示例脚本（该命令行）：
  `ADD CHARGEMETHOD: CHARGECHARACT=SPECIFIC_VALUE, CCVALUE="0x400", MASK="0x400", PRIORITY=2, CONVERGED =ENABLE, RGAPPLIED=ONLINERGONLY;`
- 操作步骤上下文（±2 行原文）：
  L60:
    >   **SET CHARGECTRL**
    >   > **说明**
    >   > **SET CHARGECTRL** 根据用户漫游属性设置计费方式， **ADD CHARGEMETHOD** 根据CC属性设置计费方式，针对同一个用户，两者规划的计费方式要一致，否则用户计费会出错。例如，针对CC是normal的本地用户，如果设置本地用户进行在线计费，又设置normal用户进行离线计费，那用户最终计费结果将出错。
    > 2. 基于UserProfile配置计费方式。
    >   **SET USRPROFCHARGE**
  L66:
    >   **SET APNCHARGECTRL**
    > 4. 基于用户计费属性配置计费方式。
    >   **ADD CHARGEMETHOD**
    > 
    > ## [任务示例](#ZH-CN_OPI_0277691175)
  L113:
    > 
    > ```
    > ADD CHARGEMETHOD: CHARGECHARACT=SPECIFIC_VALUE, CCVALUE="0x400", MASK="0x400", PRIORITY=2, CONVERGED =ENABLE, RGAPPLIED=ONLINERGONLY;
    > ```

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L33:
    > - [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
    > - [**SET GLBCHARGECHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置对本地用户、漫游用户、拜访用户所采用的计费属性（SET GLBCHARGECHAR）_09896800.md)
    > - [**ADD CHARGEMETHOD**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费属性计费控制/增加计费方式（ADD CHARGEMETHOD）_09896795.md)
    > - [**SET GLBURRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/全局使用量上报规则组/设置全局使用量上报规则组（SET GLBURRGROUP）_09897187.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L33:
    > - [**SET USRPROFCHARGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
    > - [**SET GLBCHARGECHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置对本地用户、漫游用户、拜访用户所采用的计费属性（SET GLBCHARGECHAR）_09896800.md)
    > - [**ADD CHARGEMETHOD**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费属性计费控制/增加计费方式（ADD CHARGEMETHOD）_09896795.md)
    > - [**SET GLBURRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/全局使用量上报规则组/设置全局使用量上报规则组（SET GLBURRGROUP）_09897187.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)

**md：`WSFD-109001/配置普通在线计费实例_95923459.md`**
- 操作步骤上下文（±2 行原文）：
  L130:
    >   **SET APNCHARGECTRL**
    >   > **说明**
    >   > 针对同一个用户， **ADD CHARGECHAR** 和 **ADD CHARGEMETHOD** 配置的结果要保持一致，要么是 “ONLINE” ，要么是 “OFFLINE” ，或者两者同时使能，如果不一致将导致用户计费方式错误。
    > 
    > ## [任务示例](#ZH-CN_OPI_0295923459)

**md：`WSFD-109001/配置离线_在线计费方式（GGSN_PGW-C）_15408914.md`**
- 数据规划表（该命令的参数行）：
  | **ADD CHARGEMETHOD** | 计费属性（CHARGECHARACT） | NORMAL | 全网规划 | 基于用户计费属性配置离线计费。 |
  | **ADD CHARGEMETHOD** | 计费属性值（CCVALUE） | 0x0400 | 全网规划 | 基于用户计费属性配置离线计费。 |
  | **ADD CHARGEMETHOD** | 离线计费开关（OFFLINE） | ENABLE | 全网规划 | 基于用户计费属性配置离线计费。 |
  | **ADD CHARGEMETHOD** | 计费属性（CHARGECHARACT） | NORMAL | 全网规划 | 基于用户计费属性配置在线计费。 |
  | **ADD CHARGEMETHOD** | 计费属性值（CCVALUE） | 0x0400 | 全网规划 | 基于用户计费属性配置在线计费。 |
  | **ADD CHARGEMETHOD** | 在线计费开关（ONLINE） | ENABLE | 全网规划 | 基于用户计费属性配置在线计费。 |
- 任务示例脚本（该命令行）：
  `ADD CHARGEMETHOD: CHARGECHARACT=SPECIFIC_VALUE, CCVALUE="0x0400", MASK="0x0400", PRIORITY=2, OFFLINE=ENABLE;`
  `ADD CHARGEMETHOD: CHARGECHARACT=SPECIFIC_VALUE, CCVALUE="0x0400", MASK="0x0400", PRIORITY=2, ONLINE=ENABLE;`
  `ADD CHARGEMETHOD: CHARGECHARACT=SPECIFIC_VALUE, CCVALUE="0x0400", MASK="0x0400", PRIORITY=2, ONLINE=ENABLE, OFFLINE=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L91:
    >   **SET APNCHARGECTRL**
    > 4. 基于用户计费属性使能GGSN/PGW-C的离线/在线计费方式。
    >   **ADD CHARGEMETHOD**
    > 5. 配置免费业务的计费方式。
    >     a. 配置免费业务的计费模式。
  L157:
    > 
    >   ```
    >   ADD CHARGEMETHOD: CHARGECHARACT=SPECIFIC_VALUE, CCVALUE="0x0400", MASK="0x0400", PRIORITY=2, OFFLINE=ENABLE;
    >   ```
    > 2. 使能GGSN/PGW-C的在线计费。
  L193:
    > 
    >   ```
    >   ADD CHARGEMETHOD: CHARGECHARACT=SPECIFIC_VALUE, CCVALUE="0x0400", MASK="0x0400", PRIORITY=2, ONLINE=ENABLE;
    >   ```
    > 3. 使能GGSN/PGW-C的离线和在线计费。

## ④ 自动比对
- 命令真相参数（9）：['CCVALUE', 'CHARGECHARACT', 'CONVERGED', 'MASK', 'OFFLINE', 'ONLINE', 'PRIORITY', 'QBCSW', 'RGAPPLIED']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 16}（多值→atom 应考虑 decision_driven）
