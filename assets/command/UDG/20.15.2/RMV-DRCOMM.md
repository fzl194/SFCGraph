---
id: UDG@20.15.2@MMLCommand@RMV DRCOMM
type: MMLCommand
name: RMV DRCOMM（删除容灾实例地址）
nf: UDG
version: 20.15.2
verb: RMV
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

# RMV DRCOMM（删除容灾实例地址）

## 功能

![](删除容灾实例地址(RMV DRCOMM)_51012926.assets/notice_3.0-zh-cn.png)

该操作将删除容灾配置，影响容灾数据备份，操作前请先确保已经关闭容灾激活开关。

该命令用于删除本端或对端容灾实例地址信息。

## 注意事项

- 执行该命令之前，请先确保已经关闭容灾激活开关。
- 执行该命令后，请使用**[RMV DRCOMM](删除容灾实例地址(RMV DRCOMM)_51012926.md)**和**[RMV DRINST](删除容灾实例(RMV DRINST)_51012923.md)**命令删除该网元上其他容灾通道和容灾实例，新配置的容灾实例地址才能生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| DRINSTID | 容灾实例ID | 可选必选说明：必选参数。<br>参数含义：该参数用于配置容灾实例标识。<br>数据来源：全网规划。<br>取值范围：整型，0~63。<br>默认值：无。 |
| IPVERSION | ip版本号 | 可选必选说明：必选参数。<br>参数含义：IP版本。<br>数据来源：本端规划。<br>取值范围：枚举类型。<br>COMM_IPV4：IP版本为IPv4。<br>COMM_IPV6：IP版本为IPv6。<br>默认值：无。 |
| COMMIPV4 | ipv4通信地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“COMM_IPV4”时为条件必选参数。<br>参数含义：通信IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| COMMIPV6 | ipv6通信地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“COMM_IPV6”时为条件必选参数。<br>参数含义：通信IPv6地址。<br>数据来源：全网规划。<br>取值范围：IPv6地址类型。<br>默认值：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DRCOMM]] · 容灾实例地址（DRCOMM）

## 使用实例

删除 “容灾实例ID” 为 “1” 、 “ip版本号” 为 “COMM_IPV4” 、 “ipv4通信地址” 为 “192.168.1.2” 的容灾实例地址：

```
RMV DRCOMM: DRINSTID=1, IPVERSION=COMM_IPV4, COMMIPV4="192.168.1.2";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-DRCOMM.md`
