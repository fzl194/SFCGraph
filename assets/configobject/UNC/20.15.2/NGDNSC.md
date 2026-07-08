---
id: UNC@20.15.2@ConfigObject@NGDNSC
type: ConfigObject
name: NGDNSC（DNS缓存）
nf: UNC
version: 20.15.2
object_name: NGDNSC
object_kind: action
applicable_nf:
- AMF
- SMF
status: active
---

# NGDNSC（DNS缓存）

## 说明

**适用NF：AMF、SMF**

该命令功能不生效，由CLR NGDNSCACHE命令代替。

该命令用于清除DNS缓存（DNS Cache）。当TOPO侧4/5G切换时查询FQDN的IP地址完成后，清除已经查询的缓存命令。

DNS Cache是使用DNS服务器解析时在系统中查找到的缓存，其主要内容为域名和IP地址信息，用于快速解析域名。

## 操作本对象的命令

- [[command/UNC/20.15.2/CLR-NGDNSC]] · CLR NGDNSC

## 证据

- 原始手册：`evidence/UNC/20.15.2/NGDNSC.md`
