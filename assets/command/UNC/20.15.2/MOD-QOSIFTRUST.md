---
id: UNC@20.15.2@MMLCommand@MOD QOSIFTRUST
type: MMLCommand
name: MOD QOSIFTRUST（修改QoS接口信任）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: QOSIFTRUST
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 接口信任信息
status: active
---

# MOD QOSIFTRUST（修改QoS接口信任）

## 功能

该命令用来修改在Ethernet接口或Ethernet子接口绑定的DS域，根据dscp值或802.1p值进行简单流分类，对IP报文的优先级进行修改。

## 注意事项

- 该命令执行后立即生效。
- 该命令不支持修改Eth-Trunk接口和Eth-Trunk子接口绑定的DS域。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定一个接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用LST INTERFACE命令查看可用接口。 |
| DSNAME | DS域名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DS域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |
| FLAG8021P | 8021p标志 | 可选必选说明：可选参数<br>参数含义：该参数用于指定映射的优先级。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- false：不支持以太子接口上根据802.1p的值进行简单流分类。<br>- true：支持以太子接口上根据802.1p的值进行简单流分类。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@QOSIFTRUST]] · QoS接口信任（QOSIFTRUST）

## 使用实例

修改在以太主接口Ethernet66/0/3绑定DS域ds1：

```
MOD QOSIFTRUST:DSNAME="ds1",IFNAME="Ethernet66/0/3";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-QOSIFTRUST.md`
