---
id: UNC@20.15.2@ConfigObject@SBILINKSTATUS
type: ConfigObject
name: SBILINKSTATUS（服务化接口链路状态）
nf: UNC
version: 20.15.2
object_name: SBILINKSTATUS
object_kind: query_target
status: active
---

# SBILINKSTATUS（服务化接口链路状态）

## 说明

![](查询服务化接口链路状态（DSP SBILINKSTATUS）_29213281.assets/notice_3.0-zh-cn_2.png)

当链路数较多时，执行该命令会占用运维平台较长时间，进而导致用户无法继续使用该运维平台。对于业务负载较高的设备，建议查询时加上网元类型、链路状态、全局进程标识、POD名称等参数减少命令查询的链路数，避免对设备造成冲击影响业务。

该命令用于查询服务化接口的链路状态。可支持服务端和客户端链路查询。当系统角色为服务端时，可在系统中查询由客户端发起建立的链路的基本信息。当系统为客户端时，可在系统中查询由本端发起建立的链路的详细信息。

## 操作本对象的命令

- [DSP SBILINKSTATUS](command/UNC/20.15.2/DSP-SBILINKSTATUS.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询服务化接口链路状态（DSP-SBILINKSTATUS）_29213281.md`
