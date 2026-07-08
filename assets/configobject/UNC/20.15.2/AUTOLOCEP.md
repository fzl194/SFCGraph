---
id: UNC@20.15.2@ConfigObject@AUTOLOCEP
type: ConfigObject
name: AUTOLOCEP（自动上报的NSE下的本端端点）
nf: UNC
version: 20.15.2
object_name: AUTOLOCEP
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# AUTOLOCEP（自动上报的NSE下的本端端点）

## 说明

![](删除自动上报的NSE下的本端端点(RMV AUTOLOCEP)_26145994.assets/notice_3.0-zh-cn_2.png)

- 此命令会导致删除端点的IPNSVC链路无法再承载业务。
- 删除NSE下唯一的本端端点会导致NSE相关业务不可用。

**适用网元：SGSN**

此命令用于删除自动上报的动态Gb over IP的NSE下的本端端点。自动上报的动态Gb over IP的NSE的属性和端点信息请通过 [**DSP NSE**](../../信令实体管理/显示NSE属性信息（DSP NSE）_26146030.md) 命令和 [**DSP IPNSVC**](../../Gb over IP管理/IP网络NSVC链路管理/显示IP网络NSVC配置表(DSP IPNSVC)_72345609.md) 命令查询。

## 操作本对象的命令

- [RMV AUTOLOCEP](command/UNC/20.15.2/RMV-AUTOLOCEP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除自动上报的NSE下的本端端点(RMV-AUTOLOCEP)_26145994.md`
