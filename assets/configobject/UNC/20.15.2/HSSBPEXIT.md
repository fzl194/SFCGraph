---
id: UNC@20.15.2@ConfigObject@HSSBPEXIT
type: ConfigObject
name: HSSBPEXIT（用户退出HSS BYPASS状态）
nf: UNC
version: 20.15.2
object_name: HSSBPEXIT
object_kind: action
applicable_nf:
- MME
status: active
---

# HSSBPEXIT（用户退出HSS BYPASS状态）

## 说明

**适用网元：MME**

该命令用于停止用户手动退出HSS BYPASS状态的任务。当系统中执行了用户退出HSS BYPASS状态( **[STR HSSBPEXIT](启动用户退出HSS BYPASS状态(STR HSSBPEXIT)_20995641.md)** )命令时，希望中途停止手动退出HSS BYPASS状态任务，可以执行该命令。

## 操作本对象的命令

- [STP HSSBPEXIT](command/UNC/20.15.2/STP-HSSBPEXIT.md)
- [STR HSSBPEXIT](command/UNC/20.15.2/STR-HSSBPEXIT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/停止用户退出HSS-BYPASS状态(STP-HSSBPEXIT)_70275802.md`
- 原始手册：`evidence/UNC/20.15.2/启动用户退出HSS-BYPASS状态(STR-HSSBPEXIT)_20995641.md`
