---
id: UDG@20.15.2@ConfigObject@RESOMU
type: ConfigObject
name: RESOMU（倒换主备操作维护单元）
nf: UDG
version: 20.15.2
object_name: RESOMU
object_kind: action
status: active
---

# RESOMU（倒换主备操作维护单元）

## 说明

![](倒换主备操作维护单元（SWP RESOMU）_04480462.assets/notice_3.0-zh-cn.png)

本命令为高危命令，操作不当会引起操作维护单元承载的业务受影响，如果在存储故障期间执行该命令后，原备OMU可以正常升主，原主OMU会复位，且在存储故障恢复前原主OMU无法启动，请谨慎使用并联系华为技术支持协助操作。

在硬件替换、升级或打补丁等场景中，需要通过主动倒换OMU进程来达到原主用OMU所在资源上只有备用进程的要求，从而避免在替换这个资源时所造成的业务损失，此时可使用本命令。

## 操作本对象的命令

- [SWP RESOMU](command/UDG/20.15.2/SWP-RESOMU.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/倒换主备操作维护单元（SWP-RESOMU）_04480462.md`
