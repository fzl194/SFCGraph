---
id: UNC@20.15.2@ConfigObject@SUBGP
type: ConfigObject
name: SUBGP（用户群）
nf: UNC
version: 20.15.2
object_name: SUBGP
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# SUBGP（用户群）

## 说明

**适用网元：SGSN、MME**

此命令用于增加用户群记录，同一个用户群中的用户具有相同的接入控制策略。

当将需要采用相同接入控制策略的不同的IMSI号段或MSISDN号段用户进行划分，作为一个用户群统一进行控制时，需要执行此命令。

## 操作本对象的命令

- [ADD SUBGP](command/UNC/20.15.2/ADD-SUBGP.md)
- [LST SUBGP](command/UNC/20.15.2/LST-SUBGP.md)
- [MOD SUBGP](command/UNC/20.15.2/MOD-SUBGP.md)
- [RMV SUBGP](command/UNC/20.15.2/RMV-SUBGP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改用户群(MOD-SUBGP)_72345159.md`
- 原始手册：`evidence/UNC/20.15.2/删除用户群(RMV-SUBGP)_26305372.md`
- 原始手册：`evidence/UNC/20.15.2/增加用户群(ADD-SUBGP)_72225241.md`
- 原始手册：`evidence/UNC/20.15.2/查询用户群(LST-SUBGP)_26145562.md`
