---
id: UNC@20.15.2@MMLCommand@RMV BGPVRFAF
type: MMLCommand
name: RMV BGPVRFAF（删除BGP VPN地址族）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: BGPVRFAF
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- BGP VPN地址族
status: active
---

# RMV BGPVRFAF（删除BGP VPN地址族）

## 功能

该命令用于删除BGP VPN地址族。

![](删除BGP VPN地址族（RMV BGPVRFAF）_49961802.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，该操作会删除BGP所有该VPN实例地址族下的关联配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：使用LST BGPVRFAF命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定BGP VPN实例下的地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>- ipv6uni：IPv6地址族。<br>- ipv6vpn：VPNv6地址族。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@BGPVRFAF]] · BGP VPN地址族（BGPVRFAF）

## 使用实例

删除BGP VPN中IPv4单播地址族：

```
RMV BGPVRFAF:VRFNAME="vrf1",AFTYPE=ipv4uni;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-BGPVRFAF.md`
