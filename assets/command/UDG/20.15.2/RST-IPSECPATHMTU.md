---
id: UDG@20.15.2@MMLCommand@RST IPSECPATHMTU
type: MMLCommand
name: RST IPSECPATHMTU（复位IPsec Path MTU）
nf: UDG
version: 20.15.2
verb: RST
object_keyword: IPSECPATHMTU
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- 接口管理
- IPv6Mtu
status: active
---

# RST IPSECPATHMTU（复位IPsec Path MTU）

## 功能

该命令用于重置IPsec Path MTU值。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRCIP | 源IPv6地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询MTU对应的PATH的源隧道口IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| DSTIP | 目的IPv6地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询MTU对应的PATH的目的隧道口IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPSECPATHMTU]] · 复位IPsec Path MTU（IPSECPATHMTU）

## 使用实例

重置源地址为fc00:fc01::2，目的地址为fc00:fc01:132::120的ipsec链路mtu记录。

```
RST IPSECPATHMTU: SRCIP="fc00:fc01::2", DSTIP="fc00:fc01:132::120";
RETCODE = 0  操作成功
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RST-IPSECPATHMTU.md`
