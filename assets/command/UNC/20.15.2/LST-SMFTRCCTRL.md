---
id: UNC@20.15.2@MMLCommand@LST SMFTRCCTRL
type: MMLCommand
name: LST SMFTRCCTRL（查询SMF跟踪控制功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFTRCCTRL
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 扩展调测
- OM调测
status: active
---

# LST SMFTRCCTRL（查询SMF跟踪控制功能）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询SMF跟踪功能控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFTRCCTRL]] · SMF跟踪控制功能（SMFTRCCTRL）

## 使用实例

查询SMF跟踪控制功能，执行如下命令：

```
LST SMFTRCCTRL:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMFTRCCTRL.md`
