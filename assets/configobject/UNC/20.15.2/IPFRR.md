---
id: UNC@20.15.2@ConfigObject@IPFRR
type: ConfigObject
name: IPFRR（IP FRR）
nf: UNC
version: 20.15.2
object_name: IPFRR
object_kind: global_setting
status: active
---

# IPFRR（IP FRR）

## 说明

该命令用来使能IP FRR功能。

在设备上存在多种路由协议生成的路由时，如果想在部分路由故障后能够快速切换以使报文转发顺畅，可以通过配置此命令使能协议路由间的IP FRR功能。

例如，在设备上存在OSPF协议生成的一条目的地址为10.1.1.1的OSPF路由，优先级为15。同时再配置一条到目的地址10.1.1.1的静态路由，优先级为60。在未使能IP FRR的情况下，优选OSPF路由。在使能IP FRR后，会生成一条新的路由，OSPF路由作为主路由，静态路由作为备份路由。这样，在OSPF路由故障时，系统可以快速切换到静态路由，保证转发畅通。

## 操作本对象的命令

- [LST IPFRR](command/UNC/20.15.2/LST-IPFRR.md)
- [SET IPFRR](command/UNC/20.15.2/SET-IPFRR.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IP-FRR（LST-IPFRR）_49960910.md`
- 原始手册：`evidence/UNC/20.15.2/设置IP-FRR（SET-IPFRR）_00841149.md`
