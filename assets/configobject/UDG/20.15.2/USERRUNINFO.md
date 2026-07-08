---
id: UDG@20.15.2@ConfigObject@USERRUNINFO
type: ConfigObject
name: USERRUNINFO（网关对IMSI/MSISDN指定的用户的运行信息进行收集配置）
nf: UDG
version: 20.15.2
object_name: USERRUNINFO
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# USERRUNINFO（网关对IMSI/MSISDN指定的用户的运行信息进行收集配置）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用于设置网关添加IMSI/MSISDN指定用户的运行信息，这些信息包括用户使用的动态规则、静态规则、BWM-RULE，以及各规则匹配次数，L7Filter匹配次数，动态规则名称和flow信息，car/shaping信息。

命令可用于系统维护人员收集指定用户在线期间，匹配系统中所配置的各种规则的次数。通过这些信息，增强了网关业务调测的分析功能和定位能力。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-USERRUNINFO]] · ADD USERRUNINFO
- [[command/UDG/20.15.2/LST-USERRUNINFO]] · LST USERRUNINFO
- [[command/UDG/20.15.2/RMV-USERRUNINFO]] · RMV USERRUNINFO

## 证据

- 原始手册：`evidence/UDG/20.15.2/USERRUNINFO.md`
- 原始手册：`evidence/UDG/20.15.2/USERRUNINFO.md`
- 原始手册：`evidence/UDG/20.15.2/USERRUNINFO.md`
