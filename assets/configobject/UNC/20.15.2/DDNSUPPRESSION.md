---
id: UNC@20.15.2@ConfigObject@DDNSUPPRESSION
type: ConfigObject
name: DDNSUPPRESSION（DDN抑制功能配置）
nf: UNC
version: 20.15.2
object_name: DDNSUPPRESSION
object_kind: global_setting
applicable_nf:
- SGW-C
status: active
---

# DDNSUPPRESSION（DDN抑制功能配置）

## 说明

**适用NF：SGW-C**

该命令用于设置DDN抑制功能相关参数。DDN抑制功能是指“MONITORTIMER(监控时长)”内某用户的DDN流程失败，且收到MME返回Downlink Data Notification Failure Indication消息携带失败原因值“UE not responding”或者“Unable to page UE”，失败的次数达到“MONITORTIMES(DDN失败次数)”，该用户在接下来的“SUPPTIMER(抑制时长)”内，将对DDN流程进行抑制，收到UPF的DDN请求后直接回复失败，不再向MME发送DDN消息。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-DDNSUPPRESSION]] · LST DDNSUPPRESSION
- [[command/UNC/20.15.2/SET-DDNSUPPRESSION]] · SET DDNSUPPRESSION

## 证据

- 原始手册：`evidence/UNC/20.15.2/DDNSUPPRESSION.md`
- 原始手册：`evidence/UNC/20.15.2/DDNSUPPRESSION.md`
