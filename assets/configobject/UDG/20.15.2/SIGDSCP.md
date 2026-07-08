---
id: UDG@20.15.2@ConfigObject@SIGDSCP
type: ConfigObject
name: SIGDSCP（信令报文DSCP值）
nf: UDG
version: 20.15.2
object_name: SIGDSCP
object_kind: global_setting
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# SIGDSCP（信令报文DSCP值）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用于设置信令报文的DSCP值。在IP承载网络中，通常使用DSCP标记来进行业务优先级的区分和QoS保证。为区分不同信令在IP承载网络中不同的转发优先级，系统支持设置具体信令流报文的DSCP值，使不同的信令按照DSCP值进行优先级转发。

## 操作本对象的命令

- [LST SIGDSCP](command/UDG/20.15.2/LST-SIGDSCP.md)
- [SET SIGDSCP](command/UDG/20.15.2/SET-SIGDSCP.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询信令报文DSCP值（LST-SIGDSCP）_82837691.md`
- 原始手册：`evidence/UDG/20.15.2/设置信令报文DSCP值（SET-SIGDSCP）_82837690.md`
