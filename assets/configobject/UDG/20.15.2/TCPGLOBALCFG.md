---
id: UDG@20.15.2@ConfigObject@TCPGLOBALCFG
type: ConfigObject
name: TCPGLOBALCFG（TCP全局配置）
nf: UDG
version: 20.15.2
object_name: TCPGLOBALCFG
object_kind: global_setting
status: active
---

# TCPGLOBALCFG（TCP全局配置）

## 说明

该命令用来设置TCP相关的全局配置。

以下参数说明IPv4和IPv6共用：

设置TCP FIN-Wait超时时间：当TCP的连接状态由FIN_WAIT_1变为FIN_WAIT_2时启动FIN-Wait定时器。若FIN-Wait定时器超时前仍未收到FIN报文，则TCP连接被终止。

设置TCP SYN-Wait超时时间：当发送SYN报文时，TCP启动SYN-Wait定时器，若SYN-Wait超时前未收到回应报文，则TCP连接将被终止。

设置TCP连接的MSS最大值大小：TCP在建立连接时，会协商MSS值(Maximum Segment Size)，它表示本端所能接收报文（TCP报文的静荷，不包含TCP头）的最大长度。

设置面向连接Socket的窗口值：该配置会变更TCP默认缓冲区窗口大小，当TCP连接建立时会使用这个设置的缓冲区值协商建立TCP会话。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-TCPGLOBALCFG]] · LST TCPGLOBALCFG
- [[command/UDG/20.15.2/SET-TCPGLOBALCFG]] · SET TCPGLOBALCFG

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询TCP全局配置（LST-TCPGLOBALCFG）_00601361.md`
- 原始手册：`evidence/UDG/20.15.2/设置TCP全局配置（SET-TCPGLOBALCFG）_00440885.md`
