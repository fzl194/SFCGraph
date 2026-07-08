---
id: UDG@20.15.2@MMLCommand@RMV IPSECINTFCFGIPSEC
type: MMLCommand
name: RMV IPSECINTFCFGIPSEC（删除IPsec隧道接口）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: IPSECINTFCFGIPSEC
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 互联网密钥交换
- IPsec接口配置
status: active
---

# RMV IPSECINTFCFGIPSEC（删除IPsec隧道接口）

## 功能

![](删除IPsec隧道接口（RMV IPSECINTFCFGIPSEC）_80592512.assets/notice_3.0-zh-cn.png)

删除IPSEC隧道，该条链路会直接断连，导致业务流量掉底。

该命令用于删除IPsec隧道。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTERFACENAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：配置接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：无 |
| TNLTYPE | Tunnel口协议类型 | 可选必选说明：必选参数<br>参数含义：Tunnel口协议类型。<br>数据来源：本端规划<br>取值范围：<br>- “IPSEC（IPv4IP安全）”：IPv4IP安全<br>- “IPSEC6（IPv6IP安全）”：IPv6IP安全<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [IPsec隧道接口（IPSECINTFCFGIPSEC）](configobject/UDG/20.15.2/IPSECINTFCFGIPSEC.md)

## 使用实例

删除接口名为“Tunnel1/1/1”，协议类型为“IPv4IP安全”的隧道：

```
RMV IPSECINTFCFGIPSEC:INTERFACENAME="Tunnel 1/1/1",TNLTYPE=IPSEC;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除IPsec隧道接口（RMV-IPSECINTFCFGIPSEC）_80592512.md`
