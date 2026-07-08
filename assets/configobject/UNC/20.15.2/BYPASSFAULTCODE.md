---
id: UNC@20.15.2@ConfigObject@BYPASSFAULTCODE
type: ConfigObject
name: BYPASSFAULTCODE（BYPASS故障状态码）
nf: UNC
version: 20.15.2
object_name: BYPASSFAULTCODE
object_kind: entity
applicable_nf:
- AMF
- SMF
status: active
---

# BYPASSFAULTCODE（BYPASS故障状态码）

## 说明

![](增加BYPASS故障状态码（ADD BYPASSFAULTCODE）_58840347.assets/notice_3.0-zh-cn_2.png)

该命令仅在主备UDM或者主备AUSF故障场景下应急使用，若误用该命令将使用户或会话进入Bypass状态，无法使用最新的签约信息，影响用户业务行为（例如：QOS）或体验。

**适用NF：AMF、SMF**

该命令用于添加UDM Bypas故障状态码配置。当系统针对故障的对端网元（UDM或AUSF）或收到对端网元返回特定原因值时期望用户或会话立即进入Bypass，需要添加此配置。针对不满足局向配置错误码或NF InstanceID，均需要主备对端网元均返回500及以上的状态码，用户或会话才进入Bypass状态。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-BYPASSFAULTCODE]] · ADD BYPASSFAULTCODE
- [[command/UNC/20.15.2/LST-BYPASSFAULTCODE]] · LST BYPASSFAULTCODE
- [[command/UNC/20.15.2/MOD-BYPASSFAULTCODE]] · MOD BYPASSFAULTCODE
- [[command/UNC/20.15.2/RMV-BYPASSFAULTCODE]] · RMV BYPASSFAULTCODE

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改BYPASS故障状态码（MOD-BYPASSFAULTCODE）_14120438.md`
- 原始手册：`evidence/UNC/20.15.2/删除BYPASS故障状态码（RMV-BYPASSFAULTCODE）_59000293.md`
- 原始手册：`evidence/UNC/20.15.2/增加BYPASS故障状态码（ADD-BYPASSFAULTCODE）_58840347.md`
- 原始手册：`evidence/UNC/20.15.2/查询BYPASS故障状态码（LST-BYPASSFAULTCODE）_58800305.md`
