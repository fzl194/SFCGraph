---
id: UNC@20.15.2@ConfigObject@DSCP
type: ConfigObject
name: DSCP（接口DSCP配置）
nf: UNC
version: 20.15.2
object_name: DSCP
object_kind: global_setting
applicable_nf:
- NCG
status: active
---

# DSCP（接口DSCP配置）

## 说明

**适用NF：NCG**

该命令用于设置NCG对外网元接口发送IP包时的DSCP值。

有关DSCP的内容请参见RFC2474。DSCP总共分成了4类：Class Selector(CS)、Expedited Forwarding(EF)、Assured Forwarding(AF)和Best Effort(BE)。CS（类选择器）的DSCP值后三位为0，EF（加速转发）的DSCP值为101110(46)，AF（确保转发）的DSCP值最后一位为0，BE的DSCP值为000000(0)。常用的DSCP用法见 [**表1**](设置接口DSCP配置（SET DSCP）_51174294.md#ZH-CN_CONCEPT_0251174294__table_0365AAA1) 。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-DSCP]] · LST DSCP
- [[command/UNC/20.15.2/SET-DSCP]] · SET DSCP

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSCP.md`
- 原始手册：`evidence/UNC/20.15.2/DSCP.md`
