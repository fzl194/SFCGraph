---
id: UNC@20.15.2@ConfigObject@SERVICEIPMCR
type: ConfigObject
name: SERVICEIPMCR（业务IP）
nf: UNC
version: 20.15.2
object_name: SERVICEIPMCR
object_kind: entity
applicable_nf:
- MME
status: active
---

# SERVICEIPMCR（业务IP）

## 说明

**适用网元：MME**

该命令用于配置业务IP地址。

- 命令[**ADD SDAPLE**](../../Sdup接口管理/Sdup接口业务地址管理/增加SDAP本地实体(ADD SDAPLE)_26147290.md)中的使用的地址或本端地址都必须引用该业务IP地址。不同的业务允许使用同一个业务IP地址，也允许使用不同的业务IP地址。
- 命令使用的VPN必须引用业务IP所属VPN实例。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-SERVICEIPMCR]] · ADD SERVICEIPMCR
- [[command/UNC/20.15.2/DSP-SERVICEIPMCR]] · DSP SERVICEIPMCR
- [[command/UNC/20.15.2/LST-SERVICEIPMCR]] · LST SERVICEIPMCR
- [[command/UNC/20.15.2/MOD-SERVICEIPMCR]] · MOD SERVICEIPMCR
- [[command/UNC/20.15.2/RMV-SERVICEIPMCR]] · RMV SERVICEIPMCR

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改业务IP(MOD-SERVICEIPMCR)_71850997.md`
- 原始手册：`evidence/UNC/20.15.2/删除业务IP(RMV-SERVICEIPMCR)_25291194.md`
- 原始手册：`evidence/UNC/20.15.2/增加业务IP(ADD-SERVICEIPMCR)_71731081.md`
- 原始手册：`evidence/UNC/20.15.2/显示业务IP(DSP-SERVICEIPMCR)_71731085.md`
- 原始手册：`evidence/UNC/20.15.2/查询业务IP(LST-SERVICEIPMCR)_25131366.md`
