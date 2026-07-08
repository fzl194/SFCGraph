---
id: UDG@20.15.2@MMLCommand@RMV HTTPFCIPGRP
type: MMLCommand
name: RMV HTTPFCIPGRP（删除HTTP流控组）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: HTTPFCIPGRP
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP流控管理
- HTTP流控组管理
status: active
---

# RMV HTTPFCIPGRP（删除HTTP流控组）

## 功能

该命令用于删除HTTP固定速率流控的IP地址组信息。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RMVTYPE | 删除类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待删除的HTTP固定速率流控组类型。<br>数据来源：本端规划<br>取值范围：<br>- “INDEX（索引）”：HTTP固定速率流控IP地址组索引<br>- “GROUP（流控组）”：HTTP固定速率流控IP地址组唯一标识<br>默认值：无<br>配置原则：无 |
| INDEX | 索引 | 可选必选说明：该参数在"RMVTYPE"配置为"INDEX"时为条件必选参数。<br>参数含义：该参数用于标识具有相同前缀的一组IP地址。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4095。<br>默认值：无<br>配置原则：无 |
| GROUP | 流控组 | 可选必选说明：该参数在"RMVTYPE"配置为"GROUP"时为条件必选参数。<br>参数含义：该参数用于指定HTTP固定速率流控组的唯一标识。一个流控组中可以包括多个IP地址索引。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4095。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [HTTP流控组（HTTPFCIPGRP）](configobject/UDG/20.15.2/HTTPFCIPGRP.md)

## 使用实例

删除索引为1的HTTP固定速率流控地址组信息：

```
RMV HTTPFCIPGRP:RMVTYPE=INDEX, INDEX=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除HTTP流控组（RMV-HTTPFCIPGRP）_29291775.md`
