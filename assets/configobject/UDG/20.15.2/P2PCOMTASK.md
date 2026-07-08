---
id: UDG@20.15.2@ConfigObject@P2PCOMTASK
type: ConfigObject
name: P2PCOMTASK（SDR点对点通信质量检测任务）
nf: UDG
version: 20.15.2
object_name: P2PCOMTASK
object_kind: action
status: active
---

# P2PCOMTASK（SDR点对点通信质量检测任务）

## 说明

![](激活SDR点对点通信质量检测任务（ACT P2PCOMTASK）_63673341.assets/notice_3.0-zh-cn.png)

该命令是高危命令，操作不当可能会影响性能，请谨慎使用并联系华为技术支持协助操作。

该命令用于激活SDR点对点通信质量检测任务。

> **说明**
> - 该命令执行后立即生效。
>
> - 执行此激活命令前需要确保DTP开关处于开启状态，执行[**LST SDRPARAMS**](../TCP开关控制/查询SDR参数（LST SDRPARAMS）_09587932.md)命令查询DTP开关状态，执行[**SET SDRPARAMS**](../TCP开关控制/设置SDR参数（SET SDRPARAMS）_09587912.md)命令设置DTP开关。
> - 只有PROTOCOLTYPE选择UDP可以探测丢包率，选择TCP或TLS测出的丢包率始终为0。
> - SRCID不存在时，激活命令执行成功，但激活任务不生效。
> - FLATTYPE为BASE时不支持PROTOCOLTYPE为TLS的通信探测。

## 操作本对象的命令

- [[command/UDG/20.15.2/ACT-P2PCOMTASK]] · ACT P2PCOMTASK

## 证据

- 原始手册：`evidence/UDG/20.15.2/P2PCOMTASK.md`
