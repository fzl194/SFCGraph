---
id: UDG@20.15.2@MMLCommand@RMV IPRUREACH
type: MMLCommand
name: RMV IPRUREACH（删除RU到网关的可达性检测配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: IPRUREACH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 无线路由管理
- RU到网关的可达性
status: active
---

# RMV IPRUREACH（删除RU到网关的可达性检测配置）

## 功能

该命令用于删除RU到网关可达性检测的配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| IPVERSION | IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用来表示网关地址的IP版本。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |
| DESTADDR4 | 目的地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“ipv4unicast”时为必选参数。<br>参数含义：该命令用来表示网关的IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| DESTADDR6 | 目的地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“ipv6unicast”时为必选参数。<br>参数含义：该命令用来表示网关的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| SOURCERU | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用来表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～49。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPRUREACH]] · RU到网关的可达性检测配置（IPRUREACH）

## 使用实例

删除一条RU到网关可达性检测的配置：

```
RMV IPRUREACH:VPNNAME="vrf",IPVERSION=ipv4unicast,DESTADDR4="10.1.1.1",SOURCERU="VNODE_VNRS_VNFC_IPU_0066";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除RU到网关的可达性检测配置（RMV-IPRUREACH）_00440693.md`
