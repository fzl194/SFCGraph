---
id: UDG@20.15.2@MMLCommand@ADD CPNODEID
type: MMLCommand
name: ADD CPNODEID（添加SMF的NodeID）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: CPNODEID
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 64
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- SMF属性
status: active
---

# ADD CPNODEID（添加SMF的NodeID）

## 功能

**适用NF：PGW-U、UPF**

该命令用于添加一个新的SMF实例，指定SMF的NodeID信息，用于系统基于SMF为UE分配IP地址。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为64。
- 不同SMF实例的NODEID不可以相同。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPNAME | SMF名称 | 可选必选说明：必选参数<br>参数含义：SMF的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：无 |
| CPNODEIDTYPE | CP NodeID 类型 | 可选必选说明：可选参数<br>参数含义：NodeID类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：NodeID类型是IPv4。<br>- IPV6：NodeID 类型是IPv6。<br>- FQDN：NodeID 类型是FQDN。<br>默认值：无<br>配置原则：无 |
| IPV4NODEID | IPv4地址类型的Node Id | 可选必选说明：条件可选参数<br>前提条件：该参数在“CPNODEIDTYPE”配置为“IPV4”时为可选参数。<br>参数含义：IPv4类型的SMF Node Id。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6NODEID | IPv6地址类型的Node Id | 可选必选说明：条件可选参数<br>前提条件：该参数在“CPNODEIDTYPE”配置为“IPV6”时为可选参数。<br>参数含义：IPv6类型的SMF Node Id。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| FQDNNODEID | FQDN类型的Node Id | 可选必选说明：条件可选参数<br>前提条件：该参数在“CPNODEIDTYPE”配置为“FQDN”时为可选参数。<br>参数含义：FQDN类型的SMF Node Id。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～255。不区分大小写，支持的字符类型包括：大小写字母、数字、“-”、“.”，大小写不敏感。<br>默认值：无<br>配置原则：无 |
| LOCALEMERNODE | 本地应急接入节点 | 可选必选说明：可选参数<br>参数含义：本地应急接入节点。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：非本地应急接入。<br>- TRUE：本地应急接入。<br>默认值：FALSE<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@CPNODEID]] · SMF的NodeID（CPNODEID）

## 使用实例

创建一个SMF实例，SMF名为smfnode1，IPv4地址为10.0.0.1：

```
ADD CPNODEID: CPNAME="smfnode1", CPNODEIDTYPE=IPV4, IPV4NODEID="10.0.0.1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-CPNODEID.md`
