---
id: UDG@20.15.2@MMLCommand@RMV AFDNSSERVER
type: MMLCommand
name: RMV AFDNSSERVER（删除防欺诈可信DNS服务器）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: AFDNSSERVER
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务防欺诈
- 防欺诈可信DNS服务器
status: active
---

# RMV AFDNSSERVER（删除防欺诈可信DNS服务器）

## 功能

**适用NF：PGW-U、UPF**

![](删除防欺诈可信DNS服务器（RMV AFDNSSERVER）_82837809.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除防欺诈可信DNS服务器可能会改变业务匹配结果，导致用户业务受损，请谨慎使用并联系华为支持协助操作。

该命令用于删除指定的可信DNS服务器IP。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP地址版本类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP地址版本类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：IPv4地址类型。<br>- IPV6：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| IPV4ADDR | DNS服务器IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于指定IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。<br>默认值：无<br>配置原则：无 |
| IPV6ADDR | DNS服务器IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于指定IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/AFDNSSERVER]] · 防欺诈可信DNS服务器（AFDNSSERVER）

## 使用实例

删除指定的DNS server地址：

```
RMV AFDNSSERVER:IPVERSION=IPV4,IPV4ADDR="192.168.0.1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除防欺诈可信DNS服务器（RMV-AFDNSSERVER）_82837809.md`
