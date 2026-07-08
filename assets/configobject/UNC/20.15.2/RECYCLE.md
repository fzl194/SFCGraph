---
id: UNC@20.15.2@ConfigObject@RECYCLE
type: ConfigObject
name: RECYCLE（回收地址）
nf: UNC
version: 20.15.2
object_name: RECYCLE
object_kind: action
applicable_nf:
- PGW-C
- SMF
- GGSN
status: active
---

# RECYCLE（回收地址）

## 说明

![](回收地址（ACT RECYCLE）_64343816.assets/notice_3.0-zh-cn_2.png)

使用该命令后会将强制回收正在使用的地址，对应的正常在线用户将被强制下线。

**适用NF：PGW-C、SMF、GGSN**

ACT RECYCLE命令用于回收本地或DHCP类型的地址池中的一个或一段地址。修改系统配置时，如果需要对某个地址池/段进行动态修改或删除，但地址池内有地址已经分配出去，这时候就需要利用ACT RECYCLE命令来强制回收分配出去的地址。

## 操作本对象的命令

- [[command/UNC/20.15.2/ACT-RECYCLE]] · ACT RECYCLE

## 证据

- 原始手册：`evidence/UNC/20.15.2/回收地址（ACT-RECYCLE）_64343816.md`
