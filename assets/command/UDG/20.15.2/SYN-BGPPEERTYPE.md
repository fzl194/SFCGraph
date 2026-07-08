---
id: UDG@20.15.2@MMLCommand@SYN BGPPEERTYPE
type: MMLCommand
name: SYN BGPPEERTYPE（刷新对等体类型）
nf: UDG
version: 20.15.2
verb: SYN
object_keyword: BGPPEERTYPE
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 刷新对等体类型
status: active
---

# SYN BGPPEERTYPE（刷新对等体类型）

## 功能

该命令用于刷新指定对等体类型的路由信息。

当BGP配置发生变化后，如果需要使新的配置立即生效，可以执行SYN BGPPEERTYPE命令。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | BGP地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定BGP地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>- ipv6uni：IPv6地址族。<br>- ipv6vpn：VPNv6地址族。<br>默认值：无 |
| DIRECTION | 方向 | 可选必选说明：必选参数<br>参数含义：该参数用于指定刷新BGP路由信息的方向。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- export：出口。<br>- import：入口。<br>默认值：无 |
| PEERTYPE | 对等体类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对等体类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ebgp：EBGP。<br>- ibgp：IBGP。<br>默认值：无<br>配置原则：如果不输入该参数，默认更新所有类型邻居。 |

## 操作的配置对象

- [对等体类型（BGPPEERTYPE）](configobject/UDG/20.15.2/BGPPEERTYPE.md)

## 使用实例

刷新对等体类型：

```
SYN BGPPEERTYPE:AFTYPE=ipv4uni,DIRECTION=import;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/刷新对等体类型（SYN-BGPPEERTYPE）_00600393.md`
