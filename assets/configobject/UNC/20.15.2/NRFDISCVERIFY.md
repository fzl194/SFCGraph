---
id: UNC@20.15.2@ConfigObject@NRFDISCVERIFY
type: ConfigObject
name: NRFDISCVERIFY（服务发现NF属性冲突核验参数）
nf: UNC
version: 20.15.2
object_name: NRFDISCVERIFY
object_kind: global_setting
applicable_nf:
- NRF
status: active
---

# NRFDISCVERIFY（服务发现NF属性冲突核验参数）

## 说明

![](设置服务发现NF属性冲突核验参数（SET NRFDISCVERIFY）_88377454.assets/notice_3.0-zh-cn_2.png)

开启核验后，单进程最大核验速率设置过大或不控制可能会引起服务发现进程CPU升高，请谨慎设置。

**适用NF：NRF**

该命令用于设置服务发现结果NF属性冲突核验参数，便于控制服务发现流程中NF属性冲突核验行为。当前支持以下两种核验方法：

- 本NRF管理的同类型NF间属性冲突交叉验证：选中的属性和服务发现流程的请求参数有交集，并且本次服务发现结果中有多个匹配的NF，如果这些NF的实例标识中对应的大区及省份信息不一致，则判断存在NF间属性冲突，并上报ALM-100325 服务发现NF属性核验冲突告警。
- NF属性与跨NRF寻址信息冲突交叉验证：选中的属性和服务发现流程的请求参数有交集，并且本NRF服务发现结果中有匹配的NF，NRF会对跨NRF的寻址信息进行核验，如果服务发现参数能匹配上跨NRF寻址信息，则判断存在NF属性与跨NRF寻址信息冲突，并上报ALM-100325 服务发现NF属性核验冲突告警。
  以上两种核验冲突不影响本次服务发现结果的返回。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-NRFDISCVERIFY]] · LST NRFDISCVERIFY
- [[command/UNC/20.15.2/SET-NRFDISCVERIFY]] · SET NRFDISCVERIFY

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询服务发现NF属性冲突核验参数（LST-NRFDISCVERIFY）_35374739.md`
- 原始手册：`evidence/UNC/20.15.2/设置服务发现NF属性冲突核验参数（SET-NRFDISCVERIFY）_88377454.md`
