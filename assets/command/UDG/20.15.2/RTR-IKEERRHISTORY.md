---
id: UDG@20.15.2@MMLCommand@RTR IKEERRHISTORY
type: MMLCommand
name: RTR IKEERRHISTORY（恢复IKE历史信息清空状态）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: IKEERRHISTORY
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- 操作维护
- 系统调测
- IPsec调测
- IKE历史信息
status: active
---

# RTR IKEERRHISTORY（恢复IKE历史信息清空状态）

## 功能

该命令用于清除IKE历史信息。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | Pod名称 | 可选必选说明：可选参数<br>参数含义：Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：无 |
| ADDRTYPE | 地址类型 | 可选必选说明：可选参数<br>参数含义：对端地址类型。<br>数据来源：对端协商<br>取值范围：<br>- IPV4（IPv4地址）<br>- IPV6（IPv6地址）<br>默认值：无<br>配置原则：无 |
| PEERIP | 对端IPv4地址 | 可选必选说明：该参数在"ADDRTYPE"配置为"IPV4"时为条件可选参数。<br>参数含义：对端IPv4地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| PEERIP6 | 对端IPv6地址 | 可选必选说明：该参数在"ADDRTYPE"配置为"IPV6"时为条件可选参数。<br>参数含义：对端IPv6地址。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| VRFNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：VRF名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。<br>默认值：无<br>配置原则：无 |
| PORTNUM | 端口号 | 可选必选说明：可选参数<br>参数含义：端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IKEERRHISTORY]] · IKE历史信息清空状态（IKEERRHISTORY）

## 使用实例

清除IKE历史信息

```
RTR IKEERRHISTORY:ADDRTYPE=IPV4;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RTR-IKEERRHISTORY.md`
