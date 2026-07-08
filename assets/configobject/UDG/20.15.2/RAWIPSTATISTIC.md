---
id: UDG@20.15.2@ConfigObject@RAWIPSTATISTIC
type: ConfigObject
name: RAWIPSTATISTIC（RawIP报文统计）
nf: UDG
version: 20.15.2
object_name: RAWIPSTATISTIC
object_kind: action
status: active
---

# RAWIPSTATISTIC（RawIP报文统计）

## 说明

该命令用于查看RawIP报文统计信息。

RawIP报文统计信息主要分为发送和接收两大部分。

OSPF、ICMP报文封装在RawIP报文中进行发送。因此，例如当进行ping操作时，可以通过查看本机收发RawIP报文的数量，判断是否由于RawIP报文收发不正常而导致网络异常。

## 操作本对象的命令

- [DSP RAWIPSTATISTIC](command/UDG/20.15.2/DSP-RAWIPSTATISTIC.md)
- [RTR RAWIPSTATISTIC](command/UDG/20.15.2/RTR-RAWIPSTATISTIC.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询RawIP报文统计（DSP-RAWIPSTATISTIC）_00440557.md`
- 原始手册：`evidence/UDG/20.15.2/清除RawIP报文统计（RTR-RAWIPSTATISTIC）_00600421.md`
