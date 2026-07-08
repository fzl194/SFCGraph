---
id: UDG@20.15.2@MMLCommand@MOD OSPFV3IMPORTROUTE
type: MMLCommand
name: MOD OSPFV3IMPORTROUTE（修改OSPFv3引入路由配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: OSPFV3IMPORTROUTE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3引入路由配置
status: active
---

# MOD OSPFV3IMPORTROUTE（修改OSPFv3引入路由配置）

## 功能

该命令用来修改引入到OSPFv3域中的外部路由的配置，并在OSPFv3域中发布引入的路由信息。

## 注意事项

- 该命令执行后立即生效。
- 只有配置了OSPFv3进程和设置了外部引入路由后才能使用该命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：必选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPFv3进程必须已经存在。请使用LST OSPFV3命令查看可用的OSPFv3进程。 |
| TOPOID | 拓扑标识 | 可选必选说明：必选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：目前只支持默认拓扑0。 |
| PROTOCOL | 协议号 | 可选必选说明：必选参数<br>参数含义：协议号。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- direct：直连路由。<br>- static：静态路由。<br>- bgp：BGP协议。<br>- ospfv3：OSPFv3协议。<br>- wlr：无线路由。<br>默认值：无 |
| PROTOCOLPROCID | 协议进程号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PROTOCOL”配置为“ospfv3”时为可选参数。<br>参数含义：协议进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| IMPTCOSTCFG | 引入路由开销值配置 | 可选必选说明：可选参数<br>参数含义：引入路由Cost使能标志。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| IMPTTAGCFG | 引入路由标签配置 | 可选必选说明：可选参数<br>参数含义：引入路由Tag使能标志。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| IMPTTYPECFG | 引入路由类型配置 | 可选必选说明：可选参数<br>参数含义：引入路由Type使能标志。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| COST | 路径Cost值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IMPTCOSTCFG”配置为“TRUE”时为必选参数。<br>参数含义：路径Cost值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～16777214。<br>默认值：无 |
| TAG | 标签 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IMPTTAGCFG”配置为“TRUE”时为必选参数。<br>参数含义：标签。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| TYPE | 引入路由类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IMPTTYPECFG”配置为“TRUE”时为必选参数。<br>参数含义：引入路由类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Type1：外部路由类型1。<br>- Type2：外部路由类型2。<br>默认值：无 |
| ROUPOLINAME | 路由策略名称 | 可选必选说明：可选参数<br>参数含义：路由策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| PERMITIBGPCFG | 允许BGP配置 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PROTOCOL”配置为“bgp”时为可选参数。<br>参数含义：允许BGP配置。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| INHERITCOSTCFG | 指定引入路由时继承原路由的开销值 | 可选必选说明：可选参数<br>参数含义：指定引入路由时继承原路由的开销值。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：参数INHERITCOSTCFG不能与IMPTCOSTCFG同时配置为TRUE。 |

## 操作的配置对象

- [OSPFv3引入路由配置（OSPFV3IMPORTROUTE）](configobject/UDG/20.15.2/OSPFV3IMPORTROUTE.md)

## 使用实例

将OSPFv3进程1下引入OSPFv3进程2的路由的开销设为2：

```
MOD OSPFV3IMPORTROUTE: PROCID=1, TOPOID=0, IMPTCOSTCFG=TRUE, IMPTTAGCFG=FALSE, IMPTTYPECFG=FALSE, PROTOCOL=ospfv3, PROTOCOLPROCID=2, COST=2;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改OSPFv3引入路由配置（MOD-OSPFV3IMPORTROUTE）_00440581.md`
