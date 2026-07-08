---
id: UNC@20.15.2@ConfigObject@IFDSCP
type: ConfigObject
name: IFDSCP（接口DSCP配置）
nf: UNC
version: 20.15.2
object_name: IFDSCP
object_kind: global_setting
applicable_nf:
- SGSN
- MME
status: active
---

# IFDSCP（接口DSCP配置）

## 说明

**适用网元：SGSN、MME**

此命令用于设置 UNC 对外网元接口发送IP包时的DSCP值。

有关DSCP的内容请参见RFC2474。DSCP总共分成了4类：Class Selector(CS)、Expedited Forwarding(EF)、Assured Forwarding(AF)和Best Effort(BE)。CS（类选择器）的DSCP值后三位为0，EF（加速转发）的DSCP值为101110(46)，AF（确保转发）的DSCP值最后一位为0，BE（默认）的DSCP值为000000(0)。常用的DSCP用法见 [表1](#ZH-CN_MMLREF_0000001126306022__tab1)

相关命令： [**MOD DSCPPRI**](../DSCP优先级映射管理/修改DSCP映射优先级配置表(MOD DSCPPRI)_26146208.md) 。

## 操作本对象的命令

- [LST IFDSCP](command/UNC/20.15.2/LST-IFDSCP.md)
- [SET IFDSCP](command/UNC/20.15.2/SET-IFDSCP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询接口DSCP配置(LST-IFDSCP)_72345811.md`
- 原始手册：`evidence/UNC/20.15.2/设置接口DSCP配置(SET-IFDSCP)_26306022.md`
