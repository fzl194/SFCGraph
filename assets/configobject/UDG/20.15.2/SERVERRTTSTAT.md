---
id: UDG@20.15.2@ConfigObject@SERVERRTTSTAT
type: ConfigObject
name: SERVERRTTSTAT（服务器时延统计功能配置）
nf: UDG
version: 20.15.2
object_name: SERVERRTTSTAT
object_kind: global_setting
applicable_nf:
- UPF
- PGW-U
- SGW-U
- GGSN
status: active
---

# SERVERRTTSTAT（服务器时延统计功能配置）

## 说明

**适用NF：UPF、PGW-U、SGW-U、GGSN**

![](设置服务器时延统计功能配置（SET SERVERRTTSTAT）_72428328.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，此命令开启后可能导致性能下降明显。执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。

该命令用于设置统计服务器时延统计功能。如果现网需要基于特定协议类型的CDN或DNS服务器进行进延统计，则开启开关并选择需要统计的应用类型。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-SERVERRTTSTAT]] · LST SERVERRTTSTAT
- [[command/UDG/20.15.2/SET-SERVERRTTSTAT]] · SET SERVERRTTSTAT

## 证据

- 原始手册：`evidence/UDG/20.15.2/SERVERRTTSTAT.md`
- 原始手册：`evidence/UDG/20.15.2/SERVERRTTSTAT.md`
