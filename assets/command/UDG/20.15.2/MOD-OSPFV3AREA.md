---
id: UDG@20.15.2@MMLCommand@MOD OSPFV3AREA
type: MMLCommand
name: MOD OSPFV3AREA（修改OSPFv3区域配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: OSPFV3AREA
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3区域配置
status: active
---

# MOD OSPFV3AREA（修改OSPFv3区域配置）

## 功能

该命令用于修改OSPFv3进程下区域配置。

![](修改OSPFv3区域配置（MOD OSPFV3AREA）_00440849.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，如果修改区域类型或者修改IPsec SA名称可能会使此区域的OSPFv3邻接关系中断。

## 注意事项

- 该命令执行后立即生效。
- 修改参数AREATYPE或者SANAME可能会使此区域的OSPFv3邻接关系中断。
- 只有配置了OSPFv3进程和OSPFv3区域后才能使用此命令。
- 如果AREATYPE为NSSA，则必须配置Loopback地址并在OSPFv3进程中发布出去，否则会造成负载分担不生效，极端情况下会造成业务受损。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：必选参数<br>参数含义：OSPFv3进程号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPFv3进程必须已经存在。请使用LST OSPFV3命令查看可用的OSPFv3进程。 |
| AREAID | OSPFv3区域标识 | 可选必选说明：必选参数<br>参数含义：OSPFv3区域标识。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| DESCRIPTIONTEXT | OSPFv3区域描述 | 可选必选说明：可选参数<br>参数含义：OSPFv3区域描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～80。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| AREATYPE | OSPFv3区域类型 | 可选必选说明：可选参数<br>参数含义：OSPFv3区域类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Normal：普通区域。<br>- Stub：Stub区域。<br>- NSSA：NSSA区域。<br>默认值：无 |
| STUBNOSUMMARY | 禁止ABR向Stub区域内发送Summary LSA | 可选必选说明：条件可选参数<br>前提条件：该参数在“AREATYPE”配置为“Stub”时为可选参数。<br>参数含义：禁止ABR向Stub区域内发送Summary LSA。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| DEFAULTCOST | 发送到Stub或NSSA区域的Type3缺省路由的开销 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AREATYPE”配置为“Stub” 或 “NSSA”时为可选参数。<br>参数含义：OSPF发送到Stub或NSSA区域的Type 3缺省路由的开销。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～16777214。<br>默认值：无<br>配置原则：如果不配置此参数时，则实际取值是1。 |
| SANAME | IPsec SA名称 | 可选必选说明：可选参数<br>参数含义：IPsec SA的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- IPsec SA必须已经存在。<br>- 不能直接修改，需要先删除再配置。<br>- 不能和认证同时配置。 |
| NSSADEFAULTROUTEADVERTISE | 产生缺省7类LSA到NSSA区域 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AREATYPE”配置为“NSSA”时为可选参数。<br>参数含义：在ABR或者ASBR上配置产生缺省的Type-7 LSA到NSSA区域。当骨干区域存在Full状态的邻居和UP状态的接口，ABR可以产生缺省的Type-7 LSA到NSSA区域。当配置了NSSADEFAULTROUTEADVERTISE参数并且本地路由表中存在其他缺省路由，ASBR可以产生缺省的Type-7 LSA到NSSA区域。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| NSSADEFAULTCOSTCFG | 指定缺省开销值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“NSSADEFAULTROUTEADVERTISE”配置为“TRUE”时为可选参数。<br>参数含义：指定缺省路由的开销值。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| NSSADEFAULTCOST | 缺省开销值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“NSSADEFAULTCOSTCFG”配置为“TRUE”时为必选参数。<br>参数含义：缺省开销值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～16777214。<br>默认值：无<br>配置原则：如果不配置此参数，则实际取值是1。 |
| NSSADEFAULTTAGCFG | 指定缺省路由的tag值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“NSSADEFAULTROUTEADVERTISE”配置为“TRUE”时为可选参数。<br>参数含义：指定缺省路由的tag值。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| NSSADEFAULTTAG | 缺省路由的tag值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“NSSADEFAULTTAGCFG”配置为“TRUE”时为必选参数。<br>参数含义：缺省路由的tag值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：如果不配置此参数，则实际取值是0。 |
| NSSADEFAULTTYPECFG | 指定缺省路由的类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“NSSADEFAULTROUTEADVERTISE”配置为“TRUE”时为可选参数。<br>参数含义：指定该NSSA默认LSA的类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| NSSADEFAULTTYPE | 缺省路由类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“NSSADEFAULTTYPECFG”配置为“TRUE”时为必选参数。<br>参数含义：缺省路由类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- Type1：外部路由类型1。<br>- Type2：外部路由类型2。<br>默认值：无<br>配置原则：如果不配置此参数，则实际取值是Type2。 |
| NSSANOIMPORTROUTE | 不引入外部路由 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AREATYPE”配置为“NSSA”时为可选参数。<br>参数含义：不向NSSA区域引入外部路由。当ASBR同时还是ABR时，通过配置NSSANOIMPORTROUTE参数使OSPFv3通过ADD OSPFV3IMPORTROUTE命令引入的外部路由不被通告到NSSA区域。<br>数据来源：全网规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| NSSANOSUMMARY | 禁止ABR向NSSA区域内发送Summary LSA | 可选必选说明：条件可选参数<br>前提条件：该参数在“AREATYPE”配置为“NSSA”时为可选参数。<br>参数含义：禁止ABR向NSSA区域内发送Summary LSA。当该参数配置为TRUE时，无论默认路由是否被禁止，都会产生一条默认路由。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| NSSASETNBIT | 在DD报文中配置N-bit位 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AREATYPE”配置为“NSSA”时为可选参数。<br>参数含义：在DD报文中设置N-bit位的标志。<br>数据来源：全网规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| NSSATRANSLATORALWAYS | 指定为转换路由器 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AREATYPE”配置为“NSSA”时为可选参数。<br>参数含义：该ABR是否作为转换路由器。通过在ABR上配置NSSATRANSLATORALWAYS参数，可以将某一个ABR指定为转换器。如果需要指定某两个ABR进行负载分担，可以通过配置NSSATRANSLATORALWAYS来指定两个转换器同时工作。如果需要某一个固定的转换器，防止由于转换器变动引起的LSA重新泛洪，可以预先使用此参数指定。<br>数据来源：全网规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| NSSATRANSLATORINTERVAL | 转换路由器的失效时间（s） | 可选必选说明：条件可选参数<br>前提条件：该参数在“AREATYPE”配置为“NSSA”时为可选参数。<br>参数含义：指定转换路由器的失效时间。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～120，单位是秒。<br>默认值：无<br>配置原则：如果不配置此参数，则实际取值是40秒。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFV3AREA]] · OSPFv3区域配置（OSPFV3AREA）

## 使用实例

修改OSPFv3进程下1区域0.0.0.0的描述：

```
MOD OSPFV3AREA: PROCID=1, AREAID="0.0.0.0", DESCRIPTIONTEXT="HUAWEI";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改OSPFv3区域配置（MOD-OSPFV3AREA）_00440849.md`
