---
id: UDG@20.15.2@MMLCommand@ADD UPDBGPPEERGROUP
type: MMLCommand
name: ADD UPDBGPPEERGROUP（添加BGP对等体分组）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: UPDBGPPEERGROUP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 65535
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 升级的BGP对等体分组
status: active
---

# ADD UPDBGPPEERGROUP（添加BGP对等体分组）

## 功能

该命令用于增加IPv4或IPv6对等体分组。

## 注意事项

- 该命令执行后立即生效。
- 该命令主要在灰度升级场景中使用；根据实际组网将BGP对等体成对分组，在升级中，升级流程会保证每个分组至少有1个BGP对等体邻居是建立的。
- BGP IPv4或者IPv6私网地址族下的邻居数量超过2个才需要分组。
- 该命令最大记录数为65535。
- 在灰度升级结束后，需要使用**[RMV UPDBGPPEERGROUP](删除BGP对等体分组（RMV UPDBGPPEERGROUP）_47101557.md)**命令删除分组。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户所配置的BGP VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：使用<br>**[LST BGPVRFAF](../BGP VPN地址族/查询BGP VPN地址族（LST BGPVRFAF）_50121286.md)**<br>命令查看可用BGP VPN。 |
| AFTYPE | 地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对等体的地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>- ipv6uni：IPv6地址族。<br>- ipv6vpn：VPNv6地址族。<br>默认值：无<br>配置原则：无 |
| PEERADDR1 | 对等体1地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定分组的第一个对等体地址。<br>数据来源：对端协商<br>取值范围：IPv4或IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| PEERADDR2 | 对等体2地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定分组的第二个对等体地址。<br>数据来源：对端协商<br>取值范围：IPv4或IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@UPDBGPPEERGROUP]] · BGP对等体分组（UPDBGPPEERGROUP）

## 使用实例

将名称为“vrf1”的BGP IPv4 VPN实例下对等体10.1.1.1和10.2.2.2分为1组：

```
ADD UPDBGPPEERGROUP:VRFNAME="vrf1",AFTYPE=ipv4uni,PEERADDR1="10.1.1.1",PEERADDR2="10.2.2.2";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-UPDBGPPEERGROUP.md`
