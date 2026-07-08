---
id: UNC@20.15.2@ConfigObject@USRPDPCAP
type: ConfigObject
name: USRPDPCAP（用户面PDP规格表）
nf: UNC
version: 20.15.2
object_name: USRPDPCAP
object_kind: global_setting
applicable_nf:
- SGSN
status: active
---

# USRPDPCAP（用户面PDP规格表）

## 说明

![](设置用户面PDP规格表(SET USRPDPCAP)_26305662.assets/notice_3.0-zh-cn_2.png)

配置过低会导致系统尚未达到真正的拥塞、过载时就不再允许新用户接入。

**适用网元：SGSN**

该命令用于设置GTP进程的PDP过载门限、PDP过载恢复门限、PDP拥塞门限、PDP拥塞恢复门限。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-USRPDPCAP]] · LST USRPDPCAP
- [[command/UNC/20.15.2/SET-USRPDPCAP]] · SET USRPDPCAP

## 证据

- 原始手册：`evidence/UNC/20.15.2/USRPDPCAP.md`
- 原始手册：`evidence/UNC/20.15.2/USRPDPCAP.md`
