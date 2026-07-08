---
id: UNC@20.15.2@ConfigObject@APNUPFINFO
type: ConfigObject
name: APNUPFINFO（指定APN的UPF节点信息）
nf: UNC
version: 20.15.2
object_name: APNUPFINFO
object_kind: entity
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
status: active
---

# APNUPFINFO（指定APN的UPF节点信息）

## 说明

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于增加指定APN的UPF节点信息。

同一个UPF在不同APN下可能具有不同的位置特征，比如UPF对于APN1可以作为中心UPF使用，对于APN2则可以作为边缘UPF使用，此时可通过本命令设置APN和UPF的位置特性的关系。

## 操作本对象的命令

- [ADD APNUPFINFO](command/UNC/20.15.2/ADD-APNUPFINFO.md)
- [LST APNUPFINFO](command/UNC/20.15.2/LST-APNUPFINFO.md)
- [MOD APNUPFINFO](command/UNC/20.15.2/MOD-APNUPFINFO.md)
- [RMV APNUPFINFO](command/UNC/20.15.2/RMV-APNUPFINFO.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改指定APN的UPF节点信息（MOD-APNUPFINFO）_96242549.md`
- 原始手册：`evidence/UNC/20.15.2/删除指定APN的UPF节点信息（RMV-APNUPFINFO）_96242745.md`
- 原始手册：`evidence/UNC/20.15.2/增加指定APN的UPF节点信息（ADD-APNUPFINFO）_96241630.md`
- 原始手册：`evidence/UNC/20.15.2/查询指定APN的UPF节点信息（LST-APNUPFINFO）_96242084.md`
