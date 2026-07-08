---
id: UDG@20.15.2@MMLCommand@RMV IPSQMSHAPING
type: MMLCommand
name: RMV IPSQMSHAPING（删除IPSQM整形配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: IPSQMSHAPING
command_category: 配置类
applicable_nf:
- SGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- IPSQM控制
- IPSQM Shaping配置
status: active
---

# RMV IPSQMSHAPING（删除IPSQM整形配置）

## 功能

**适用NF：SGW-U、UPF**

该命令用于删除基于基站的下行流量整形带宽。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP地址类型 | 可选必选说明：可选参数<br>参数含义：指定对端地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：表示地址类型为IPv4。<br>- IPv6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| PEERIPV4 | 对端IPv4地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPTYPE”配置为“IPv4”时为可选参数。<br>参数含义：指定基站的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无<br>配置原则：无 |
| PEERIPV6 | 对端IPv6地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPTYPE”配置为“IPv6”时为可选参数。<br>参数含义：指定基站的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| VPNINSTANCE | VPN实例 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPTYPE”配置为“IPv4” 或 “IPv6”时为可选参数。<br>参数含义：指定基站所在VPN，如果整形配置的VPN与实际的VPN不一致，则整形失败。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [IPSQM整形配置（IPSQMSHAPING）](configobject/UDG/20.15.2/IPSQMSHAPING.md)

## 使用实例

删除基于基站的下行流量整形带宽：

```
RMV IPSQMSHAPING: IPTYPE=IPv4, PEERIPV4="10.0.0.1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除IPSQM整形配置（RMV-IPSQMSHAPING）_21392218.md`
