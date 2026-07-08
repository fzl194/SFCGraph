---
id: UDG@20.15.2@MMLCommand@RMV OSPFNETWORK
type: MMLCommand
name: RMV OSPFNETWORK（删除OSPF运行的接口及所属区域）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: OSPFNETWORK
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- 指定OSPF运行的接口及所属区域
status: active
---

# RMV OSPFNETWORK（删除OSPF运行的接口及所属区域）

## 功能

该命令用于在OSPF进程下的区域删除网段的配置。

## 注意事项

- 该命令执行后立即生效。
- 只有配置了OSPF进程、OSPF区域和区域下的网段后才能使用该命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| AREAID | 区域号 | 可选必选说明：必选参数<br>参数含义：OSPF区域号。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| IPADDRESS | IP地址 | 可选必选说明：必选参数<br>参数含义：接口所在的网段地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| WILDCARDMASK | 反掩码 | 可选必选说明：必选参数<br>参数含义：IP地址的反掩码。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@OSPFNETWORK]] · OSPF运行的接口及所属区域（OSPFNETWORK）

## 使用实例

删除在OSPF进程下1区域0.0.0.0下网段192.168.0.0/24：

```
RMV OSPFNETWORK: PROCID=1, AREAID="0.0.0.0", IPADDRESS="192.168.0.0", WILDCARDMASK="0.0.0.255";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-OSPFNETWORK.md`
