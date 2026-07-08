---
id: UNC@20.15.2@ConfigObject@CDFTOKENWEIGHT
type: ConfigObject
name: CDFTOKENWEIGHT（cdf token权重）
nf: UNC
version: 20.15.2
object_name: CDFTOKENWEIGHT
object_kind: entity
applicable_nf:
- NCG
status: active
---

# CDFTOKENWEIGHT（cdf token权重）

## 说明

![](增加cdf的token权重（ADD CDFTOKENWEIGHT）_87839684.assets/notice_3.0-zh-cn_2.png)

当CDFTOKENPOLICY开关配置为使能且设置cdf token权重时，会影响各个cgfa-pod与cgfb-pod或cgfa2-pod与cgfb2-pod之间的token权重分配，从而影响话务量均衡。

**适用NF：NCG**

该命令用于设置cdf token权重。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-CDFTOKENWEIGHT]] · ADD CDFTOKENWEIGHT
- [[command/UNC/20.15.2/LST-CDFTOKENWEIGHT]] · LST CDFTOKENWEIGHT
- [[command/UNC/20.15.2/MOD-CDFTOKENWEIGHT]] · MOD CDFTOKENWEIGHT
- [[command/UNC/20.15.2/RMV-CDFTOKENWEIGHT]] · RMV CDFTOKENWEIGHT

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改cdf-token权重（MOD-CDFTOKENWEIGHT）_87360196.md`
- 原始手册：`evidence/UNC/20.15.2/删除cdf-token权重（RMV-CDFTOKENWEIGHT）_39919397.md`
- 原始手册：`evidence/UNC/20.15.2/增加cdf的token权重（ADD-CDFTOKENWEIGHT）_87839684.md`
- 原始手册：`evidence/UNC/20.15.2/查询cdf-token权重（LST-CDFTOKENWEIGHT）_87520116.md`
