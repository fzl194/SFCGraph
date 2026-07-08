---
id: UNC@20.15.2@ConfigObject@ARPPARA
type: ConfigObject
name: ARPPARA（ARP策略参数配置）
nf: UNC
version: 20.15.2
object_name: ARPPARA
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# ARPPARA（ARP策略参数配置）

## 说明

**适用网元：SGSN**

此命令用于设置核心网侧PDP上下文中的ARP参数到无线侧ARP参数的映射规则。SGSN会根据配置的规则，将核心网侧PDP上下文中的ARP以及业务级别参数映射成无线侧的ARP参数，2G网络中SGSN向BSC发送的Create BSS Packet Flow Context Request消息（Priority信元中的Priority Level，Pre-emption Capability ，Pre-emption Vulnerability，Queuing Allowed），或SGSN向BSC发送的数传DL-UNITDATA消息（Priority信元中的Priority Level），3G网络中SGSN向RNC发送的RAB Assign消息和Relocation Request消息（包含4个信元：Priority Level，Pre-emption Capability，Pre-emption Vulnerability，Queuing Allowed）。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-ARPPARA]] · ADD ARPPARA
- [[command/UNC/20.15.2/LST-ARPPARA]] · LST ARPPARA
- [[command/UNC/20.15.2/MOD-ARPPARA]] · MOD ARPPARA
- [[command/UNC/20.15.2/RMV-ARPPARA]] · RMV ARPPARA

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改ARP策略参数配置(MOD-ARPPARA)_72345825.md`
- 原始手册：`evidence/UNC/20.15.2/删除ARP策略参数配置(RMV-ARPPARA)_26306036.md`
- 原始手册：`evidence/UNC/20.15.2/增加ARP策略参数配置(ADD-ARPPARA)_72225903.md`
- 原始手册：`evidence/UNC/20.15.2/查询ARP策略参数配置(LST-ARPPARA)_26146226.md`
