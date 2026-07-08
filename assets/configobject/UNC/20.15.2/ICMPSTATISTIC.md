---
id: UNC@20.15.2@ConfigObject@ICMPSTATISTIC
type: ConfigObject
name: ICMPSTATISTIC（ICMP报文统计）
nf: UNC
version: 20.15.2
object_name: ICMPSTATISTIC
object_kind: query_target
status: active
---

# ICMPSTATISTIC（ICMP报文统计）

## 说明

该命令用于查看ICMP报文统计信息。统计值可以通过RTR IPSTATISTIC命令清除。

ICMP（Internet Control Message Protocol）是一个差错报告机制，通常被IP层或更高层协议（TCP或UDP）使用。ICMP报文被封装在IP数据报内部，作为IP数据报的数据部分通过互联网传递。

当数据报产生差错时，ICMP只向数据报的源端报告这个差错，即不会去纠正这个差错也不会通知中间的网络设备。

通过查看DSP ICMPSTATISTIC命令的显示信息，可以查看到接收和发送的ICMP错误报文、echo报文和echo reply报文的统计信息。

例如在进行Ping和Trace-route操作时，可以通过在路由设备上查看DSP ICMPSTATISTIC命令的显示信息，判断本设备发送和接收的报文总数是否正确。

不指定参数时，查询所有接口的统计信息；当指定参数时，可以查询指定接口的统计信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-ICMPSTATISTIC]] · DSP ICMPSTATISTIC

## 证据

- 原始手册：`evidence/UNC/20.15.2/ICMPSTATISTIC.md`
