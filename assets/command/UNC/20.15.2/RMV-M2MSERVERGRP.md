---
id: UNC@20.15.2@MMLCommand@RMV M2MSERVERGRP
type: MMLCommand
name: RMV M2MSERVERGRP（删除M2M服务器组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: M2MSERVERGRP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- M2M
- M2M服务器组
status: active
---

# RMV M2MSERVERGRP（删除M2M服务器组）

## 功能

**适用NF：PGW-C、SMF**

该命令用于删除M2M服务器配置，以及M2M服务器组下的M2M服务器IP配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | M2M服务器组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定M2M服务器组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。字符串类型，输入长度范围为1～31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/M2MSERVERGRP]] · M2M服务器组（M2MSERVERGRP）

## 使用实例

删除组名为m2msrvgroup01的M2M服务器组配置信息：

```
RMV M2MSERVERGRP:GROUPNAME="m2msrvgroup01";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除M2M服务器组（RMV-M2MSERVERGRP）_73321243.md`
