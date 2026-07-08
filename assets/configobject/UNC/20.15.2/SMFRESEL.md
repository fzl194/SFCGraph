---
id: UNC@20.15.2@ConfigObject@SMFRESEL
type: ConfigObject
name: SMFRESEL（本地SMF重选策略）
nf: UNC
version: 20.15.2
object_name: SMFRESEL
object_kind: entity
applicable_nf:
- AMF
status: active
---

# SMFRESEL（本地SMF重选策略）

## 说明

**适用NF：AMF**

该命令用于增加一条本地SMF重选策略的配置记录。UE在网络在中移动，可能造成SMF与AMF不属于同一区域。增加该配置后，系统可以针对指定DNN和S-NSSAI的PDU会话，在用户处于空闲态的前提下，为UE重新选择和AMF在同一区域的本地SMF进行业务。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-SMFRESEL]] · ADD SMFRESEL
- [[command/UNC/20.15.2/LST-SMFRESEL]] · LST SMFRESEL
- [[command/UNC/20.15.2/MOD-SMFRESEL]] · MOD SMFRESEL
- [[command/UNC/20.15.2/RMV-SMFRESEL]] · RMV SMFRESEL

## 证据

- 原始手册：`evidence/UNC/20.15.2/SMFRESEL.md`
- 原始手册：`evidence/UNC/20.15.2/SMFRESEL.md`
- 原始手册：`evidence/UNC/20.15.2/SMFRESEL.md`
- 原始手册：`evidence/UNC/20.15.2/SMFRESEL.md`
