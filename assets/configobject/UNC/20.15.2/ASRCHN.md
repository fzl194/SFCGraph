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

- [ADD ASRCHN](command/UNC/20.15.2/ADD-ASRCHN.md)
- [DSP ASRCHN](command/UNC/20.15.2/DSP-ASRCHN.md)
- [LST ASRCHN](command/UNC/20.15.2/LST-ASRCHN.md)
- [MOD ASRCHN](command/UNC/20.15.2/MOD-ASRCHN.md)
- [RMV ASRCHN](command/UNC/20.15.2/RMV-ASRCHN.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改容灾业务通道配置(MOD-ASRCHN)_72345727.md`
- 原始手册：`evidence/UNC/20.15.2/删除容灾业务通道配置(RMV-ASRCHN)_26146128.md`
- 原始手册：`evidence/UNC/20.15.2/增加容灾业务通道配置(ADD-ASRCHN)_26305936.md`
- 原始手册：`evidence/UNC/20.15.2/显示容灾业务通道状态(DSP-ASRCHN)_26305938.md`
- 原始手册：`evidence/UNC/20.15.2/查询容灾业务通道配置(LST-ASRCHN)_72225807.md`
