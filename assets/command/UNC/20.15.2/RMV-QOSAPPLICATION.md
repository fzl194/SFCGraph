---
id: UNC@20.15.2@MMLCommand@RMV QOSAPPLICATION
type: MMLCommand
name: RMV QOSAPPLICATION（删除流策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: QOSAPPLICATION
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 流量策略
status: active
---

# RMV QOSAPPLICATION（删除流策略）

## 功能

该命令用来删除接口上流量策略的应用配置；支持接口：以太主接口/子接口。

## 注意事项

- 该命令执行后立即生效。
- 本命令参数参与自动化配置，请在下发本MML命令前使用DSP OPSASSISTSTATE命令查询自动化配置维护助手autoscaling_autoconfig.py，确保当前设备不在自动化配置过程中。如果当前正在自动化配置过程中，不要做本业务的增删改操作，否则最终生效的配置将不可预期。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定应用流量策略的接口，以太主接口/子接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：与设备接口名称保持一致，下发本MML命令前可使用LST INTERFACE查看设备接口。 |
| DIRECTION | 报文方向 | 可选必选说明：必选参数<br>参数含义：该参数用于指定在接口入方向还是出方向应用流量策略。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- inbound：入方向报文。<br>- outbound：出方向报文。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSAPPLICATION]] · 流策略（QOSAPPLICATION）

## 使用实例

删除在以太网接口Ethernet66/0/3入方向应用流量策略：

```
RMV QOSAPPLICATION:IFNAME="Ethernet66/0/3", DIRECTION=inbound;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-QOSAPPLICATION.md`
