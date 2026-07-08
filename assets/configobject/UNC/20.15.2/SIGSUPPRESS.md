---
id: UNC@20.15.2@ConfigObject@SIGSUPPRESS
type: ConfigObject
name: SIGSUPPRESS（S11接口信令风暴抑制功能的控制与统计信息）
nf: UNC
version: 20.15.2
object_name: SIGSUPPRESS
object_kind: global_setting
applicable_nf:
- MME
status: active
---

# SIGSUPPRESS（S11接口信令风暴抑制功能的控制与统计信息）

## 说明

**适用网元：MME**

此命令用于配置S11接口故障场景下的信令风暴抑制功能。当存在因S11接口闪断或中断导致大量用户集中分离的风险时，可以开启该功能来平滑异常流程（例如Intra Handover/X2 Path Switch without S-GW Change、Service Request、Intra TAU/Combined TAU without S-GW Change流程的Modify Bearer Request处理超时，或者Intra Handover/X2 Path Switch、Intra TAU/Combined TAU流程进行上游网元选择失败）导致的用户集中分离过程，达到降低S11接口信令风暴风险目的。

## 操作本对象的命令

- [DSP SIGSUPPRESS](command/UNC/20.15.2/DSP-SIGSUPPRESS.md)
- [LST SIGSUPPRESS](command/UNC/20.15.2/LST-SIGSUPPRESS.md)
- [SET SIGSUPPRESS](command/UNC/20.15.2/SET-SIGSUPPRESS.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示S11接口信令风暴抑制功能的控制与统计信息(DSP-SIGSUPPRESS)_72225847.md`
- 原始手册：`evidence/UNC/20.15.2/查询S11接口信令风暴抑制功能参数(LST-SIGSUPPRESS)_26146168.md`
- 原始手册：`evidence/UNC/20.15.2/设置S11接口信令风暴抑制功能参数(SET-SIGSUPPRESS)_72345767.md`
