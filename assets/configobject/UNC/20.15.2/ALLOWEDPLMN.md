---
id: UNC@20.15.2@ConfigObject@ALLOWEDPLMN
type: ConfigObject
name: ALLOWEDPLMN（NF或NF服务支持的PLMN）
nf: UNC
version: 20.15.2
object_name: ALLOWEDPLMN
object_kind: entity
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- NCG
status: active
---

# ALLOWEDPLMN（NF或NF服务支持的PLMN）

## 说明

**适用NF：AMF、SMF、NRF、NSSF、NCG**

该命令用于添加NF实例或NF服务实例所支持的PLMN。当NF实例或NF服务实例只支持为某些PLMN服务时，需要对支持的PLMN进行配置。配置后，其他NF只能通过本NF支持的PLMN来访问本NF的服务实例。

如果仅配置某个NF实例支持的PLMN，表示该NF实例下的所有服务实例支持的PLMN相同。

## 操作本对象的命令

- [ADD ALLOWEDPLMN](command/UNC/20.15.2/ADD-ALLOWEDPLMN.md)
- [LST ALLOWEDPLMN](command/UNC/20.15.2/LST-ALLOWEDPLMN.md)
- [RMV ALLOWEDPLMN](command/UNC/20.15.2/RMV-ALLOWEDPLMN.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NF或NF服务支持的PLMN（RMV-ALLOWEDPLMN）_09652389.md`
- 原始手册：`evidence/UNC/20.15.2/增加NF或NF服务支持的PLMN（ADD-ALLOWEDPLMN）_09652458.md`
- 原始手册：`evidence/UNC/20.15.2/查询NF或NF服务支持的PLMN（LST-ALLOWEDPLMN）_09653265.md`
