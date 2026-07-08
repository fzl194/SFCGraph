---
id: UNC@20.15.2@ConfigObject@SCTPLE
type: ConfigObject
name: SCTPLE（SCTP本地实体）
nf: UNC
version: 20.15.2
object_name: SCTPLE
object_kind: entity
applicable_nf:
- MME
- AMF
status: active
---

# SCTPLE（SCTP本地实体）

## 说明

**适用网元：MME、AMF**

此命令用于添加基于IP的宽带信令SCTP(Stream Control Transmission Protocol)偶联的本端信息，SCTP偶联是两个SCTP端点通过SCTP协议规定的4步握手机制建立起来的进行数据传递的逻辑联系或者通道。本命令中配置的是SCTP偶联的两个端点中的本端。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-SCTPLE]] · ADD SCTPLE
- [[command/UNC/20.15.2/LST-SCTPLE]] · LST SCTPLE
- [[command/UNC/20.15.2/MOD-SCTPLE]] · MOD SCTPLE
- [[command/UNC/20.15.2/RMV-SCTPLE]] · RMV SCTPLE

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SCTP本地实体(MOD-SCTPLE)_11295829.md`
- 原始手册：`evidence/UNC/20.15.2/删除SCTP本地实体(RMV-SCTPLE)_11295837.md`
- 原始手册：`evidence/UNC/20.15.2/增加SCTP本地实体(ADD-SCTPLE)_11295747.md`
- 原始手册：`evidence/UNC/20.15.2/查询SCTP本地实体(LST-SCTPLE)_11295784.md`
