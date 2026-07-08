---
id: UNC@20.15.2@ConfigObject@LOGIFDSCP
type: ConfigObject
name: LOGIFDSCP（逻辑接口DSCP配置）
nf: UNC
version: 20.15.2
object_name: LOGIFDSCP
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- AMF
- SMF
- NRF
- NSSF
- GGSN
- SMSF
- NCG
status: active
---

# LOGIFDSCP（逻辑接口DSCP配置）

## 说明

**适用NF：SGW-C、PGW-C、AMF、SMF、NRF、NSSF、SMSF、NCG**

该命令用于设置信令报文的DSCP值。在IP承载网络中，通常使用DSCP标记来进行业务优先级的区分和QoS保证。为区分不同信令在IP承载网络中不同的转发优先级，UNC支持设置具体信令流报文的DSCP值，使不同的信令按照DSCP值进行优先级转发。

有关DSCP的内容请参见RFC2474。DSCP总共分成了4类：Class Selector(CS)、Expedited Forwarding(EF)、Assured Forwarding(AF)和Best Effort(BE)。CS（类选择器）的DSCP值后三位为0，EF（加速转发）的DSCP值为101110(46)，AF（确保转发）的DSCP值最后一位为0，BE（默认）的DSCP值为000000(0)。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-LOGIFDSCP]] · LST LOGIFDSCP
- [[command/UNC/20.15.2/SET-LOGIFDSCP]] · SET LOGIFDSCP

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询逻辑接口DSCP配置（LST-LOGIFDSCP）_50558742.md`
- 原始手册：`evidence/UNC/20.15.2/设置逻辑接口DSCP值（SET-LOGIFDSCP）_50558771.md`
