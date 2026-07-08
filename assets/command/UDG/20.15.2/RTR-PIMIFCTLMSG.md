---
id: UDG@20.15.2@MMLCommand@RTR PIMIFCTLMSG
type: MMLCommand
name: RTR PIMIFCTLMSG（清除PIM接口报文统计计数）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: PIMIFCTLMSG
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- PIM配置
- PIM报文统计计数
status: active
---

# RTR PIMIFCTLMSG（清除PIM接口报文统计计数）

## 功能

该命令用于清除PIM接口报文统计计数。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PIMIFCTLMSG]] · PIM接口报文统计计数（PIMIFCTLMSG）

## 使用实例

清除PIM接口报文统计计数：

```
RTR PIMIFCTLMSG: VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast,IFNAME="Ethernet64/0/3";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RTR-PIMIFCTLMSG.md`
