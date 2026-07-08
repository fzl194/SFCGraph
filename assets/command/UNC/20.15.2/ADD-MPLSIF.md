---
id: UNC@20.15.2@MMLCommand@ADD MPLSIF
type: MMLCommand
name: ADD MPLSIF（添加MPLS接口）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MPLSIF
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 65535
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- MPLS基础
- MPLS接口
status: active
---

# ADD MPLSIF（添加MPLS接口）

## 功能

该命令用于添加MPLS接口。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| MTUVALUE | 接口配置的MPLS MTU | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口配置的MPLS MTU。MTU的大小决定了发送端一次能够发送报文的最大字节数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为46～9600。<br>默认值：无<br>配置原则：<br>- 如果不输入该参数，则采用接口的MTU值作为MPLS转发的MTU值。<br>- 如果配置了接口的MPLS MTU值，则与接口的MTU值比较，采用两者中的较小值作为MPLS转发的MTU值。 |

## 操作的配置对象

- [MPLS接口（MPLSIF）](configobject/UNC/20.15.2/MPLSIF.md)

## 使用实例

添加MPLS接口：

```
ADD MPLSIF:IFNAME="Ethernet64/0/3",MTUVALUE=1500;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/添加MPLS接口（ADD-MPLSIF）_50281798.md`
