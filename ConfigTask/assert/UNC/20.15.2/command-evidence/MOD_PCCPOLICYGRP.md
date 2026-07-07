# 命令证据包：MOD PCCPOLICYGRP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_09897174.md`
> 用该命令的特性数：5

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

此命令用于修改PccPolicyGrp配置，只有已经添加成功的PccPolicyGrp才能够修改。可以通过此命令，修改PCC策略组，包括计费属性、Qos属性、扩展属性等构成策略集，同时支持基于ServiceProp选择不同的非默认策略集。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- PccPolicyGrp可以包含URRGroupName(Charge porperty)，FupSessionExc，QosPropName，所有参数都是可选，如果一个都没有选，则配置一个空的PccPolicyGrp。
- PccPolicyGrp中最多可以配置十个URRGroupName，FupSessionExc的组合。一个默认组合，九个非默认组合，或者无默认

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| PCCPOLICYGRPNM | PCC策略组名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| URRGROUPNAME | 使用量上报规则组名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| FUPSESSIONEXC | Session级FUP累计标识 | local_planned | optional | 无 | 枚举类型。 |
| QOSPROPNAME | QoS属性名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109103

**md：`WSFD-109103/WSFD-109103 IPv6 SA参考信息_78881328.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > - [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    > - [**MOD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_09897174.md)/[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)

### WSFD-109104

**md：`WSFD-109104/WSFD-109104 基于累计流量的策略控制参考信息_29056192.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > - [**MOD PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/修改PCRF（MOD PCRF）_09897102.md)
    > - [**MOD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_09897174.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0229056192)

**md：`WSFD-109104/激活基于累计流量的策略控制_29056190.md`**
- 数据规划表（该命令的参数行）：
  | [**MOD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_09897174.md) | PCC策略组名称（PCCPOLICYGRPNM ） | pccpolicygrp_01 | 已配置数据中获取 | 使用<br>[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)<br>定义的PCC策略组名称。 |
  | [**MOD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_09897174.md) | Session级FUP累计标识（FUPSESSIONEXC ） | ENABLE | 本端规划 | ENABLE表示该PCC策略组对应的业务不计入Session级流量。 |
- 操作步骤上下文（±2 行原文）：
  L45:
    >   [**MOD PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/修改PCRF（MOD PCRF）_09897102.md)
    > 5. 配置将某类业务/应用的流量不统计到会话级流量。
    >   [**MOD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_09897174.md)
    >   “Session级FUP累计标识（FUPSESSIONEXC）” 默认值为 “DISABLE” ，表示该PCC策略组对应的业务计入Session级流量。
    > 

### WSFD-211009

**md：`WSFD-211009/WSFD-211009 基于业务累计流量的策略控制参考信息_27915158.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > - [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    > - [**MOD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_09897174.md)/[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)

### WSFD-011206

**md：`WSFD-011206/调测融合计费的流量计费功能_89257221.md`**
- 操作步骤上下文（±2 行原文）：
  L56:
    >           - 如果绑定了计费RG，且匹配中业务流，请执行[步骤 8](#ZH-CN_OPI_0289257221__step1829245425110)。
    >           - 如果没有绑定计费RG，请执行[步骤 7.b](#ZH-CN_OPI_0289257221__substep469521910418)。
    >     b. 执行 [**MOD URR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/修改URR（MOD URR）_09897159.md) 、 [**MOD URRGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/修改URR组（MOD URRGROUP）_09897194.md) 、 [**MOD PCCPOLICYGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_09897174.md) 、 [**MOD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/修改规则（MOD RULE）_09897202.md) ，按照规划值为用户绑定RG。重新激活用户，观察N40接口计费流量与用户实际访问流量是否一致。
    >           - 如果一致，调测完成。
    >           - 如果不一致，请执行[步骤 8](#ZH-CN_OPI_0289257221__step1829245425110)。

### WSFD-201207

**md：`WSFD-201207/WSFD-201207 语音PCF_PCRF故障Bypass参考信息_85304300.md`**
- 操作步骤上下文（±2 行原文）：
  L40:
    > **[RMV PCCPOLICYGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/删除PCC策略组（RMV PCCPOLICYGRP）_09897175.md)**
    > 
    > **[MOD PCCPOLICYGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_09897174.md)**
    > 
    > **[LST PCCPOLICYGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/查询PCC策略组（LST PCCPOLICYGRP）_09897176.md)**

## ④ 自动比对
- 命令真相参数（4）：['FUPSESSIONEXC', 'PCCPOLICYGRPNM', 'QOSPROPNAME', 'URRGROUPNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 1, '本端规划': 1}（多值→atom 应考虑 decision_driven）
