---
id: UNC@20.15.2@ConfigObject@USRCTLGGSN
type: ConfigObject
name: USRCTLGGSN（手工恢复GGSN地址）
nf: UNC
version: 20.15.2
object_name: USRCTLGGSN
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# USRCTLGGSN（手工恢复GGSN地址）

## 说明

**适用网元：SGSN**

该命令用于增加需手工恢复的GGSN地址。

如果由于网络等原因导致到某个GGSN的通信经常中断，为了避免业务的频繁切换，可以通过此命令屏蔽该GGSN，在确认故障完全排除后，再恢复到该GGSN的业务。

当 UNC 检测到本表中配置的GGSN故障恢复后，产生ALM-12605 GTPC路径恢复正常需手工启动新业务接入告警，并且只有在经过操作员人工确认（ [**RES USRCTLGGSN**](恢复可用的GGSN地址(RES USRCTLGGSN)_72345507.md) ）后，才选择故障恢复后的GGSN业务。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-USRCTLGGSN]] · ADD USRCTLGGSN
- [[command/UNC/20.15.2/DSP-USRCTLGGSN]] · DSP USRCTLGGSN
- [[command/UNC/20.15.2/LST-USRCTLGGSN]] · LST USRCTLGGSN
- [[command/UNC/20.15.2/RES-USRCTLGGSN]] · RES USRCTLGGSN
- [[command/UNC/20.15.2/RMV-USRCTLGGSN]] · RMV USRCTLGGSN

## 证据

- 原始手册：`evidence/UNC/20.15.2/USRCTLGGSN.md`
- 原始手册：`evidence/UNC/20.15.2/USRCTLGGSN.md`
- 原始手册：`evidence/UNC/20.15.2/USRCTLGGSN.md`
- 原始手册：`evidence/UNC/20.15.2/USRCTLGGSN.md`
- 原始手册：`evidence/UNC/20.15.2/USRCTLGGSN.md`
