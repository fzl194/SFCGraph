---
id: UNC@20.15.2@ConfigObject@GBACCAREALST
type: ConfigObject
name: GBACCAREALST（Gb模式区域漫游限制参数）
nf: UNC
version: 20.15.2
object_name: GBACCAREALST
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# GBACCAREALST（Gb模式区域漫游限制参数）

## 说明

![](增加Gb模式区域漫游限制参数（ADD GBACCAREALST）_72345149.assets/notice_3.0-zh-cn_2.png)

- 执行该命令可能会导致用户接入异常，请谨慎操作。
- 参数（控制类型）：为防止误操作产生的业务影响，请确认命令中各参数取值合理有效。

**适用网元：SGSN**

该命令用于增加Gb模式区域漫游限制参数，根据用户当前所在的位置，控制是否允许进行漫游。

当针对不同的用户群在相应的区域群中设置对应的漫游控制策略时，需要执行此命令。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-GBACCAREALST]] · ADD GBACCAREALST
- [[command/UNC/20.15.2/LST-GBACCAREALST]] · LST GBACCAREALST
- [[command/UNC/20.15.2/RMV-GBACCAREALST]] · RMV GBACCAREALST

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Gb模式区域漫游限制参数(RMV-GBACCAREALST)_26145552.md`
- 原始手册：`evidence/UNC/20.15.2/增加Gb模式区域漫游限制参数（ADD-GBACCAREALST）_72345149.md`
- 原始手册：`evidence/UNC/20.15.2/查询Gb模式区域漫游限制参数(LST-GBACCAREALST)_72225233.md`
