---
id: UDG@20.15.2@MMLCommand@RMV HTTPFIXEDFCINF
type: MMLCommand
name: RMV HTTPFIXEDFCINF（删除HTTP接口类型固定速率流控信息）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: HTTPFIXEDFCINF
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP流控管理
- HTTP接口类型固定速率流控管理
status: active
---

# RMV HTTPFIXEDFCINF（删除HTTP接口类型固定速率流控信息）

## 功能

该命令用于删除HTTP接口类型固定速率流控门限值信息。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OFCIDX | 局向索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定局向索引。该参数来源于<br>[**ADD HTTPOFC**](../../HTTP管理/HTTP局向管理/增加HTTP局向（ADD HTTPOFC）_35230482.md)<br>命令的“局向索引”参数，可通过<br>[**LST HTTPOFC**](../../HTTP管理/HTTP局向管理/查询HTTP局向（LST HTTPOFC）_86150085.md)<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4095。<br>默认值：无<br>配置原则：<br>此处只能绑定"NFITEM"包含"FIXSPDFCINTF（基于接口类型固定速率流控）"的局向。 |
| LETYPE | 本端实体类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HTTP本端实体的类型。<br>数据来源：全网规划<br>取值范围：<br>- “SERVER（服务端）”：服务端<br>- “CLIENT（客户端）”：客户端<br>默认值：无<br>配置原则：<br>HTTP本端实体可以作为服务端也可以作为客户端，两者需要分别配置。 |

## 操作的配置对象

- [HTTP接口类型固定速率流控信息（HTTPFIXEDFCINF）](configobject/UDG/20.15.2/HTTPFIXEDFCINF.md)

## 使用实例

删除局向索引为1，本端实体类型为客户端的HTTP接口类型固定速率流控门限值信息：

```
RMV HTTPFIXEDFCINF: OFCIDX=1, LETYPE=CLIENT;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除HTTP接口类型固定速率流控信息（RMV-HTTPFIXEDFCINF）_52280614.md`
