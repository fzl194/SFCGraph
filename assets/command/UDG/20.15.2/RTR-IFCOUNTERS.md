---
id: UDG@20.15.2@MMLCommand@RTR IFCOUNTERS
type: MMLCommand
name: RTR IFCOUNTERS（清除接口统计信息）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: IFCOUNTERS
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- 接口统计信息
status: active
---

# RTR IFCOUNTERS（清除接口统计信息）

## 功能

当需要统计一定时间内某接口的流量信息时，必须在统计开始前清除该接口原有的统计信息，从而使接口重新进行统计。

该命令用于重置逻辑接口及虚拟物理接口的计数。虚拟物理接口是存在于虚拟机中的接口，和真实存在的物理接口有映射关系。逻辑接口是指能够实现数据交换功能但物理上不存在、需要通过配置建立的接口。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RSTTYPE | 清除类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置清除统计计数的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ByName：按接口名清除。<br>- ByType：按接口类型清除。<br>- AllIf：清除所有接口。<br>默认值：无 |
| IFNAME | 接口名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“RSTTYPE”配置为“ByName”时为必选参数。<br>参数含义：该参数用于设置清除统计计数的接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| IFPHYTYPE | 接口类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“RSTTYPE”配置为“ByType”时为必选参数。<br>参数含义：该参数用于显示接口的物理类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Ethernet：以太接口。<br>- Eth_trunk：Eth-Trunk接口。<br>- Tunnel：Tunnel接口。<br>- Loopback：Loopback接口。<br>- Null：Null接口。<br>- Fabric-Tunnel：Fabric-Tunnel接口。<br>- 400GE：400GE接口<br>- 200GE：200GE接口<br>- 100GE：100GE接口。<br>- 25GE：25GE接口。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IFCOUNTERS]] · 接口统计信息（IFCOUNTERS）

## 使用实例

清除接口名为Ethernet64/0/3的接口统计计数：

```
RTR IFCOUNTERS:RSTTYPE=ByName,IFNAME="ethernet64/0/3";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RTR-IFCOUNTERS.md`
