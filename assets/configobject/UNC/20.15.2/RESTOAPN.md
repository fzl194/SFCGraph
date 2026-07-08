---
id: UNC@20.15.2@ConfigObject@RESTOAPN
type: ConfigObject
name: RESTOAPN（容灾APN特征参数）
nf: UNC
version: 20.15.2
object_name: RESTOAPN
object_kind: entity
applicable_nf:
- MME
status: active
---

# RESTOAPN（容灾APN特征参数）

## 说明

**适用网元：MME**

本命令用于增加支持容灾备份的APN，即APNNI。启用“MME链式备份特性”后，若用户激活的PDN连接的APNNI与本命令配置的APNNI匹配，此用户支持容灾备份功能；反之，用户不支持容灾备份功能。

## 操作本对象的命令

- [ADD RESTOAPN](command/UNC/20.15.2/ADD-RESTOAPN.md)
- [LST RESTOAPN](command/UNC/20.15.2/LST-RESTOAPN.md)
- [RMV RESTOAPN](command/UNC/20.15.2/RMV-RESTOAPN.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除容灾APN特征参数(RMV-RESTOAPN)_72345715.md`
- 原始手册：`evidence/UNC/20.15.2/增加容灾APN特征参数(ADD-RESTOAPN)_26305924.md`
- 原始手册：`evidence/UNC/20.15.2/查询容灾APN特征参数(LST-RESTOAPN)_26146116.md`
