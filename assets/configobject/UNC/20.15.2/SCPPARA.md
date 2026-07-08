---
id: UNC@20.15.2@ConfigObject@SCPPARA
type: ConfigObject
name: SCPPARA（SCP参数）
nf: UNC
version: 20.15.2
object_name: SCPPARA
object_kind: global_setting
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
status: active
---

# SCPPARA（SCP参数）

## 说明

![](设置SCP参数（SET SCPPARA）_98868309.assets/notice_3.0-zh-cn_2.png)

在通过DSP SBILINKSET命令查询SCP链路存在的情况下，将DISCPOLICY设置为“LOCAL_ONLY”且未通过ADD PNFPROFILE配置SCP，或将DISCPOLICY设置为“REMOTE_ONLY”且没有满足条件的SCP注册到NRF上时，本端网元会因选不到SCP导致间接路由业务中断。

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于设置SCP参数。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-SCPPARA]] · LST SCPPARA
- [[command/UNC/20.15.2/SET-SCPPARA]] · SET SCPPARA

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SCP参数（LST-SCPPARA）_52469392.md`
- 原始手册：`evidence/UNC/20.15.2/设置SCP参数（SET-SCPPARA）_98868309.md`
