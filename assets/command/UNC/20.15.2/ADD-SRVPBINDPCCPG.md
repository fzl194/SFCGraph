---
id: UNC@20.15.2@MMLCommand@ADD SRVPBINDPCCPG
type: MMLCommand
name: ADD SRVPBINDPCCPG（增加PCC组业务属性绑定）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SRVPBINDPCCPG
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 90000
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务策略
- PCC策略组业务属性绑定
status: active
---

# ADD SRVPBINDPCCPG（增加PCC组业务属性绑定）

## 功能

**适用NF：PGW-C、SMF**

此命令用于新增PCC策略组业务属性绑定组合。可以通过命令，配置包含业务属性的非默认组合，非默认组合还可以包括使用量上报规则组、Session级FUP累计标识等。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为90000。
- 每个PCC策略组可以配置十个基于业务属性的非默认组合。
- 配置PCC策略组基于业务属性的非默认组合，可以包含用量上报规则组、Session级FUP累计标识等，所有参数都是可选，如果一个都没有选，则配置一个空的SrvPBindPccPG。
- 如果每个PCC策略组配置了多种非默认组合，则匹配优先级取决于SrvPBindPccPG下配置的ServiceProp优先级。默认组合的优先级最低。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCCPOLICYGRPNM | PCC策略组名称 | 可选必选说明：必选参数<br>参数含义：PCC策略组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD PCCPOLICYGRP命令配置生成。 |
| SRVPROPNAME | 业务属性名称 | 可选必选说明：必选参数<br>参数含义：业务属性名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD SERVICEPROP命令配置生成。<br>- 如果运营商需要定义该PCC策略组基于业务属性的非默认策略组合时，需要配置业务属性对象名称，只有签约了该业务属性才可以选择本策略组合中的各种策略进行业务处理。 |
| URRGROUPNAME | 使用量上报规则组名称 | 可选必选说明：可选参数<br>参数含义：使用量上报规则组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD URRGROUP命令配置生成。<br>- 如果运营商需要定义该PCC策略组基于该业务属性的计费策略时，建议配置用于计费处理的计费属性对象名称。 |
| FUPSESSIONEXC | Session级FUP累计标识 | 可选必选说明：可选参数<br>参数含义：设置Session级FUP流量累计标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能，表明该PccPolicyGrp对应的业务流量计入Session级流量。<br>- ENABLE：使能，表明该PccPolicyGrp对应的业务流量不计入Session级流量。<br>默认值：DISABLE<br>配置原则：如果运营商需要定义该PCC策略组基于该业务属性的业务级FUP流量累计时，是否同时累计到Session级流量，建议配置Session级FUP流量累计标识。 |

## 操作的配置对象

- [PCC组业务属性绑定（SRVPBINDPCCPG）](configobject/UNC/20.15.2/SRVPBINDPCCPG.md)

## 使用实例

假如运营商需要为PCC策略组TestPccPolicyGrpName增加一个基于名称为TestServicePropName的业务属性的策略组合，要求在该PCC策略组合中包含使用量上报规则组、Session级FUP累计标识且不需要累计到Session级流量中进行上报。 增加PCC策略组业务属性绑定组合，设置包括业务属性、使用量上报规则组、Session级FUP累计标识的默认组合；“PCCPOLICYGRPNM”为“TestPccPolicyGrpName”，“SRVPROPNAME”为“TestServicePropName”，“URRGROUPNAME”为“TestUrrGroupName”，“FUPSESSIONEXC”为“ENABLE”：

```
ADD SRVPBINDPCCPG:PCCPOLICYGRPNM="TestPccPolicyGrpName",SRVPROPNAME="TestServicePropName",URRGROUPNAME="TestUrrGroupName", FUPSESSIONEXC=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加PCC组业务属性绑定（ADD-SRVPBINDPCCPG）_09897178.md`
