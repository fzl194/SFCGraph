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

- [[command/UNC/20.15.2/ADD-IPAREAAPN]] · ADD IPAREAAPN
- [[command/UNC/20.15.2/LST-IPAREAAPN]] · LST IPAREAAPN
- [[command/UNC/20.15.2/RMV-IPAREAAPN]] · RMV IPAREAAPN

## 证据

- 原始手册：`evidence/UNC/20.15.2/IPAREAAPN.md`
- 原始手册：`evidence/UNC/20.15.2/IPAREAAPN.md`
- 原始手册：`evidence/UNC/20.15.2/IPAREAAPN.md`
