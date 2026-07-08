---
id: UDG@20.15.2@MMLCommand@RMV LOGICIP
type: MMLCommand
name: RMV LOGICIP（删除逻辑IP地址）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: LOGICIP
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IP管理
- IP配置
status: active
---

# RMV LOGICIP（删除逻辑IP地址）

## 功能

该命令用于删除指定的逻辑IP地址。

> **说明**
> - 该命令执行后立即生效。
>
> - 使用该命令删除LOGICIP前，需检查是否存在引用该LOGICIP的其他配置（例如，执行[**LST HTTPLE**](../../HTTP功能管理/HTTP管理/HTTP本端实体管理/查询HTTP本端实体（LST HTTPLE）_29291769.md)查询是否存在依赖于该LOGICIP的HTTPLE），并判断是否需要先删除上层依赖的记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置的IP地址的版本，用于区别配置的是IPv4地址还是IPv6地址。<br>数据来源：全网规划<br>取值范围：<br>- “IPv4（IPv4）”：IPv4地址<br>- “IPv6（IPv6）”：IPv6地址<br>默认值：无<br>配置原则：无 |
| LOGICIPV4 | IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定逻辑IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。业务地址必须是A、B或者C类地址。<br>默认值：无<br>配置原则：<br>业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。业务地址必须是A、B或者C类地址。 |
| LOGICIPV6 | IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定逻辑IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>默认值：无<br>配置原则：<br>IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |

## 操作的配置对象

- [逻辑IP地址信息（LOGICIP）](configobject/UDG/20.15.2/LOGICIP.md)

## 使用实例

删除地址为“192.168.1.1”的逻辑IP地址。

```
RMV LOGICIP: IPVERSION=IPv4, LOGICIPV4="192.168.1.1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除逻辑IP地址（RMV-LOGICIP）_09587388.md`
