---
id: UNC@20.15.2@ConfigObject@QOSTRANS
type: ConfigObject
name: QOSTRANS（签约QoS转换配置）
nf: UNC
version: 20.15.2
object_name: QOSTRANS
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# QOSTRANS（签约QoS转换配置）

## 说明

**适用网元：SGSN**

该命令用于增加QoS转换功能记录。当SGSN、GGSN、RNC、MS等网元支持Rel7格式的QoS，但是HLR只支持Rel5或者更早版本的QoS时，通过QoS转换特性可以在不升级HLR的情况下使用HSPA+功能。当MS附着到SGSN时，HLR给SGSN发送签约数据，SGSN根据转换规则，把签约请求中携带的Rel5或Rel99版本的QoS转换为Rel7版本的QoS，保存在用户的签约数据中，MS就会使用Rel7版本的QoS发起业务请求。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-QOSTRANS]] · ADD QOSTRANS
- [[command/UNC/20.15.2/LST-QOSTRANS]] · LST QOSTRANS
- [[command/UNC/20.15.2/RMV-QOSTRANS]] · RMV QOSTRANS

## 证据

- 原始手册：`evidence/UNC/20.15.2/QOSTRANS.md`
- 原始手册：`evidence/UNC/20.15.2/QOSTRANS.md`
- 原始手册：`evidence/UNC/20.15.2/QOSTRANS.md`
