---
id: UNC@20.15.2@MMLCommand@RMV M2MSERVER
type: MMLCommand
name: RMV M2MSERVER（删除M2M服务器）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: M2MSERVER
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
- M2M服务器
status: active
---

# RMV M2MSERVER（删除M2M服务器）

## 功能

**适用NF：PGW-C、SMF**

该命令用来删除指定M2M服务器组下的M2M服务器。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | M2M服务器组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定M2M服务器所属M2M服务器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：<br>GROUPNAME参数依赖M2MSERVERGRP命令的GROUPNAME参数。 |
| SERVERINDEX | M2M服务器索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定M2M服务器索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@M2MSERVER]] · M2M服务器（M2MSERVER）

## 使用实例

删除“m2msrvgroup01”M2M服务器组下的M2M服务器：

```
RMV M2MSERVER: GROUPNAME="m2msrvgroup01", SERVERINDEX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-M2MSERVER.md`
