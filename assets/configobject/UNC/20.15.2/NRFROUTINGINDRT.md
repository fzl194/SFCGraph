---
id: UNC@20.15.2@ConfigObject@NRFROUTINGINDRT
type: ConfigObject
name: NRFROUTINGINDRT（选路指示器路由）
nf: UNC
version: 20.15.2
object_name: NRFROUTINGINDRT
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFROUTINGINDRT（选路指示器路由）

## 说明

**适用NF：NRF**

跨NRF的NF查询，当基于不同属性选择NF时，需要在NRF（多层NRF组网中的H-NRF或PLMN-NRF，单层NRF组网中存在东西向NRF的NRF）上配置下一跳路由，以便NRF能够寻址到其下一级NRF上所管理的NF。

该命令用于新增基于选路指示器的路由信息。当跨NRF对某个NF进行寻址时，通过本命令配置的信息可以找到当前NRF的下一级NRF路由，即目标NF所归属的NRF。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NRFROUTINGINDRT]] · ADD NRFROUTINGINDRT
- [[command/UNC/20.15.2/LST-NRFROUTINGINDRT]] · LST NRFROUTINGINDRT
- [[command/UNC/20.15.2/MOD-NRFROUTINGINDRT]] · MOD NRFROUTINGINDRT
- [[command/UNC/20.15.2/RMV-NRFROUTINGINDRT]] · RMV NRFROUTINGINDRT

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改选路指示器路由（MOD-NRFROUTINGINDRT）_09652652.md`
- 原始手册：`evidence/UNC/20.15.2/删除选路指示器路由（RMV-NRFROUTINGINDRT）_09651650.md`
- 原始手册：`evidence/UNC/20.15.2/增加选路指示器路由（ADD-NRFROUTINGINDRT）_09651833.md`
- 原始手册：`evidence/UNC/20.15.2/查询选路指示器路由（LST-NRFROUTINGINDRT）_09652642.md`
