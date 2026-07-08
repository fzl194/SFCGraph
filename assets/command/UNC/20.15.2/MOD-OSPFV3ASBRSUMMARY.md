---
id: UNC@20.15.2@MMLCommand@MOD OSPFV3ASBRSUMMARY
type: MMLCommand
name: MOD OSPFV3ASBRSUMMARY（修改OSPFv3引入路由聚合配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: OSPFV3ASBRSUMMARY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3引入路由聚合配置
status: active
---

# MOD OSPFV3ASBRSUMMARY（修改OSPFv3引入路由聚合配置）

## 功能

该命令用于修改自治系统边界路由器ASBR对OSPFv3引入的路由进行路由聚合配置。

## 注意事项

- 该命令执行后立即生效。
- 只有在配置了OSPFv3进程后才能使用此命令。
- 当有大量聚合路由时，可以配置DISTRDELAYINTV 参数设置延迟发布聚合路由的时间，使每次发布的聚合路由信息中包含更多的有效路由，避免网络振荡而出现路由信息不准确的现象。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：必选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPFv3进程必须已经存在，并且已经存在OSPFV3ASBRSUMMARY时才可修改。 |
| TOPOID | 拓扑标识 | 可选必选说明：必选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：目前只支持默认拓扑0。 |
| IPADDRESS | IPv6地址 | 可选必选说明：必选参数<br>参数含义：IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| IPV6MASKLEN | IPv6前缀长度 | 可选必选说明：必选参数<br>参数含义：IPv6前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～128。<br>默认值：无 |
| CONFIGCOST | 使能聚合路由的开销值 | 可选必选说明：可选参数<br>参数含义：使能聚合路由的开销值。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无<br>配置原则：如果不配置此参数，则实际取值为FALSE。 |
| COST | 聚合路由的开销 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONFIGCOST”配置为“TRUE”时为必选参数。<br>参数含义：当此参数缺省时，对于Type1类外部路由，取所有被聚合路由中的最大开销值作为聚合路由的开销；对于Type2类外部路由，则取所有被聚合路由中的最大开销值再加上1作为聚合路由的开销。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～16777214。<br>默认值：无<br>配置原则：<br>- 对于Type-1类型的外部路由，聚合路由的开销值是所有被聚合路由中的最大开销值。<br>- 对于Type-2类型的外部路由，聚合路由的开销值是所有被聚合路由中的最大开销值再加上1。 |
| CONFIGDISTRDELAYINTV | 使能延迟发布聚合路由 | 可选必选说明：可选参数<br>参数含义：使能延迟发布聚合路由。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无<br>配置原则：如果不配置此参数，则实际取值为FALSE。 |
| DISTRDELAYINTV | 延迟发布聚合路由的时间（s） | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONFIGDISTRDELAYINTV”配置为“TRUE”时为必选参数。<br>参数含义：设置延迟发布聚合路由的时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535，单位是秒。<br>默认值：无 |
| NOTADVFLAG | 不发布路由 | 可选必选说明：可选参数<br>参数含义：用来指定是否发布聚合路由，默认值是发布聚合路由。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DoNotAdvertise：不发布。<br>- Advertise：发布。<br>默认值：无 |
| CONFIGTAG | 使能聚合路由的标记 | 可选必选说明：可选参数<br>参数含义：使能聚合路由的标记。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无<br>配置原则：如果不配置此参数，则实际取值为FALSE。 |
| TAG | 路由标签 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONFIGTAG”配置为“TRUE”时为必选参数。<br>参数含义：路由标签，用于通过路由策略控制路由发布。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：如果不配置此参数，则实际取值为1。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OSPFV3ASBRSUMMARY]] · OSPFv3引入路由聚合配置（OSPFV3ASBRSUMMARY）

## 使用实例

修改OSPFv3进程1下引入的2001:db8::路由聚合的Cost值为200：

```
MOD OSPFV3ASBRSUMMARY:PROCID=1,TOPOID=0,IPADDRESS="2001:db8::",IPV6MASKLEN=64,CONFIGCOST=TRUE,COST=200,NOTADVFLAG=Advertise;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-OSPFV3ASBRSUMMARY.md`
