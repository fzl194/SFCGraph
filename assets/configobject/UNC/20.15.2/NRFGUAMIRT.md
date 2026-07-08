---
id: UNC@20.15.2@ConfigObject@NRFGUAMIRT
type: ConfigObject
name: NRFGUAMIRT（GUAMI路由）
nf: UNC
version: 20.15.2
object_name: NRFGUAMIRT
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFGUAMIRT（GUAMI路由）

## 说明

**适用NF：NRF**

跨NRF的NF查询，当基于不同属性选择NF时，需要在NRF（多层NRF组网中的H-NRF或PLMN-NRF，单层NRF组网中存在东西向NRF的NRF）上配置下一跳路由，以便NRF能够寻址到其下一级NRF上所管理的NF。

该命令用于新增基于GUAMI的路由信息。当跨NRF对某个NF进行寻址时，通过本命令配置的信息可以找到当前NRF的下一级NRF路由，即目标NF所归属的NRF。

## 操作本对象的命令

- [ADD NRFGUAMIRT](command/UNC/20.15.2/ADD-NRFGUAMIRT.md)
- [LST NRFGUAMIRT](command/UNC/20.15.2/LST-NRFGUAMIRT.md)
- [MOD NRFGUAMIRT](command/UNC/20.15.2/MOD-NRFGUAMIRT.md)
- [RMV NRFGUAMIRT](command/UNC/20.15.2/RMV-NRFGUAMIRT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改GUAMI路由（MOD-NRFGUAMIRT）_09653263.md`
- 原始手册：`evidence/UNC/20.15.2/删除GUAMI路由（RMV-NRFGUAMIRT）_09652546.md`
- 原始手册：`evidence/UNC/20.15.2/增加GUAMI路由（ADD-NRFGUAMIRT）_09652588.md`
- 原始手册：`evidence/UNC/20.15.2/查询GUAMI路由（LST-NRFGUAMIRT）_09654421.md`
