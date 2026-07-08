---
id: UNC@20.15.2@ConfigObject@AUTONSE
type: ConfigObject
name: AUTONSE（自动上报的NSE）
nf: UNC
version: 20.15.2
object_name: AUTONSE
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# AUTONSE（自动上报的NSE）

## 说明

![](删除自动上报的NSE(RMV AUTONSE)_72225673.assets/notice_3.0-zh-cn_2.png)

删除AUTONSE将导致NSE相关业务无法使用。

**适用网元：SGSN**

此命令用于删除自动上报的动态Gb over IP的NSE。自动上报的动态Gb over IP的NSE的信息请通过 [**DSP NSE**](../../信令实体管理/显示NSE属性信息（DSP NSE）_26146030.md) 命令查询。

## 操作本对象的命令

- [RMV AUTONSE](command/UNC/20.15.2/RMV-AUTONSE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除自动上报的NSE(RMV-AUTONSE)_72225673.md`
