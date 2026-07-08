---
id: UDG@20.15.2@MMLCommand@MOD APPLYCOST
type: MMLCommand
name: MOD APPLYCOST（修改路由开销值设置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: APPLYCOST
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 应用Cost
status: active
---

# MOD APPLYCOST（修改路由开销值设置）

## 功能

该命令用于修改路由开销值。

## 注意事项

- 该命令执行后立即生效。
- 配置该命令前，必须已经配置了指定路由策略的名字以及该策略下的节点。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：不支持输入空格，必须存在该路由策略。 |
| NODESEQUENCE | 路由策略节点号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：必须存在该路由策略节点。 |
| APPLYCHOICE | 应用选择 | 可选必选说明：必选参数<br>参数含义：该参数用于指定设置方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Add：加上路由的原有开销值。<br>- Sub：减去路由的原有开销值。<br>- Replace：代替路由的原有开销值。<br>- Inherit：继承路由的原有开销值。<br>默认值：无<br>配置原则：当取值Inherit时，与COSTVALUE互斥，不可同时配置。 |
| COSTVALUE | Cost值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“APPLYCHOICE”配置为“Replace”、“Add” 或 “Sub”时为必选参数。<br>参数含义：该参数用于指定开销值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：<br>- 当APPLYCHOICE参数取值为Inherit时，不可配置该参数，其他情况必须配置该参数。<br>- 当某条链路状况较差或带宽较小时，建议配置的路由开销值偏大，当某条链路状况较好或带宽较大时，建议配置的路由开销值偏小。 |

## 操作的配置对象

- [路由开销值设置（APPLYCOST）](configobject/UDG/20.15.2/APPLYCOST.md)

## 使用实例

路由策略a节点10，修改路由开销值10：

```
MOD APPLYCOST:NODESEQUENCE=10,COSTVALUE=10,POLICYNAME="a", APPLYCHOICE=Replace;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改路由开销值设置（MOD-APPLYCOST）_00441481.md`
