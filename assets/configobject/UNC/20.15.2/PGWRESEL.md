---
id: UNC@20.15.2@ConfigObject@PGWRESEL
type: ConfigObject
name: PGWRESEL（本地P-GW重选策略）
nf: UNC
version: 20.15.2
object_name: PGWRESEL
object_kind: entity
applicable_nf:
- MME
status: active
---

# PGWRESEL（本地P-GW重选策略）

## 说明

**适用网元：MME**

该命令用于增加一条本地P-GW重选策略的配置记录。

UE在网络在中移动，可能造成S-GW与P-GW不属于同一区域。增加该配置后，系统可以针对指定APN的PDN连接，在对用户业务无影响的前提下，为UE重新选择和S-GW在同一区域的本地P-GW进行业务，节省网络中异地S-GW和P-GW之间的迂回流量，降低业务时延。

## 操作本对象的命令

- [ADD PGWRESEL](command/UNC/20.15.2/ADD-PGWRESEL.md)
- [LST PGWRESEL](command/UNC/20.15.2/LST-PGWRESEL.md)
- [MOD PGWRESEL](command/UNC/20.15.2/MOD-PGWRESEL.md)
- [RMV PGWRESEL](command/UNC/20.15.2/RMV-PGWRESEL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改本地P-GW重选策略(MOD-PGWRESEL)_26145714.md`
- 原始手册：`evidence/UNC/20.15.2/删除本地P-GW重选策略(RMV-PGWRESEL)_72345309.md`
- 原始手册：`evidence/UNC/20.15.2/增加本地P-GW重选策略(ADD-PGWRESEL)_26305522.md`
- 原始手册：`evidence/UNC/20.15.2/查询本地P-GW重选策略(LST-PGWRESEL)_72225393.md`
