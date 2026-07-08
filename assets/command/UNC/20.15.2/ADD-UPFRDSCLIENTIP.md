---
id: UNC@20.15.2@MMLCommand@ADD UPFRDSCLIENTIP
type: MMLCommand
name: ADD UPFRDSCLIENTIP（增加中转UPF与Radius客户端的绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: UPFRDSCLIENTIP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- 连接管理
- UPF中转Radius客户端IP
status: active
---

# ADD UPFRDSCLIENTIP（增加中转UPF与Radius客户端的绑定关系）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于增加中转UPF与Radius客户端的绑定关系。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入6000条记录。当配置记录数大于规格的98%时，会上报“ALM-135602215 配置数量超阈值”告警。当配置记录数小于等于配置规格95%时，恢复“ALM-135602215 配置数量超阈值”告警。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLIENTYPE | 客户端类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RADIUS客户端类型。<br>数据来源：本端规划<br>取值范围：<br>- “AUTHENTICATION（鉴权客户端）”：表示鉴权客户端。<br>- “ACCOUNTING（计费客户端）”：表示计费客户端。<br>- “ACCT_AND_AUTH（计费和鉴权客户端）”：表示计费和鉴权客户端。<br>默认值：无<br>配置原则：无 |
| IPVERSION | 客户端IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RADIUS客户端IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4（IPv4）”：IPv4<br>- “IPV6（IPv6）”：IPv6<br>默认值：无<br>配置原则：无 |
| CLIENTIPV4 | IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定RADIUS客户端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| CLIENTIPV6 | IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定RADIUS客户端IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| UPLISTNAME | UP列表名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UP列表名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD UPLIST4RDS**](../UP列表/向RADIUS服务器使用的UP列表中增加UP（ADD UPLIST4RDS）_52749060.md)<br>命令配置生成。 |
| VPNINSTANCE | VPN实例 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：无 |
| NETINSTNAMESRC | 网络实例名称来源 | 可选必选说明：可选参数<br>参数含义：该参数用于指定网络实例名称来源。<br>数据来源：本端规划<br>取值范围：<br>- “VPN（VPN实例名称）”：和本配置的VPN实例一致。<br>- “Specified（指定网络实例名称）”：和本配置的指定网络实例名称一致。<br>默认值：VPN<br>配置原则：<br>取值为VPN时表示网络实例名称和VPN实例一致，当VPN实例为空时，默认为“_public_”；取值为Specified时表示网络实例名称和本配置的指定网络实例名称一致。 |
| SPECNETINSTNAME | 指定网络实例名称 | 可选必选说明：该参数在"NETINSTNAMESRC"配置为"Specified"时为条件必选参数。<br>参数含义：该参数用于指定网络实例名称。网络实例名称用于设定建立中转AAA的PFCP会话的PFCP Session Establishment Request中的下行数据包检测规则的网络实例。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~100。只允许输入字母、数字、“.”、“_”、和“-”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [中转UPF与Radius客户端的绑定关系（UPFRDSCLIENTIP）](configobject/UNC/20.15.2/UPFRDSCLIENTIP.md)

## 使用实例

如果想要新增UPF中转RADIUS客户端IP，可以指定客户端类型为鉴权，客户端IP版本为“IPv4”，客户端地址为“192.168.10.1”，UP列表名称为“uplist1”，VPN实例为“vpnInstance1”，例如：

```
ADD UPFRDSCLIENTIP: CLIENTYPE=AUTHENTICATION, IPVERSION=IPV4, UPLISTNAME="uplist1", VPNINSTANCE="vpnInstance1", CLIENTIPV4="192.168.10.1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加中转UPF与Radius客户端的绑定关系（ADD-UPFRDSCLIENTIP）_90026962.md`
