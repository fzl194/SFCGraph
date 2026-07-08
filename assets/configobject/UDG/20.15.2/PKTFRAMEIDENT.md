---
id: UDG@20.15.2@ConfigObject@PKTFRAMEIDENT
type: ConfigObject
name: PKTFRAMEIDENT（帧包识别功能相关参数）
nf: UDG
version: 20.15.2
object_name: PKTFRAMEIDENT
object_kind: global_setting
applicable_nf:
- UPF
- PGW-U
status: active
---

# PKTFRAMEIDENT（帧包识别功能相关参数）

## 说明

**适用NF：UPF、PGW-U**

该命令用于设置帧包关系识别功能开关及相关参数。针对游戏、XR等通过帧传输且对时延敏感的业务，帧包识别功能可以识别报文的帧信息，并通过GTPU的标签将帧信息传递到无线侧，无线侧对同一帧数据的报文进行统一调度，避免部分报文调度不及时而产生的帧时延。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-PKTFRAMEIDENT]] · LST PKTFRAMEIDENT
- [[command/UDG/20.15.2/SET-PKTFRAMEIDENT]] · SET PKTFRAMEIDENT

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询帧包识别功能相关参数（LST-PKTFRAMEIDENT）_29298862.md`
- 原始手册：`evidence/UDG/20.15.2/设置帧包识别功能相关参数（SET-PKTFRAMEIDENT）_29529276.md`
