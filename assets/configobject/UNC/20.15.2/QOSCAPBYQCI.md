---
id: UNC@20.15.2@ConfigObject@QOSCAPBYQCI
type: ConfigObject
name: QOSCAPBYQCI（基于QCI的Non-GBR承载QoS限制配置）
nf: UNC
version: 20.15.2
object_name: QOSCAPBYQCI
object_kind: entity
applicable_nf:
- MME
status: active
---

# QOSCAPBYQCI（基于QCI的Non-GBR承载QoS限制配置）

## 说明

**适用网元：MME**

该命令用于根据用户范围及承载的QCI配置Non-GBR承载QoS限制。相比 [**ADD QOSCAP**](../Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md) 和 **[ADD QOSCAPGBR](../GBR承载QoS限制/增加GBR承载QoS限制配置(ADD QOSCAPGBR)_26146216.md)** 只能指定用户范围，本命令可根据用户号段和承载的QCI联合定义本地QoS策略，为运营商提供更加灵活的QoS控制

## 操作本对象的命令

- [ADD QOSCAPBYQCI](command/UNC/20.15.2/ADD-QOSCAPBYQCI.md)
- [LST QOSCAPBYQCI](command/UNC/20.15.2/LST-QOSCAPBYQCI.md)
- [MOD QOSCAPBYQCI](command/UNC/20.15.2/MOD-QOSCAPBYQCI.md)
- [RMV QOSCAPBYQCI](command/UNC/20.15.2/RMV-QOSCAPBYQCI.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改基于QCI的Non-GBR承载QoS限制配置(MOD-QOSCAPBYQCI)_72345821.md`
- 原始手册：`evidence/UNC/20.15.2/删除基于QCI的Non-GBR承载QoS限制配置(RMV-QOSCAPBYQCI)_26146222.md`
- 原始手册：`evidence/UNC/20.15.2/增加基于QCI的Non-GBR承载QoS限制配置(ADD-QOSCAPBYQCI)_26306032.md`
- 原始手册：`evidence/UNC/20.15.2/查询基于QCI的Non-GBR承载QoS限制配置(LST-QOSCAPBYQCI)_72225901.md`
