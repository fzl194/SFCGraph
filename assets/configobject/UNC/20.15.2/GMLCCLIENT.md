---
id: UNC@20.15.2@ConfigObject@GMLCCLIENT
type: ConfigObject
name: GMLCCLIENT（GMLC和LCS Client对照关系）
nf: UNC
version: 20.15.2
object_name: GMLCCLIENT
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# GMLCCLIENT（GMLC和LCS Client对照关系）

## 说明

**适用网元：SGSN**

此命令用于增加GMLC和LCS CLIENT的对照关系。在移动始发的位置业务中，SGSN根据手机发送信息中携带的LCS CLIENT信息，查询此表，获得对应的GMLC。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-GMLCCLIENT]] · ADD GMLCCLIENT
- [[command/UNC/20.15.2/LST-GMLCCLIENT]] · LST GMLCCLIENT
- [[command/UNC/20.15.2/MOD-GMLCCLIENT]] · MOD GMLCCLIENT
- [[command/UNC/20.15.2/RMV-GMLCCLIENT]] · RMV GMLCCLIENT

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改GMLC和LCS-Client对照关系(MOD-GMLCCLIENT)_72345403.md`
- 原始手册：`evidence/UNC/20.15.2/删除GMLC和LCS-Client对照关系(RMV-GMLCCLIENT)_26305612.md`
- 原始手册：`evidence/UNC/20.15.2/增加GMLC和LCS-Client对照关系(ADD-GMLCCLIENT)_72225481.md`
- 原始手册：`evidence/UNC/20.15.2/查询GMLC和LCS-Client对照关系(LST-GMLCCLIENT)_26145804.md`
