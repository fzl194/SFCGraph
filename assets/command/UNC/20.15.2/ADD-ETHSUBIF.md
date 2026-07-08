---
id: UNC@20.15.2@MMLCommand@ADD ETHSUBIF
type: MMLCommand
name: ADD ETHSUBIF（增加子接口配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: ETHSUBIF
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 262144
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- VLAN管理
- VLAN子接口
status: active
---

# ADD ETHSUBIF（增加子接口配置）

## 功能

该命令用于配置子接口关联VLAN。

为了实现VLAN间通信，可在接入用户终端的接口上通过创建子接口并关联VLAN实现二层网络接入三层网络，从而实现不同网段、不同VLAN间的通信。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为262144。
- 该命令只允许配置在子接口上，每个子接口只可关联一个VLAN。
- 不同主接口下的子接口可以关联相同的VLAN，但是同一主接口下的不同子接口必须关联不同的VLAN。
- 执行该命令前，必须先创建子接口。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 子接口名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定子接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。以太网接口名称由接口类型和接口编号组成。<br>默认值：无<br>配置原则：该参数必须先由ADD INTERFACE命令定义，才能在此处索引。 |
| SUBIFTYPE | 子接口流封装类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定子接口的流封装类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- VlanType：VLAN类型子接口。<br>默认值：VlanType |
| VLANTYPEVID | VLAN ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定子接口关联的VLAN ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4094。<br>默认值：无 |

## 操作的配置对象

- [子接口配置（ETHSUBIF）](configobject/UNC/20.15.2/ETHSUBIF.md)

## 使用实例

配置子接口Ethernet64/0/3.1关联VLAN 10：

```
ADD ETHSUBIF: IFNAME="Ethernet64/0/3.1", VLANTYPEVID=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加子接口配置（ADD-ETHSUBIF）_49801486.md`
