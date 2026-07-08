---
id: UNC@20.15.2@ConfigObject@S1ALGPRIORITY
type: ConfigObject
name: S1ALGPRIORITY（S1模式加密和完整性算法优先级配置信息）
nf: UNC
version: 20.15.2
object_name: S1ALGPRIORITY
object_kind: entity
applicable_nf:
- MME
status: active
---

# S1ALGPRIORITY（S1模式加密和完整性算法优先级配置信息）

## 说明

**适用网元：MME**

该命令用于增加S1模式加密和完整性算法优先级的信息。MME根据此命令配置不同加密算法或完整性算法的算法优先级，在UE和MME同时支持此算法的前提下，选择优先级最高的算法发送给UE。如果所有算法均未设置优先级，系统会根据四种算法的默认优先级（从高到低分别为AES、SNOW 3G、ZUC、空加密/空完整性算法）和UE进行协商，最终确定采用的加密/完整性算法。

## 操作本对象的命令

- [ADD S1ALGPRIORITY](command/UNC/20.15.2/ADD-S1ALGPRIORITY.md)
- [LST S1ALGPRIORITY](command/UNC/20.15.2/LST-S1ALGPRIORITY.md)
- [MOD S1ALGPRIORITY](command/UNC/20.15.2/MOD-S1ALGPRIORITY.md)
- [RMV S1ALGPRIORITY](command/UNC/20.15.2/RMV-S1ALGPRIORITY.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改S1模式加密和完整性算法优先级配置信息(MOD-S1ALGPRIORITY)_26145652.md`
- 原始手册：`evidence/UNC/20.15.2/删除S1模式加密和完整性算法优先级配置信息(RMV-S1ALGPRIORITY)_72345249.md`
- 原始手册：`evidence/UNC/20.15.2/增加S1模式加密和完整性算法优先级配置信息(ADD-S1ALGPRIORITY)_26305462.md`
- 原始手册：`evidence/UNC/20.15.2/查询S1模式加密和完整性算法优先级配置信息(LST-S1ALGPRIORITY)_72225333.md`
