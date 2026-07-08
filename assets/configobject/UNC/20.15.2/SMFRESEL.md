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

- 原始手册：`evidence/UNC/20.15.2/修改本地SMF重选策略（MOD-SMFRESEL）_45495625.md`
- 原始手册：`evidence/UNC/20.15.2/删除本地SMF重选策略（RMV-SMFRESEL）_45495626.md`
- 原始手册：`evidence/UNC/20.15.2/增加本地SMF重选策略（ADD-SMFRESEL）_45495622.md`
- 原始手册：`evidence/UNC/20.15.2/查询本地SMF重选策略（LST-SMFRESEL）_45495624.md`
