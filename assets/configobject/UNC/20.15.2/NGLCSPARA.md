---
id: UNC@20.15.2@ConfigObject@NGLCSPARA
type: ConfigObject
name: NGLCSPARA（5G定位服务参数）
nf: UNC
version: 20.15.2
object_name: NGLCSPARA
object_kind: global_setting
applicable_nf:
- AMF
status: active
---

# NGLCSPARA（5G定位服务参数）

## 说明

![](设置5G定位服务参数（SET NGLCSPARA）_44007975.assets/notice_3.0-zh-cn_2.png)

开启定位服务功能后，为保护用户位置信息，应添加位置定位安全加固配置。

**适用NF：AMF**

该命令用于设置AMF的定位服务功能的相关参数。

Non-UE辅助定位流程中，AMF是否支持Namf_Communication_NonUeN2InfoSubscribe Request消息不携带globalRanNodeList信元受软参DWORD71 BIT7控制。

## 操作本对象的命令

- [LST NGLCSPARA](command/UNC/20.15.2/LST-NGLCSPARA.md)
- [SET NGLCSPARA](command/UNC/20.15.2/SET-NGLCSPARA.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G定位服务参数（LST-NGLCSPARA）_44007004.md`
- 原始手册：`evidence/UNC/20.15.2/设置5G定位服务参数（SET-NGLCSPARA）_44007975.md`
