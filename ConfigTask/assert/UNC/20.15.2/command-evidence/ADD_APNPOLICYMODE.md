# 命令证据包：ADD APNPOLICYMODE
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/基于APN的策略接口选择方式配置/增加基于APN的策略接口的选择方式（ADD APNPOLICYMODE）_72001541.md`
> 用该命令的特性数：4

## ② 命令真相（mml_commands.jsonl）
**功能**：![](增加基于APN的策略接口的选择方式（ADD APNPOLICYMODE）_72001541.assets/notice_3.0-zh-cn_2.png)

配置基于APN的策略接口的选择方式不当可能导致PCC用户选择错误接口的PCRF/PCF服务器，进而影响用户使用业务，比如用户无法正常激活。

**适用NF：PGW-C、SMF、GGSN**

该命令用于增加基于APN的策略接口的选择方式
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。

- 当需要使用本命令配置2G和3G接入使用Npcf接口时，需要提前和对端PCF确认是否支持。

- 最多可输入20000条记录。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| APN | APN名称 | local_planned | required | 无 | 字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字 |
| TMACCTYPE | 指定终端和接入类型 | local_planned | required | 无 | <br>- “UE5G_RAT4G（5G终端4G接入）”：5G终端4G接入是指在4G接入的PDN激活 |
| BY5GSIWKI | 按5GS互操作指示选择策略接口开关 | local_planned | conditional | DISABLE | <br>- “DISABLE（不使能）”：不使能 |
| FORCED | 指定策略接口 | local_planned | conditional | 无 | <br>- “Npcf（Npcf接口）”：使用Npcf接口。 |
| PCFRESELBYPCFID | 是否基于PCF实例标识决策策略接口类型 | local_planned | optional | 无 | <br>- TRUE(TRUE) |
| BY5GCNRI | 按5GC无限制接入标识选择策略接口开关 | local_planned | conditional | DISABLE | <br>- “DISABLE（不使能）”：不使能 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 操作步骤上下文（±2 行原文）：
  L204:
    >       [**SET POLICYMODE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/策略模式选择/设置策略接口的选择方式（SET POLICYMODE）_09653658.md)
    >     2. **可选：**增加基于APN的策略接口的选择模式。
    >       [**ADD APNPOLICYMODE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/基于APN的策略接口选择方式配置/增加基于APN的策略接口的选择方式（ADD APNPOLICYMODE）_72001541.md)
    >     3. **可选：**增加基于PCF实例标识的策略接口的选择模式。
    >       [**ADD PCCCHGMODEBYPCFID**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/计费策略接口选择/增加基于PCF的计费策略接口类型（ADD PCCCHGMODEBYPCFID）_72001542.md)

### WSFD-011201

**md：`WSFD-011201/配置计费和策略接口选择（GGSN_SGW-C_PGW-C）_97906843.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APNPOLICYMODE** | APN名称（APN） | apn-test | 已配置数据中获取 | 添加APN/DNN策略接口选择方式，指定5G终端4G接入的策略接口为Npcf。 |
  | **ADD APNPOLICYMODE** | 指定终端和接入类型（TMACCTYPE） | UE5G_RAT4G | 本端规划 | 添加APN/DNN策略接口选择方式，指定5G终端4G接入的策略接口为Npcf。 |
  | **ADD APNPOLICYMODE** | 按5GS互操作指示选择策略接口（BY5GSIWKI） | DISABLE | 本端规划 | 添加APN/DNN策略接口选择方式，指定5G终端4G接入的策略接口为Npcf。 |
  | **ADD APNPOLICYMODE** | 指定的策略接口（FORCED） | Npcf | 本端规划 | 添加APN/DNN策略接口选择方式，指定5G终端4G接入的策略接口为Npcf。 |
- 任务示例脚本（该命令行）：
  `ADD APNPOLICYMODE: APN="HUAWEI.COM",TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=DISABLE, FORCED=Gx;`
