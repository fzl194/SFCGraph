---
id: UDG@20.15.2@MMLCommand@SET IFIPV6ENABLEIPSEC
type: MMLCommand
name: SET IFIPV6ENABLEIPSEC（设置接口IPv6使能）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: IFIPV6ENABLEIPSEC
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- 接口管理
- IPv6使能
status: active
---

# SET IFIPV6ENABLEIPSEC（设置接口IPv6使能）

## 功能

该命令用于修改接口的IPv6使能情况，用户可通过该命令修改接口的IPv6 MTU和Autolinklocal标志。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令在VNRS_VNFC上的Ethernet接口，Ethernet子接口，Eth-Trunk接口，Eth-Trunk子接口以及Loopback口，Tunnel口上配置执行。
> - 缺省情况下，接口上不使能IPv6。
> - 若IPv4 MTU与IPv6 MTU都配置的时候，实际取两者之间的较大值配置至vNic。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于配置IPv6使能的接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。接口名称由接口类型+接口编号组成。<br>默认值：无。<br>配置原则：<br>请使用<br>[**LST INTERFACEIPSEC**](../接口配置/查询接口（LST INTERFACEIPSEC）_80592504.md)<br>命令查看可用接口。 |
| ENABLEFLAG | IPv6使能标志 | 可选必选说明：必选参数<br>参数含义：该参数用于配置接口IPv6使能的标志。<br>数据来源：本端规划<br>取值范围：<br>- FALSE（不使能）<br>- TRUE（使能）<br>默认值：无。<br>配置原则：<br>本参数参与自动化配置，请在下发本MML命令前使用<br>[**DSP OPSASSISTSTATE**](../../../../VNRS功能管理/操作维护/系统调测/开放可编程系统/显示系统助手的当前信息（DSP OPSASSISTSTATE）_00601449.md)<br>命令查询自动化配置维护助手autoscaling_autoconfig.py，确保当前设备是否在自动化配置过程中。如果当前正在自动化配置过程中，不要做本业务的增删改操作，否则最终生效的配置将不可预期。 |
| IFMTU6 | IPv6接口最大传输单元(字节) | 可选必选说明：该参数在"ENABLEFLAG"配置为"TRUE"时为条件可选参数。<br>参数含义：该参数用于配置接口IPv6 MTU值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1280~9600，单位是字节。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IFIPV6ENABLEIPSEC查询当前参数配置值。<br>配置原则：<br>前提条件：该参数在“ENABLEFLAG”配置为“TRUE”时为可选参数。<br>由于实际环境上不同网卡支持的MTU范围不一样，所以配置过大或者过小的MTU值可能会不成功，建议配置的MTU为1500~9000之间的值。<br>本参数参与自动化配置，请在下发本MML命令前使用<br>[**DSP OPSASSISTSTATE**](../../../../VNRS功能管理/操作维护/系统调测/开放可编程系统/显示系统助手的当前信息（DSP OPSASSISTSTATE）_00601449.md)<br>命令查询自动化配置维护助手autoscaling_autoconfig.py，确保当前设备是否在自动化配置过程中。如果当前正在自动化配置过程中，不要做本业务的增删改操作，否则最终生效的配置将不可预期。<br>IPv6使能，缺省值为1500。 |

## 操作的配置对象

- [接口IPv6使能（IFIPV6ENABLEIPSEC）](configobject/UDG/20.15.2/IFIPV6ENABLEIPSEC.md)

## 使用实例

修改接口IPv6使能情况：

```
SET IFIPV6ENABLEIPSEC:IFNAME="LoopBack4",ENABLEFLAG=TRUE,IFMTU6=1500;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置接口IPv6使能（SET-IFIPV6ENABLEIPSEC）_68201005.md`
