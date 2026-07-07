# 命令证据包：SET POLICYMODE
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/策略模式选择/设置策略接口的选择方式（SET POLICYMODE）_09653658.md`
> 用该命令的特性数：6

## ② 命令真相（mml_commands.jsonl）
**功能**：![](设置策略接口的选择方式（SET POLICYMODE）_09653658.assets/notice_3.0-zh-cn_2.png)

配置策略接口的选择方式不当可能导致PCC用户选择错误接口的PCRF/PCF服务器，进而影响用户使用业务，比如用户无法正常激活。

**适用NF：PGW-C、SMF、GGSN**

该命令用于配置策略接口的选择方式。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。

- 5G终端在5G接入时使用Npcf接口。
- 4G/5G互操作流程的策略接口不变。2/3/4G互操作流程的策略接口不变。
- 当需要使用本命令配置2G和3G接入使用Npcf接口时，需要提前和对端PCF确认是否支持。
- 当非5G终端4G接入时，若通过该命令修改参数“FORCED”的取值，则对应的参数“BYIWKUEN5GR4G”的取值会被同步修改成“DIS

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| TMACCTYPE | 指定终端和接入类型 | global_planned | required | 无。 | <br>- “UE5G_RAT4G（5G终端4G接入）”：5G终端4G接入是指在4G接入的PDN激活 |
| BY5GSIWKI | 按5GS互操作指示选择策略接口开关 | global_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST POLI | <br>- “DISABLE（不使能）”：不使能 |
| BYIWKUEN5GR4G | 非5G终端4G接入按5GS互操作指示选择策略接口开关 | global_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST POLI | <br>- “DISABLE（不使能）”：不使能 |
| FORCED | 指定策略接口 | global_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST POLI | <br>- “Npcf（Npcf接口）”：使用Npcf接口。 |
| PCFRESELBYPCFID | 是否基于PCF实例标识决策策略接口类型 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST POLI | <br>- TRUE(TRUE) |
| BY5GCNRI | 按5GC无限制接入标识选择策略接口开关 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST POLI | <br>- “DISABLE（不使能）”：不使能 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 操作步骤上下文（±2 行原文）：
  L202:
    >     - 未配置指定APN的策略接口类型，全局的策略接口类型为Gx接口时，未配置基于PCF实例标识的策略接口类型或基于PCF实例标识的策略接口类型设置为Gx接口时，使用Gx接口。
    >     1. 设置全局的策略接口的选择模式。
    >       [**SET POLICYMODE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/策略模式选择/设置策略接口的选择方式（SET POLICYMODE）_09653658.md)
    >     2. **可选：**增加基于APN的策略接口的选择模式。
    >       [**ADD APNPOLICYMODE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/基于APN的策略接口选择方式配置/增加基于APN的策略接口的选择方式（ADD APNPOLICYMODE）_72001541.md)

### WSFD-106010

**md：`WSFD-106010/WSFD-106010 指定区域用户位置上报(PRA)（适用于MME）&WSFD-211003 基于指_2ac2a24c_68358200.md`**
- 操作步骤上下文（±2 行原文）：
  L103:
    > 除了采用Gx接口连接PGW-C和PCRF的典型EPC组网之外， UNC 还允许采用N7接口连接PGW-C和PCF。PCF通过N7接口下发策略给PGW-C，MME实时将eNodeB侧上报的位置信息给SGW-C/PGW-C，PGW-C上报位置信息给PCF，PCF进行策略决策和更新。
    > 
    > 通过配置（ [**SET POLICYMODE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/策略模式选择/设置策略接口的选择方式（SET POLICYMODE）_09653658.md) ）命令， UNC 可以选择是通过Gx接口连接PCRF还是通过N7接口连接PCF。在这种场景下，Gx接口的消息和相关的信元换成了N7接口的相关消息和信元。N7接口和Gx接口对应的消息如下：
    > 
    > *表1 N7接口和Gx接口对应的消息*

### WSFD-011201

**md：`WSFD-011201/配置计费和策略接口选择（GGSN_SGW-C_PGW-C）_97906843.md`**
- 数据规划表（该命令的参数行）：
  | **SET POLICYMODE** | 指定终端和接入类型（TMACCTYPE） | UE5G_RAT4G | 全网规划 | 设置5G终端4G接入的策略接口为Npcf。 |
  | **SET POLICYMODE** | 按5GS互操作指示选择策略接口（BY5GSIWKI） | DISABLE | 全网规划 | 设置5G终端4G接入的策略接口为Npcf。 |
  | **SET POLICYMODE** | 指定的策略接口（FORCED） | Npcf | 全网规划 | 设置5G终端4G接入的策略接口为Npcf。 |
- 任务示例脚本（该命令行）：
  `SET POLICYMODE: TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=DISABLE, FORCED=Gx;`
  `SET POLICYMODE: TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=DISABLE, FORCED=Gx;`
- 操作步骤上下文（±2 行原文）：
  L85:
    >   ****ADD ROAMCHGMODE****
    > 4. 配置策略接口的选择方式。
    >   **SET POLICYMODE**
    > 5. 配置基于APN/DNN的策略接口的选择方式。
    >   **ADD APNPOLICYMODE**
  L118:
    > 
    > ```
    > SET POLICYMODE: TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=DISABLE, FORCED=Gx;
    > ```
    > 
  L146:
    > 
    > ```
    > SET POLICYMODE: TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=DISABLE, FORCED=Gx;
    > ```
    > 

### WSFD-011206

**md：`WSFD-011206/配置计费和策略模式_77825710.md`**
- 数据规划表（该命令的参数行）：
  | **SET POLICYMODE** | 指定终端和接入类型（TMACCTYPE） | UE5G_RAT4G | 全网规划 | 设置5G终端4G接入的策略接口为Npcf。 |
  | **SET POLICYMODE** | 按5GS互操作指示选择策略接口（BY5GSIWKI） | DISABLE | 全网规划 | 设置5G终端4G接入的策略接口为Npcf。 |
  | **SET POLICYMODE** | 指定的策略接口（FORCED） | Npcf | 全网规划 | 设置5G终端4G接入的策略接口为Npcf。 |
- 任务示例脚本（该命令行）：
  `SET POLICYMODE: TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=DISABLE, FORCED=Npcf;`
  `SET POLICYMODE: TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=DISABLE, FORCED=Npcf;`
- 操作步骤上下文（±2 行原文）：
  L84:
    >   ****ADD ROAMCHGMODE****
    > 4. 配置策略接口的选择方式。
    >   **SET POLICYMODE**
    > 5. 配置基于APN/DNN的策略接口的选择方式。
    >   **ADD APNPOLICYMODE**
  L117:
    > 
    > ```
    > SET POLICYMODE: TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=DISABLE, FORCED=Npcf;
    > ```
    > 
  L157:
    > 
    > ```
    > SET POLICYMODE: TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=DISABLE, FORCED=Npcf;
    > ```
    > 

### WSFD-109001

**md：`WSFD-109001/配置计费和策略接口选择（GGSN_SGW-C_PGW-C）_15408913.md`**
- 数据规划表（该命令的参数行）：
  | **SET POLICYMODE** | 指定终端和接入类型（TMACCTYPE） | UE5G_RAT4G | 全网规划 | 设置5G终端4G接入的策略接口为Npcf。 |
  | **SET POLICYMODE** | 按5GS互操作指示选择策略接口（BY5GSIWKI） | DISABLE | 全网规划 | 设置5G终端4G接入的策略接口为Npcf。 |
  | **SET POLICYMODE** | 指定的策略接口（FORCED） | Npcf | 全网规划 | 设置5G终端4G接入的策略接口为Npcf。 |
- 任务示例脚本（该命令行）：
  `SET POLICYMODE: TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=DISABLE, FORCED=Gx;`
  `SET POLICYMODE: TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=DISABLE, FORCED=Gx;`
- 操作步骤上下文（±2 行原文）：
  L85:
    >   ****ADD ROAMCHGMODE****
    > 4. 配置策略接口的选择方式。
    >   **SET POLICYMODE**
    > 5. 配置基于APN/DNN的策略接口的选择方式。
    >   **ADD APNPOLICYMODE**
  L118:
    > 
    > ```
    > SET POLICYMODE: TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=DISABLE, FORCED=Gx;
    > ```
    > 
  L146:
    > 
    > ```
    > SET POLICYMODE: TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=DISABLE, FORCED=Gx;
    > ```
    > 

### WSFD-102703

**md：`WSFD-102703/实现原理_89832510.md`**
- 操作步骤上下文（±2 行原文）：
  L65:
    > 4. UE在4G网络建立到紧急APN的PDN链接，默认承载QCI=5。
    >   > **说明**
    >   > 如果命令 **[SET POLICYMODE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/策略模式选择/设置策略接口的选择方式（SET POLICYMODE）_09653658.md)** 的 “FORCED” 参数配置为 “Gx（Gx接口）” ，通过CCR/CCA进行策略更新。
    >   >
    >   > 如果命令 **[SET POLICYMODE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/策略模式选择/设置策略接口的选择方式（SET POLICYMODE）_09653658.md)** 的 “FORCED” 参数配置为 “Npcf（Npcf接口）” ，通过Npcf_SMPolicyControl_Create Request/Response进行策略更新。
  L67:
    >   > 如果命令 **[SET POLICYMODE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/策略模式选择/设置策略接口的选择方式（SET POLICYMODE）_09653658.md)** 的 “FORCED” 参数配置为 “Gx（Gx接口）” ，通过CCR/CCA进行策略更新。
    >   >
    >   > 如果命令 **[SET POLICYMODE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/策略模式选择/设置策略接口的选择方式（SET POLICYMODE）_09653658.md)** 的 “FORCED” 参数配置为 “Npcf（Npcf接口）” ，通过Npcf_SMPolicyControl_Create Request/Response进行策略更新。
    >   >
    >   > 系统初始设置值为 “Gx（Gx接口）” 。

## ④ 自动比对
- 命令真相参数（6）：['BY5GCNRI', 'BY5GSIWKI', 'BYIWKUEN5GR4G', 'FORCED', 'PCFRESELBYPCFID', 'TMACCTYPE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 9}（多值→atom 应考虑 decision_driven）
