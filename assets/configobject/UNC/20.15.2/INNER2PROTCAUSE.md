---
id: UNC@20.15.2@ConfigObject@INNER2PROTCAUSE
type: ConfigObject
name: INNER2PROTCAUSE（内部原因值映射为协议原因值的配置）
nf: UNC
version: 20.15.2
object_name: INNER2PROTCAUSE
object_kind: entity
applicable_nf:
- SGW-C
- PGW-C
- GGSN
- SMF
status: active
---

# INNER2PROTCAUSE（内部原因值映射为协议原因值的配置）

## 说明

![](增加内部原因值映射为协议原因值的配置（ADD INNER2PROTCAUSE）_44226317.assets/notice_3.0-zh-cn_2.png)

配置下发的原因值可能会对终端行为产生影响，对性能指标的统计值产生影响，在配置前请联系华为研发工程师评估影响。

**适用NF：SGW-C、PGW-C、GGSN、SMF**

该命令用于增加内部原因值映射为协议原因值的配置。

当现网出现协议原因值不合理，客户要求修改的场景下需要使用该命令进行修改。

## 操作本对象的命令

- [ADD INNER2PROTCAUSE](command/UNC/20.15.2/ADD-INNER2PROTCAUSE.md)
- [LST INNER2PROTCAUSE](command/UNC/20.15.2/LST-INNER2PROTCAUSE.md)
- [RMV INNER2PROTCAUSE](command/UNC/20.15.2/RMV-INNER2PROTCAUSE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除内部原因值映射为协议原因值的配置（RMV-INNER2PROTCAUSE）_44106693.md`
- 原始手册：`evidence/UNC/20.15.2/增加内部原因值映射为协议原因值的配置（ADD-INNER2PROTCAUSE）_44226317.md`
- 原始手册：`evidence/UNC/20.15.2/查询内部原因值映射为协议原因值的配置（LST-INNER2PROTCAUSE）_93747100.md`
