---
id: UDG@20.15.2@ConfigObject@CFSHEALCTRL
type: ConfigObject
name: CFSHEALCTRL（在复杂故障场景下自愈功能控制参数）
nf: UDG
version: 20.15.2
object_name: CFSHEALCTRL
object_kind: global_setting
status: active
---

# CFSHEALCTRL（在复杂故障场景下自愈功能控制参数）

## 说明

![](设置在复杂故障场景下自愈功能控制参数（SET CFSHEALCTRL）_80236120.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当可能会加剧业务负载，请谨慎使用并联系华为技术支持协助操作。

该命令用于在复杂故障场景下，设置自愈功能控制参数。

> **说明**
> - 该命令执行后立即生效。
>
> - 为避免频繁执行对系统性能产生冲击，该命令在三分钟之内只能执行一次。
> - 如果系统时间发生跳变，跳变到上一次执行本命令的前N（N<=3）分钟，下一次可执行本命令最少需等待N+3分钟。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | SUBHEALTHSW | SUBHWAITTIME | Q922PERIOD | NFSUBHEALTHSW | NFSUBWAITTIME | NFSUBEXEPLY | SGLSUBHEALTHSW | SGLSUBWAITTIME | FAULTTHR | DIFFTHR |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | DISABLE | 10 | 3 | DISABLE | 300 | MANUAL | DISABLE | 120 | 90 | 20 |

## 操作本对象的命令

- [LST CFSHEALCTRL](command/UDG/20.15.2/LST-CFSHEALCTRL.md)
- [SET CFSHEALCTRL](command/UDG/20.15.2/SET-CFSHEALCTRL.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询在复杂故障场景下自愈功能控制参数（LST-CFSHEALCTRL）_28195461.md`
- 原始手册：`evidence/UDG/20.15.2/设置在复杂故障场景下自愈功能控制参数（SET-CFSHEALCTRL）_80236120.md`
