---
id: UNC@20.15.2@ConfigObject@SIGBVC
type: ConfigObject
name: SIGBVC（复位SigBvc）
nf: UNC
version: 20.15.2
object_name: SIGBVC
object_kind: action
applicable_nf:
- SGSN
status: active
---

# SIGBVC（复位SigBvc）

## 说明

![](复位SigBvc(RST SIGBVC)_26305840.assets/notice_3.0-zh-cn_2.png)

复位SIG信令实体将导致所有与该SIG信令实体相关的PTP实体被复位，所有相关小区的业务暂时中断。

**适用网元：SGSN**

该命令用于复位SigBvc信令实体，当系统发生影响信令实体功能的故障恢复时，可执行此命令，使BSS和SGSN两端同步初始化信令实体的相关上下文。SigBvc对应了一个NSE。BSS和SGSN中的网络业务实体提供了Gb接口运行需要的网络管理功能，网络业务实体在3GPP TS 48.016中详细描述。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-SIGBVC]] · DSP SIGBVC
- [[command/UNC/20.15.2/RST-SIGBVC]] · RST SIGBVC

## 证据

- 原始手册：`evidence/UNC/20.15.2/复位SigBvc(RST-SIGBVC)_26305840.md`
- 原始手册：`evidence/UNC/20.15.2/显示SigBvc上下文信息(DSP-SIGBVC)_72225709.md`
