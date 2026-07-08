---
id: UNC@20.15.2@MMLCommand@RMV DHCPSERVER
type: MMLCommand
name: RMV DHCPSERVER（删除DHCP服务器）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DHCPSERVER
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- DHCP管理
- DHCP服务器
status: active
---

# RMV DHCPSERVER（删除DHCP服务器）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除DHCP服务器配置。

## 注意事项

- 该命令执行后立即生效。

- 不带任何可选参数表示删除该DHCP服务器组里的所有DHCP服务器配置。如果指定了DHCP服务器的ISPRIMARY参数，则根据指定的参数删除配置。
- 如果DHCP服务器组已经与远端地址池组绑定，则不允许删除DHCP服务器组的配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | DHCP服务器组名称 | 可选必选说明：必选参数<br>参数含义：该参数指定DHCP服务器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| ISPRIMARY | 是否是主DHCP服务器 | 可选必选说明：可选参数<br>参数含义：该参数指定是否为主DHCP服务器。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：<br>ENABLE指删除主服务器，DISABLE指删除备服务器。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DHCPSERVER]] · DHCP服务器（DHCPSERVER）

## 使用实例

当需要删除DHCP服务器组group1的主DHCP服务器，使用该命令：

```
RMV DHCPSERVER:GROUPNAME="group1",ISPRIMARY=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除DHCP服务器（RMV-DHCPSERVER）_32102617.md`
