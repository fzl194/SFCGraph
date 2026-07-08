---
id: UNC@20.15.2@ConfigObject@VIRTUALUPFID
type: ConfigObject
name: VIRTUALUPFID（虚拟UPF实例标识）
nf: UNC
version: 20.15.2
object_name: VIRTUALUPFID
object_kind: entity
applicable_nf:
- SMF
status: active
---

# VIRTUALUPFID（虚拟UPF实例标识）

## 说明

**适用NF：SMF**

该命令用于增加虚拟UPF实例标识。

在主锚点会话和辅锚点会话共部署或者多辅锚点会话共部署的场景下，一个UPF上会同时承载主锚点会话和辅锚点会话或者同时承载多个辅锚点会话。这个时候需要配置VUPFINSTANCEID，用于标识辅锚点会话，该标识也会被上报到计费侧，通知计费对该辅锚点会话进行计费。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-VIRTUALUPFID]] · ADD VIRTUALUPFID
- [[command/UNC/20.15.2/LST-VIRTUALUPFID]] · LST VIRTUALUPFID
- [[command/UNC/20.15.2/RMV-VIRTUALUPFID]] · RMV VIRTUALUPFID

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除虚拟UPF实例标识（RMV-VIRTUALUPFID）_96243048.md`
- 原始手册：`evidence/UNC/20.15.2/增加虚拟UPF实例标识（ADD-VIRTUALUPFID）_76311126.md`
- 原始手册：`evidence/UNC/20.15.2/查询虚拟UPF实例标识（LST-VIRTUALUPFID）_96242532.md`
