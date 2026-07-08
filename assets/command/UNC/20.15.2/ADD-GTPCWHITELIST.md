---
id: UNC@20.15.2@MMLCommand@ADD GTPCWHITELIST
type: MMLCommand
name: ADD GTPCWHITELIST（增加GTP-C路径白名单）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: GTPCWHITELIST
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
max_records: 1000
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GTP-C协议管理
- GTP-C路径白名单
status: active
---

# ADD GTPCWHITELIST（增加GTP-C路径白名单）

## 功能

**适用网元：MME**

本命令用于增加GTP-C路径白名单，用于控制GTP-C路径的本端IP地址选择。

应用场景：Sv接口与SGs接口共用信令网络，但信令网络只提供平行路径的互通，不支持交叉路径的互通。比如，MSC提供IP地址MSC_IP_1、MSC_IP_2， UNC 提供IP地址USN_IP_A、USN_IP_B，平行路径指{MSC_IP_1，USN_IP_A}，{MSC_IP_2，USN_IP_B}，交叉路径指{MSC_IP_1，USN_IP_B}，{MSC_IP_2，USN_IP_A}。

Sv接口为GTP协议的接口，要求组网上DNS解析的IP地址全互联。为了解决这种矛盾，本命令提供Sv接口互通路径的配置。如果对端IP地址落入本命令的配置记录中， UNC 只能选择GTP-C路径白名单中指定的本端IP地址；如果对端IP地址不在本命令的配置记录中， UNC 在Sv接口的本端IP地址中进行轮选。

## 注意事项

- 此命令最大记录数为1000。
- 本命令只对Sv接口生效。
- 本命令执行后对新的SRVCC流程生效。
- 本命令的使用优先级高于[**ADD GTPCINTFATTR**](../../GTP-C接口类型属性/增加GTP-C IP地址接口属性(ADD GTPCINTFATTR)_72225579.md)，即本命令指定的本端IP地址不受[**ADD GTPCINTFATTR**](../../GTP-C接口类型属性/增加GTP-C IP地址接口属性(ADD GTPCINTFATTR)_72225579.md)的规则约束，并且优先使用本命令的配置结果。
- 本命令配置的记录唯一性的关键字是{接口类型、本端IP、对端IP}，不允许出现重复记录。
- 本命令配置的本端IP地址必须在GTPCLE表中已经配置，可以用[**LST GTPCLE**](../../Gtpc本端实体管理/查询GTP-C本地实体(LST GTPCLE)_72345567.md)命令查询本端IP地址。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTFTP | 接口类型 | 可选必选说明：必选参数<br>参数含义：本参数用于指定对端IP地址所属的接口类型。<br>数据来源：全网规划<br>取值范围：<br>- “Sv(Sv)”<br>默认值：无 |
| IPT | IP地址类型 | 可选必选说明：必选参数<br>参数含义：本参数用于指定IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4(IPV4)”<br>- “IPV6(IPV6)”<br>默认值：无 |
| LIPV4 | 本端IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定本端IPv4地址。<br>前提条件：本参数在"IP地址类型"参数配置为"IPV4(IPV4)"后生效，并且此IP地址必须在<br>[**ADD GTPCLE**](../../Gtpc本端实体管理/增加GTP-C本地实体(ADD GTPCLE)_26145966.md)<br>中已经配置。<br>数据来源：全网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| PIPV4 | 对端IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定对端IPv4地址。<br>前提条件：本参数在"IP地址类型"参数配置为"IPV4(IPV4)"后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| LIPV6 | 本端IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定本端IPv6地址。<br>前提条件：本参数在"IP地址类型"参数配置为"IPV6(IPV6)"后生效，并且此IP地址必须在<br>[**ADD GTPCLE**](../../Gtpc本端实体管理/增加GTP-C本地实体(ADD GTPCLE)_26145966.md)<br>中已经配置。<br>数据来源：全网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| PIPV6 | 对端IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定对端IPv6地址。<br>前提条件：本参数在"IP地址类型"参数配置为"IPV6(IPV6)"后生效。<br>数据来源：全网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：本参数用于描述路径信息，比如描述对端IP地址所属设备名称。<br>数据来源：本端规划<br>取值范围：0~32位字符串<br>默认值：无 |

## 操作的配置对象

- [GTP-C路径白名单（GTPCWHITELIST）](configobject/UNC/20.15.2/GTPCWHITELIST.md)

## 使用实例

增加GTP-C路径白名单，用于控制Sv接口GTP-C路径的本端IP地址选择。

ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="192.168.23.67";

ADD GTPCLE: IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="192.168.23.67";

ADD GTPCWHITELIST: INTFTP=Sv, IPT=IPV4, LIPV4="192.168.23.67", PIPV4="192.168.123.4", DESC="MSC1";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加GTP-C路径白名单(ADD-GTPCWHITELIST)_72345517.md`
