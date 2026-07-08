---
id: UNC@20.15.2@ConfigObject@FEMPACKET
type: ConfigObject
name: FEMPACKET（格式引擎配置信息）
nf: UNC
version: 20.15.2
object_name: FEMPACKET
object_kind: query_target
applicable_nf:
- NCG
status: active
---

# FEMPACKET（格式引擎配置信息）

## 说明

**适用NF：NCG**

该命令用于显示当前生效的格式引擎配置信息。该命令执行后，系统会查询当前生效的格式引擎信息，返回相应的格式引擎包文件名、通道信息和后存盘补丁名称。

在系统新安装、系统调测或者故障时，可以使用该命令进行检查。

## 操作本对象的命令

- [DSP FEMPACKET](command/UNC/20.15.2/DSP-FEMPACKET.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示格式引擎配置信息（DSP-FEMPACKET）_51174306.md`
