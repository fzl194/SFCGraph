---
id: UDG@20.15.2@ConfigObject@IPBINDVPNIPSEC
type: ConfigObject
name: IPBINDVPNIPSEC（接口绑定VPN）
nf: UDG
version: 20.15.2
object_name: IPBINDVPNIPSEC
object_kind: binding
status: active
---

# IPBINDVPNIPSEC（接口绑定VPN）

## 说明

![](增加接口绑定VPN（ADD IPBINDVPNIPSEC）_80751060.assets/notice_3.0-zh-cn.png)

该配置影响该隧道下的地址信息，有业务影响。

该命令用于配置接口绑定VPN。

> **说明**
> - 该命令执行后立即生效。
>
> - 执行该命令将清除该接口下所有的IP配置。
> - 需要在执行[**ADD IPSECINTFCFGIPSEC**](../../IP安全管理/互联网密钥交换/IPsec接口配置/增加IPsec隧道接口（ADD IPSECINTFCFGIPSEC）_80910986.md)之前执行该命令，来使绑定的VPN生效。
>
> - 最多可输入65535条记录。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-IPBINDVPNIPSEC]] · ADD IPBINDVPNIPSEC
- [[command/UDG/20.15.2/LST-IPBINDVPNIPSEC]] · LST IPBINDVPNIPSEC
- [[command/UDG/20.15.2/MOD-IPBINDVPNIPSEC]] · MOD IPBINDVPNIPSEC
- [[command/UDG/20.15.2/RMV-IPBINDVPNIPSEC]] · RMV IPBINDVPNIPSEC

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改接口绑定VPN（MOD-IPBINDVPNIPSEC）_26150759.md`
- 原始手册：`evidence/UDG/20.15.2/删除接口绑定VPN（RMV-IPBINDVPNIPSEC）_25830701.md`
- 原始手册：`evidence/UDG/20.15.2/增加接口绑定VPN（ADD-IPBINDVPNIPSEC）_80751060.md`
- 原始手册：`evidence/UDG/20.15.2/查询接口绑定VPN（LST-IPBINDVPNIPSEC）_26032195.md`
