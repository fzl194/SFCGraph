---
id: UNC@20.15.2@ConfigObject@IPAREAAPN
type: ConfigObject
name: IPAREAAPN（IP区域APN网络标识）
nf: UNC
version: 20.15.2
object_name: IPAREAAPN
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# IPAREAAPN（IP区域APN网络标识）

## 说明

**适用网元：SGSN、MME**

该命令用于为“基于位置的IP地址重分配”功能配置APN网络标识。当本网本地用户和本网异地用户激活PDP或者创建PDN连接时，且使用的APN网络标识与本命令配置的任意一条APN网络标识匹配时，系统就会对该用户启用“基于位置的IP地址重分配”功能。

## 操作本对象的命令

- [ADD IPAREAAPN](command/UNC/20.15.2/ADD-IPAREAAPN.md)
- [LST IPAREAAPN](command/UNC/20.15.2/LST-IPAREAAPN.md)
- [RMV IPAREAAPN](command/UNC/20.15.2/RMV-IPAREAAPN.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除IP区域APN网络标识(RMV-IPAREAAPN)_26145604.md`
- 原始手册：`evidence/UNC/20.15.2/增加IP区域APN网络标识(ADD-IPAREAAPN)_72345201.md`
- 原始手册：`evidence/UNC/20.15.2/查询IP区域APN网络标识(LST-IPAREAAPN)_72225285.md`
