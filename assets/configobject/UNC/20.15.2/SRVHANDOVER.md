---
id: UNC@20.15.2@ConfigObject@SRVHANDOVER
type: ConfigObject
name: SRVHANDOVER（业务切换策略）
nf: UNC
version: 20.15.2
object_name: SRVHANDOVER
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# SRVHANDOVER（业务切换策略）

## 说明

**适用网元：SGSN**

该命令用于增加业务切换策略信息。切换策略控制就是根据业务级别、用户级别确定用户在2G和3G网络中的切换策略，来引导2G和3G的网络业务承载和网络负荷。切换策略可以由运营商配置。

通过Iu接口消息RAB ASSIGNMENT REQUEST和RELOCATION REQUEST中信元Service Handover以及Gb接口消息Create-BSS-PFC携带的信元Service UTRAN CCO将业务切换策略结果通知RNC/BSS。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-SRVHANDOVER]] · ADD SRVHANDOVER
- [[command/UNC/20.15.2/LST-SRVHANDOVER]] · LST SRVHANDOVER
- [[command/UNC/20.15.2/MOD-SRVHANDOVER]] · MOD SRVHANDOVER
- [[command/UNC/20.15.2/RMV-SRVHANDOVER]] · RMV SRVHANDOVER

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改业务切换策略(MOD-SRVHANDOVER)_26145668.md`
- 原始手册：`evidence/UNC/20.15.2/删除业务切换策略(RMV-SRVHANDOVER)_72345263.md`
- 原始手册：`evidence/UNC/20.15.2/增加业务切换策略(ADD-SRVHANDOVER)_26305476.md`
- 原始手册：`evidence/UNC/20.15.2/查询业务切换策略(LST-SRVHANDOVER)_72225347.md`
