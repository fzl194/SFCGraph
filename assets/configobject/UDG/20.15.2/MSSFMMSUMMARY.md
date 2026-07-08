---
id: UDG@20.15.2@ConfigObject@MSSFMMSUMMARY
type: ConfigObject
name: MSSFMMSUMMARY（FMM的PBUF概要信息）
nf: UDG
version: 20.15.2
object_name: MSSFMMSUMMARY
object_kind: query_target
status: active
---

# MSSFMMSUMMARY（FMM的PBUF概要信息）

## 说明

该命令用于显示MSS的PBUF内存池信息。MSS会自动创建一个PBUF内存池和一个二次管理内存池。PBUF内存池为定长内存池，可以由多进程共享访问调用，主要用于报文缓存。二次管理内存池为变长内存，主要用于控制转发平面。该命令可查看PBUF内存池信息。通过获取的信息，可了解配置是否正常，并进行故障诊断。

## 操作本对象的命令

- [[command/UDG/20.15.2/DSP-MSSFMMSUMMARY]] · DSP MSSFMMSUMMARY

## 证据

- 原始手册：`evidence/UDG/20.15.2/MSSFMMSUMMARY.md`
