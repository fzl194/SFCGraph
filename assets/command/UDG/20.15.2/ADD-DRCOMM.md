---
id: UDG@20.15.2@MMLCommand@ADD DRCOMM
type: MMLCommand
name: ADD DRCOMM（增加容灾实例地址）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: DRCOMM
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 容灾管理
status: active
---

# ADD DRCOMM（增加容灾实例地址）

## 功能

该命令用于配置本端或者对端容灾实例地址信息。

## 注意事项

- 该命令必须在本端容灾实例信息配置完成之后执行。

- 一个网元最多只允许配置两条容灾实例地址信息，本端和对端各一条。
- 执行该命令后，三分钟内请勿使用**[RMV DRCOMM](删除容灾实例地址(RMV DRCOMM)_51012926.md)**和**[RMV DRINST](删除容灾实例(RMV DRINST)_51012923.md)**等删除容灾配置的命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| DRINSTID | 容灾实例ID | 可选必选说明：必选参数。<br>参数含义：该参数用于配置容灾实例标识。当在本端配置本端容灾实例地址时，该参数必须与本端<br>**[ADD DRINST](配置容灾实例(ADD DRINST)_51011025.md)**<br>命令中配置的<br>“容灾实例ID”<br>保持一致；当在本端配置对端容灾实例地址时，该参数必须与对端<br>**[ADD DRINST](配置容灾实例(ADD DRINST)_51011025.md)**<br>命令中配置的<br>“容灾实例ID”<br>保持一致。<br>数据来源：全网规划。<br>取值范围：整型，0~63。<br>默认值：无。 |
| IPVERSION | ip版本号 | 可选必选说明：必选参数。<br>参数含义：IP版本。<br>数据来源：本端规划。<br>取值范围：枚举类型。<br>COMM_IPV4：IP版本为IPv4。<br>COMM_IPV6：IP版本为IPv6。<br>默认值：无。 |
| COMMIPV4 | ipv4通信地址 | 可选必选说明：条件必选参数。<br>前提条件：该参数在“IPVERSION”配置为“COMM_IPV4”时为条件必选参数。<br>参数含义：该参数用于配置本端或对端容灾通道IPv4地址。<br>数据来源：全网规划。<br>取值范围：IPv4地址类型。<br>默认值：无。 |
| COMMIPV6 | ipv6通信地址 | 可选必选说明：条件必选参数。<br>前提条件：该参数在“IPVERSION”配置为“COMM_IPV6”时为条件必选参数。<br>参数含义：该参数用于配置本端或对端容灾通道IPv6地址。<br>数据来源：全网规划。<br>取值范围：IPv6地址类型。<br>默认值：无。 |
| VPNNAME | VPN名称 | 可选必选说明：必选参数。<br>参数含义：VPN实例名称。<br>数据来源：全网规划。<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_。 |
| COMMNAME | 通信名称 | 可选必选说明：可选参数。<br>参数含义：通信名称。<br>数据来源：全网规划。<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DRCOMM]] · 容灾实例地址（DRCOMM）

## 使用实例

增加 “容灾实例ID” 为 “1” 、 “ip版本号” 为 “COMM_IPV4” 、 “ipv4通信地址” 为 “192.168.1.1” 、 “VPN名称” 为 “_public_” 的容灾实例地址：

```
ADD DRCOMM: DRINSTID=1, IPVERSION=COMM_IPV4, COMMIPV4="192.168.1.1", VPNNAME="_public_";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-DRCOMM.md`
