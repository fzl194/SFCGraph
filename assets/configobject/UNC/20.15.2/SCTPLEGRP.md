---
id: UNC@20.15.2@ConfigObject@SCTPLEGRP
type: ConfigObject
name: SCTPLEGRP（SCTP本地实体组）
nf: UNC
version: 20.15.2
object_name: SCTPLEGRP
object_kind: entity
applicable_nf:
- MME
- AMF
status: active
---

# SCTPLEGRP（SCTP本地实体组）

## 说明

**适用网元：MME、AMF**

本命令用于添加SCTP本端实体组。5G基站(NG RAN)支持多偶联接入，添加SCTP本端实体组用于将多个SCTP本端实体绑定，从而实现多偶联。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-SCTPLEGRP]] · ADD SCTPLEGRP
- [[command/UNC/20.15.2/LST-SCTPLEGRP]] · LST SCTPLEGRP
- [[command/UNC/20.15.2/RMV-SCTPLEGRP]] · RMV SCTPLEGRP

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SCTP本地实体组(RMV-SCTPLEGRP)_19187105.md`
- 原始手册：`evidence/UNC/20.15.2/增加SCTP本地实体组(ADD-SCTPLEGRP)_19186931.md`
- 原始手册：`evidence/UNC/20.15.2/查询SCTP本地实体组(LST-SCTPLEGRP)_19187146.md`
