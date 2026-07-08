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

- [[command/UNC/20.15.2/ADD-PGWRESEL]] · ADD PGWRESEL
- [[command/UNC/20.15.2/LST-PGWRESEL]] · LST PGWRESEL
- [[command/UNC/20.15.2/MOD-PGWRESEL]] · MOD PGWRESEL
- [[command/UNC/20.15.2/RMV-PGWRESEL]] · RMV PGWRESEL

## 证据

- 原始手册：`evidence/UNC/20.15.2/PGWRESEL.md`
- 原始手册：`evidence/UNC/20.15.2/PGWRESEL.md`
- 原始手册：`evidence/UNC/20.15.2/PGWRESEL.md`
- 原始手册：`evidence/UNC/20.15.2/PGWRESEL.md`
