---
id: UNC@20.15.2@ConfigObject@SMFCAUSECTRL
type: ConfigObject
name: SMFCAUSECTRL（SMF流程控制参数）
nf: UNC
version: 20.15.2
object_name: SMFCAUSECTRL
object_kind: entity
applicable_nf:
- SMF
status: active
---

# SMFCAUSECTRL（SMF流程控制参数）

## 说明

![](增加SMF流程控制参数（ADD SMFCAUSECTRL）_09652124.assets/notice_3.0-zh-cn_2.png)

配置下发的原因值可能会对终端行为产生影响，对性能指标的统计值产生影响，在配置前请联系华为技术支持工程师评估影响。

**适用NF：SMF**

该命令用于增加SMF流程控制参数。当用户接入SMF时，UNC可通过该命令控制SMF流程特殊场景下指定的NAS原因值下发，以满足运营商实现对现网设备兼容性特殊控制的需求。关于不同原因值的含义及对终端行为的影响请参见协议3GPP TS 24.501。

## 操作本对象的命令

- [ADD SMFCAUSECTRL](command/UNC/20.15.2/ADD-SMFCAUSECTRL.md)
- [LST SMFCAUSECTRL](command/UNC/20.15.2/LST-SMFCAUSECTRL.md)
- [MOD SMFCAUSECTRL](command/UNC/20.15.2/MOD-SMFCAUSECTRL.md)
- [RMV SMFCAUSECTRL](command/UNC/20.15.2/RMV-SMFCAUSECTRL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SMF流程控制参数（MOD-SMFCAUSECTRL）_09652290.md`
- 原始手册：`evidence/UNC/20.15.2/删除SMF流程控制参数（RMV-SMFCAUSECTRL）_09653009.md`
- 原始手册：`evidence/UNC/20.15.2/增加SMF流程控制参数（ADD-SMFCAUSECTRL）_09652124.md`
- 原始手册：`evidence/UNC/20.15.2/查询SMF流程控制参数（LST-SMFCAUSECTRL）_09652371.md`
