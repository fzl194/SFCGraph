---
id: UNC@20.15.2@ConfigObject@LAIVLRBLACKLIST
type: ConfigObject
name: LAIVLRBLACKLIST（LAIVLR黑名单）
nf: UNC
version: 20.15.2
object_name: LAIVLRBLACKLIST
object_kind: entity
applicable_nf:
- MME
status: active
---

# LAIVLRBLACKLIST（LAIVLR黑名单）

## 说明

**适用网元：MME**

该命令用于MSC POOL场景下，当BSC与某个或多个MSC连接中断但与其它MSC连接正常时，增加LAI与MSC/VLR的黑名单对应关系。 UNC 选择黑名单以外MSC POOL内的其它正常MSC/VLR进行服务。

## 操作本对象的命令

- [ADD LAIVLRBLACKLIST](command/UNC/20.15.2/ADD-LAIVLRBLACKLIST.md)
- [LST LAIVLRBLACKLIST](command/UNC/20.15.2/LST-LAIVLRBLACKLIST.md)
- [RMV LAIVLRBLACKLIST](command/UNC/20.15.2/RMV-LAIVLRBLACKLIST.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除LAIVLR黑名单(RMV-LAIVLRBLACKLIST)_72345025.md`
- 原始手册：`evidence/UNC/20.15.2/增加LAIVLR黑名单(ADD-LAIVLRBLACKLIST)_26305238.md`
- 原始手册：`evidence/UNC/20.15.2/查询LAIVLR黑名单(LST-LAIVLRBLACKLIST)_26145424.md`
