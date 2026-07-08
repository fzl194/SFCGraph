---
id: UDG@20.15.2@MMLCommand@DSP PAESWITCH
type: MMLCommand
name: DSP PAESWITCH（显示PAE开关信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PAESWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 资源管理
status: active
---

# DSP PAESWITCH（显示PAE开关信息）

## 功能

该命令用于查询PAE配置信息开关。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/PAESWITCH]] · PAE开关信息（PAESWITCH）

## 使用实例

显示PAE开关配置。

```
%%DSP PAESWITCH:;%%
RETCODE = 0  操作成功

结果如下
--------
PAE隔离核统计开关 =  去除PAE隔离核
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示PAE开关信息（DSP-PAESWITCH）_31405490.md`
