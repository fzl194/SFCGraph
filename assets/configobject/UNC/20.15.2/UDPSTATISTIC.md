---
id: UNC@20.15.2@ConfigObject@UDPSTATISTIC
type: ConfigObject
name: UDPSTATISTIC（UDP报文统计）
nf: UNC
version: 20.15.2
object_name: UDPSTATISTIC
object_kind: action
status: active
---

# UDPSTATISTIC（UDP报文统计）

## 说明

该命令用于查看UDP连接报文统计信息。

UDP连接报文统计信息主要分为发送和接收两大部分。BFD、LDP、TracerRoute等报文封装在UDP报文中进行发送。因此，例如当以上报文的发送出现异常时，可以通过查看本机收发UDP报文的数量，判断是否由于UDP报文收发不正常而导致网络异常。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-UDPSTATISTIC]] · DSP UDPSTATISTIC
- [[command/UNC/20.15.2/RTR-UDPSTATISTIC]] · RTR UDPSTATISTIC

## 证据

- 原始手册：`evidence/UNC/20.15.2/UDPSTATISTIC.md`
- 原始手册：`evidence/UNC/20.15.2/UDPSTATISTIC.md`
