---
id: UNC@20.15.2@MMLCommand@ADD HTTPRESCFG
type: MMLCommand
name: ADD HTTPRESCFG（增加HTTP资源流控门限）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: HTTPRESCFG
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP流控管理
- HTTP资源流控管理
status: active
---

# ADD HTTPRESCFG（增加HTTP资源流控门限）

## 功能

该命令用于增加HTTP资源流控门限信息。

## 注意事项

- 该命令执行后立即生效。

- 执行本命令前，需要确认资源流控功能已开启，可通过[**LST HTTPCONF**](../../HTTP管理/HTTP属性管理/查询HTTP属性（LST HTTPCONF）_28971839.md)/xref>查看。

- 最多可输入4096条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | HTTP资源门限索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HTTP资源门限的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~4096。<br>默认值：无<br>配置原则：无 |
| RESTYPE | 资源类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HTTP资源类型。<br>数据来源：本端规划<br>取值范围：<br>- “REQCB（REQCB）”：REQCB<br>默认值：无<br>配置原则：无 |
| LETYPE | 本端实体类型 | 可选必选说明：该参数在"RESTYPE"配置为"REQCB"时为条件必选参数。<br>参数含义：该参数用于指定HTTP本端实体的类型。<br>数据来源：本端规划<br>取值范围：<br>- “CLIENT（客户端）”：客户端<br>- “SERVER（服务端）”：服务端<br>默认值：无<br>配置原则：<br>HTTP本端实体可以作为服务端也可以作为客户端，两者需要分别配置。 |
| PEERIPTYPE | 对端地址IP类型 | 可选必选说明：该参数在"RESTYPE"配置为"REQCB"时为条件必选参数。<br>参数含义：该参数用于指定配置的对端地址的IP类型。<br>数据来源：本端规划<br>取值范围：<br>- “IPv4（IPv4地址）”：IPv4地址<br>- “IPv6（IPv6地址）”：IPv6地址<br>默认值：无<br>配置原则：无 |
| PEERIPV4 | 对端IPv4地址 | 可选必选说明：该参数在"PEERIPTYPE"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定对端IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| PEERIPV6 | 对端IPv6地址 | 可选必选说明：该参数在"PEERIPTYPE"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定对端IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| THRESHOLD | 资源门限 | 可选必选说明：该参数在"RESTYPE"配置为"REQCB"时为条件必选参数。<br>参数含义：该参数用于指定资源门限。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~4294967295，单位是个。<br>默认值：无<br>配置原则：<br>当资源类型为REQCB时，该参数需要配置为1-32640。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HTTPRESCFG]] · HTTP资源流控门限（HTTPRESCFG）

## 使用实例

增加HTTP资源流控门限，索引为1，资源类型为REQCB，本端实体类型为CLIENT，对端IP类型为IPv4，对端IP地址为192.168.1.1，资源门限为100，可以用如下命令：

```
ADD HTTPRESCFG: INDEX=1, RESTYPE=REQCB, LETYPE=CLIENT, PEERIPTYPE=IPv4, PEERIPV4="192.168.1.1", THRESHOLD=100;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-HTTPRESCFG.md`
