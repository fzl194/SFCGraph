---
id: UDG@20.15.2@MMLCommand@ADD IFIPV6CGA
type: MMLCommand
name: ADD IFIPV6CGA（添加IPv6 CGA地址信息）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: IFIPV6CGA
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 262144
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- IPv6 CGA地址配置
status: active
---

# ADD IFIPV6CGA（添加IPv6 CGA地址信息）

## 功能

该命令用于添加IPv6 CGA地址信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为262144。
- 该命令可以在VNRS_VNFC的Ethernet接口，Ethernet子接口，Eth-Trunk接口，Eth-Trunk子接口上配置。
- 接口名称可以通过LST INTERFACE命令获取。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IPv6地址CGA信息的接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| KEYPAIRLABEL | 密钥名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IPv6 CGA密钥信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～35。<br>默认值：无 |
| SECLEVEL | 安全级别 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IPv6 CGA安全级别。high表示最高安全级别，如果配置安全级别为high，则由系统自动生成修正值。配置安全级别为low时，可以手动配置修正值。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- low：安全级别低，支持手动配置地址修正值。<br>- high：安全级别高，自动生成地址修正值。<br>- notConfigured：未配置。<br>默认值：无 |
| MODIFIER | 修正地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SECLEVEL”配置为“low”时为可选参数。<br>参数含义：该参数用于指定IPv6 CGA地址修正值。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IFIPV6CGA]] · IPv6 CGA地址信息（IFIPV6CGA）

## 使用实例

添加接口IPv6 CGA信息：

```
ADD IFIPV6CGA:IFNAME="ethernet64/0/3",KEYPAIRLABEL="aa",SECLEVEL=high;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/添加IPv6-CGA地址信息（ADD-IFIPV6CGA）_00866573.md`
