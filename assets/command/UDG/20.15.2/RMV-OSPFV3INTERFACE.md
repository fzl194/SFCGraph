---
id: UDG@20.15.2@MMLCommand@RMV OSPFV3INTERFACE
type: MMLCommand
name: RMV OSPFV3INTERFACE（删除OSPFv3接口配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: OSPFV3INTERFACE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3接口配置
status: active
---

# RMV OSPFV3INTERFACE（删除OSPFv3接口配置）

## 功能

该命令用于在删除一个OSPFv3进程的区域下的接口。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：必选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：本参数参与自动化配置，请在下发本MML命令前使用DSP OPSASSISTSTATE命令查询自动化配置维护助手autoscaling_autoconfig.py，确保其状态为准备好状态或者查询无该脚本来保证当前设备不在自动化配置过程中。如果当前正在自动化配置过程中，不要做本业务的增删改操作，否则最终生效的配置将不可预期。 |
| AREAID | OSPFv3区域号 | 可选必选说明：必选参数<br>参数含义：OSPFv3区域号。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无<br>配置原则：本参数参与自动化配置，请在下发本MML命令前使用DSP OPSASSISTSTATE命令查询自动化配置维护助手autoscaling_autoconfig.py，确保其状态为准备好状态或者查询无该脚本来保证当前设备不在自动化配置过程中。如果当前正在自动化配置过程中，不要做本业务的增删改操作，否则最终生效的配置将不可预期。 |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| INSTANCEID | 实例号 | 可选必选说明：必选参数<br>参数含义：实例号。同一接口下可以绑定多个OSPFv3进程，不同的进程可以使用实例号区分。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无 |

## 操作的配置对象

- [OSPFv3接口配置（OSPFV3INTERFACE）](configobject/UDG/20.15.2/OSPFV3INTERFACE.md)

## 使用实例

接口Ethernet64/0/5下去使能OSPFv3进程1的区域0.0.0.0：

```
RMV OSPFV3INTERFACE: PROCID=1, AREAID="0.0.0.0", IFNAME="Ethernet64/0/5",INSTANCEID=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除OSPFv3接口配置（RMV-OSPFV3INTERFACE）_50121730.md`
