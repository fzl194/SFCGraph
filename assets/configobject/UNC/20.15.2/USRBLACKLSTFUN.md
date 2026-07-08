---
id: UNC@20.15.2@ConfigObject@USRBLACKLSTFUN
type: ConfigObject
name: USRBLACKLSTFUN（用户黑名单接入控制功能）
nf: UNC
version: 20.15.2
object_name: USRBLACKLSTFUN
object_kind: global_setting
applicable_nf:
- SGSN
- MME
- AMF
status: active
---

# USRBLACKLSTFUN（用户黑名单接入控制功能）

## 说明

![](设置用户黑名单接入控制功能（SET USRBLACKLSTFUN）_65393486.assets/notice_3.0-zh-cn_2.png)

执行此命令，如果参数“RESTRICTSW”误配为“YES”，可能导致用户无法接入。

**适用NF：SGSN、MME、AMF**

该命令用于设置用户黑名单接入限制功能开关以及拒绝原因值。

## 操作本对象的命令

- [LST USRBLACKLSTFUN](command/UNC/20.15.2/LST-USRBLACKLSTFUN.md)
- [SET USRBLACKLSTFUN](command/UNC/20.15.2/SET-USRBLACKLSTFUN.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询用户黑名单接入控制功能（LST-USRBLACKLSTFUN）_65233886.md`
- 原始手册：`evidence/UNC/20.15.2/设置用户黑名单接入控制功能（SET-USRBLACKLSTFUN）_65393486.md`
