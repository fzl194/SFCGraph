---
id: UNC@20.15.2@ConfigObject@GLOBALDNS
type: ConfigObject
name: GLOBALDNS（系统默认DNS）
nf: UNC
version: 20.15.2
object_name: GLOBALDNS
object_kind: global_setting
applicable_nf:
- SMF
status: active
---

# GLOBALDNS（系统默认DNS）

## 说明

**适用NF：SMF**

该命令用来设置系统默认的DNS属性。一般情况下应在UNC上配置DNS地址，以保证UE能够解析Internet域名。当用户需要修改整机默认的主、备DNS地址或者主、备DNS64地址时，使用该命令配置。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-GLOBALDNS]] · LST GLOBALDNS
- [[command/UNC/20.15.2/RTR-GLOBALDNS]] · RTR GLOBALDNS
- [[command/UNC/20.15.2/SET-GLOBALDNS]] · SET GLOBALDNS

## 证据

- 原始手册：`evidence/UNC/20.15.2/恢复系统默认DNS（RTR-GLOBALDNS）_09652557.md`
- 原始手册：`evidence/UNC/20.15.2/查询系统默认DNS（LST-GLOBALDNS）_09651751.md`
- 原始手册：`evidence/UNC/20.15.2/设置系统默认DNS（SET-GLOBALDNS）_09653745.md`
