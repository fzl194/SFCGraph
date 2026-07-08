---
id: UNC@20.15.2@ConfigObject@ASRCHN
type: ConfigObject
name: ASRCHN（容灾业务通道配置）
nf: UNC
version: 20.15.2
object_name: ASRCHN
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# ASRCHN（容灾业务通道配置）

## 说明

**适用网元：SGSN、MME**

该命令已废弃。

此命令为构建了主备容灾关系的两套 UNC 网元（互相称对方为容灾网元）配置容灾业务通道。

容灾业务通道是主网元的LINK_VNFC（简称主LINK）和备网元的LINK_VNFC（简称备LINK）之间的业务通道。

主备LINK定时在容灾业务通道上发送探测报文，检测对方是否正常。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-ASRCHN]] · ADD ASRCHN
- [[command/UNC/20.15.2/DSP-ASRCHN]] · DSP ASRCHN
- [[command/UNC/20.15.2/LST-ASRCHN]] · LST ASRCHN
- [[command/UNC/20.15.2/MOD-ASRCHN]] · MOD ASRCHN
- [[command/UNC/20.15.2/RMV-ASRCHN]] · RMV ASRCHN

## 证据

- 原始手册：`evidence/UNC/20.15.2/ASRCHN.md`
- 原始手册：`evidence/UNC/20.15.2/ASRCHN.md`
- 原始手册：`evidence/UNC/20.15.2/ASRCHN.md`
- 原始手册：`evidence/UNC/20.15.2/ASRCHN.md`
- 原始手册：`evidence/UNC/20.15.2/ASRCHN.md`
