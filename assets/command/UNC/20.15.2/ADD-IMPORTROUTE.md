---
id: UNC@20.15.2@MMLCommand@ADD IMPORTROUTE
type: MMLCommand
name: ADD IMPORTROUTE（增加指定协议中的入口路由配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IMPORTROUTE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 100000
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 入口路由
status: active
---

# ADD IMPORTROUTE（增加指定协议中的入口路由配置）

## 功能

BGP协议自身不能发现路由，所以需要引入其他协议的路由（如IGP或者静态路由等）注入到BGP路由表中，从而将这些路由在AS之内和AS之间传播。

BGP引入路由时支持Import和Network两种方式：

Import方式是按协议类型，将OSPF路由、静态路由和直连路由等某一协议的路由注入到BGP路由表中。

Network方式比Import方式更精确，将指定前缀和掩码的一条路由注入到BGP路由表中。

该命令用于使用Import方式引入其他协议路由信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为100000。
- 需要确保指定的BGP VPN实例在设备上已创建。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定BGP VPN实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定BGP VPN实例下的地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv6uni：IPv6地址族。<br>默认值：无 |
| IMPORTPROTOCOL | 路由协议 | 可选必选说明：必选参数<br>参数含义：用户设定引入其他协议路由时的策略名称。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- direct：直连路由。<br>- ospf：开放式最短路径优先协议。<br>- static：静态路由。<br>- ospfv3：OSPFv3协议。<br>- wlr：WLR协议。<br>默认值：无<br>配置原则：配置ospf或ospfv3时，需指定IMPORTPROCESSID参数，其他协议，IMPORTPROCESSID无需填写。 |
| IMPORTPROCESSID | 路由进程号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IMPORTPROTOCOL”配置为“ospf” 或 “ospfv3”时为必选参数。<br>参数含义：该参数用于指定所引入路由的协议进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：IMPORTPROTOCOL参数配置为ospf和ospfv3时，需指定本参数，范围为1~4294967295，其他协议，本参数无需填写。 |
| IMPORTROUTEPOLICY | 引入路由策略 | 可选必选说明：可选参数<br>参数含义：用户设定引入其他协议路由时的策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：在此之前应使用ADD ROUTEPOLICY命令配置对应策略。使用LST ROUTEPOLICY命令查看可用路由策略。 |
| MEDENABLE | 使能MED | 可选必选说明：可选参数<br>参数含义：该参数用于使能MED。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：FALSE |
| MED | MED | 可选必选说明：条件必选参数<br>前提条件：该参数在“MEDENABLE”配置为“TRUE”时为必选参数。<br>参数含义：指定引入路由的MED值，BGP选路时，选择MED值较小的路由。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：0<br>配置原则：根据实际业务配置合适的MED值。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMPORTROUTE]] · 指定协议中的入口路由配置（IMPORTROUTE）

## 使用实例

在名称为“vrf1”的BGP VPN实例下增加引入静态路由：

```
SET BGP:ASNUM="100",BGPENABLE=TRUE;
ADD L3VPNINST:VRFNAME="vrf1";
ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
ADD BGPVRF:VRFNAME="vrf1";
ADD IMPORTROUTE:VRFNAME="vrf1", AFTYPE=ipv4uni, IMPORTPROTOCOL=static;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加指定协议中的入口路由配置（ADD-IMPORTROUTE）_49801554.md`
