---
id: UNC@20.15.2@ConfigObject@PESELPLCY
type: ConfigObject
name: PESELPLCY（SGSN/MME选择策略）
nf: UNC
version: 20.15.2
object_name: PESELPLCY
object_kind: global_setting
applicable_nf:
- SGSN
- MME
status: active
---

# PESELPLCY（SGSN/MME选择策略）

## 说明

![](设置SGSN_MME选择策略（SET PESELPLCY）_72225643.assets/notice_3.0-zh-cn_2.png)

如果SGSN/MME选择策略参数设置不正确，可能导致大量234G间的切换业务失败。

**适用网元：SGSN、MME**

该命令用于设置SGSN/MME选择策略，选择策略用来识别对端网元是SGSN还是MME。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-PESELPLCY]] · LST PESELPLCY
- [[command/UNC/20.15.2/SET-PESELPLCY]] · SET PESELPLCY

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SGSN_MME选择策略(LST-PESELPLCY)_26305774.md`
- 原始手册：`evidence/UNC/20.15.2/设置SGSN_MME选择策略（SET-PESELPLCY）_72225643.md`
