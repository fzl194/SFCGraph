---
id: UDG@20.15.2@MMLCommand@RMV IFALLOWEDVLAN
type: MMLCommand
name: RMV IFALLOWEDVLAN（删除主接口允许通过的VLAN）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: IFALLOWEDVLAN
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- VLAN管理
- 主接口允许通过的VLAN
status: active
---

# RMV IFALLOWEDVLAN（删除主接口允许通过的VLAN）

## 功能

该命令用于删除主接口允许通过的VLAN。

## 注意事项

- 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划。<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无。<br>配置原则：请使用<br>[LST INTERFACE](../../接口管理/接口配置/查询接口（LST INTERFACE）_49801850.md)<br>命令查看可用接口。 |
| VLANBEGIN | VLAN最小值 | 可选必选说明：必选参数。<br>参数含义：该参数用于设置允许通过的VLAN范围最小值。<br>数据来源：本端规划。<br>取值范围：2~4094，VLANBEGIN <= VLANEND。<br>默认值：无。<br>配置原则：无。 |
| VLANEND | VLAN最大值 | 可选必选说明：必选参数。<br>参数含义：该参数用于设置允许通过的VLAN范围最大值。<br>数据来源：本端规划。<br>取值范围：2~4094，VLANEND >= VLANBEGIN。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [主接口允许通过的VLAN（IFALLOWEDVLAN）](configobject/UDG/20.15.2/IFALLOWEDVLAN.md)

## 使用实例

删除主接口Ethernet64/0/4允许通过的VLAN范围，VLAN最小值为20，VLAN最大值为25：

```
RMV IFALLOWEDVLAN: IFNAME="Ethernet64/0/4",  VLANBEGIN=20, VLANEND=25;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除主接口允许通过的VLAN（RMV-IFALLOWEDVLAN）_79264164.md`
