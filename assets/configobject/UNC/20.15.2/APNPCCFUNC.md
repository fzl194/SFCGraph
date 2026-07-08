---
id: UNC@20.15.2@ConfigObject@APNPCCFUNC
type: ConfigObject
name: APNPCCFUNC（APN PCC功能）
nf: UNC
version: 20.15.2
object_name: APNPCCFUNC
object_kind: global_setting
applicable_nf:
- PGW-C
- SMF
status: active
---

# APNPCCFUNC（APN PCC功能）

## 说明

**适用NF：PGW-C、SMF**

此命令用于使能或关闭指定APN/DNN用户的动态PCC功能。

PCC即策略和计费控制，当运营商需要通过动态PCC功能对计费策略和计费的粒度进行灵活控制，从而优化运营商的计费手段，提高收益时，可以通过此命令使能指定APN用户的动态PCC功能。

## 操作本对象的命令

- [LST APNPCCFUNC](command/UNC/20.15.2/LST-APNPCCFUNC.md)
- [SET APNPCCFUNC](command/UNC/20.15.2/SET-APNPCCFUNC.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APN-PCC功能（LST-APNPCCFUNC）_09897035.md`
- 原始手册：`evidence/UNC/20.15.2/设置APN-PCC功能（SET-APNPCCFUNC）_09897034.md`
