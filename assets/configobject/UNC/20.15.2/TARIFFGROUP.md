---
id: UNC@20.15.2@ConfigObject@TARIFFGROUP
type: ConfigObject
name: TARIFFGROUP（费率切换组）
nf: UNC
version: 20.15.2
object_name: TARIFFGROUP
object_kind: entity
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# TARIFFGROUP（费率切换组）

## 说明

**适用NF：SGW-C、PGW-C、SMF**

该命令用来配置费率切换点。如果费率切换点所在的费率切换组不存在，则新建一个费率切换组。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-TARIFFGROUP]] · ADD TARIFFGROUP
- [[command/UNC/20.15.2/LST-TARIFFGROUP]] · LST TARIFFGROUP
- [[command/UNC/20.15.2/RMV-TARIFFGROUP]] · RMV TARIFFGROUP

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除费率切换组（RMV-TARIFFGROUP）_09896837.md`
- 原始手册：`evidence/UNC/20.15.2/查询费率切换组（LST-TARIFFGROUP）_09896838.md`
- 原始手册：`evidence/UNC/20.15.2/配置费率切换组（ADD-TARIFFGROUP）_09896836.md`
