---
id: UNC@20.15.2@ConfigObject@HAFEDETECT
type: ConfigObject
name: HAFEDETECT（HAFETCD网络亚健康探测参数）
nf: UNC
version: 20.15.2
object_name: HAFEDETECT
object_kind: global_setting
status: active
---

# HAFEDETECT（HAFETCD网络亚健康探测参数）

## 说明

该命令用于设置HAFETCD网络亚健康探测功能的开关、探测发包间隔、亚健康阈值、租约到期阈值、统计周期等参数。

当开关参数设置为关闭时，不开启探测功能或将已开启的探测功能关闭。

当开关参数设置为开启时，根据探测间隔、亚健康阈值、租约到期阈值和统计周期等参数开启探测功能。

当探测功能已开启，修改探测间隔、亚健康阈值、租约到期阈值或统计周期等参数时，则根据新的参数重启探测功能。

当探测功能开启后，在统计周期结束时，会对链路的状态进行判定，若超过半数的HAFETCD备节点到HAFETCD主节点之间的链路状态异常，或者HAFETCD主节点与SDRE容器之间的链路状态异常，则计算HAFETCD备节点之间的链路两两互通的节点集合，若集合中节点数量超过HAFETCD节点数量的一半，则将HAFETCD主节点迁移到集合中节点通信地址最小的节点上。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-HAFEDETECT]] · LST HAFEDETECT
- [[command/UNC/20.15.2/SET-HAFEDETECT]] · SET HAFEDETECT

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询HAFETCD网络亚健康探测参数（LST-HAFEDETECT）_11896664.md`
- 原始手册：`evidence/UNC/20.15.2/设置HAFETCD网络亚健康探测参数（SET-HAFEDETECT）_59776225.md`
