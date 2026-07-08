---
id: UNC@20.15.2@ConfigObject@PCSCF
type: ConfigObject
name: PCSCF（锁定P-CSCF地址配置）
nf: UNC
version: 20.15.2
object_name: PCSCF
object_kind: action
applicable_nf:
- PGW-C
- SMF
- GGSN
status: active
---

# PCSCF（锁定P-CSCF地址配置）

## 说明

**适用NF：PGW-C、SMF、GGSN**

该命令用来配置对指定P-CSCF组或者P-CSCF IP进行锁定操作。锁定后，后续使用该P-CSCF组或者P-CSCF IP激活的用户无法携带P-CSCF IP，已经在线的用户无影响。缺省情况下未锁定。

## 操作本对象的命令

- [[command/UNC/20.15.2/LCK-PCSCF]] · LCK PCSCF

## 证据

- 原始手册：`evidence/UNC/20.15.2/PCSCF.md`
