---
id: UDG@20.15.2@MMLCommand@LST HTTPRESCFG
type: MMLCommand
name: LST HTTPRESCFG（查询HTTP资源流控门限）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HTTPRESCFG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP流控管理
- HTTP资源流控管理
status: active
---

# LST HTTPRESCFG（查询HTTP资源流控门限）

## 功能

该命令用于查询HTTP资源流控门限信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | HTTP资源门限索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HTTP资源门限的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~4096。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [HTTP资源流控门限（HTTPRESCFG）](configobject/UDG/20.15.2/HTTPRESCFG.md)

## 使用实例

查询所有HTTP资源流控门限信息，可以用如下命令；

```
%%LST HTTPRESCFG:;%%
RETCODE = 0  操作成功

结果如下
------------------------
HTTP资源门限索引           资源类型       本端实体类型      对端IP地址类型  对端IPV4地址    对端IPV6地址       资源门限

1                           REQCB          Client             IPv4 Address  192.168.2.1        ::                 100
2                           REQCB          Server             IPv4 Address  192.168.2.1        ::                 100
3                           REQCB          Client             IPv4 Address  192.168.1.1        ::                 100
(结果个数 = 3)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询HTTP资源流控门限（LST-HTTPRESCFG）_01384194.md`
