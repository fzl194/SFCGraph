---
id: UDG@20.15.2@MMLCommand@LST UPDBGPPEERGROUP
type: MMLCommand
name: LST UPDBGPPEERGROUP（查询BGP对等体分组）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPDBGPPEERGROUP
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 升级的BGP对等体分组
status: active
---

# LST UPDBGPPEERGROUP（查询BGP对等体分组）

## 功能

该命令用于查看IPv4或IPv6对等体分组。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户所配置的BGP VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：使用<br>**[LST BGPVRFAF](../BGP VPN地址族/查询BGP VPN地址族（LST BGPVRFAF）_50121286.md)**<br>命令查看可用BGP VPN。 |
| AFTYPE | 地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对等体的地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>- ipv6uni：IPv6地址族。<br>- ipv6vpn：VPNv6地址族。<br>默认值：无<br>配置原则：无 |
| PEERADDR1 | 对等体1地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定分组的第一个对等体地址。<br>数据来源：对端协商<br>取值范围：IPv4或IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| PEERADDR2 | 对等体2地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定分组的第二个对等体地址。<br>数据来源：对端协商<br>取值范围：IPv4或IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPDBGPPEERGROUP]] · BGP对等体分组（UPDBGPPEERGROUP）

## 使用实例

查看名称为“vrf1”的BGP VPN实例下对等体分组：

```
LST UPDBGPPEERGROUP:VRFNAME="vrf1";
RETCODE = 0  操作成功
结果如下:
---------
VPN实例名称  =  vrf1
 地址族类型  =  IPv4uni
对等体1地址  =  10.1.1.1
对等体2地址  =  10.2.2.2
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-UPDBGPPEERGROUP.md`
