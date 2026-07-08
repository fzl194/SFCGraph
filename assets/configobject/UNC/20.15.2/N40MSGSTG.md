---
id: UNC@20.15.2@ConfigObject@N40MSGSTG
type: ConfigObject
name: N40MSGSTG（缓存开关、回放间隔、回放速率）
nf: UNC
version: 20.15.2
object_name: N40MSGSTG
object_kind: global_setting
applicable_nf:
- SMF
- PGW-C
status: active
---

# N40MSGSTG（缓存开关、回放间隔、回放速率）

## 说明

![](设置缓存开关、回放间隔、回放速率（SET N40MSGSTG）_34667405.assets/notice_3.0-zh-cn_2.png)

当打开缓存功能后，需要使用命令SET CNVRGDCHGPARA配置参数CHGDATAREFGEN为SMF，即配置生成ChargingDataRef的方法为使用SMF生成，如果使用CHF生成ChargingDataRef时，可能导致放通用户用量丢失。

**适用NF：SMF、PGW-C**

该命令用于设置缓存开关、回放间隔、回放速率。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-N40MSGSTG]] · LST N40MSGSTG
- [[command/UNC/20.15.2/SET-N40MSGSTG]] · SET N40MSGSTG

## 证据

- 原始手册：`evidence/UNC/20.15.2/N40MSGSTG.md`
- 原始手册：`evidence/UNC/20.15.2/N40MSGSTG.md`
