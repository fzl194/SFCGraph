---
id: UDG@20.15.2@ConfigObject@ALMNRMODE
type: ConfigObject
name: ALMNRMODE（网管北向告警上报模式）
nf: UDG
version: 20.15.2
object_name: ALMNRMODE
object_kind: global_setting
status: active
---

# ALMNRMODE（网管北向告警上报模式）

## 说明

本命令用于设置网管北向告警上报模式。

本命令的使用场景为：日常的操作维护中，操作员可根据实际需要使用此命令设置网管北向告警上报模式，使告警上报北向网管系统时使用统一的网元ID或者指定某个源网元ID的告警使用目标网元ID上报到北向网管系统。

> **说明**
> - 此命令允许修改本站点所有网元告警的北向上报模式，影响设备与北向网管系统的对接。系统初始预置“告警北向上报模式”为“MN(多网元独立模式)”，需要根据具体局点的要求进行设置。
> - 单网元合并模式下，删除目标网元或源网元时，针对该网元的设置都将失效。
> - 单网元合并模式下，删除所有的源网元和目标网元时，“告警北向上报模式”自动恢复到“MN(多网元独立模式)”。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-ALMNRMODE]] · LST ALMNRMODE
- [[command/UDG/20.15.2/SET-ALMNRMODE]] · SET ALMNRMODE

## 证据

- 原始手册：`evidence/UDG/20.15.2/ALMNRMODE.md`
- 原始手册：`evidence/UDG/20.15.2/ALMNRMODE.md`
