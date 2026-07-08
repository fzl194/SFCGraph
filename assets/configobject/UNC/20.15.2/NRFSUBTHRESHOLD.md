---
id: UNC@20.15.2@ConfigObject@NRFSUBTHRESHOLD
type: ConfigObject
name: NRFSUBTHRESHOLD（NF的订阅门限）
nf: UNC
version: 20.15.2
object_name: NRFSUBTHRESHOLD
object_kind: global_setting
applicable_nf:
- NRF
status: active
---

# NRFSUBTHRESHOLD（NF的订阅门限）

## 说明

**适用NF：NRF**

该命令用于设置NF的订阅个数上限，通过IP区分订阅者，每个订阅者同时订阅的个数不能超过设置的个数上限。

## 操作本对象的命令

- [LST NRFSUBTHRESHOLD](command/UNC/20.15.2/LST-NRFSUBTHRESHOLD.md)
- [SET NRFSUBTHRESHOLD](command/UNC/20.15.2/SET-NRFSUBTHRESHOLD.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NF的订阅门限（LST-NRFSUBTHRESHOLD）_09653067.md`
- 原始手册：`evidence/UNC/20.15.2/设置NF的订阅门限（SET-NRFSUBTHRESHOLD）_09653220.md`
