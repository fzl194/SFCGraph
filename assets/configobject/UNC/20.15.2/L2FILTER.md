---
id: UNC@20.15.2@ConfigObject@L2FILTER
type: ConfigObject
name: L2FILTER（层二过滤器）
nf: UNC
version: 20.15.2
object_name: L2FILTER
object_kind: entity
applicable_nf:
- SMF
status: active
---

# L2FILTER（层二过滤器）

## 说明

**适用NF：SMF**

该命令用于添加层二过滤器。在以太网会话流程中，SMF将层二过滤器下发给UE侧，UE侧基于层二过滤器配置的参数匹配数据包并执行相应的动作。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-L2FILTER]] · ADD L2FILTER
- [[command/UNC/20.15.2/LST-L2FILTER]] · LST L2FILTER
- [[command/UNC/20.15.2/MOD-L2FILTER]] · MOD L2FILTER
- [[command/UNC/20.15.2/RMV-L2FILTER]] · RMV L2FILTER

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改层二过滤器（MOD-L2FILTER）_23622974.md`
- 原始手册：`evidence/UNC/20.15.2/删除层二过滤器（RMV-L2FILTER）_23622994.md`
- 原始手册：`evidence/UNC/20.15.2/增加层二过滤器（ADD-L2FILTER）_23782722.md`
- 原始手册：`evidence/UNC/20.15.2/查询层二过滤器（LST-L2FILTER）_70462541.md`
