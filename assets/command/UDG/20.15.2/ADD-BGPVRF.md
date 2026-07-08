---
id: UDG@20.15.2@MMLCommand@ADD BGPVRF
type: MMLCommand
name: ADD BGPVRF（增加BGP VPN实例）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: BGPVRF
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 8192
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- BGP VPN实例
status: active
---

# ADD BGPVRF（增加BGP VPN实例）

## 功能

该命令用于创建BGP VPN实例。

如果BGP需要对私网路由进行引入等操作，则需先创建对应的BGP VPN实例。公网VPN实例在使能BGP时会默认创建。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为8192。
- 需对应的L3VPN实例已创建，才能够创建BGP VPN实例。
- 当该VPN地址族指定RD时，执行RMV BGPVRFAF会关联删除该BGP VPN实例。如需恢复该BGP VPN地址族，不需要添加BGP VPN实例，直接执行ADD BGPVRFAF增加该BGP VPN地址族。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定BGP VPN实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| DEFAULTAFTYPE | 默认地址族 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该VPN默认的地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- noaf：不创建VPN默认的地址族类型。<br>- ipv4uni：IPv4地址族。<br>- ipv6uni：IPv6地址族。<br>默认值：ipv4uni<br>配置原则：该参数不可修改。如果不配置，则缺省创建ipv4uni地址族。如果配置，则创建指定地址族。如果同一个私网VPN实例要创建多个地址族，请使用ADD BGPVRFAF命令。当该参数配置为noaf时，VRFNAME不能为_public_。 |
| ROUTERID | 路由器ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定BGP VPN实例的路由器ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。IPv4地址格式，但不允许输入0.0.0.0或255.255.255.255。<br>默认值：无<br>配置原则：ROUTERID和VRFRIDAUTOSEL的配置相互覆盖，且二者不可同时配置。 |
| VRFRIDAUTOSEL | VPN路由器ID自动选择 | 可选必选说明：可选参数<br>参数含义：该参数指定是否设置VPN实例自动选择Router ID。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE<br>配置原则：VRFRIDAUTOSEL只对私网起作用，公网下配置不起作用，ROUTERID和VRFRIDAUTOSEL的配置相互覆盖，且二者不可同时配置。只有当同一个私网VPN实例下存在IPv4接口地址时，VRFRIDAUTOSEL才能起作用。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@BGPVRF]] · BGP VPN实例（BGPVRF）

## 使用实例

新建名称为“vrf1”的BGP VPN实例：

```
SET BGP:ASNUM="100",BGPENABLE=TRUE;
ADD L3VPNINST:VRFNAME="vrf1";
ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
ADD BGPVRF:VRFNAME="vrf1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-BGPVRF.md`
