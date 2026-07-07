# 命令证据包：ADD PCCPOLICYGRP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md`
> 用该命令的特性数：11

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

此命令用于增加PCC策略组配置。当需要配置PCC策略组时，可以通过此命令配置包括计费属性、Qos属性、扩展属性等构成的策略集，同时支持基于ServiceProp选择不同的非默认策略集。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为40000。
- PccPolicyGrp可以包含URRGroupName(Charge porperty)，FupSessionExc，QosPropName，所有参数都是可选，如果一个都没有选，则配置一个空的PccPolicyGrp。
- PccPolicyGrp中最多可以配置十个URRGroupName，FupSessionExc的组合。一个

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| PCCPOLICYGRPNM | PCC策略组名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| URRGROUPNAME | 使用量上报规则组名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| FUPSESSIONEXC | Session级FUP累计标识 | local_planned | optional | DISABLE | 枚举类型。 |
| QOSPROPNAME | QoS属性名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L27:
    > - [**ADD UPBINDUPG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD PCCPOLICYGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULEBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD APNUSRPROFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)

**md：`WSFD-109101/配置本地PCC功能_30805097.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCCPOLICYGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | PCC策略组名称（PCCPOLICYGRPNM） | pccpolicy_group | 本端规划 | 配置QoS类型的PCC策略。 |
  | [**ADD PCCPOLICYGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | Qos属性名称（QOSPROPNAME） | qos_property1 | 已配置数据中获取 | 配置QoS类型的PCC策略。 |
- 任务示例脚本（该命令行）：
  `ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicy_group",QOSPROPNAME="qos_property1";`
