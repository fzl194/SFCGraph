---
id: UDG@20.15.2@MMLCommand@LST PODHEALCTRL
type: MMLCommand
name: LST PODHEALCTRL（查询自愈功能配置信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PODHEALCTRL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST PODHEALCTRL（查询自愈功能配置信息）

## 功能

该命令用于显示自愈功能配置信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PODHEALCTRL]] · 自愈功能配置信息（PODHEALCTRL）

## 使用实例

显示自愈功能配置信息。

```
%%LST PODHEALCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
自愈开关  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-PODHEALCTRL.md`
