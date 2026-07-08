---
id: UNC@20.15.2@ConfigObject@S1PAGINGFC
type: ConfigObject
name: S1PAGINGFC（S1寻呼流控参数）
nf: UNC
version: 20.15.2
object_name: S1PAGINGFC
object_kind: global_setting
applicable_nf:
- MME
status: active
---

# S1PAGINGFC（S1寻呼流控参数）

## 说明

![](设置S1寻呼流控参数(SET S1PAGINGFC)_26146156.assets/notice_3.0-zh-cn_2.png)

如果S1寻呼流控功能被关闭或者相关流控参数设置不正确，可能影响S1寻呼流控的效果。

**适用网元：MME**

该命令用于设置S1模式寻呼流控功能的相关参数。

S1模式寻呼流控功能会对触发S1模式寻呼的消息（下面简称“寻呼”）处理速率进行控制，这些消息包括：从S-GW收到的Downlink Data Notification、Delete Bearer Request、Update Bearer Request、Create Bearer Request消息，从SGs接口收到的SGsAP Paging Request消息。

对寻呼的控制主要有如下两个场景：突发预防和拥塞控制。

- 突发预防：系统正常运行时，UNC会学习最近3天的寻呼速率历史峰值，用于自动调整当前系统允许处理的寻呼速率和增长速率；在学习过程中可能会有少量寻呼消息被丢弃；在寻呼高倍突发时，本功能可以有效缓解其对系统的冲击，避免系统进入重度拥塞。
- 拥塞控制：当出S1接口的UNC的包转发速率、Fabric通道流量拥塞或者UNC的CPU过载（下面简称“拥塞条件”）时，系统会进入寻呼流控状态，自动调整并控制系统允许处理的寻呼速率，保证系统过载情况下业务的正常进行，避免造成整个系统瘫痪。

S1模式寻呼流控过程有三种状态：正常状态、流控状态和恢复状态。流控状态为满足拥塞条件的起控状态；恢复状态为系统处于流控状态下，不满足拥塞条件时，系统进入的状态；正常状态为系统初始状态，或者恢复状态下连续一段时间没有消息丢弃而进入的状态。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-S1PAGINGFC]] · LST S1PAGINGFC
- [[command/UNC/20.15.2/SET-S1PAGINGFC]] · SET S1PAGINGFC

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询S1寻呼流控参数(LST-S1PAGINGFC)_72225835.md`
- 原始手册：`evidence/UNC/20.15.2/设置S1寻呼流控参数(SET-S1PAGINGFC)_26146156.md`
