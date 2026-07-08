---
id: UNC@20.15.2@MMLCommand@MOD NETWORKROUTE
type: MMLCommand
name: MOD NETWORKROUTE（修改引入路由指定前缀和掩码长度）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NETWORKROUTE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 引入路由指定前缀和掩码长度
status: active
---

# MOD NETWORKROUTE（修改引入路由指定前缀和掩码长度）

## 功能

该命令用于修改使用Network方式引入BGP外部路由。

## 注意事项

- 该命令执行后立即生效。
- 需要确保指定的BGP VPN实例在设备上已创建。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户增加引入network路由的BGP VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定BGP VPN实例下的地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv6uni：IPv6地址族。<br>默认值：无 |
| NETWORKADDRESS | IPv4路由前缀地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni”时为必选参数。<br>参数含义：该参数用于指定引入IPv4路由的前缀信息。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：配置该参数时，需要同时配置MASKLEN指定路由的掩码长度。 |
| MASKLEN | IPv4掩码长度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni”时为必选参数。<br>参数含义：该参数用于指定引入外部IPv4路由的掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32。<br>默认值：无<br>配置原则：配置NETWORKADDRESS参数时，需要配置本参数指定引入路由的掩码长度，AFTYPE参数为ipv4uni时，掩码长度范围为0~32。 |
| NETWORKADDRESSV6 | IPv6路由前缀地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv6uni”时为必选参数。<br>参数含义：该参数用于指定引入IPv6路由的前缀信息。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：配置该参数时，需要同时配置MASKLENV6指定路由的前缀长度。 |
| MASKLENV6 | IPv6掩码长度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv6uni”时为必选参数。<br>参数含义：该参数用于指定引入外部IPv6路由的前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无<br>配置原则：配置NETWORKADDRESSV6参数时，需要配置本参数指定引入路由的前缀长度，前缀长度范围为0~128。 |
| NETWORKPOLICY | 策略名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：用户设定引入其他协议路由时的策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 路由策略必须已经存在。使用ADD ROUTEPOLICY命令可配置路由策略。使用LST ROUTEPOLICY命令查看可用路由策略。 |

## 操作的配置对象

- [引入路由指定前缀和掩码长度（NETWORKROUTE）](configobject/UNC/20.15.2/NETWORKROUTE.md)

## 使用实例

- 修改在名称为“vrf1”的BGP VPN实例下引入192.168.2.0/24外部路由时的路由策略：
  ```
  ADD NETWORKROUTE:VRFNAME="vrf1", AFTYPE=ipv4uni,NETWORKADDRESS="192.168.2.0",MASKLEN=24;
  MOD NETWORKROUTE:VRFNAME="vrf1", AFTYPE=ipv4uni,NETWORKADDRESS="192.168.2.0",MASKLEN=24,NETWORKPOLICY="PolicyABC";
  ```
- 修改在名称为“vrf1”的BGP VPN实例下引入2001:db8:1:1:1:1:1:1/32外部路由时的路由策略：
  ```
  ADD NETWORKROUTE:VRFNAME="vrf1", AFTYPE=ipv6uni,NETWORKADDRESSV6="2001:db8:1:1:1:1:1:1",MASKLENV6=32;
  MOD NETWORKROUTE:VRFNAME="vrf1", AFTYPE=ipv6uni,NETWORKADDRESSV6="2001:db8:1:1:1:1:1:1",MASKLENV6=32,NETWORKPOLICY="PolicyABC";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改引入路由指定前缀和掩码长度（MOD-NETWORKROUTE）_50121266.md`
