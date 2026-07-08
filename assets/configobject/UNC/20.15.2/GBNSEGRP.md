---
id: UNC@20.15.2@ConfigObject@GBNSEGRP
type: ConfigObject
name: GBNSEGRP（NSE和属性模板的关联）
nf: UNC
version: 20.15.2
object_name: GBNSEGRP
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# GBNSEGRP（NSE和属性模板的关联）

## 说明

**适用网元：SGSN**

此命令用于增加一组NSE到属性模板的关联，通过属性模板来制定NSE的属性。使用 [**LST GBNSECFGPARA**](../NSE属性模板管理/查询NSE属性模板(LST GBNSECFGPARA)_72345605.md) 命令查询NSE属性模板，与该命令中配置的属性相关联。

此命令只适用于Gb over IP自动配置的场景。

## 操作本对象的命令

- [ADD GBNSEGRP](command/UNC/20.15.2/ADD-GBNSEGRP.md)
- [LST GBNSEGRP](command/UNC/20.15.2/LST-GBNSEGRP.md)
- [MOD GBNSEGRP](command/UNC/20.15.2/MOD-GBNSEGRP.md)
- [RMV GBNSEGRP](command/UNC/20.15.2/RMV-GBNSEGRP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改NSE和属性模板的关联(MOD-GBNSEGRP)_72225681.md`
- 原始手册：`evidence/UNC/20.15.2/删除NSE和属性模板的关联(RMV-GBNSEGRP)_26146002.md`
- 原始手册：`evidence/UNC/20.15.2/增加NSE和属性模板的关联(ADD-GBNSEGRP)_72345601.md`
- 原始手册：`evidence/UNC/20.15.2/查询NSE和属性模板的关联(LST-GBNSEGRP)_26305812.md`
