---
id: UDG@20.15.2@MMLCommand@DEA IDLESESSION
type: MMLCommand
name: DEA IDLESESSION（去激活空闲会话）
nf: UDG
version: 20.15.2
verb: DEA
object_keyword: IDLESESSION
command_category: 动作类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- 空闲会话去激活
status: active
---

# DEA IDLESESSION（去激活空闲会话）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

![](去激活空闲会话（DEA IDLESESSION）_77631308.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，若不指定APNTYPE或CPNODEIDTYPE，将去活所有空闲会话。

该命令用于去激活系统的空闲会话。当会话空闲时长超过了指定的空闲时长阈值，需要手动去激活空闲会话时，使用该命令。可以基于APNTYPE或者CPNODEIDTYPE去激活。

## 注意事项

- 执行该命令去激活空闲会话时，如果指定了APN，需要首先执行命令LCK APN锁定APN。
- 该命令执行后立即生效。
- 不指定APNTYPE和CPNODEIDTYPE时，表示去激活所有空闲会话。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SESSIDLETHD | 空闲时长阈值（分） | 可选必选说明：必选参数<br>参数含义：该参数用于指定空闲时长阈值，会话空闲时长超过了指定阈值的会话将被去激活。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5～12000，单位是分钟。<br>默认值：无<br>配置原则：无 |
| APNTYPE | APN类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示使用的APN类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- REQUESTED：表示使用用户请求的APN。<br>- SERVICE：表示使用用户的真实APN。<br>默认值：无<br>配置原则：<br>- 指定APNTYPE为SERVICE时，表示去激活用户的真实APN为该APN的所有满足时长条件的会话。<br>- 指定APNTYPE为REQUESTED时，表示去激活用户请求的APN为该APN的所有满足时长条件的会话。 |
| APN | APN名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“APNTYPE”配置为“REQUESTED” 或 “SERVICE”时为必选参数。<br>参数含义：该参数用于指定待去激活用户的APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写，不支持空格以及特殊字符：“_”、“#”、“$”、“&”等。<br>默认值：无<br>配置原则：无 |
| CPNODEIDTYPE | Node ID 类型 | 可选必选说明：可选参数<br>参数含义：该参数用来指定Node ID 类型，Node ID用于指定SMF。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IPv4：表示Node ID类型为IPv4地址。<br>- IPv6：表示Node ID类型为IPv6地址。<br>- FQDN：表示Node ID类型为FQDN。<br>默认值：无<br>配置原则：指定CPNODEIDTYPE时，表示去激活该CPNODEIDTYPE下的满足时长条件的会话。 |
| CPNODEIDIPV4 | Node ID中的IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CPNODEIDTYPE”配置为“IPv4”时为必选参数。<br>参数含义：该参数用于指定，在根据Node ID查询CP信息时，Node ID中的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| CPNODEIDIPV6 | Node ID中的IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CPNODEIDTYPE”配置为“IPv6”时为必选参数。<br>参数含义：该参数用于指定，在根据Node ID查询CP信息时，Node ID中的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| CPNODEFQDN | Node ID的FQDN | 可选必选说明：条件必选参数<br>前提条件：该参数在“CPNODEIDTYPE”配置为“FQDN”时为必选参数。<br>参数含义：该参数用于指定，在根据NODE ID查询CP信息时，Node ID中的FQDN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～255。不支持空格，必须是可见ASCII码，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IDLESESSION]] · 空闲会话（IDLESESSION）

## 使用实例

当会话空闲时长超过了指定的空闲时长阈值，需要手动去激活空闲会话时，使用该命令，指定空闲时长阈值为120分钟：

```
DEA IDLESESSION:SESSIDLETHD=120;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/去激活空闲会话（DEA-IDLESESSION）_77631308.md`
