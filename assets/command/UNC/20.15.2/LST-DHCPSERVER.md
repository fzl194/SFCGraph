---
id: UNC@20.15.2@MMLCommand@LST DHCPSERVER
type: MMLCommand
name: LST DHCPSERVER（查询DHCP服务器）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DHCPSERVER
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
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

# LST DHCPSERVER（查询DHCP服务器）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询DHCP服务器信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | DHCP服务器组名称 | 可选必选说明：可选参数<br>参数含义：该参数指定DHCP服务器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD DHCPSERVERGRP命令配置生成。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DHCPSERVER]] · DHCP服务器（DHCPSERVER）

## 使用实例

当需要查看DHCP服务器组group1的DHCP服务器信息时，使用该命令：

```
%%LST DHCPSERVER:GROUPNAME="group1";%%
RETCODE = 0  操作成功

结果如下
--------
  DHCP服务器组名称  =  group1
是否是主DHCP服务器  =  使能
        IP地址类型  =  IPV4
DHCPv4服务器IP地址  =  10.1.1.1
DHCPv6服务器IP地址  =  ::
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DHCPSERVER.md`
