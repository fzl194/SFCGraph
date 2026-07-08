---
id: UNC@20.15.2@ConfigObject@OMU
type: ConfigObject
name: OMU（倒换主备操作维护单元）
nf: UNC
version: 20.15.2
object_name: OMU
object_kind: action
status: active
---

# OMU（倒换主备操作维护单元）

## 说明

![](倒换主备操作维护单元（SWP OMU）_59104194.assets/notice_3.0-zh-cn_2.png)

本命令为高危命令，可能使得操作维护单元承载的业务受影响，如果在存储故障期间执行该命令后，原备OMU可以正常升主，原主OMU会复位，且在存储故障恢复前原主OMU无法启动，请谨慎使用并联系华为技术支持协助操作。

在硬件替换、升级或打补丁等场景中，需要通过主动倒换OMU进程来达到原主用OMU所在RU上只有备用进程的要求，从而避免在替换这个RU时所造成的业务损失，此时可使用本命令。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-OMU]] · DSP OMU
- [[command/UNC/20.15.2/SWP-OMU]] · SWP OMU

## 证据

- 原始手册：`evidence/UNC/20.15.2/倒换主备操作维护单元（SWP-OMU）_59104194.md`
- 原始手册：`evidence/UNC/20.15.2/显示主备操作维护单元信息（DSP-OMU）_59103381.md`
