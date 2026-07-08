---
id: UDG@20.15.2@MMLCommand@RMV L3VPNINST
type: MMLCommand
name: RMV L3VPNINST（删除L3VPN实例）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: L3VPNINST
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- VPN管理
- L3VPN管理
- L3VPN实例
status: active
---

# RMV L3VPNINST（删除L3VPN实例）

## 功能

![](删除L3VPN实例（RMV L3VPNINST）_50120962.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会删除所有该VPN下的关联配置，请谨慎使用并联系华为技术支持协助操作。

该命令用来删除已创建的L3VPN实例。

## 注意事项

- 该命令执行后立即生效。
- 该操作会删除所有该VPN下的关联配置。
- 不能删除VPN实例_public_、__mpp_vpn_inner__、__mpp_vpn_inner_server__。
- 使用RMV L3VPNINST删除VPN实例后，VPN关联配置VPNINSTAF、PREFIXLIMIT等也会联动删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定L3VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/L3VPNINST]] · L3VPN实例（L3VPNINST）

## 使用实例

删除名称为“vrf1”的VPN实例：

```
RMV L3VPNINST: VRFNAME="vrf1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除L3VPN实例（RMV-L3VPNINST）_50120962.md`
