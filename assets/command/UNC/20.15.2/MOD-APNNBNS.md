---
id: UNC@20.15.2@MMLCommand@MOD APNNBNS
type: MMLCommand
name: MOD APNNBNS（修改APN的NBNS属性）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: APNNBNS
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- DN网络DNS_NBNS选择管理
- NBNS选择管理
- APN的NBNS属性
status: active
---

# MOD APNNBNS（修改APN的NBNS属性）

## 功能

**适用NF：PGW-C、GGSN、SMF**

该命令用来修改APN实例的NBNS属性。

## 注意事项

- 该命令执行后立即生效。

- 配置该命令时至少输入一个可选参数，如果输入备NBNS服务器IP，必须输入主NBNS服务器IP。
- 允许同时设置主备NBNS服务器IP为0.0.0.0。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPV4PRIMARYIP | 主NBNS | 可选必选说明：可选参数<br>参数含义：该参数用于指定主NBNS服务器IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制IPv4地址，仅支持A、B、C类IP。0.0.0.0表示无效值。在MOD APNNBNS命令下，允许同时设置主备NBNS为0.0.0.0。<br>默认值：无<br>配置原则：无 |
| IPV4SECONDARYIP | 备NBNS | 可选必选说明：可选参数<br>参数含义：该参数用于指定备NBNS服务器IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制IPv4地址，仅支持A、B、C类IP。0.0.0.0表示无效值。在MOD APNNBNS命令下，允许同时设置主备NBNS为0.0.0.0。<br>默认值：无<br>配置原则：<br>在执行ADD APNNBNS时，不配置该参数时默认为NULL。 |
| IPV4PRIORFIRST | 第一优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv4第一优先级属性。<br>数据来源：全网规划<br>取值范围：在执行ADD APNNBNS时，不配置该参数时默认为DHCP。<br>- “LOCAL（local）”：指定本地配置优先。<br>- “RADIUS（radius）”：指定RADIUS服务器返回的NBNS属性优先。<br>- “DHCP（dhcp）”：指定DHCP服务器返回的NBNS属性优先。<br>默认值：无<br>配置原则：无 |
| IPV4PRIORSECOND | 第二优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv4第二优先级属性。<br>数据来源：全网规划<br>取值范围：在执行ADD APNNBNS时，不配置该参数时默认为RADIUS。<br>- “LOCAL（local）”：指定本地配置优先。<br>- “RADIUS（radius）”：指定RADIUS服务器返回的NBNS属性优先。<br>- “DHCP（dhcp）”：指定DHCP服务器返回的NBNS属性优先。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNNBNS]] · APN的NBNS属性（APNNBNS）

## 使用实例

修改APN为“huawei.com”NBNS属性的主备NBNS地址：

```
MOD APNNBNS: APN="huawei.com", IPV4PRIMARYIP="10.1.1.1", IPV4SECONDARYIP="10.2.2.2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-APNNBNS.md`
