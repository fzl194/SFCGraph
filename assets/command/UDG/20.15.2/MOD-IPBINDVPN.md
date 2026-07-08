---
id: UDG@20.15.2@MMLCommand@MOD IPBINDVPN
type: MMLCommand
name: MOD IPBINDVPN（修改接口绑定VPN）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: IPBINDVPN
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- IP绑定VPN
status: active
---

# MOD IPBINDVPN（修改接口绑定VPN）

## 功能

该命令用于修改接口已绑定的VPN。

## 注意事项

- 该命令执行后立即生效。
- 当参数IFIPADDR不指定时，会清空该接口下原来的IP地址；当参数IFIPADDR指定时，会使用被指定的地址替代原来的地址。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于表示绑定VPN的接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| IFIPADDR | IPv4地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要配置的IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。0.0.0.0～255.255.255.255。<br>默认值：无<br>配置原则：本参数参与自动化配置，请在下发本MML命令前使用DSP OPSASSISTSTATE命令查询自动化配置维护助手autoscaling_autoconfig.py，确保当前设备不在自动化配置过程中。如果当前正在自动化配置过程中，不要做本业务的增删改操作，否则最终生效的配置将不可预期。 |
| SUBNETMASK | IPv4地址掩码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要配置的接口IPv4地址的网络掩码。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。0.0.0.0～255.255.255.255。<br>默认值：无<br>配置原则：本参数参与自动化配置，请在下发本MML命令前使用DSP OPSASSISTSTATE命令查询自动化配置维护助手autoscaling_autoconfig.py，确保当前设备不在自动化配置过程中。如果当前正在自动化配置过程中，不要做本业务的增删改操作，否则最终生效的配置将不可预期。 |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口绑定的VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：本参数参与自动化配置，请在下发本MML命令前使用DSP OPSASSISTSTATE命令查询自动化配置维护助手autoscaling_autoconfig.py，确保当前设备不在自动化配置过程中。如果当前正在自动化配置过程中，不要做本业务的增删改操作，否则最终生效的配置将不可预期。请使用LST L3VPNINST命令查看可用VPN。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPBINDVPN]] · 接口绑定VPN（IPBINDVPN）

## 使用实例

修改接口绑定VPN：

```
MOD IPBINDVPN:IFNAME="Ethernet64/0/3",VRFNAME="vrf1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-IPBINDVPN.md`
