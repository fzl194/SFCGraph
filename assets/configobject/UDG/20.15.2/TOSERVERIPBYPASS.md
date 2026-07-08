---
id: UDG@20.15.2@ConfigObject@TOSERVERIPBYPASS
type: ConfigObject
name: TOSERVERIPBYPASS（异常Server IP自动bypass功能配置）
nf: UDG
version: 20.15.2
object_name: TOSERVERIPBYPASS
object_kind: global_setting
applicable_nf:
- UPF
status: active
---

# TOSERVERIPBYPASS（异常Server IP自动bypass功能配置）

## 说明

**适用NF：UPF**

该命令用于设置异常Server IP自动bypass功能，当开启该功能后，若存在五次及以上建链尝试仍无法正常建链的Server IP地址，该Server IP地址后续的所有流将被Bypass。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-TOSERVERIPBYPASS]] · LST TOSERVERIPBYPASS
- [[command/UDG/20.15.2/SET-TOSERVERIPBYPASS]] · SET TOSERVERIPBYPASS

## 证据

- 原始手册：`evidence/UDG/20.15.2/TOSERVERIPBYPASS.md`
- 原始手册：`evidence/UDG/20.15.2/TOSERVERIPBYPASS.md`
