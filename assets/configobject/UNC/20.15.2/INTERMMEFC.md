---
id: UNC@20.15.2@ConfigObject@INTERMMEFC
type: ConfigObject
name: INTERMMEFC（Inter-MME流控参数）
nf: UNC
version: 20.15.2
object_name: INTERMMEFC
object_kind: global_setting
applicable_nf:
- MME
status: active
---

# INTERMMEFC（Inter-MME流控参数）

## 说明

![](设置Inter-MME流控参数(SET INTERMMEFC)_72345763.assets/notice_3.0-zh-cn_2.png)

- 此命令需要华为技术支持人员指导下才能执行，请慎重使用。
- 该命令主要用于Inter-MME用户的接入控制，配置不当可能导致业务受损，建议保持系统初始设置值。

**适用网元：MME**

该命令用于设置Inter-MME接入流控功能的相关参数。

MME组Pool时，如果某个MME故障，则故障MME上的用户会接入到Pool内正常的MME上，或非Pool组网下，大量用户同时从其他区域移动到某些MME覆盖区域时，均可能对这些MME造成较大冲击，导致其过载。为了防止这些场景下MME间的新接入用户影响在网用户的正常业务， UNC 系统能够基于当前CPU负荷，自动调节非本MME用户的接入消息允许处理速率。这些消息包括：Attach Request、Service Request消息。 如果这些消息是针对“WSFD- 102004 基于VoLTE的优先语音服务”或者“WSFD- 102101 VoLTE紧急呼叫”，则不对该消息进行流控。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-INTERMMEFC]] · LST INTERMMEFC
- [[command/UNC/20.15.2/SET-INTERMMEFC]] · SET INTERMMEFC

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Inter-MME流控参数(LST-INTERMMEFC)_26146164.md`
- 原始手册：`evidence/UNC/20.15.2/设置Inter-MME流控参数(SET-INTERMMEFC)_72345763.md`
