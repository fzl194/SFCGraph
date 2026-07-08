---
id: UNC@20.15.2@ConfigObject@TRUNKACTPORT
type: ConfigObject
name: TRUNKACTPORT（切换Trunk激活口）
nf: UNC
version: 20.15.2
object_name: TRUNKACTPORT
object_kind: action
status: active
---

# TRUNKACTPORT（切换Trunk激活口）

## 说明

该命令用于切换Trunk激活口。

该命令仅支持工作模式为主备的Trunk接口。

不指定MEMBERIFNAME参数时，在备份口中随机选择可用的接口作为激活口；指定MEMBERIFNAME参数时，可以切换至指定的成员口。

## 操作本对象的命令

- [[command/UNC/20.15.2/SWP-TRUNKACTPORT]] · SWP TRUNKACTPORT

## 证据

- 原始手册：`evidence/UNC/20.15.2/切换Trunk激活口（SWP-TRUNKACTPORT）_00601477.md`
