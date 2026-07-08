---
id: UNC@20.15.2@ConfigObject@FCSWITCH
type: ConfigObject
name: FCSWITCH（流控开关）
nf: UNC
version: 20.15.2
object_name: FCSWITCH
object_kind: global_setting
status: active
---

# FCSWITCH（流控开关）

## 说明

![](设置流控开关（SET FCSWITCH）_09587940.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，关闭流控功能后在接入业务量大的情况下可能导致系统过载和复位，请谨慎使用。如需使用本命令请联系华为技术支持协助操作。

该命令用于设置整系统的流控功能禁用/启用状态。在通过 [**ADD FCPARAM**](增加流控参数（ADD FCPARAM）_09587901.md) 命令完成流控参数配置后，可以通过本命令来开启流控功能。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-FCSWITCH]] · LST FCSWITCH
- [[command/UNC/20.15.2/SET-FCSWITCH]] · SET FCSWITCH

## 证据

- 原始手册：`evidence/UNC/20.15.2/FCSWITCH.md`
- 原始手册：`evidence/UNC/20.15.2/FCSWITCH.md`
