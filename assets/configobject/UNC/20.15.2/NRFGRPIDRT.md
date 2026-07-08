---
id: UNC@20.15.2@ConfigObject@NRFGRPIDRT
type: ConfigObject
name: NRFGRPIDRT（NF组标识路由）
nf: UNC
version: 20.15.2
object_name: NRFGRPIDRT
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFGRPIDRT（NF组标识路由）

## 说明

**适用NF：NRF**

跨NRF的NF查询，当基于不同属性选择NF时，需要在NRF（多层NRF组网中的H-NRF或PLMN-NRF，单层NRF组网中存在东西向NRF的NRF）上配置下一跳路由，以便NRF能够寻址到其下一级NRF上所管理的NF。

该命令用于新增基于NF组标识的路由信息。当跨NRF对某个NF进行寻址时，通过本命令配置的信息可以找到当前NRF的下一级NRF路由，即目标NF所归属的NRF。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NRFGRPIDRT]] · ADD NRFGRPIDRT
- [[command/UNC/20.15.2/LST-NRFGRPIDRT]] · LST NRFGRPIDRT
- [[command/UNC/20.15.2/MOD-NRFGRPIDRT]] · MOD NRFGRPIDRT
- [[command/UNC/20.15.2/RMV-NRFGRPIDRT]] · RMV NRFGRPIDRT

## 证据

- 原始手册：`evidence/UNC/20.15.2/NRFGRPIDRT.md`
- 原始手册：`evidence/UNC/20.15.2/NRFGRPIDRT.md`
- 原始手册：`evidence/UNC/20.15.2/NRFGRPIDRT.md`
- 原始手册：`evidence/UNC/20.15.2/NRFGRPIDRT.md`
