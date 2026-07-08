---
id: UNC@20.15.2@MMLCommand@MOD SRBFDPARA6
type: MMLCommand
name: MOD SRBFDPARA6（修改IPv6 BFD模板）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SRBFDPARA6
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 静态路由管理
- 配置IPv6 BFD模板
status: active
---

# MOD SRBFDPARA6（修改IPv6 BFD模板）

## 功能

该命令用来修改IPv6 BFD模板。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFTYPE | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv6unicast：IPv6单播。<br>默认值：无<br>配置原则：默认IPv6单播。 |
| IFNAME | 接口名字 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由的传输接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～64。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 下一跳所在VPN为私网时，应输入Invalid0，共网段场景除外，不区分大小写。<br>- 请使用LST INTERFACE命令查看可用接口。 |
| NEXTHOP | 路由下一跳 | 可选必选说明：可选参数<br>参数含义：该参数用于指定下一跳地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| LOCALADDRESS | 本机地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本机地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：IPv6地址，当配置成::时，去配置恢复成默认值。 |
| DESTVRFNAME | 网关地址VPN | 可选必选说明：可选参数<br>参数含义：该参数用于指定网关地址所属VPN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 共网段场景下，下一跳所在VPN为私网时，请通过接口名配置。 |
| MINRXINTERVAL | 最小接收间隔（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于指定期望从对端接收IPv6 BFD报文的最小接收间隔。如果未指定，采用全局缺省值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为30～1000，单位是毫秒。<br>默认值：无<br>配置原则：<br>- 单位为毫秒。<br>- 缺省值为200毫秒。 |
| MINTXINTERVAL | 最小传输间隔（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于指定向对端发送IPv6 BFD报文的最小传输间隔。如果未指定，采用全局缺省值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为30～1000，单位是毫秒。<br>默认值：无<br>配置原则：<br>- 单位为毫秒。<br>- 缺省值为200毫秒。 |
| MULTIPLIER | 时间倍数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本地检测倍数。如果未指定，采用全局缺省值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为3～50。<br>默认值：无<br>配置原则：缺省值为3。 |
| DHCPENABLE | DHCP使能 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DHCP使能标志。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：接口下DHCP使能，BFD模板联动DHCP才能生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SRBFDPARA6]] · IPv6 BFD模板（SRBFDPARA6）

## 使用实例

修改IPv6 BFD模板：

```
MOD SRBFDPARA6:AFTYPE=ipv6unicast, NEXTHOP="2001:DB8::1",LOCALADDRESS="2001:DB8::2",DESTVRFNAME="_public_", IFNAME="ethernet64/0/5",MINTXINTERVAL=500;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改IPv6-BFD模板（MOD-SRBFDPARA6）_49801386.md`
