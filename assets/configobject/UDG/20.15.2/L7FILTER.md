---
id: UDG@20.15.2@ConfigObject@L7FILTER
type: ConfigObject
name: L7FILTER（七层过滤器）
nf: UDG
version: 20.15.2
object_name: L7FILTER
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# L7FILTER（七层过滤器）

## 说明

**适用NF：PGW-U、UPF**

该命令用于增加一条新的L7Filter。L7Filter是一种定义七层过滤条件的过滤器，可以通过本命令完成新建七层过滤组，并支持同时为该七层过滤器其添加子七层过滤器的功能，子七层过滤器的内容定义包括URL/host、User-Agent、method等七层关键字段在内的各种过滤条件。URL可以包含*，不允许包含“http://”、“rtsp://”、“ftp://”、“https://”等头部。

## 操作本对象的命令

- [ADD L7FILTER](command/UDG/20.15.2/ADD-L7FILTER.md)
- [LST L7FILTER](command/UDG/20.15.2/LST-L7FILTER.md)
- [MOD L7FILTER](command/UDG/20.15.2/MOD-L7FILTER.md)
- [RMV L7FILTER](command/UDG/20.15.2/RMV-L7FILTER.md)

## 关联对象

- [PROTBINDFLOWF](configobject/UDG/20.15.2/PROTBINDFLOWF.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改七层过滤器（MOD-L7FILTER）_86527044.md`
- 原始手册：`evidence/UDG/20.15.2/删除七层过滤器（RMV-L7FILTER）_82837399.md`
- 原始手册：`evidence/UDG/20.15.2/增加七层过滤器（ADD-L7FILTER）_82837397.md`
- 原始手册：`evidence/UDG/20.15.2/查询七层过滤器（LST-L7FILTER）_86526660.md`
