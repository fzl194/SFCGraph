---
id: UDG@20.15.2@ConfigObject@CONFLICTIP
type: ConfigObject
name: CONFLICTIP（本地地址池中冲突IPv4地址）
nf: UDG
version: 20.15.2
object_name: CONFLICTIP
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# CONFLICTIP（本地地址池中冲突IPv4地址）

## 说明

**适用NF：PGW-U、UPF**

该命令用于在本地地址池中标识指定IPv4地址为冲突状态。如果要限制本地地址池中的某个IPv4地址不能分配给终端用户，比如这个地址与系统或其他设备本身的地址冲突，可以使用ADD CONFLICTIP命令标识相应地址为冲突状态，禁止设备地址被分配给终端用户。

## 操作本对象的命令

- [ADD CONFLICTIP](command/UDG/20.15.2/ADD-CONFLICTIP.md)
- [LST CONFLICTIP](command/UDG/20.15.2/LST-CONFLICTIP.md)
- [RMV CONFLICTIP](command/UDG/20.15.2/RMV-CONFLICTIP.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除本地地址池中冲突IPv4地址（RMV-CONFLICTIP）_82837121.md`
- 原始手册：`evidence/UDG/20.15.2/查询本地地址池中冲突地址（LST-CONFLICTIP）_82837122.md`
- 原始手册：`evidence/UDG/20.15.2/添加本地地址池中冲突IPv4地址（ADD-CONFLICTIP）_82837120.md`
