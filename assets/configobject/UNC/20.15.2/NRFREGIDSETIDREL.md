---
id: UNC@20.15.2@ConfigObject@NRFREGIDSETIDREL
type: ConfigObject
name: NRFREGIDSETIDREL（AMF区域标识和集合标识的关联关系）
nf: UNC
version: 20.15.2
object_name: NRFREGIDSETIDREL
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFREGIDSETIDREL（AMF区域标识和集合标识的关联关系）

## 说明

**适用NF：NRF**

跨NRF的NF查询，当基于不同属性选择NF时，需要在NRF（多层NRF组网中的H-NRF或PLMN-NRF，单层NRF组网中存在东西向NRF的NRF）上配置下一跳路由，以便NRF能够寻址到其下一级NRF上所管理的NF。

该命令用于新增基于AMF区域标识和集合标识的路由信息。当跨NRF对某个NF进行寻址时，通过本命令配置的信息可以找到当前NRF的下一级NRF路由，即目标NF所归属的NRF。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NRFREGIDSETIDREL]] · ADD NRFREGIDSETIDREL
- [[command/UNC/20.15.2/LST-NRFREGIDSETIDREL]] · LST NRFREGIDSETIDREL
- [[command/UNC/20.15.2/MOD-NRFREGIDSETIDREL]] · MOD NRFREGIDSETIDREL
- [[command/UNC/20.15.2/RMV-NRFREGIDSETIDREL]] · RMV NRFREGIDSETIDREL

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改AMF区域标识和集合标识的关联关系（MOD-NRFREGIDSETIDREL）_10484607.md`
- 原始手册：`evidence/UNC/20.15.2/删除AMF区域标识和集合标识的关联关系（RMV-NRFREGIDSETIDREL）_09651341.md`
- 原始手册：`evidence/UNC/20.15.2/增加AMF区域标识和集合标识的关联关系（ADD-NRFREGIDSETIDREL）_09654410.md`
- 原始手册：`evidence/UNC/20.15.2/查询AMF区域标识和集合标识的关联关系（LST-NRFREGIDSETIDREL）_09652661.md`
