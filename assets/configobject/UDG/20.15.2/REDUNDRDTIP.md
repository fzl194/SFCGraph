---
id: UDG@20.15.2@ConfigObject@REDUNDRDTIP
type: ConfigObject
name: REDUNDRDTIP（冗余备份重定向IP）
nf: UDG
version: 20.15.2
object_name: REDUNDRDTIP
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# REDUNDRDTIP（冗余备份重定向IP）

## 说明

**适用NF：PGW-U、UPF**

该命令用来配置全局的冗余备份隧道虚拟重定向IP，即用于将业务流重定向到Gre Tunnel的虚拟IP地址。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-REDUNDRDTIP]] · ADD REDUNDRDTIP
- [[command/UDG/20.15.2/LST-REDUNDRDTIP]] · LST REDUNDRDTIP
- [[command/UDG/20.15.2/MOD-REDUNDRDTIP]] · MOD REDUNDRDTIP
- [[command/UDG/20.15.2/RMV-REDUNDRDTIP]] · RMV REDUNDRDTIP

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改冗余备份重定向IP（MOD-REDUNDRDTIP）_75097448.md`
- 原始手册：`evidence/UDG/20.15.2/删除冗余备份重定向IP地址（RMV-REDUNDRDTIP）_75097446.md`
- 原始手册：`evidence/UDG/20.15.2/增加冗余备份重定向IP地址（ADD-REDUNDRDTIP）_75097445.md`
- 原始手册：`evidence/UDG/20.15.2/查询冗余备份重定向IP（LST-REDUNDRDTIP）_75097447.md`
