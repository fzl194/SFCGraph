---
id: UNC@20.15.2@ConfigObject@QOSCHARS
type: ConfigObject
name: QOSCHARS（QoS特征）
nf: UNC
version: 20.15.2
object_name: QOSCHARS
object_kind: entity
applicable_nf:
- PGW-C
- SMF
status: active
---

# QOSCHARS（QoS特征）

## 说明

**适用NF：PGW-C、SMF**

该命令用来配置QoS特征，其中包括资源类型、5QI优先级、包时延预算、包错误率、平均窗口、最大数据突发。

业务触发专载流程，如果PCF下发了这些参数，以PCF下发的为准，否则读取该配置中的Qos参数。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-QOSCHARS]] · ADD QOSCHARS
- [[command/UNC/20.15.2/LST-QOSCHARS]] · LST QOSCHARS
- [[command/UNC/20.15.2/MOD-QOSCHARS]] · MOD QOSCHARS
- [[command/UNC/20.15.2/RMV-QOSCHARS]] · RMV QOSCHARS

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改QoS特征（MOD-QOSCHARS）_71516445.md`
- 原始手册：`evidence/UNC/20.15.2/删除QoS特征（RMV-QOSCHARS）_24796836.md`
- 原始手册：`evidence/UNC/20.15.2/增加QoS特征（ADD-QOSCHARS）_24796806.md`
- 原始手册：`evidence/UNC/20.15.2/查询Qos特征（LST-QOSCHARS）_24796824.md`
