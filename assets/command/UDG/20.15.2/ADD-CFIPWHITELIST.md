---
id: UDG@20.15.2@MMLCommand@ADD CFIPWHITELIST
type: MMLCommand
name: ADD CFIPWHITELIST（增加内容过滤IP白名单）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: CFIPWHITELIST
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 64
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- 内容过滤IP白名单配置
status: active
---

# ADD CFIPWHITELIST（增加内容过滤IP白名单）

## 功能

**适用NF：PGW-U、UPF**

该命令用于增加IP地址白名单。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为64。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置Ip地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4：IPv4地址类型。<br>- IPV6：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| IPV4ADDR | IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPTYPE”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于指定IPv4地址。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：无 |
| IPV4MASKLEN | IPv4地址掩码长度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPTYPE”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于指定IPv4地址掩码长度。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：无 |
| IPV6ADDR | IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPTYPE”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于设置Ipv6地址。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：无 |
| IPV6MASKLEN | IPv6地址掩码长度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPTYPE”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于指定IPv6地址掩码长度。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPTYPE”配置为“IPV4” 或 “IPV6”时为可选参数。<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1~31.。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@CFIPWHITELIST]] · IP地址白名单列表（CFIPWHITELIST）

## 使用实例

增加内容过滤IP白名单：

```
ADD CFIPWHITELIST: IPTYPE=IPV4, IPV4ADDR="0.0.0.0", IPV4MASKLEN=12;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-CFIPWHITELIST.md`
