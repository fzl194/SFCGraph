---
id: UDG@20.15.2@MMLCommand@DSP IPSECPATHMTU
type: MMLCommand
name: DSP IPSECPATHMTU（显示IPsec Path MTU）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: IPSECPATHMTU
command_category: 查询类
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

# DSP IPSECPATHMTU（显示IPsec Path MTU）

## 功能

该命令用于显示IPsec Path MTU值。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRCIP | 源IPv6地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询MTU对应的PATH的源隧道口IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| DSTIP | 目的IPv6地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询MTU对应的PATH的目的隧道口IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [复位IPsec Path MTU（IPSECPATHMTU）](configobject/UDG/20.15.2/IPSECPATHMTU.md)

## 使用实例

显示源地址为fc00:fc01::2，目的地址为fc00:fc01:132::120的链路mtu记录。

```
DSP IPSECPATHMTU: SRCIP="fc00:fc01::2", DSTIP="fc00:fc01:132::120";
RETCODE = 0  操作成功.

结果如下
------------------------
路径MTU  =  1500
 (结果个数 = 1) 
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示IPsec-Path-MTU（DSP-IPSECPATHMTU）_34023363.md`
