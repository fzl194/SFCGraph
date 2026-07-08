---
id: UNC@20.15.2@MMLCommand@RMV DHCPGIP
type: MMLCommand
name: RMV DHCPGIP（删除支持DHCP服务的GGSN IP地址）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DHCPGIP
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GnGp-GGSN_S5_S8接口管理
- 支持DHCP服务的GGSN IP地址
status: active
---

# RMV DHCPGIP（删除支持DHCP服务的GGSN IP地址）

## 功能

![](删除支持DHCP服务的GGSN IP地址（RMV DHCPGIP）_72225629.assets/notice_3.0-zh-cn_2.png)

删除支持DHCP服务的GGSN IP地址可能会导致DHCP方式接入方式下的PDP激活失败。

**适用网元：SGSN**

1. 删除支持DHCP服务的GGSN IP地址。
2. SGSN支持用户采用DHCP方式接入，在采用DHCP接入方式时，不需要对APN进行DNS解析，只需要在SGSN中配置支持DHCP服务的GGSN IP地址即可。用户在激活PDP上下文时，如果携带的APN为"DHCP"，SGSN可以通过这张表获得支持DHCP服务的GGSN。

## 注意事项

- 该命令执行后立即生效。
- 删除后如果本表记录为空，则不能采用DHCP方式激活PDP。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPT | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP地址类型。<br>数据来源：整网规划<br>取值范围：<br>“IPV4(IPV4)”<br>、<br>“IPV6(IPV6)”<br>、<br>“IPV4V6(IPV4V6)”<br>默认值： 无。 |
| IPV4 | GGSN IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GGSN IPv4地址。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值： 无。<br>配置原则：<br>- 有效的IPv4地址不能为 0.0.0.0,255.255.255.255，或0.x.y.z。<br>- 有效的IPv4地址不能为环回地址(127.x.y.z)，或组播地址(224.x.y.z)。<br>- 有效的IPv4地址必须是A、B或者C类地址。 |
| IPV6 | GGSN IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GGSN IPv6地址。<br>数据来源：整网规划<br>取值范围： ::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值： 无。<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、 FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |

## 操作的配置对象

- [支持DHCP服务的GGSN IP地址（DHCPGIP）](configobject/UNC/20.15.2/DHCPGIP.md)

## 使用实例

删除一个支持DHCP服务的GGSN IP地址“192.168.33.171”：

**RMV DHCPGIP: IPT=IPV4, IPV4="192.168.33.171";**

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除支持DHCP服务的GGSN-IP地址（RMV-DHCPGIP）_72225629.md`
