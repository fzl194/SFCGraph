---
id: UNC@20.15.2@ConfigObject@NRFNFTYPERT
type: ConfigObject
name: NRFNFTYPERT（NF类型路由）
nf: UNC
version: 20.15.2
object_name: NRFNFTYPERT
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFNFTYPERT（NF类型路由）

## 说明

**适用NF：NRF**

跨NRF的NF查询，当基于不同属性选择NF时，需要在NRF（多层NRF组网中的H-NRF或PLMN-NRF，单层NRF组网中存在东西向NRF的NRF）上配置下一跳路由，以便NRF能够寻址到其下一级NRF上所管理的NF。

该命令用于新增NF类型路由信息。当跨NRF对某个NF进行寻址时，通过本命令配置的信息可以找到当前NRF的下一级NRF路由，即目标NF所归属的NRF。

如果针对同一个NF类型配置了多个不同的下一跳归属NRF组名称，那么当前NRF会选取下一跳所有归属NRF组中优先级最高的NRF。

## 操作本对象的命令

- [ADD NRFNFTYPERT](command/UNC/20.15.2/ADD-NRFNFTYPERT.md)
- [LST NRFNFTYPERT](command/UNC/20.15.2/LST-NRFNFTYPERT.md)
- [RMV NRFNFTYPERT](command/UNC/20.15.2/RMV-NRFNFTYPERT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NF类型路由（RMV-NRFNFTYPERT）_25121205.md`
- 原始手册：`evidence/UNC/20.15.2/增加NF类型路由（ADD-NRFNFTYPERT）_25120875.md`
- 原始手册：`evidence/UNC/20.15.2/查询NF类型路由（LST-NRFNFTYPERT）_25121191.md`
