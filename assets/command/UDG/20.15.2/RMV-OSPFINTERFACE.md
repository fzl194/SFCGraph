---
id: UDG@20.15.2@MMLCommand@RMV OSPFINTERFACE
type: MMLCommand
name: RMV OSPFINTERFACE（删除OSPF接口配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: OSPFINTERFACE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF接口配置
status: active
---

# RMV OSPFINTERFACE（删除OSPF接口配置）

## 功能

该命令用于删除一个OSPF进程的区域下的接口。

## 注意事项

- 该命令执行后立即生效。
- 该命令只是把接口下使能OSPF的配置删除，如果OSPF进程下还存在OSPFNETWORK的相关配置，需要同时删除该配置来删除OSPF接口。
- 当RMV OSPFINTERFACE删除接口OSPF使能后，该接口网段的OSPFNETWORK配置自动生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：本参数参与自动化配置，请在下发本MML命令前使用DSP OPSASSISTSTATE命令查询自动化配置维护助手autoscaling_autoconfig.py，确保其状态为准备好状态或者查询无该脚本来保证当前设备不在自动化配置过程中。如果当前正在自动化配置过程中，不要做本业务的增删改操作，否则最终生效的配置将不可预期。 |
| AREAID | 区域标识 | 可选必选说明：必选参数<br>参数含义：OSPF区域号。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无<br>配置原则：本参数参与自动化配置，请在下发本MML命令前使用DSP OPSASSISTSTATE命令查询自动化配置维护助手autoscaling_autoconfig.py，确保其状态为准备好状态或者查询无该脚本来保证当前设备不在自动化配置过程中。如果当前正在自动化配置过程中，不要做本业务的增删改操作，否则最终生效的配置将不可预期。 |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：指定特定的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [OSPF接口配置（OSPFINTERFACE）](configobject/UDG/20.15.2/OSPFINTERFACE.md)

## 使用实例

接口Ethernet64/0/5下去使能OSPF进程1的区域0.0.0.0：

```
RMV OSPFINTERFACE: PROCID=1, AREAID="0.0.0.0", IFNAME="Ethernet64/0/5";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除OSPF接口配置（RMV-OSPFINTERFACE）_50281090.md`
