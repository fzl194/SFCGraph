---
id: UNC@20.15.2@ConfigObject@NGALGPRIORITY
type: ConfigObject
name: NGALGPRIORITY（5G算法优先级属性）
nf: UNC
version: 20.15.2
object_name: NGALGPRIORITY
object_kind: entity
applicable_nf:
- AMF
status: active
---

# NGALGPRIORITY（5G算法优先级属性）

## 说明

![](增加5G算法优先级属性（ADD NGALGPRIORITY）_09652959.assets/notice_3.0-zh-cn_2.png)

执行该命令配置的加密性算法或者完整性算法优先级不合理，可能导致终端接入异常。

**适用NF：AMF**

该命令用于增加加密或完整性算法的优先级属性。

AMF根据加密或完整性算法的优先级属性，在UE和AMF同时支持的前提下，选择优先级最高的算法发送给UE，用以对NAS消息的加密和完整性保护。如果所有算法均未设置优先级属性，系统会根据各算法的默认优先级属性（从高到低依次为AES、SNOW 3G、ZUC、空加密算法）和UE进行协商，最终确定采用的加密或完整性算法。

## 操作本对象的命令

- [ADD NGALGPRIORITY](command/UNC/20.15.2/ADD-NGALGPRIORITY.md)
- [LST NGALGPRIORITY](command/UNC/20.15.2/LST-NGALGPRIORITY.md)
- [MOD NGALGPRIORITY](command/UNC/20.15.2/MOD-NGALGPRIORITY.md)
- [RMV NGALGPRIORITY](command/UNC/20.15.2/RMV-NGALGPRIORITY.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改5G算法优先级属性（MOD-NGALGPRIORITY）_09653199.md`
- 原始手册：`evidence/UNC/20.15.2/删除5G算法优先级属性（RMV-NGALGPRIORITY）_09652634.md`
- 原始手册：`evidence/UNC/20.15.2/增加5G算法优先级属性（ADD-NGALGPRIORITY）_09652959.md`
- 原始手册：`evidence/UNC/20.15.2/查询5G算法优先级属性（LST-NGALGPRIORITY）_09652999.md`
