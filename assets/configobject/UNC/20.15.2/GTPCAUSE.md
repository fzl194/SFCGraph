---
id: UNC@20.15.2@ConfigObject@GTPCAUSE
type: ConfigObject
name: GTPCAUSE（GTP原因值）
nf: UNC
version: 20.15.2
object_name: GTPCAUSE
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# GTPCAUSE（GTP原因值）

## 说明

**适用网元：SGSN、MME**

- 此命令用于增加一条记录，规定了当相应GTP版本消息携带了特定拒绝原因值，将进行P-GW/GGSN重选。
- UNC 在以下流程中根据消息中返回的Cause值及Cause值在该 [表1](#ZH-CN_MMLREF_0000001172225465__table1) 中的配置，判断是否将该P-GW/GGSN进行网元重选流程。
    - E-UTRAN发起的附着流程和UE请求的PDN连接流程，收到S-GW返回的Create Session Response消息，且消息中携带远端(P-GW)带回的特定拒绝原因值。
    - UE发起的PDP一次激活流程，收到GGSN返回的Create PDP Context Response消息。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-GTPCAUSE]] · ADD GTPCAUSE
- [[command/UNC/20.15.2/LST-GTPCAUSE]] · LST GTPCAUSE
- [[command/UNC/20.15.2/RMV-GTPCAUSE]] · RMV GTPCAUSE

## 证据

- 原始手册：`evidence/UNC/20.15.2/GTPCAUSE.md`
- 原始手册：`evidence/UNC/20.15.2/GTPCAUSE.md`
- 原始手册：`evidence/UNC/20.15.2/GTPCAUSE.md`
