---
id: UNC@20.15.2@MMLCommand@RTR SQOSPOLICYSTC
type: MMLCommand
name: RTR SQOSPOLICYSTC（清除端口流量策略报文统计）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: SQOSPOLICYSTC
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 端口统计
status: active
---

# RTR SQOSPOLICYSTC（清除端口流量策略报文统计）

## 功能

该命令用来清除端口流量策略报文统计。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用来指定接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：与设备接口名称保持一致，下发本MML命令前可使用LST INTERFACE查看设备接口。 |
| DIRECTION | 方向 | 可选必选说明：必选参数<br>参数含义：该参数用来指定应用流策略的方向。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- inbound：入方向。<br>- outbound：出方向。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SQOSPOLICYSTC]] · 查看端口流量策略报文统计（SQOSPOLICYSTC）

## 使用实例

清除Ethernet66/0/2端口流量策略报文统计：

```
RTR SQOSPOLICYSTC:IFNAME="Ethernet66/0/2",DIRECTION=inbound;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RTR-SQOSPOLICYSTC.md`
