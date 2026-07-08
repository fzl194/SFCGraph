---
id: UNC@20.15.2@ConfigObject@SMFPDUREACT
type: ConfigObject
name: SMFPDUREACT（跨区域PDU会话重建策略）
nf: UNC
version: 20.15.2
object_name: SMFPDUREACT
object_kind: entity
applicable_nf:
- SMF
status: active
---

# SMFPDUREACT（跨区域PDU会话重建策略）

## 说明

**适用NF：SMF**

该命令用于增加一条跨区域PDU会话重建策略。UE在网络中移动，可能会出现跨区域漫游场景。增加该配置之后，系统可以针对指定DNN和S-NSSAI的PDU会话，在用户只有缺省QoS Flow的前提下发起PDU会话重建，以便为UE选择本地SMF进行业务。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-SMFPDUREACT]] · ADD SMFPDUREACT
- [[command/UNC/20.15.2/LST-SMFPDUREACT]] · LST SMFPDUREACT
- [[command/UNC/20.15.2/MOD-SMFPDUREACT]] · MOD SMFPDUREACT
- [[command/UNC/20.15.2/RMV-SMFPDUREACT]] · RMV SMFPDUREACT

## 证据

- 原始手册：`evidence/UNC/20.15.2/SMFPDUREACT.md`
- 原始手册：`evidence/UNC/20.15.2/SMFPDUREACT.md`
- 原始手册：`evidence/UNC/20.15.2/SMFPDUREACT.md`
- 原始手册：`evidence/UNC/20.15.2/SMFPDUREACT.md`
