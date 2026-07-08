---
id: UNC@20.15.2@ConfigObject@UEUSGTYPEGP
type: ConfigObject
name: UEUSGTYPEGP（UE USAGE TYPE群组）
nf: UNC
version: 20.15.2
object_name: UEUSGTYPEGP
object_kind: entity
applicable_nf:
- MME
status: active
---

# UEUSGTYPEGP（UE USAGE TYPE群组）

## 说明

**适用网元：MME**

该命令增加一条UE USAGE TYPE群组记录，用于在 [**ADD DNSN**](../../../GTP-C接口管理/DNS/DNS NAPTR管理/增加DNS NAPTR记录(ADD DNSN)_72225569.md) 中辅助进行DNS查询。需要结合 [**ADD UEUSGTYPEGPMEM**](../UE USAGE TYPE群组成员管理/增加UE USAGE TYPE群组成员(ADD UEUSGTYPEGPMEM)_26305632.md) 命令为UE USAGE TYPE群组添加成员。

## 操作本对象的命令

- [ADD UEUSGTYPEGP](command/UNC/20.15.2/ADD-UEUSGTYPEGP.md)
- [LST UEUSGTYPEGP](command/UNC/20.15.2/LST-UEUSGTYPEGP.md)
- [MOD UEUSGTYPEGP](command/UNC/20.15.2/MOD-UEUSGTYPEGP.md)
- [RMV UEUSGTYPEGP](command/UNC/20.15.2/RMV-UEUSGTYPEGP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改UE-USAGE-TYPE群组(MOD-UEUSGTYPEGP)_26305630.md`
- 原始手册：`evidence/UNC/20.15.2/删除UE-USAGE-TYPE群组(RMV-UEUSGTYPEGP)_72345421.md`
- 原始手册：`evidence/UNC/20.15.2/增加UE-USAGE-TYPE群组(ADD-UEUSGTYPEGP)_72225499.md`
- 原始手册：`evidence/UNC/20.15.2/查询UE-USAGE-TYPE群组(LST-UEUSGTYPEGP)_26145822.md`
