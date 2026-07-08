---
id: UNC@20.15.2@ConfigObject@IUDETACH
type: ConfigObject
name: IUDETACH（Iu分离非活动用户参数）
nf: UNC
version: 20.15.2
object_name: IUDETACH
object_kind: global_setting
applicable_nf:
- SGSN
status: active
---

# IUDETACH（Iu分离非活动用户参数）

## 说明

**适用网元：SGSN**

此命令用于设置3G分离非活动用户配置参数。当用户通过附着或路由区更新流程接入到本SGSN后，如果在指定时长(大于 “非活动用户分离定时器(分)” 时长)没有PDP（Packet Data Protocol）激活，则认为该用户为非活动用户对用户进行分离操作；当系统将用户判断为非活动用户进行分离后，如果用户马上重新附着且与上次分离的时间间隔不超过配置的 “永久在线识别定时器长(秒)” 时长， 则该用户被定义为永久在线用户，后续系统不会对该用户进行分离非活动用户操作。SGSN发起分离非活动用户的流程，可以释放这些用户的空闲资源，以支持更多的用户。分离非活动用户的参数设置需要符合运营商的控制策略。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-IUDETACH]] · LST IUDETACH
- [[command/UNC/20.15.2/SET-IUDETACH]] · SET IUDETACH

## 证据

- 原始手册：`evidence/UNC/20.15.2/IUDETACH.md`
- 原始手册：`evidence/UNC/20.15.2/IUDETACH.md`
