---
id: UNC@20.15.2@ConfigObject@SEQCHK
type: ConfigObject
name: SEQCHK（序号检查信息表）
nf: UNC
version: 20.15.2
object_name: SEQCHK
object_kind: global_setting
applicable_nf:
- SGSN
- MME
status: active
---

# SEQCHK（序号检查信息表）

## 说明

**适用网元：SGSN、MME**

该命令用于设置GTP-U序号检查开关，指示是否进行序号检查。GTP协议规定在进行GTP-U用户面数据转发时，可以对GTP的序号进行检查，也可以不进行检查。如果打开序号检查开关，对无效序号的报文将会做丢弃处理。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-SEQCHK]] · LST SEQCHK
- [[command/UNC/20.15.2/SET-SEQCHK]] · SET SEQCHK

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询序号检查信息表(LST-SEQCHK)_72345633.md`
- 原始手册：`evidence/UNC/20.15.2/设置序号检查信息表(SET-SEQCHK)_26305842.md`
