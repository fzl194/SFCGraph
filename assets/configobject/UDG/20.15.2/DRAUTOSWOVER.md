---
id: UDG@20.15.2@ConfigObject@DRAUTOSWOVER
type: ConfigObject
name: DRAUTOSWOVER（热备模式下是否开启自动倒换功能）
nf: UDG
version: 20.15.2
object_name: DRAUTOSWOVER
object_kind: global_setting
status: active
---

# DRAUTOSWOVER（热备模式下是否开启自动倒换功能）

## 说明

该命令用于设置在热备容灾模式下是否开启自动倒换功能。

> **说明**
> - 该命令执行后立即生效。
>
> - 为避免频繁执行对系统性能产生冲击，该命令在三分钟之内只能执行一次。
> - 如果系统时间发生跳变，跳变到上一次执行本命令的前N（N<=3）分钟，下一次可执行本命令最少需等待N+3分钟。
> - 以521软参的优先级最高，当521软参设置为1时，即便满足自动倒回条件也不会触发。当设置为0时，则以本命令设置为准。
> - 开关开时，该功能受备升主次数限制，即达到次数，由自动倒回触发的倒换无法成功。
> - 该命令仅在配置备容灾实例生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | AUTOSWOVER | WAITTIME |
> | --- | --- |
> | DISABLE | 5 |

## 操作本对象的命令

- [LST DRAUTOSWOVER](command/UDG/20.15.2/LST-DRAUTOSWOVER.md)
- [SET DRAUTOSWOVER](command/UDG/20.15.2/SET-DRAUTOSWOVER.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询热备模式下是否开启自动倒换功能（LST-DRAUTOSWOVER）_80076380.md`
- 原始手册：`evidence/UDG/20.15.2/设置在热备容灾模式下是否开启自动倒换功能（SET-DRAUTOSWOVER）_28275349.md`
