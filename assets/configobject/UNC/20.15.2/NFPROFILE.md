---
id: UNC@20.15.2@ConfigObject@NFPROFILE
type: ConfigObject
name: NFPROFILE（NF实例概述信息）
nf: UNC
version: 20.15.2
object_name: NFPROFILE
object_kind: entity
applicable_nf:
- AMF
- SMF
- NSSF
- NRF
- NCG
- SMSF
status: active
---

# NFPROFILE（NF实例概述信息）

## 说明

**适用NF：AMF、SMF、NSSF、NRF、NCG、SMSF**

该命令用于添加NF实例的概述信息。当NF实例向NRF注册时，可以将实例的概述信息带给NRF，为在业务流程中其他NF发现该NF时提供选择信息。配置的本端NFPROFILE类型为向NRF服务订阅时携带的本端网元类型。

## 操作本对象的命令

- [ADD NFPROFILE](command/UNC/20.15.2/ADD-NFPROFILE.md)
- [LST NFPROFILE](command/UNC/20.15.2/LST-NFPROFILE.md)
- [MOD NFPROFILE](command/UNC/20.15.2/MOD-NFPROFILE.md)
- [RMV NFPROFILE](command/UNC/20.15.2/RMV-NFPROFILE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改NF实例概述信息（MOD-NFPROFILE）_09652236.md`
- 原始手册：`evidence/UNC/20.15.2/删除NF实例概述信息（RMV-NFPROFILE）_09651742.md`
- 原始手册：`evidence/UNC/20.15.2/增加NF实例概述信息（ADD-NFPROFILE）_09654146.md`
- 原始手册：`evidence/UNC/20.15.2/查询NF实例概述信息（LST-NFPROFILE）_09651589.md`
