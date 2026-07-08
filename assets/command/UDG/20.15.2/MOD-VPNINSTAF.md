---
id: UDG@20.15.2@MMLCommand@MOD VPNINSTAF
type: MMLCommand
name: MOD VPNINSTAF（修改L3VPN实例地址族）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: VPNINSTAF
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- VPN管理
- L3VPN管理
- L3VPN实例地址族
status: active
---

# MOD VPNINSTAF（修改L3VPN实例地址族）

## 功能

![](修改L3VPN实例地址族（MOD VPNINSTAF）_49961066.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致此VPN实例地址族下的配置和此VPN实例在BGP中的相关配置被删除，请谨慎使用并联系华为技术支持协助操作。

该命令用于修改设备上VPN实例下配置的地址族参数，例如修改VPN实例地址族下的路由标识符RD、应用策略等。

## 注意事项

- 该命令执行后立即生效。
- 该命令删除RD会导致此VPN实例地址族下的配置和此VPN实例在BGP中的相关配置被删除
- 配置该命令前，需要对应的VPN实例地址族已创建。
- 不能修改VPN实例__mpp_vpn_inner__、__mpp_vpn_inner_server__的配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定L3VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VPN实例下的地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv6uni：IPv6地址族。<br>默认值：无 |
| VRFRD | 路由标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户需要修改的路由标识符。在不同VPN使用相同网段的场景下，BGP服务可以根据VRFRD区分使用相同网段的不同VPN的路由。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为3～21。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 该参数配置后不支持直接修改，但是可以下发单空格，执行清空操作，再进行配置。VRFRD值唯一，取值范围是X.X.X.X:number<0-65535>、number<0-65535>:number<0-4294967295>、number<0-65535>.number<0-65535>:number<0-65535>或者number<65536-4294967295>:number<0-65535>，但不支持配置为0:0和0.0:0。 |
| IMPOLICYNAME | 引入路由策略名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由交叉入该VPN时的入口策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 路由策略必须已经存在。使用ADD ROUTEPOLICY命令可配置路由策略。使用LST ROUTEPOLICY命令查看可用路由策略。 |
| LOCALCROSSNHPMOD | 可更改本地交叉下一跳 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否使能本地交叉修改下一跳功能。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：该参数配置为“TRUE”时，需要同时配置IMPOLICYNAME参数。 |
| EXPOLICYNAME | 发布路由策略名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由发布时的出口策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 路由策略必须已经存在。使用ADD ROUTEPOLICY命令可配置路由策略。使用LST ROUTEPOLICY命令查看可用路由策略。 |
| EXPLYADDERTFIRST | 路由上送时首先添加ERT | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由上送时是否在过策略前添加ERT。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：<br>- 该参数配置时，需要配置EXPOLICYNAME参数。<br>- 当指定的路由策略中有对RT值进行匹配的条件时，需要配置此参数。 |
| VRFLABELMODE | 实例的标签分配模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例的标签分配模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- perRoute：每路由每标签。<br>- perInstance：每实例每标签。<br>- perInstanceStatic：每实例每静态标签。<br>默认值：无<br>配置原则：为了节省标签资源，必须配置为perInstance。 |
| VRFLABEL | 实例的标签值 | 可选必选说明：该参数在“VRFLABELMODE”配置为“perInstanceStatic”时为条件可选参数。<br>参数含义：该参数用于指定VPN实例的静态标签值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为16～32767。<br>默认值：无<br>配置原则：无 |
| TNLPOLICYNAME | 隧道策略名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定隧道策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～39。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 隧道策略必须已经存在。使用ADD TUNNELPOLICY命令可配置隧道策略。使用LST TUNNELPOLICY命令查看可用隧道策略。 |
| FRRENABLE | FRR使能 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否允许FRR使能。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：<br>- 只有配置了VRFRD才可配置FRRENABLE为TRUE。<br>- 配置FRR可以形成主备路由，提升路由收敛性能。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@VPNINSTAF]] · L3VPN实例地址族（VPNINSTAF）

## 关联任务

- [[UDG@20.15.2@Task@0-00145]]

## 使用实例

修改名称为“vrf1”的VPN实例下的IPv4单播地址族RD参数：

```
ADD L3VPNINST:VRFNAME="vrf1";
ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
MOD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni, VRFRD="1:1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-VPNINSTAF.md`
