---
id: UNC@20.15.2@ConfigObject@PDPAPN
type: ConfigObject
name: PDPAPN（本地APN NI配置）
nf: UNC
version: 20.15.2
object_name: PDPAPN
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# PDPAPN（本地APN NI配置）

## 说明

**适用网元：SGSN、MME**

该命令用于增加指定用户PDP类型与APN NI地址的映射关系，即为指定用户PDP类型配置缺省的APNNI地址。

UNC 中一次激活场景和MME中PDN连接建立场景，用户匹配到野卡或者匹配到多组签约数据时，需要根据IMSI和PDP/PDN类型查询本地的APN NI。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PDPAPN]] · ADD PDPAPN
- [[command/UNC/20.15.2/LST-PDPAPN]] · LST PDPAPN
- [[command/UNC/20.15.2/MOD-PDPAPN]] · MOD PDPAPN
- [[command/UNC/20.15.2/RMV-PDPAPN]] · RMV PDPAPN

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改本地APN-NI配置(MOD-PDPAPN)_72225359.md`
- 原始手册：`evidence/UNC/20.15.2/删除本地APN-NI配置(RMV-PDPAPN)_26145680.md`
- 原始手册：`evidence/UNC/20.15.2/增加本地APN-NI配置(ADD-PDPAPN)_72345275.md`
- 原始手册：`evidence/UNC/20.15.2/查询本地APN-NI配置(LST-PDPAPN)_26305490.md`
