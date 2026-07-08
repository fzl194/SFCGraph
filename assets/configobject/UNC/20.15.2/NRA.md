---
id: UNC@20.15.2@ConfigObject@NRA
type: ConfigObject
name: NRA（空路由区对照表）
nf: UNC
version: 20.15.2
object_name: NRA
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# NRA（空路由区对照表）

## 说明

**适用网元：SGSN**

该命令用于增加空路由区配置表。对每个存在不支持GPRS业务的小区的位置区，SGSN将属于该位置区的所有不支持GPRS业务的小区组成称之为NULL RA。配置此命令后，在2.5G/3G手机的电路域寻呼流程中，系统除了寻呼支持GPRS业务的路由区，还会寻呼空路由区表内的路由区，从而提高电路域寻呼的成功率。同一位置区下，只能有一个NULL RA，NULL RA与普通RA的编码格式相同。

与MSC/VLR设备对接时，位置区下存在不支持GPRS业务的小区，则需要执行此命令。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NRA]] · ADD NRA
- [[command/UNC/20.15.2/LST-NRA]] · LST NRA
- [[command/UNC/20.15.2/RMV-NRA]] · RMV NRA

## 证据

- 原始手册：`evidence/UNC/20.15.2/NRA.md`
- 原始手册：`evidence/UNC/20.15.2/NRA.md`
- 原始手册：`evidence/UNC/20.15.2/NRA.md`
