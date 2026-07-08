---
id: UDG@20.15.2@MMLCommand@RTR DHCP6CLIENTSTC
type: MMLCommand
name: RTR DHCP6CLIENTSTC（清除DHCPv6客户端报文统计）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: DHCP6CLIENTSTC
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- DHCP管理
- DHCPv6客户端报文统计
status: active
---

# RTR DHCP6CLIENTSTC（清除DHCPv6客户端报文统计）

## 功能

该命令用于清除DHCPv6客户端报文统计计数。

## 注意事项

- 该命令执行后立即生效。
- 该命令在Ethernet接口上配置执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定清除计数的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [DHCPv6客户端报文统计（DHCP6CLIENTSTC）](configobject/UDG/20.15.2/DHCP6CLIENTSTC.md)

## 使用实例

清除DHCPv6客户端报文统计信息：

```
RTR DHCP6CLIENTSTC: IFNAME="Ethernet64/0/4";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/清除DHCPv6客户端报文统计（RTR-DHCP6CLIENTSTC）_49801542.md`
