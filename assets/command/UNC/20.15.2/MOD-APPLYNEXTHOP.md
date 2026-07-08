---
id: UNC@20.15.2@MMLCommand@MOD APPLYNEXTHOP
type: MMLCommand
name: MOD APPLYNEXTHOP（修改下一跳设置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: APPLYNEXTHOP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 应用下一跳
status: active
---

# MOD APPLYNEXTHOP（修改下一跳设置）

## 功能

该命令用于修改配置路由下一跳。

## 注意事项

- 该命令执行后立即生效。
- 配置该命令前，必须已经配置了指定路由策略的名字以及该策略下的节点。
- 当参数ISPEERADDRESS配置为TRUE时，不能配置参数NEXTHOP、NEXTHOPTYPE和IFNAME。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：不支持输入空格，必须存在该路由策略。 |
| NODESEQUENCE | 路由策略节点号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：必须存在该路由策略节点。 |
| ISPEERADDRESS | 是否是对等体IP地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否是对等体IP地址。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：否。<br>- TRUE：是。<br>默认值：无<br>配置原则：无 |
| NEXTHOPTYPE | 下一跳类型 | 可选必选说明：可选参数<br>前提条件：该参数在“ISPEERADDRESS”配置为“FALSE”时为可选参数。<br>参数含义：该参数用于指定应用下一跳的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipaddress：下一跳类型为IP地址。<br>- interface：下一跳类型为接口名称。<br>默认值：无<br>配置原则：无 |
| NEXTHOP | 下一跳地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ISPEERADDRESS”配置为“FALSE”且“NEXTHOPTYPE”不为“interface”时为必选参数。<br>参数含义：该参数用于指定下一跳IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IFNAME | 接口名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“NEXTHOPTYPE”配置为“interface”时为必选参数。<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APPLYNEXTHOP]] · 下一跳设置（APPLYNEXTHOP）

## 使用实例

路由策略a节点10，修改设置下一跳为10.1.1.1：

```
MOD APPLYNEXTHOP:NODESEQUENCE=10, NEXTHOP="10.1.1.1",POLICYNAME="a",ISPEERADDRESS=FALSE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-APPLYNEXTHOP.md`
