---
id: UDG@20.15.2@MMLCommand@RMV AGGREGATEROUTE
type: MMLCommand
name: RMV AGGREGATEROUTE（删除BGP聚合路由）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: AGGREGATEROUTE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- BGP聚合路由
status: active
---

# RMV AGGREGATEROUTE（删除BGP聚合路由）

## 功能

该命令用于删除聚合IPv4或IPv6路由。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VRF的地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv6uni：IPv6地址族。<br>默认值：无 |
| AGGREADDRESS | IPv4聚合地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni”时为必选参数。<br>参数含义：该参数用于指定IPv4聚合路由的地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：配置该参数时，需要同时配置MASKLENGTH指定聚合路由的掩码长度。 |
| MASKLENGTH | IPv4地址掩码长度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni”时为必选参数。<br>参数含义：该参数用于指定IPv4聚合路由的掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32。<br>默认值：无<br>配置原则：配置AGGREADDRESS参数时，需要配置本参数指定聚合路由的掩码长度，掩码长度范围为0~32。 |
| AGGREADDRESSV6 | IPv6聚合地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv6uni”时为必选参数。<br>参数含义：该参数用于指定IPv6聚合路由的地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：配置该参数时，需要同时配置MASKLENGTHV6指定路由的前缀长度。 |
| MASKLENGTHV6 | IPv6地址掩码长度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv6uni”时为必选参数。<br>参数含义：该参数用于指定IPv6聚合路由的前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无<br>配置原则：配置AGGREADDRESSV6参数时，需要配置本参数指定引入路由的前缀长度，前缀长度范围为0~128。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/AGGREGATEROUTE]] · BGP聚合路由（AGGREGATEROUTE）

## 使用实例

- 在名称为"vrf1"的BGP VPN实例下删除IPv4聚合路由：
  ```
  RMV AGGREGATEROUTE:VRFNAME="vrf1",AFTYPE=ipv4uni,AGGREADDRESS="10.2.2.2",MASKLENGTH=32;
  ```
- 在名称为"vrf1"的BGP VPN实例下删除IPv6聚合路由：
  ```
  RMV AGGREGATEROUTE:VRFNAME="vrf1",AFTYPE=ipv6uni,AGGREADDRESSV6="2001:db8:1:1:1:1:1:1",MASKLENGTHV6=32;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-AGGREGATEROUTE.md`
