---
id: UDG@20.15.2@MMLCommand@SET ARPIFLIMIT
type: MMLCommand
name: SET ARPIFLIMIT（配置ARP表项限制）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: ARPIFLIMIT
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ARP管理
- 接口下ARP配置
status: active
---

# SET ARPIFLIMIT（配置ARP表项限制）

## 功能

该命令用于设置接口下ARP动态表项的数量限制。

## 注意事项

- 该命令执行后立即生效。
- 该命令在配置的时候，若已经学习到的表项数量大于命令配置的数量，此时配置命令仍然会生效，但是不会再学习新的用户。
- 参数LIMITNUM的初始值为65536，且配置为65536时查询为空。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| VLANID | LIMITNUM |
| --- | --- |
| 0 | 65536 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于需要设置表项限制的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。以太网接口名称由接口类型和接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| VLANID | VLAN ID值 | 可选必选说明：可选参数<br>参数含义：接口所属的VLAN ID值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4094。<br>默认值：无 |
| LIMITNUM | 限制数量 | 可选必选说明：必选参数<br>参数含义：表项限制值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65536。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ARPIFLIMIT]] · ARP表项限制（ARPIFLIMIT）

## 使用实例

配置主接口Ethernet64/0/5接口最多可以学习到2000个动态ARP表项：

```
SET ARPIFLIMIT:IFNAME="Ethernet64/0/5",LIMITNUM=2000;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-ARPIFLIMIT.md`
