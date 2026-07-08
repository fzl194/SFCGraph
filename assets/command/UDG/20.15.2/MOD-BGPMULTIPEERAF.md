---
id: UDG@20.15.2@MMLCommand@MOD BGPMULTIPEERAF
type: MMLCommand
name: MOD BGPMULTIPEERAF（修改BGP多源对等体地址族）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: BGPMULTIPEERAF
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- BGP多源对等体地址族
status: active
---

# MOD BGPMULTIPEERAF（修改BGP多源对等体地址族）

## 功能

该命令用于在地址族下使能和去使能BGP多源对等体。

## 注意事项

- 该命令执行后立即生效。
- 该命令依赖于ADD BGPMULTIPEER和ADD BGPPEERAF。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv6uni：IPv6地址族。<br>默认值：无<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| PEERADDR | 对等体地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定建立对等体的接口地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |
| SOURCEIFNAME | 源接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定建立对等体的源接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：仅支持Ethernet及其子接口类型，不区分大小写。 |
| MULTIENABLE | 是否使能多源对等体 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否使能多源对等体。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |

## 操作的配置对象

- [BGP多源对等体地址族（BGPMULTIPEERAF）](configobject/UDG/20.15.2/BGPMULTIPEERAF.md)

## 使用实例

修改BGP多源对等体地址族：

```
MOD BGPMULTIPEERAF:VRFNAME="vrf1",AFTYPE=ipv4uni,PEERADDR="10.2.2.2",SOURCEIFNAME="Ethernet66/0/3",MULTIENABLE=FALSE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改BGP多源对等体地址族（MOD-BGPMULTIPEERAF）_49802050.md`
