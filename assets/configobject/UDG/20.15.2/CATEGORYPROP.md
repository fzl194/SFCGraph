---
id: UDG@20.15.2@ConfigObject@CATEGORYPROP
type: ConfigObject
name: CATEGORYPROP（分类属性）
nf: UDG
version: 20.15.2
object_name: CATEGORYPROP
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# CATEGORYPROP（分类属性）

## 说明

**适用NF：PGW-U、UPF**

该命令用于配置带宽控制属性，用户进行带宽控制时，通过CATEPROPNAME匹配到相应的带宽控制策略，以完成带宽控制功能，用于关联预定义规则中的过滤条件进行ADC检测上报。

## 操作本对象的命令

- [ADD CATEGORYPROP](command/UDG/20.15.2/ADD-CATEGORYPROP.md)
- [LST CATEGORYPROP](command/UDG/20.15.2/LST-CATEGORYPROP.md)
- [RMV CATEGORYPROP](command/UDG/20.15.2/RMV-CATEGORYPROP.md)

## 关联对象

- [BWMSERVICE](configobject/UDG/20.15.2/BWMSERVICE.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除分类属性（RMV-CATEGORYPROP）_82837505.md`
- 原始手册：`evidence/UDG/20.15.2/增加分类属性（ADD-CATEGORYPROP）_82837504.md`
- 原始手册：`evidence/UDG/20.15.2/查询分类属性（LST-CATEGORYPROP）_82837506.md`
