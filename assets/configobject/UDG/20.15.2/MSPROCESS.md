---
id: UDG@20.15.2@ConfigObject@MSPROCESS
type: ConfigObject
name: MSPROCESS（复位微服务进程）
nf: UDG
version: 20.15.2
object_name: MSPROCESS
object_kind: action
status: active
---

# MSPROCESS（复位微服务进程）

## 说明

![](复位微服务进程（RST MSPROCESS）_09587898.assets/notice_3.0-zh-cn.png)

复位进程可能会造成业务的短时中断，在存储故障期间执行该命令复位进程后，该进程在存储故障恢复期都无法启动。请谨慎使用并联系华为技术支持协助操作。

此命令用于重启进程。

> **说明**
> - 该命令执行后立即生效。
>
> - 复位进程可能会造成业务的短时中断。
> - 复位有主备模式的主进程，会导致备升主。
> - 在存储故障期间执行该命令复位进程后，该进程在存储故障恢复期都无法启动。
> - 执行本命令批量复位CELL_SCFA进程可能会导致业务故障。建议执行本命令批量复位CELL_SCFA进程前，先执行[**SET MSFAULTTOLERANCE**](设置故障检测参数（SET MSFAULTTOLERANCE）_09587879.md)命令修改进程级正向监控心跳超时周期数为24，进程级反向监控心跳超时周期数为22。

## 操作本对象的命令

- [[command/UDG/20.15.2/CLR-MSPROCESS]] · CLR MSPROCESS
- [[command/UDG/20.15.2/DSP-MSPROCESS]] · DSP MSPROCESS
- [[command/UDG/20.15.2/RST-MSPROCESS]] · RST MSPROCESS

## 证据

- 原始手册：`evidence/UDG/20.15.2/复位微服务进程（RST-MSPROCESS）_09587898.md`
- 原始手册：`evidence/UDG/20.15.2/显示微服务进程信息（DSP-MSPROCESS）_09587887.md`
- 原始手册：`evidence/UDG/20.15.2/清除进程（CLR-MSPROCESS）_00520125.md`
