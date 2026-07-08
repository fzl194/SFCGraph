---
id: UDG@20.15.2@ConfigObject@MK
type: ConfigObject
name: MK（更新主密钥）
nf: UDG
version: 20.15.2
object_name: MK
object_kind: entity
status: active
---

# MK（更新主密钥）

## 说明

![](更新主密钥（MOD MK）_59103979.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，执行该命令会更新主密钥，系统中所有的密文数据都会同步更新，操作不当会导致加密的数据无法恢复，请谨慎使用并联系华为技术支持协助操作。

该命令用于更新主密钥。当主密钥即将过期或者已经过期时，可使用该命令更新主密钥，系统中所有的密文数据都会使用新密钥加密。

## 操作本对象的命令

- [[command/UDG/20.15.2/MOD-MK]] · MOD MK

## 证据

- 原始手册：`evidence/UDG/20.15.2/更新主密钥（MOD-MK）_59103979.md`
