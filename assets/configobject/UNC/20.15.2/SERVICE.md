---
id: UNC@20.15.2@ConfigObject@SERVICE
type: ConfigObject
name: SERVICE（复位业务）
nf: UNC
version: 20.15.2
object_name: SERVICE
object_kind: action
applicable_nf:
- NCG
status: active
---

# SERVICE（复位业务）

## 说明

![](复位业务（RST SERVICE）_51174329.assets/notice_3.0-zh-cn_2.png)

复位业务属于危险操作。如果参数配置有误，重启后会导致业务故障。建议不要在业务繁忙时进行此项操作。

**适用NF：NCG**

该命令用于将UNC上的所有业务重新启动。系统会去激活所有的业务进程。

在更改了不能动态生效的参数后，需要复位业务，使参数生效。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-SERVICE]] · DSP SERVICE
- [[command/UNC/20.15.2/RST-SERVICE]] · RST SERVICE

## 证据

- 原始手册：`evidence/UNC/20.15.2/复位业务（RST-SERVICE）_51174329.md`
- 原始手册：`evidence/UNC/20.15.2/显示业务状态（DSP-SERVICE）_51174328.md`
