---
id: UNC@20.15.2@ConfigObject@PTPBVC
type: ConfigObject
name: PTPBVC（复位小区）
nf: UNC
version: 20.15.2
object_name: PTPBVC
object_kind: action
applicable_nf:
- SGSN
status: active
---

# PTPBVC（复位小区）

## 说明

![](复位小区(RST PTPBVC)_72345591.assets/notice_3.0-zh-cn_2.png)

复位小区会中断相关小区的服务。

**适用网元：SGSN**

该命令对GBP进程BSSGP层的PTPBVC实体进行复位。PTPBVC用来在对等点对点功能实体间传输BSSGP PDU，可参考 3GPP TS 08.18。

当系统发生影响PTP实体功能的故障恢复时，可执行此命令，使BSS和SGSN两端同步初始化PTP实体的相关上下文。

## 操作本对象的命令

- [DSP PTPBVC](command/UNC/20.15.2/DSP-PTPBVC.md)
- [RST PTPBVC](command/UNC/20.15.2/RST-PTPBVC.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/复位小区(RST-PTPBVC)_72345591.md`
- 原始手册：`evidence/UNC/20.15.2/显示小区上下文信息(DSP-PTPBVC)_26305800.md`
