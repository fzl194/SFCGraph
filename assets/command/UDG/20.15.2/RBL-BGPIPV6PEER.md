---
id: UDG@20.15.2@MMLCommand@RBL BGPIPV6PEER
type: MMLCommand
name: RBL BGPIPV6PEER（复位BGP IPv6邻居）
nf: UDG
version: 20.15.2
verb: RBL
object_keyword: BGPIPV6PEER
command_category: 动作类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 复位BGP IPv6对等体
status: active
---

# RBL BGPIPV6PEER（复位BGP IPv6邻居）

## 功能

![](复位BGP IPv6邻居（RBL BGPIPV6PEER）_50120730.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致IPv6邻居断连，请谨慎使用并联系华为技术支持协助操作。

该命令用于重置某地址族下某IPv6地址邻居。

## 注意事项

- 该命令执行后立即生效。
- 该命令用于重置某地址族下某IPV6邻居，执行该命令会复位与指定对等体的TCP连接，通过此连接学到的所有路由也同时被删除。
- 执行该命令会导致IPv6邻居断连。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户所配置的VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv6uni：IPv6地址族。<br>默认值：无 |
| REMOTEADDRESS | 对等体地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对等体地址。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/BGPIPV6PEER]] · BGP IPv6对等体（BGPIPV6PEER）

## 使用实例

重置BGP IPv6邻居：

```
RBL BGPIPV6PEER: VRFNAME="_public_", AFTYPE=ipv6uni;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/复位BGP-IPv6邻居（RBL-BGPIPV6PEER）_50120730.md`
