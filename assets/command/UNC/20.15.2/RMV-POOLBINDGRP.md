---
id: UNC@20.15.2@MMLCommand@RMV POOLBINDGRP
type: MMLCommand
name: RMV POOLBINDGRP（删除地址池与地址池组的绑定关系）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV POOLBINDGRP（删除地址池与地址池组的绑定关系）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除地址池与地址池组的绑定关系，当地址池不再使用时，可使用该命令将其删除。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLGRPNAME | 地址池组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定已配置的地址池组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRPOOLGRP命令配置生成。 |
| POOLNAME | 地址池名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定已配置的地址池的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。不支持空格及特殊字符“#”、“$”和“&”等，由“-”、“_”、数字、字母和“.”组成，不能以“.”开头，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRPOOL命令配置生成。 |

## 操作的配置对象

- [地址池与地址池组的绑定关系（POOLBINDGRP）](configobject/UNC/20.15.2/POOLBINDGRP.md)

## 使用实例

删除地址池与地址池组的绑定关系，地址池组是spoolgrp1，地址池是spool1：

```
RMV POOLBINDGRP: POOLGRPNAME="spoolgrp1", POOLNAME="spool1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除地址池与地址池组的绑定关系（RMV-POOLBINDGRP）_32232826.md`