- 操作步骤上下文（±2 行原文）：
  L88:
    >       [**ADD QOSPROP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)
    >     b. 配置PCC策略。
    >       [**ADD PCCPOLICYGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    >     c. 配置本地静态规则
    >       [**ADD RULE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
  L145:
    >   ```
    >   ```
    >   ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicy_group",QOSPROPNAME="qos_property1";
    >   ```
    >   ```

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCCPOLICYGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | PCC策略组名称（PCCPOLICYGRPNM） | pccpolicygrp_01 | 本端规划 | 存在多条记录时，该参数不能重复。 |
  | [**ADD PCCPOLICYGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | 使用量上报规则组名称（URRGROUPNAME） | urrgrp_01 | 已配置数据中获取 | 使用<br>[**ADD URRGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)<br>定义的URRGROUPNAME。 |
  | [**ADD PCCPOLICYGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | Session级FUP累计标识（FUPSESSIONEXC ） | ENABLE | 本端规划 | ENABLE表示该PCC策略组对应的业务不计入Session级流量。默认DISABLE，计入Session级流量。 |
- 任务示例脚本（该命令行）：
  `ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicy_group",URRGROUPNAME="urrgrp_01",FUPSESSIONEXC=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L171:
    >             [**MOD NFPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/NF概述信息管理/修改NF实例概述信息（MOD NFPROFILE）_09652236.md)
    >     11. **可选：**配置PCC策略组。用于动态PCC时PCF下发预定义规则，或本地PCC时的静态规则。
    >       [**ADD PCCPOLICYGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    >     12. **可选：**配置SMF上的本地rule。用于动态PCC时PCF下发预定义规则，或本地PCC时的静态规则。
    >       [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
  L252:
    > 
    > ```
    > ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicy_group",URRGROUPNAME="urrgrp_01",FUPSESSIONEXC=ENABLE;
    > ADD RULE:RULENAME="rule_test",POLICYTYPE=PCC,POLICYNAME="pccpolicy_group",RULERANGE=ALL;
    > ```

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

**md：`WSFD-109104/激活基于累计流量的策略控制_29056190.md`**
- 任务示例脚本（该命令行）：
  `ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicygrp_01", FUPSESSIONEXC=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L77:
    > 
    > ```
    > ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicygrp_01", FUPSESSIONEXC=ENABLE;
    > ```

### WSFD-109107

**md：`WSFD-109107/WSFD-109107 业务触发的QoS保证参考信息_85397060.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    > - [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)
    > - [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)

**md：`WSFD-109107/激活业务触发的QoS保证_85397058.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | PCC策略组名称（PCCPOLICYGRPNM） | pccpolicygrp_01 | 本端规划 | 存在多条记录时，该参数不能重复。 |
  | [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | QOSPROPNAME（Qos属性名称） | qosprop_501 | 已配置数据中获取 | 使用<br>[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)<br>定义的QOSPROPNAME。 |
- 任务示例脚本（该命令行）：
  `ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicy_group",QOSPROPNAME="qosprop_501";`
- 操作步骤上下文（±2 行原文）：
  L76:
    >   [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)
    > 4. 规则通过PCC策略组绑定QoS属性时，配置PCC策略组。规则直接绑定QoS属性时，请跳过本步骤。
    >   [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > 5. 配置SMF上的本地rule。
    >   [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
  L79:
    > 5. 配置SMF上的本地rule。
    >   [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    >     - 规则通过PCC策略组绑定QoS属性时，“POLICYTYPE”设置为“PCC”，“POLICYNAME”使用[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)命令配置的“PCCPOLICYGRPNM”参数值。
    >     - 规则直接绑定QoS属性时，“POLICYTYPE”设置为“QOS”“POLICYNAME”使用[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)命令配置的“QOSPROPNAME”参数值。
    >     - PCC类型的“RULENAME”值与QOS类型的“RULENAME”值不能相同。
  L139:
    > 
    > ```
    > ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicy_group",QOSPROPNAME="qosprop_501";
    > ADD RULE:RULENAME="rule_test",POLICYTYPE=PCC,POLICYNAME="pccpolicy_group";
    > ```

### WSFD-211009

**md：`WSFD-211009/WSFD-211009 基于业务累计流量的策略控制参考信息_27915158.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > - [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    > - [**MOD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_09897174.md)/[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)

**md：`WSFD-211009/激活基于业务累计流量的策略控制_27915156.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | PCC策略组名称（PCCPOLICYGRPNM） | pccpolicygrp_01 | 本端规划 | 存在多条记录时，该参数不能重复。 |
  | [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | 使用量上报规则组名称（URRGROUPNAME） | urrgrp_01 | 已配置数据中获取 | 使用<br>[**ADD URRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)<br>定义的URRGROUPNAME。 |
  | [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | Session级FUP累计标识（FUPSESSIONEXC ） | ENABLE | 本端规划 | ENABLE表示该PCC策略组对应的业务不计入Session级流量。默认DISABLE，计入Session级流量。 |
- 任务示例脚本（该命令行）：
  `ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicygrp_01",URRGROUPNAME="urr_01",FUPSESSIONEXC=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L55:
    >   [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    > 5. 在PCC策略组中配置用于累计流量的URR标识。
    >   [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > 6. 配置预定义规则。
    >   [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
  L87:
    > 
    > ```
    > ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicygrp_01",URRGROUPNAME="urr_01",FUPSESSIONEXC=ENABLE;
    > ```
    > 

### WSFD-011201

**md：`WSFD-011201/配置离线计费的费率标识（GGSN_SGW-C_PGW-C）_98555879.md`**
- 数据规划表（该命令的参数行）：
  | **ADD PCCPOLICYGRP** | PCC策略组名称（PCCPOLICYGRPNM） | cg-test | 本端规划 | 配置内容计费使用的Rule。 |
- 任务示例脚本（该命令行）：
  `ADD PCCPOLICYGRP: PCCPOLICYGRPNM="cg-test", URRGROUPNAME="urrgroup1";`
- 操作步骤上下文（±2 行原文）：
  L97:
    >     3. 配置内容计费使用的Rule，将URR组绑定到对应的Rule上。
    >           a. 配置Rule绑定的PCC策略组，将URR组绑定到PCC策略组。
    >             **ADD PCCPOLICYGRP**
    >           b. 配置Rule，将PCC策略组绑定到Rule上。
    >             **ADD RULE**
  L161:
    > 
    >   ```
    >   ADD PCCPOLICYGRP: PCCPOLICYGRPNM="cg-test", URRGROUPNAME="urrgroup1";
    >   ADD RULE: RULENAME="Rule001", POLICYTYPE=PCC, PRIORITY=110, POLICYNAME="cg-test";
    >   ```

### WSFD-011206

**md：`WSFD-011206/配置融合计费费率标识_93360308.md`**
- 数据规划表（该命令的参数行）：
  | **ADD PCCPOLICYGRP** | PCC策略组名称（PCCPOLICYGRPNM） | pccpolicy_URL<br>pccpolicy_IMS<br>pccpolicy_any | 本端规划 | 配置PCC业务策略组。 |
  | **ADD PCCPOLICYGRP** | URR组名称（URRGROUPNAME） | UrrGp_URL<br>UrrGp_IMS<br>UrrGp_any | 已配置数据中获取 | 使用<br>**ADD URRGROUP**<br>命令定义的<br>“URRGROUPNAME”<br>。 |
- 任务示例脚本（该命令行）：
  `ADD PCCPOLICYGRP: PCCPOLICYGRPNM="pccpolicy_URL", URRGROUPNAME="UrrGp_URL";`
  `ADD PCCPOLICYGRP: PCCPOLICYGRPNM="pccpolicy_IMS", URRGROUPNAME="UrrGp_IMS";`
  `ADD PCCPOLICYGRP: PCCPOLICYGRPNM="pccpolicy_any", URRGROUPNAME="UrrGp_any";`
- 操作步骤上下文（±2 行原文）：
  L94:
    >     2. 配置内容计费使用的Rule，将URR组绑定到对应的Rule上。
    >           a. 配置PCC策略组，将URR组绑定到PCC策略组。
    >             **ADD PCCPOLICYGRP**
    >           b. 配置Rule，将PCC策略组绑定到Rule上。
    >             **ADD RULE**
  L167:
    > 
    > ```
    > ADD PCCPOLICYGRP: PCCPOLICYGRPNM="pccpolicy_URL", URRGROUPNAME="UrrGp_URL";
    > ADD PCCPOLICYGRP: PCCPOLICYGRPNM="pccpolicy_IMS", URRGROUPNAME="UrrGp_IMS";
    > ADD PCCPOLICYGRP: PCCPOLICYGRPNM="pccpolicy_any", URRGROUPNAME="UrrGp_any";
  L168:
    > ```
    > ADD PCCPOLICYGRP: PCCPOLICYGRPNM="pccpolicy_URL", URRGROUPNAME="UrrGp_URL";
    > ADD PCCPOLICYGRP: PCCPOLICYGRPNM="pccpolicy_IMS", URRGROUPNAME="UrrGp_IMS";
    > ADD PCCPOLICYGRP: PCCPOLICYGRPNM="pccpolicy_any", URRGROUPNAME="UrrGp_any";
    > ```

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L40:
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L40:
    > - [**ADD UPBINDUPG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)
    > - [**ADD APNUSRPROFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)

**md：`WSFD-109001/配置在线计费的费率标识_95923388.md`**
- 数据规划表（该命令的参数行）：
  | **ADD PCCPOLICYGRP** | PCC策略组名称（PCCPOLICYGRPNM） | cg-test | 本端规划 | 配置内容计费使用的Rule。 |
- 任务示例脚本（该命令行）：
  `ADD PCCPOLICYGRP: PCCPOLICYGRPNM="cg-test", URRGROUPNAME="urrgroup001";`
- 操作步骤上下文（±2 行原文）：
  L101:
    >     3. 配置内容计费使用的Rule，将URR组绑定到对应的Rule上。
    >           a. 配置Rule绑定的PCC策略组，将URR组绑定到PCC策略组。
    >             **ADD PCCPOLICYGRP**
    >           b. 配置Rule，将PCC策略组绑定到Rule上。
    >             **ADD RULE**
  L166:
    > 
    >   ```
    >   ADD PCCPOLICYGRP: PCCPOLICYGRPNM="cg-test", URRGROUPNAME="urrgroup001";
    >   ADD RULE: RULENAME="Rule002", POLICYTYPE=PCC, POLICYNAME="cg-test",PRIORITY=120;
    >   ```

### WSFD-109007

**md：`WSFD-109007/WSFD-109007 支持事件计费参考信息_74112323.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - [**ADD URRGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)
    > - [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD CCT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)

**md：`WSFD-109007/配置事件计费功能_74112321.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | PCCPOLICYGRPNM（PCC策略组名称） | cg-test | 本端规划 | 配置事件计费使用的Rule。 |
- 任务示例脚本（该命令行）：
  `ADD PCCPOLICYGRP: PCCPOLICYGRPNM="cg-test", URRGROUPNAME="urrgroup1";`
- 操作步骤上下文（±2 行原文）：
  L82:
    > 5. 配置事件计费使用的Rule，将URR组绑定到对应的Rule上。
    >     a. 配置Rule绑定的PCC策略组，将URR组绑定到PCC策略组。
    >       [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    >     b. 配置Rule，将PCC策略组绑定到Rule上。
    >       [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
  L137:
    > 
    > ```
    > ADD PCCPOLICYGRP: PCCPOLICYGRPNM="cg-test", URRGROUPNAME="urrgroup1";
    > ADD RULE: RULENAME="rule-test", POLICYTYPE=PCC, POLICYNAME="cg-test";
    > ```

### WSFD-201207

**md：`WSFD-201207/WSFD-201207 语音PCF_PCRF故障Bypass参考信息_85304300.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > **[LST QOSPROP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/查询QoS属性（LST QOSPROP）_09897166.md)**
    > 
    > [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    > 
    > **[RMV PCCPOLICYGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/删除PCC策略组（RMV PCCPOLICYGRP）_09897175.md)**

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（Gx接口）_60552093.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | PCC策略组名称（PCCPOLICYGRPNM） | pccpolicygrp_signaling | 本端规划 | 配置PCC策略组。存在多条记录时，PCC策略组名称不能重复。 |
  | [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | 使用量上报规则组名称（URRGROUPNAME） | urrg_signaling_01 | 已配置数据中获取 | 使用<br>**[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)**<br>定义的使用量上报规则组。 |
  | [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | PCC策略组名称（PCCPOLICYGRPNM） | pccpolicygrp_voice | 本端规划 | 配置PCC策略组。存在多条记录时，PCC策略组名称不能重复。 |
  | [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | 使用量上报规则组名称（URRGROUPNAME） | urrg_voice_01 | 已配置数据中获取 | 使用<br>**[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)**<br>定义的使用量上报规则组。 |
  | [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | Qos属性名称（QOSPROPNAME） | qosprop_voice | 已配置数据中获取 | 使用<br>[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)<br>定义的QOSPROPNAME。 |
- 任务示例脚本（该命令行）：
  `ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicygrp_signaling", URRGROUPNAME="urrg_signaling_01";`
  `ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicygrp_voice", URRGROUPNAME="urrg_voice_01", QOSPROPNAME="qosprop_voice";`
  `ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicygrp_voice", URRGROUPNAME="urrg_voice_01", QOSPROPNAME="qosprop_voice";`
- 操作步骤上下文（±2 行原文）：
  L198:
    >       **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)**
    >     c. 配置PCC策略组。
    >       [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    >     d. 配置业务策略规则。
    >       [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
  L229:
    >       [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)
    >     d. 配置PCC策略组。
    >       [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    >     e. 配置业务策略规则。
    >       [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
  L316:
    > 
    >       ```
    >       ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicygrp_signaling", URRGROUPNAME="urrg_signaling_01";
    >       ```
    >       //配置业务策略规则。

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（N7接口）_32852169.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | PCC策略组名称（PCCPOLICYGRPNM） | pccpolicygrp_signaling | 本端规划 | 配置PCC策略组。存在多条记录时，PCC策略组名称不能重复。 |
  | [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | 使用量上报规则组名称（URRGROUPNAME） | urrg_signaling_01 | 已配置数据中获取 | 使用<br>**[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)**<br>定义的使用量上报规则组。 |
  | [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | PCC策略组名称（PCCPOLICYGRPNM） | pccpolicygrp_voice | 本端规划 | 配置PCC策略组。存在多条记录时，PCC策略组名称不能重复。 |
  | [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | 使用量上报规则组名称（URRGROUPNAME） | urrg_voice_01 | 已配置数据中获取 | 使用<br>**[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)**<br>定义的使用量上报规则组。 |
  | [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | Qos属性名称（QOSPROPNAME） | qosprop_voice | 已配置数据中获取 | 使用<br>[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)<br>定义的QOSPROPNAME。 |
- 任务示例脚本（该命令行）：
  `ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicygrp_signaling", URRGROUPNAME="urrg_signaling_01";`
  `ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicygrp_voice", URRGROUPNAME="urrg_voice_01", QOSPROPNAME="qosprop_voice";`
  `ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicygrp_voice", URRGROUPNAME="urrg_voice_01", QOSPROPNAME="qosprop_voice";`
- 操作步骤上下文（±2 行原文）：
  L217:
    >       **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)**
    >     c. 配置PCC策略组。
    >       [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    >     d. 配置业务策略规则。
    >       [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
  L248:
    >       [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)
    >     d. 配置PCC策略组。
    >       [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    >     e. 配置业务策略规则。
    >       [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
  L344:
    > 
    >       ```
    >       ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicygrp_signaling", URRGROUPNAME="urrg_signaling_01";
    >       ```
    >       //配置业务策略规则。

## ④ 自动比对
- 命令真相参数（4）：['FUPSESSIONEXC', 'PCCPOLICYGRPNM', 'QOSPROPNAME', 'URRGROUPNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 14, '已配置数据中获取': 11}（多值→atom 应考虑 decision_driven）
