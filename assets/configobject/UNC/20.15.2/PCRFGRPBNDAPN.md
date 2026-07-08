---
id: UNC@20.15.2@ConfigObject@PCRFGRPBNDAPN
type: ConfigObject
name: PCRFGRPBNDAPN（APN和Pcrf组关联关系）
nf: UNC
version: 20.15.2
object_name: PCRFGRPBNDAPN
object_kind: entity
applicable_nf:
- PGW-C
- GGSN
status: active
---

# PCRFGRPBNDAPN（APN和Pcrf组关联关系）

## 说明

**适用NF：PGW-C、GGSN**

此命令用来设置APN和Pcrf组关联关系。PCC即策略和计费控制，运营商可以通过PCC功能，做到对计费策略和计费粒度的灵活控制，从而优化运营商的计费手段，提高收益。从业务功能角度看，在MS用户激活或者更新过程中，可以选择由网元PCRF下发计费策略，做到业务级的QoS控制和计费，并可以动态调整策略。在UNC系统中，可以通过ADD PCRF等一系列命令实现该功能。在UNC系统的PCRF和PCRF分组配置都已经完成的情况下，UNC系统可以通过PCRF分组绑定功能，将PCC功能绑定到特定用户群。此命令即将某PCRF分组绑定到指定APN的用户上，当该APN的用户激活时，系统选择该分组下的Master PCRF进行业务处理。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PCRFGRPBNDAPN]] · ADD PCRFGRPBNDAPN
- [[command/UNC/20.15.2/LST-PCRFGRPBNDAPN]] · LST PCRFGRPBNDAPN
- [[command/UNC/20.15.2/MOD-PCRFGRPBNDAPN]] · MOD PCRFGRPBNDAPN
- [[command/UNC/20.15.2/RMV-PCRFGRPBNDAPN]] · RMV PCRFGRPBNDAPN

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改APN和Pcrf组关联关系（MOD-PCRFGRPBNDAPN）_09897107.md`
- 原始手册：`evidence/UNC/20.15.2/删除APN和Pcrf组关联关系（RMV-PCRFGRPBNDAPN）_09897108.md`
- 原始手册：`evidence/UNC/20.15.2/增加APN和Pcrf组关联关系（ADD-PCRFGRPBNDAPN）_09897106.md`
- 原始手册：`evidence/UNC/20.15.2/查询APN和Pcrf组关联关系（LST-PCRFGRPBNDAPN）_09897109.md`
