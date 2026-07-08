---
id: UNC@20.15.2@ConfigObject@VLRFAULTEXIT
type: ConfigObject
name: VLRFAULTEXIT（用户退出VLR故障增强状态）
nf: UNC
version: 20.15.2
object_name: VLRFAULTEXIT
object_kind: action
applicable_nf:
- MME
status: active
---

# VLRFAULTEXIT（用户退出VLR故障增强状态）

## 说明

**适用网元：MME**

该命令用于停止用户退出VLR故障增强状态的任务。当系统中执行了用户退出VLR故障增强状态( [STR VLRFAULTEXIT](启动用户退出VLR故障增强状态(STR VLRFAULTEXIT)_92963924.md) )命令时，希望中途停止退出VLR故障增强状态任务，可以执行该命令。

## 操作本对象的命令

- [[command/UNC/20.15.2/STP-VLRFAULTEXIT]] · STP VLRFAULTEXIT
- [[command/UNC/20.15.2/STR-VLRFAULTEXIT]] · STR VLRFAULTEXIT

## 证据

- 原始手册：`evidence/UNC/20.15.2/停止用户退出VLR故障增强状态(STP-VLRFAULTEXIT)_93021280.md`
- 原始手册：`evidence/UNC/20.15.2/启动用户退出VLR故障增强状态(STR-VLRFAULTEXIT)_92963924.md`
