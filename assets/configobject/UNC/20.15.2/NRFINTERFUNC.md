---
id: UNC@20.15.2@ConfigObject@NRFINTERFUNC
type: ConfigObject
name: NRFINTERFUNC（国际漫游功能参数）
nf: UNC
version: 20.15.2
object_name: NRFINTERFUNC
object_kind: global_setting
applicable_nf:
- NRF
status: active
---

# NRFINTERFUNC（国际漫游功能参数）

## 说明

![](设置国际漫游功能参数（SET NRFINTERFUNC）_24796840.assets/notice_3.0-zh-cn_2.png)

若ROAMINSUPIWLSW置为FUNC_ON而未通过ADD ROAMINSUPIWL配置漫入SUPI服务发现白名单会导致漫入场景下在I-NRF上服务发现他网AUSF/UDM失败。

**适用NF：NRF**

此命令用于设置NRF国际漫游功能参数。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-NRFINTERFUNC]] · LST NRFINTERFUNC
- [[command/UNC/20.15.2/SET-NRFINTERFUNC]] · SET NRFINTERFUNC

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询国际漫游功能参数（LST-NRFINTERFUNC）_24956636.md`
- 原始手册：`evidence/UNC/20.15.2/设置国际漫游功能参数（SET-NRFINTERFUNC）_24796840.md`
