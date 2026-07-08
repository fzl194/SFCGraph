---
id: UNC@20.15.2@ConfigObject@SCTPPARA
type: ConfigObject
name: SCTPPARA（SCTP协议参数）
nf: UNC
version: 20.15.2
object_name: SCTPPARA
object_kind: entity
applicable_nf:
- SGSN
- MME
- AMF
- SMSF
status: active
---

# SCTPPARA（SCTP协议参数）

## 说明

**适用网元：SGSN、MME、AMF** 、 **SMSF**

该命令用于增加基于IP的宽带信令SCTP(Stream Control Transmission Protocol)偶联的协议参数。偶联就是两个SCTP端点通过SCTP协议规定的4步握手机制建立起来的进行数据传递的逻辑联系或者通道。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-SCTPPARA]] · ADD SCTPPARA
- [[command/UNC/20.15.2/LST-SCTPPARA]] · LST SCTPPARA
- [[command/UNC/20.15.2/MOD-SCTPPARA]] · MOD SCTPPARA
- [[command/UNC/20.15.2/RMV-SCTPPARA]] · RMV SCTPPARA

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SCTP协议参数(MOD-SCTPPARA)_26146340.md`
- 原始手册：`evidence/UNC/20.15.2/删除SCTP协议参数(RMV-SCTPPARA)_72345939.md`
- 原始手册：`evidence/UNC/20.15.2/增加SCTP协议参数(ADD-SCTPPARA)_26306150.md`
- 原始手册：`evidence/UNC/20.15.2/查询SCTP协议参数(LST-SCTPPARA)_72226019.md`
