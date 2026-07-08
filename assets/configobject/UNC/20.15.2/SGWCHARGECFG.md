---
id: UNC@20.15.2@ConfigObject@SGWCHARGECFG
type: ConfigObject
name: SGWCHARGECFG（SGW计费配置）
nf: UNC
version: 20.15.2
object_name: SGWCHARGECFG
object_kind: global_setting
applicable_nf:
- SGW-C
status: active
---

# SGWCHARGECFG（SGW计费配置）

## 说明

**适用NF：SGW-C**

![](SGW计费配置（SET SGWCHARGECFG）_09896989.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，修改配置可能导致无可用CG，SGW话单无法被正常处理，从而导致用户无法计费。

SET SGWCHARGECFG命令用来修改SGW计费配置，包括本地离线计费、漫游离线计费、拜访离线计费、使用本地CG或使用PGW携带的CG。

## 操作本对象的命令

- [LST SGWCHARGECFG](command/UNC/20.15.2/LST-SGWCHARGECFG.md)
- [SET SGWCHARGECFG](command/UNC/20.15.2/SET-SGWCHARGECFG.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/SGW计费配置（SET-SGWCHARGECFG）_09896989.md`
- 原始手册：`evidence/UNC/20.15.2/查询SGW计费配置（LST-SGWCHARGECFG）_09896990.md`
