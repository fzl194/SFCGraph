---
id: UDG@20.15.2@ConfigObject@GLOBUEMUTACC
type: ConfigObject
name: GLOBUEMUTACC（全局用户互访控制配置）
nf: UDG
version: 20.15.2
object_name: GLOBUEMUTACC
object_kind: global_setting
applicable_nf:
- UPF
status: active
---

# GLOBUEMUTACC（全局用户互访控制配置）

## 说明

**适用NF：UPF**

![](设置全局用户互访控制配置（SET GLOBUEMUTACC）_82837773.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，整机终端互访控制功能开启后，如果未在具体APN下关闭相应终端互访控制功能，所有APN内或APN间的终端互访将无法进行。

本命令仅适用于同一UPF网元内不同UE会话的互访控制，如果需要跨UPF网元的不同UE会话的互访控制，需要在UPF上配置ACL规则。

该命令用来配置整机终端互访控制功能。支持配置是否开启整机APN内终端互访控制功能以及整机APN间终端互访控制功能。

## 操作本对象的命令

- [LST GLOBUEMUTACC](command/UDG/20.15.2/LST-GLOBUEMUTACC.md)
- [SET GLOBUEMUTACC](command/UDG/20.15.2/SET-GLOBUEMUTACC.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询全局用户互访控制配置（LST-GLOBUEMUTACC）_82837774.md`
- 原始手册：`evidence/UDG/20.15.2/设置全局用户互访控制配置（SET-GLOBUEMUTACC）_82837773.md`
