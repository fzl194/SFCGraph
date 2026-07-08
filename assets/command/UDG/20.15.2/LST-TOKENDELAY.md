---
id: UDG@20.15.2@MMLCommand@LST TOKENDELAY
type: MMLCommand
name: LST TOKENDELAY（查询Token延时迁移时间）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TOKENDELAY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- DCF功能管理
- DCF管理
- DCF参数管理
status: active
---

# LST TOKENDELAY（查询Token延时迁移时间）

## 功能

该命令用于查询当前Token延时迁移时间。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/TOKENDELAY]] · Token延时迁移时间（TOKENDELAY）

## 使用实例

查询当前Token延时迁移时间。

```
%%LST TOKENDELAY:;%%
RETCODE = 0  操作成功

结果如下
--------
延时迁移时间(秒) = 0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Token延时迁移时间（LST-TOKENDELAY）_78965049.md`
