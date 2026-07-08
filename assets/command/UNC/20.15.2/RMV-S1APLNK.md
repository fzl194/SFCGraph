---
id: UNC@20.15.2@MMLCommand@RMV S1APLNK
type: MMLCommand
name: RMV S1APLNK（删除S1AP连接）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: S1APLNK
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1AP链路
status: active
---

# RMV S1APLNK（删除S1AP连接）

## 功能

![](删除S1AP连接(RMV S1APLNK)_26306064.assets/notice_3.0-zh-cn_2.png)

删除链路可能影响正在进行的业务。

**适用网元：MME**

此命令用于删除S1AP链路。

## 注意事项

- 此命令执行后立即生效。
- 此命令在版本升级过程中禁止执行。
- 删除链路可能影响正在进行的业务。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定<br>SPU<br>资源单元名。该参数可以通过<br>[DSP RU](../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：1~63位字符串<br>默认值 ：无<br>配置原则：RU名称、删除时进程类型、进程号必须同时输入或同时不输入。 |
| PROCTYPERMV | 删除时进程类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定S1AP链路的进程类型。<br>取值范围：<br>- “SGP(SGP)”<br>默认值：无<br>配置原则：RU名称、删除时进程类型、进程号必须同时输入或同时不输入。 |
| PROCESSNO | 进程号 | 可选必选说明：可选参数<br>参数含义：待删除链路所在SGP的进程号。通过<br>[**DSP PROCESSLINK**](../../../../../平台服务管理/操作维护/VNFC公共功能管理/操作维护/系统调测/进程管理/查询LINK进程信息(DSP PROCESSLINK)_11295772.md)<br>获取。<br>取值范围： 0~11<br>默认值 ：无<br>配置原则：RU名称、删除时进程类型、进程号必须同时输入或同时不输入。 |
| PLCYRMV | S1AP链路删除策略 | 可选必选说明：必选参数<br>参数含义：指定删除链路的方式。<br>取值范围：<br>- ENODEBID(指定ENODEBID)：通过指定eNodeB删除链路<br>- IPANDPORT(指定IP和PORT)：通过指定IP与端口号删除链路<br>默认值 ：无 |
| MCC | 移动国家码 | 可选必选说明：条件必选参数<br>参数含义：待删除S1AP链路的eNodeB的移动国家码。<br>前提条件：<br>“S1AP链路删除策略”<br>参数需要设置为<br>“ENODEBID(指定ENODEBID)”<br>，参见<br>“S1AP链路删除策略”<br>。<br>取值范围：3位BCD码<br>默认值 ：无 |
| MNC | 移动网号 | 可选必选说明：条件必选参数<br>参数含义：待删除S1AP链路的eNodeB的移动网号。<br>前提条件：<br>“S1AP链路删除策略”<br>参数需要设置为<br>“ENODEBID(指定ENODEBID)”<br>，参见<br>“S1AP链路删除策略”<br>。<br>取值范围：2~3位BCD码<br>默认值 ：无 |
| ENODEBTYPE | eNodeB类型 | 可选必选说明：条件必选参数<br>参数含义：待删除S1AP链路的eNodeB的类型。<br>前提条件：<br>“S1AP链路删除策略”<br>参数需要设置为<br>“ENODEBID(指定ENODEBID)”<br>，参见<br>“S1AP链路删除策略”<br>。<br>取值范围：<br>- HOME_ENB(HOME_ENB)<br>- MACRO_ENB(MACRO_ENB)<br>默认值 ：无 |
| ENODEBID | eNodeB标识 | 可选必选说明：条件必选参数<br>参数含义：待删除S1AP链路的eNodeB的标识。<br>前提条件：<br>“S1AP链路删除策略”<br>参数需要设置为<br>“ENODEBID(指定ENODEBID)”<br>，参见<br>“S1AP链路删除策略”<br>。<br>取值范围：0~268435455<br>默认值 ：无 |
| IPTYPE | IP类型 | 可选必选说明：条件必选参数<br>参数含义：待删除链路的IP地址类型<br>前提条件：<br>“S1AP链路删除策略”<br>参数需要设置为<br>“IPANDPORT(指定IP和PORT)”<br>，参见<br>“S1AP链路删除策略”<br>。<br>取值范围：<br>- IPV4(IPv4)<br>- IPV6(IPv6)<br>默认值 ：无 |
| PEERIPV4ADDR1 | 对端IPv4地址1 | 可选必选说明：条件必选参数<br>参数含义：待删除S1AP链路中eNodeB的第一个IP地址。<br>前提条件：<br>“IP类型”<br>参数需要设置为<br>“IPV4(IPv4)”<br>，参见<br>“IP类型”<br>。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值 ：无 |
| PEERIPV4ADDR2 | 对端IPv4地址2 | 可选必选说明：可选参数<br>参数含义：待删除S1AP链路中eNodeB的第二个IP地址。<br>前提条件：<br>“IP类型”<br>参数需要设置为<br>“IPV4(IPv4)”<br>，参见<br>“IP类型”<br>。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值 ：无 |
| PEERIPV6ADDR1 | 对端IPv6地址1 | 可选必选说明：条件必选参数<br>参数含义：待删除S1AP链路中eNodeB的第一个IP地址。<br>前提条件：<br>“IP类型”<br>参数需要设置为<br>“IPV6(IPv6)”<br>，参见<br>“IP类型”<br>。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值 ：无 |
| PEERIPV6ADDR2 | 对端IPv6地址2 | 可选必选说明：可选参数<br>参数含义：待删除S1AP链路中eNodeB的第二个IP地址。<br>前提条件：<br>“IP类型”<br>参数需要设置为<br>“IPV6(IPv6)”<br>，参见<br>“IP类型”<br>。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值 ：无 |
| PEERPORT | 对端端口号 | 可选必选说明：条件必选参数<br>参数含义：待删除S1AP链路中eNodeB的端口号。<br>前提条件：<br>“S1AP链路删除策略”<br>参数需要设置为<br>“IPANDPORT(指定IP和PORT)”<br>，参见<br>“S1AP链路删除策略”<br>。<br>取值范围：0~65534<br>默认值 ：无 |
| LOCALIPV4ADDR1 | 本端IPv4地址1 | 可选必选说明：可选参数<br>参数含义：待删除S1AP链路中MME侧S1AP本端端点的第一个IP地址。<br>前提条件：<br>“IP类型”<br>参数需要设置为<br>“IPV4(IPv4)”<br>，参见<br>“IP类型”<br>。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值 ：无 |
| LOCALIPV4ADDR2 | 本端IPv4地址2 | 可选必选说明：可选参数<br>参数含义：待删除S1AP链路中MME侧S1AP本端端点的第二个IP地址。<br>前提条件：<br>“IP类型”<br>参数需要设置为<br>“IPV4(IPv4)”<br>，参见<br>“IP类型”<br>。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值 ：无 |
| LOCALIPV6ADDR1 | 本端IPv6地址1 | 可选必选说明：可选参数<br>参数含义：待删除S1AP链路中MME侧S1AP本端端点的第一个IP地址。<br>前提条件：<br>“IP类型”<br>参数需要设置为<br>“IPV6(IPv6)”<br>，参见<br>“IP类型”<br>。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值 ：无 |
| LOCALIPV6ADDR2 | 本端IPv6地址2 | 可选必选说明：可选参数<br>参数含义：待删除S1AP链路中MME侧S1AP本端端点的第二个IP地址。<br>前提条件：<br>“IP类型”<br>参数需要设置为<br>“IPV6(IPv6)”<br>，参见<br>“IP类型”<br>。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值 ：无 |
| LOCALPORT | 本端端口号 | 可选必选说明：可选参数<br>参数含义：待删除S1AP链路中MME侧S1AP本端端点的端口号。<br>前提条件：<br>“S1AP链路删除策略”<br>参数需要设置为<br>“IPANDPORT(指定IP和PORT)”<br>，参见<br>“S1AP链路删除策略”<br>。<br>取值范围：1024~65534<br>默认值 ：无 |

## 操作的配置对象

- [S1AP连接（S1APLNK）](configobject/UNC/20.15.2/S1APLNK.md)

## 使用实例

删除移动国家码为123，移动网号为01，标识为2的home eNodeB的S1AP连接：

RMV S1APLNK: PLCYRMV=ENODEBID, MCC="123", MNC="01", ENODEBTYPE=HOME_ENB, ENODEBID=2;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除S1AP连接(RMV-S1APLNK)_26306064.md`
