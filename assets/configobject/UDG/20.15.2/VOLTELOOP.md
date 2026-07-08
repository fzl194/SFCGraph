---
id: UDG@20.15.2@ConfigObject@VOLTELOOP
type: ConfigObject
name: VOLTELOOP（VoLTE话路环回功能）
nf: UDG
version: 20.15.2
object_name: VOLTELOOP
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# VOLTELOOP（VoLTE话路环回功能）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

![](配置VoLTE话路环回功能（ADD VOLTELOOP）_07016805.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，配置了话路环回功能的用户无法进行正常的语音业务。VoLTE话路环回功能主要用于拨测场景下定位语音质量故障问题，开启话路环回功能，会导致通话双方语音业务数据中断，实际部署当中，需要在遵循当地法律允许的目的和范围内启用相应的功能，以确保符合当地通信自由相关的法律要求。

此命令用于配置VoLTE话路环回功能。VoLTE语音质量故障环回解决方案主要应用于拨测场景下的语音质量故障定位，此时需要使用该命令。

语音环回就是在指定网元设备指定接口将指定用户发送语音通路上的数据报文转发到接收语音通路上。同时原有呼叫对端发送过来的语音数据报文也会进行环回。终端用户通过对比环回后自发自收的语音从而判断该段传输路径上的语音是否存在问题，可以逐段的界定语音问题所产生的环节。

语音在系统中分为发送方向和接收方向，各有自己的通路。拨测场景下复现语音故障后，通过在语音媒体所经过的网元设备上进行语音环回，则可快速隔离定界语音故障问题。通过在网元设备的接入侧和核心网侧接口采用语音环回操作，则可基本把语音问题界定到三段范围内：接入侧、本端网元、核心网侧。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-VOLTELOOP]] · ADD VOLTELOOP
- [[command/UDG/20.15.2/LST-VOLTELOOP]] · LST VOLTELOOP
- [[command/UDG/20.15.2/MOD-VOLTELOOP]] · MOD VOLTELOOP
- [[command/UDG/20.15.2/RMV-VOLTELOOP]] · RMV VOLTELOOP

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改VoLTE话路环回功能（MOD-VOLTELOOP）_07016806.md`
- 原始手册：`evidence/UDG/20.15.2/删除VoLTE话路环回功能（RMV-VOLTELOOP）_07016807.md`
- 原始手册：`evidence/UDG/20.15.2/查询VoLTE话路环回功能（LST-VOLTELOOP）_07016808.md`
- 原始手册：`evidence/UDG/20.15.2/配置VoLTE话路环回功能（ADD-VOLTELOOP）_07016805.md`
