---
id: UNC@20.15.2@ConfigObject@SEGFILENOTIFY
type: ConfigObject
name: SEGFILENOTIFY（号段文件通知记录）
nf: UNC
version: 20.15.2
object_name: SEGFILENOTIFY
object_kind: entity
applicable_nf:
- NRF
status: active
---

# SEGFILENOTIFY（号段文件通知记录）

## 说明

![](增加号段文件通知记录（ADD SEGFILENOTIFY）_50738957.assets/notice_3.0-zh-cn_2.png)

该操作会触发订阅通知，导致后续号段导入通知记录与预期不符。

**适用NF：NRF**

该命令用于在NRF上通过手动新增NF对应的IMSI/MSISDN号段信息达到NF号段更新，触发订阅通知。

## 操作本对象的命令

- [ADD SEGFILENOTIFY](command/UNC/20.15.2/ADD-SEGFILENOTIFY.md)
- [LST SEGFILENOTIFY](command/UNC/20.15.2/LST-SEGFILENOTIFY.md)
- [RMV SEGFILENOTIFY](command/UNC/20.15.2/RMV-SEGFILENOTIFY.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除号段文件通知记录（RMV-SEGFILENOTIFY）_50738961.md`
- 原始手册：`evidence/UNC/20.15.2/增加号段文件通知记录（ADD-SEGFILENOTIFY）_50738957.md`
- 原始手册：`evidence/UNC/20.15.2/查询号段文件通知记录（LST-SEGFILENOTIFY）_50738960.md`
