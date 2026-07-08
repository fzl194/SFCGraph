---
id: UNC@20.15.2@ConfigObject@ALGPRIORITY
type: ConfigObject
name: ALGPRIORITY（算法优先级配置信息）
nf: UNC
version: 20.15.2
object_name: ALGPRIORITY
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# ALGPRIORITY（算法优先级配置信息）

## 说明

**适用网元：SGSN**

该命令用于配置算法优先级。SGSN在给RAN发送算法时会根据算法优先级排序。当 [**MOD IUAUTHCIPH**](修改Iu模式用户安全参数(MOD IUAUTHCIPH)_72345245.md) 命令中加密开关打开后，选择不同的加密算法或完整性算法，系统根据该命令配置的算法优先级对算法进行重排序。如果所有算法均未设置优先级，则为随机顺序。

## 操作本对象的命令

- [ADD ALGPRIORITY](command/UNC/20.15.2/ADD-ALGPRIORITY.md)
- [LST ALGPRIORITY](command/UNC/20.15.2/LST-ALGPRIORITY.md)
- [MOD ALGPRIORITY](command/UNC/20.15.2/MOD-ALGPRIORITY.md)
- [RMV ALGPRIORITY](command/UNC/20.15.2/RMV-ALGPRIORITY.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改算法优先级配置信息(MOD-ALGPRIORITY)_72345243.md`
- 原始手册：`evidence/UNC/20.15.2/删除算法优先级配置信息(RMV-ALGPRIORITY)_26305456.md`
- 原始手册：`evidence/UNC/20.15.2/增加算法优先级配置信息（ADD-ALGPRIORITY）_72225325.md`
- 原始手册：`evidence/UNC/20.15.2/查询算法优先级配置信息(LST-ALGPRIORITY)_26145646.md`
