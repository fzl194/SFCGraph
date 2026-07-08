---
id: UDG@20.15.2@ConfigObject@SFEBFDPKTIPID
type: ConfigObject
name: SFEBFDPKTIPID（BFD报文IPID的使能标记）
nf: UDG
version: 20.15.2
object_name: SFEBFDPKTIPID
object_kind: global_setting
status: active
---

# SFEBFDPKTIPID（BFD报文IPID的使能标记）

## 说明

该命令用于控制BFD探测报文中IPID字段是否填充。IPID为IP报文头中Identification字段的简称，它为一个计数器，每发一个报文，IPID自增1，填充后可以方便查看报文流向，帮助问题定位。

## 操作本对象的命令

- [SET SFEBFDPKTIPID](command/UDG/20.15.2/SET-SFEBFDPKTIPID.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置BFD报文IPID的使能标记（SET-SFEBFDPKTIPID）_00601345.md`
