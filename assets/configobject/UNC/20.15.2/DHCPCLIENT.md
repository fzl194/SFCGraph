---
id: UNC@20.15.2@ConfigObject@DHCPCLIENT
type: ConfigObject
name: DHCPCLIENT（DHCPv4客户端）
nf: UNC
version: 20.15.2
object_name: DHCPCLIENT
object_kind: entity
status: active
---

# DHCPCLIENT（DHCPv4客户端）

## 说明

该命令用于使能DHCPv4客户端功能，DHCPv4客户端通过DHCP协议向服务器请求分配一个IP地址。客户端申请地址时，先向服务器发送DHCP请求报文，服务器接收到请求报文后，将返回DHCP响应报文。DHCPv4客户端从接收到响应报文中可以获取所分配到的IP地址的相关信息。

## 操作本对象的命令

- [ADD DHCPCLIENT](command/UNC/20.15.2/ADD-DHCPCLIENT.md)
- [LST DHCPCLIENT](command/UNC/20.15.2/LST-DHCPCLIENT.md)
- [MOD DHCPCLIENT](command/UNC/20.15.2/MOD-DHCPCLIENT.md)
- [RMV DHCPCLIENT](command/UNC/20.15.2/RMV-DHCPCLIENT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改DHCPv4客户端（MOD-DHCPCLIENT）_00600529.md`
- 原始手册：`evidence/UNC/20.15.2/删除DHCPv4客户端（RMV-DHCPCLIENT）_49801902.md`
- 原始手册：`evidence/UNC/20.15.2/增加DHCPv4客户端（ADD-DHCPCLIENT）_50120978.md`
- 原始手册：`evidence/UNC/20.15.2/查询DHCPv4客户端配置（LST-DHCPCLIENT）_50121566.md`
