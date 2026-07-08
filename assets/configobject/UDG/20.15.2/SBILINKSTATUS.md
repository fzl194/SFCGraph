---
id: UDG@20.15.2@ConfigObject@SBILINKSTATUS
type: ConfigObject
name: SBILINKSTATUS（服务化接口链路状态）
nf: UDG
version: 20.15.2
object_name: SBILINKSTATUS
object_kind: query_target
status: active
---

# SBILINKSTATUS（服务化接口链路状态）

## 说明

![](查询服务化接口链路状态（DSP SBILINKSTATUS）_29213281.assets/notice_3.0-zh-cn.png)

当链路数较多时，执行该命令会占用运维平台较长时间，进而导致用户无法继续使用该运维平台。对于业务负载较高的设备，建议查询时加上网元类型、链路状态、全局进程标识、POD名称等参数减少命令查询的链路数，避免对设备造成冲击影响业务。

该命令用于查询服务化接口的链路状态。可支持服务端和客户端链路查询。当系统角色为服务端时，可在系统中查询由客户端发起建立的链路的基本信息。当系统为客户端时，可在系统中查询由本端发起建立的链路的详细信息。

> **说明**
> - 如果是客户端链路，本命令会显示该链路所属的链路集标识，此信息可用于[**DSP SBILINKSET**](../服务化接口链路集管理/显示服务化接口链路集信息（DSP SBILINKSET）_84132098.md)命令基于该链路集标识查询对应的链路集信息。
> - 如果是服务端链路，链路集标识显示为空，服务端链路不做链路集管理。
> - 当输入链路ID查询链路详细信息时必须同时输入链路集ID。
> - 该命令执行之后，会查询满足输入参数条件的所有链路。在链路数比较多的情况下，查询客户端或服务端的全部链路会有一定的资源消耗。
> - 当[**DSP HTTPPROCESS**](../../HTTP管理/HTTP进程状态管理/显示HTTP进程信息（DSP HTTPPROCESS）_29053327.md)命令查询的CPU结果超过95%时，可能无法查询到所有的客户端链路。

## 操作本对象的命令

- [[command/UDG/20.15.2/DSP-SBILINKSTATUS]] · DSP SBILINKSTATUS

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询服务化接口链路状态（DSP-SBILINKSTATUS）_29213281.md`
