---
id: UNC@20.15.2@ConfigObject@FAULTLNKDETCFG
type: ConfigObject
name: FAULTLNKDETCFG（故障链路探测配置）
nf: UNC
version: 20.15.2
object_name: FAULTLNKDETCFG
object_kind: global_setting
applicable_nf:
- SGSN
- MME
status: active
---

# FAULTLNKDETCFG（故障链路探测配置）

## 说明

**适用网元：SGSN、MME**

该命令用于设置系统是否开启故障链路的TRACEROUTE探测功能，支持的链路包括：Diameter、S1AP、SGs、GTPC、M3UA、IP NS-VC、Ga、Dns类型的链路。本功能开启后，链路故障时系统自动获取链路本对端IP地址，并启动TRACEROUTE探测。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-FAULTLNKDETCFG]] · LST FAULTLNKDETCFG
- [[command/UNC/20.15.2/SET-FAULTLNKDETCFG]] · SET FAULTLNKDETCFG

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询故障链路探测配置(LST-FAULTLNKDETCFG)_72225551.md`
- 原始手册：`evidence/UNC/20.15.2/设置故障链路探测功能(SET-FAULTLNKDETCFG)_26145872.md`
