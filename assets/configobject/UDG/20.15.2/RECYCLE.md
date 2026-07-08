---
id: UDG@20.15.2@ConfigObject@RECYCLE
type: ConfigObject
name: RECYCLE（回收地址）
nf: UDG
version: 20.15.2
object_name: RECYCLE
object_kind: action
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# RECYCLE（回收地址）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

![](回收地址（ACT RECYCLE）_82837124.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，使用该命令后会将强制回收正在使用的地址，对应的正常在线用户将被强制下线。

ACT RECYCLE命令用于回收本地地址池、组播地址池或远端地址池中的一个或一段地址。修改系统配置时，如果需要对某个地址池/段进行动态修改或删除，但地址池内有地址已经分配出去，这时候就需要利用ACT RECYCLE命令来强制回收分配出去的地址。

## 操作本对象的命令

- [ACT RECYCLE](command/UDG/20.15.2/ACT-RECYCLE.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/回收地址（ACT-RECYCLE）_82837124.md`
