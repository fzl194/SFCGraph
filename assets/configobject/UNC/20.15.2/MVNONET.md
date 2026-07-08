---
id: UNC@20.15.2@ConfigObject@MVNONET
type: ConfigObject
name: MVNONET（MVNO网络配置信息）
nf: UNC
version: 20.15.2
object_name: MVNONET
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# MVNONET（MVNO网络配置信息）

## 说明

**适用网元：SGSN、MME**

此命令用于增加MVNO的网络配置。 UNC 根据MVNOMCC、MVNOMNC、MATCHIMSI这三个参数及用户的IMSI，判断用户的归属MVNO，为用户提供所属MVNO的服务。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-MVNONET]] · ADD MVNONET
- [[command/UNC/20.15.2/LST-MVNONET]] · LST MVNONET
- [[command/UNC/20.15.2/RMV-MVNONET]] · RMV MVNONET

## 证据

- 原始手册：`evidence/UNC/20.15.2/MVNONET.md`
- 原始手册：`evidence/UNC/20.15.2/MVNONET.md`
- 原始手册：`evidence/UNC/20.15.2/MVNONET.md`
