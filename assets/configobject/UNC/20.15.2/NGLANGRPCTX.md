---
id: UNC@20.15.2@ConfigObject@NGLANGRPCTX
type: ConfigObject
name: NGLANGRPCTX（5G LAN组会话）
nf: UNC
version: 20.15.2
object_name: NGLANGRPCTX
object_kind: entity
applicable_nf:
- SMF
status: active
---

# NGLANGRPCTX（5G LAN组会话）

## 说明

![](删除5G LAN组会话（RMV NGLANGRPCTX）_04057524.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，执行该命令将删除指定的5G LAN组会话，组内所有用户将无法正常使用5G LAN业务。

**适用NF：SMF**

该命令用于5G LAN特性删除指定组会话以及组内所有UE会话的上下文。

## 操作本对象的命令

- [RMV NGLANGRPCTX](command/UNC/20.15.2/RMV-NGLANGRPCTX.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除5G-LAN组会话（RMV-NGLANGRPCTX）_04057524.md`
