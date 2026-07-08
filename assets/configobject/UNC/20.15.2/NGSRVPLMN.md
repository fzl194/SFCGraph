---
id: UNC@20.15.2@ConfigObject@NGSRVPLMN
type: ConfigObject
name: NGSRVPLMN（5G Serving PLMN）
nf: UNC
version: 20.15.2
object_name: NGSRVPLMN
object_kind: entity
applicable_nf:
- SGW-C
- PGW-C
- AMF
- SMF
- NRF
- NSSF
status: active
---

# NGSRVPLMN（5G Serving PLMN）

## 说明

**适用NF：SGW-C、PGW-C、AMF、SMF、NRF、NSSF**

该命令用于为运营商配置Serving PLMN信息。

运营商的每个签约用户都有其所归属的Home PLMN。从运营商的角度，如果其签约用户数量较多，分别归属于不同的Home PLMN，那么我们称这个运营商支持多Home PLMN。运营商支持多Home PLMN场景下，往往不需要在每个Home PLMN下配置网络切片，或者将每个Home PLMN下发给接入侧，而是使用某个或者某几个PLMN来代表该运营商网络，我们称这样的PLMN为该运营商的Serving PLMN。简言之，Serving PLMN就是当前为UE提供服务的运营商的PLMN。运营商在Serving PLMN下配置网络切片（见ADD PLMNNS）、GUAMI，在基站建链时，AMF将Serving PLMN下发给接入侧。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NGSRVPLMN]] · ADD NGSRVPLMN
- [[command/UNC/20.15.2/LST-NGSRVPLMN]] · LST NGSRVPLMN
- [[command/UNC/20.15.2/MOD-NGSRVPLMN]] · MOD NGSRVPLMN
- [[command/UNC/20.15.2/RMV-NGSRVPLMN]] · RMV NGSRVPLMN

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改5G-Serving-PLMN（MOD-NGSRVPLMN）_09653241.md`
- 原始手册：`evidence/UNC/20.15.2/删除5G-Serving-PLMN（RMV-NGSRVPLMN）_09653774.md`
- 原始手册：`evidence/UNC/20.15.2/增加5G-Serving-PLMN（ADD-NGSRVPLMN）_09654167.md`
- 原始手册：`evidence/UNC/20.15.2/查询5G-Serving-PLMN（LST-NGSRVPLMN）_09652615.md`
