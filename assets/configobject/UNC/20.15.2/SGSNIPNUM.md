---
id: UNC@20.15.2@ConfigObject@SGSNIPNUM
type: ConfigObject
name: SGSNIPNUM（SGSN控制面IP地址与SGSN号码对应关系）
nf: UNC
version: 20.15.2
object_name: SGSNIPNUM
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# SGSNIPNUM（SGSN控制面IP地址与SGSN号码对应关系）

## 说明

**适用网元：SGSN**

此命令用于增加SGSN控制面IP地址与SGSN号码的对照关系。在延迟定位过程中，当用户在其它SGSN重现时，需要根据用户所重现的SGSN IP地址来获得该SGSN号码，并在SGSN给GMLC的上报消息中携带此SGSN号码传送给GMLC，使得GMLC能根据此SGSN号码向用户重现的SGSN重新发起定位流程。如果该表中没有配置该SGSN的IP地址与SGSN号码的对照关系，则SGSN给GMLC的上报消息中不携带SGSN号码，GMLC向HLR查询用户当前附着的SGSN号码，然后GMLC根据从HLR获得的SGSN号码向用户重现的SGSN重新发起定位流程。

## 操作本对象的命令

- [ADD SGSNIPNUM](command/UNC/20.15.2/ADD-SGSNIPNUM.md)
- [LST SGSNIPNUM](command/UNC/20.15.2/LST-SGSNIPNUM.md)
- [MOD SGSNIPNUM](command/UNC/20.15.2/MOD-SGSNIPNUM.md)
- [RMV SGSNIPNUM](command/UNC/20.15.2/RMV-SGSNIPNUM.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SGSN控制面IP地址与SGSN号码对应关系(MOD-SGSNIPNUM)_26145806.md`
- 原始手册：`evidence/UNC/20.15.2/删除SGSN控制面IP地址与SGSN号码对应关系(RMV-SGSNIPNUM)_72345405.md`
- 原始手册：`evidence/UNC/20.15.2/增加SGSN控制面IP地址与SGSN号码对应关系(ADD-SGSNIPNUM)_26305614.md`
- 原始手册：`evidence/UNC/20.15.2/查询SGSN控制面IP地址与SGSN号码对应关系(LST-SGSNIPNUM)_72225485.md`
