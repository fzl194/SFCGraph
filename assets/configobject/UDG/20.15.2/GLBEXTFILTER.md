---
id: UDG@20.15.2@ConfigObject@GLBEXTFILTER
type: ConfigObject
name: GLBEXTFILTER（全局扩展过滤器绑定配置）
nf: UDG
version: 20.15.2
object_name: GLBEXTFILTER
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# GLBEXTFILTER（全局扩展过滤器绑定配置）

## 说明

**适用NF：PGW-U、UPF**

该命令用于配置全局扩展过滤器绑定关系，即绑定重定向动作过滤条件，只有符合扩展过滤器的条件，才能执行重定向动作。重定向动作包括URL重定向（使用ADD REDIRECT或MOD REDIRECT配置）和CaptivePortal智能重定向动作（在ADD RULE或MOD RULE配置时指定Policy Type为SMARTREDIRECT，Policy Name为CaptivePortal业务对应的IPFarm的名称）。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-GLBEXTFILTER]] · LST GLBEXTFILTER
- [[command/UDG/20.15.2/RMV-GLBEXTFILTER]] · RMV GLBEXTFILTER
- [[command/UDG/20.15.2/SET-GLBEXTFILTER]] · SET GLBEXTFILTER

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除全局扩展过滤器绑定配置（RMV-GLBEXTFILTER）_82837358.md`
- 原始手册：`evidence/UDG/20.15.2/查询全局扩展过滤器绑定配置（LST-GLBEXTFILTER）_82837359.md`
- 原始手册：`evidence/UDG/20.15.2/配置全局扩展过滤器绑定关系（SET-GLBEXTFILTER）_82837357.md`
