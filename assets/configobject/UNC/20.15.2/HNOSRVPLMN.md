---
id: UNC@20.15.2@ConfigObject@HNOSRVPLMN
type: ConfigObject
name: HNOSRVPLMN（归属网络Serving PLMN信息）
nf: UNC
version: 20.15.2
object_name: HNOSRVPLMN
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# HNOSRVPLMN（归属网络Serving PLMN信息）

## 说明

**适用网元：SGSN**

在MOCN、GWCN下，当一个运营商有多个HPLMN时，可以通过此命令为当前运营商的Non-supporting UE提供一个或多个Serving PLMN。

在MOCN、GWCN下，当一个运营商有多个HPLMN时，运营商通常对外只使用一个PLMN ID，这样使在用户呈现上和网间计费结算上更为简洁，因此一般只为一个运营商配置一个Serving PLMN。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-HNOSRVPLMN]] · ADD HNOSRVPLMN
- [[command/UNC/20.15.2/LST-HNOSRVPLMN]] · LST HNOSRVPLMN
- [[command/UNC/20.15.2/MOD-HNOSRVPLMN]] · MOD HNOSRVPLMN
- [[command/UNC/20.15.2/RMV-HNOSRVPLMN]] · RMV HNOSRVPLMN

## 证据

- 原始手册：`evidence/UNC/20.15.2/HNOSRVPLMN.md`
- 原始手册：`evidence/UNC/20.15.2/HNOSRVPLMN.md`
- 原始手册：`evidence/UNC/20.15.2/HNOSRVPLMN.md`
- 原始手册：`evidence/UNC/20.15.2/HNOSRVPLMN.md`
