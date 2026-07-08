---
id: UNC@20.15.2@MMLCommand@RTR UEDNSBINDAPN
type: MMLCommand
name: RTR UEDNSBINDAPN（恢复APN的DNS属性）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: UEDNSBINDAPN
command_category: 动作类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- DN网络DNS_NBNS选择管理
- DNS选择管理
- APN DNS域名策略
status: active
---

# RTR UEDNSBINDAPN（恢复APN的DNS属性）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用来删除指定APN实例的DNS属性和DNS64属性，恢复配置之前的状态。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| DNSSERVERTYPE | DNS服务器类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要删除的IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- DNS_IPV4（IPv4 DNS Server）<br>- DNS_IPV6（IPv6 DNS Server）<br>- DNS_64（DNS64 Server）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [APN的DNS属性（UEDNSBINDAPN）](configobject/UNC/20.15.2/UEDNSBINDAPN.md)

## 使用实例

删除APN实例huawei.com下的DNS地址：

```
RTR UEDNSBINDAPN:APN="huawei.com",DNSSERVERTYPE=DNS_IPV4-1&DNS_IPV6-1&DNS_64-1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/恢复APN的DNS属性（RTR-UEDNSBINDAPN）_09652442.md`
