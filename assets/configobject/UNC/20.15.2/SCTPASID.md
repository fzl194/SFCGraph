---
id: UNC@20.15.2@ConfigObject@SCTPASID
type: ConfigObject
name: SCTPASID（SCTP偶联ID）
nf: UNC
version: 20.15.2
object_name: SCTPASID
object_kind: query_target
applicable_nf:
- SGSN
- MME
- SMSF
status: active
---

# SCTPASID（SCTP偶联ID）

## 说明

**适用网元：SGSN、MME、SMSF**

该命令用于查看SCTP(Stream Control Transmission Protocol)偶联ID及相关信息。偶联就是两个SCTP端点通过SCTP协议规定的4步握手机制建立起来的进行数据传递的逻辑联系或者通道。

## 操作本对象的命令

- [DSP SCTPASID](command/UNC/20.15.2/DSP-SCTPASID.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示SCTP偶联ID(DSP-SCTPASID)_72226017.md`
