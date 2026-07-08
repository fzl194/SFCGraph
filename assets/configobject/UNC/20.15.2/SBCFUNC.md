---
id: UNC@20.15.2@ConfigObject@SBCFUNC
type: ConfigObject
name: SBCFUNC（小区广播功能）
nf: UNC
version: 20.15.2
object_name: SBCFUNC
object_kind: global_setting
applicable_nf:
- MME
status: active
---

# SBCFUNC（小区广播功能）

## 说明

该命令用于设置小区广播功能参数。需要MME支持向CBC反馈无线侧告警消息广播情况，或者当CBC发送的Write-Replace Warning Request/Stop Warning Request消息超过64K的规格时，需要MME支持处理，可以通过本命令进行控制。

**适用网元：MME**

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-SBCFUNC]] · LST SBCFUNC
- [[command/UNC/20.15.2/SET-SBCFUNC]] · SET SBCFUNC

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询小区广播功能(LST-SBCFUNC)_72345979.md`
- 原始手册：`evidence/UNC/20.15.2/设置小区广播功能(SET-SBCFUNC)_26306190.md`
