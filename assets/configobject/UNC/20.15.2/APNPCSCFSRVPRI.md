---
id: UNC@20.15.2@ConfigObject@APNPCSCFSRVPRI
type: ConfigObject
name: APNPCSCFSRVPRI（APN P-CSCF地址获取方式的优先级配置）
nf: UNC
version: 20.15.2
object_name: APNPCSCFSRVPRI
object_kind: global_setting
applicable_nf:
- PGW-C
status: active
---

# APNPCSCFSRVPRI（APN P-CSCF地址获取方式的优先级配置）

## 说明

**适用NF：PGW-C**

该命令用来配置获取P-CSCF方式的优先级，当用户既从DHCP服务器获取了P-CSCF地址，本地也配置了P-CSCF地址时，通过此命令配置本地P-CSCF地址优先或DHCP P-CSCF地址优先。

## 操作本对象的命令

- [LST APNPCSCFSRVPRI](command/UNC/20.15.2/LST-APNPCSCFSRVPRI.md)
- [SET APNPCSCFSRVPRI](command/UNC/20.15.2/SET-APNPCSCFSRVPRI.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APN-P-CSCF地址获取方式的优先级配置（LST-APNPCSCFSRVPRI）_09653843.md`
- 原始手册：`evidence/UNC/20.15.2/设置APN-P-CSCF地址获取方式的优先级配置（SET-APNPCSCFSRVPRI）_33845577.md`
