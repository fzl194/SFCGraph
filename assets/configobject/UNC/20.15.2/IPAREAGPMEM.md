---
id: UNC@20.15.2@ConfigObject@IPAREAGPMEM
type: ConfigObject
name: IPAREAGPMEM（IP区域群成员）
nf: UNC
version: 20.15.2
object_name: IPAREAGPMEM
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# IPAREAGPMEM（IP区域群成员）

## 说明

**适用网元：SGSN、MME**

该命令用于为一个区域群增加一条区域群成员记录，同一个区域群中的成员具有相同的IP地址分配策略。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-IPAREAGPMEM]] · ADD IPAREAGPMEM
- [[command/UNC/20.15.2/LST-IPAREAGPMEM]] · LST IPAREAGPMEM
- [[command/UNC/20.15.2/RMV-IPAREAGPMEM]] · RMV IPAREAGPMEM

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除IP区域群成员(RMV-IPAREAGPMEM)_72345197.md`
- 原始手册：`evidence/UNC/20.15.2/增加IP区域群成员(ADD-IPAREAGPMEM)_26305410.md`
- 原始手册：`evidence/UNC/20.15.2/查询IP区域群成员(LST-IPAREAGPMEM)_26145600.md`
