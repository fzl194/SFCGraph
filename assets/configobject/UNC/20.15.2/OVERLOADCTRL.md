---
id: UNC@20.15.2@ConfigObject@OVERLOADCTRL
type: ConfigObject
name: OVERLOADCTRL（过载控制的配置信息）
nf: UNC
version: 20.15.2
object_name: OVERLOADCTRL
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
status: active
---

# OVERLOADCTRL（过载控制的配置信息）

## 说明

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用来配置GiGn联动信令抑制功能的开关以及老化定时器时长。配置针对业务触发的信令导致的用户去活场景是否开启信令抑制功能。

## 操作本对象的命令

- [LST OVERLOADCTRL](command/UNC/20.15.2/LST-OVERLOADCTRL.md)
- [SET OVERLOADCTRL](command/UNC/20.15.2/SET-OVERLOADCTRL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询过载控制的配置信息（LST-OVERLOADCTRL）_35803152.md`
- 原始手册：`evidence/UNC/20.15.2/设置信令抑制功能开关以及老化定时器时长（SET-OVERLOADCTRL）_82122531.md`
