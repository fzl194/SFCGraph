---
id: UNC@20.15.2@MMLCommand@RMV SRBFDTEMPLET
type: MMLCommand
name: RMV SRBFDTEMPLET（删除BFD模板）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SRBFDTEMPLET
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 静态路由管理
- 配置BFD模板
status: active
---

# RMV SRBFDTEMPLET（删除BFD模板）

## 功能

该命令用于删除BFD模板。

## 注意事项

- 该命令执行后立即生效。
- 删除该BFD模板时，要保证该模板添加过。
- 可能有静态路由正在使用该模板，删除会导致静态路由与BFD取消关联，进而无法感知链路状态。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFTYPE | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| NEXTHOP | 路由下一跳 | 可选必选说明：可选参数<br>参数含义：该参数用于指定下一跳地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| IFNAME | 接口名字 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由的传输接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 下一跳所在VPN为私网时，应输入Invalid0，不区分大小写。<br>- 请使用LST INTERFACE命令查看可用接口。 |
| DESTVRFNAME | 网关地址VPN | 可选必选说明：可选参数<br>参数含义：该参数用于指定网关地址所属VPN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| DHCPENABLE | DHCP使能 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DHCP使能标志。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SRBFDTEMPLET]] · BFD模板（SRBFDTEMPLET）

## 使用实例

删除一个BFD模板，BFD模板的网关地址为10.1.1.1：

```
RMV SRBFDTEMPLET: NEXTHOP="10.1.1.1",AFTYPE=ipv4unicast,DESTVRFNAME="_public_", IFNAME="ethernet64/0/5";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除BFD模板（RMV-SRBFDTEMPLET）_49801730.md`
