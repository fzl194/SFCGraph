---
id: UDG@20.15.2@MMLCommand@ADD OSPFIMPORTROUTE
type: MMLCommand
name: ADD OSPFIMPORTROUTE（创建OSPF引入路由配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: OSPFIMPORTROUTE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 8000
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- 引入外部路由配置
status: active
---

# ADD OSPFIMPORTROUTE（创建OSPF引入路由配置）

## 功能

该命令用来将外部路由引入到OSPF域中，并在OSPF域中发布引入的路由信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为8000。
- 只有执行ADD OSPF配置了OSPF进程才能使用此命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：<br>- 设备支持OSPF特性。<br>- OSPF进程必须已经存在。<br>- 请使用LST OSPF命令查看可用的OSPF进程。 |
| TOPOID | 拓扑标识 | 可选必选说明：可选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：0<br>配置原则：目前只支持默认拓扑0。 |
| PROTOCOL | 协议分类 | 可选必选说明：必选参数<br>参数含义：用于指定OSPF引入外部路由的路由类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Direct：直连路由。<br>- OSPF：OSPF路由。<br>- Static：静态路由。<br>- BGP：BGP路由。<br>- wlr：无线路由。<br>默认值：无 |
| PROTOCOLPROCID | 协议进程号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PROTOCOL”配置为“OSPF”时为可选参数。<br>参数含义：引入路由协议的进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：1 |
| IMPTCOSTCFG | 引入路由开销值配置 | 可选必选说明：可选参数<br>参数含义：标志是否设置路径开销值。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：FALSE |
| IMPTTAGCFG | 引入路由标签配置 | 可选必选说明：可选参数<br>参数含义：标志是否设置类型的值。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：FALSE |
| IMPTTYPECFG | 引入路由类型配置 | 可选必选说明：可选参数<br>参数含义：标志是否置位外部LSA的标记。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：FALSE |
| COST | 路径Cost值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IMPTCOSTCFG”配置为“TRUE”时为必选参数。<br>参数含义：该参数用于指定自治系统外部路径的开销。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～16777214。<br>默认值：无 |
| TAG | 标签 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IMPTTAGCFG”配置为“TRUE”时为必选参数。<br>参数含义：外部LSA中的标记。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| TYPE | 引入路由类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IMPTTYPECFG”配置为“TRUE”时为必选参数。<br>参数含义：外部LSA的度量类型。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～2。<br>默认值：无 |
| ROUPOLINAME | 路由策略名称 | 可选必选说明：可选参数<br>参数含义：路由策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |
| PERMITIBGPCFG | 允许BGP配置 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PROTOCOL”配置为“BGP”时为可选参数。<br>参数含义：使能引入IBGP路由。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |

## 操作的配置对象

- [OSPF引入路由配置（OSPFIMPORTROUTE）](configobject/UDG/20.15.2/OSPFIMPORTROUTE.md)

## 关联任务

- [[UDG@20.15.2@Task@0-00077]]

## 使用实例

在OSPF进程下1下引入OSPF进程2的路由：

```
ADD OSPFIMPORTROUTE:PROCID=1,TOPOID=0,PROTOCOL=OSPF,PROTOCOLPROCID=2;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/创建OSPF引入路由配置（ADD-OSPFIMPORTROUTE）_00601057.md`
