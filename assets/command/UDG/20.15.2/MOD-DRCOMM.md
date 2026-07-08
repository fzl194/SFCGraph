---
id: UDG@20.15.2@MMLCommand@MOD DRCOMM
type: MMLCommand
name: MOD DRCOMM（修改容灾实例地址）
nf: UDG
version: 20.15.2
verb: MOD
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

# MOD DRCOMM（修改容灾实例地址）

## 功能

该命令用于修改本端或对端容灾实例地址信息。

## 注意事项

修改容灾实例地址后需要去激活再激活license才能进入实备。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| DRINSTID | 容灾实例ID | 可选必选说明：必选参数。<br>参数含义：该参数用于配置容灾实例标识。<br>数据来源：全网规划。<br>取值范围：整型，0~63。<br>默认值：无。 |
| IPVERSION | ip版本号 | 可选必选说明：必选参数。<br>参数含义：IP版本。<br>数据来源：本端规划。<br>取值范围：枚举类型。<br>COMM_IPV4：IP版本为IPv4。<br>COMM_IPV6：IP版本为IPv6。<br>默认值：无。 |
| COMMIPV4 | ipv4通信地址 | 可选必选说明：条件必选参数。<br>前提条件：该参数在“IPVERSION”配置为“COMM_IPV4”时为条件必选参数。<br>参数含义：通信IPv4地址。<br>数据来源：全网规划。<br>取值范围：IPv4地址类型。<br>默认值：无。 |
| COMMIPV6 | ipv6通信地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“COMM_IPV6”时为条件必选参数。<br>参数含义：通信IPv6地址。<br>数据来源：全网规划。<br>取值范围：IPv6地址类型。<br>默认值：无。 |
| VPNNAME | VPN名称 | 可选必选说明：可选参数。<br>参数含义：VPN实例名称。<br>数据来源：全网规划。<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无。 |
| COMMNAME | 通信名称 | 可选必选说明：可选参数。<br>参数含义：通信名称。<br>数据来源：全网规划。<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@DRCOMM]] · 容灾实例地址（DRCOMM）

## 使用实例

修改 “容灾实例ID” 为 “1” 、 “ip版本号” 为 “COMM_IPV4” 、 “ipv4通信地址” 为 “192.168.1.2” 的容灾实例地址：

```
MOD DRCOMM: DRINSTID=1, IPVERSION=COMM_IPV4, COMMIPV4="192.168.1.2";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-DRCOMM.md`
