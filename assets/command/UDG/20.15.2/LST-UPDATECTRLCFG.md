---
id: UDG@20.15.2@MMLCommand@LST UPDATECTRLCFG
type: MMLCommand
name: LST UPDATECTRLCFG（查询内部升级配置表）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPDATECTRLCFG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP平台管理
status: active
---

# LST UPDATECTRLCFG（查询内部升级配置表）

## 功能

该命令用于查询内部升级配置表。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPDATECTRLCFG]] · 内部升级配置表（UPDATECTRLCFG）

## 使用实例

查询内部升级配置表，执行如下命令：

```
%%LST UPDATECTRLCFG:;%%
RETCODE = 0  操作成功

结果如下
------------------------
升级状态 = 0
低版本号 = 0
高版本号 = 100
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询内部升级配置表（LST-UPDATECTRLCFG）_38848818.md`
