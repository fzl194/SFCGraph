---
id: UNC@20.15.2@ConfigObject@GBLOCPORTRGE
type: ConfigObject
name: GBLOCPORTRGE（本端端口号选择范围）
nf: UNC
version: 20.15.2
object_name: GBLOCPORTRGE
object_kind: global_setting
applicable_nf:
- SGSN
status: active
---

# GBLOCPORTRGE（本端端口号选择范围）

## 说明

**适用网元：SGSN**

此命令用于设置自动上报NSE的本端端点选择端口号的范围。

当自动配置的NSE分配本端端点时，如果NSEI值在本配置命令配置的端口范围内并且没有被其他NSE（包括知名端口：3386、2123、2152、4784、53、123、3784、3785、4500）占用，则分配端口号为NSEI。否则从本配置命令配置的端口范围内随机选择一个未被占用的端口号（携带不同ip地址的NSE可以使用同一端口）。新分配的端口使用新的范围配置，对已分配的无影响。

## 操作本对象的命令

- [LST GBLOCPORTRGE](command/UNC/20.15.2/LST-GBLOCPORTRGE.md)
- [SET GBLOCPORTRGE](command/UNC/20.15.2/SET-GBLOCPORTRGE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询本端端口号选择范围(LST-GBLOCPORTRGE)_72225679.md`
- 原始手册：`evidence/UNC/20.15.2/设置本端端口号选择范围(SET-GBLOCPORTRGE)_26146000.md`
