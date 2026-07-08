---
id: UNC@20.15.2@ConfigObject@PCCCHGMODEBYPCFID
type: ConfigObject
name: PCCCHGMODEBYPCFID（基于PCF的计费策略接口类型）
nf: UNC
version: 20.15.2
object_name: PCCCHGMODEBYPCFID
object_kind: entity
applicable_nf:
- SMF
status: active
---

# PCCCHGMODEBYPCFID（基于PCF的计费策略接口类型）

## 说明

![](增加基于PCF的计费策略接口类型（ADD PCCCHGMODEBYPCFID）_72001542.assets/notice_3.0-zh-cn_2.png)

配置基于PCF的计费策略接口类型不当可能导致PCC用户选择错误接口的PCRF/PCF服务器，进而影响用户使用业务，比如用户无法正常激活。

**适用NF：SMF**

增加基于PCF的计费策略接口类型。当需要基于PCF实例标识调整用户最终使用的策略接口类型 (N7/Gx) 或计费接口类型 (N40/GaGy) 时，可以通过此命令进行配置。

## 操作本对象的命令

- [ADD PCCCHGMODEBYPCFID](command/UNC/20.15.2/ADD-PCCCHGMODEBYPCFID.md)
- [LST PCCCHGMODEBYPCFID](command/UNC/20.15.2/LST-PCCCHGMODEBYPCFID.md)
- [MOD PCCCHGMODEBYPCFID](command/UNC/20.15.2/MOD-PCCCHGMODEBYPCFID.md)
- [RMV PCCCHGMODEBYPCFID](command/UNC/20.15.2/RMV-PCCCHGMODEBYPCFID.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改基于PCF的计费策略接口类型（MOD-PCCCHGMODEBYPCFID）_72001551.md`
- 原始手册：`evidence/UNC/20.15.2/删除基于PCF的计费策略接口类型（RMV-PCCCHGMODEBYPCFID）_72001554.md`
- 原始手册：`evidence/UNC/20.15.2/增加基于PCF的计费策略接口类型（ADD-PCCCHGMODEBYPCFID）_72001542.md`
- 原始手册：`evidence/UNC/20.15.2/查询基于PCF的计费策略接口类型（LST-PCCCHGMODEBYPCFID）_96242347.md`
