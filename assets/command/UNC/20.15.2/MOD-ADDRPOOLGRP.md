---
id: UNC@20.15.2@MMLCommand@MOD ADDRPOOLGRP
type: MMLCommand
name: MOD ADDRPOOLGRP（修改地址池组）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: ADDRPOOLGRP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址池组管理
status: active
---

# MOD ADDRPOOLGRP（修改地址池组）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于修改指定地址池组的信息。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLGRPNAME | 地址池组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址池组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。不支持空格及特殊字符“#”、“$”和“&”等，由“-”、“_”、数字、字母和“.”组成，不能以“.”开头，不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPV4ALLOCPRIALG | IPv4基于地址池优先级分配地址算法 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv4地址池是否使用基于地址池优先级算法。若开启，则从该地址池组中选取IPv4类型地址时，按优先级算法进行选取。<br>数据来源：本端规划<br>取值范围：<br>- Disable（去使能）<br>- Enable（使能）<br>默认值：无<br>配置原则：无 |
| IPV6ALLOCPRIALG | IPv6基于地址池优先级分配地址算法 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv6地址池是否使用基于地址池优先级算法。若开启，则从该地址池组中选取IPv6类型地址时，按优先级算法进行选取。<br>数据来源：本端规划<br>取值范围：<br>- Disable（去使能）<br>- Enable（使能）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ADDRPOOLGRP]] · 地址池组（ADDRPOOLGRP）

## 使用实例

修改地址池组名为poolgroup1的地址池组，使其IPv6地址池使用基于地址池优先级算法：

```
MOD ADDRPOOLGRP: POOLGRPNAME="poolgroup1", IPV6ALLOCPRIALG=Enable;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改地址池组（MOD-ADDRPOOLGRP）_64343894.md`
