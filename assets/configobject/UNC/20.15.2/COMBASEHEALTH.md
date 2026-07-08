---
id: UNC@20.15.2@ConfigObject@COMBASEHEALTH
type: ConfigObject
name: COMBASEHEALTH（Base平面通信质量）
nf: UNC
version: 20.15.2
object_name: COMBASEHEALTH
object_kind: global_setting
status: active
---

# COMBASEHEALTH（Base平面通信质量）

## 说明

该命令用于设置Base平面的亚健康检测参数。当需要开启或关闭Base平面的网络亚健康质量检测任务，或者不想使用系统初始值时，可以使用此命令进行设置。

开启后，当检测出本端Pod与其它Pod之间的链路存在亚健康情况时，系统产生ALM-100319 Base平面Pod级亚健康告警。两个Pod之间的链路存在亚健康情况是指：在最近一个告警统计周期内，每一个告警检测周期计算出的亚健康度都大于告警阈值时。亚健康度是由两个Pod之间1个检测周期内的丢包率和错包率计算出的值，计算公式为（丢包率（千分比）+ 5 * 错包率（千分比））/ 2。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-COMBASEHEALTH]] · DSP COMBASEHEALTH
- [[command/UNC/20.15.2/LST-COMBASEHEALTH]] · LST COMBASEHEALTH
- [[command/UNC/20.15.2/SET-COMBASEHEALTH]] · SET COMBASEHEALTH

## 证据

- 原始手册：`evidence/UNC/20.15.2/COMBASEHEALTH.md`
- 原始手册：`evidence/UNC/20.15.2/COMBASEHEALTH.md`
- 原始手册：`evidence/UNC/20.15.2/COMBASEHEALTH.md`
