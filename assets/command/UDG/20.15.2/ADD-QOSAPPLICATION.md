---
id: UDG@20.15.2@MMLCommand@ADD QOSAPPLICATION
type: MMLCommand
name: ADD QOSAPPLICATION（增加流策略）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: QOSAPPLICATION
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 131072
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 流量策略
status: active
---

# ADD QOSAPPLICATION（增加流策略）

## 功能

该命令用来在接口应用流量策略；需要对接口进行QoS策略时，可以使用该命令在配置指定的QoS流策略。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为131072。
- 本命令参数参与自动化配置，请在下发本MML命令前使用DSP OPSASSISTSTATE命令查询自动化配置维护助手autoscaling_autoconfig.py，确保当前设备不在自动化配置过程中。如果当前正在自动化配置过程中，不要做本业务的增删改操作，否则最终生效的配置将不可预期。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定应用流量策略的接口，以太主接口/子接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：与设备接口名称保持一致，下发本MML命令前可使用LST INTERFACE查看设备接口。 |
| DIRECTION | 报文方向 | 可选必选说明：必选参数<br>参数含义：该参数用于指定在接口入方向还是出方向应用流量策略。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- inbound：入方向报文。<br>- outbound：出方向报文。<br>默认值：无<br>配置原则：inbound入方向流量策略不支持对非单播协议报文过滤。 outbound出方向流量策略不支持对IPv6报文过滤，对于IPv4报文只支持Permit/Deny动作。 |
| POLICYNAME | 策略名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定应用的流量策略。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：需要先使用ADD MQCPOLICY命令增加流策略。 |
| LAYER | 层信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定应用的流量策略。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- default：此策略应用在IP层。<br>- link_layer：此策略应用在链路层。<br>默认值：default |

## 操作的配置对象

- [流策略（QOSAPPLICATION）](configobject/UDG/20.15.2/QOSAPPLICATION.md)

## 关联任务

- [0-00204](task/UDG/20.15.2/0-00204.md)

## 使用实例

在以太网接口Ethernet66/0/3入方向应用流量策略p1：

```
ADD QOSAPPLICATION:IFNAME="Ethernet66/0/3", DIRECTION=inbound, POLICYNAME="p1",LAYER=link_layer;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加流策略（ADD-QOSAPPLICATION）_50281230.md`
