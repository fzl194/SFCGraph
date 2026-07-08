---
id: UDG@20.15.2@MMLCommand@RMV ALLOWSERNAME
type: MMLCommand
name: RMV ALLOWSERNAME（删除基于地址的白名单）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: ALLOWSERNAME
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- 白名单管理
- 基于地址的白名单管理
status: active
---

# RMV ALLOWSERNAME（删除基于地址的白名单）

## 功能

该命令用于删除基于服务地址的指定NF的服务的白名单信息。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定白名单索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [基于地址的白名单（ALLOWSERNAME）](configobject/UDG/20.15.2/ALLOWSERNAME.md)

## 使用实例

删除标识为SMF_Instance_0的NF实例服务白名单信息:索引为0。

```
RMV ALLOWSERNAME: INDEX=0;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除基于地址的白名单（RMV-ALLOWSERNAME）_29213289.md`
