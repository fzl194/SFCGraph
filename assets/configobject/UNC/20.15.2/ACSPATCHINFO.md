---
id: UNC@20.15.2@ConfigObject@ACSPATCHINFO
type: ConfigObject
name: ACSPATCHINFO（系统当前补丁信息）
nf: UNC
version: 20.15.2
object_name: ACSPATCHINFO
object_kind: query_target
status: active
---

# ACSPATCHINFO（系统当前补丁信息）

## 说明

该命令用于显示VNFC系统当前补丁信息，包括补丁包名称、版本号、状态及生效时间。

补丁的加载、激活、删除都会触发补丁状态的变化，通过该命令可及时查询系统当前补丁的状态信息。

本命令只适用于ACS服务，其他微服务请使用DSP PATCHINFO命令。

## 操作本对象的命令

- [DSP ACSPATCHINFO](command/UNC/20.15.2/DSP-ACSPATCHINFO.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示系统当前补丁信息（DSP-ACSPATCHINFO）_05338949.md`
