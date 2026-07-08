---
id: UNC@20.15.2@ConfigObject@PCCPCRFMSGATTR
type: ConfigObject
name: PCCPCRFMSGATTR（PCRF返回消息属性）
nf: UNC
version: 20.15.2
object_name: PCCPCRFMSGATTR
object_kind: global_setting
applicable_nf:
- PGW-C
- SMF
status: active
---

# PCCPCRFMSGATTR（PCRF返回消息属性）

## 说明

**适用NF：PGW-C、SMF**

该命令用于配置激活和更新流程中，UNC是否支持由DRA或PCRF触发的PCRF重选。

如果希望在激活或者更新流程中，UNC根据DRA或者PCRF消息触发的PCRF重选，则可将对应的参数使能。

## 操作本对象的命令

- [LST PCCPCRFMSGATTR](command/UNC/20.15.2/LST-PCCPCRFMSGATTR.md)
- [SET PCCPCRFMSGATTR](command/UNC/20.15.2/SET-PCCPCRFMSGATTR.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询PCRF返回消息属性（LST-PCCPCRFMSGATTR）_96782685.md`
- 原始手册：`evidence/UNC/20.15.2/设置PCRF返回消息属性（SET-PCCPCRFMSGATTR）_09897077.md`
