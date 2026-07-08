---
id: UDG@20.15.2@ConfigObject@HOST
type: ConfigObject
name: HOST（Host）
nf: UDG
version: 20.15.2
object_name: HOST
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# HOST（Host）

## 说明

**适用NF：PGW-U、UPF**

该命令用于配置Host信息，用以支持通过三四层过滤识别出应用层的信息，主要原理是一般web业务访问都是先发起DNS请求，系统通过对DNS报文解析获得业务的IP地址，建立七层信息与IP地址的关联关系，可以将后续访问该IP地址的业务报文关联匹配到相应的规则。

## 操作本对象的命令

- [ADD HOST](command/UDG/20.15.2/ADD-HOST.md)
- [LST HOST](command/UDG/20.15.2/LST-HOST.md)
- [MOD HOST](command/UDG/20.15.2/MOD-HOST.md)
- [RMV HOST](command/UDG/20.15.2/RMV-HOST.md)

## 关联对象

- [FILTER](configobject/UDG/20.15.2/FILTER.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改Host（MOD-HOST）_82837323.md`
- 原始手册：`evidence/UDG/20.15.2/删除Host（RMV-HOST）_86528750.md`
- 原始手册：`evidence/UDG/20.15.2/增加Host（ADD-HOST）_82837322.md`
- 原始手册：`evidence/UDG/20.15.2/查询Host（LST-HOST）_82837325.md`
