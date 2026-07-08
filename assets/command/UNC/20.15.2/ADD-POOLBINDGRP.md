---
id: UNC@20.15.2@MMLCommand@ADD POOLBINDGRP
type: MMLCommand
name: ADD POOLBINDGRP（增加地址池和地址池组的绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: POOLBINDGRP
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

# ADD POOLBINDGRP（增加地址池和地址池组的绑定关系）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于增加地址池和地址池组的绑定关系。

## 注意事项

- 该命令执行后立即生效。

- 同一地址池组下的IP地址段不能交叉重叠。
- 如果地址池组类型为UDM、Radius或DHCP（通过LST ADDRPOOLGRP查询），一个地址池只能绑定一个地址池组。
- 如果地址池组类型为Local（通过LST ADDRPOOLGRP查询），一个地址池可以绑定多个地址池组。
- 如果地址池组的映射规则中有APN，则增加的地址池的VPN（通过LST ADDRPOOL查询）必须与APN对应的VPN（通过LST APN查询）相同。
- 每个地址池组下，对于每个VPN实例（包含不配置VPN实例的场景），最多能绑定16个相同VPN实例的IPv4地址池和16个相同VPN实例的IPv6地址池，一个地址池可以被多个地址池组绑定。

- 最多可输入40000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLGRPNAME | 地址池组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定已配置的地址池组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRPOOLGRP命令配置生成。 |
| POOLNAME | 地址池名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定已配置的地址池的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。不支持空格及特殊字符“#”、“$”和“&”等，由“-”、“_”、数字、字母和“.”组成，不能以“.”开头，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRPOOL命令配置生成。 |
| PRIORITY | 地址池优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址池优先级。生效范围为地址池组内相同VPN的地址池。优先级数值越小，优先级越高。对于配置优先级相同的地址池，选择地址池的顺序不做要求。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~16。<br>默认值：16<br>配置原则：无 |

## 操作的配置对象

- [地址池与地址池组的绑定关系（POOLBINDGRP）](configobject/UNC/20.15.2/POOLBINDGRP.md)

## 使用实例

增加地址池和地址池组的绑定关系，地址池组是spoolgrp1，地址池是pool_1，优先级为15：

```
ADD POOLBINDGRP: POOLGRPNAME="spoolgrp1", POOLNAME="pool_1", PRIORITY=15;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加地址池和地址池组的绑定关系（ADD-POOLBINDGRP）_32232813.md`
