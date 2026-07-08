---
id: UDG@20.15.2@MMLCommand@MOD OSPFASBRSUMMARY
type: MMLCommand
name: MOD OSPFASBRSUMMARY（修改引入路由聚合配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: OSPFASBRSUMMARY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF引入路由聚合配置
status: active
---

# MOD OSPFASBRSUMMARY（修改引入路由聚合配置）

## 功能

该命令用于修改自治系统边界路由器ASBR对OSPF引入的路由进行路由聚合配置。

## 注意事项

- 该命令执行后立即生效。
- 只有在配置了OSPF进程后才能使用此命令。
- 当有大量聚合路由时，可以配置DISTRDELAYINTV 参数设置延迟发布聚合路由的时间，使每次发布的聚合路由信息中包含更多的有效路由，避免网络振荡而出现路由信息不准确的现象。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPF进程必须已经存在。请使用LST OSPF命令查看可用的OSPF进程。 |
| TOPOID | 拓扑标识 | 可选必选说明：必选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：目前只支持默认拓扑0。 |
| IPADDRESS | IP地址 | 可选必选说明：必选参数<br>参数含义：IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| ADDRESSMASK | 地址掩码 | 可选必选说明：必选参数<br>参数含义：地址掩码。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| CONFIGCOST | 使能聚合路由的开销值 | 可选必选说明：可选参数<br>参数含义：使能聚合路由的开销值。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| COST | 聚合路由的开销 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONFIGCOST”配置为“TRUE”时为必选参数。<br>参数含义：设置聚合路由的开销。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～16777214。<br>默认值：无<br>配置原则：<br>- 对于Type-1类型的外部路由，聚合路由的开销值是所有被聚合路由中的最大开销值。<br>- 对于Type-2类型的外部路由，聚合路由的开销值是所有被聚合路由中的最大开销值再加上1。 |
| CONFIGDISTRDELAYINTV | 使能延迟发布聚合路由 | 可选必选说明：可选参数<br>参数含义：使能延迟发布聚合路由。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| DISTRDELAYINTV | 延迟发布聚合路由的时间（s） | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONFIGDISTRDELAYINTV”配置为“TRUE”时为必选参数。<br>参数含义：设置延迟发布聚合路由的时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535，单位是秒。<br>默认值：无 |
| NOTADVFLAG | 不发布路由 | 可选必选说明：可选参数<br>参数含义：用来指定是否发布聚合路由，默认值是发布聚合路由。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DoNotAdvertise：不发布。<br>- Advertise：发布。<br>默认值：无 |
| CONFIGTAG | 使能聚合路由的标记 | 可选必选说明：可选参数<br>参数含义：使能聚合路由的标记。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| TAG | 路由标签 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONFIGTAG”配置为“TRUE”时为必选参数。<br>参数含义：路由标签，用于通过路由策略控制路由发布。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：如果不配置此参数，则实际取值为1。 |
| BLACKHOLECFG | 生成路由黑洞 | 可选必选说明：可选参数<br>参数含义：生成路由黑洞。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFASBRSUMMARY]] · 引入路由聚合配置（OSPFASBRSUMMARY）

## 使用实例

修改OSPF进程1下引入的10.1.0.0路由聚合的Cost值为200：

```
MOD OSPFASBRSUMMARY:PROCID=1,TOPOID=0,IPADDRESS="10.1.0.0",ADDRESSMASK="255.255.0.0",CONFIGCOST=TRUE,COST=200,NOTADVFLAG=DoNotAdvertise;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-OSPFASBRSUMMARY.md`
