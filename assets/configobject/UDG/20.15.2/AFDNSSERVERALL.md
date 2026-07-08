---
id: UDG@20.15.2@ConfigObject@AFDNSSERVERALL
type: ConfigObject
name: AFDNSSERVERALL（所有防欺诈可信DNS服务器）
nf: UDG
version: 20.15.2
object_name: AFDNSSERVERALL
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# AFDNSSERVERALL（所有防欺诈可信DNS服务器）

## 说明

**适用NF：PGW-U、UPF**

![](删除所有防欺诈可信DNS服务器（RMV AFDNSSERVERALL）_05304032.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除所有防欺诈可信DNS服务器可能会改变业务匹配结果，导致用户业务受损，，请谨慎使用并联系华为技术支持协助操作。

该命令用于删除所有配置的可信DNS服务器IP。

## 操作本对象的命令

- [[command/UDG/20.15.2/RMV-AFDNSSERVERALL]] · RMV AFDNSSERVERALL

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除所有防欺诈可信DNS服务器（RMV-AFDNSSERVERALL）_05304032.md`
