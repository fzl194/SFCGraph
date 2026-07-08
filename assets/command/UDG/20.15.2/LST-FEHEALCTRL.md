---
id: UDG@20.15.2@MMLCommand@LST FEHEALCTRL
type: MMLCommand
name: LST FEHEALCTRL（查询FE自愈功能配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FEHEALCTRL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- FEMF
status: active
---

# LST FEHEALCTRL（查询FE自愈功能配置）

## 功能

该命令用于查询FE自愈功能配置：包括Mesh网口故障自愈功能开关和FE服务丢失心跳自愈开关。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/FEHEALCTRL]] · FE自愈功能配置（FEHEALCTRL）

## 使用实例

查询FE自愈功能配置

```
LST FEHEALCTRL:;
RETCODE = 0  操作成功

结果如下
--------
Mesh网口故障自愈功能开关  =  使能
  FE服务丢失心跳自愈开关  =  使能
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-FEHEALCTRL.md`
