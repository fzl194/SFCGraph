---
id: UNC@20.15.2@ConfigObject@GTPCV2CMPT
type: ConfigObject
name: GTPCV2CMPT（GTP-C V2协议兼容性）
nf: UNC
version: 20.15.2
object_name: GTPCV2CMPT
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# GTPCV2CMPT（GTP-C V2协议兼容性）

## 说明

**适用网元：SGSN、MME**

该命令用于配置GTP-C V2消息是否携带特性信元以及定义相关信元格式。主要用于因 UNC 产品进行了协议升级，或对端设备对3GPP TS 29.274标准协议定义的消息和信元理解不一致而产生兼容性问题的场景。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-GTPCV2CMPT]] · ADD GTPCV2CMPT
- [[command/UNC/20.15.2/LST-GTPCV2CMPT]] · LST GTPCV2CMPT
- [[command/UNC/20.15.2/MOD-GTPCV2CMPT]] · MOD GTPCV2CMPT
- [[command/UNC/20.15.2/RMV-GTPCV2CMPT]] · RMV GTPCV2CMPT

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改GTP-C-V2协议兼容性(MOD-GTPCV2CMPT)_26145926.md`
- 原始手册：`evidence/UNC/20.15.2/删除GTP-C-V2协议兼容性(RMV-GTPCV2CMPT)_72345525.md`
- 原始手册：`evidence/UNC/20.15.2/增加GTP-C-V2协议兼容性(ADD-GTPCV2CMPT)_26305734.md`
- 原始手册：`evidence/UNC/20.15.2/查询GTP-C-V2协议兼容性(LST-GTPCV2CMPT)_72225605.md`
