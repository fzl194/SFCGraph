---
id: UNC@20.15.2@MMLCommand@SYN BGPPEER
type: MMLCommand
name: SYN BGPPEER（刷新BGP对等体）
nf: UNC
version: 20.15.2
verb: SYN
object_keyword: BGPPEER
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 刷新BGP对等体
status: active
---

# SYN BGPPEER（刷新BGP对等体）

## 功能

该命令用于刷新指定BGP对等体信息。

当BGP配置发生变化后，如果需要使新的配置立即生效，可以执行SYN BGPPEER命令。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | BGP地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定BGP地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>- ipv6vpn：VPNv6地址族。<br>默认值：无 |
| DIRECTION | 方向 | 可选必选说明：必选参数<br>参数含义：该参数用于指定刷新BGP路由信息的方向。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- export：出口。<br>- import：入口。<br>默认值：无 |
| REMOTEADDRESS | 对等体地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对等体地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@BGPPEER]] · BGP对等体（BGPPEER）

## 使用实例

刷新BGP对等体：

```
SYN BGPPEER:VRFNAME="_public_",AFTYPE=ipv4uni,DIRECTION=export,REMOTEADDRESS="10.1.1.1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SYN-BGPPEER.md`
