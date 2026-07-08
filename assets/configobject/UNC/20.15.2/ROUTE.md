---
id: UNC@20.15.2@ConfigObject@ROUTE
type: ConfigObject
name: ROUTE（IPv4路由表）
nf: UNC
version: 20.15.2
object_name: ROUTE
object_kind: query_target
status: active
---

# ROUTE（IPv4路由表）

## 说明

该命令用于显示IPv4路由表，默认显示公网路由和所有VPN路由。

路由表是设备转发数据包的关键，路由表中保存了各种路由协议发现的路由，根据来源不同，路由表中的路由通常可以分为链路层协议发现的路由即直连路由、由网络管理员手工配置的静态路由，以及动态路由协议发现的路由。

在路由数目较多时，该命令执行时间较长，且最多查询20万条路由。

## 操作本对象的命令

- [DSP ROUTE](command/UNC/20.15.2/DSP-ROUTE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示IPv4路由表（DSP-ROUTE）_00441129.md`
