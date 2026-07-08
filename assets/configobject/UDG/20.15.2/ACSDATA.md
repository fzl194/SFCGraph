---
id: UDG@20.15.2@ConfigObject@ACSDATA
type: ConfigObject
name: ACSDATA（ACS管理服务数据）
nf: UDG
version: 20.15.2
object_name: ACSDATA
object_kind: action
status: active
---

# ACSDATA（ACS管理服务数据）

## 说明

![](清除ACS管理服务数据(CLR ACSDATA)_98165797.assets/notice_3.0-zh-cn.png)

该命令将清除ACS管理服务的数据并导致业务中断，需谨慎执行。

该命令用于清除ACS管理服务数据。

> **说明**
> - 该命令执行后，对应的服务会在3分钟内无法通过ACS进行配置管理，3分钟后服务开始向ACS进行注册，注册成功后恢复该服务的配置管理业务。
> - 当执行该命令删除服务数据后，若对应的服务发生重启，则会重新向ACS注册，注册成功后恢复该服务的配置管理业务。
> - 当执行该命令后，若ACS发生重启、主备倒换等操作，所有服务重新向ACS进行注册，注册成功后恢复所有服务的配置管理业务。
> - 该命令在清除ACS管理服务的数据时，仅清除微服务在ACS中的数据。
> - 命令执行后，需要通过**DSP ACSSYNCINFO**查询对应微服务是否清理完成。

## 操作本对象的命令

- [[command/UDG/20.15.2/CLR-ACSDATA]] · CLR ACSDATA

## 证据

- 原始手册：`evidence/UDG/20.15.2/ACSDATA.md`
