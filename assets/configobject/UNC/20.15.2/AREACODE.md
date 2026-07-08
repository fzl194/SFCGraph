---
id: UNC@20.15.2@ConfigObject@AREACODE
type: ConfigObject
name: AREACODE（区域编码）
nf: UNC
version: 20.15.2
object_name: AREACODE
object_kind: entity
applicable_nf:
- AMF
status: active
---

# AREACODE（区域编码）

## 说明

**适用NF：AMF**

AMF可基于运营商规划的区域做差异化控制（比如用户接入控制）。AMF配置上述“区域”分为两个步骤，首先是定义区域编码（AreaCode），其次是为已定义的区域编码添加位置成员。本命令用于在AMF上增加区域编码。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-AREACODE]] · ADD AREACODE
- [[command/UNC/20.15.2/LST-AREACODE]] · LST AREACODE
- [[command/UNC/20.15.2/RMV-AREACODE]] · RMV AREACODE

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除区域编码（RMV-AREACODE）_44007539.md`
- 原始手册：`evidence/UNC/20.15.2/增加区域编码（ADD-AREACODE）_44006351.md`
- 原始手册：`evidence/UNC/20.15.2/查询区域编码（LST-AREACODE）_44006821.md`
