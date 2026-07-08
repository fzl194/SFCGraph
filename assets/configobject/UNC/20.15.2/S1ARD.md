---
id: UNC@20.15.2@ConfigObject@S1ARD
type: ConfigObject
name: S1ARD（S1模式接入限制参数）
nf: UNC
version: 20.15.2
object_name: S1ARD
object_kind: entity
applicable_nf:
- MME
status: active
---

# S1ARD（S1模式接入限制参数）

## 说明

**适用网元：MME**

该命令用于增加S1模式接入限制参数。该命令先根据IMSI号段将用户进行分类，再对每一类用户按照用户签约的ARD信息、签约的APN信息进行区分而控制用户接入E-UTRAN网络。

该命令适用于以下场景。若运营商希望拒绝某个号段接入E-UTRAN系统，则可以启用根据签约ARD控制用户接入特性；若运营商希望控制某类用户是否允许接入E-UTRAN，但HLR/HSS不支持ARD时，则可以启用根据签约APN控制用户接入特性。

## 操作本对象的命令

- [ADD S1ARD](command/UNC/20.15.2/ADD-S1ARD.md)
- [LST S1ARD](command/UNC/20.15.2/LST-S1ARD.md)
- [MOD S1ARD](command/UNC/20.15.2/MOD-S1ARD.md)
- [RMV S1ARD](command/UNC/20.15.2/RMV-S1ARD.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改S1模式接入限制参数(MOD-S1ARD)_26305290.md`
- 原始手册：`evidence/UNC/20.15.2/删除S1模式接入限制参数(RMV-S1ARD)_72225159.md`
- 原始手册：`evidence/UNC/20.15.2/增加S1模式接入限制参数(ADD-S1ARD)_26145478.md`
- 原始手册：`evidence/UNC/20.15.2/查询S1模式接入限制参数(LST-S1ARD)_72345077.md`
