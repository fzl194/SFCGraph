---
id: UNC@20.15.2@ConfigObject@CHGRATECTRL
type: ConfigObject
name: CHGRATECTRL（计费速率控制）
nf: UNC
version: 20.15.2
object_name: CHGRATECTRL
object_kind: global_setting
applicable_nf:
- PGW-C
- SMF
status: active
---

# CHGRATECTRL（计费速率控制）

## 说明

**适用NF：PGW-C、SMF**

![](计费速率控制（SET CHGRATECTRL）_09896823.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，ONLINEREC --- POD粒度生效，如果现网smpod个数多，可能导致对UPF，OCS造成信令冲击； CONVERGEDREC --- 整机粒度生效，配置上限1000条/s，对周边无影响;

该命令用于设置每个POD上，当在线计费用户转离线后，每秒最大离线转在线的用户数。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-CHGRATECTRL]] · LST CHGRATECTRL
- [[command/UNC/20.15.2/SET-CHGRATECTRL]] · SET CHGRATECTRL

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示计费速率控制（LST-CHGRATECTRL）_09896824.md`
- 原始手册：`evidence/UNC/20.15.2/计费速率控制（SET-CHGRATECTRL）_09896823.md`
