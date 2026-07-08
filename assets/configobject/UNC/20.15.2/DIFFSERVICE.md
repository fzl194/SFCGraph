---
id: UNC@20.15.2@ConfigObject@DIFFSERVICE
type: ConfigObject
name: DIFFSERVICE（差异化服务接入门限）
nf: UNC
version: 20.15.2
object_name: DIFFSERVICE
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# DIFFSERVICE（差异化服务接入门限）

## 说明

**适用网元：SGSN**

该命令用于增加差异化服务配置信息。差异化服务是指针对不同优先级的用户，提供不同的接入控制策略，保证优先级别高的用户具有优先使用网络资源的权力。 当差异化服务的License开启时，如果用户接入比例或者系统PDP比例大于等于差异化服务配置信息中的门限，则启动差异化服务功能，否则不启动差异化服务功能。差异化服务功能启动后系统依据用户级别或者业务级别控制不同用户接入或者激活。

用户接入比例等于系统当前用户数量除以系统容量得到系统资源使用情况比例。

系统PDP比例等于PDP（Packet Data Protocol）数量除以系统容量得到系统资源使用情况比例。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-DIFFSERVICE]] · ADD DIFFSERVICE
- [[command/UNC/20.15.2/DSP-DIFFSERVICE]] · DSP DIFFSERVICE
- [[command/UNC/20.15.2/LST-DIFFSERVICE]] · LST DIFFSERVICE
- [[command/UNC/20.15.2/MOD-DIFFSERVICE]] · MOD DIFFSERVICE
- [[command/UNC/20.15.2/RMV-DIFFSERVICE]] · RMV DIFFSERVICE

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改差异化服务接入门限(MOD-DIFFSERVICE)_26305484.md`
- 原始手册：`evidence/UNC/20.15.2/删除差异化服务接入门限(RMV-DIFFSERVICE)_72225353.md`
- 原始手册：`evidence/UNC/20.15.2/增加差异化服务接入门限(ADD-DIFFSERVICE)_26145674.md`
- 原始手册：`evidence/UNC/20.15.2/显示差异化服务信息(DSP-DIFFSERVICE)_26145676.md`
- 原始手册：`evidence/UNC/20.15.2/查询差异化服务接入门限(LST-DIFFSERVICE)_72345271.md`
