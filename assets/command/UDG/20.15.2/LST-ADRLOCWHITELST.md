---
id: UDG@20.15.2@MMLCommand@LST ADRLOCWHITELST
type: MMLCommand
name: LST ADRLOCWHITELST（查询位置区域地址分配用户白名单）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ADRLOCWHITELST
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 位置区域地址分配用户白名单
status: active
---

# LST ADRLOCWHITELST（查询位置区域地址分配用户白名单）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询位置区域分配地址用户白名单。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/ADRLOCWHITELST]] · 位置区域地址分配用户白名单（ADRLOCWHITELST）

## 使用实例

查询位置区域分配地址用户白名单：

```
LST ADRLOCWHITELST:;
```

```

RETCODE = 0  操作成功。

位置区域地址分配白名单
----------------------
MSISDN  =  123456
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询位置区域地址分配用户白名单（LST-ADRLOCWHITELST）_06054825.md`
