---
id: UNC@20.15.2@ConfigObject@CTXSTARTRATING
type: ConfigObject
name: CTXSTARTRATING（给OCS/CHF发送的消息初始携带的计费属性）
nf: UNC
version: 20.15.2
object_name: CTXSTARTRATING
object_kind: entity
applicable_nf:
- PGW-C
- SMF
status: active
---

# CTXSTARTRATING（给OCS/CHF发送的消息初始携带的计费属性）

## 说明

**适用NF：PGW-C、SMF**

该命令用于配置上下文激活时的给OCS/CHF发送的消息的计费属性。配置该命令后，用户激活时，UNC与在线计费服务器交互的消息中将携带指定的费率组，在线计费服务器会给该费率组下发相应的配额。当用户从离线计费自动恢复成在线计费时，UNC根据该命令的配置决定是否在发送的消息中为该用户使用过的业务重新申请配额。

## 操作本对象的命令

- [[command/UNC/20.15.2/RMV-CTXSTARTRATING]] · RMV CTXSTARTRATING
- [[command/UNC/20.15.2/SET-CTXSTARTRATING]] · SET CTXSTARTRATING

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除给OCS_CHF发送的消息初始携带的计费属性（RMV-CTXSTARTRATING）_09897212.md`
- 原始手册：`evidence/UNC/20.15.2/设置给OCS_CHF发送的消息初始携带的计费属性（SET-CTXSTARTRATING）_09897210.md`
