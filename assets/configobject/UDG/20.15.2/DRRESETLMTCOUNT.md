---
id: UDG@20.15.2@ConfigObject@DRRESETLMTCOUNT
type: ConfigObject
name: DRRESETLMTCOUNT（复位限制的次数）
nf: UDG
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

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令只用于在UEG/UEN/UEG+网元执行。
> - 组成容灾关系的网元需要分别进行配置，两边保持一致。
> - 每日凌晨0点或去使能容灾模式时，会将已记录的复位次数清零。
> - 若网元复位完成时，时间在凌晨0点过后的保护期长度的时间内，会将已记录的复位次数清零。若超过保护期，则不会清零。
> - 可通过OPR命令手动清零已记录的复位次数。
> - 当此命令与其他命令冲突时，以以下原则生效：
>
> - 以521软参的优先级为最高，当521软参设置为1时，忽略是否超过复位限制的次数。当设置为0时，则再以DRSTBYRSTCTRL命令设置为准。
> - 以DRSTBYRSTCTRL命令的优先级为更高，当设置为“否”时，忽略是否超过复位限制的次数。当设置为“是”时，则再以此命令设置为准。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | RESETLMTCOUNT | PROTECTTIME |
> | --- | --- |
> | 3 | 30 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-DRRESETLMTCOUNT]] · LST DRRESETLMTCOUNT
- [[command/UDG/20.15.2/SET-DRRESETLMTCOUNT]] · SET DRRESETLMTCOUNT

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询复位限制的次数（LST-DRRESETLMTCOUNT）_42155864.md`
- 原始手册：`evidence/UDG/20.15.2/设置复位限制的次数（SET-DRRESETLMTCOUNT）_93394829.md`
