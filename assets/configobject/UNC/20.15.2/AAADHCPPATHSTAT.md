---
id: UNC@20.15.2@ConfigObject@AAADHCPPATHSTAT
type: ConfigObject
name: AAADHCPPATHSTAT（复位RADIUS或DHCP链路状态）
nf: UNC
version: 20.15.2
object_name: AAADHCPPATHSTAT
object_kind: action
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
status: active
---

# AAADHCPPATHSTAT（复位RADIUS或DHCP链路状态）

## 说明

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于手动复位RADIUS或DHCP链路状态，当对端服务器为直连RADIUS服务器、中转RADIUS服务器或DHCP服务器且链路状态为异常时，执行本命令可将链路状态全部置为正常。

## 操作本对象的命令

- [[command/UNC/20.15.2/RST-AAADHCPPATHSTAT]] · RST AAADHCPPATHSTAT

## 证据

- 原始手册：`evidence/UNC/20.15.2/复位RADIUS或DHCP链路状态（RST-AAADHCPPATHSTAT）_15764440.md`
