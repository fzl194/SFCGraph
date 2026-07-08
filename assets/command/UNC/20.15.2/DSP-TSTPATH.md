---
id: UNC@20.15.2@MMLCommand@DSP TSTPATH
type: MMLCommand
name: DSP TSTPATH（显示UPC到UPF或者PFCP到UPF的路径状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: TSTPATH
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UPC链路告警
status: active
---

# DSP TSTPATH（显示UPC到UPF或者PFCP到UPF的路径状态）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于检测UPC到UPF或者PFCP到UPF的链路状态。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP类型 | 可选必选说明：必选参数<br>参数含义：该参数用于标识逻辑接口支持的IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPv4（IPv4）<br>- IPv6（IPv6）<br>默认值：无<br>配置原则：无 |
| LOCALIP | 本端地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv4"时为条件必选参数。<br>参数含义：该地址标识本端IPV4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| LOCALIPV6 | IPV6本端地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv6"时为条件必选参数。<br>参数含义：该地址标识本端IPV6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| PEERIP | 对端地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv4"时为条件可选参数。<br>参数含义：该地址标识对端IPV4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| PEERIPV6 | IPV6对端地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv6"时为条件可选参数。<br>参数含义：该地址标识对端IPV6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| LOCALPORT | 本端端口 | 可选必选说明：必选参数<br>参数含义：该地址标识本端端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：无<br>配置原则：无 |
| PEERPORT | 对端端口 | 可选必选说明：可选参数<br>参数含义：该地址标识对端端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：无<br>配置原则：无 |
| PATTERN | TSTPATH命令模式 | 可选必选说明：必选参数<br>参数含义：该参数用于标识TSTPATH命令模式。<br>数据来源：本端规划<br>取值范围：<br>- “Statistics（统计模式）”：统计模式<br>- “Detection（检测模式）”：检测模式<br>默认值：无<br>配置原则：无 |
| TARGET | 目标网元 | 可选必选说明：必选参数<br>参数含义：该参数用于标识目标网元，当前版本不支持参数UPC。<br>数据来源：本端规划<br>取值范围：<br>- “Upc（upc）”：upc<br>- “Pfcp（pfcp）”：pfcp<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [UPC到UPF或者PFCP到UPF的路径状态（TSTPATH）](configobject/UNC/20.15.2/TSTPATH.md)

## 使用实例

查询本端IP为192.168.1.1，对端IP为192.168.1.2，本端端口为8805，对端端口为8806的路径状态。

```
DSP TSTPATH:IPVERSION=IPv4,LOCALIP="192.168.1.1", PEERIP="192.168.1.2", LOCALPORT=8805, PEERPORT=8806,PATTERN=Detection,TARGET=Pfcp;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示UPC到UPF或者PFCP到UPF的路径状态（DSP-TSTPATH）_12701645.md`
