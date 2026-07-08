---
id: UNC@20.15.2@MMLCommand@RMV DHCPCLIENT
type: MMLCommand
name: RMV DHCPCLIENT（删除DHCPv4客户端）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV DHCPCLIENT（删除DHCPv4客户端）

## 功能

该命令用于删除DHCPv4客户端。

## 注意事项

- 该命令执行后立即生效。
- 该命令在Ethernet接口上配置执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [DHCPv4客户端（DHCPCLIENT）](configobject/UNC/20.15.2/DHCPCLIENT.md)

## 使用实例

删除DHCPv4客户端：

```
RMV DHCPCLIENT: IFNAME="Ethernet64/0/4";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除DHCPv4客户端（RMV-DHCPCLIENT）_49801902.md`
