---
id: UDG@20.15.2@ConfigObject@DRSTBYRSTCTRL
type: ConfigObject
name: DRSTBYRSTCTRL（运行备整系统复位开关）
nf: UDG
version: 20.15.2
object_name: DRSTBYRSTCTRL
object_kind: global_setting
status: active
---

# DRSTBYRSTCTRL（运行备整系统复位开关）

## 说明

该命令用于设置容灾实例在检测到关键服务异常或者周边网元故障时是否需要复位。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令只用于在UEN/UEG-S/UEG-L/UEG-M网元采用主备容灾模式下执行。
> - 主容灾实例和备容灾实例都可以下发该命令，但只有备容灾实例生效。可使用[**DSP DRGROUPSTATUS**](显示容灾组的运行状态信息（DSP DRGROUPSTATUS）_74554621.md)命令中"RUNNINGSTATUS"查询到本容灾实例是运行主还是运行备。
> - 当此命令与521软参冲突时，以521软参的优先级为最高，当521软参设置为1时，忽略此命令的设置。当设置为0时，则再以此命令设置为准。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | STANDBYRESETSW |
> | --- |
> | TRUE |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-DRSTBYRSTCTRL]] · LST DRSTBYRSTCTRL
- [[command/UDG/20.15.2/SET-DRSTBYRSTCTRL]] · SET DRSTBYRSTCTRL

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询运行备整系统复位开关（LST-DRSTBYRSTCTRL）_51001445.md`
- 原始手册：`evidence/UDG/20.15.2/设置运行备整系统复位开关（SET-DRSTBYRSTCTRL）_00921394.md`
