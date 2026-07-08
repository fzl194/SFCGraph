---
id: UNC@20.15.2@ConfigObject@EPSREMARK
type: ConfigObject
name: EPSREMARK（EPS QoS到TOS/DSCP的映射规则）
nf: UNC
version: 20.15.2
object_name: EPSREMARK
object_kind: entity
applicable_nf:
- SGW-C
- PGW-C
status: active
---

# EPSREMARK（EPS QoS到TOS/DSCP的映射规则）

## 说明

**适用NF：SGW-C、PGW-C**

该命令用来增加在SAE架构下，QoS参数到IP报头中的DSCP（区别服务编码点）/TOS（服务类型）的映射规则，用户的数据将根据映射得到的DSCP（区别服务编码点）/TOS（服务类型）中的参数值进行转发。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-EPSREMARK]] · ADD EPSREMARK
- [[command/UNC/20.15.2/LST-EPSREMARK]] · LST EPSREMARK
- [[command/UNC/20.15.2/MOD-EPSREMARK]] · MOD EPSREMARK
- [[command/UNC/20.15.2/RMV-EPSREMARK]] · RMV EPSREMARK

## 证据

- 原始手册：`evidence/UNC/20.15.2/EPSREMARK.md`
- 原始手册：`evidence/UNC/20.15.2/EPSREMARK.md`
- 原始手册：`evidence/UNC/20.15.2/EPSREMARK.md`
- 原始手册：`evidence/UNC/20.15.2/EPSREMARK.md`
