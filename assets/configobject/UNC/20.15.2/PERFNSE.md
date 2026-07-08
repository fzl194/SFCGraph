---
id: UNC@20.15.2@ConfigObject@PERFNSE
type: ConfigObject
name: PERFNSE（NSE标识）
nf: UNC
version: 20.15.2
object_name: PERFNSE
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# PERFNSE（NSE标识）

## 说明

**适用网元：SGSN**

该命令用于增加一个NSE标识，用于Gb接口NSE话统上报的对象。指定NSE NS和指定NSE BSSGP话统测量单元下的指标上报时必需知道所要上报的NSEI，否则无法上报。因此需要通过该命令手动增加动态上报的NSE ID。

## 操作本对象的命令

- [ADD PERFNSE](command/UNC/20.15.2/ADD-PERFNSE.md)
- [LST PERFNSE](command/UNC/20.15.2/LST-PERFNSE.md)
- [RMV PERFNSE](command/UNC/20.15.2/RMV-PERFNSE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NSE标识(RMV-PERFNSE)_26146190.md`
- 原始手册：`evidence/UNC/20.15.2/增加NSE标识(ADD-PERFNSE)_72345789.md`
- 原始手册：`evidence/UNC/20.15.2/查询NSE标识(LST-PERFNSE)_72225869.md`