- 操作步骤上下文（±2 行原文）：
  L87:
    >   **SET POLICYMODE**
    > 5. 配置基于APN/DNN的策略接口的选择方式。
    >   **ADD APNPOLICYMODE**
    > 6. **可选：**配置基于PCF的计费接口和策略接口类型。
    >   **ADD PCCCHGMODEBYPCFID**
  L132:
    > 
    > ```
    > ADD APNPOLICYMODE: APN="HUAWEI.COM",TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=DISABLE, FORCED=Gx;
    > ```
    > 

### WSFD-011206

**md：`WSFD-011206/配置计费和策略模式_77825710.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APNPOLICYMODE** | APN名称（APN） | apn-test | 已配置数据中获取 | 添加APN/DNN策略接口选择方式，指定5G终端4G接入的策略接口为Npcf。 |
  | **ADD APNPOLICYMODE** | 指定终端和接入类型（TMACCTYPE） | UE5G_RAT4G | 本端规划 | 添加APN/DNN策略接口选择方式，指定5G终端4G接入的策略接口为Npcf。 |
  | **ADD APNPOLICYMODE** | 按5GS互操作指示选择策略接口（BY5GSIWKI） | DISABLE | 本端规划 | 添加APN/DNN策略接口选择方式，指定5G终端4G接入的策略接口为Npcf。 |
  | **ADD APNPOLICYMODE** | 指定的策略接口（FORCED） | Npcf | 本端规划 | 添加APN/DNN策略接口选择方式，指定5G终端4G接入的策略接口为Npcf。 |
- 任务示例脚本（该命令行）：
  `ADD APNPOLICYMODE: APN="HUAWEI.COM",TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=DISABLE, FORCED=Npcf;`
- 操作步骤上下文（±2 行原文）：
  L86:
    >   **SET POLICYMODE**
    > 5. 配置基于APN/DNN的策略接口的选择方式。
    >   **ADD APNPOLICYMODE**
    > 6. **可选：**配置基于PCF的计费接口和策略接口类型。
    >   **ADD PCCCHGMODEBYPCFID**
  L137:
    > 
    > ```
    > ADD APNPOLICYMODE: APN="HUAWEI.COM",TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=DISABLE, FORCED=Npcf;
    > ```
    > 

### WSFD-109001

**md：`WSFD-109001/配置计费和策略接口选择（GGSN_SGW-C_PGW-C）_15408913.md`**
- 数据规划表（该命令的参数行）：
  | **ADD APNPOLICYMODE** | APN名称（APN） | apn-test | 已配置数据中获取 | 添加APN/DNN策略接口选择方式，指定5G终端4G接入的策略接口为Npcf。 |
  | **ADD APNPOLICYMODE** | 指定终端和接入类型（TMACCTYPE） | UE5G_RAT4G | 本端规划 | 添加APN/DNN策略接口选择方式，指定5G终端4G接入的策略接口为Npcf。 |
  | **ADD APNPOLICYMODE** | 按5GS互操作指示选择策略接口（BY5GSIWKI） | DISABLE | 本端规划 | 添加APN/DNN策略接口选择方式，指定5G终端4G接入的策略接口为Npcf。 |
  | **ADD APNPOLICYMODE** | 指定的策略接口（FORCED） | Npcf | 本端规划 | 添加APN/DNN策略接口选择方式，指定5G终端4G接入的策略接口为Npcf。 |
- 任务示例脚本（该命令行）：
  `ADD APNPOLICYMODE: APN="HUAWEI.COM",TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=DISABLE, FORCED=Gx;`
- 操作步骤上下文（±2 行原文）：
  L87:
    >   **SET POLICYMODE**
    > 5. 配置基于APN/DNN的策略接口的选择方式。
    >   **ADD APNPOLICYMODE**
    > 6. **可选：**配置基于PCF的计费接口和策略接口类型。
    >   **ADD PCCCHGMODEBYPCFID**
  L132:
    > 
    > ```
    > ADD APNPOLICYMODE: APN="HUAWEI.COM",TMACCTYPE=UE5G_RAT4G, BY5GSIWKI=DISABLE, FORCED=Gx;
    > ```
    > 

## ④ 自动比对
- 命令真相参数（6）：['APN', 'BY5GCNRI', 'BY5GSIWKI', 'FORCED', 'PCFRESELBYPCFID', 'TMACCTYPE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 3, '本端规划': 9}（多值→atom 应考虑 decision_driven）
