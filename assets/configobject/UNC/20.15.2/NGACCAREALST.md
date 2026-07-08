---
id: UNC@20.15.2@ConfigObject@NGACCAREALST
type: ConfigObject
name: NGACCAREALST（5G接入限制区域列表）
nf: UNC
version: 20.15.2
object_name: NGACCAREALST
object_kind: entity
applicable_nf:
- AMF
status: active
---

# NGACCAREALST（5G接入限制区域列表）

## 说明

**适用NF：AMF**

该命令用于增加5G接入限制区域信息。AMF可基于用户当前驻留的位置和本命令的配置，控制是否允许用户接入。

本限制功能涉及流程参考WSFD-105003 区域漫游限制（适用AMF）实现原理章节。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NGACCAREALST]] · ADD NGACCAREALST
- [[command/UNC/20.15.2/LST-NGACCAREALST]] · LST NGACCAREALST
- [[command/UNC/20.15.2/MOD-NGACCAREALST]] · MOD NGACCAREALST
- [[command/UNC/20.15.2/RMV-NGACCAREALST]] · RMV NGACCAREALST

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改5G接入限制区域列表（MOD-NGACCAREALST）_44007375.md`
- 原始手册：`evidence/UNC/20.15.2/删除5G接入限制区域列表（RMV-NGACCAREALST）_44007640.md`
- 原始手册：`evidence/UNC/20.15.2/增加5G接入限制区域列表（ADD-NGACCAREALST）_44006447.md`
- 原始手册：`evidence/UNC/20.15.2/查询5G接入限制区域列表（LST-NGACCAREALST）_44006984.md`
