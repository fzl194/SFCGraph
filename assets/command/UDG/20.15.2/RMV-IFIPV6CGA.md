---
id: UDG@20.15.2@MMLCommand@RMV IFIPV6CGA
type: MMLCommand
name: RMV IFIPV6CGA（删除IPv6 CGA地址信息）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: IFIPV6CGA
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- IPv6 CGA地址配置
status: active
---

# RMV IFIPV6CGA（删除IPv6 CGA地址信息）

## 功能

该命令用于删除IPv6 CGA地址信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令可以在VNRS_VNFC的Ethernet接口，Ethernet子接口上配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IPv6地址CGA信息的接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| KEYPAIRLABEL | 密钥名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IPv6 CGA密钥信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～35。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IFIPV6CGA]] · IPv6 CGA地址信息（IFIPV6CGA）

## 使用实例

删除接口IPv6 CGA信息：

```
RMV IFIPV6CGA:IFNAME="ethernet64/0/3",KEYPAIRLABEL="aa";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-IFIPV6CGA.md`
