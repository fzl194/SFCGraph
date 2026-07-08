---
id: UNC@20.15.2@ConfigObject@FHBYPASS
type: ConfigObject
name: FHBYPASS（旁路失败处理的配置参数）
nf: UNC
version: 20.15.2
object_name: FHBYPASS
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# FHBYPASS（旁路失败处理的配置参数）

## 说明

**适用NF：SGW-C、PGW-C、SMF**

![](设置失败旁路处理（SET FHBYPASS）_09896714.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，该命令仅用于紧急情况下的故障恢复，执行该命令可能会导致一定的计费误差，请谨慎使用。执行该命令将改变失败处理的原则，请确认已经进行了必要的预检查，并已获得了执行该命令的权限。

该命令用来配置当周边网元（OCS/PCRF/AAA）故障或者达到性能瓶颈触发网关消息流控时是否对故障网元进行放通。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-FHBYPASS]] · LST FHBYPASS
- [[command/UNC/20.15.2/RTR-FHBYPASS]] · RTR FHBYPASS
- [[command/UNC/20.15.2/SET-FHBYPASS]] · SET FHBYPASS

## 证据

- 原始手册：`evidence/UNC/20.15.2/恢复旁路失败处理的配置参数（RTR-FHBYPASS）_09896716.md`
- 原始手册：`evidence/UNC/20.15.2/查询失败旁路处理配置（LST-FHBYPASS）_09896715.md`
- 原始手册：`evidence/UNC/20.15.2/设置失败旁路处理（SET-FHBYPASS）_09896714.md`
