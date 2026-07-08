---
id: UDG@20.15.2@MMLCommand@ADD MPACBINDIF
type: MMLCommand
name: ADD MPACBINDIF（增加MPAC接口策略）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: MPACBINDIF
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 256
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- MPAC
- 接口策略配置
status: active
---

# ADD MPACBINDIF（增加MPAC接口策略）

## 功能

该命令用于配置接口MPAC策略。接口名称可以通过LST INTERFACE命令获取。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为256。
- MPAC策略接口绑定指定接口仅支持绑定IPv4、IPv6策略各一条。
- 不支持修改命令，必须先删除原来接口绑定的策略，然后重新增加。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定绑定策略生效的接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| IPVERSION | IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP版本。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4协议族。<br>- IPv6：IPv6协议族。<br>默认值：无 |
| POLICYNAMEV4 | IPv4策略名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv4”时为必选参数。<br>参数含义：该参数用于指定IPv4策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。大小写敏感，英文字母开头，不支持空格。<br>默认值：无 |
| POLICYNAMEV6 | IPv6策略名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv6”时为必选参数。<br>参数含义：该参数用于指定IPv6策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。大小写敏感，英文字母开头，不支持空格。<br>默认值：无 |

## 操作的配置对象

- [MPAC接口策略（MPACBINDIF）](configobject/UDG/20.15.2/MPACBINDIF.md)

## 使用实例

配置MPAC接口策略：

```
ADD MPACBINDIF:IFNAME="Ethernet64/0/3",IPVERSION=IPv4,POLICYNAMEV4="policyV4";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加MPAC接口策略（ADD-MPACBINDIF）_49961922.md`
