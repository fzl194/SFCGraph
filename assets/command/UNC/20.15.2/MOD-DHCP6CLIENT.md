---
id: UNC@20.15.2@MMLCommand@MOD DHCP6CLIENT
type: MMLCommand
name: MOD DHCP6CLIENT（修改DHCPv6客户端）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: DHCP6CLIENT
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- DHCP管理
- DHCPv6客户端配置
status: active
---

# MOD DHCP6CLIENT（修改DHCPv6客户端）

## 功能

该命令用于修改DHCPv6客户端属性。

## 注意事项

- 该命令执行后立即生效。
- 该命令在Ethernet接口上配置执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| ISDHCPV6CENABLE | DHCPv6客户端使能 | 可选必选说明：可选参数<br>参数含义：该参数用于标识DHCPv6客户端是否使能。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。TRUE表示使能，FALSE表示不使能。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DHCP6CLIENT]] · DHCPv6客户端（DHCP6CLIENT）

## 使用实例

修改DHCPv6客户端：

```
MOD DHCP6CLIENT: IFNAME="Ethernet64/0/4", ISDHCPV6CENABLE=FALSE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-DHCP6CLIENT.md`
