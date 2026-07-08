---
id: UNC@20.15.2@ConfigObject@GLBOFCTEMPCFG
type: ConfigObject
name: GLBOFCTEMPCFG（全局生效离线计费模板配置）
nf: UNC
version: 20.15.2
object_name: GLBOFCTEMPCFG
object_kind: query_target
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# GLBOFCTEMPCFG（全局生效离线计费模板配置）

## 说明

**适用NF：SGW-C、PGW-C、SMF**

该命令用来查看全局离线计费模板生效的配置信息。

如果全局离线计费配置未绑定离线计费模板，则显示全局缺省配置。显示信息中如果模板名字为NULL，则表示是全局缺省配置。

## 操作本对象的命令

- [DSP GLBOFCTEMPCFG](command/UNC/20.15.2/DSP-GLBOFCTEMPCFG.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询全局生效离线计费模板配置（DSP-GLBOFCTEMPCFG）_09897012.md`
