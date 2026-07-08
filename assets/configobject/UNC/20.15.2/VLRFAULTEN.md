---
id: UNC@20.15.2@ConfigObject@VLRFAULTEN
type: ConfigObject
name: VLRFAULTEN（VLR故障增强功能）
nf: UNC
version: 20.15.2
object_name: VLRFAULTEN
object_kind: global_setting
applicable_nf:
- MME
status: active
---

# VLRFAULTEN（VLR故障增强功能）

## 说明

![](设置VLR故障增强功能(SET VLRFAULTEN)_92948544.assets/notice_3.0-zh-cn_2.png)

该命令只有未部署IMS语音，并且VLR全部故障的场景下使用，否则可能造成整网语音不可用。在VLR恢复后请及时关闭该故障增强功能。

**适用网元：MME**

该命令用于设置VLR全故障场景增强功能开关。此配置仅在已明确VLR全故障的场景下应急使用，功能默认关闭。开启VLR故障增强开关后，在VLR全故障的场景下，通过模拟用户联合附着/TAU成功响应，使用户可以驻留4G使用数据业务。

## 操作本对象的命令

- [LST VLRFAULTEN](command/UNC/20.15.2/LST-VLRFAULTEN.md)
- [SET VLRFAULTEN](command/UNC/20.15.2/SET-VLRFAULTEN.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询VLR故障增强功能(LST-VLRFAULTEN)_35400473.md`
- 原始手册：`evidence/UNC/20.15.2/设置VLR故障增强功能(SET-VLRFAULTEN)_92948544.md`
