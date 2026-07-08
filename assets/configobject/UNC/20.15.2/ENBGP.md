---
id: UNC@20.15.2@ConfigObject@ENBGP
type: ConfigObject
name: ENBGP（eNodeB群组）
nf: UNC
version: 20.15.2
object_name: ENBGP
object_kind: entity
applicable_nf:
- MME
status: active
---

# ENBGP（eNodeB群组）

## 说明

**适用网元：MME**

此命令用于增加eNdoeB群组记录。eNdoeB群组用于定义一组eNdoeB组成的区域，以该区域为粒度进行业务策略控制。需要结合 [**ADD ENBGPMEM**](../eNodeB群组成员管理/增加eNodeB群组成员(ADD ENBGPMEM)_72225289.md) 命令为eNodeB群组添加成员。

## 操作本对象的命令

- [ADD ENBGP](command/UNC/20.15.2/ADD-ENBGP.md)
- [LST ENBGP](command/UNC/20.15.2/LST-ENBGP.md)
- [MOD ENBGP](command/UNC/20.15.2/MOD-ENBGP.md)
- [RMV ENBGP](command/UNC/20.15.2/RMV-ENBGP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改eNodeB群组(MOD-ENBGP)_72225287.md`
- 原始手册：`evidence/UNC/20.15.2/删除eNodeB群组(RMV-ENBGP)_26305418.md`
- 原始手册：`evidence/UNC/20.15.2/增加eNodeB群组(ADD-ENBGP)_26145606.md`
- 原始手册：`evidence/UNC/20.15.2/查询eNodeB群组(LST-ENBGP)_72345205.md`
