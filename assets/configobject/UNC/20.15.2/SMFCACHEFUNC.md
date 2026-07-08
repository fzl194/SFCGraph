---
id: UNC@20.15.2@ConfigObject@SMFCACHEFUNC
type: ConfigObject
name: SMFCACHEFUNC（SMF映射关系的本地缓存策略）
nf: UNC
version: 20.15.2
object_name: SMFCACHEFUNC
object_kind: global_setting
applicable_nf:
- AMF
status: active
---

# SMFCACHEFUNC（SMF映射关系的本地缓存策略）

## 说明

![](设置SMF映射关系的本地缓存策略（SET SMFCACHEFUNC）_88377456.assets/notice_3.0-zh-cn_2.png)

开关变更可能对进程CPU和内存产生影响。

**适用NF：AMF**

该命令用于设置SMF映射关系的本地缓存策略，通过设置缓存策略，后续查询时先判断当前缓存信息是否可用，以减少SMF服务发现。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-SMFCACHEFUNC]] · LST SMFCACHEFUNC
- [[command/UNC/20.15.2/SET-SMFCACHEFUNC]] · SET SMFCACHEFUNC

## 证据

- 原始手册：`evidence/UNC/20.15.2/SMFCACHEFUNC.md`
- 原始手册：`evidence/UNC/20.15.2/SMFCACHEFUNC.md`
