---
id: UNC@20.15.2@ConfigObject@EPSSUBQOS
type: ConfigObject
name: EPSSUBQOS（EPS签约QoS配置）
nf: UNC
version: 20.15.2
object_name: EPSSUBQOS
object_kind: entity
applicable_nf:
- SGW-C
- PGW-C
status: active
---

# EPSSUBQOS（EPS签约QoS配置）

## 说明

**适用NF：SGW-C、PGW-C**

该命令用来配置用户的签约QoS属性。当APN下使能COA功能时，RADIUS鉴权服务器会下发subscriber-qos index，UNC根据index匹配到subscriber-qos配置，用来进行用户QoS的协商控制，主动调整带宽等。

如果RADIUS鉴权服务器没有下发subscriber-qos index，则根据APN下绑定的qos-profile下的subscriber-qos index进行用户QoS的协商控制、调整带宽等。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-EPSSUBQOS]] · ADD EPSSUBQOS
- [[command/UNC/20.15.2/LST-EPSSUBQOS]] · LST EPSSUBQOS
- [[command/UNC/20.15.2/MOD-EPSSUBQOS]] · MOD EPSSUBQOS
- [[command/UNC/20.15.2/RMV-EPSSUBQOS]] · RMV EPSSUBQOS

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改EPS签约QoS配置（MOD-EPSSUBQOS）_09654145.md`
- 原始手册：`evidence/UNC/20.15.2/删除EPS签约QoS配置（RMV-EPSSUBQOS）_09653729.md`
- 原始手册：`evidence/UNC/20.15.2/增加EPS签约QoS配置（ADD-EPSSUBQOS）_09653648.md`
- 原始手册：`evidence/UNC/20.15.2/查询EPS签约QoS配置（LST-EPSSUBQOS）_09651639.md`
