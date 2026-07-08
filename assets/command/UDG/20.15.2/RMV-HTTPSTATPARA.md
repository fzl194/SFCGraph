---
id: UDG@20.15.2@MMLCommand@RMV HTTPSTATPARA
type: MMLCommand
name: RMV HTTPSTATPARA（删除HTTP统计参数）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: HTTPSTATPARA
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP链路内部统计管理
status: active
---

# RMV HTTPSTATPARA（删除HTTP统计参数）

## 功能

该命令用于删除一个HTTP对端地址。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERIPTYPE | 对端IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPv4（IPv4）”：IPv4地址<br>- “IPv6（IPv6）”：IPv6地址<br>默认值：无<br>配置原则：无 |
| PEERIPV4 | 对端IPv4地址 | 可选必选说明：该参数在"PEERIPTYPE"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定对端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| PEERIPV6 | 对端IPv6地址 | 可选必选说明：该参数在"PEERIPTYPE"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定对端IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HTTPSTATPARA]] · HTTP统计参数（HTTPSTATPARA）

## 使用实例

删除一条对端IP地址，执行命令如下：

```
RMV HTTPSTATPARA: PEERIPTYPE=IPv4, PEERIPV4="10.2.3.4";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除HTTP统计参数（RMV-HTTPSTATPARA）_29053337.md`
