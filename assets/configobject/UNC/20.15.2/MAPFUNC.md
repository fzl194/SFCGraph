---
id: UNC@20.15.2@ConfigObject@MAPFUNC
type: ConfigObject
name: MAPFUNC（MAP功能配置）
nf: UNC
version: 20.15.2
object_name: MAPFUNC
object_kind: global_setting
applicable_nf:
- SGSN
- MME
status: active
---

# MAPFUNC（MAP功能配置）

## 说明

![](设置MAP功能配置(SET MAPFUNC)_26145466.assets/notice_3.0-zh-cn_2.png)

修改MAP的功能参数会导致与对端网元协商流程和消息信元的变化，可能造成后续接入用户的Attach/RAU流程的失败。

**适用网元：SGSN、MME**

该命令用于设置MAP各项功能属性。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-MAPFUNC]] · LST MAPFUNC
- [[command/UNC/20.15.2/SET-MAPFUNC]] · SET MAPFUNC

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询MAP功能配置(LST-MAPFUNC)_72225147.md`
- 原始手册：`evidence/UNC/20.15.2/设置MAP功能配置(SET-MAPFUNC)_26145466.md`
