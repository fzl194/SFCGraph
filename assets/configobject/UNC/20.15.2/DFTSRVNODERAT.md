---
id: UNC@20.15.2@ConfigObject@DFTSRVNODERAT
type: ConfigObject
name: DFTSRVNODERAT（默认RAT类型）
nf: UNC
version: 20.15.2
object_name: DFTSRVNODERAT
object_kind: global_setting
applicable_nf:
- GGSN
status: active
---

# DFTSRVNODERAT（默认RAT类型）

## 说明

**适用NF：GGSN**

该命令用来设置默认的RAT类型。获取RAT类型用于从虚拟APN映射到真实APN、匹配user-profile进行业务、计费控制。当SGSN IP在表中没有匹配项并且消息中没有携带RAT Type信元时，会用这个默认的RAT类型作为它对应的RAT类型。当要配置该表的默认表项时，使用这条命令。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-DFTSRVNODERAT]] · LST DFTSRVNODERAT
- [[command/UNC/20.15.2/SET-DFTSRVNODERAT]] · SET DFTSRVNODERAT

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询默认RAT类型（LST-DFTSRVNODERAT）_09652266.md`
- 原始手册：`evidence/UNC/20.15.2/设置默认RAT类型（SET-DFTSRVNODERAT）_09653166.md`
