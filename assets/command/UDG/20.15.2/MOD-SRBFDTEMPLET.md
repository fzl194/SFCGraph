---
id: UDG@20.15.2@MMLCommand@MOD SRBFDTEMPLET
type: MMLCommand
name: MOD SRBFDTEMPLET（修改BFD模板）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: SRBFDTEMPLET
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 静态路由管理
- 配置BFD模板
status: active
---

# MOD SRBFDTEMPLET（修改BFD模板）

## 功能

该命令用于修改BFD模板。

## 注意事项

- 该命令执行后立即生效。
- 修改该BFD模板时，要保证该模板添加过。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFTYPE | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无<br>配置原则：不配置此参数时，默认IPv4单播。 |
| NEXTHOP | 路由下一跳 | 可选必选说明：可选参数<br>参数含义：该参数用于指定下一跳地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：IPv4地址。 |
| LOCALADDRESS | 本机地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本机地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：IPv4地址，配置成0.0.0.0时，去配置恢复成默认值。 |
| DESTVRFNAME | 网关地址VPN | 可选必选说明：可选参数<br>参数含义：该参数用于指定网关地址所属VPN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：共网段场景下，下一跳所在VPN为私网时，请通过接口名配置。 |
| IFNAME | 接口名字 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由的传输接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 下一跳所在VPN为私网时，应输入Invalid0，共网段场景除外，不区分大小写。<br>- 请使用LST INTERFACE命令查看可用接口。 |
| MINRXINTERVAL | 最小接收间隔（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于指定期望从对端接收IPv4 BFD报文的最小接收间隔。如果未指定，采用全局缺省值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为30～1000，单位是毫秒。<br>默认值：无<br>配置原则：<br>- 单位为毫秒。<br>- 缺省值为200毫秒。 |
| MINTXINTERVAL | 最小传输间隔（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于指定向对端发送IPv4 BFD报文的最小传输间隔。如果未指定，采用全局缺省值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为30～1000，单位是毫秒。<br>默认值：无<br>配置原则：<br>- 单位为毫秒。<br>- 缺省值为200毫秒。 |
| MULTIPLIER | 时间倍数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本地检测倍数。如果未指定，采用全局缺省值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为3～50。<br>默认值：无<br>配置原则：缺省值为3。 |
| DHCPENABLE | DHCP使能 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DHCP使能标志。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：接口下DHCP使能，BFD模板联动DHCP才能生效。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SRBFDTEMPLET]] · BFD模板（SRBFDTEMPLET）

## 使用实例

修改一个BFD模板，网关地址为10.1.1.1，修改检测倍数为10：

```
MOD SRBFDTEMPLET: NEXTHOP="10.1.1.1",LOCALADDRESS="10.1.1.2",AFTYPE=ipv4unicast, MULTIPLIER=10,DESTVRFNAME="_public_", IFNAME="ethernet64/0/5";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改BFD模板（MOD-SRBFDTEMPLET）_00440993.md`
