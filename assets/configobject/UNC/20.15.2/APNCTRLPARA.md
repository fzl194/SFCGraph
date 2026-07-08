---
id: UNC@20.15.2@ConfigObject@APNCTRLPARA
type: ConfigObject
name: APNCTRLPARA（基于APN的信令控制参数）
nf: UNC
version: 20.15.2
object_name: APNCTRLPARA
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# APNCTRLPARA（基于APN的信令控制参数）

## 说明

**适用网元：SGSN**

该命令用于增加基于APN的信令控制相关参数。

现网中存在多类M2M用户，比如电力用户为一类用户，水表用户为另一类用户，这些M2M用户在服务器升级或者故障排除等操作时可能会触发信令风暴，导致网关过载。为了保护网关，可通过本命令配置开启基于APN的信令控制功能。

## 操作本对象的命令

- [ADD APNCTRLPARA](command/UNC/20.15.2/ADD-APNCTRLPARA.md)
- [LST APNCTRLPARA](command/UNC/20.15.2/LST-APNCTRLPARA.md)
- [MOD APNCTRLPARA](command/UNC/20.15.2/MOD-APNCTRLPARA.md)
- [RMV APNCTRLPARA](command/UNC/20.15.2/RMV-APNCTRLPARA.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改基于APN的信令控制参数(MOD-APNCTRLPARA)_26145784.md`
- 原始手册：`evidence/UNC/20.15.2/删除基于APN的信令控制参数(RMV-APNCTRLPARA)_72225463.md`
- 原始手册：`evidence/UNC/20.15.2/增加基于APN的信令控制参数(ADD-APNCTRLPARA)_72345383.md`
- 原始手册：`evidence/UNC/20.15.2/查询基于APN的信令控制参数(LST-APNCTRLPARA)_26305594.md`
