---
id: UNC@20.15.2@MMLCommand@MOD GTPCLE
type: MMLCommand
name: MOD GTPCLE（修改GTP-C本地实体）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: GTPCLE
command_category: 配置类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- Gtpc本端实体管理
status: active
---

# MOD GTPCLE（修改GTP-C本地实体）

## 功能

**适用网元：SGSN、MME、AMF**

本命令用于修改已存在的GTPC本端实体的描述信息。

## 注意事项

- 本命令执行后立即生效。
- 同一个IP地址不能配置不同的VPN名称。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MODTYPE | 修改类型 | 可选必选说明：必选参数<br>参数含义：本参数用于指定修改GTPC本端实体的操作类型。<br>数据来源：本端规划<br>取值范围：<br>- “BYINDEX(根据记录索引)”<br>- “BYIP(根据IP地址)”<br>默认值：无 |
| LEINDEX | GTP-C本端实体标识 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定GTPC本端实体的记录索引。<br>前提条件：该参数在<br>“修改类型”<br>参数配置为<br>“BYINDEX(根据记录索引)”<br>后生效。<br>数据来源：本端规划<br>取值范围：0~255<br>默认值：无<br>说明：使用<br>[**LST GTPCLE**](查询GTP-C本地实体(LST GTPCLE)_72345567.md)<br>查询记录的索引。 |
| GROUPID | 组号 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定GTPC本端实体对应的组号。组号用于组网规划时不同接口，或者不同用户范围使用独立的GTPC本端实体。<br>前提条件：该参数在<br>“修改类型”<br>参数配置为<br>“BYIP(根据IP地址)”<br>后生效。<br>数据来源：本端规划<br>取值范围：0~32<br>默认值：无<br>说明：组号的应用参考<br>[**ADD GTPCINTFATTR**](../GTP-C接口类型属性/增加GTP-C IP地址接口属性(ADD GTPCINTFATTR)_72225579.md)<br>命令帮助。 |
| IPTYPE | IP地址类型 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定GTPC本端实体的IP地址类型。<br>前提条件：该参数在<br>“修改类型”<br>参数配置为<br>“BYIP(根据IP地址)”<br>后生效。<br>数据来源：本端规划<br>取值范围：<br>- “TPTADDR_TYPE_IPV4(IPv4)”<br>- “TPTADDR_TYPE_IPV6(IPv6)”<br>默认值：无 |
| LEIPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定GTPC本端实体的IPv4地址。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“TPTADDR_TYPE_IPV4(IPv4)”<br>后生效。<br>数据来源：本端规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| LEIPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定GTPC本端实体的IPv6地址。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“TPTADDR_TYPE_IPV6(IPv6)”<br>后生效。<br>数据来源：本端规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| VPNNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：本参数用于指定新的VPN名称。<br>数据来源：本端规划<br>取值范围：0~31位字符串<br>默认值：无<br>配置原则：<br>- 支持输入的字符为字母、数字、下划线。<br>- vpn名称区分英文字母的大小写。<br>- 当输入字符为空时，表示vpn名称不修改。 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：本参数用于指定新的描述信息。新的描述信息将会覆盖原描述信息。<br>数据来源：本端规划<br>取值范围：0~32位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPCLE]] · GTP-C本地实体（GTPCLE）

## 使用实例

修改索引为1的GTPC本地实体的描述信息：

MOD GTPCLE: MODTYPE=BYINDEX, LEINDEX=1, DESC="private";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-GTPCLE.md`
