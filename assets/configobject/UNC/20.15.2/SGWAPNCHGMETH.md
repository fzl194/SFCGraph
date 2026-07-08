---
id: UNC@20.15.2@ConfigObject@SGWAPNCHGMETH
type: ConfigObject
name: SGWAPNCHGMETH（SGW APN计费方式）
nf: UNC
version: 20.15.2
object_name: SGWAPNCHGMETH
object_kind: global_setting
applicable_nf:
- SGW-C
status: active
---

# SGWAPNCHGMETH（SGW APN计费方式）

## 说明

**适用NF：SGW-C**

![](设置SGW APN计费方式（SET SGWAPNCHGMETH）_09896992.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，修改配置会影响新激活的SGW用户是否产生S-GW话单，可能导致用户无法计费。

SET SGWAPNCHGMETH命令用来控制APN下的用户是否产生S-GW话单。

## 操作本对象的命令

- [LST SGWAPNCHGMETH](command/UNC/20.15.2/LST-SGWAPNCHGMETH.md)
- [SET SGWAPNCHGMETH](command/UNC/20.15.2/SET-SGWAPNCHGMETH.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SGW-APN计费方式（LST-SGWAPNCHGMETH）_09896993.md`
- 原始手册：`evidence/UNC/20.15.2/设置SGW-APN计费方式（SET-SGWAPNCHGMETH）_09896992.md`
