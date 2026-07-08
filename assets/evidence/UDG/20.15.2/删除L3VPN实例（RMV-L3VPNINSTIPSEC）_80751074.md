# 删除L3VPN实例（RMV L3VPNINSTIPSEC）

- [命令功能](#ZH-CN_MMLREF_0000001180751074__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001180751074__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001180751074__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001180751074__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001180751074)

![](删除L3VPN实例（RMV L3VPNINSTIPSEC）_80751074.assets/notice_3.0-zh-cn.png)

该操作会删除所有该VPN下的关联配置，请谨慎使用。

该命令用来删除L3VPN实例。

> **说明**
> - 该命令执行后立即生效。
>
> - 不能删除VPN实例 _public_、__mpp_vpn_inner__ 。
> - 使用RMV L3VPNINSTIPSEC删除VPN实例后，VPN关联配置VPNINSTAF等也会联动删除。

#### [操作用户权限](#ZH-CN_MMLREF_0000001180751074)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001180751074)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户需要增加的L3VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：<br>不支持空格。 |

## [使用实例](#ZH-CN_MMLREF_0000001180751074)

删除名称为“vrf1”的VPN实例：

```
RMV L3VPNINSTIPSEC: VRFNAME="vrf1";
```
