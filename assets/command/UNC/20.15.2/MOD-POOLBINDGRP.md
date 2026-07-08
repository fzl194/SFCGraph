---
id: UNC@20.15.2@MMLCommand@MOD POOLBINDGRP
type: MMLCommand
name: MOD POOLBINDGRP（修改地址池与地址池组的绑定关系）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: POOLBINDGRP
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

# MOD POOLBINDGRP（修改地址池与地址池组的绑定关系）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于修改指定地址池组中指定地址池的优先级。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLGRPNAME | 地址池组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定已配置的地址池组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRPOOLGRP命令配置生成。 |
| POOLNAME | 地址池名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定已配置的地址池的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。不支持空格及特殊字符“#”、“$”和“&”等，由“-”、“_”、数字、字母和“.”组成，不能以“.”开头，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRPOOL命令配置生成。 |
| PRIORITY | 地址池优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址池优先级。生效范围为地址池组内相同VPN的地址池。优先级数值越小，优先级越高。对于配置优先级相同的地址池，选择地址池的顺序不做要求。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~16。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@POOLBINDGRP]] · 地址池与地址池组的绑定关系（POOLBINDGRP）

## 使用实例

将名为poolgroup1地址池组与名为pool1的地址池绑定关系的地址池优先级调整为15：

```
MOD POOLBINDGRP: POOLGRPNAME="poolgroup1", POOLNAME="pool1", PRIORITY=15;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-POOLBINDGRP.md`
