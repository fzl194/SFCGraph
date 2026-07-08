---
id: UDG@20.15.2@MMLCommand@ADD QOSRDRWLRFLOW
type: MMLCommand
name: ADD QOSRDRWLRFLOW（增加WLR引流重定向）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: QOSRDRWLRFLOW
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 65535
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 重定向WLR业务流
status: active
---

# ADD QOSRDRWLRFLOW（增加WLR引流重定向）

## 功能

该命令用于将接口收到的报文与WLR引流表进行匹配。如果匹配成功，则将流量引到CSLB_VNFC上；否则，报文查找路由表进行转发。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。
- 如果CSLB没有引流表业务，则该配置不生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置的接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：与设备接口名称保持一致，下发本MML命令前可使用LST INTERFACE查看设备接口。 |
| IPVERSION | IP协议版本 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口重定向引流使能的地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4：IPv4类型。<br>- ipv6：IPv6类型。<br>默认值：ipv4 |

## 操作的配置对象

- [WLR引流重定向（QOSRDRWLRFLOW）](configobject/UDG/20.15.2/QOSRDRWLRFLOW.md)

## 使用实例

配置以太网接口Ethernet66/0/3 WLR引流重定向：

```
ADD QOSRDRWLRFLOW:IFNAME="Ethernet66/0/3",IPVERSION=ipv4;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加WLR引流重定向（ADD-QOSRDRWLRFLOW）_00600289.md`
