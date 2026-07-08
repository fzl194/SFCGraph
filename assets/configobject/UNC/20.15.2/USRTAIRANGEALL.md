---
id: UNC@20.15.2@ConfigObject@USRTAIRANGEALL
type: ConfigObject
name: USRTAIRANGEALL（所有的用户TAI区域）
nf: UNC
version: 20.15.2
object_name: USRTAIRANGEALL
object_kind: entity
applicable_nf:
- PGW-C
- SMF
- GGSN
status: active
---

# USRTAIRANGEALL（所有的用户TAI区域）

## 说明

![](删除所有的用户TAI区域（RMV USRTAIRANGEALL）_38729357.assets/notice_3.0-zh-cn_2.png)

删除用户TAI区域不当可能导致动态PCC用户无法基于用户TAI区域绑定的业务服务区选择PCF，进而影响用户使用业务。

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除所有的用户TAI区域。

## 操作本对象的命令

- [RMV USRTAIRANGEALL](command/UNC/20.15.2/RMV-USRTAIRANGEALL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除所有的用户TAI区域（RMV-USRTAIRANGEALL）_38729357.md`
