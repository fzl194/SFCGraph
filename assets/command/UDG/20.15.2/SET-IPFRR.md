---
id: UDG@20.15.2@MMLCommand@SET IPFRR
type: MMLCommand
name: SET IPFRR（设置IP FRR）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: IPFRR
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由基础
- 路由管控功能列表
status: active
---

# SET IPFRR（设置IP FRR）

## 功能

该命令用来使能IP FRR功能。

在设备上存在多种路由协议生成的路由时，如果想在部分路由故障后能够快速切换以使报文转发顺畅，可以通过配置此命令使能协议路由间的IP FRR功能。

例如，在设备上存在OSPF协议生成的一条目的地址为10.1.1.1的OSPF路由，优先级为15。同时再配置一条到目的地址10.1.1.1的静态路由，优先级为60。在未使能IP FRR的情况下，优选OSPF路由。在使能IP FRR后，会生成一条新的路由，OSPF路由作为主路由，静态路由作为备份路由。这样，在OSPF路由故障时，系统可以快速切换到静态路由，保证转发畅通。

## 注意事项

- 该命令执行后立即生效。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| FRRENABLE |
| --- |
| FALSE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFTYPE | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址族类型。支持IPv4和IPv6单播地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：<br>- 需要确保指定的VPN实例在设备上已经通过ADD L3VPNINST创建，公网除外。<br>- 必须已经通过ADD VPNINSTAF使能了该VPN的地址族。 |
| FRRENABLE | 是否使能FRR | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否使能IP FRR功能。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：初始值为FALSE。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPFRR]] · IP FRR（IPFRR）

## 使用实例

配置IPv4公网FRR：

```
SET IPFRR:AFTYPE=ipv4unicast,VRFNAME="_public_",FRRENABLE=TRUE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-IPFRR.md`
