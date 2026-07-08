---
id: UDG@20.15.2@ConfigObject@AFPROXYSRVALL
type: ConfigObject
name: AFPROXYSRVALL（所有防欺诈可信代理服务器）
nf: UDG
version: 20.15.2
object_name: AFPROXYSRVALL
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# AFPROXYSRVALL（所有防欺诈可信代理服务器）

## 说明

**适用NF：PGW-U、UPF**

![](删除所有防欺诈可信代理服务器（RMV AFPROXYSRVALL）_08935041.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除所有可信代理服务器可能会改变业务匹配结果，导致用户业务受损，请谨慎使用并联系华为技术支持协助操作。

该命令用于删除所有配置的可信代理服务器IP。

## 操作本对象的命令

- [[command/UDG/20.15.2/RMV-AFPROXYSRVALL]] · RMV AFPROXYSRVALL

## 证据

- 原始手册：`evidence/UDG/20.15.2/AFPROXYSRVALL.md`
