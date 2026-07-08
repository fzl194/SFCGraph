---
id: UNC@20.15.2@MMLCommand@ADD IPBINDVPN
type: MMLCommand
name: ADD IPBINDVPN（增加接口绑定VPN）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IPBINDVPN
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 65535
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- IP绑定VPN
status: active
---

# ADD IPBINDVPN（增加接口绑定VPN）

## 功能

该命令用于配置接口绑定VPN。配置VPN实例后，需要将设备上与VPN网络连接的接口与VPN实例绑定。接口与VPN实例绑定后，该接口将变为私网接口，可以配置私网地址、运行私网路由协议等，从而使该接口进入的报文使用VPN实例中的转发信息进行转发。如果要配置私网下的IPv6地址，请使用该命令配置接口下VPN之后，使用ADD IFIPV6ADDRESS命令配置IPv6地址。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。
- 当参数IFIPADDR不指定时，会清空该接口下原来的IP地址；当参数IFIPADDR指定时，会使用被指定的地址替代原来的地址。
- 该接口需要支持配置IP地址。
- 该命令在版本升级过程中禁止执行。
- 每个主用接口最大允许配置256个接口IP地址：1个主IP地址和255个从IP地址。
- 该命令的必选参数IFNAME可通过LST INTERFACE命令查询到。

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

- [接口绑定VPN（IPBINDVPN）](configobject/UNC/20.15.2/IPBINDVPN.md)

## 使用实例

配置接口绑定VPN：

```
ADD IPBINDVPN:IFNAME="Ethernet64/0/3",VRFNAME="vrf1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加接口绑定VPN（ADD-IPBINDVPN）_50120734.md`
