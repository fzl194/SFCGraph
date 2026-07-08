---
id: UNC@20.15.2@MMLCommand@SET MASTERPCRF
type: MMLCommand
name: SET MASTERPCRF（设置主用PCRF）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: MASTERPCRF
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 100
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCRF Diameter连接
- PCRF组
status: active
---

# SET MASTERPCRF（设置主用PCRF）

## 功能

**适用NF：PGW-C、SMF**

此命令用于设置主用PCRF主机名。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为100。
- 配置的PCRF必须已通过ADD PCRFBINDGRP命令绑定到PCRF组。
- 该命令设定后的数据，需要通过LST PCRFGROUP命令进行查看。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCRFGRPNAME | PCRF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PCRF组的名字，要求在系统内唯一，数据来源为运营商规划。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～128。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| MASTERPCRF | 主用PCRF主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于设置主用PCRF主机名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MASTERPCRF]] · 主用PCRF（MASTERPCRF）

## 使用实例

设置主用PCRF，“PCRFGRPNAME”为“huawei”，“MASTERPCRF”为“test”：

```
SET MASTERPCRF:PCRFGRPNAME="huawei",MASTERPCRF="test";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-MASTERPCRF.md`
