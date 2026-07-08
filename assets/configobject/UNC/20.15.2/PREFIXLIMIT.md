---
id: UNC@20.15.2@ConfigObject@PREFIXLIMIT
type: ConfigObject
name: PREFIXLIMIT（前缀限制）
nf: UNC
version: 20.15.2
object_name: PREFIXLIMIT
object_kind: global_setting
status: active
---

# PREFIXLIMIT（前缀限制）

## 说明

该命令用于配置前缀限制，缺省情况下，不限制IPv4（IPv6）的最大路由前缀数。

设备引入较多的路由会占用较多的系统资源，在系统业务繁忙时，这就有可能影响设备的正常运行。

为提高系统的安全性和可靠性，可以配置前缀限制对设备上指定的VPN实例的IPv4（IPv6）路由前缀数量进行限制。

配置前缀限制后，当路由前缀数超过预先设定的值时，系统会输出告警信息，从而提醒用户检查IPv4（IPv6）路由前缀的有效性。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-PREFIXLIMIT]] · LST PREFIXLIMIT
- [[command/UNC/20.15.2/SET-PREFIXLIMIT]] · SET PREFIXLIMIT

## 证据

- 原始手册：`evidence/UNC/20.15.2/PREFIXLIMIT.md`
- 原始手册：`evidence/UNC/20.15.2/PREFIXLIMIT.md`
