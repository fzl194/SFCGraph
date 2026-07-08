---
id: UDG@20.15.2@MMLCommand@RMV HTTPLEGRP
type: MMLCommand
name: RMV HTTPLEGRP（删除HTTP本端实体组）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: HTTPLEGRP
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP本端实体组管理
status: active
---

# RMV HTTPLEGRP（删除HTTP本端实体组）

## 功能

该命令用于删除HTTP本端实体组信息。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HTTP本端实体组的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~64。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HTTPLEGRP]] · HTTP本端实体组（HTTPLEGRP）

## 使用实例

若想删除一组索引为1的HTTP本端实体组：

```
RMV HTTPLEGRP: INDEX=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-HTTPLEGRP.md`
