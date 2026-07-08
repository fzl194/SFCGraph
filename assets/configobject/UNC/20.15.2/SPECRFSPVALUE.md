---
id: UNC@20.15.2@ConfigObject@SPECRFSPVALUE
type: ConfigObject
name: SPECRFSPVALUE（特征RFSP取值）
nf: UNC
version: 20.15.2
object_name: SPECRFSPVALUE
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# SPECRFSPVALUE（特征RFSP取值）

## 说明

**适用网元：SGSN、MME**

该命令用于增加一组RFSP(RAT/Frequency Selection Priority)。运营商为特定用户在HSS里签约特征RFSP(RAT/Frequency Selection Priority)作为标识， UNC 针对这些用户提供特殊处理，如：

通过 [**ADD S1ACCAREALST**](../../../区域漫游限制管理/S1模式区域漫游限制参数/增加S1模式接入控制配置（ADD S1ACCAREALST）_72345153.md) 命令禁止签约了特征RFSP的用户接入指定区域。

通过 [**ADD VOICEDEPLOY**](../../../../业务安全管理/语音业务管理/增加语音部署配置(ADD VOICEDEPLOY)_72345361.md) 命令禁止签约了特征RFSP的用户使用IMS VoPS业务。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-SPECRFSPVALUE]] · ADD SPECRFSPVALUE
- [[command/UNC/20.15.2/LST-SPECRFSPVALUE]] · LST SPECRFSPVALUE
- [[command/UNC/20.15.2/RMV-SPECRFSPVALUE]] · RMV SPECRFSPVALUE

## 证据

- 原始手册：`evidence/UNC/20.15.2/SPECRFSPVALUE.md`
- 原始手册：`evidence/UNC/20.15.2/SPECRFSPVALUE.md`
- 原始手册：`evidence/UNC/20.15.2/SPECRFSPVALUE.md`
