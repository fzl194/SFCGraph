---
id: UNC@20.15.2@ConfigObject@RULEBINDDNAI
type: ConfigObject
name: RULEBINDDNAI（预定义规则关联的DNAI）
nf: UNC
version: 20.15.2
object_name: RULEBINDDNAI
object_kind: binding
applicable_nf:
- SMF
- PGW-C
- GGSN
status: active
---

# RULEBINDDNAI（预定义规则关联的DNAI）

## 说明

**适用NF：SMF、PGW-C、GGSN**

该命令用于增加预定义规则关联的DNAI。

当需要指定预定义规则下发某边缘UPF时，可通过本命令绑定Rule和边缘UPF的DNAI的对应关系来实现。

当一个预定义规则绑定到某边缘UPF所对应的DNAI时，该预定义相关规则就只下发给该边缘UPF。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-RULEBINDDNAI]] · ADD RULEBINDDNAI
- [[command/UNC/20.15.2/LST-RULEBINDDNAI]] · LST RULEBINDDNAI
- [[command/UNC/20.15.2/RMV-RULEBINDDNAI]] · RMV RULEBINDDNAI

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除预定义规则关联的DNAI（RMV-RULEBINDDNAI）_26931973.md`
- 原始手册：`evidence/UNC/20.15.2/增加预定义规则关联的DNAI（ADD-RULEBINDDNAI）_27170471.md`
- 原始手册：`evidence/UNC/20.15.2/查询预定义规则关联的DNAI（LST-RULEBINDDNAI）_26850415.md`
