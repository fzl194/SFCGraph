---
id: UNC@20.15.2@ConfigObject@NFUPDATE
type: ConfigObject
name: NFUPDATE（更新NF注册信息）
nf: UNC
version: 20.15.2
object_name: NFUPDATE
object_kind: global_setting
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- NCG
- SMSF
status: active
---

# NFUPDATE（更新NF注册信息）

## 说明

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG**

该命令用于设置NF信息更新推送到NRF的方式。

- 设置Patch更新缓存最大数量为N，如果NF的Patch更新在缓存中累计的次数到达N，则会立即将NF的更新信息推送到NRF，否则，更新信息缓存起来不推送。
- 设置Patch更新定时推送任务时长(分钟)为L，Patch更新在缓存中停留L时长后会被推送到NRF，L为0表示不使用定时推送。
- Patch更新缓存限制数量与Patch更新定时推送任务时长(分钟)中任意一个条件满足都会进行Patch更新推送。

## 操作本对象的命令

- [ACT NFUPDATE](command/UNC/20.15.2/ACT-NFUPDATE.md)
- [LST NFUPDATE](command/UNC/20.15.2/LST-NFUPDATE.md)
- [SET NFUPDATE](command/UNC/20.15.2/SET-NFUPDATE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/更新NF注册信息（ACT-NFUPDATE）_09652336.md`
- 原始手册：`evidence/UNC/20.15.2/查询NF更新方式（LST-NFUPDATE）_09653014.md`
- 原始手册：`evidence/UNC/20.15.2/设置NF更新方式（SET-NFUPDATE）_09651782.md`
