---
id: UDG@20.15.2@MMLCommand@ADD EPRPSTA
type: MMLCommand
name: ADD EPRPSTA（添加EPRPSTA对象）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: EPRPSTA
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
effect_mode: 立即生效
is_dangerous: false
max_records: 4096
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- EPRPSTA性能统计对象
status: active
---

# ADD EPRPSTA（添加EPRPSTA对象）

## 功能

**适用NF：SGW-U、PGW-U**

该命令用于添加一个新的EpRpSta对象，用于系统基于EpRpSta的性能统计。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为4096。
- 创建偶联时会自动生成NODEIDTYPE为IP类型的配置，偶联删除时会删掉自动生成的NODEIDTYPE为IP类型配置。FQDN类型的配置不会触发核查和删除，不建议手工配置额外FQDN类型的配置。
- 如果手动配置的IP和已有的配置的IP相同，则性能指标只会统计到一条路径上。建议不要添加IP相同的配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EPRPSTANAME | 对象名称 | 可选必选说明：必选参数<br>参数含义：对象名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| INTERFACETYPE | 接口类型 | 可选必选说明：必选参数<br>参数含义：接口类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SXA：接口类型为Sxa。<br>- SXB：接口类型为Sxb。<br>- SXBGSN：接口类型为Sxb，且用户角色为GGSN。<br>默认值：无<br>配置原则：无 |
| NODEIDTYPE | CP NodeID 类型 | 可选必选说明：必选参数<br>参数含义：NodeID类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：NodeID类型是IPv4。<br>- IPV6：NodeID 类型是IPv6。<br>- FQDN：NodeID 类型是FQDN。<br>默认值：无<br>配置原则：无 |
| IPV4NODEID | IPv4地址类型的Node Id | 可选必选说明：条件必选参数<br>前提条件：该参数在“NODEIDTYPE”配置为“IPV4”时为必选参数。<br>参数含义：IPv4类型的SMF Node Id。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6NODEID | IPv6地址类型的Node Id | 可选必选说明：条件必选参数<br>前提条件：该参数在“NODEIDTYPE”配置为“IPV6”时为必选参数。<br>参数含义：IPv6类型的SMF Node Id。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| FQDNNODEID | FQDN类型的Node Id | 可选必选说明：条件必选参数<br>前提条件：该参数在“NODEIDTYPE”配置为“FQDN”时为必选参数。<br>参数含义：FQDN类型的SMF Node Id。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～255。不区分大小写，支持的字符类型包括：大小写字母、数字、“-”、“.”，大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/EPRPSTA]] · EPRPSTA对象（EPRPSTA）

## 使用实例

创建一个EpRpSta对象，EpRpSta名为huawei，FQDN为new：

```
ADD EPRPSTA: EPRPSTANAME="huawei", INTERFACETYPE=SXA, NODEIDTYPE=FQDN, FQDNNODEID="new";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-EPRPSTA.md`
