---
id: UDG@20.15.2@MMLCommand@RMV HTTPRESCFG
type: MMLCommand
name: RMV HTTPRESCFG（删除HTTP资源流控门限）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: HTTPRESCFG
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP流控管理
- HTTP资源流控管理
status: active
---

# RMV HTTPRESCFG（删除HTTP资源流控门限）

## 功能

该命令用于删除HTTP资源流控门限信息。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | HTTP资源门限索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HTTP资源门限的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~4096。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@HTTPRESCFG]] · HTTP资源流控门限（HTTPRESCFG）

## 使用实例

删除索引为1的HTTP资源流控门限，可以用如下命令：

```
RMV HTTPRESCFG: INDEX=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-HTTPRESCFG.md`
