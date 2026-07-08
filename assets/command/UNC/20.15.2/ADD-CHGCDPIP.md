---
id: UNC@20.15.2@MMLCommand@ADD CHGCDPIP
type: MMLCommand
name: ADD CHGCDPIP（增加计费相关的IP配置参数）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CHGCDPIP
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 256
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- CDPIP 配置
status: active
---

# ADD CHGCDPIP（增加计费相关的IP配置参数）

## 功能

**适用网元：SGSN**

该命令用于对资源池内所有CDP进程配IP地址和端口号的组合，系统从该资源池中为每个CDP进程分配一个IP地址与端口号，作为向CG发送话单时的本端IP地址、端口号。

## 注意事项

- 一个CDP进程分配一个IP与端口号的组合，IP与端口号的组合个数必须大于等于系统中的CDP进程个数，否则会导致部分CDP进程无法获取到IP与端口号的组合，从而无法用于话单发送。
- 如果UNCGa口配置IP地址时，配置的本端端口数必须大于等于环境的SPU数量。
- 在和不支持单IP多端口的CG对接时，配置记录数需与SPU数量相等，且只能配置一个端口号，即配置相同的“PORTBGN”和“PORTEND”。
- 该命令执行后立即生效。
- 本表最大记录数为256个，IPV4和IPV6各配置128个。
- 该命令在版本升级过程中禁止执行。
- IP地址和vpn名称必须在SERVICEIP表中已经配置，可以用[**LST SERVICEIP**](../../控制面管理/业务IP管理/业务IP/查询业务IP(LST SERVICEIP)_72226047.md)查询。
- 端口号和IP的组合不能超过1200个。
- 如果配置端口号包含3386，则配置的IP地址不能与GTPCLE和GTPULE的IP地址重复，可以用[**LST GTPCLE**](../../控制面管理/GTP-C接口管理/Gtpc本端实体管理/查询GTP-C本地实体(LST GTPCLE)_72345567.md)，[**LST GTPULE**](../../控制面管理/GTP-U接口管理/Gtpu本端实体管理/查询GTP-U本地实体(LST GTPULE)_26305792.md)查询。
- 整系统只能配置一条拨测CDP端点为YES的记录，建议拨测CDP端点为YES的记录只配置一个端口号，既能够支撑拨测的计费业务，又节省端口资源。
- 拨测CDP端点为YES的配置只能用于灰度升级的拨测功能，非拨测状态下将不会被使用。
- 灰度升级期间不允许新增本配置，因此应该在灰度升级之前提前配置拨测CDP端点为YES的记录供拨测使用。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPT | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP地址类型。<br>数据来源：整网规划<br>取值范围：<br>- “IPv4(IPv4地址)”<br>- “IPv6(IPv6地址)”<br>默认值： 无 |
| IPV4ADDR | IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定CDP的IPv4地址。<br>前提条件：该参数在<br>“IPT”<br>设置为<br>“IPv4(IPv4地址)”<br>时有效。<br>数据来源：整网规划<br>取值范围：0.0.0.1～255.255.255.254<br>默认值：无<br>配置原则：<br>- IPv4地址不能为0.0.0.0、255.255.255.255和0.x.y.z。<br>- IPv4地址不能为组播地址（如：224.x.y.z）和环回地址（如：127.x.y.z）。<br>- IPv4地址必须是A、B或者C类地址。 |
| IPV6ADDR | IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定CDP的IPv6地址。<br>前提条件：该参数在<br>“IPT”<br>设置为<br>“IPv6(IPv6地址)”<br>时有效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）和组播地址（FF00::/8）。 |
| VPNNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN名称。<br>数据来源：整网规划<br>取值范围：1～31位字符串<br>默认值：无 |
| PORTBGN | 起始端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定起始端口号。<br>数据来源：整网规划<br>取值范围：1024～65534<br>默认值：1024<br>配置原则：端口号不可使用下述知名端口：2123(GTPCv1)，2152(GTPUv1)，3784(BFD)，3785(BFD)，4784(BFD)，4500(IKEv2)。 |
| PORTEND | 结束端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定结束端口号。<br>数据来源：整网规划<br>取值范围：1024～65534<br>默认值：<br>“PORTBGN”<br>+ 127<br>配置原则：端口号不可使用下述知名端口：2123(GTPCv1)，2152(GTPUv1)，3784(BFD)，3785(BFD)，4784(BFD)，4500(IKEv2)。 |
| ISFORDIALTST | 是否为拨测CDP IP端点 | 可选必选说明：可选参数<br>参数含义：本参数用于指示当前配置记录的CDP IP端点是否用于灰度升级拨测用途。拨测CDP IP端点只在灰度升级过程的拨测状态下，被绑定到新版本USN_VNFC供拨测用户的计费业务使用，在系统升级完成拨测完成后，端点会被回收，供下一次灰度升级的拨测使用。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NO：否。<br>- YES：是。<br>默认值：NO |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGCDPIP]] · 计费相关的IP配置参数（CHGCDPIP）

## 使用实例

增加CDP IP地址，IP地址类型为IPv4地址，IP地址为172.22.5.50，起始端口号3699，结束端口号3700，不是拨测CDP IP端点：

ADD CHGCDPIP: IPT=IPv4, IPV4ADDR="172.22.5.50",PORTBGN=3699, PORTEND=3700, VPNNAME="_abc_", ISFORDIALTST=NO;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-CHGCDPIP.md`
