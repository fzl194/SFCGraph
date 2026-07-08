---
id: UNC@20.15.2@MMLCommand@MOD DIAMETERAAA
type: MMLCommand
name: MOD DIAMETERAAA（修改Diameter AAA服务器）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: DIAMETERAAA
command_category: 配置类
applicable_nf:
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- Diameter AAA管理
- 服务器配置
- Diameter AAA信息
status: active
---

# MOD DIAMETERAAA（修改Diameter AAA服务器）

## 功能

**适用NF：PGW-C**

此命令用于修改Diameter AAA服务器信息，包括VPN实例。当网络重新规划，需要修改Diameter AAA的VPN信息时，需要执行该命令。

## 注意事项

- 该命令执行后立即生效。

- 如果该DIAMETERAAA已经被绑定到DIAMCONNGRP中，不允许修改VPN实例。
- 一个DIAMAAAGRP下所绑定的DIAMETERAAA的VPN要保持一致。因此，如果该DIAMETERAAA已经被绑定到DIAMAAAGRP中，且DIAMAAAGRP下绑定了其他的DIAMETERAAA，则不允许修改VPN实例。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter AAA服务器的主机名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，由软参BIT150控制是否区分大小写。BIT150值为0时，不区分大小写；值为1时，区分大小写，但不允许配置多个仅大小写不同的host-name或realm-name。BIT150详细信息请参见产品文档中的《UNC软件参数》。<br>默认值：无<br>配置原则：无 |
| VPNINSTANCE | VPN实例名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter AAA服务器所在的VPN实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用[**ADD VPNINST**](../../../../接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)命令配置生成。<br>- 输入单空格将删除该参数已有配置项。 |
| WALVALUE | WAL值 | 可选必选说明：可选参数<br>参数含义：该参数表示整机（UNC）每秒发送给该Diameter AAA服务器的最大消息数，但STR消息的发送不受发送窗口限制。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65534。<br>默认值：无<br>配置原则：<br>1、缺省为0，表示不控制消息数。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DIAMETERAAA]] · Diameter AAA服务器（DIAMETERAAA）

## 使用实例

根据网络规划，需要修改名称为“diameteraaa1”的Diameter AAA服务器的VPN实例为“vpn2”：

```
MOD DIAMETERAAA:HOSTNAME="diameteraaa1",VPNINSTANCE="vpn2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Diameter-AAA服务器（MOD-DIAMETERAAA）_64343897.md`
