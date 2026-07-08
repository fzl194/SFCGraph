---
id: UNC@20.15.2@MMLCommand@ADD DHCPGIP
type: MMLCommand
name: ADD DHCPGIP（增加支持DHCP服务的GGSN IP地址）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD DHCPGIP（增加支持DHCP服务的GGSN IP地址）

## 功能

**适用网元：SGSN**

1. 该命令用于增加支持DHCP服务的GGSN IP地址。
2. SGSN支持用户采用DHCP方式接入，在采用DHCP接入方式时，不需要对APN进行DNS解析，只需要在SGSN中配置支持DHCP服务的GGSN IP地址即可。

## 注意事项

- 该命令执行后立即生效。
- 最多可以输入4条记录。
- 输入的IP地址不允许与已有的记录重复。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPT | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP地址类型。<br>数据来源：整网规划<br>取值范围：<br>“IPV4(IPV4)”<br>、<br>“IPV6(IPV6)”<br>、<br>“IPV4V6(IPV4V6)”<br>默认值：<br>“IPV4(IPV4)” |
| IPV4 | GGSN IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GGSN IPv4地址。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值： 无。<br>配置原则：<br>- 有效的IPv4地址不能为 0.0.0.0,255.255.255.255，或0.x.y.z。<br>- 有效的IPv4地址不能为环回地址(127.x.y.z)，或组播地址(224.x.y.z)。<br>- 有效的IPv4地址必须是A、B或者C类地址。 |
| IPV6 | GGSN IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GGSN IPv6地址。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值： 无。<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、 FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于增加配置命令的描述信息。<br>数据来源：整网规划<br>取值范围：0~32位字符串<br>默认值：无 |

## 操作的配置对象

- [支持DHCP服务的GGSN IP地址（DHCPGIP）](configobject/UNC/20.15.2/DHCPGIP.md)

## 使用实例

1. 增加一个支持DHCP服务的GGSN IPv4地址“192.168.22.22”：
  **ADD DHCPGIP: IPT=IPV4, IPV4="192.168.22.22";**

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加支持DHCP服务的GGSN-IP地址（ADD-DHCPGIP）_26145950.md`
