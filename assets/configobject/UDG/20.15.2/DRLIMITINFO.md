---
id: UDG@20.15.2@ConfigObject@DRLIMITINFO
type: ConfigObject
name: DRLIMITINFO（已发生的倒换和复位次数和距离限制结束的时间）
nf: UDG
version: 20.15.2
object_name: DRLIMITINFO
object_kind: query_target
status: active
---

# DRLIMITINFO（已发生的倒换和复位次数和距离限制结束的时间）

## 说明

此命令用于查询由于关键服务故障而引发的复位次数和距离限制结束的时间以及备升主已发生的次数和距离限制结束的时间。

> **说明**
> - 该命令只用于在UEG/UEN/UEG+网元执行。
> - 不能简单依据此命令的查询结果判定是否受到限制，需要结合其他配置，如查询521软参的配置、[**LST DRSTBYRSTCTRL**](查询运行备整系统复位开关（LST DRSTBYRSTCTRL）_51001445.md)中配置综合判断 ：
>
> - 以521软参的优先级最高，当521软参设置为1时，忽略是否超过复位限制的次数。当设置为0时，则再以DRSTBYRSTCTRL命令设置为准。
> - 以DRSTBYRSTCTRL命令的优先级更高，当设置为“否”时，忽略是否超过复位限制的次数。当设置为“是”时，则再以DRRESETLMTCOUNT命令设置为准。
> - 达到复位限制次数后才会显示距离限制复位结束的时间。
> - 在负荷分担容灾模式下，倒换次数和距离限制倒换结束的时间显示为NULL。
> - 在冷备模式下，倒换限制依照当前时间过去24小时计算，在热备模式下，倒换限制依照每日24小时计算。

## 操作本对象的命令

- [[command/UDG/20.15.2/DSP-DRLIMITINFO]] · DSP DRLIMITINFO

## 证据

- 原始手册：`evidence/UDG/20.15.2/DRLIMITINFO.md`
