---
id: UDG@20.15.2@MMLCommand@MOD DHCPCLIENT
type: MMLCommand
name: MOD DHCPCLIENT（修改DHCPv4客户端）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: DHCPCLIENT
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- DHCP管理
- DHCP客户端配置
status: active
---

# MOD DHCPCLIENT（修改DHCPv4客户端）

## 功能

该命令用于修改DHCPv4客户端属性。如：期望租期、上报MTU使能。

## 注意事项

- 该命令执行后立即生效。
- 该命令在Ethernet接口上配置执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| ISDHCPV4CENABLE | DHCPv4客户端使能 | 可选必选说明：可选参数<br>参数含义：该参数用于标识DHCPv4客户端是否使能。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。TRUE表示使能，FALSE表示不使能。<br>默认值：无 |
| EXPECTLEASE | 期望租期（秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定DHCPv4客户端期望租期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0，60～864000，单位是秒。<br>默认值：无 |
| MTUENABLE | 上报MTU使能 | 可选必选说明：可选参数<br>参数含义：该参数用于标识DHCP客户端是否使能上报mtu功能。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。TRUE表示使能，FALSE表示不使能。<br>默认值：无<br>配置原则：该缺省值为FALSE，DHCPv4客户端不再向接口上报从DHCP服务器获取到的MTU，并删除已上报过的MTU值。如果配置为TRUE，DHCPv4客户端会通过重新申请地址获取DHCPv4服务器最新配置的MTU值，并上报给接口。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DHCPCLIENT]] · DHCPv4客户端（DHCPCLIENT）

## 使用实例

修改DHCPv4客户端：

```
MOD DHCPCLIENT: IFNAME="Ethernet64/0/4", ISDHCPV4CENABLE=TRUE, EXPECTLEASE=60, MTUENABLE=TRUE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-DHCPCLIENT.md`
