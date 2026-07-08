---
id: UNC@20.15.2@ConfigObject@ALLOWEDNFNS
type: ConfigObject
name: ALLOWEDNFNS（NF或NF服务支持的切片）
nf: UNC
version: 20.15.2
object_name: ALLOWEDNFNS
object_kind: entity
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- NCG
status: active
---

# ALLOWEDNFNS（NF或NF服务支持的切片）

## 说明

**适用NF：AMF、SMF、NRF、NSSF、NCG**

该命令用于添加NF实例或NF服务实例所支持的切片信息。当NF实例或NF服务实例只支持为某些切片服务时，需要对支持的切片进行配置。配置后，其他NF只能通过本NF支持的切片来访问本NF的服务实例。

如果仅配置某个NF实例支持的切片，表示该NF实例下的所有服务实例支持的切片相同。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-ALLOWEDNFNS]] · ADD ALLOWEDNFNS
- [[command/UNC/20.15.2/LST-ALLOWEDNFNS]] · LST ALLOWEDNFNS
- [[command/UNC/20.15.2/RMV-ALLOWEDNFNS]] · RMV ALLOWEDNFNS

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NF或NF服务支持的切片（RMV-ALLOWEDNFNS）_09654194.md`
- 原始手册：`evidence/UNC/20.15.2/增加NF或NF服务支持的切片（ADD-ALLOWEDNFNS）_09652539.md`
- 原始手册：`evidence/UNC/20.15.2/查询NF或NF服务支持的切片（LST-ALLOWEDNFNS）_09652600.md`
