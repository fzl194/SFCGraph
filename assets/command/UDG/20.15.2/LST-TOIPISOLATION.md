---
id: UDG@20.15.2@MMLCommand@LST TOIPISOLATION
type: MMLCommand
name: LST TOIPISOLATION（查询IP地址隔离功能配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TOIPISOLATION
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- TCP优化服务管理
- IP地址隔离功能
status: active
---

# LST TOIPISOLATION（查询IP地址隔离功能配置）

## 功能

**适用NF：UPF**

该命令用于查询IP地址隔离功能配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/TOIPISOLATION]] · IP地址隔离功能配置（TOIPISOLATION）

## 使用实例

查询IP地址隔离功能配置：

```
LST TOIPISOLATION:;
```

```

RETCODE = 0  操作成功

IP地址隔离配置
-------------
IP地址隔离功能开关  =  ENABLE
(结果个数 = 1)

--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-TOIPISOLATION.md`
