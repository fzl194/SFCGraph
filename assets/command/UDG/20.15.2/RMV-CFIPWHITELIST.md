---
id: UDG@20.15.2@MMLCommand@RMV CFIPWHITELIST
type: MMLCommand
name: RMV CFIPWHITELIST（删除IP地址白名单列表）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: CFIPWHITELIST
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- 内容过滤IP白名单配置
status: active
---

# RMV CFIPWHITELIST（删除IP地址白名单列表）

## 功能

**适用NF：PGW-U、UPF**

![](删除IP地址白名单列表（RMV CFIPWHITELIST）_28121349.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除IP地址白名单列表，可能会影响用户ICAP业务匹配，导致用户业务受损，请谨慎使用并联系华为支持协助操作。

该命令用于删除配置IP地址白名单。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置Ip地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4：IPv4地址类型。<br>- IPV6：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| IPV4ADDR | IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPTYPE”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于指定IPv4地址。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：无 |
| IPV4MASKLEN | IPv4地址掩码长度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPTYPE”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于指定IPv4地址掩码长度。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：无 |
| IPV6ADDR | IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPTYPE”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于设置Ipv6地址。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：无 |
| IPV6MASKLEN | IPv6地址掩码长度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPTYPE”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于指定IPv6地址掩码长度。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CFIPWHITELIST]] · IP地址白名单列表（CFIPWHITELIST）

## 使用实例

删除IP地址列表RMV CFIPWHITELIST：

```
RMV CFIPWHITELIST: IPTYPE=IPV4, IPV4ADDR="0.0.0.0", IPV4MASKLEN=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除IP地址白名单列表（RMV-CFIPWHITELIST）_28121349.md`
