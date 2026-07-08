---
id: UDG@20.15.2@ConfigObject@DEACTIVERATE
type: ConfigObject
name: DEACTIVERATE（去活用户会话的速率）
nf: UDG
version: 20.15.2
object_name: DEACTIVERATE
object_kind: global_setting
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# DEACTIVERATE（去活用户会话的速率）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

![](配置去活用户会话的速率（SET DEACTIVERATE）_82837081.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，需要根据周边设备的处理能力设置合适的去活速率。若设置去活速率过高，将导致周边设备过载。

该命令用于当系统主动去活用户时，配置去活用户的速率。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-DEACTIVERATE]] · LST DEACTIVERATE
- [[command/UDG/20.15.2/SET-DEACTIVERATE]] · SET DEACTIVERATE

## 证据

- 原始手册：`evidence/UDG/20.15.2/DEACTIVERATE.md`
- 原始手册：`evidence/UDG/20.15.2/DEACTIVERATE.md`
