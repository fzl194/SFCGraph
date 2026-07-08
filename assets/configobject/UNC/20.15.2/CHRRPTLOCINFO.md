---
id: UNC@20.15.2@ConfigObject@CHRRPTLOCINFO
type: ConfigObject
name: CHRRPTLOCINFO（CHR本地存盘位置配置）
nf: UNC
version: 20.15.2
object_name: CHRRPTLOCINFO
object_kind: entity
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
status: active
---

# CHRRPTLOCINFO（CHR本地存盘位置配置）

## 说明

![](增加CHR本地存盘位置配置（ADD CHRRPTLOCINFO）_15429033.assets/notice_3.0-zh-cn_2.png)

开启基于位置信息的小范围CHR用户上报时，需要开启软参流控，若未开启软参流控，可能导致OMU过载，引起系统异常复位。

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用来配置需要本地存储CHR的用户位置过滤条件，包括N2TAC、S1TAC、LACRAC、eNodeB、gNodeB。

## 操作本对象的命令

- [ADD CHRRPTLOCINFO](command/UNC/20.15.2/ADD-CHRRPTLOCINFO.md)
- [LST CHRRPTLOCINFO](command/UNC/20.15.2/LST-CHRRPTLOCINFO.md)
- [MOD CHRRPTLOCINFO](command/UNC/20.15.2/MOD-CHRRPTLOCINFO.md)
- [RMV CHRRPTLOCINFO](command/UNC/20.15.2/RMV-CHRRPTLOCINFO.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改CHR本地存盘位置配置（MOD-CHRRPTLOCINFO）_79789962.md`
- 原始手册：`evidence/UNC/20.15.2/删除CHR本地存盘位置配置（RMV-CHRRPTLOCINFO）_15343997.md`
- 原始手册：`evidence/UNC/20.15.2/增加CHR本地存盘位置配置（ADD-CHRRPTLOCINFO）_15429033.md`
- 原始手册：`evidence/UNC/20.15.2/查询CHR本地存盘位置配置（LST-CHRRPTLOCINFO）_79944706.md`
