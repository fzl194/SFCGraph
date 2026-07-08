---
id: UDG@20.15.2@MMLCommand@LST MSETCDTTL
type: MMLCommand
name: LST MSETCDTTL（查询租约时长）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MSETCDTTL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST MSETCDTTL（查询租约时长）

## 功能

该命令用于查询租约时长。

> **说明**
> 无

## 权限

G_1，管理员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/MSETCDTTL]] · 租约时长（MSETCDTTL）

## 使用实例

查询租约时长

```
LST MSETCDTTL;
RETCODE = 0  操作成功

结果如下
------------------------
租约时长  =  3
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-MSETCDTTL.md`
