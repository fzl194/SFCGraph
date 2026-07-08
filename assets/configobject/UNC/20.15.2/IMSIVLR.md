---
id: UNC@20.15.2@ConfigObject@IMSIVLR
type: ConfigObject
name: IMSIVLR（IMSI与VLR对应关系）
nf: UNC
version: 20.15.2
object_name: IMSIVLR
object_kind: entity
applicable_nf:
- MME
status: active
---

# IMSIVLR（IMSI与VLR对应关系）

## 说明

![](增加IMSI与VLR对应关系(ADD IMSIVLR)_72225129.assets/notice_3.0-zh-cn_2.png)

该命令可能导致SGs接口MSC/VLR选择方式发生变化，只建议对拨测用户使用该命令，拨测完成后请删除。请确认是否要继续？

**适用网元：MME**

该命令用于增加IMSI与MSC/VLR对应关系。当用户接入时，通过SGs接口选择MSC/VLR发送Location Update Request消息时，会优先选择IMSI对应的MSC/VLR。 该命令仅用于拨测场景，在MSC/VLR新割接入网后，可通过指定用户接入该MSC/VLR，拨测设备是否工作正常。拨测完毕后，请删除该命令以免后续影响该拨测用户。

如果选择的MSC/VLR处于“自动迁移中”或者“手动迁移中”状态，或者与当前IMSI匹配的MSC/VLR的链路异常时，会按照原有MSC/VLR选择方式重新进行选择，原有选择方式参见“WSFD- 102301 基于CSFB的语音业务”中的描述。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-IMSIVLR]] · ADD IMSIVLR
- [[command/UNC/20.15.2/LST-IMSIVLR]] · LST IMSIVLR
- [[command/UNC/20.15.2/MOD-IMSIVLR]] · MOD IMSIVLR
- [[command/UNC/20.15.2/RMV-IMSIVLR]] · RMV IMSIVLR

## 证据

- 原始手册：`evidence/UNC/20.15.2/IMSIVLR.md`
- 原始手册：`evidence/UNC/20.15.2/IMSIVLR.md`
- 原始手册：`evidence/UNC/20.15.2/IMSIVLR.md`
- 原始手册：`evidence/UNC/20.15.2/IMSIVLR.md`
