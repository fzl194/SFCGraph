---
id: UDG@20.15.2@ConfigObject@HAFEDETECT
type: ConfigObject
name: HAFEDETECT（HAFETCD网络亚健康探测参数）
nf: UDG
version: 20.15.2
object_name: HAFEDETECT
object_kind: global_setting
status: active
---

# HAFEDETECT（HAFETCD网络亚健康探测参数）

## 说明

该命令用于设置HAFETCD网络亚健康探测功能的开关、探测发包间隔、丢错包阈值、租约到期阈值、统计周期等参数。

当开关参数设置为关闭时，不开启探测功能或将已开启的探测功能关闭。

当开关参数设置为开启时，根据探测间隔、阈值和统计周期等参数开启探测功能。

当探测功能已开启，修改探测间隔、阈值或统计周期等参数时，则根据新的参数重启探测功能。

当探测功能开启后，在统计周期结束时，会对链路的状态进行判定，若超过半数的HAFETCD备节点到HAFETCD主节点之间的链路状态异常，或者HAFETCD主节点与SDRE容器之间的链路状态异常，则计算HAFETCD备节点之间的链路两两互通的节点集合，若集合中节点数量超过HAFETCD节点数量的一半，则将HAFETCD主节点迁移到集合中节点通信地址最小的节点上。

> **说明**
> - 该命令执行后立即生效。
>
> - 两个节点之间链路两两互通，指的是第一个节点向第二个节点发送探测报文能够收到响应报文，丢错包占比不超出阈值，并且第二个节点向第一个节点发送探测报文丢错包占比同样不超出阈值。
> - 节点通信地址最小，指的是HAFETCD节点的通信IP与端口号拼接的字符串按自然排序后的第一个元素，可以使用指令[**DSP ELECTION**](显示集群选举实例信息（DSP ELECTION）_09587911.md)查询节点的通信地址。
> - 设置参数时，应考虑合理性，如探测间隔设置为5，丢错包阈值设置为10，统计周期设置为10，即每500毫秒发送一次探测报文，统计周期10秒，预期发送20个包，即使丢错包数量为1，丢错包占比也达到了二十分之一，远远超出了设置的阈值千分之十，这种不合理的配置使得探测能力过于敏感，可能会导致HAFETCD主发生不必要的迁移。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | SUBHEALTHSW | DETECTINTERVAL | THRESHOLD | LEASETHRESHOLD | STATISINTERVAL |
> | --- | --- | --- | --- | --- |
> | ON | 5 | 300 | 50 | 30 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-HAFEDETECT]] · LST HAFEDETECT
- [[command/UDG/20.15.2/SET-HAFEDETECT]] · SET HAFEDETECT

## 证据

- 原始手册：`evidence/UDG/20.15.2/HAFEDETECT.md`
- 原始手册：`evidence/UDG/20.15.2/HAFEDETECT.md`
