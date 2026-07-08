---
id: UDG@20.15.2@MMLCommand@ADD UPDIAMAAABNDG
type: MMLCommand
name: ADD UPDIAMAAABNDG（增加Diameter AAA服务器到Diameter AAA服务器组）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: UPDIAMAAABNDG
command_category: 配置类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
max_records: 20
category_path:
- 用户面服务管理
- Diameter AAA管理
- 服务器配置
- Diameter AAA服务器和Diameter AAA服务器组的绑定关系
status: active
---

# ADD UPDIAMAAABNDG（增加Diameter AAA服务器到Diameter AAA服务器组）

## 功能

**适用NF：UPF**

此命令用于绑定指定的Diameter AAA到Diameter AAA组。当新建立的会话需要到某个Diameter AAA鉴权时，操作员可以执行此命令增加该绑定关系。

## 注意事项

- 该命令执行后对新接入的会话生效。
- 该命令最大记录数为20。对于同一个服务器组，添加记录时，请先添加主用服务器再添加备用服务器；删除记录时，请先删除备用服务器再删除主用服务器。对于同一个服务器组，主用服务器和备用服务器的VPN需要相同。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | Diameter AAA组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter AAA组名。<br>数据来源：本端规划<br>取值范围：不区分大小写，不支持空格。<br>默认值：无<br>配置原则：该参数使用ADD UPDIAMAAAGRP命令配置生成。 |
| SERVERTYPE | 服务器类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务器类型。<br>数据来源：本端规划<br>取值范围：<br>- PARA_3GPP：表示使用遵循3GPP协议的服务器。<br>默认值：无<br>配置原则：无 |
| HOSTNAME | 主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter AAA。<br>数据来源：全网规划<br>取值范围：只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，由软参BIT2670控制是否区分大小写。BIT2670值为0时，不区分大小写；值为1时，区分大小写，但不允许配置多个仅大小写不同的host-name或realm-name。<br>默认值：无<br>配置原则：该参数使用ADD UPDIAMETERAAA命令配置生成。 |
| PRIORSEC | 主备用标记 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务器主备标记。<br>数据来源：本端规划<br>取值范围：<br>- PRIMARY：表示该服务器是主用服务器。<br>- SECONDARY：表示该服务器是备用服务器。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [Diameter AAA服务器组里的Diameter AAA服务器（UPDIAMAAABNDG）](configobject/UDG/20.15.2/UPDIAMAAABNDG.md)

## 使用实例

根据网络规划，绑定名称为“diameteraaa1”的Diameter AAA到名称为“diametergroup”的Diameter AAA组下，指定服务器类型为3GPP，指定主备标记为PRIMARY：

```
ADD UPDIAMAAABNDG: GROUPNAME="diametergroup", SERVERTYPE=PARA_3GPP, HOSTNAME="diameteraaa1", PRIORSEC=PRIMARY;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加Diameter-AAA服务器到Diameter-AAA服务器组（ADD-UPDIAMAAABNDG）_97080179.md`
