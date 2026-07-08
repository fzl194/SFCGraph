---
id: UNC@20.15.2@ConfigObject@NFTAI
type: ConfigObject
name: NFTAI（NF TAI信息）
nf: UNC
version: 20.15.2
object_name: NFTAI
object_kind: entity
applicable_nf:
- SMF
status: active
---

# NFTAI（NF TAI信息）

## 说明

**适用NF：SMF**

该命令用于添加NF实例支持的TAI信息。

- 当NF实例只支持为某些TAI服务时，需要对支持的TAI进行配置。
- 当SMF向NRF注册时，如果BINDSMFINFOID不为空或者“null”，则必须在ADD SMFINFOEXT中配置ID与BINDSMFINFOID相同的记录，否则该命令将不生效。
- 当NWDAF向NRF注册时，如果BINDNWDAFINFOID不为空或者“null”，则必须在ADD NWDAFINFOEXT中配置ID与BINDNWDAFINFOID相同的记录，否则该命令将不生效。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NFTAI]] · ADD NFTAI
- [[command/UNC/20.15.2/LST-NFTAI]] · LST NFTAI
- [[command/UNC/20.15.2/RMV-NFTAI]] · RMV NFTAI

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NF-TAI信息（RMV-NFTAI）_09652202.md`
- 原始手册：`evidence/UNC/20.15.2/增加NF-TAI信息（ADD-NFTAI）_09652077.md`
- 原始手册：`evidence/UNC/20.15.2/查询NF-TAI信息（LST-NFTAI）_09654437.md`
