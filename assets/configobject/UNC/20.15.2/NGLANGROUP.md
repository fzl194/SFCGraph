---
id: UNC@20.15.2@ConfigObject@NGLANGROUP
type: ConfigObject
name: NGLANGROUP（5G LAN群组）
nf: UNC
version: 20.15.2
object_name: NGLANGROUP
object_kind: entity
applicable_nf:
- SMF
status: active
---

# NGLANGROUP（5G LAN群组）

## 说明

**适用NF：SMF**

该命令用于增加5G LAN群组。在PDU激活流程中，SMF会根据DNN、切片和PDUSessionType等信息，判断该会话是否属于一个5G LAN群组。如果是，按5G LAN PDU激活流程进行处理；如果否，按正常PDU会话流程进行处理。

## 操作本对象的命令

- [ADD NGLANGROUP](command/UNC/20.15.2/ADD-NGLANGROUP.md)
- [LST NGLANGROUP](command/UNC/20.15.2/LST-NGLANGROUP.md)
- [MOD NGLANGROUP](command/UNC/20.15.2/MOD-NGLANGROUP.md)
- [RMV NGLANGROUP](command/UNC/20.15.2/RMV-NGLANGROUP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改5G-LAN群组（MOD-NGLANGROUP）_04284719.md`
- 原始手册：`evidence/UNC/20.15.2/删除5G-LAN群组（RMV-NGLANGROUP）_04284722.md`
- 原始手册：`evidence/UNC/20.15.2/增加5G-LAN群组（ADD-NGLANGROUP）_04284708.md`
- 原始手册：`evidence/UNC/20.15.2/查询5G-LAN群组（LST-NGLANGROUP）_04284714.md`
