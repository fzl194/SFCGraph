---
id: UNC@20.15.2@ConfigObject@SDAPLNK
type: ConfigObject
name: SDAPLNK（SDUP链路）
nf: UNC
version: 20.15.2
object_name: SDAPLNK
object_kind: query_target
applicable_nf:
- MME
status: active
---

# SDAPLNK（SDUP链路）

## 说明

**适用网元：MME**

本命令用于查询系统内正在使用的Sdup接口链路详细信息。

输出结果分为两个报表，报表1显示每条链路的状态以及链路指向的对端MME；报表2显示正常与故障状态的链路数量。

## 操作本对象的命令

- [DSP SDAPLNK](command/UNC/20.15.2/DSP-SDAPLNK.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示SDUP链路(DSP-SDAPLNK)_72346897.md`
