---
id: UDG@20.15.2@ConfigObject@REDUNDUSER
type: ConfigObject
name: REDUNDUSER（静态地址用户路由冗余功能）
nf: UDG
version: 20.15.2
object_name: REDUNDUSER
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# REDUNDUSER（静态地址用户路由冗余功能）

## 说明

**适用NF：PGW-U、UPF**

![](配置静态地址用户路由冗余功能（SET REDUNDUSER）_71074367.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，改此配置前先确认是否存在静态地址冗余用户，否则可能导致此部分用户业务不通。

该命令用来配置静态地址用户路由冗余功能。

## 操作本对象的命令

- [LST REDUNDUSER](command/UDG/20.15.2/LST-REDUNDUSER.md)
- [SET REDUNDUSER](command/UDG/20.15.2/SET-REDUNDUSER.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询静态地址用户路由冗余功能（LST-REDUNDUSER）_71074368.md`
- 原始手册：`evidence/UDG/20.15.2/配置静态地址用户路由冗余功能（SET-REDUNDUSER）_71074367.md`
