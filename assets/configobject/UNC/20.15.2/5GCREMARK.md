---
id: UNC@20.15.2@ConfigObject@5GCREMARK
type: ConfigObject
name: 5GCREMARK（5GC QoS到TOS/DSCP的映射规则）
nf: UNC
version: 20.15.2
object_name: 5GCREMARK
object_kind: entity
applicable_nf:
- SMF
status: active
---

# 5GCREMARK（5GC QoS到TOS/DSCP的映射规则）

## 说明

**适用NF：SMF**

该命令用来增加5G用户QoS参数到IP报头中的DSCP（区别服务编码点）/TOS（服务类型）的映射规则，用户的数据将根据映射得到的DSCP（区别服务编码点）/TOS（服务类型）中的参数值进行转发。

## 操作本对象的命令

- [ADD 5GCREMARK](command/UNC/20.15.2/ADD-5GCREMARK.md)
- [LST 5GCREMARK](command/UNC/20.15.2/LST-5GCREMARK.md)
- [MOD 5GCREMARK](command/UNC/20.15.2/MOD-5GCREMARK.md)
- [RMV 5GCREMARK](command/UNC/20.15.2/RMV-5GCREMARK.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改5GC-QoS到TOS_DSCP的映射规则（MOD-5GCREMARK）_09652540.md`
- 原始手册：`evidence/UNC/20.15.2/删除5GC-QoS到TOS_DSCP的映射规则（RMV-5GCREMARK）_09652352.md`
- 原始手册：`evidence/UNC/20.15.2/增加5GC-QoS到TOS_DSCP的映射规则（ADD-5GCREMARK）_09653051.md`
- 原始手册：`evidence/UNC/20.15.2/查询5GC-QoS到TOS_DSCP的映射规则（LST-5GCREMARK）_09652281.md`
