---
id: UDG@20.15.2@MMLCommand@LST HTTPUPGSTAGE
type: MMLCommand
name: LST HTTPUPGSTAGE（查询HTTP灰度升级状态）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HTTPUPGSTAGE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP平台管理
status: active
---

# LST HTTPUPGSTAGE（查询HTTP灰度升级状态）

## 功能

该命令用于查询HTTP灰度升级状态。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [HTTP灰度升级状态（HTTPUPGSTAGE）](configobject/UDG/20.15.2/HTTPUPGSTAGE.md)

## 使用实例

查询HTTP灰度升级状态，执行如下命令：

```
%%LST HTTPUPGSTAGE:;%%
RETCODE = 0  操作成功

结果如下
------------------------
灰度升级状态 = 稳态
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询HTTP灰度升级状态（LST-HTTPUPGSTAGE）_31559911.md`
