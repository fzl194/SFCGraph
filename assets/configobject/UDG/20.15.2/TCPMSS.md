---
id: UDG@20.15.2@ConfigObject@TCPMSS
type: ConfigObject
name: TCPMSS（Tcp Mss配置）
nf: UDG
version: 20.15.2
object_name: TCPMSS
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# TCPMSS（Tcp Mss配置）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

![](添加Tcp Mss配置（ADD TCPMSS）_82837694.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该配置影响传输的TCP报文长度，请确认参数值合理。

该命令用于开启指定APN及用户归属属性的TCP MSS调整功能并配置TCP MSS的值。为了避免由于TCP报文过长而分片或被路由器丢弃，导致TCP连接半关闭/无法重建的问题，要开启TCP-MSS调整功能，通告对端自己能接收的最大报文段长度。如果部署网络中，由于中间节点无法处理业务分片导致业务异常，需要全网使能TCP MSS。 建议在防火墙使能TCP MSS。如果部署网络中，某个APN由于中间节点无法处理业务分片导致业务异常，需要针对该APN使能TCP MSS。建议基于该APN使能TCP MSS。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-TCPMSS]] · ADD TCPMSS
- [[command/UDG/20.15.2/LST-TCPMSS]] · LST TCPMSS
- [[command/UDG/20.15.2/MOD-TCPMSS]] · MOD TCPMSS
- [[command/UDG/20.15.2/RMV-TCPMSS]] · RMV TCPMSS

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改Tcp-Mss配置（MOD-TCPMSS）_82837695.md`
- 原始手册：`evidence/UDG/20.15.2/删除Tcp-Mss配置（RMV-TCPMSS）_82837696.md`
- 原始手册：`evidence/UDG/20.15.2/查询Tcp-Mss配置（LST-TCPMSS）_82837697.md`
- 原始手册：`evidence/UDG/20.15.2/添加Tcp-Mss配置（ADD-TCPMSS）_82837694.md`
