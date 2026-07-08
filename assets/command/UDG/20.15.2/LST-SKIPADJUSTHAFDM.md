---
id: UDG@20.15.2@MMLCommand@LST SKIPADJUSTHAFDM
type: MMLCommand
name: LST SKIPADJUSTHAFDM（查询跳过调整HAF域开关状态）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SKIPADJUSTHAFDM
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- NFVI分批升级管理
status: active
---

# LST SKIPADJUSTHAFDM（查询跳过调整HAF域开关状态）

## 功能

该命令用于查询跳过调整HAF域开关状态。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/SKIPADJUSTHAFDM]] · 跳过调整HAF域开关状态（SKIPADJUSTHAFDM）

## 使用实例

查询跳过调整HAF域开关状态。

```
%%LST SKIPADJUSTHAFDM:;%%
RETCODE = 0  操作成功

结果如下
------------------------
开关状态      = 关闭
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询跳过调整HAF域开关状态（LST-SKIPADJUSTHAFDM）_21361336.md`
