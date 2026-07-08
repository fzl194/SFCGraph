---
id: UDG@20.15.2@MMLCommand@LST DRAUTOACTIVE
type: MMLCommand
name: LST DRAUTOACTIVE（查询冷备容灾自动升主功能参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DRAUTOACTIVE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST DRAUTOACTIVE（查询冷备容灾自动升主功能参数）

## 功能

该命令用于查询冷备容灾自动升主功能参数。

> **说明**
> - 此命令只在冷备容灾模式下生效。
> - 此命令只能在配置主网元执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [冷备容灾自动升主功能参数（DRAUTOACTIVE）](configobject/UDG/20.15.2/DRAUTOACTIVE.md)

## 使用实例

查询冷备容灾自动升主功能参数：

```
%%LST DRAUTOACTIVE:;%%
RETCODE = 0  操作成功

结果如下
--------
                          是否自动升主  =  是
运行备升为运行主所需的持续时间（分钟）  =  15
        配置不自动升主容忍时间（分钟）  =  60
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询冷备容灾自动升主功能参数（LST-DRAUTOACTIVE）_74494005.md`
