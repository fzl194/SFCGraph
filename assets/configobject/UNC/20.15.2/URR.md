---
id: UNC@20.15.2@ConfigObject@URR
type: ConfigObject
name: URR
nf: UNC
version: 20.15.2
object_name: URR
object_kind: entity
applicable_nf:
- PGW-C
- SMF
status: active
---

# URR

## 说明

**适用NF：PGW-C、SMF**

该命令用于增加使用量上报规则信息，通过该命令可以针对不同应用类型的数据采取不同的上报规则。URR即Usage Reporting Rule用量上报规则，一般对应用户报文的时长、流量等上报控制规则。URR可以通过ADD URRGROUP命令配置到使用量上报规则组。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-URR]] · ADD URR
- [[command/UNC/20.15.2/LST-URR]] · LST URR
- [[command/UNC/20.15.2/MOD-URR]] · MOD URR
- [[command/UNC/20.15.2/RMV-URR]] · RMV URR

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改URR（MOD-URR）_09897159.md`
- 原始手册：`evidence/UNC/20.15.2/删除URR（RMV-URR）_09897160.md`
- 原始手册：`evidence/UNC/20.15.2/增加URR（ADD-URR）_09897158.md`
- 原始手册：`evidence/UNC/20.15.2/查询URR（LST-URR）_09897161.md`
