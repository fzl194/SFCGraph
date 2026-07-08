---
id: UDG@20.15.2@ConfigObject@SECAUTHMEM
type: ConfigObject
name: SECAUTHMEM（二次授权命令）
nf: UDG
version: 20.15.2
object_name: SECAUTHMEM
object_kind: entity
status: active
---

# SECAUTHMEM（二次授权命令）

## 说明

用于添加一条需要二次授权的MML命令。

二次授权功能开启后，对于需要进行二次授权的MML命令将需要输入可以二次授权的用户名和密码进行授权后，才能继续执行。

需要进行二次授权的MML命令可以通过 [LST SECAUTHMEM](查看二次授权命令（LST SECAUTHMEM）_88107917.md) 命令查询。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-SECAUTHMEM]] · ADD SECAUTHMEM
- [[command/UDG/20.15.2/LST-SECAUTHMEM]] · LST SECAUTHMEM
- [[command/UDG/20.15.2/MOD-SECAUTHMEM]] · MOD SECAUTHMEM
- [[command/UDG/20.15.2/RMV-SECAUTHMEM]] · RMV SECAUTHMEM

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改二次授权命令（MOD-SECAUTHMEM）_88107919.md`
- 原始手册：`evidence/UDG/20.15.2/删除二次授权命令（RMV-SECAUTHMEM）_88107920.md`
- 原始手册：`evidence/UDG/20.15.2/增加二次授权命令（ADD-SECAUTHMEM）_88107918.md`
- 原始手册：`evidence/UDG/20.15.2/查看二次授权命令（LST-SECAUTHMEM）_88107917.md`
