---
id: UNC@20.15.2@ConfigObject@IPSTATISTIC
type: ConfigObject
name: IPSTATISTIC（IP报文统计）
nf: UNC
version: 20.15.2
object_name: IPSTATISTIC
object_kind: action
status: active
---

# IPSTATISTIC（IP报文统计）

## 说明

该命令用于查看IP报文统计信息。

通过该命令的显示信息可以查看包括接收报文（其中包括被丢弃的带源路由选项的报文）、发送报文、分片报文、重组报文的统计信息。

在传输报文的过程中，当源端对报文进行了分片，可以通过该命令查看分片成功的IP报文总数和发送的分片报文总数，然后再在目的端查看接收到的分片报文数是否正确。

通过DSP IPSTATISTIC命令可以用来查看IP流量统计详细信息，从而帮助用户定位到具体应用在报文收发过程中的丢包问题。

不指定参数时，查询所有接口的统计信息；当指定参数时，可以查询指定接口的统计信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-IPSTATISTIC]] · DSP IPSTATISTIC
- [[command/UNC/20.15.2/RTR-IPSTATISTIC]] · RTR IPSTATISTIC

## 证据

- 原始手册：`evidence/UNC/20.15.2/IPSTATISTIC.md`
- 原始手册：`evidence/UNC/20.15.2/IPSTATISTIC.md`
