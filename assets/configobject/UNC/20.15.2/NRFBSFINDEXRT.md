---
id: UNC@20.15.2@ConfigObject@NRFBSFINDEXRT
type: ConfigObject
name: NRFBSFINDEXRT（BSFINDEX路由）
nf: UNC
version: 20.15.2
object_name: NRFBSFINDEXRT
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFBSFINDEXRT（BSFINDEX路由）

## 说明

**适用NF：NRF**

跨NRF的NF查询，当基于不同属性选择NF时，需要在NRF（多层NRF组网中的H-NRF或PLMN-NRF，单层NRF组网中存在东西向NRF的NRF）上配置下一跳路由，以便NRF能够寻址到其下一级NRF上所管理的NF。

该命令用于新增选择BSF时的路由实例信息。当跨NRF对BSF进行寻址时，通过本命令配置的信息可以找到当前NRF的下一级NRF路由，即目标BSF所归属的NRF。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NRFBSFINDEXRT]] · ADD NRFBSFINDEXRT
- [[command/UNC/20.15.2/LST-NRFBSFINDEXRT]] · LST NRFBSFINDEXRT
- [[command/UNC/20.15.2/RMV-NRFBSFINDEXRT]] · RMV NRFBSFINDEXRT

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除BSFINDEX路由（RMV-NRFBSFINDEXRT）_44007679.md`
- 原始手册：`evidence/UNC/20.15.2/增加BSFINDEX路由（ADD-NRFBSFINDEXRT）_44006485.md`
- 原始手册：`evidence/UNC/20.15.2/查询BSFINDEX路由（LST-NRFBSFINDEXRT）_44007034.md`
