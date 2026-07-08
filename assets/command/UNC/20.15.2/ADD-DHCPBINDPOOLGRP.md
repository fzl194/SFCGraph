---
id: UNC@20.15.2@MMLCommand@ADD DHCPBINDPOOLGRP
type: MMLCommand
name: ADD DHCPBINDPOOLGRP（增加DHCP服务器组与地址池组绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DHCPBINDPOOLGRP
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
- DHCP服务器绑定
status: active
---

# ADD DHCPBINDPOOLGRP（增加DHCP服务器组与地址池组绑定关系）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于将DHCP服务器组与地址池组相关联。当需要UNC上激活DHCP服务器分配地址的用户时，使用该命令将UNC上配置的远端地址池组和DHCP服务器组相关联。

## 注意事项

- 该命令执行后立即生效。

- 每个远端地址池组最多可以绑定一个DHCP服务器组。一个DHCP服务器组可以被多个远端地址池组绑定。
- 使用该命令将远端地址池组和DHCP服务器组相关联前，必须使用ADD DHCPSERVER配置DHCP服务器。
- 如果要修改远端地址池组关联的DHCP服务器组，需要先执行RMV DHCPBINDPOOLGRP将原来关联的DHCP服务器组删除，然后执行该命令关联新的DHCP服务器组。

- 最多可输入6000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLGRPNAME | 地址池组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址池组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。不支持空格及特殊字符“_”、“#”、“$”和“&”等，由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRPOOLGRP命令配置生成。 |
| GROUPNAME | DHCP服务器组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DHCP服务器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD DHCPSERVERGRP命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DHCPBINDPOOLGRP]] · DHCP服务器组与地址池组绑定关系（DHCPBINDPOOLGRP）

## 使用实例

当需要UNC上激活DHCP服务器分配地址的用户时，使用该命令将UNC上配置的远端地址池组poolgrp1和DHCP服务器组group1相关联

```
ADD DHCPBINDPOOLGRP:POOLGRPNAME="poolgrp1",GROUPNAME="group1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-DHCPBINDPOOLGRP.md`
