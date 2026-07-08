---
id: UNC@20.15.2@ConfigObject@LCSPERMITCFG
type: ConfigObject
name: LCSPERMITCFG（定位服务权限配置）
nf: UNC
version: 20.15.2
object_name: LCSPERMITCFG
object_kind: entity
applicable_nf:
- AMF
status: active
---

# LCSPERMITCFG（定位服务权限配置）

## 说明

**适用NF：AMF**

该命令用于增加定位服务权限配置：AMF收到定位服务消费者的定位请求时检查定位请求是否越权，如果越权，AMF拒绝其定位请求；紧急呼叫触发的NI-LR模式定位时，AMF检查通过服务发现的GMLC是否有定位此UE的权限，如果没有权限，AMF取消位置通知。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-LCSPERMITCFG]] · ADD LCSPERMITCFG
- [[command/UNC/20.15.2/LST-LCSPERMITCFG]] · LST LCSPERMITCFG
- [[command/UNC/20.15.2/RMV-LCSPERMITCFG]] · RMV LCSPERMITCFG

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除定位服务权限配置（RMV-LCSPERMITCFG）_18115686.md`
- 原始手册：`evidence/UNC/20.15.2/增加定位服务权限配置（ADD-LCSPERMITCFG）_62595587.md`
- 原始手册：`evidence/UNC/20.15.2/查询定位服务权限配置（LST-LCSPERMITCFG）_17955726.md`
