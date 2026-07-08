---
id: UNC@20.15.2@ConfigObject@AMFNSSECPLCY
type: ConfigObject
name: AMFNSSECPLCY（AMF切片安全策略）
nf: UNC
version: 20.15.2
object_name: AMFNSSECPLCY
object_kind: global_setting
applicable_nf:
- AMF
status: active
---

# AMFNSSECPLCY（AMF切片安全策略）

## 说明

![](设置AMF切片安全策略（SET AMFNSSECPLCY）_97735773.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，在使用该命令后，AMF将开启跨切片访问保护，需要周边NF都开启该功能，否则业务流程失败，请谨慎使用。

**适用NF：AMF**

该命令用于设置AMF切片安全策略。

## 操作本对象的命令

- [LST AMFNSSECPLCY](command/UNC/20.15.2/LST-AMFNSSECPLCY.md)
- [SET AMFNSSECPLCY](command/UNC/20.15.2/SET-AMFNSSECPLCY.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询AMF切片安全策略（LST-AMFNSSECPLCY）_97815871.md`
- 原始手册：`evidence/UNC/20.15.2/设置AMF切片安全策略（SET-AMFNSSECPLCY）_97735773.md`
