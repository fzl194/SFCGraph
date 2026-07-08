---
id: UNC@20.15.2@ConfigObject@IFDSCPMCR
type: ConfigObject
name: IFDSCPMCR（接口DSCP配置）
nf: UNC
version: 20.15.2
object_name: IFDSCPMCR
object_kind: global_setting
applicable_nf:
- MME
status: active
---

# IFDSCPMCR（接口DSCP配置）

## 说明

**适用网元：MME**

此命令用于设置MCR对外网元接口发送IP包时的DSCP值。

有关DSCP的内容请参见RFC2474。DSCP总共分成了4类：Class Selector(CS)、Expedited Forwarding(EF)、Assured Forwarding(AF)和Best Effort(BE)。CS（类选择器）的DSCP值后三位为0，EF（加速转发）的DSCP值为101110(46)，AF（确保转发）的DSCP值最后一位为0，BE（默认）的DSCP值为000000(0)。常用的DSCP用法见 [表1](#ZH-CN_MMLREF_0000001171850995__tab1)

相关命令： [**MOD DSCPPRIMCR**](../DSCP优先级映射管理/修改DSCP映射优先级配置表(MOD DSCPPRIMCR)_71731089.md) 。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-IFDSCPMCR]] · LST IFDSCPMCR
- [[command/UNC/20.15.2/SET-IFDSCPMCR]] · SET IFDSCPMCR

## 证据

- 原始手册：`evidence/UNC/20.15.2/IFDSCPMCR.md`
- 原始手册：`evidence/UNC/20.15.2/IFDSCPMCR.md`
