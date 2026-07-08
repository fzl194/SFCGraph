---
id: UDG@20.15.2@MMLCommand@ADD OSPFAREA
type: MMLCommand
name: ADD OSPFAREA（创建OSPF区域配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: OSPFAREA
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 8016
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF区域配置
status: active
---

# ADD OSPFAREA（创建OSPF区域配置）

## 功能

该命令用于在OSPF进程下创建区域。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为8016。
- 只有执行ADD OSPF配置了OSPF进程才能使用此命令。
- 如果AREATYPE为NSSA，则必须配置Loopback地址并在OSPF进程中发布出去，否则会造成负载分担不生效，极端情况下会造成业务受损。
- OSPF区域实例数规格默认为单进程50，实际以服务规格文件为准。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPF进程号必须已经存在。请使用LST OSPF命令查看可用的OSPF进程。 |
| AREAID | 区域号 | 可选必选说明：必选参数<br>参数含义：OSPF区域号。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无<br>配置原则：规划的邻居所在的区域必须一致。 |
| DESCRIPTIONTEXT | 区域描述 | 可选必选说明：可选参数<br>参数含义：OSPF区域描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～80。<br>默认值：无 |
| AREATYPE | 区域类型 | 可选必选说明：可选参数<br>参数含义：OSPF区域类型。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- Normal：普通区域。<br>- Stub：Stub区域。<br>- NSSA：NSSA区域。<br>默认值：Normal |
| NSSADEFAULTROUTEADVERTISE | 产生缺省7类LSA到NSSA区域 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AREATYPE”配置为“NSSA”时为可选参数。<br>参数含义：在ABR或者ASBR上配置产生缺省的Type-7 LSA到NSSA区域。当骨干区域存在Full状态的邻居和UP状态的接口，ABR可以产生缺省的Type-7 LSA到NSSA区域。当配置了NSSADEFAULTROUTEADVERTISE参数并且本地路由表中存在其他缺省路由，ASBR可以产生缺省的Type-7 LSA到NSSA区域。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |
| NSSANOIMPORTROUTE | 不引入外部路由 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AREATYPE”配置为“NSSA”时为可选参数。<br>参数含义：不向NSSA区域引入外部路由。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |
| NSSANOSUMMARY | 禁止ABR向NSSA区域内发送Summary LSA | 可选必选说明：条件可选参数<br>前提条件：该参数在“AREATYPE”配置为“NSSA”时为可选参数。<br>参数含义：禁止ABR向NSSA区域内发送Summary LSA。当该参数配置为TRUE时，无论默认路由是否被禁止，都会产生一条默认路由。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：FALSE |
| NSSASETNBIT | 配置N-bit位 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AREATYPE”配置为“NSSA”时为可选参数。<br>参数含义：在DD报文中设置N-bit位的标志。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |
| NSSASUPPRESSFORWARDINGADDRESS | 转换后生成的Type5 LSA的FA配置为0.0.0.0 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AREATYPE”配置为“NSSA”时为可选参数。<br>参数含义：将Type7 LSA通过该NSSA ABR转换后生成的Type5 LSA的FA（Forwarding Address ）设置为0.0.0.0。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |
| NSSATRANSLATORALWAYS | 转换路由器 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AREATYPE”配置为“NSSA”时为可选参数。<br>参数含义：该ABR是否作为转换路由器。通过在ABR上配置NSSATRANSLATORALWAYS参数，可以将某一个ABR指定为转换器。如果需要指定某两个ABR进行负载分担，可以通过配置NSSATRANSLATORALWAYS来指定两个转换器同时工作。如果需要某一个固定的转换器，防止由于转换器变动引起的LSA重新泛洪，可以预先使用此参数指定。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |
| NSSATRANSLATORINTERVAL | 失效时间（s） | 可选必选说明：条件可选参数<br>前提条件：该参数在“AREATYPE”配置为“NSSA”时为可选参数。<br>参数含义：指定转换路由器的失效时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～120，单位是秒。<br>默认值：40<br>配置原则：如果不配置此参数，则实际取值是40秒。 |
| NSSAZEROADDRESSFORWARDING | 将生成的Type7 LSA的FA置为0.0.0.0 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AREATYPE”配置为“NSSA”时为可选参数。<br>参数含义：在NSSA区域的ABR上引入外部路由时，将生成的NSSA LSA的FA置为0.0.0.0。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |
| STUBNOSUMMARY | 禁止ABR向Stub区域内发送Summary LSA | 可选必选说明：条件可选参数<br>前提条件：该参数在“AREATYPE”配置为“Stub”时为可选参数。<br>参数含义：禁止ABR向Stub区域内发送Summary LSA。要想使一个区域为stub区域，则该区域内的所有路由器都要配置AREATYPE为Stub。DEFAULTCOST参数配置只有在ABR上配置才起作用，用于指定ABR发送到Stub区域的Summary类型的缺省路由开销。此外，在ABR上，还可以通过配置STUBNOSUMMARY来禁止Type-3 LSA进入该ABR连接的Stub区域。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |
| DEFAULTCOST | 发送到Stub或NSSA区域的Type3缺省路由的开销 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AREATYPE”配置为“Stub” 或 “NSSA”时为可选参数。<br>参数含义：OSPF发送到Stub或NSSA区域的Type 3缺省路由的开销。只有配置在连接到Stub或NSSA区域的边界路由器（ABR）上时才生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～16777214。<br>默认值：1<br>配置原则：如果不配置此参数，则实际取值是1。 |
| LDPSYNCENABLE | 使能LDP和OSPF同步功能 | 可选必选说明：可选参数<br>参数含义：使能LDP和OSPF同步功能。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE<br>配置原则：<br>- 私网OSPF进程下不支持LDP和OSPF联动功能。<br>- 如果不配置此参数，则实际取值是FALSE。 |
| MAXCOSTFLAG | 保持最大开销值标志 | 可选必选说明：可选参数<br>参数含义：是否配置本地设备通告链路最大开销值的时间。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：FALSE |
| MAXCOSTINTVL | 保持最大开销值时间间隔（s） | 可选必选说明：条件必选参数<br>前提条件：该参数在“MAXCOSTFLAG”配置为“TRUE”时为必选参数。<br>参数含义：指定OSPF在本地设备的中保持通告最大开销值的时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |

## 操作的配置对象

- [OSPF区域配置（OSPFAREA）](configobject/UDG/20.15.2/OSPFAREA.md)

## 关联任务

- [[UDG@20.15.2@Task@0-00075]]

## 使用实例

配置OSPF进程下1新增区域0.0.0.0：

```
ADD OSPFAREA: PROCID=1, AREAID="0.0.0.0";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/创建OSPF区域配置（ADD-OSPFAREA）_50120650.md`
