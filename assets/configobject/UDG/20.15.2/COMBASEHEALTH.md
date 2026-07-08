---
id: UDG@20.15.2@ConfigObject@COMBASEHEALTH
type: ConfigObject
name: COMBASEHEALTH（Base平面通信质量）
nf: UDG
version: 20.15.2
object_name: COMBASEHEALTH
object_kind: global_setting
status: active
---

# COMBASEHEALTH（Base平面通信质量）

## 说明

该命令用于设置Base平面的亚健康检测参数。当需要开启或关闭Base平面的网络亚健康质量检测任务，或者不想使用系统初始值时，可以使用此命令进行设置。

开启后，当检测出本端Pod与其它Pod之间的链路存在亚健康情况时，系统产生ALM-100319 Base平面Pod级亚健康告警。两个Pod之间的链路存在亚健康情况是指：在最近一个告警统计周期内，每一个告警检测周期计算出的亚健康度都大于告警阈值时。亚健康度是由两个Pod之间1个检测周期内的丢包率和错包率计算出的值，计算公式为（丢包率（千分比）+ 5 * 错包率（千分比））/ 2。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | DETECTINTERVAL | STATISINTERVAL | THRESHOLD | ENABLEFLAG |
> | --- | --- | --- | --- |
> | 1 | 30 | 50 | ENABLE |

## 操作本对象的命令

- [[command/UDG/20.15.2/DSP-COMBASEHEALTH]] · DSP COMBASEHEALTH
- [[command/UDG/20.15.2/LST-COMBASEHEALTH]] · LST COMBASEHEALTH
- [[command/UDG/20.15.2/SET-COMBASEHEALTH]] · SET COMBASEHEALTH

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示Base平面通信质量（DSP-COMBASEHEALTH）_32217474.md`
- 原始手册：`evidence/UDG/20.15.2/查询Base平面的亚健康检测参数（LST-COMBASEHEALTH）_32217475.md`
- 原始手册：`evidence/UDG/20.15.2/设置Base平面的亚健康检测参数（SET-COMBASEHEALTH）_32217476.md`
