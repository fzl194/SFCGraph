---
id: UNC@20.15.2@ConfigObject@NRFAMFSETIDRT
type: ConfigObject
name: NRFAMFSETIDRT（AMF集合标识路由）
nf: UNC
version: 20.15.2
object_name: NRFAMFSETIDRT
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFAMFSETIDRT（AMF集合标识路由）

## 说明

**适用NF：NRF**

跨NRF的NF查询，当基于不同属性选择NF时，需要在NRF（多层NRF组网中的H-NRF或PLMN-NRF，单层NRF组网中存在东西向NRF的NRF）上配置下一跳路由，以便NRF能够寻址到其下一级NRF上所管理的NF。

该命令用于新增基于AMF集合标识的路由信息。当跨NRF对某个NF进行寻址时，通过本命令配置的信息可以找到当前NRF的下一级NRF路由，即目标NF所归属的NRF。

## 操作本对象的命令

- [ADD NRFAMFSETIDRT](command/UNC/20.15.2/ADD-NRFAMFSETIDRT.md)
- [LST NRFAMFSETIDRT](command/UNC/20.15.2/LST-NRFAMFSETIDRT.md)
- [MOD NRFAMFSETIDRT](command/UNC/20.15.2/MOD-NRFAMFSETIDRT.md)
- [RMV NRFAMFSETIDRT](command/UNC/20.15.2/RMV-NRFAMFSETIDRT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改AMF集合标识路由（MOD-NRFAMFSETIDRT）_09653674.md`
- 原始手册：`evidence/UNC/20.15.2/删除AMF集合标识路由（RMV-NRFAMFSETIDRT）_09652995.md`
- 原始手册：`evidence/UNC/20.15.2/增加AMF集合标识路由（ADD-NRFAMFSETIDRT）_09652504.md`
- 原始手册：`evidence/UNC/20.15.2/查询AMF集合标识路由（LST-NRFAMFSETIDRT）_09652233.md`
