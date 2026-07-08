---
id: UNC@20.15.2@MMLCommand@RMV CONFLICTIP
type: MMLCommand
name: RMV CONFLICTIP（删除冲突地址）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CONFLICTIP
command_category: 配置类
applicable_nf:
- GGSN
- SMF
- PGW-C
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 冲突地址管理
status: active
---

# RMV CONFLICTIP（删除冲突地址）

## 功能

**适用NF：GGSN、SMF、PGW-C**

该命令用于取消本地地址池中指定地址或所有地址的冲突状态。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | 地址池名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定已配置的地址池的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRPOOL命令配置生成。 |
| IPVERSION | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- “IPv4（IPv4）”：IPv4<br>- “IPv6（IPv6）”：IPv6<br>默认值：IPv4<br>配置原则：无 |
| IPADDRESS | 冲突IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv4"时为条件可选参数。<br>参数含义：该参数用于指定冲突IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>- 取值范围：1.0.0.0~255.255.255.254。<br>- IPv4地址不能为组播地址（224.x.y.z）和环回地址(127.x.y.z)。<br>- IPv4地址必须是A、B或者C类地址。 |
| IPV6PREFIX | 冲突IPv6地址前缀 | 可选必选说明：该参数在"IPVERSION"配置为"IPv6"时为条件可选参数。<br>参数含义：该参数用于指定冲突IPv6地址前缀。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>- 取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）、组播地址（FF00::/8）和IPv4映射地址（::FFFF:XXXX:XXXX），若为IPv4兼容地址时，需判断是否符合IPv4地址要求。 |
| IPV6PREFIXLEN | IPv6前缀长度 | 可选必选说明：该参数在"IPVERSION"配置为"IPv6"时为条件可选参数。<br>参数含义：该参数用于指定IPv6前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是49~64。<br>默认值：无<br>配置原则：<br>该参数必须与对应地址池规划的指定IPv6前缀长度一致，否则无法生效。 |

## 操作的配置对象

- [冲突地址（CONFLICTIP）](configobject/UNC/20.15.2/CONFLICTIP.md)

## 使用实例

在本地地址池lap中删除IPv4地址“10.1.1.1”的冲突状态：

```
RMV CONFLICTIP:POOLNAME="lap",IPVERSION=IPv4,IPADDRESS="10.1.1.1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除冲突地址（RMV-CONFLICTIP）_64343901.md`
