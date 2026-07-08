---
id: UDG@20.15.2@ConfigObject@TRANSCOMTASK
type: ConfigObject
name: TRANSCOMTASK（SDR进程间透明通信检测任务）
nf: UDG
version: 20.15.2
object_name: TRANSCOMTASK
object_kind: action
status: active
---

# TRANSCOMTASK（SDR进程间透明通信检测任务）

## 说明

![](激活SDR进程间透明通信检测任务（ACT TRANSCOMTASK）_94730385.assets/notice_3.0-zh-cn.png)

该命令是高危命令，操作不当可能会影响性能，请谨慎使用并联系华为技术支持协助操作。

该命令用于激活SDR进程间透明通信检测任务。

> **说明**
> - 该命令执行后立即生效。
>
> - 执行此激活命令前需要确保DTP开关处于开启状态，执行[**LST SDRPARAMS**](../TCP开关控制/查询SDR参数（LST SDRPARAMS）_09587932.md)命令查询DTP开关状态，执行[**SET SDRPARAMS**](../TCP开关控制/设置SDR参数（SET SDRPARAMS）_09587912.md)命令设置DTP开关。
> - SRCID不存在时，激活命令执行成功，但激活任务不生效。

## 操作本对象的命令

- [ACT TRANSCOMTASK](command/UDG/20.15.2/ACT-TRANSCOMTASK.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/激活SDR进程间透明通信检测任务（ACT-TRANSCOMTASK）_94730385.md`
