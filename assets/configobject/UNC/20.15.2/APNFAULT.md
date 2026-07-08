---
id: UNC@20.15.2@ConfigObject@APNFAULT
type: ConfigObject
name: APNFAULT（APN粒度的故障处理开关）
nf: UNC
version: 20.15.2
object_name: APNFAULT
object_kind: global_setting
applicable_nf:
- PGW-C
- GGSN
- SMF
status: active
---

# APNFAULT（APN粒度的故障处理开关）

## 说明

![](设置APN粒度的故障处理开关（SET APNFAULT）_98988893.assets/notice_3.0-zh-cn_2.png)

UPFAULTMODE设置为DETECTION时，SMF会隔离故障的N6链路，UPF存在过载风险。RESTOREFAULT设置为ENABLE时，SMF收到UPF上报的N6故障消息后，如果链路故障的UPF是主锚点UPF，则会去活使用故障N6链路的用户。

**适用NF：PGW-C、GGSN、SMF**

该命令用于控制APN粒度的故障处理开关。

## 操作本对象的命令

- [LST APNFAULT](command/UNC/20.15.2/LST-APNFAULT.md)
- [SET APNFAULT](command/UNC/20.15.2/SET-APNFAULT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APN粒度的故障处理开关（LST-APNFAULT）_98629445.md`
- 原始手册：`evidence/UNC/20.15.2/设置APN粒度的故障处理开关（SET-APNFAULT）_98988893.md`
