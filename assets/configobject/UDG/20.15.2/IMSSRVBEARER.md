---
id: UDG@20.15.2@ConfigObject@IMSSRVBEARER
type: ConfigObject
name: IMSSRVBEARER（指定用户的IMS Bypass状态）
nf: UDG
version: 20.15.2
object_name: IMSSRVBEARER
object_kind: action
applicable_nf:
- PGW-U
- UPF
status: active
---

# IMSSRVBEARER（指定用户的IMS Bypass状态）

## 说明

**适用NF：PGW-U、UPF**

![](去激活指定用户的IMS Bypass状态（DEA IMSSRVBEARER）_94130730.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，此命令将触发对特定用户/用户组/整机的IMS Bypass用户发送QoS URR Stop消息，可能中断这些用户的语音业务。

该命令用于退出指定用户的IMS Bypass状态，触发指定的IMS Bypass用户发送QoS URR Stop消息，SMF收到此消息后会去激活IMS Bypass的专有承载。

## 操作本对象的命令

- [DEA IMSSRVBEARER](command/UDG/20.15.2/DEA-IMSSRVBEARER.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/去激活指定用户的IMS-Bypass状态（DEA-IMSSRVBEARER）_94130730.md`
