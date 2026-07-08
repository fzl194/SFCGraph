---
id: UNC@20.15.2@ConfigObject@OFCCDRPARA
type: ConfigObject
name: OFCCDRPARA（离线计费话单参数）
nf: UNC
version: 20.15.2
object_name: OFCCDRPARA
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# OFCCDRPARA（离线计费话单参数）

## 说明

**适用NF：SGW-C、PGW-C、SMF**

![](配置离线计费话单参数（SET OFCCDRPARA）_09896905.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，配置SPCDRCONTROL=PGW_SGW_CDR后需检查流量容器占用率，防止资源耗尽引发用户激活成功率下降

该命令用于配置离线计费话单参数。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-OFCCDRPARA]] · LST OFCCDRPARA
- [[command/UNC/20.15.2/SET-OFCCDRPARA]] · SET OFCCDRPARA

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示离线计费话单参数（LST-OFCCDRPARA）_09896906.md`
- 原始手册：`evidence/UNC/20.15.2/配置离线计费话单参数（SET-OFCCDRPARA）_09896905.md`
