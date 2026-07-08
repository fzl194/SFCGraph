---
id: UDG@20.15.2@ConfigObject@RESVNFC
type: ConfigObject
name: RESVNFC（复位VNFC）
nf: UDG
version: 20.15.2
object_name: RESVNFC
object_kind: action
status: active
---

# RESVNFC（复位VNFC）

## 说明

![](复位VNFC（RST RESVNFC）_51149357.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该命令会重启VNFP或指定的VNFC。如果是强制重启，还可能会导致正在操作的配置丢失，请谨慎使用并联系华为技术支持协助操作。

该命令用于重启VNFP或指定VNFC。

当VNFC出现系统异常时，可使用本命令进行恢复。

## 操作本对象的命令

- [[command/UDG/20.15.2/RST-RESVNFC]] · RST RESVNFC

## 证据

- 原始手册：`evidence/UDG/20.15.2/复位VNFC（RST-RESVNFC）_51149357.md`
