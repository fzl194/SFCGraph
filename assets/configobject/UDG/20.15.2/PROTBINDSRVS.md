---
id: UDG@20.15.2@ConfigObject@PROTBINDSRVS
type: ConfigObject
name: PROTBINDSRVS（业务统计协议绑定配置）
nf: UDG
version: 20.15.2
object_name: PROTBINDSRVS
object_kind: binding
applicable_nf:
- PGW-U
- UPF
status: active
---

# PROTBINDSRVS（业务统计协议绑定配置）

## 说明

**适用NF：PGW-U、UPF**

![](增加业务统计协议绑定配置（ADD PROTBINDSRVS）_82837388.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致性能下降明显，请谨慎使用并联系华为技术支持协助操作。

该命令用于配置基于业务的性能统计组合中的Protocol和Protocol Group对象，筛选统计所绑定的七层协议类型报文的上下行数据包数及字节数等性能统计指标。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-PROTBINDSRVS]] · ADD PROTBINDSRVS
- [[command/UDG/20.15.2/LST-PROTBINDSRVS]] · LST PROTBINDSRVS
- [[command/UDG/20.15.2/RMV-PROTBINDSRVS]] · RMV PROTBINDSRVS

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除业务统计协议绑定配置（RMV-PROTBINDSRVS）_82837389.md`
- 原始手册：`evidence/UDG/20.15.2/增加业务统计协议绑定配置（ADD-PROTBINDSRVS）_82837388.md`
- 原始手册：`evidence/UDG/20.15.2/查询业务统计协议绑定配置（LST-PROTBINDSRVS）_86527040.md`
