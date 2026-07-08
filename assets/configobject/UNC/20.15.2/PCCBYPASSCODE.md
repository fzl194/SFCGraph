---
id: UNC@20.15.2@ConfigObject@PCCBYPASSCODE
type: ConfigObject
name: PCCBYPASSCODE（PCC故障场景维持BYPASS状态码配置）
nf: UNC
version: 20.15.2
object_name: PCCBYPASSCODE
object_kind: entity
applicable_nf:
- PGW-C
- SMF
- GGSN
status: active
---

# PCCBYPASSCODE（PCC故障场景维持BYPASS状态码配置）

## 说明

**适用NF：PGW-C、SMF、GGSN**

该命令用于添加PCRF/PCF Bypass故障状态码配置。当非直连组网场景，UNC退出Bypass时发送探测消息后，收到对端网元返回特定状态码希望继续保持Bypass状态时，需要添加此配置。

## 操作本对象的命令

- [ADD PCCBYPASSCODE](command/UNC/20.15.2/ADD-PCCBYPASSCODE.md)
- [LST PCCBYPASSCODE](command/UNC/20.15.2/LST-PCCBYPASSCODE.md)
- [RMV PCCBYPASSCODE](command/UNC/20.15.2/RMV-PCCBYPASSCODE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除PCC故障场景维持BYPASS状态码配置（RMV-PCCBYPASSCODE）_18689757.md`
- 原始手册：`evidence/UNC/20.15.2/增加PCC故障场景维持BYPASS状态码配置（ADD-PCCBYPASSCODE）_83249518.md`
- 原始手册：`evidence/UNC/20.15.2/查询PCC故障场景维持BYPASS状态码配置（LST-PCCBYPASSCODE）_83409210.md`
