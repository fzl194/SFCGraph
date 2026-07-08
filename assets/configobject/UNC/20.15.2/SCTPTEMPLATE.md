---
id: UNC@20.15.2@ConfigObject@SCTPTEMPLATE
type: ConfigObject
name: SCTPTEMPLATE（SCTP模板）
nf: UNC
version: 20.15.2
object_name: SCTPTEMPLATE
object_kind: entity
applicable_nf:
- PGW-C
- SMF
status: active
---

# SCTPTEMPLATE（SCTP模板）

## 说明

**适用NF：PGW-C、SMF**

此命令用于创建SCTP模板，根据现网规划，当UNC需要使用SCTP承载逻辑接口信令时，可以使用此命令创建SCTP模板并配置SCTP协议参数。

## 操作本对象的命令

- [ADD SCTPTEMPLATE](command/UNC/20.15.2/ADD-SCTPTEMPLATE.md)
- [LST SCTPTEMPLATE](command/UNC/20.15.2/LST-SCTPTEMPLATE.md)
- [MOD SCTPTEMPLATE](command/UNC/20.15.2/MOD-SCTPTEMPLATE.md)
- [RMV SCTPTEMPLATE](command/UNC/20.15.2/RMV-SCTPTEMPLATE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SCTP模板（MOD-SCTPTEMPLATE）_09897333.md`
- 原始手册：`evidence/UNC/20.15.2/删除SCTP模板（RMV-SCTPTEMPLATE）_09897334.md`
- 原始手册：`evidence/UNC/20.15.2/增加SCTP模板（ADD-SCTPTEMPLATE）_09897332.md`
- 原始手册：`evidence/UNC/20.15.2/查询SCTP模板（LST-SCTPTEMPLATE）_09897335.md`
