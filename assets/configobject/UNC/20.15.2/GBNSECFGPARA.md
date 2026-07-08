---
id: UNC@20.15.2@ConfigObject@GBNSECFGPARA
type: ConfigObject
name: GBNSECFGPARA（NSE属性模板）
nf: UNC
version: 20.15.2
object_name: GBNSECFGPARA
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# GBNSECFGPARA（NSE属性模板）

## 说明

**适用网元：SGSN**

某些局点可能不同NSE的属性也不相同，此命令用于增加NSE属性模板，以制定NSE的属性。只适用于Gb over IP自动配置的场景。

NSE属性匹配规则：一般是通过 [**ADD GBNSEGRP**](../NSE属性管理/增加NSE和属性模板的关联(ADD GBNSEGRP)_72345601.md) 命令进行NSE与属性模版的关联。对于没有关联配置的NSE，使用默认配置。系统默认模板，其“模板索引”值为“0”，其余属性参见下面参数的默认值。自动上报的NSE匹配不到其他属性时，使用该默认模板。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-GBNSECFGPARA]] · ADD GBNSECFGPARA
- [[command/UNC/20.15.2/LST-GBNSECFGPARA]] · LST GBNSECFGPARA
- [[command/UNC/20.15.2/MOD-GBNSECFGPARA]] · MOD GBNSECFGPARA
- [[command/UNC/20.15.2/RMV-GBNSECFGPARA]] · RMV GBNSECFGPARA

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改NSE属性模板(MOD-GBNSECFGPARA)_26305814.md`
- 原始手册：`evidence/UNC/20.15.2/删除NSE属性模板(RMV-GBNSECFGPARA)_72225683.md`
- 原始手册：`evidence/UNC/20.15.2/增加NSE属性模板(ADD-GBNSECFGPARA)_26146004.md`
- 原始手册：`evidence/UNC/20.15.2/查询NSE属性模板(LST-GBNSECFGPARA)_72345605.md`
