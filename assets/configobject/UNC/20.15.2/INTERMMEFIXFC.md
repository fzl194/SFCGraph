---
id: UNC@20.15.2@ConfigObject@INTERMMEFIXFC
type: ConfigObject
name: INTERMMEFIXFC（Inter-MME接入固定速率流控功能相关参数）
nf: UNC
version: 20.15.2
object_name: INTERMMEFIXFC
object_kind: global_setting
applicable_nf:
- MME
status: active
---

# INTERMMEFIXFC（Inter-MME接入固定速率流控功能相关参数）

## 说明

**适用网元：MME**

该命令设置Inter-MME接入固定速率流控功能的相关参数。

MME组Pool时，如果某个MME故障，则故障MME上的用户会接入到Pool内正常的MME上，可能造成对正常MME、S6a接口、HSS的冲击，导致相关网元过载。为了防止这类MME间的新接入用户影响在网用户的正常业务，控制非本MME用户的接入消息允许处理速率。这些消息包括：Attach Request消息、Service Request消息。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-INTERMMEFIXFC]] · LST INTERMMEFIXFC
- [[command/UNC/20.15.2/SET-INTERMMEFIXFC]] · SET INTERMMEFIXFC

## 证据

- 原始手册：`evidence/UNC/20.15.2/INTERMMEFIXFC.md`
- 原始手册：`evidence/UNC/20.15.2/INTERMMEFIXFC.md`
