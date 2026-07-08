---
id: UNC@20.15.2@ConfigObject@NRFWILDCARDSTRRT
type: ConfigObject
name: NRFWILDCARDSTRRT（分层互联信元字符串通配属性路由）
nf: UNC
version: 20.15.2
object_name: NRFWILDCARDSTRRT
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFWILDCARDSTRRT（分层互联信元字符串通配属性路由）

## 说明

![](增加分层互联信元字符串通配属性路由（ADD NRFWILDCARDSTRRT）_96241787.assets/notice_3.0-zh-cn_2.png)

通配字符串配置错误，可能会导致业务路由到其他大区或者省份，引起业务不可用。

**适用NF：NRF**

跨NRF的NF查询，当基于不同属性选择NF时，需要在NRF（多层NRF组网中的H-NRF或PLMN-NRF，单层NRF组网中存在东西向NRF的NRF）上配置下一跳路由，以便NRF能够寻址到其下一级NRF上所管理的NF。

该命令用于配置新增分层互联信元字符串通配属性路由。当需要对某个NF进行跨NRF寻址时，通过本命令配置的信息可以找到当前NRF的下一级NRF路由，即目标NF所归属的NRF。

## 操作本对象的命令

- [ADD NRFWILDCARDSTRRT](command/UNC/20.15.2/ADD-NRFWILDCARDSTRRT.md)
- [LST NRFWILDCARDSTRRT](command/UNC/20.15.2/LST-NRFWILDCARDSTRRT.md)
- [RMV NRFWILDCARDSTRRT](command/UNC/20.15.2/RMV-NRFWILDCARDSTRRT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除分层互联信元字符串通配属性路由（RMV-NRFWILDCARDSTRRT）_96242905.md`
- 原始手册：`evidence/UNC/20.15.2/增加分层互联信元字符串通配属性路由（ADD-NRFWILDCARDSTRRT）_96241787.md`
- 原始手册：`evidence/UNC/20.15.2/查询分层互联信元字符串通配属性路由（LST-NRFWILDCARDSTRRT）_96242330.md`
