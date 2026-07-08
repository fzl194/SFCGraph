---
id: UNC@20.15.2@ConfigObject@UPFADDR
type: ConfigObject
name: UPFADDR（解锁UPF地址）
nf: UNC
version: 20.15.2
object_name: UPFADDR
object_kind: action
applicable_nf:
- SGW-C
- GGSN
- PGW-C
- SMF
status: active
---

# UPFADDR（解锁UPF地址）

## 说明

**适用NF：SGW-C、GGSN、PGW-C、SMF**

该命令用于解锁UPF地址。解锁后新激活的用户可以选择该UPF地址建立PFCP会话。

## 操作本对象的命令

- [[command/UNC/20.15.2/LCK-UPFADDR]] · LCK UPFADDR
- [[command/UNC/20.15.2/ULK-UPFADDR]] · ULK UPFADDR

## 证据

- 原始手册：`evidence/UNC/20.15.2/解锁UPF地址（ULK-UPFADDR）_50361721.md`
- 原始手册：`evidence/UNC/20.15.2/锁定UPF地址（LCK-UPFADDR）_50201745.md`
