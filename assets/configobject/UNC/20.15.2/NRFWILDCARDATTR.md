---
id: UNC@20.15.2@ConfigObject@NRFWILDCARDATTR
type: ConfigObject
name: NRFWILDCARDATTR（分层互联通配属性）
nf: UNC
version: 20.15.2
object_name: NRFWILDCARDATTR
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFWILDCARDATTR（分层互联通配属性）

## 说明

**适用NF：NRF**

该命令用于在NRF新增分层互联通配属性，以减少分层互联路由信息的配置量。

若此命令与ADD NRFTAIRT命令配置了多个不同的下一跳归属NRF组名称，那么当前NRF会选取下一跳所有归属NRF组中优先级最高的NRF。

## 操作本对象的命令

- [ADD NRFWILDCARDATTR](command/UNC/20.15.2/ADD-NRFWILDCARDATTR.md)
- [LST NRFWILDCARDATTR](command/UNC/20.15.2/LST-NRFWILDCARDATTR.md)
- [MOD NRFWILDCARDATTR](command/UNC/20.15.2/MOD-NRFWILDCARDATTR.md)
- [RMV NRFWILDCARDATTR](command/UNC/20.15.2/RMV-NRFWILDCARDATTR.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改分层互联通配属性（MOD-NRFWILDCARDATTR）_09652967.md`
- 原始手册：`evidence/UNC/20.15.2/删除分层互联通配属性（RMV-NRFWILDCARDATTR）_09652345.md`
- 原始手册：`evidence/UNC/20.15.2/增加分层互联通配属性（ADD-NRFWILDCARDATTR）_09653194.md`
- 原始手册：`evidence/UNC/20.15.2/查询分层互联通配属性（LST-NRFWILDCARDATTR）_09652485.md`
