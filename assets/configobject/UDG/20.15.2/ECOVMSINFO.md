---
id: UDG@20.15.2@ConfigObject@ECOVMSINFO
type: ConfigObject
name: ECOVMSINFO（VM的CPU节能策略）
nf: UDG
version: 20.15.2
object_name: ECOVMSINFO
object_kind: query_target
status: active
---

# ECOVMSINFO（VM的CPU节能策略）

## 说明

该命令用于在开启节能策略后，查询当前VM的CPU节能策略。

> **说明**
> - 此命令仅在虚机场景下支持。
> - 部分场景下，VM实际节能策略可能与网元期望策略不同，此时，最长需要24小时可自动刷新为期望策略。此时，可通过执行[**SET ECOPOLICY**](设置全局的CPU调频和休眠策略（SET ECOPOLICY）_97016349.md)命令先关闭、再开启节能功能，使VM实际节能策略快速恢复（约2分钟）。
>
> - VNF更新操作会将网元所有VM的实际节能策略恢复为VNFD模板定义的初始节能策略。
> - VM重建、对没有部署Pod的VM进行上下电操作，会将该VM的实际节能策略恢复为VNFD模板定义的初始节能策略。

## 操作本对象的命令

- [[command/UDG/20.15.2/DSP-ECOVMSINFO]] · DSP ECOVMSINFO

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示VM的CPU节能策略（DSP-ECOVMSINFO）_96831057.md`
