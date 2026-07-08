---
id: UNC@20.15.2@MMLCommand@RMV ACCESSLISTIP
type: MMLCommand
name: RMV ACCESSLISTIP（删除黑白名单）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ACCESSLISTIP
command_category: 配置类
applicable_nf:
- GGSN
- SGW-C
- PGW-C
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 黑白名单地址列表
status: active
---

# RMV ACCESSLISTIP（删除黑白名单）

## 功能

**适用NF：GGSN、SGW-C、PGW-C**

该命令用来删除黑白名单功能中SGSN/S-GW/MME的IP地址。在需要删除对SGSN/S-GW/MME的IP地址的黑白名单功能的控制时，使用该命令对已经配置的IP地址段进行删除操作。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP地址版本类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP类型。<br>数据来源：本端规划<br>取值范围：<br>- “IPV4（IPV4）”：表示地址类型为IPv4<br>- “IPV6（IPV6）”：表示地址类型为IPv6<br>默认值：无<br>配置原则：无 |
| SRVNODEIPV4 | IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定要进行黑白名单控制的SGSN/S-GW/MME的IPv4地址段的地址，该配置需要和网络规划保持一致。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| SRVNODEIPV4MASK | 掩码长度 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定黑白名单控制的SGSN/S-GW/MME的IPv4地址段的掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~32。<br>默认值：无<br>配置原则：无 |
| SRVNODEIPV6 | IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定要进行黑白名单控制的SGSN/S-GW/MME的IPv6地址段的地址，该配置需要和网络规划保持一致。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| SRVNODEIPV6MASK | 掩码长度 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定黑白名单控制的SGSN/S-GW/MME的IPv6地址段的掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ACCESSLISTIP]] · 黑白名单（ACCESSLISTIP）

## 使用实例

用户要删除对SGSN/S-GW/MME的IP地址的黑白名单功能的控制，需要删除已配置的IP地址为10.36.0.2，mask为27的IP地址段的记录：

```
RMV ACCESSLISTIP: IPVERSION=IPV4, SRVNODEIPV4="10.36.0.2", SRVNODEIPV4MASK=27;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-ACCESSLISTIP.md`
