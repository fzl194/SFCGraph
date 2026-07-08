---
id: UNC@20.15.2@ConfigObject@OFFLOADBYENODEB
type: ConfigObject
name: OFFLOADBYENODEB（eNodeB迁移任务）
nf: UNC
version: 20.15.2
object_name: OFFLOADBYENODEB
object_kind: action
applicable_nf:
- MME
status: active
---

# OFFLOADBYENODEB（eNodeB迁移任务）

## 说明

**适用网元：MME**

此命令用于启动eNodeB迁移任务。

当LTE网络需做调整时，如将MME下的一个或几个eNodeB割接至其他MME，可使用此命令启动eNodeB迁移任务。此命令一次性最多指定10个eNodeB启动迁移任务。

## 操作本对象的命令

- [[command/UNC/20.15.2/STR-OFFLOADBYENODEB]] · STR OFFLOADBYENODEB

## 证据

- 原始手册：`evidence/UNC/20.15.2/启动eNodeB迁移任务(STR-OFFLOADBYENODEB)_26305902.md`
