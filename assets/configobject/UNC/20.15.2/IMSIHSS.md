---
id: UNC@20.15.2@ConfigObject@IMSIHSS
type: ConfigObject
name: IMSIHSS（IMSI-HSS对应关系）
nf: UNC
version: 20.15.2
object_name: IMSIHSS
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# IMSIHSS（IMSI-HSS对应关系）

## 说明

**适用网元：SGSN、MME**

此命令用于增加IMSI（International Mobile Subscriber Identity）与HSS（Home Subscriber Server）的映射关系表记录， UNC 根据IMSI与HSS的映射关系表记录选择IMSI归属的HSS。

## 操作本对象的命令

- [ADD IMSIHSS](command/UNC/20.15.2/ADD-IMSIHSS.md)
- [LST IMSIHSS](command/UNC/20.15.2/LST-IMSIHSS.md)
- [MOD IMSIHSS](command/UNC/20.15.2/MOD-IMSIHSS.md)
- [RMV IMSIHSS](command/UNC/20.15.2/RMV-IMSIHSS.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改IMSI-HSS对应关系(MOD-IMSIHSS)_26305266.md`
- 原始手册：`evidence/UNC/20.15.2/删除IMSI-HSS对应关系(RMV-IMSIHSS)_72225135.md`
- 原始手册：`evidence/UNC/20.15.2/增加IMSI-HSS对应关系(ADD-IMSIHSS)_26145454.md`
- 原始手册：`evidence/UNC/20.15.2/查询IMSI-HSS对应关系(LST-IMSIHSS)_72345053.md`
