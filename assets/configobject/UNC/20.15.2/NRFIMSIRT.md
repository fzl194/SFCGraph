---
id: UNC@20.15.2@ConfigObject@NRFIMSIRT
type: ConfigObject
name: NRFIMSIRT（IMSI号段路由）
nf: UNC
version: 20.15.2
object_name: NRFIMSIRT
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFIMSIRT（IMSI号段路由）

## 说明

**适用NF：NRF**

跨NRF的NF查询，当基于不同属性选择NF时，需要在NRF（多层NRF组网中的H-NRF或PLMN-NRF，单层NRF组网中存在东西向NRF的NRF）上配置下一跳路由，以便NRF能够寻址到其下一级NRF上所管理的NF。

该命令用于新增基于IMSI号段的路由信息。当跨NRF对某个NF进行寻址时，通过本命令配置的信息可以找到当前NRF的下一级NRF路由，即目标NF所归属的NRF。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NRFIMSIRT]] · ADD NRFIMSIRT
- [[command/UNC/20.15.2/DSP-NRFIMSIRT]] · DSP NRFIMSIRT
- [[command/UNC/20.15.2/LST-NRFIMSIRT]] · LST NRFIMSIRT
- [[command/UNC/20.15.2/MOD-NRFIMSIRT]] · MOD NRFIMSIRT
- [[command/UNC/20.15.2/RMV-NRFIMSIRT]] · RMV NRFIMSIRT

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改IMSI号段路由（MOD-NRFIMSIRT）_09652684.md`
- 原始手册：`evidence/UNC/20.15.2/删除IMSI号段路由（RMV-NRFIMSIRT）_09651646.md`
- 原始手册：`evidence/UNC/20.15.2/增加IMSI号段路由（ADD-NRFIMSIRT）_09652993.md`
- 原始手册：`evidence/UNC/20.15.2/显示IMSI路由匹配信息（DSP-NRFIMSIRT）_45604555.md`
- 原始手册：`evidence/UNC/20.15.2/查询IMSI号段路由（LST-NRFIMSIRT）_09653131.md`
