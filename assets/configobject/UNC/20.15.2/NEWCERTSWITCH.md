---
id: UNC@20.15.2@ConfigObject@NEWCERTSWITCH
type: ConfigObject
name: NEWCERTSWITCH（证书开关状态）
nf: UNC
version: 20.15.2
object_name: NEWCERTSWITCH
object_kind: global_setting
status: active
---

# NEWCERTSWITCH（证书开关状态）

## 说明

![](设置证书开关状态（SET NEWCERTSWITCH）_10015761.assets/notice_3.0-zh-cn_2.png)

命令执行期间系统内部证书将进行切换，在此过程中通信会发生中断，节点CPU利用率会上涨20%~30%左右，证书切换完成后CPU利用率恢复正常。请确保系统处于低负载状态，节点平均CPU利用率不要超过50%，业务高峰期需谨慎执行。

设置证书开关状态，此命令用于开启或关闭证书变革相关功能。

- 命令开启，将更新内部通信证书，开启证书过期逃生能力，MAE可管理网元外部证书等。
- 命令关闭，将更新内部通信证书，关闭证书过期逃生能力，网元外部证书无法在MAE管理等。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-NEWCERTSWITCH]] · LST NEWCERTSWITCH
- [[command/UNC/20.15.2/SET-NEWCERTSWITCH]] · SET NEWCERTSWITCH

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询证书开关状态（LST-NEWCERTSWITCH）_59336676.md`
- 原始手册：`evidence/UNC/20.15.2/设置证书开关状态（SET-NEWCERTSWITCH）_10015761.md`
