---
id: UDG@20.15.2@MMLCommand@RMV IFIPV6NDRAPREFIX
type: MMLCommand
name: RMV IFIPV6NDRAPREFIX（删除IPv6 RA通告前缀）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: IFIPV6NDRAPREFIX
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- IPv6地址前缀通告
status: active
---

# RMV IFIPV6NDRAPREFIX（删除IPv6 RA通告前缀）

## 功能

该命令用于删除接口IPv6 RA通告前缀。

## 注意事项

- 该命令执行后立即生效。
- 指定的前缀不能为链路本地地址（fe80::）、组播地址（ff00::）以及其他接口已经使用的前缀（包括接口地址前缀和RA消息携带的前缀）。
- 该命令可以在VNRS_VNFC的Ethernet接口，Ethernet子接口以及Tunnel口上配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IPV6前缀接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| IPV6ADDRPREFIX | IPv6地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IPv6前缀地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| PREFIXLEN | IPv6前缀长度 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口IPv6地址前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IFIPV6NDRAPREFIX]] · IPv6 RA通告前缀（IFIPV6NDRAPREFIX）

## 使用实例

删除接口IPv6 RA通告前缀：

```
RMV IFIPV6NDRAPREFIX:IFNAME="ethernet64/0/3",IPV6ADDRPREFIX="2001:db8::1",PREFIXLEN=64;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-IFIPV6NDRAPREFIX.md`
