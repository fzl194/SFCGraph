---
id: UNC@20.15.2@MMLCommand@RMV APNWHITENODE
type: MMLCommand
name: RMV APNWHITENODE（删除APN设备白名单）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNWHITENODE
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- APN设备白名单
status: active
---

# RMV APNWHITENODE（删除APN设备白名单）

## 功能

**适用NF：PGW-C、SMF**

该命令用于删除APN设备白名单。

## 注意事项

该命令会在新会话建立、发生移动性变更后生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数必须已经通过命令<br>[**ADD APN**](../../APN管理/APN/增加APN配置（ADD APN）_09653747.md)<br>配置。 |
| NODETYPE | 网元类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网元类型。<br>数据来源：本端规划<br>取值范围：<br>- SGW（SGW）<br>- SMF（SMF）<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP地址类型 | 可选必选说明：该参数在"NODETYPE"配置为"SGW"时为条件必选参数。<br>参数含义：该参数用于指定SGW设备的地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPV4）<br>- IPV6（IPV6）<br>默认值：无<br>配置原则：无 |
| NODEIPV4 | IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定SGW设备的IPv4地址段的地址，该配置需要和网络规划保持一致。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| NODEIPV4MASK | IPv4掩码长度 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件可选参数。<br>参数含义：该参数用于指定SGW设备的IPv4地址段的掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~32。<br>默认值：无<br>配置原则：无 |
| NODEIPV6 | IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定SGW设备的Pv6地址段的地址，该配置需要和网络规划保持一致。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| NODEIPV6MASK | IPv6掩码长度 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件可选参数。<br>参数含义：该参数用于指定SGW设备的IPv6地址段的掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |
| NFINSTANCEID | NF实例标识 | 可选必选说明：该参数在"NODETYPE"配置为"SMF"时为条件必选参数。<br>参数含义：该参数用于指定SMF设备的NF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~36。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [APN设备白名单（APNWHITENODE）](configobject/UNC/20.15.2/APNWHITENODE.md)

## 使用实例

当需要删除APN为huawei.com，SGW设备IP地址为"10.0.0.2"的APN设备白名单，可执行如下命令：

```
RMV APNWHITENODE: APN="huawei.com", NODETYPE=SGW, IPVERSION=IPV4, NODEIPV4="10.0.0.2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除APN设备白名单（RMV-APNWHITENODE）_58542676.md`
