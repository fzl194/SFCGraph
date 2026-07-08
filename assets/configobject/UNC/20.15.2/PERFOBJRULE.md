---
id: UNC@20.15.2@ConfigObject@PERFOBJRULE
type: ConfigObject
name: PERFOBJRULE（性能对象规则）
nf: UNC
version: 20.15.2
object_name: PERFOBJRULE
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# PERFOBJRULE（性能对象规则）

## 说明

**适用网元：SGSN、MME**

该命令用于特定性能统计对象规则的配置，当前仅支持TAI组对象规则的配置。

TAI组是将同一区域范围内的TAI组合在一起。当配置了TAI组规则后，属于该规则下的TAI，性能指标均会统计到该TAI组对象下。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PERFOBJRULE]] · ADD PERFOBJRULE
- [[command/UNC/20.15.2/LST-PERFOBJRULE]] · LST PERFOBJRULE
- [[command/UNC/20.15.2/MOD-PERFOBJRULE]] · MOD PERFOBJRULE
- [[command/UNC/20.15.2/RMV-PERFOBJRULE]] · RMV PERFOBJRULE

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改性能对象规则(MOD-PERFOBJRULE)_72345795.md`
- 原始手册：`evidence/UNC/20.15.2/删除性能对象规则(RMV-PERFOBJRULE)_26306006.md`
- 原始手册：`evidence/UNC/20.15.2/增加性能对象规则(ADD-PERFOBJRULE)_72225873.md`
- 原始手册：`evidence/UNC/20.15.2/查询性能对象规则(LST-PERFOBJRULE)_26146196.md`
