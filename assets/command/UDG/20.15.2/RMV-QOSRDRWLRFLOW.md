---
id: UDG@20.15.2@MMLCommand@RMV QOSRDRWLRFLOW
type: MMLCommand
name: RMV QOSRDRWLRFLOW（删除WLR引流重定向）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: QOSRDRWLRFLOW
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 重定向WLR业务流
status: active
---

# RMV QOSRDRWLRFLOW（删除WLR引流重定向）

## 功能

该命令用于删除WLR引流重定向的配置，该命令执行之后，从接口收到的报文不再与WLR引流表进行匹配。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置的接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用LST INTERFACE命令查看可用接口。 |
| IPVERSION | IP协议版本 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口重定向引流使能的地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4：IPv4类型。<br>- ipv6：IPv6类型。<br>默认值：ipv4 |

## 操作的配置对象

- [WLR引流重定向（QOSRDRWLRFLOW）](configobject/UDG/20.15.2/QOSRDRWLRFLOW.md)

## 使用实例

删除以太网接口Ethernet66/0/3 WLR引流重定向：

```
RMV QOSRDRWLRFLOW:IFNAME="Ethernet66/0/3",IPVERSION=ipv4;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除WLR引流重定向（RMV-QOSRDRWLRFLOW）_50281186.md`
