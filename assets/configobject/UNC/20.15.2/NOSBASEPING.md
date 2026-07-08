---
id: UNC@20.15.2@ConfigObject@NOSBASEPING
type: ConfigObject
name: NOSBASEPING（NOS Base平面网络Ping功能）
nf: UNC
version: 20.15.2
object_name: NOSBASEPING
object_kind: action
status: active
---

# NOSBASEPING（NOS Base平面网络Ping功能）

## 说明

该命令用于诊断不同节点间网络通断。PING是最常见的用于检测网络设备可访问性的调试工具，它使用ICMP报文来检测远程设备是否可用、远程主机通信的来回旅程的延迟以及包的丢失情况。

应用场景包括：

- 第一种场景：云设备内部，检测VNFC和VNFP的连通性。
- 第二种场景：设备的转发面，检测与其他配置IP业务设备的连通性。

## 操作本对象的命令

- [[command/UNC/20.15.2/ACT-NOSBASEPING]] · ACT NOSBASEPING

## 证据

- 原始手册：`evidence/UNC/20.15.2/NOSBASEPING.md`
