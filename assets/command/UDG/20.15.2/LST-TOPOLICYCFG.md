---
id: UDG@20.15.2@MMLCommand@LST TOPOLICYCFG
type: MMLCommand
name: LST TOPOLICYCFG（查询TCP优化策略配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TOPOLICYCFG
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- TCP优化服务管理
- TCP策略配置
status: active
---

# LST TOPOLICYCFG（查询TCP优化策略配置）

## 功能

**适用NF：UPF**

该命令用于查询TCP优化策略配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/TOPOLICYCFG]] · TCP优化策略配置（TOPOLICYCFG）

## 使用实例

运营商需要查询所有的TCP优化策略配置：

```
LST TOPOLICYCFG:;
```

```

```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询TCP优化策略配置（LST-TOPOLICYCFG）_93335773.md`
