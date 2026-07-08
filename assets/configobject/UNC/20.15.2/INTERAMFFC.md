---
id: UNC@20.15.2@ConfigObject@INTERAMFFC
type: ConfigObject
name: INTERAMFFC（Inter-AMF流控参数）
nf: UNC
version: 20.15.2
object_name: INTERAMFFC
object_kind: global_setting
applicable_nf:
- AMF
status: active
---

# INTERAMFFC（Inter-AMF流控参数）

## 说明

![](设置Inter-AMF流控参数（SET INTERAMFFC）_96243129.assets/notice_3.0-zh-cn_2.png)

存在较大操作风险，执行不当会导致业务受损或中断。

**适用NF：AMF**

设置Inter-AMF接入流控功能的相关参数。

AMF组Pool时，如果某个AMF故障，则故障AMF上的用户会接入到Pool内正常的AMF上，可能对正常AMF造成较大冲击，导致其过载。为了防止这类AMF间的新接入用户影响在网用户的正常业务，控制非本AMF用户的接入消息允许处理速率。这些消息包括：Registration Request(Initial类型携带5G-GUTI)、Service Request消息。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-INTERAMFFC]] · LST INTERAMFFC
- [[command/UNC/20.15.2/SET-INTERAMFFC]] · SET INTERAMFFC

## 证据

- 原始手册：`evidence/UNC/20.15.2/INTERAMFFC.md`
- 原始手册：`evidence/UNC/20.15.2/INTERAMFFC.md`
