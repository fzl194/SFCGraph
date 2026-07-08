---
id: UNC@20.15.2@ConfigObject@PDPFILTERCTL
type: ConfigObject
name: PDPFILTERCTL（PDP过滤功能参数）
nf: UNC
version: 20.15.2
object_name: PDPFILTERCTL
object_kind: global_setting
applicable_nf:
- SGSN
status: active
---

# PDPFILTERCTL（PDP过滤功能参数）

## 说明

**适用网元：SGSN**

该命令用于设置PDP过滤功能相关参数，PDP过滤功能是指当用户通过RAU或者RELOCATION流程从LTE网络迁移到GU网络后，SGSN主动识别出低优先级的PDP，通过PDP去激活流程删除旧侧LTE网络专有承载对应的PDP以及低优先级的PDP。当运营商GU网络无线侧PDP能力不足时使用。

## 操作本对象的命令

- [LST PDPFILTERCTL](command/UNC/20.15.2/LST-PDPFILTERCTL.md)
- [SET PDPFILTERCTL](command/UNC/20.15.2/SET-PDPFILTERCTL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询PDP过滤功能参数(LST-PDPFILTERCTL)_72225367.md`
- 原始手册：`evidence/UNC/20.15.2/设置PDP过滤功能参数(SET-PDPFILTERCTL)_26145688.md`
