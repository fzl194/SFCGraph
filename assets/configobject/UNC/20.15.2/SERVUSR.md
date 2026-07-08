---
id: UNC@20.15.2@ConfigObject@SERVUSR
type: ConfigObject
name: SERVUSR（模拟设备故障删除用户信息）
nf: UNC
version: 20.15.2
object_name: SERVUSR
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# SERVUSR（模拟设备故障删除用户信息）

## 说明

**适用网元：SGSN、MME**

本命令通过本地删除指定用户的所有数据，删除用户的操作不会通知周边网元以及终端。用于调测"MME链式备份特性"，模拟设备故障场景后该指定用户的业务恢复测试。

## 操作本对象的命令

- [RMV SERVUSR](command/UNC/20.15.2/RMV-SERVUSR.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/模拟设备故障删除用户信息(RMV-SERVUSR)_26305928.md`
