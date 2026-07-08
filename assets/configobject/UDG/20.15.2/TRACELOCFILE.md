---
id: UDG@20.15.2@ConfigObject@TRACELOCFILE
type: ConfigObject
name: TRACELOCFILE（上传跟踪本地文件）
nf: UDG
version: 20.15.2
object_name: TRACELOCFILE
object_kind: action
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# TRACELOCFILE（上传跟踪本地文件）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

![](上传跟踪本地文件（ULD TRACELOCFILE）_78310840.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，命令执行成功会将FileSver已经存在的文件删除

该命令用于上传指定pod下用户跟踪存盘文件到文件服务器上。

## 操作本对象的命令

- [[command/UDG/20.15.2/DSP-TRACELOCFILE]] · DSP TRACELOCFILE
- [[command/UDG/20.15.2/ULD-TRACELOCFILE]] · ULD TRACELOCFILE

## 证据

- 原始手册：`evidence/UDG/20.15.2/上传跟踪本地文件（ULD-TRACELOCFILE）_78310840.md`
- 原始手册：`evidence/UDG/20.15.2/查询用户跟踪本地文件（DSP-TRACELOCFILE）_78071068.md`
