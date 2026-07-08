---
id: UDG@20.15.2@ConfigObject@TCPSTATRTTRANGE
type: ConfigObject
name: TCPSTATRTTRANGE（TCP统计功能的RTT区间为初始值）
nf: UDG
version: 20.15.2
object_name: TCPSTATRTTRANGE
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# TCPSTATRTTRANGE（TCP统计功能的RTT区间为初始值）

## 说明

**适用NF：PGW-U、UPF**

该命令用于设置TCP统计功能中的UE侧、SP侧RTT区间。通过观察网络中TCP业务流的UE侧、SP侧RTT比例分布，可以评估网络的传输质量。基于业务的TCP统计功能支持根据UE侧RTT区间、SP侧RTT区间统计TCP流数；如UE侧RTT区间为0到20ms的TCP流数，SP侧RTT区间为0到3ms的TCP流数。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-TCPSTATRTTRANGE]] · LST TCPSTATRTTRANGE
- [[command/UDG/20.15.2/RTR-TCPSTATRTTRANGE]] · RTR TCPSTATRTTRANGE
- [[command/UDG/20.15.2/SET-TCPSTATRTTRANGE]] · SET TCPSTATRTTRANGE

## 证据

- 原始手册：`evidence/UDG/20.15.2/TCPSTATRTTRANGE.md`
- 原始手册：`evidence/UDG/20.15.2/TCPSTATRTTRANGE.md`
- 原始手册：`evidence/UDG/20.15.2/TCPSTATRTTRANGE.md`
