---
id: UNC@20.15.2@MMLCommand@TST GTPUPATHINFO
type: MMLCommand
name: TST GTPUPATHINFO（测试GTPU路径）
nf: UNC
version: 20.15.2
verb: TST
object_keyword: GTPUPATHINFO
command_category: 调测类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N4 GTP-U管理
- N4 GTP-U路径管理
status: active
---

# TST GTPUPATHINFO（测试GTPU路径）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于通过发送Echo消息的方法测试本端与对端之间的GTPU路径是否正常。如果路径正常，则返回报文显示路径地址信息；如果路径不正常，则返回报文显示20111错误码，提示无记录。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTPU的IP类型。<br>数据来源：全网规划<br>取值范围：<br>- IPV4（IPV4）<br>- IPV6（IPV6）<br>默认值：无<br>配置原则：无 |
| LOCALIPV4 | 本端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定GTPU本端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| PEERIPV4 | 对端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定GTPU对端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| LOCALIPV6 | 本端IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定GTPU本端IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| PEERIPV6 | 对端IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定GTPU对端IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| VPN | VPN | 可选必选说明：可选参数<br>参数含义：该参数用于指定本端VPN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。<br>默认值：无<br>配置原则：无 |
| PORT | 对端端口 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端GTPU端口。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GTPUPATHINFO]] · GTPU路径（GTPUPATHINFO）

## 使用实例

测试本端与对端之间的GTPU路径是否正常，IP地址类型为IPTypeV4，本端IP地址为10.0.0.1，对端IP地址为10.0.0.2;

```
TST GTPUPATHINFO: IPTYPE=IPV4, LOCALIPV4="10.0.0.1", PEERIPV4="10.0.0.2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/TST-GTPUPATHINFO.md`
