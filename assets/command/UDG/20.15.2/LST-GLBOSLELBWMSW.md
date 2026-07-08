---
id: UDG@20.15.2@MMLCommand@LST GLBOSLELBWMSW
type: MMLCommand
name: LST GLBOSLELBWMSW（查询整机操作系统级带宽管理开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: GLBOSLELBWMSW
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 带宽控制
- 整机操作系统级带宽管理
status: active
---

# LST GLBOSLELBWMSW（查询整机操作系统级带宽管理开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查询整机操作系统级带宽管理开关。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@GLBOSLELBWMSW]] · 整机操作系统级带宽管理开关（GLBOSLELBWMSW）

## 使用实例

查询整机操作系统级带宽管理开关信息：

```
LST GLBOSLELBWMSW:;
```

```

RETCODE = 0 Operation Success.

Global OS Level Bandwidth Managament Switch Information
--------------------------------------------------------------------------------
 Global OS Level Bandwidth Managament Switch = ENABLE
(Number of results = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-GLBOSLELBWMSW.md`
