---
id: UDG@20.15.2@MMLCommand@RMV HTTPLE
type: MMLCommand
name: RMV HTTPLE（删除HTTP本端实体）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: HTTPLE
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP本端实体管理
status: active
---

# RMV HTTPLE（删除HTTP本端实体）

## 功能

该命令用于删除HTTP本端实体。

> **说明**
> - 该命令执行后立即生效。
>
> - 删除HTTP本端实体时，如果该HTTP本端实体所属的HTTP本端实体组已经被SBIAPLE引用且该HTTP本端实体中只配置了一个客户端或一个服务端，则不允许删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | HTTPLE本端实体索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HTTP本端实体的索引信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [HTTP本端实体（HTTPLE）](configobject/UDG/20.15.2/HTTPLE.md)

## 使用实例

若运营商想删除索引为1的HTTP本端实体配置，可以用如下命令

```
RMV HTTPLE: INDEX=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除HTTP本端实体（RMV-HTTPLE）_28971847.md`
