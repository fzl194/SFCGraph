---
id: UNC@20.15.2@MMLCommand@RMV DHCPSERVERGRP
type: MMLCommand
name: RMV DHCPSERVERGRP（删除DHCP服务器组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DHCPSERVERGRP
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
- DHCP服务器组
status: active
---

# RMV DHCPSERVERGRP（删除DHCP服务器组）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除DHCP服务器组，以及服务器组下的DHCP服务器IP配置。

## 注意事项

- 该命令执行后立即生效。

- 如果DHCP服务器组已经与远端地址池组绑定，要删除DHCP服务器组时，必须先使用RMV DHCPBINDPOOLGRP命令解除和远端地址池组的关联。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | DHCP服务器组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DHCP服务器组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DHCPSERVERGRP]] · DHCP服务器组（DHCPSERVERGRP）

## 使用实例

当需要删除一个名称为“testgrp”的DHCP服务器组时，使用该命令：

```
RMV DHCPSERVERGRP:GROUPNAME="testgrp";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除DHCP服务器组（RMV-DHCPSERVERGRP）_86824472.md`
