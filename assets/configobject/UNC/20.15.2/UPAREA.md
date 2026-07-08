---
id: UNC@20.15.2@ConfigObject@UPAREA
type: ConfigObject
name: UPAREA（UPF服务区）
nf: UNC
version: 20.15.2
object_name: UPAREA
object_kind: entity
applicable_nf:
- SMF
- GGSN
- SGW-C
- PGW-C
status: active
---

# UPAREA（UPF服务区）

## 说明

**适用NF：SMF、GGSN、SGW-C、PGW-C**

该命令用于增加UPF服务区域，并指定服务区域的名称与类型。后续指定UPF支持的服务范围时需要以本配置中的服务区域为粒度进行分配。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-UPAREA]] · ADD UPAREA
- [[command/UNC/20.15.2/LST-UPAREA]] · LST UPAREA
- [[command/UNC/20.15.2/RMV-UPAREA]] · RMV UPAREA

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除UPF服务区（RMV-UPAREA）_09651668.md`
- 原始手册：`evidence/UNC/20.15.2/增加UPF服务区（ADD-UPAREA）_09652457.md`
- 原始手册：`evidence/UNC/20.15.2/查询UPF服务区（LST-UPAREA）_09651370.md`
