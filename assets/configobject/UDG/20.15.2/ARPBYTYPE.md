---
id: UDG@20.15.2@ConfigObject@ARPBYTYPE
type: ConfigObject
name: ARPBYTYPE（根据ARP表项类型清除ARP表项）
nf: UDG
version: 20.15.2
object_name: ARPBYTYPE
object_kind: action
status: active
---

# ARPBYTYPE（根据ARP表项类型清除ARP表项）

## 说明

![](根据ARP表项类型清除ARP表项（RTR ARPBYTYPE）_50280966.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致业务故障，请谨慎使用并联系华为技术支持协助操作。

该命令用于删除设备上的动态表项。当非法用户发送大量ARP报文攻击目标设备时，会导致设备在短时间学习到大量的ARP信息，导致ARP表项缓存溢出，影响合法用户使用网络。为了解决这样的问题，用户可以执行此命令对ARP表项进行维护，重新建立ARP表项，从而保证合法用户正常使用网络。

## 操作本对象的命令

- [[command/UDG/20.15.2/RTR-ARPBYTYPE]] · RTR ARPBYTYPE

## 证据

- 原始手册：`evidence/UDG/20.15.2/ARPBYTYPE.md`
