---
id: UNC@20.15.2@ConfigObject@QOSCAP
type: ConfigObject
name: QOSCAP（Non-GBR承载QoS限制配置）
nf: UNC
version: 20.15.2
object_name: QOSCAP
object_kind: entity
applicable_nf:
- MME
status: active
---

# QOSCAP（Non-GBR承载QoS限制配置）

## 说明

**适用网元：MME**

该命令用于增加一条QoS限制配置记录，限制特定用户群的QoS。

在网络资源比较紧张时，为了保证大部分用户的正常业务，可以使用此命令对部分用户的QoS进行限制。

## 操作本对象的命令

- [ADD QOSCAP](command/UNC/20.15.2/ADD-QOSCAP.md)
- [LST QOSCAP](command/UNC/20.15.2/LST-QOSCAP.md)
- [MOD QOSCAP](command/UNC/20.15.2/MOD-QOSCAP.md)
- [RMV QOSCAP](command/UNC/20.15.2/RMV-QOSCAP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Non-GBR承载QoS限制配置(MOD-QOSCAP)_72345819.md`
- 原始手册：`evidence/UNC/20.15.2/删除Non-GBR承载QoS限制配置(RMV-QOSCAP)_26306030.md`
- 原始手册：`evidence/UNC/20.15.2/增加Non-GBR承载QoS限制配置(ADD-QOSCAP)_72225897.md`
- 原始手册：`evidence/UNC/20.15.2/查询Non-GBR承载QoS限制配置(LST-QOSCAP)_26146220.md`
