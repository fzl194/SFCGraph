---
id: UNC@20.15.2@ConfigObject@DDNATTR
type: ConfigObject
name: DDNATTR（DDN消息参数以及Delay信元处理开关）
nf: UNC
version: 20.15.2
object_name: DDNATTR
object_kind: global_setting
applicable_nf:
- SGW-C
status: active
---

# DDNATTR（DDN消息参数以及Delay信元处理开关）

## 说明

**适用NF：SGW-C**

该命令用来设置Downlink Data Notification消息中是否支持携带EBI和ARP信元，以及控制SGW-C是否基于DownlinkData Notification Ack消息和Modify Bearer Request消息中的Delay信元进行处理。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-DDNATTR]] · LST DDNATTR
- [[command/UNC/20.15.2/SET-DDNATTR]] · SET DDNATTR

## 证据

- 原始手册：`evidence/UNC/20.15.2/DDNATTR.md`
- 原始手册：`evidence/UNC/20.15.2/DDNATTR.md`
