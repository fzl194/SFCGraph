---
id: UNC@20.15.2@MMLCommand@ADD ADDRPOOLGRP
type: MMLCommand
name: ADD ADDRPOOLGRP（增加地址池组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: ADDRPOOLGRP
command_category: 配置类
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
- UE地址管理
- UE地址池管理
- 地址池组管理
status: active
---

# ADD ADDRPOOLGRP（增加地址池组）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用来增加地址池组。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入40000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLGRPNAME | 地址池组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址池组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。不支持空格及特殊字符“#”、“$”和“&”等，由“-”、“_”、数字、字母和“.”组成，不能以“.”开头，不区分大小写。<br>默认值：无<br>配置原则：无 |
| POOLGRPTYPE | 地址池组类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址池组的类型。<br>数据来源：本端规划<br>取值范围：<br>- “Local（本地）”：地址池组用于SMF、UPF或AAA服务器分配动态地址场景。<br>- “UDM（UDM）”：地址池组用于UDM分配静态地址场景。<br>- “Radius（RADIUS）”：地址池组用于AAA服务器分配静态地址场景。<br>- “DHCP（DHCP）”：地址池组用于外置DHCP服务器分配静态地址场景。<br>默认值：Local<br>配置原则：无 |
| IPV4ALLOCPRIALG | IPv4基于地址池优先级分配地址算法 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv4地址池是否使用基于地址池优先级算法。若开启，则从该地址池组中选取IPv4类型地址时，按优先级算法进行选取。<br>数据来源：本端规划<br>取值范围：<br>- Disable（去使能）<br>- Enable（使能）<br>默认值：Disable<br>配置原则：无 |
| IPV6ALLOCPRIALG | IPv6基于地址池优先级分配地址算法 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv6地址池是否使用基于地址池优先级算法。若开启，则从该地址池组中选取IPv6类型地址时，按优先级算法进行选取。<br>数据来源：本端规划<br>取值范围：<br>- Disable（去使能）<br>- Enable（使能）<br>默认值：Disable<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ADDRPOOLGRP]] · 地址池组（ADDRPOOLGRP）

## 使用实例

增加地址池组, 名称是spoolgrp1，类型是UDM：

```
ADD ADDRPOOLGRP: POOLGRPNAME="spoolgrp1", POOLGRPTYPE=UDM;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-ADDRPOOLGRP.md`
