---
id: UNC@20.15.2@ConfigObject@SCALELOADMON
type: ConfigObject
name: SCALELOADMON（自动扩缩容监测的虚机资源）
nf: UNC
version: 20.15.2
object_name: SCALELOADMON
object_kind: entity
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
- AMF
status: active
---

# SCALELOADMON（自动扩缩容监测的虚机资源）

## 说明

**适用NF：SGW-C、PGW-C、SMF、GGSN、AMF**

该命令用于自动扩缩容场景下，开启指定虚机资源的负载监测，并作为虚机自动扩缩容的依据。

## 操作本对象的命令

- [ADD SCALELOADMON](command/UNC/20.15.2/ADD-SCALELOADMON.md)
- [LST SCALELOADMON](command/UNC/20.15.2/LST-SCALELOADMON.md)
- [RMV SCALELOADMON](command/UNC/20.15.2/RMV-SCALELOADMON.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除自动扩缩容监测的虚机资源（RMV-SCALELOADMON）_24015948.md`
- 原始手册：`evidence/UNC/20.15.2/增加自动扩缩容监测的虚机资源（ADD-SCALELOADMON）_24015920.md`
- 原始手册：`evidence/UNC/20.15.2/查询自动扩缩容监测的虚机资源（LST-SCALELOADMON）_23736552.md`
