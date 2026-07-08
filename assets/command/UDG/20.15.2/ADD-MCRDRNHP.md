---
id: UDG@20.15.2@MMLCommand@ADD MCRDRNHP
type: MMLCommand
name: ADD MCRDRNHP（增加组播报文重定向策略）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: MCRDRNHP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 4093
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- MRM
- 组播报文重定向策略配置
status: active
---

# ADD MCRDRNHP（增加组播报文重定向策略）

## 功能

该命令用来创建组播报文重定向策略。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为4093。
- 当前仅支持地址类型为IPv4的下一跳，且下一跳地址不能为空。
- “_public_”、“_mpp_vpn_inner__”和“__mpp_vpn_inner_server__”不支持配置组播报文重定向策略。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNNAME | VPN名称 | 可选必选说明：必选参数<br>参数含义：该参数用来表示VPN实例名称。<br>数据来源：本端规划。<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无。<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| IPVERSION | 地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定下一跳地址为IPv4类型或IPv6类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4类型。<br>- IPv6：IPv6类型。<br>默认值：IPv4<br>配置原则：无 |
| NEXTHOPADDRV4 | IPv4下一跳地址 | 可选必选说明：条件必选<br>参数含义：该参数用于指定下一跳IPv4地址，表示重定向到的网关IP。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| NEXTHOPADDRV6 | IPv6下一跳地址 | 可选必选说明：条件必选<br>参数含义：该参数用于指定下一跳IPv6地址，表示重定向到的网关IP。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@MCRDRNHP]] · 组播报文重定向策略（MCRDRNHP）

## 使用实例

增加组播报文重定向策略：

```
ADD MCRDRNHP: VPNNAME="vrf1", IPVERSION=IPv4, NEXTHOPADDRV4="192.168.0.1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-MCRDRNHP.md`
