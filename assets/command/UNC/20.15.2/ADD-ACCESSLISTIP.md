---
id: UNC@20.15.2@MMLCommand@ADD ACCESSLISTIP
type: MMLCommand
name: ADD ACCESSLISTIP（增加黑白名单）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD ACCESSLISTIP（增加黑白名单）

## 功能

**适用NF：GGSN、SGW-C、PGW-C**

该命令用来配置黑白名单功能中SGSN/S-GW/MME的IP地址。当运营商在部署分组交换网，新增SGSN/MME/S-GW时，如果需要对SGSN/MME/S-GW进行接入控制，使用该命令增加需要被控制网元的IP地址。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 多条记录的IP地址和掩码表示的IP地址段不允许重合。
- 当配置SGSN/S-GW/MME的IP地址的黑白名单功能时，需要先执行命令SET ACCESSLISTFUNC使能接入控制名单的功能，并配置系统支持的接入控制名单类型。

- 最多可输入100条记录。

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

配置IP地址为10.36.0.2，mask为27的IP地址段进入接入控制名单：

```
ADD ACCESSLISTIP: IPVERSION=IPV4, SRVNODEIPV4="10.36.0.2", SRVNODEIPV4MASK=27;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-ACCESSLISTIP.md`
