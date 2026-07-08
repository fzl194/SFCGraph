---
id: UNC@20.15.2@MMLCommand@RMV APPLYCOST
type: MMLCommand
name: RMV APPLYCOST（删除设置路由开销值）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV APPLYCOST（删除设置路由开销值）

## 功能

该命令用于删除匹配路由开销值。

## 注意事项

- 该命令执行后立即生效。
- 配置该命令前，必须已经配置了指定路由策略的名字以及该策略下的节点。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |
| NODESEQUENCE | 路由策略节点号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| APPLYCHOICE | 应用选择 | 可选必选说明：必选参数<br>参数含义：该参数用于指定设置方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Add：加上路由的原有开销值。<br>- Sub：减去路由的原有开销值。<br>- Replace：代替路由的原有开销值。<br>- Inherit：继承路由的原有开销值。<br>默认值：无 |
| COSTVALUE | Cost值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“APPLYCHOICE”配置为“Replace”、“Add” 或 “Sub”时为必选参数。<br>参数含义：该参数用于指定开销值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APPLYCOST]] · 路由开销值设置（APPLYCOST）

## 使用实例

路由策略a节点10，取消设置路由开销：

```
RMV APPLYCOST:NODESEQUENCE=10,COSTVALUE=10,POLICYNAME="a", APPLYCHOICE=Replace;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-APPLYCOST.md`
