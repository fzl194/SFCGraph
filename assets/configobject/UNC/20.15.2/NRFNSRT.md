---
id: UNC@20.15.2@ConfigObject@NRFNSRT
type: ConfigObject
name: NRFNSRT（网络切片的路由）
nf: UNC
version: 20.15.2
object_name: NRFNSRT
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFNSRT（网络切片的路由）

## 说明

**适用NF：NRF**

跨NRF的NF查询，当基于不同属性选择NF时，需要在NRF（多层NRF组网中的H-NRF或PLMN-NRF，单层NRF组网中存在东西向NRF的NRF）上配置下一跳路由，以便NRF能够寻址到其下一级NRF上所管理的NF。

该命令用于新增基于网络切片的路由信息。当跨NRF对某个NF进行寻址时，通过本命令配置的信息可以找到当前NRF的下一级NRF路由，即目标NF所归属的NRF。

如果针对同一个网络切片了多个不同的下一跳归属NRF组名称，那么当前NRF会选取下一跳所有归属NRF组中优先级最高的NRF。

## 操作本对象的命令

- [ADD NRFNSRT](command/UNC/20.15.2/ADD-NRFNSRT.md)
- [LST NRFNSRT](command/UNC/20.15.2/LST-NRFNSRT.md)
- [MOD NRFNSRT](command/UNC/20.15.2/MOD-NRFNSRT.md)
- [RMV NRFNSRT](command/UNC/20.15.2/RMV-NRFNSRT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改网络切片的路由（MOD-NRFNSRT）_86184263.md`
- 原始手册：`evidence/UNC/20.15.2/删除网络切片的路由（RMV-NRFNSRT）_09652206.md`
- 原始手册：`evidence/UNC/20.15.2/增加网络切片的路由（ADD-NRFNSRT）_09652449.md`
- 原始手册：`evidence/UNC/20.15.2/查询网络切片的路由（LST-NRFNSRT）_09653222.md`
