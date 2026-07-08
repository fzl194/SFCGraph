---
id: UNC@20.15.2@ConfigObject@RFSP
type: ConfigObject
name: RFSP（RFSP配置）
nf: UNC
version: 20.15.2
object_name: RFSP
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# RFSP（RFSP配置）

## 说明

**适用网元：SGSN、MME**

此命令用于增加RFSP(RAT/Frequency Selection Priority) ID配置。RFSP ID是在用户进行附着、插入签约数据、服务请求、位置更新流程时由MME/SGSN下发给eNodeB/RNC的一个信元，eNodeB/RNC通过本地配置将RFSP ID转换为一组带有优先级信息的频点列表，发给终端进行频点选择。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-RFSP]] · ADD RFSP
- [[command/UNC/20.15.2/LST-RFSP]] · LST RFSP
- [[command/UNC/20.15.2/MOD-RFSP]] · MOD RFSP
- [[command/UNC/20.15.2/RMV-RFSP]] · RMV RFSP

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改RFSP配置(MOD-RFSP)_26145540.md`
- 原始手册：`evidence/UNC/20.15.2/删除RFSP配置(RMV-RFSP)_72345137.md`
- 原始手册：`evidence/UNC/20.15.2/增加RFSP配置(ADD-RFSP)_26305350.md`
- 原始手册：`evidence/UNC/20.15.2/查询RFSP配置(LST-RFSP)_72225221.md`
