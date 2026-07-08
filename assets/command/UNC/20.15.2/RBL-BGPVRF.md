---
id: UNC@20.15.2@MMLCommand@RBL BGPVRF
type: MMLCommand
name: RBL BGPVRF（复位BGP VPN实例）
nf: UNC
version: 20.15.2
verb: RBL
object_keyword: BGPVRF
command_category: 动作类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 复位BGP VPN实例
status: active
---

# RBL BGPVRF（复位BGP VPN实例）

## 功能

![](复位BGP VPN实例（RBL BGPVRF）_00840661.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，操作不当会重置实例下所有的地址族和邻居，请谨慎使用并联系华为技术支持协助操作。

该命令会重置实例下所有的地址族、邻居信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令用于重置BGP VPN实例信息，执行该命令会重置实例下所有的地址族、邻居信息。
- VRFNAME和AFTYPE不输入参数时表示复位所有公私网实例。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户所配置的VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VRF的地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv6uni：IPv6地址族。<br>默认值：无<br>配置原则：如果不输入该参数，默认复位所有地址族下邻居。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@BGPVRF]] · BGP VPN实例（BGPVRF）

## 使用实例

重置路由器中的BGPVRF：

```
RBL BGPVRF: VRFNAME="_public_", AFTYPE=ipv4uni;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RBL-BGPVRF.md`
