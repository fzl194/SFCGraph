---
id: UDG@20.15.2@ConfigObject@LACGROUP
type: ConfigObject
name: LACGROUP（指定的LAC组）
nf: UDG
version: 20.15.2
object_name: LACGROUP
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# LACGROUP（指定的LAC组）

## 说明

**适用NF：PGW-U、UPF**

该命令用来在LAC组内绑定LAC号段。当需要在指定LAC组内绑定某个LAC号段时，使用该命令。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-LACGROUP]] · ADD LACGROUP
- [[command/UDG/20.15.2/LST-LACGROUP]] · LST LACGROUP
- [[command/UDG/20.15.2/RMV-LACGROUP]] · RMV LACGROUP

## 关联对象

- [[configobject/UDG/20.15.2/LACID]] · LACID
- [[configobject/UDG/20.15.2/POOLGRPMAP]] · POOLGRPMAP

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除指定的LAC组（RMV-LACGROUP）_06054836.md`
- 原始手册：`evidence/UDG/20.15.2/查看指定LAC组或者已配置所有LAC组的配置信息（LST-LACGROUP）_06054837.md`
- 原始手册：`evidence/UDG/20.15.2/添加一个新的LAC组（ADD-LACGROUP）_82837193.md`
