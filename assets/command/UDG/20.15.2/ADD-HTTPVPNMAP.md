---
id: UDG@20.15.2@MMLCommand@ADD HTTPVPNMAP
type: MMLCommand
name: ADD HTTPVPNMAP（增加HTTP VPN映射关系）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: HTTPVPNMAP
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP VPN映射管理
status: active
---

# ADD HTTPVPNMAP（增加HTTP VPN映射关系）

## 功能

该命令用于增加HTTP对端地址与本端VPN的映射关系。当使用多VPN组网，基于对端地址选择本端VPN和IP地址时，需要使用该命令配置对端地址与本端VPN的映射关系。

> **说明**
> - 该命令执行后立即生效。
>
> - 最多可输入512条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HTTP VPN映射的索引信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~512。<br>默认值：无<br>配置原则：无 |
| PEERADDRESSTYPE | 对端地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端地址类型。<br>数据来源：本端规划<br>取值范围：<br>- “IPv4（IPv4地址）”：IPv4地址<br>- “IPv6（IPv6地址）”：IPv6地址<br>默认值：无<br>配置原则：无 |
| IPV4 | IPv4地址 | 可选必选说明：该参数在"PEERADDRESSTYPE"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定对端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV4MASK | IPv4掩码 | 可选必选说明：该参数在"PEERADDRESSTYPE"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定对端IPv4掩码。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6 | IPv6地址 | 可选必选说明：该参数在"PEERADDRESSTYPE"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定对端IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6PREFIX | IPv6地址前缀长度 | 可选必选说明：该参数在"PEERADDRESSTYPE"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定对端IPv6地址前缀长度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |
| VPNNAME | VPN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VPN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。<br>默认值：无<br>配置原则：无 |
| DESCRIPTION | 配置描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HTTP VPN映射配置描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@HTTPVPNMAP]] · HTTP VPN映射关系（HTTPVPNMAP）

## 使用实例

若运营商要配置一条HTTP VPN映射，索引为1，对端地址类型为IPv4，地址为192.168.0.0，掩码为255.255.0.0，VPN名称为“VPN1”,可以用如下命令

```
ADD HTTPVPNMAP: INDEX=1, PEERADDRESSTYPE=IPv4, IPV4="192.168.0.0", IPV4MASK="255.255.0.0", VPNNAME="VPN1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-HTTPVPNMAP.md`
