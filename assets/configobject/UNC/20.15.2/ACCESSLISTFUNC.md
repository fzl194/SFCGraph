---
id: UNC@20.15.2@ConfigObject@ACCESSLISTFUNC
type: ConfigObject
name: ACCESSLISTFUNC（接入控制名单功能）
nf: UNC
version: 20.15.2
object_name: ACCESSLISTFUNC
object_kind: global_setting
applicable_nf:
- GGSN
- SGW-C
- PGW-C
status: active
---

# ACCESSLISTFUNC（接入控制名单功能）

## 说明

**适用NF：GGSN、SGW-C、PGW-C**

该命令用来配置当前系统是否支持接入控制名单的功能以及系统支持的接入控制名单类型。假设运营商希望允许或者禁止某个名单接入，使用该命令。

当配置SGSN/S-GW/MME IP地址黑白名单控制类型为白名单时，如果SGSN/S-GW/MME信令面IP没有落在该命令配置的SGSN/S-GW/MME IP和掩码所表示的地址段里，用户激活或更新失败，失败原因码：service not supported。

当配置SGSN/S-GW/MME IP地址黑白名单控制类型为黑名单时，如果SGSN/S-GW/MME信令面IP落在该命令配置的SGSN/S-GW/MME IP和掩码所表示的地址段里，用户激活或更新失败，失败原因码：service not supported。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-ACCESSLISTFUNC]] · LST ACCESSLISTFUNC
- [[command/UNC/20.15.2/SET-ACCESSLISTFUNC]] · SET ACCESSLISTFUNC

## 证据

- 原始手册：`evidence/UNC/20.15.2/ACCESSLISTFUNC.md`
- 原始手册：`evidence/UNC/20.15.2/ACCESSLISTFUNC.md`
