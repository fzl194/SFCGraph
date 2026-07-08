---
id: UNC@20.15.2@ConfigObject@PCSCFGRPBINDIMSI
type: ConfigObject
name: PCSCFGRPBINDIMSI（P-CSCF组和IMSI/MSISDN号段的绑定关系）
nf: UNC
version: 20.15.2
object_name: PCSCFGRPBINDIMSI
object_kind: binding
applicable_nf:
- SMF
- GGSN
- PGW-C
status: active
---

# PCSCFGRPBINDIMSI（P-CSCF组和IMSI/MSISDN号段的绑定关系）

## 说明

**适用NF：SMF、GGSN、PGW-C**

该命令用于将指定的p-cscf组绑定到指定的号段。在网络中规划IMS业务时，该命令可以把指定的号段和p-cscf组绑定。

## 操作本对象的命令

- [ADD PCSCFGRPBINDIMSI](command/UNC/20.15.2/ADD-PCSCFGRPBINDIMSI.md)
- [LST PCSCFGRPBINDIMSI](command/UNC/20.15.2/LST-PCSCFGRPBINDIMSI.md)
- [MOD PCSCFGRPBINDIMSI](command/UNC/20.15.2/MOD-PCSCFGRPBINDIMSI.md)
- [RMV PCSCFGRPBINDIMSI](command/UNC/20.15.2/RMV-PCSCFGRPBINDIMSI.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改P-CSCF组和IMSI_MSISDN号段的绑定关系（MOD-PCSCFGRPBINDIMSI）_76878556.md`
- 原始手册：`evidence/UNC/20.15.2/删除P-CSCF组和IMSI_MSISDN号段的绑定关系（RMV-PCSCFGRPBINDIMSI）_09653017.md`
- 原始手册：`evidence/UNC/20.15.2/增加P-CSCF组和IMSI_MSISDN号段的绑定关系（ADD-PCSCFGRPBINDIMSI）_09654389.md`
- 原始手册：`evidence/UNC/20.15.2/查询P-CSCF组和IMSI_MSISDN号段的绑定关系（LST-PCSCFGRPBINDIMSI）_09652383.md`
