---
id: UNC@20.15.2@ConfigObject@DRRESETLMTCOUNT
type: ConfigObject
name: DRRESETLMTCOUNT（复位限制的次数）
nf: UNC
version: 20.15.2
object_name: DRRESETLMTCOUNT
object_kind: global_setting
status: active
---

# DRRESETLMTCOUNT（复位限制的次数）

## 说明

此命令用于设置在24小时内整系统复位的最大次数：

- 在负荷分担容灾模式下，限制由于关键服务故障或者周边网元故障引发的整系统复位的次数。
- 在冷备容灾模式下，限制运行主由于关键服务故障或周边网元故障叠加通道异常时引发的整系统复位的次数，以及限制运行备由于关键服务故障或周边网元故障引发的整系统复位的次数。
- 在热备容灾模式下，限制运行备由于关键服务故障引发的整系统复位的次数。

## 操作本对象的命令

- [LST DRRESETLMTCOUNT](command/UNC/20.15.2/LST-DRRESETLMTCOUNT.md)
- [SET DRRESETLMTCOUNT](command/UNC/20.15.2/SET-DRRESETLMTCOUNT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询复位限制的次数（LST-DRRESETLMTCOUNT）_42155864.md`
- 原始手册：`evidence/UNC/20.15.2/设置复位限制的次数（SET-DRRESETLMTCOUNT）_93394829.md`
