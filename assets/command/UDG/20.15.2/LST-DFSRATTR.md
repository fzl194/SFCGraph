---
id: UDG@20.15.2@MMLCommand@LST DFSRATTR
type: MMLCommand
name: LST DFSRATTR（查询双发选收属性配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DFSRATTR
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN双发选收配置
- 双发选收属性配置
status: active
---

# LST DFSRATTR（查询双发选收属性配置）

## 功能

**适用NF：UPF**

该命令用于查询双发选收相关的属性信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@DFSRATTR]] · 双发选收属性配置（DFSRATTR）

## 使用实例

查询该网元双发选收相关的属性信息：

```
LST DFSRATTR:;
```

```

```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-DFSRATTR.md`
