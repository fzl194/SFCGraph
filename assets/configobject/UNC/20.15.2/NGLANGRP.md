---
id: UNC@20.15.2@ConfigObject@NGLANGRP
type: ConfigObject
name: NGLANGRP（测试5G LAN组会话状态）
nf: UNC
version: 20.15.2
object_name: NGLANGRP
object_kind: action
applicable_nf:
- SMF
status: active
---

# NGLANGRP（测试5G LAN组会话状态）

## 说明

**适用NF：SMF**

该命令用于主动发起5G LAN组会话核查。命令执行后，SMF会主动给UPF发送一个PFCP Session Modification Request消息来核查SMF和UPF之间的组会话信息。核查结果可通过DSP NGLANUPINFO: NGLANUPINFOTYPE=ALL命令来查询。

## 操作本对象的命令

- [TST NGLANGRP](command/UNC/20.15.2/TST-NGLANGRP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/测试5G-LAN组会话状态（TST-NGLANGRP）_81407236.md`
