---
id: UNC@20.15.2@ConfigObject@ALLOWEDNFDOMAIN
type: ConfigObject
name: ALLOWEDNFDOMAIN（NF或NF服务支持的域名）
nf: UNC
version: 20.15.2
object_name: ALLOWEDNFDOMAIN
object_kind: entity
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- NCG
status: active
---

# ALLOWEDNFDOMAIN（NF或NF服务支持的域名）

## 说明

**适用NF：AMF、SMF、NRF、NSSF、NCG**

该命令用于添加NF实例或NF服务实例所支持的域名。当NF实例或NF服务实例只支持为某些域名服务时，需要对支持的域名进行配置。配置后，其他NF只能通过本NF支持的域名来访问本NF的服务实例。

如果仅配置某个NF实例支持的域名，表示该NF实例下的所有服务实例支持的域名相同。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-ALLOWEDNFDOMAIN]] · ADD ALLOWEDNFDOMAIN
- [[command/UNC/20.15.2/LST-ALLOWEDNFDOMAIN]] · LST ALLOWEDNFDOMAIN
- [[command/UNC/20.15.2/RMV-ALLOWEDNFDOMAIN]] · RMV ALLOWEDNFDOMAIN

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NF或NF服务支持的域名（RMV-ALLOWEDNFDOMAIN）_09651481.md`
- 原始手册：`evidence/UNC/20.15.2/增加NF或NF服务支持的域名（ADD-ALLOWEDNFDOMAIN）_09651550.md`
- 原始手册：`evidence/UNC/20.15.2/查询NF或NF服务支持的域名（LST-ALLOWEDNFDOMAIN）_09653662.md`
