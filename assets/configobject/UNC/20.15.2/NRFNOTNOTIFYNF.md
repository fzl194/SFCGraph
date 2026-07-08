---
id: UNC@20.15.2@ConfigObject@NRFNOTNOTIFYNF
type: ConfigObject
name: NRFNOTNOTIFYNF（不通知NF实例）
nf: UNC
version: 20.15.2
object_name: NRFNOTNOTIFYNF
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFNOTNOTIFYNF（不通知NF实例）

## 说明

![](增加不通知NF实例（ADD NRFNOTNOTIFYNF）_60329621.assets/notice_3.0-zh-cn_2.png)

该命令与NRF通知策略SET NRFNOTIFYPLY配合使用，当SET NRFNOTIFYPLY的NRFNOTIFYPLY设置为NFINSTANCEIDNOT时，请谨慎添加NF实例信息，否则对于添加到列表中的NF，NRF将不会通知其注册变更信息。

**适用NF：NRF**

该命令用于增加不通知的NF实例，当列表中的NF注册信息发生变更时，NRF将不会发送对应的订阅通知消息。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NRFNOTNOTIFYNF]] · ADD NRFNOTNOTIFYNF
- [[command/UNC/20.15.2/LST-NRFNOTNOTIFYNF]] · LST NRFNOTNOTIFYNF
- [[command/UNC/20.15.2/RMV-NRFNOTNOTIFYNF]] · RMV NRFNOTNOTIFYNF

## 证据

- 原始手册：`evidence/UNC/20.15.2/NRFNOTNOTIFYNF.md`
- 原始手册：`evidence/UNC/20.15.2/NRFNOTNOTIFYNF.md`
- 原始手册：`evidence/UNC/20.15.2/NRFNOTNOTIFYNF.md`
