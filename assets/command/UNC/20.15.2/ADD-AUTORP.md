---
id: UNC@20.15.2@MMLCommand@ADD AUTORP
type: MMLCommand
name: ADD AUTORP（添加Auto-RP配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: AUTORP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 65535
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- PIM配置
- Auto-RP侦听
status: active
---

# ADD AUTORP（添加Auto-RP配置）

## 功能

该命令用于添加Auto-RP的配置。

当路由器与支持Auto-RP的设备互通时，需要配置此命令来使能Auto-RP侦听功能，即接收Auto-RP宣告和发现报文，并从发现报文中学习RP信息。

路由器在接收到Auto-RP宣告报文或发现报文之后，解析报文的源地址，根据源地址进行RPF检查。

如果RPF检查失败，则路由器丢弃该报文；如果RPF检查通过，则路由器向其他PIM邻居转发该报文。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。
- 需要首先在公网或VPN实例下配置ADD MCASTENABLE命令。
- 需要首先在公网或VPN实例下配置ADD PIMSITE命令。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |

## 操作的配置对象

- [Auto-RP配置（AUTORP）](configobject/UNC/20.15.2/AUTORP.md)

## 使用实例

配置支持Auto-RP功能：

```
ADD AUTORP:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/添加Auto-RP配置（ADD-AUTORP）_49961218.md`
