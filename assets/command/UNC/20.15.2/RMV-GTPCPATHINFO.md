---
id: UNC@20.15.2@MMLCommand@RMV GTPCPATHINFO
type: MMLCommand
name: RMV GTPCPATHINFO（删除GTP-C路径）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GTPCPATHINFO
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- GTP-C路径维护
status: active
---

# RMV GTPCPATHINFO（删除GTP-C路径）

## 功能

**适用NF：SGW-C、PGW-C、AMF、GGSN**

该命令用于删除GTP-C路径信息。

## 注意事项

- 该命令执行后立即生效。

- 当SET AMFN26PLCY命令中N26ITFMODE取值为“COMBINE”时，当前命令无效，请使用命令RMV GTPCPATH删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GTPVER | GTP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C路径的版本号。<br>数据来源：全网规划<br>取值范围：<br>- GTPv1（GTPv1）<br>- GTPv2（GTPv2）<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C路径的IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPTypeV4（IPv4类型）”：IPTypeV4<br>- “IPTypeV6（IPv6类型）”：IPTypeV6<br>默认值：无<br>配置原则：无 |
| LOCALIPV4 | 本端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPTypeV4"时为条件必选参数。<br>参数含义：该参数用于指定GTP-C路径的本端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>业务地址必须是A、B或者C类地址。 |
| PEERIPV4 | 对端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPTypeV4"时为条件必选参数。<br>参数含义：该参数用于指定GTP-C路径的对端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>业务地址必须是A、B或者C类地址。 |
| LOCALIPV6 | 本端IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPTypeV6"时为条件必选参数。<br>参数含义：该参数用于指定GTP-C路径的本端IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| PEERIPV6 | 对端IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPTypeV6"时为条件必选参数。<br>参数含义：该参数用于指定GTP-C路径的对端IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPCPATHINFO]] · GTP-C路径（GTPCPATHINFO）

## 使用实例

删除GTP-C路径，路径版本GTPv2版本，本端IP地址为10.2.14.20，对端IP地址为10.2.9.20：

```
RMV GTPCPATHINFO: GTPVER=GTPv2, IPTYPE=IPTypeV4, LOCALIPV4="10.2.14.20", PEERIPV4="10.2.9.20";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-GTPCPATHINFO.md`
