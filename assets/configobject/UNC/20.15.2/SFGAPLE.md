---
id: UNC@20.15.2@ConfigObject@SFGAPLE
type: ConfigObject
name: SFGAPLE（SFGAP本端实体）
nf: UNC
version: 20.15.2
object_name: SFGAPLE
object_kind: entity
applicable_nf:
- AMF
status: active
---

# SFGAPLE（SFGAP本端实体）

## 说明

**适用NF：AMF**

在部署感知的场景下，通过ADD SFGAPLE增加SFGAP本端实体，AMF可以通过SFGAP本端实体和感知gNodeB完成链路建立，并实现感知gNodeB接入到AMF。一个SFGAP本端实体可引用一个SCTP本端实体组，一个SCTP本端实体组下最多可配置32个SCTP本端实体。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-SFGAPLE]] · ADD SFGAPLE
- [[command/UNC/20.15.2/LST-SFGAPLE]] · LST SFGAPLE
- [[command/UNC/20.15.2/RMV-SFGAPLE]] · RMV SFGAPLE

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SFGAP本端实体（RMV-SFGAPLE）_75982872.md`
- 原始手册：`evidence/UNC/20.15.2/增加SFGAP本端实体（ADD-SFGAPLE）_75822964.md`
- 原始手册：`evidence/UNC/20.15.2/查询SFGAP本端实体（LST-SFGAPLE）_75822980.md`
