---
id: UDG@20.15.2@ConfigObject@HOSTGLBCONFIG
type: ConfigObject
name: HOSTGLBCONFIG（主机收发全局属性）
nf: UDG
version: 20.15.2
object_name: HOSTGLBCONFIG
object_kind: global_setting
status: active
---

# HOSTGLBCONFIG（主机收发全局属性）

## 说明

该命令用于设置主机收发忽略管理平面接口上送的TCP或UDP协议报文的校验和。

如果网卡开启了GRO功能，分片的TCP或UDP报文被网卡聚合上送，聚合时校验和未刷新，在这种场景下使用该命令通知主机收发忽略校验和检查。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-HOSTGLBCONFIG]] · LST HOSTGLBCONFIG
- [[command/UDG/20.15.2/SET-HOSTGLBCONFIG]] · SET HOSTGLBCONFIG

## 证据

- 原始手册：`evidence/UDG/20.15.2/HOSTGLBCONFIG.md`
- 原始手册：`evidence/UDG/20.15.2/HOSTGLBCONFIG.md`
