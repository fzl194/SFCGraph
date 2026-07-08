---
id: UNC@20.15.2@ConfigObject@DFTGBRBEARER
type: ConfigObject
name: DFTGBRBEARER（缺省GBR承载参数）
nf: UNC
version: 20.15.2
object_name: DFTGBRBEARER
object_kind: global_setting
applicable_nf:
- PGW-C
- SMF
status: active
---

# DFTGBRBEARER（缺省GBR承载参数）

## 说明

**适用NF：PGW-C、SMF**

该命令用于配置SMF是否支持创建default-gbr承载（提供最低带宽保障的any to any GBR专有承载），该承载可由PCF/PCRF发起创建，也可以由SMF发起创建。

## 操作本对象的命令

- [LST DFTGBRBEARER](command/UNC/20.15.2/LST-DFTGBRBEARER.md)
- [SET DFTGBRBEARER](command/UNC/20.15.2/SET-DFTGBRBEARER.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询缺省GBR承载参数（LST-DFTGBRBEARER）_09897062.md`
- 原始手册：`evidence/UNC/20.15.2/设置缺省GBR承载参数（SET-DFTGBRBEARER）_09897061.md`
