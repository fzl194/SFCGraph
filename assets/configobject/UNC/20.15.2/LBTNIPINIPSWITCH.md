---
id: UNC@20.15.2@ConfigObject@LBTNIPINIPSWITCH
type: ConfigObject
name: LBTNIPINIPSWITCH（CSLB隧道IP-in-IP开关）
nf: UNC
version: 20.15.2
object_name: LBTNIPINIPSWITCH
object_kind: global_setting
status: active
---

# LBTNIPINIPSWITCH（CSLB隧道IP-in-IP开关）

## 说明

![](设置CSLB隧道IP-in-IP开关（SET LBTNIPINIPSWITCH）_21584628.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，操作不当会导致容灾业务受损，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置CSLB隧道IP-in-IP功能开关配置。

该命令使用场景：网络防火墙存在对分片报文的带宽限制，会导致容灾业务受损。此时，配置容灾关系的网元，可开启CSLB隧道IP-in-IP功能开关，隧道中的IPV6分片报文会被重新进行UDP封装，避免网络防火墙对带宽的限制，防止容灾业务受损。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-LBTNIPINIPSWITCH]] · LST LBTNIPINIPSWITCH
- [[command/UNC/20.15.2/SET-LBTNIPINIPSWITCH]] · SET LBTNIPINIPSWITCH

## 证据

- 原始手册：`evidence/UNC/20.15.2/LBTNIPINIPSWITCH.md`
- 原始手册：`evidence/UNC/20.15.2/LBTNIPINIPSWITCH.md`
