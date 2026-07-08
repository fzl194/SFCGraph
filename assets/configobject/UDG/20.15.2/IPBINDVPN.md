---
id: UDG@20.15.2@ConfigObject@IPBINDVPN
type: ConfigObject
name: IPBINDVPN（接口绑定VPN）
nf: UDG
version: 20.15.2
object_name: IPBINDVPN
object_kind: binding
status: active
---

# IPBINDVPN（接口绑定VPN）

## 说明

该命令用于配置接口绑定VPN。配置VPN实例后，需要将设备上与VPN网络连接的接口与VPN实例绑定。接口与VPN实例绑定后，该接口将变为私网接口，可以配置私网地址、运行私网路由协议等，从而使该接口进入的报文使用VPN实例中的转发信息进行转发。如果要配置私网下的IPv6地址，请使用该命令配置接口下VPN之后，使用ADD IFIPV6ADDRESS命令配置IPv6地址。

## 操作本对象的命令

- [ADD IPBINDVPN](command/UDG/20.15.2/ADD-IPBINDVPN.md)
- [LST IPBINDVPN](command/UDG/20.15.2/LST-IPBINDVPN.md)
- [MOD IPBINDVPN](command/UDG/20.15.2/MOD-IPBINDVPN.md)
- [RMV IPBINDVPN](command/UDG/20.15.2/RMV-IPBINDVPN.md)

## 关联对象

- [GRETUNNEL](configobject/UDG/20.15.2/GRETUNNEL.md)
- [INTERFACE](configobject/UDG/20.15.2/INTERFACE.md)
- [L3VPNINST](configobject/UDG/20.15.2/L3VPNINST.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改接口绑定VPN（MOD-IPBINDVPN）_49962014.md`
- 原始手册：`evidence/UDG/20.15.2/删除接口绑定VPN（RMV-IPBINDVPN）_50281362.md`
- 原始手册：`evidence/UDG/20.15.2/增加接口绑定VPN（ADD-IPBINDVPN）_50120734.md`
- 原始手册：`evidence/UDG/20.15.2/查询接口绑定VPN（LST-IPBINDVPN）_00601457.md`
