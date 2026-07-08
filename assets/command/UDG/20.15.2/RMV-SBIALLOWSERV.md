---
id: UDG@20.15.2@MMLCommand@RMV SBIALLOWSERV
type: MMLCommand
name: RMV SBIALLOWSERV（删除基于服务的白名单）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: SBIALLOWSERV
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- 白名单管理
- 基于服务的白名单管理
status: active
---

# RMV SBIALLOWSERV（删除基于服务的白名单）

## 功能

该命令用于删除已配置的服务白名单。当服务白名单删除后，如果该服务无其他白名单配置，则原白名单中指定网元类型允许访问该服务的限制失效，即该服务可以被所有类型网元访问；如果该服务还有其他白名单配置，则被删除的白名单中指定网元类型不再允许访问该服务。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置的白名单索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [基于服务的白名单（SBIALLOWSERV）](configobject/UDG/20.15.2/SBIALLOWSERV.md)

## 使用实例

若运营商想要取消只有nrf类型的网元可以访问“nnrf-nfm”服务的限制，且该服务的白名单只配置了一条，其索引值为1，则执行如下命令。

```
RMV SBIALLOWSERV: INDEX=1; 
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除基于服务的白名单（RMV-SBIALLOWSERV）_83972194.md`
