---
id: UDG@20.15.2@ConfigObject@TORESTTO
type: ConfigObject
name: TORESTTO（TCP重启TO）
nf: UDG
version: 20.15.2
object_name: TORESTTO
object_kind: action
applicable_nf:
- UPF
status: active
---

# TORESTTO（TCP重启TO）

## 说明

**适用NF：UPF**

![](TCP重启TO（ACT TORESTTO）_44249102.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，此命令执行后，会复位TO进程，导致业务中断，请确保在无业务时执行此命令。

该命令用于重启TO。

## 操作本对象的命令

- [[command/UDG/20.15.2/ACT-TORESTTO]] · ACT TORESTTO

## 证据

- 原始手册：`evidence/UDG/20.15.2/TCP重启TO（ACT-TORESTTO）_44249102.md`
