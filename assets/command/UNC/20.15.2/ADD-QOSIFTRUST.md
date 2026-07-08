---
id: UNC@20.15.2@MMLCommand@ADD QOSIFTRUST
type: MMLCommand
name: ADD QOSIFTRUST（增加QoS接口信任）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: QOSIFTRUST
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 65536
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 接口信任信息
status: active
---

# ADD QOSIFTRUST（增加QoS接口信任）

## 功能

该命令用来在Ethernet接口、Ethernet子接口或Eth-Trunk接口绑定DS域，根据dscp值或802.1p值进行简单流分类，对IP报文的优先级进行修改。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65536。
- 该命令不支持在Eth-Trunk子接口绑定DS域。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定一个接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：与设备接口名称保持一致，下发本MML命令前可使用LST INTERFACE查看设备接口。 |
| DSNAME | DS域名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DS域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 需要先使用ADD QOSDIFFERSERV命令配置DS域。 |
| FLAG8021P | 8021p标志 | 可选必选说明：可选参数<br>参数含义：该参数用于指定映射的优先级。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- false：不支持以太子接口上根据802.1p的值进行简单流分类。<br>- true：支持以太子接口上根据802.1p的值进行简单流分类。<br>默认值：false |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSIFTRUST]] · QoS接口信任（QOSIFTRUST）

## 使用实例

在以太主接口Ethernet66/0/3绑定DS域ds1：

```
ADD QOSIFTRUST:DSNAME="ds1",IFNAME="Ethernet66/0/3";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-QOSIFTRUST.md`
