---
id: UDG@20.15.2@MMLCommand@ADD NDNEIGHBOR
type: MMLCommand
name: ADD NDNEIGHBOR（增加静态ND邻居表项）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: NDNEIGHBOR
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 16384
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- IPv6 ND表项
status: active
---

# ADD NDNEIGHBOR（增加静态ND邻居表项）

## 功能

该命令用于IPv6 ND静态表项的新增。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为16384。
- 接口名称可以通过LST INTERFACE命令获取。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| IPV6ADDRESS | IPv6地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| MACADDRESS | MAC地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MAC地址。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～18。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NDNEIGHBOR]] · 静态ND邻居表项（NDNEIGHBOR）

## 使用实例

新增IPv6 ND静态表项：

```
ADD NDNEIGHBOR:IFNAME="Ethernet65/0/8",IPV6ADDRESS="2001:db8::11",MACADDRESS="00e0-fc01-0001";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加静态ND邻居表项（ADD-NDNEIGHBOR）_00600305.md`
