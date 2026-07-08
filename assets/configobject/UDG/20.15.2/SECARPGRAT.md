---
id: UDG@20.15.2@ConfigObject@SECARPGRAT
type: ConfigObject
name: SECARPGRAT（免费ARP过滤）
nf: UDG
version: 20.15.2
object_name: SECARPGRAT
object_kind: global_setting
status: active
---

# SECARPGRAT（免费ARP过滤）

## 说明

该命令用于设置免费ARP过滤。

当网络中有新的设备接入时，该设备会以广播的方式发送免费ARP报文，向网络中的其他设备通告自己的存在。由于任何设备都可以发送免费ARP报文，且设备接收免费ARP报文时无需身份验证，所以网络中很容易出现大量的免费ARP报文，这会导致设备忙于免费ARP报文的处理，造成CPU超载，影响其它业务的正常运行。当网络中存在非法用户恶意发送报文内容不合理的ARP报文，可能造成协议栈崩溃或CPU利用率很高，影响正常业务。为了防止网络中出现免费ARP报文攻击，可以执行SET SECARPGRAT命令配置免费ARP报文主动丢弃的功能。设备收到免费ARP报文后直接将其丢弃，减少CPU资源的消耗，从而保证了用户业务的优先级。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-SECARPGRAT]] · LST SECARPGRAT
- [[command/UDG/20.15.2/SET-SECARPGRAT]] · SET SECARPGRAT

## 证据

- 原始手册：`evidence/UDG/20.15.2/SECARPGRAT.md`
- 原始手册：`evidence/UDG/20.15.2/SECARPGRAT.md`
