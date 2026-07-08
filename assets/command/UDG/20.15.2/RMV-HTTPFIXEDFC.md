---
id: UDG@20.15.2@MMLCommand@RMV HTTPFIXEDFC
type: MMLCommand
name: RMV HTTPFIXEDFC（删除HTTP流控组固定速率流控信息）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: HTTPFIXEDFC
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP流控管理
- HTTP流控组固定速率流控管理
status: active
---

# RMV HTTPFIXEDFC（删除HTTP流控组固定速率流控信息）

## 功能

该命令用于删除HTTP固定速率流控门限值信息。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUP | 流控组 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HTTP固定速率流控组的唯一标识。该参数来源于<br>[**ADD HTTPFCIPGRP**](../HTTP流控组管理/增加HTTP流控组（ADD HTTPFCIPGRP）_29053323.md)<br>命令的“流控组”参数，可通过<br>[**LST HTTPFCIPGRP**](../HTTP流控组管理/查询HTTP流控组（LST HTTPFCIPGRP）_83813632.md)<br>命令查询获取。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4095。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HTTPFIXEDFC]] · HTTP流控组固定速率流控信息（HTTPFIXEDFC）

## 使用实例

删除HTTP固定速率流控门限值信息

```
RMV HTTPFIXEDFC: GROUP=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-HTTPFIXEDFC.md`
