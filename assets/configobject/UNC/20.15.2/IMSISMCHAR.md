---
id: UNC@20.15.2@ConfigObject@IMSISMCHAR
type: ConfigObject
name: IMSISMCHAR（QoS协商参数）
nf: UNC
version: 20.15.2
object_name: IMSISMCHAR
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# IMSISMCHAR（QoS协商参数）

## 说明

![](增加QoS协商参数(ADD IMSISMCHAR)_26306040.assets/notice_3.0-zh-cn_2.png)

该命令将影响2/3G用户QOS的协商结果。

**适用网元：SGSN**

该命令用于增加SM属性配置：

- 当用户使用GPRS接入网接入并进行PDP激活时，分以下三种场景进行处理：
    - 如果用户所在的IMSI号段或用户归属地在该表中配置，并且“是否配置2G QoS”参数配置为“是”，系统使用该表中配置的2G QoS参数对PDP上下文使用的QoS进行限制。
    - 如果用户所在的IMSI号段或用户归属地在该表中配置，但是“是否配置2G QoS”参数配置为“否”，系统将为该条配置指定默认的2G QoS参数，系统使用匹配到“用户范围”为“ALL_USER（所有用户）”记录中所配置的默认QoS参数对PDP上下文使用的QoS进行限制。
    - 如果用户所在的IMSI号段和用户归属地未在该表中配置，系统使用该命令“用户范围”为“所有用户”记录中配置的QoS参数对PDP上下文使用的QoS进行限制。
- 当用户使用UMTS接入网接入并进行PDP激活时，分以下三种场景进行处理：
    - 如果用户所在的IMSI号段或用户归属地在该表中配置，并且“是否配置3G QoS”参数配置为“是”，系统使用该表中配置的3G QoS参数对PDP上下文使用的QoS进行限制。
    - 如果用户所在的IMSI号段或用户归属地在该表中配置，但是“是否配置3G QoS”参数配置为“否”，系统将为该条配置指定默认的3G QoS参数，系统使用匹配到“用户范围”为“ALL_USER（所有用户）”记录中所配置的默认QoS参数对PDP上下文使用的QoS进行限制。
    - 如果用户所在的IMSI号段和用户归属地未在该表中配置，系统使用该命令“用户范围”为“所有用户”记录中配置的QoS参数对PDP上下文使用的QoS进行限制。
- QoS各参数的取值及含义具体请参见3GPP TS 23.107（QoS协议）。
- 对于2G和3G QoS参数，当“协商方式”为“NET_NEGO_QOS（网络侧协商QoS）”或“MIX_QOS（混合模式）”时生效。

## 操作本对象的命令

- [ADD IMSISMCHAR](command/UNC/20.15.2/ADD-IMSISMCHAR.md)
- [LST IMSISMCHAR](command/UNC/20.15.2/LST-IMSISMCHAR.md)
- [MOD IMSISMCHAR](command/UNC/20.15.2/MOD-IMSISMCHAR.md)
- [RMV IMSISMCHAR](command/UNC/20.15.2/RMV-IMSISMCHAR.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改QoS协商参数(MOD-IMSISMCHAR)_26146230.md`
- 原始手册：`evidence/UNC/20.15.2/删除QoS协商参数(RMV-IMSISMCHAR)_72345829.md`
- 原始手册：`evidence/UNC/20.15.2/增加QoS协商参数(ADD-IMSISMCHAR)_26306040.md`
- 原始手册：`evidence/UNC/20.15.2/查询QoS协商参数(LST-IMSISMCHAR)_72225909.md`
