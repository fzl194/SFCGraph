---
id: UNC@20.15.2@ConfigObject@DHCPGIP
type: ConfigObject
name: DHCPGIP（支持DHCP服务的GGSN IP地址）
nf: UNC
version: 20.15.2
object_name: DHCPGIP
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# DHCPGIP（支持DHCP服务的GGSN IP地址）

## 说明

**适用网元：SGSN**

1. 该命令用于增加支持DHCP服务的GGSN IP地址。
2. SGSN支持用户采用DHCP方式接入，在采用DHCP接入方式时，不需要对APN进行DNS解析，只需要在SGSN中配置支持DHCP服务的GGSN IP地址即可。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-DHCPGIP]] · ADD DHCPGIP
- [[command/UNC/20.15.2/LST-DHCPGIP]] · LST DHCPGIP
- [[command/UNC/20.15.2/RMV-DHCPGIP]] · RMV DHCPGIP

## 证据

- 原始手册：`evidence/UNC/20.15.2/DHCPGIP.md`
- 原始手册：`evidence/UNC/20.15.2/DHCPGIP.md`
- 原始手册：`evidence/UNC/20.15.2/DHCPGIP.md`
