---
id: UNC@20.15.2@ConfigObject@NFDISCSRVLBSW
type: ConfigObject
name: NFDISCSRVLBSW（服务发现Service负载均衡功能）
nf: UNC
version: 20.15.2
object_name: NFDISCSRVLBSW
object_kind: entity
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
status: active
---

# NFDISCSRVLBSW（服务发现Service负载均衡功能）

## 说明

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于开启或关闭服务发现时的NF Service负载均衡功能。业务进行服务发现时，如果未指定NF Service负载均衡策略，则根据此命令决定是否需要NF Service负载均衡；如果已指定NF Service负载均衡策略，则此命令不生效。

## 操作本对象的命令

- [ADD NFDISCSRVLBSW](command/UNC/20.15.2/ADD-NFDISCSRVLBSW.md)
- [LST NFDISCSRVLBSW](command/UNC/20.15.2/LST-NFDISCSRVLBSW.md)
- [MOD NFDISCSRVLBSW](command/UNC/20.15.2/MOD-NFDISCSRVLBSW.md)
- [RMV NFDISCSRVLBSW](command/UNC/20.15.2/RMV-NFDISCSRVLBSW.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改服务发现Service负载均衡功能（MOD-NFDISCSRVLBSW）_04536948.md`
- 原始手册：`evidence/UNC/20.15.2/删除服务发现Service负载均衡功能（RMV-NFDISCSRVLBSW）_04217460.md`
- 原始手册：`evidence/UNC/20.15.2/增加服务发现NF-Service负载均衡开关（ADD-NFDISCSRVLBSW）_04217452.md`
- 原始手册：`evidence/UNC/20.15.2/查询服务发现Service负载均衡功能（LST-NFDISCSRVLBSW）_57337229.md`
