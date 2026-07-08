---
id: UDG@20.15.2@ConfigObject@BWMRULE
type: ConfigObject
name: BWMRULE（带宽管理规则）
nf: UDG
version: 20.15.2
object_name: BWMRULE
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# BWMRULE（带宽管理规则）

## 说明

**适用NF：PGW-U、UPF**

该命令用于增加一条用户组或用户的业务带宽管理规则。规则包括用户组级默认、特定规则和用户级默认、特定规则。当运营商希望基于用户组或用户级进行精细化带宽控制时，则使用该命令配置用户组和用户级的规则，并配置业务类型、用户属性和时间段及相应的带宽控制器。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-BWMRULE]] · ADD BWMRULE
- [[command/UDG/20.15.2/LST-BWMRULE]] · LST BWMRULE
- [[command/UDG/20.15.2/MOD-BWMRULE]] · MOD BWMRULE
- [[command/UDG/20.15.2/RMV-BWMRULE]] · RMV BWMRULE

## 关联对象

- [[configobject/UDG/20.15.2/BWMCONTROLLER]] · BWMCONTROLLER
- [[configobject/UDG/20.15.2/BWMSERVICE]] · BWMSERVICE
- [[configobject/UDG/20.15.2/BWMUSERGROUP]] · BWMUSERGROUP
- [[configobject/UDG/20.15.2/TIMERANGE]] · TIMERANGE

## 证据

- 原始手册：`evidence/UDG/20.15.2/BWMRULE.md`
- 原始手册：`evidence/UDG/20.15.2/BWMRULE.md`
- 原始手册：`evidence/UDG/20.15.2/BWMRULE.md`
- 原始手册：`evidence/UDG/20.15.2/BWMRULE.md`
