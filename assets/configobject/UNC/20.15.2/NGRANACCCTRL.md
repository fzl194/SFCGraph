---
id: UNC@20.15.2@ConfigObject@NGRANACCCTRL
type: ConfigObject
name: NGRANACCCTRL（5G基站接入控制策略）
nf: UNC
version: 20.15.2
object_name: NGRANACCCTRL
object_kind: global_setting
applicable_nf:
- AMF
status: active
---

# NGRANACCCTRL（5G基站接入控制策略）

## 说明

![](设置5G基站接入控制策略（SET NGRANACCCTRL）_58492657.assets/notice_3.0-zh-cn_2.png)

功能开启前，需要对已接入基站的TAC进行检查，确认是否在规划范围内，避免功能开启后，已接入的基站断链后无法再次接入，导致业务受损。

**适用NF：AMF**

此命令用于配置5G基站接入控制参数，根据基站所在的TAC区域，控制是否允许基站接入。当希望只允许在白名单TAC区的基站接入时，可执行此命令。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-NGRANACCCTRL]] · LST NGRANACCCTRL
- [[command/UNC/20.15.2/SET-NGRANACCCTRL]] · SET NGRANACCCTRL

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G基站接入控制策略（LST-NGRANACCCTRL）_09253254.md`
- 原始手册：`evidence/UNC/20.15.2/设置5G基站接入控制策略（SET-NGRANACCCTRL）_58492657.md`
