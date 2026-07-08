---
id: UNC@20.15.2@MMLCommand@RMV GBEPPOOL
type: MMLCommand
name: RMV GBEPPOOL（删除地址池中IP地址）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GBEPPOOL
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- Gb自动配置管理
- Gb地址池管理
status: active
---

# RMV GBEPPOOL（删除地址池中IP地址）

## 功能

![](删除地址池中IP地址(RMV GBEPPOOL)_72225677.assets/notice_3.0-zh-cn_2.png)

删除GBEPPOOL可能导致GB over IP相关业务无法使用。

**适用网元：SGSN**

此命令用于删除地址池中IP地址。

## 注意事项

- 此命令执行后立即生效。
- 如果该IP地址已经被使用，可以删除。所以此命令会导致已使用此IP的Gb业务不可用，用户需谨慎操作。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址池中待删除的IP地址类型。<br>取值范围：<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：无 |
| IPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定地址池中待删除的IPv4地址。<br>前提条件：该参数在<br>“ IP类型 ”<br>设置为<br>“IPV4(IPv4)”<br>时生效。<br>取值范围：0.0.0.1～255.255.255.254<br>默认值：无<br>配置原则：<br>- 有效的IPV4地址不能为环回地址(127.x.y.z)。<br>- 有效的IPV4地址必须是A、B或者C类地址。 |
| IPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定地址池中待删除的IPv6地址。<br>前提条件：该参数在<br>“ IP类型 ”<br>设置为<br>“IPV6(IPv6)”<br>时生效。<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：IPV6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GBEPPOOL]] · 地址池中IP地址（GBEPPOOL）

## 使用实例

从地址池中删除一个 “IP类型” 为 “IPV4(IPv4)” ， “IPv4地址” 为 “192.168.4.101” 的IP：

RMV GBEPPOOL: IPTYPE=IPV4, IPV4="192.168.4.101";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除地址池中IP地址(RMV-GBEPPOOL)_72225677.md`
