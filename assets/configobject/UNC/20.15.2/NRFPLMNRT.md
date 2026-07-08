---
id: UNC@20.15.2@ConfigObject@NRFPLMNRT
type: ConfigObject
name: NRFPLMNRT（PLMN路由）
nf: UNC
version: 20.15.2
object_name: NRFPLMNRT
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFPLMNRT（PLMN路由）

## 说明

**适用NF：NRF**

跨NRF的NF查询，当基于不同属性选择NF时，需要在NRF（多层NRF组网中的H-NRF或PLMN-NRF，单层NRF组网中存在东西向NRF的NRF）上配置下一跳路由，以便NRF能够寻址到其下一级NRF上所管理的NF。

该命令用于新增基于PLMN的路由信息。当跨NRF对某个NF进行寻址时，通过本命令配置的信息可以找到当前NRF的下一级NRF路由，即目标NF所归属的NRF。

## 操作本对象的命令

- [ADD NRFPLMNRT](command/UNC/20.15.2/ADD-NRFPLMNRT.md)
- [LST NRFPLMNRT](command/UNC/20.15.2/LST-NRFPLMNRT.md)
- [MOD NRFPLMNRT](command/UNC/20.15.2/MOD-NRFPLMNRT.md)
- [RMV NRFPLMNRT](command/UNC/20.15.2/RMV-NRFPLMNRT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改PLMN路由（MOD-NRFPLMNRT）_09652637.md`
- 原始手册：`evidence/UNC/20.15.2/删除PLMN路由（RMV-NRFPLMNRT）_09653720.md`
- 原始手册：`evidence/UNC/20.15.2/增加PLMN路由（ADD-NRFPLMNRT）_09651822.md`
- 原始手册：`evidence/UNC/20.15.2/查询PLMN路由（LST-NRFPLMNRT）_09654379.md`
