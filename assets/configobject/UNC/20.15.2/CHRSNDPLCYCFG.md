---
id: UNC@20.15.2@ConfigObject@CHRSNDPLCYCFG
type: ConfigObject
name: CHRSNDPLCYCFG（CHR传输策略控制参数）
nf: UNC
version: 20.15.2
object_name: CHRSNDPLCYCFG
object_kind: global_setting
applicable_nf:
- SGSN
- MME
status: active
---

# CHRSNDPLCYCFG（CHR传输策略控制参数）

## 说明

**适用网元：SGSN、MME**

该命令用于设置CHR传输策略控制参数，通过配置自定义策略，以满足客户允许指定用户传输CHR的需求。

本命令中CHR传输策略选择为 “整系统传输” 时，按照 [**SET CHRSTORECFG**](../CHR存盘管理/设置CHR存盘配置（SET CHRSTORECFG）_26145616.md) 配置的整系统产生的CHR都传输至CloudUDN；CHR传输策略选择为 “自定义策略传输” 时，只有满足 [**ADD CHRSNDPLCY**](增加CHR传输策略(ADD CHRSNDPLCY)_72345209.md) 指定策略的用户的CHR传输至CloudUDN。

## 操作本对象的命令

- [LST CHRSNDPLCYCFG](command/UNC/20.15.2/LST-CHRSNDPLCYCFG.md)
- [SET CHRSNDPLCYCFG](command/UNC/20.15.2/SET-CHRSNDPLCYCFG.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CHR传输策略控制参数(LST-CHRSNDPLCYCFG)_72345211.md`
- 原始手册：`evidence/UNC/20.15.2/设置CHR传输策略控制参数(SET-CHRSNDPLCYCFG)_26305424.md`
