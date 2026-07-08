---
id: UNC@20.15.2@MMLCommand@DSP SMARTFCDURA
type: MMLCommand
name: DSP SMARTFCDURA（显示智能流控开启时长）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SMARTFCDURA
command_category: 查询类
applicable_nf:
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 流控管理
- 信令抑制
status: active
---

# DSP SMARTFCDURA（显示智能流控开启时长）

## 功能

**适用NF：PGW-C**

该命令用于查询智能流控功能的定时开启时长。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMARTFCDURA]] · 智能流控开启时长（SMARTFCDURA）

## 使用实例

查询智能流控定时时长。

```
DSP SMARTFCDURA:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示智能流控开启时长（DSP-SMARTFCDURA）_10605248.md`
