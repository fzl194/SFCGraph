---
id: UDG@20.15.2@MMLCommand@MOD OSPFFRR
type: MMLCommand
name: MOD OSPFFRR（修改OSPF IP FRR配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: OSPFFRR
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF的FRR配置
status: active
---

# MOD OSPFFRR（修改OSPF IP FRR配置）

## 功能

该命令用来修改OSPF IP FRR（快速重路由）配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| ISLFAENABLE | LFA是否使能 | 可选必选说明：可选参数<br>参数含义：LFA是否使能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无<br>配置原则：Loop Free Alternate（LFA）是实现IP FRR的一种方式，使能此参数后，OSPF IP FRR功能才会生效，生成无环备份路由。 |
| NODEPROTECT | 节点保护优先级 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ISLFAENABLE”配置为“TRUE”时为可选参数。<br>参数含义：该参数表示备份路径节点保护优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：无<br>配置原则：<br>- LDP联动最大开销路径优先级默认值为10。<br>- LDP联动最大开销路径和节点保护优先级及最小开销路径优先级，三者互不冲突。 |
| LOWESTCOST | 最小开销路径优先级 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ISLFAENABLE”配置为“TRUE”时为可选参数。<br>参数含义：该参数表示备份路径最小开销路径优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：无<br>配置原则：<br>- LDP联动最大开销路径优先级默认值为10。<br>- LDP联动最大开销路径和节点保护优先级及最小开销路径优先级，三者互不冲突。 |
| POLICYTYPE | 路由策略类型 | 可选必选说明：可选参数<br>参数含义：该参数用来指定路由策略的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- none：无策略。<br>- route_policy：路由策略。<br>默认值：无 |
| POLICYNAME | 路由策略名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“POLICYTYPE”配置为“route_policy”时为必选参数。<br>参数含义：该参数用于指定一个路由策略的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |

## 操作的配置对象

- [OSPF IP FRR配置（OSPFFRR）](configobject/UDG/20.15.2/OSPFFRR.md)

## 使用实例

修改OSPF进程号为1的IP FRR（快速重路由）配置，去使能LFA：

```
MOD OSPFFRR: PROCID=1, ISLFAENABLE=FALSE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改OSPF-IP-FRR配置（MOD-OSPFFRR）_49960914.md`
