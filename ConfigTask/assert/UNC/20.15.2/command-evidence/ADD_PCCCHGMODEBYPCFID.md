# 命令证据包：ADD PCCCHGMODEBYPCFID
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/计费策略接口选择/增加基于PCF的计费策略接口类型（ADD PCCCHGMODEBYPCFID）_72001542.md`
> 用该命令的特性数：4

## ② 命令真相（mml_commands.jsonl）
**功能**：![](增加基于PCF的计费策略接口类型（ADD PCCCHGMODEBYPCFID）_72001542.assets/notice_3.0-zh-cn_2.png)

配置基于PCF的计费策略接口类型不当可能导致PCC用户选择错误接口的PCRF/PCF服务器，进而影响用户使用业务，比如用户无法正常激活。

**适用NF：SMF**

增加基于PCF的计费策略接口类型。当需要基于PCF实例标识调整
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。

- 用户的策略接口类型以ADD APNPOLICYMODE或SET POLICYMODE为初选结果，在此基础上，可以通过本命令决策是否由N7回落Gx，或者是否由Gx升级为N7。PCF实例标识在此命令中未配置时，用户的策略接口类型以ADD APNPOLICYMODE或SET POLICYMODE的初选结果为准。
- 用户的计费接口类型以ADD APNCHGMO

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| PCFINSID | PCF实例标识 | global_planned | required | 无 | 字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。 |
| POLICYINTF | 策略接口类型 | global_planned | required | 无 | <br>- “INHERIT（继承）”：继承ADD APNPOLICYMODE或SET POLICY |
| CHGINTF | 计费接口类型 | global_planned | required | 无 | <br>- “INHERIT（继承）”：继承ADD APNCHGMODE或SET CHGMODE命令 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 操作步骤上下文（±2 行原文）：
  L206:
    >       [**ADD APNPOLICYMODE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/基于APN的策略接口选择方式配置/增加基于APN的策略接口的选择方式（ADD APNPOLICYMODE）_72001541.md)
    >     3. **可选：**增加基于PCF实例标识的策略接口的选择模式。
    >       [**ADD PCCCHGMODEBYPCFID**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/计费策略接口选择/增加基于PCF的计费策略接口类型（ADD PCCCHGMODEBYPCFID）_72001542.md)
    > - SMF需要根据SERVINGSCOPE选择PCF时，配置PCF业务服务区和用户TAI区域的绑定关系。
    >     1. 增加PCF的业务服务区。

### WSFD-011201

**md：`WSFD-011201/配置计费和策略接口选择（GGSN_SGW-C_PGW-C）_97906843.md`**
- 数据规划表（该命令的参数行）：
  | **ADD PCCCHGMODEBYPCFID** | PCF实例标识（PCFINSID） | pcf1 | 全网规划 | （可选）一般情况下不需要配置该命令，当需要基于PCF实例标识调整用户最终使用的策略接口类型 (N7/Gx) 或计费接口类型 (N40/GaGy) 时，可以配置此命令。<br>用户的计费接口类型以<br>**ADD APNCHGMODE**<br>或<br>**SET CHGMODE**<br>为初选结果，在此基础上，可以通过该命令决策是否由N40回落GaGy，或者是否由GaGy升级为N40。 |
  | **ADD PCCCHGMODEBYPCFID** | 策略接口类型（POLICYINTF） | N7 | 全网规划 | （可选）一般情况下不需要配置该命令，当需要基于PCF实例标识调整用户最终使用的策略接口类型 (N7/Gx) 或计费接口类型 (N40/GaGy) 时，可以配置此命令。<br>用户的计费接口类型以<br>**ADD APNCHGMODE**<br>或<br>**SET CHGMODE**<br>为初选结果，在此基础上，可以通过该命令决策是否由N40回落GaGy，或者是否由GaGy升级为N40。 |
  | **ADD PCCCHGMODEBYPCFID** | 计费接口类型（CHGINTF） | N40 | 全网规划 | （可选）一般情况下不需要配置该命令，当需要基于PCF实例标识调整用户最终使用的策略接口类型 (N7/Gx) 或计费接口类型 (N40/GaGy) 时，可以配置此命令。<br>用户的计费接口类型以<br>**ADD APNCHGMODE**<br>或<br>**SET CHGMODE**<br>为初选结果，在此基础上，可以通过该命令决策是否由N40回落GaGy，或者是否由GaGy升级为N40。 |
- 操作步骤上下文（±2 行原文）：
  L31:
    > 当UNC在上述计费接口和策略接口决策下，为指定用户选择Gx策略接口进行策略处理时，计费接口和策略接口选择完成。
    > 
    > 当UNC在上述计费接口和策略接口决策下，为指定用户选择N7策略接口进行策略处理时，需要通过 **ADD PCCCHGMODEBYPCFID** 命令中指定PCF instance ID的配置决策用户策略执行是否使用Gx接口、计费执行是否使用Gy接口，即策略接口选择N7时，需要 **ADD PCCCHGMODEBYPCFID** 进行最终决策。
    > 
    > > **说明**
  L89:
    >   **ADD APNPOLICYMODE**
    > 6. **可选：**配置基于PCF的计费接口和策略接口类型。
    >   **ADD PCCCHGMODEBYPCFID**
    >   > **说明**
    >   > 一般情况下不需要配置该命令，当需要基于PCF实例标识调整用户最终使用的策略接口类型 (N7/Gx) 或计费接口类型 (N40/GaGy) 时，可以配置该命令。

### WSFD-011206

**md：`WSFD-011206/配置计费和策略模式_77825710.md`**
- 数据规划表（该命令的参数行）：
  | **ADD PCCCHGMODEBYPCFID** | PCF实例标识（PCFINSID） | pcf1 | 全网规划 | （可选）一般情况下不需要配置该命令，当需要基于PCF实例标识调整用户最终使用的策略接口类型 (N7/Gx) 或计费接口类型 (N40/GaGy) 时，可以配置此命令。<br>用户的计费接口类型以<br>**ADD APNCHGMODE**<br>或<br>**SET CHGMODE**<br>为初选结果，在此基础上，可以通过该命令决策是否由N40回落GaGy，或者是否由GaGy升级为N40。 |
  | **ADD PCCCHGMODEBYPCFID** | 策略接口类型（POLICYINTF） | N7 | 全网规划 | （可选）一般情况下不需要配置该命令，当需要基于PCF实例标识调整用户最终使用的策略接口类型 (N7/Gx) 或计费接口类型 (N40/GaGy) 时，可以配置此命令。<br>用户的计费接口类型以<br>**ADD APNCHGMODE**<br>或<br>**SET CHGMODE**<br>为初选结果，在此基础上，可以通过该命令决策是否由N40回落GaGy，或者是否由GaGy升级为N40。 |
  | **ADD PCCCHGMODEBYPCFID** | 计费接口类型（CHGINTF） | N40 | 全网规划 | （可选）一般情况下不需要配置该命令，当需要基于PCF实例标识调整用户最终使用的策略接口类型 (N7/Gx) 或计费接口类型 (N40/GaGy) 时，可以配置此命令。<br>用户的计费接口类型以<br>**ADD APNCHGMODE**<br>或<br>**SET CHGMODE**<br>为初选结果，在此基础上，可以通过该命令决策是否由N40回落GaGy，或者是否由GaGy升级为N40。 |
- 任务示例脚本（该命令行）：
  `ADD PCCCHGMODEBYPCFID: PCFINSID="pcf1",POLICYINTF=N7,CHGINTF=N40;`
  `ADD PCCCHGMODEBYPCFID: PCFINSID="pcf1",POLICYINTF=N7,CHGINTF=N40;`
- 操作步骤上下文（±2 行原文）：
  L31:
    > 当UNC在上述计费接口和策略接口决策下，为指定用户选择Gx策略接口进行策略处理时，计费接口和策略接口选择完成。
    > 
    > 当UNC上述计费接口和策略接口决策下，需要基于PCF实例标识调整用户最终使用的计费接口时，可以通过 **ADD PCCCHGMODEBYPCFID** 命令配置。此时，用户的计费接口类型以 **ADD APNCHGMODE** 或 **SET CHGMODE** 为初选结果，在此基础上，可以通过本命令决策是否由N40回落GaGy，或者是否由GaGy升级为N40。
    > 
    > > **说明**
  L88:
    >   **ADD APNPOLICYMODE**
    > 6. **可选：**配置基于PCF的计费接口和策略接口类型。
    >   **ADD PCCCHGMODEBYPCFID**
    >   > **说明**
    >   > 一般情况下不需要配置该命令，当需要基于PCF实例标识调整用户最终使用的策略接口类型 (N7/Gx) 或计费接口类型 (N40/GaGy) 时，可以配置该命令。
  L123:
    > 
    > ```
    > ADD PCCCHGMODEBYPCFID: PCFINSID="pcf1",POLICYINTF=N7,CHGINTF=N40;
    > ```
    > 

### WSFD-109001

**md：`WSFD-109001/配置计费和策略接口选择（GGSN_SGW-C_PGW-C）_15408913.md`**
- 数据规划表（该命令的参数行）：
  | **ADD PCCCHGMODEBYPCFID** | PCF实例标识（PCFINSID） | pcf1 | 全网规划 | （可选）一般情况下不需要配置该命令，当需要基于PCF实例标识调整用户最终使用的策略接口类型 (N7/Gx) 或计费接口类型 (N40/GaGy) 时，可以配置此命令。<br>用户的计费接口类型以<br>**ADD APNCHGMODE**<br>或<br>**SET CHGMODE**<br>为初选结果，在此基础上，可以通过该命令决策是否由N40回落GaGy，或者是否由GaGy升级为N40。 |
  | **ADD PCCCHGMODEBYPCFID** | 策略接口类型（POLICYINTF） | N7 | 全网规划 | （可选）一般情况下不需要配置该命令，当需要基于PCF实例标识调整用户最终使用的策略接口类型 (N7/Gx) 或计费接口类型 (N40/GaGy) 时，可以配置此命令。<br>用户的计费接口类型以<br>**ADD APNCHGMODE**<br>或<br>**SET CHGMODE**<br>为初选结果，在此基础上，可以通过该命令决策是否由N40回落GaGy，或者是否由GaGy升级为N40。 |
  | **ADD PCCCHGMODEBYPCFID** | 计费接口类型（CHGINTF） | N40 | 全网规划 | （可选）一般情况下不需要配置该命令，当需要基于PCF实例标识调整用户最终使用的策略接口类型 (N7/Gx) 或计费接口类型 (N40/GaGy) 时，可以配置此命令。<br>用户的计费接口类型以<br>**ADD APNCHGMODE**<br>或<br>**SET CHGMODE**<br>为初选结果，在此基础上，可以通过该命令决策是否由N40回落GaGy，或者是否由GaGy升级为N40。 |
- 操作步骤上下文（±2 行原文）：
  L31:
    > 当UNC在上述计费接口和策略接口决策下，为指定用户选择Gx策略接口进行策略处理时，计费接口和策略接口选择完成。
    > 
    > 当UNC在上述计费接口和策略接口决策下，为指定用户选择N7策略接口进行策略处理时，需要通过 **ADD PCCCHGMODEBYPCFID** 命令中指定PCF instance ID的配置决策用户策略执行是否使用Gx接口、计费执行是否使用Gy接口，即策略接口选择N7时，需要 **ADD PCCCHGMODEBYPCFID** 进行最终决策。
    > 
    > > **说明**
  L89:
    >   **ADD APNPOLICYMODE**
    > 6. **可选：**配置基于PCF的计费接口和策略接口类型。
    >   **ADD PCCCHGMODEBYPCFID**
    >   > **说明**
    >   > 一般情况下不需要配置该命令，当需要基于PCF实例标识调整用户最终使用的策略接口类型 (N7/Gx) 或计费接口类型 (N40/GaGy) 时，可以配置该命令。

## ④ 自动比对
- 命令真相参数（3）：['CHGINTF', 'PCFINSID', 'POLICYINTF']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 9}（多值→atom 应考虑 decision_driven）
