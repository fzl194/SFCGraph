---
id: UNC@20.15.2@MMLCommand@ADD L3VPNINSTIPSEC
type: MMLCommand
name: ADD L3VPNINSTIPSEC（增加L3VPN实例）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: L3VPNINSTIPSEC
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- VPN管理
- L3VPN管理
- L3VPN实例配置命令
status: active
---

# ADD L3VPNINSTIPSEC（增加L3VPN实例）

## 功能

该命令用于增加L3VPN实例。

## 注意事项

- 该命令执行后立即生效。

- 不能增加VPN实例 _public_、__mpp_vpn_inner__ 。

- 最多可输入1001条记录。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| VRFNAME |
| --- |
| _public_ |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户需要增加的L3VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：<br>不支持空格。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@L3VPNINSTIPSEC]] · L3VPN实例（L3VPNINSTIPSEC）

## 使用实例

新建名称为“vrf1”的VPN实例：

```
ADD L3VPNINSTIPSEC: VRFNAME="vrf1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-L3VPNINSTIPSEC.md`
