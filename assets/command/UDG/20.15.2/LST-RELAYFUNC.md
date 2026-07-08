---
id: UDG@20.15.2@MMLCommand@LST RELAYFUNC
type: MMLCommand
name: LST RELAYFUNC（查询媒体中继功能配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RELAYFUNC
command_category: 查询类
applicable_nf:
- UPF
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继功能
status: active
---

# LST RELAYFUNC（查询媒体中继功能配置）

## 功能

**适用NF：UPF、PGW-U**

该命令用于查询媒体中继功能配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/RELAYFUNC]] · 媒体中继功能配置（RELAYFUNC）

## 使用实例

查询媒体中继功能配置：

```
LST RELAYFUNC:;
```

```

RETCODE = 0  操作成功

媒体中继功能配置
-----------------------------
媒体中继功能开关  =  禁用
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询媒体中继功能配置（LST-RELAYFUNC）_14541477.md`
