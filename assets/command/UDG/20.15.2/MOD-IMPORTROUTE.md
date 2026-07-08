---
id: UDG@20.15.2@MMLCommand@MOD IMPORTROUTE
type: MMLCommand
name: MOD IMPORTROUTE（修改指定协议中的入口路由配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: IMPORTROUTE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 入口路由
status: active
---

# MOD IMPORTROUTE（修改指定协议中的入口路由配置）

## 功能

该命令用于修改使用Import方式引入其他协议路由信息。

## 注意事项

- 该命令执行后立即生效。
- 需要确保指定的BGP VPN实例在设备上已创建。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定BGP VPN实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定BGP VPN实例下的地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv6uni：IPv6地址族。<br>默认值：无 |
| IMPORTPROTOCOL | 路由协议 | 可选必选说明：必选参数<br>参数含义：用户设定引入其他协议路由时的策略名称。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- direct：直连路由。<br>- ospf：开放式最短路径优先协议。<br>- static：静态路由。<br>- ospfv3：OSPFv3协议。<br>- wlr：WLR协议。<br>默认值：无<br>配置原则：配置ospf或ospfv3时，需指定IMPORTPROCESSID参数，其他协议，IMPORTPROCESSID无需填写。 |
| IMPORTPROCESSID | 路由进程号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IMPORTPROTOCOL”配置为“ospf” 或 “ospfv3”时为必选参数。<br>参数含义：该参数用于指定所引入路由的协议进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：IMPORTPROTOCOL参数配置为ospf和ospfv3时，需指定本参数，范围为1~4294967295，其他协议，本参数无需填写。 |
| IMPORTROUTEPOLICY | 引入路由策略 | 可选必选说明：可选参数<br>参数含义：用户设定引入其他协议路由时的策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 路由策略必须已经存在。使用ADD ROUTEPOLICY命令可配置路由策略。使用LST ROUTEPOLICY命令查看可用路由策略。 |
| MEDENABLE | 使能MED | 可选必选说明：可选参数<br>参数含义：该参数用于使能MED。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| MED | MED | 可选必选说明：条件必选参数<br>前提条件：该参数在“MEDENABLE”配置为“TRUE”时为必选参数。<br>参数含义：指定引入路由的MED值，BGP选路时，选择MED值较小的路由。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：根据实际业务配置合适的MED值。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IMPORTROUTE]] · 指定协议中的入口路由配置（IMPORTROUTE）

## 使用实例

在名称为“vrf1”的BGP VPN实例下修改引入静态路由的策略名称：

```
ADD IMPORTROUTE:VRFNAME="vrf1", AFTYPE=ipv4uni, IMPORTPROTOCOL=static;
ADD ROUTEPOLICY:POLICYNAME="PolicyABC";
MOD IMPORTROUTE:VRFNAME="vrf1", AFTYPE=ipv4uni, IMPORTPROTOCOL=static, IMPORTROUTEPOLICY="PolicyABC";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-IMPORTROUTE.md`
