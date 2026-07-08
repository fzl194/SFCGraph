---
id: UDG@20.15.2@MMLCommand@RMV IPBINDVPN
type: MMLCommand
name: RMV IPBINDVPN（删除接口绑定VPN）
nf: UDG
version: 20.15.2
verb: RMV
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

# RMV IPBINDVPN（删除接口绑定VPN）

## 功能

该命令用于配置接口去绑定VPN。如果接口不再与VPN网络连接，需要去绑定VPN。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令将清除该接口下所有的IP配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于表示绑定VPN的接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口绑定的VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：本参数参与自动化配置，请在下发本MML命令前使用DSP OPSASSISTSTATE命令查询自动化配置维护助手autoscaling_autoconfig.py，确保当前设备不在自动化配置过程中。如果当前正在自动化配置过程中，不要做本业务的增删改操作，否则最终生效的配置将不可预期。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IPBINDVPN]] · 接口绑定VPN（IPBINDVPN）

## 使用实例

配置接口去绑定VPN：

```
RMV IPBINDVPN:IFNAME="Ethernet64/0/3",VRFNAME="vrf1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-IPBINDVPN.md`
