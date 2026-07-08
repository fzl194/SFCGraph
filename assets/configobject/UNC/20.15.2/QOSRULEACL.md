---
id: UNC@20.15.2@ConfigObject@QOSRULEACL
type: ConfigObject
name: QOSRULEACL（流分类下删除ACL规则组）
nf: UNC
version: 20.15.2
object_name: QOSRULEACL
object_kind: entity
status: active
---

# QOSRULEACL（流分类下删除ACL规则组）

## 说明

该命令用来配置基于IPv4或IPv6的ACL规则进行复杂流分类的匹配规则；当某个接口需要根据接收报文的源IP、目的IP、源端口、目的端口和协议类型对报文进行分类时，可以对该接口通过引用定义的ACL来满足。即先定义ACL以及配置规则，然后在流分类下配置该命令实现复杂流分类。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-QOSRULEACL]] · ADD QOSRULEACL
- [[command/UNC/20.15.2/LST-QOSRULEACL]] · LST QOSRULEACL
- [[command/UNC/20.15.2/RMV-QOSRULEACL]] · RMV QOSRULEACL

## 证据

- 原始手册：`evidence/UNC/20.15.2/流分类下删除ACL规则组（RMV-QOSRULEACL）_00841669.md`
- 原始手册：`evidence/UNC/20.15.2/流分类下增加ACL规则组（ADD-QOSRULEACL）_00600841.md`
- 原始手册：`evidence/UNC/20.15.2/流分类下查询ACL规则组（LST-QOSRULEACL）_49801690.md`
