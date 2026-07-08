---
id: UNC@20.15.2@ConfigObject@PBUFREUSE5GC
type: ConfigObject
name: PBUFREUSE5GC（pbuf重用检测开关设置）
nf: UNC
version: 20.15.2
object_name: PBUFREUSE5GC
object_kind: entity
status: active
---

# PBUFREUSE5GC（pbuf重用检测开关设置）

## 说明

![](设置pbuf重用检测开关（SET PBUFREUSE5GC）_99859361.assets/notice_3.0-zh-cn_2.png)

本命令用于使能PBUF重用检测，开启后会降低性能，关闭后性能恢复。请谨慎使用并联系华为技术支持协助操作。

此命令用于设置MSS的PBUF重用检测开关，重用检测功能用来检测多个进程是否同时在使用同一片PBUF。用户打开开关后，系统收集运行信息，导致转发面性能下降，开关关闭后性能恢复。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-PBUFREUSE5GC]] · LST PBUFREUSE5GC
- [[command/UNC/20.15.2/RMV-PBUFREUSE5GC]] · RMV PBUFREUSE5GC
- [[command/UNC/20.15.2/SET-PBUFREUSE5GC]] · SET PBUFREUSE5GC

## 证据

- 原始手册：`evidence/UNC/20.15.2/PBUFREUSE5GC.md`
- 原始手册：`evidence/UNC/20.15.2/PBUFREUSE5GC.md`
- 原始手册：`evidence/UNC/20.15.2/PBUFREUSE5GC.md`
