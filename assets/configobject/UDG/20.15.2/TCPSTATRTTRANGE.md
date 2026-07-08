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

- [LST TCPSTATRTTRANGE](command/UDG/20.15.2/LST-TCPSTATRTTRANGE.md)
- [RTR TCPSTATRTTRANGE](command/UDG/20.15.2/RTR-TCPSTATRTTRANGE.md)
- [SET TCPSTATRTTRANGE](command/UDG/20.15.2/SET-TCPSTATRTTRANGE.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/恢复TCP统计功能的RTT区间为初始值（RTR-TCPSTATRTTRANGE）_74589219.md`
- 原始手册：`evidence/UDG/20.15.2/查询TCP统计功能的RTT区间（LST-TCPSTATRTTRANGE）_74749243.md`
- 原始手册：`evidence/UDG/20.15.2/设置TCP统计功能的RTT区间（SET-TCPSTATRTTRANGE）_87938410.md`
