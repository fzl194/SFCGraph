---
id: UDG@20.15.2@ConfigObject@MSSSCHTHRDLOAD
type: ConfigObject
name: MSSSCHTHRDLOAD（调度线程负载信息）
nf: UDG
version: 20.15.2
object_name: MSSSCHTHRDLOAD
object_kind: query_target
status: active
---

# MSSSCHTHRDLOAD（调度线程负载信息）

## 说明

该命令用于查询调度线程负载信息。

调度线程负载信息统计默认是关闭的，当统计关闭时，查询信息无回显。

例如，当发现某个线程的负载不符合预期时，可打开统计开关，然后执行该命令查询线程的负载统计，查看具体是哪一种业务的负载统计不符合预期。

## 操作本对象的命令

- [[command/UDG/20.15.2/DSP-MSSSCHTHRDLOAD]] · DSP MSSSCHTHRDLOAD

## 证据

- 原始手册：`evidence/UDG/20.15.2/MSSSCHTHRDLOAD.md`
