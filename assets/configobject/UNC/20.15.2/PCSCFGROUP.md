---
id: UNC@20.15.2@ConfigObject@PCSCFGROUP
type: ConfigObject
name: PCSCFGROUP（P-CSCF组配置）
nf: UNC
version: 20.15.2
object_name: PCSCFGROUP
object_kind: entity
applicable_nf:
- PGW-C
- SMF
- GGSN
status: active
---

# PCSCFGROUP（P-CSCF组配置）

## 说明

**适用NF：PGW-C、SMF、GGSN**

该命令用于增加P-CSCF组配置。在规划IMS网络，配置P-CSCF服务器地址时，需要先执行该命令配置P-CSCF组。当P-CSCF服务器地址由DHCP服务器分配时，用户具体使用DHCP P-CSCF分组中的哪个P-CSCF地址由用户激活时外置DHCP服务器返回的响应消息决定。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PCSCFGROUP]] · ADD PCSCFGROUP
- [[command/UNC/20.15.2/LST-PCSCFGROUP]] · LST PCSCFGROUP
- [[command/UNC/20.15.2/RMV-PCSCFGROUP]] · RMV PCSCFGROUP

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除P-CSCF组配置（RMV-PCSCFGROUP）_09651437.md`
- 原始手册：`evidence/UNC/20.15.2/增加P-CSCF组配置（ADD-PCSCFGROUP）_09653619.md`
- 原始手册：`evidence/UNC/20.15.2/查询P-CSCF组配置（LST-PCSCFGROUP）_09654405.md`
