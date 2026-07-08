---
id: UNC@20.15.2@ConfigObject@INNERSTAT
type: ConfigObject
name: INNERSTAT（内统配置参数）
nf: UNC
version: 20.15.2
object_name: INNERSTAT
object_kind: global_setting
applicable_nf:
- AMF
status: active
---

# INNERSTAT（内统配置参数）

## 说明

![](设置内统配置参数（SET INNERSTAT）_21603484.assets/notice_3.0-zh-cn_2.png)

内统的日志打印周期设置过小会导致CPU和内存使用率升高，设置过大会导致关键统计信息丢失。

**适用NF：AMF**

该命令用于设置内统（内统指系统内部统计）配置参数，支持针对不同优先级的内统修改日志打印周期。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-INNERSTAT]] · LST INNERSTAT
- [[command/UNC/20.15.2/SET-INNERSTAT]] · SET INNERSTAT

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询内统配置参数（LST-INNERSTAT）_69803421.md`
- 原始手册：`evidence/UNC/20.15.2/设置内统配置参数（SET-INNERSTAT）_21603484.md`
