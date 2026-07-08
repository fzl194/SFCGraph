---
id: UNC@20.15.2@ConfigObject@SMPDUCTRL
type: ConfigObject
name: SMPDUCTRL（PDU会话控制参数）
nf: UNC
version: 20.15.2
object_name: SMPDUCTRL
object_kind: global_setting
applicable_nf:
- AMF
status: active
---

# SMPDUCTRL（PDU会话控制参数）

## 说明

![](设置PDU会话控制参数（SET SMPDUCTRL）_44008047.assets/notice_3.0-zh-cn_2.png)

执行该命令配置的原因值不合理可能导致终端行为异常。

**适用NF：AMF**

该命令用于设置AMF管理PDU会话的控制参数，如UE使用某个DNN可建立的最大PDU会话数。

## 操作本对象的命令

- [LST SMPDUCTRL](command/UNC/20.15.2/LST-SMPDUCTRL.md)
- [SET SMPDUCTRL](command/UNC/20.15.2/SET-SMPDUCTRL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询PDU会话控制参数（LST-SMPDUCTRL）_44007229.md`
- 原始手册：`evidence/UNC/20.15.2/设置PDU会话控制参数（SET-SMPDUCTRL）_44008047.md`
