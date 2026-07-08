---
id: UNC@20.15.2@ConfigObject@RESTOUSR
type: ConfigObject
name: RESTOUSR（容灾用户特征参数）
nf: UNC
version: 20.15.2
object_name: RESTOUSR
object_kind: entity
applicable_nf:
- MME
status: active
---

# RESTOUSR（容灾用户特征参数）

## 说明

**适用网元：MME**

本命令应用于MME链式备份业务调测，用于增加支持容灾备份的用户特征，即IMSI。

启用“WSFD- 201201 MME链式备份”特性license后，若“容灾功能运行模式”设定为“调测模式”，系统根据本命令的配置记录对用户的IMSI进行匹配，匹配成功的用户才能使用备份功能。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-RESTOUSR]] · ADD RESTOUSR
- [[command/UNC/20.15.2/LST-RESTOUSR]] · LST RESTOUSR
- [[command/UNC/20.15.2/RMV-RESTOUSR]] · RMV RESTOUSR

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除容灾用户特征参数(RMV-RESTOUSR)_72345717.md`
- 原始手册：`evidence/UNC/20.15.2/增加容灾用户特征参数(ADD-RESTOUSR)_26305926.md`
- 原始手册：`evidence/UNC/20.15.2/查询容灾用户特征参数(LST-RESTOUSR)_26146118.md`
