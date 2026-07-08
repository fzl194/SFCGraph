---
id: UNC@20.15.2@ConfigObject@NGREQMSGCACHE
type: ConfigObject
name: NGREQMSGCACHE（清空DNS客户端的缓存消息）
nf: UNC
version: 20.15.2
object_name: NGREQMSGCACHE
object_kind: action
applicable_nf:
- AMF
status: active
---

# NGREQMSGCACHE（清空DNS客户端的缓存消息）

## 说明

**适用NF：AMF**

该命令用于清空请求消息缓存链中所有缓存消息。

AMF可向系统的DNS客户端微服务查询MME，当DNS客户端相关配置命令正确，但一直查询不到MME的IP，执行该命令。

## 操作本对象的命令

- [[command/UNC/20.15.2/CLR-NGREQMSGCACHE]] · CLR NGREQMSGCACHE

## 证据

- 原始手册：`evidence/UNC/20.15.2/NGREQMSGCACHE.md`
