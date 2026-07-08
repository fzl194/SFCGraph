---
id: UNC@20.15.2@ConfigObject@NFSERVICEVER
type: ConfigObject
name: NFSERVICEVER（NF服务版本信息）
nf: UNC
version: 20.15.2
object_name: NFSERVICEVER
object_kind: entity
applicable_nf:
- AMF
- SMF
- NSSF
- NRF
- SMSF
- NCG
status: active
---

# NFSERVICEVER（NF服务版本信息）

## 说明

![](添加NF服务版本信息（ADD NFSERVICEVER）_09653292.assets/notice_3.0-zh-cn_2.png)

若APIFULLVERSION配置不符合规范，会导致业务校验APIVERSIONINURI失败。

**适用NF：AMF、SMF、NSSF、NRF、SMSF、NCG**

该命令用于添加NFS实例的版本信息。NF向NRF注册的时候可以将NFS的该版本信息带给NRF，在后续的NF发现流程中，NRF可以自行根据版本信息进行决策。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NFSERVICEVER]] · ADD NFSERVICEVER
- [[command/UNC/20.15.2/LST-NFSERVICEVER]] · LST NFSERVICEVER
- [[command/UNC/20.15.2/RMV-NFSERVICEVER]] · RMV NFSERVICEVER

## 证据

- 原始手册：`evidence/UNC/20.15.2/NFSERVICEVER.md`
- 原始手册：`evidence/UNC/20.15.2/NFSERVICEVER.md`
- 原始手册：`evidence/UNC/20.15.2/NFSERVICEVER.md`
